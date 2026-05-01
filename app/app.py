import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import xlsxwriter
from io import BytesIO
from datetime import datetime

from src.predict import predict_risk, prepare_input
from src.explain import get_shap_values, get_feature_importance

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(layout="wide", page_title="FinRisk AI")

# ---------------- HIDE MENU + FOOTER ---------------- #
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- DARK UI ---------------- #
st.markdown("""
<style>
.stApp { background: #0B1220; color: #E5E7EB; }
[data-testid="stSidebar"] { background: #0F172A; }
.kpi { background: linear-gradient(135deg,#1E3A8A,#2563EB); padding: 15px; border-radius: 10px; text-align:center; }
.section { background:#111827;padding:15px;border-radius:12px;border:1px solid #1F2937;margin-bottom:10px; }
.stButton>button { background:#2563EB;color:white;border-radius:10px;border:none; }
</style>
""", unsafe_allow_html=True)

# ---------------- NAVBAR ---------------- #
col1, col2, col3, col4, col5 = st.columns([2,1,1,1,1])

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

def nav(p):
    st.session_state.page = p

with col1:
    st.markdown("### FinRisk AI")

with col2:
    if st.button("Dashboard"):
        nav("Dashboard")
with col3:
    if st.button("Risk Engine"):
        nav("Risk")
with col4:
    if st.button("Simulator"):
        nav("Simulator")
with col5:
    if st.button("Data Guide"):
        nav("Guide")

page = st.session_state.page

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("Applicant Details")

age = st.sidebar.number_input('Age ℹ',18,100,28,help="Applicant age")
income = st.sidebar.number_input('Income ℹ',0,10000000,1200000,help="Annual income")
loan_amount = st.sidebar.number_input('Loan Amount ℹ',0,10000000,2560000,help="Loan amount")
loan_tenure = st.sidebar.number_input('Loan Tenure ℹ',1,120,36,help="Months")
dpd = st.sidebar.number_input('Avg DPD ℹ',0,100,20)
delinq = st.sidebar.number_input('Delinquency % ℹ',0,100,30)
util = st.sidebar.number_input('Utilization % ℹ',0,100,30)
accounts = st.sidebar.number_input('Accounts ℹ',1,10,2)

residence = st.sidebar.selectbox('Residence ℹ',['Owned','Rented','Mortgage'])
purpose = st.sidebar.selectbox('Purpose ℹ',['Education','Home','Auto','Personal'])
loan_type = st.sidebar.selectbox('Loan Type ℹ',['Unsecured','Secured'])

# =====================================================
# 🔥 NEW ADDITIONS (SAFE BLOCK)
# =====================================================

risk_flags = []

if util > 70:
    risk_flags.append("High Utilization ⚠")
if delinq > 40:
    risk_flags.append("High Delinquency ⚠")
if dpd > 30:
    risk_flags.append("Late Payments ⚠")
if loan_amount > income * 3:
    risk_flags.append("Loan too high ⚠")
if accounts <= 1:
    risk_flags.append("Low credit history ⚠")

if risk_flags:
    for f in risk_flags:
        st.sidebar.warning(f)
else:
    st.sidebar.success("Profile stable")

def color_metric(val, low, high):
    return "🟢" if val < low else "🟡" if val < high else "🔴"

st.sidebar.markdown(f"Utilization: {color_metric(util,40,70)}")
st.sidebar.markdown(f"Delinquency: {color_metric(delinq,20,40)}")
st.sidebar.markdown(f"DPD: {color_metric(dpd,15,30)}")

st.sidebar.markdown("### EMI Calculator")

interest_rate = st.sidebar.slider("Interest Rate (%)",5.0,20.0,10.0)
r = interest_rate / 12 / 100

emi = (loan_amount*r*(1+r)**loan_tenure)/((1+r)**loan_tenure-1) if r>0 else loan_amount/loan_tenure
st.sidebar.metric("EMI",f"₹ {int(emi):,}")

monthly_income = income/12 if income>0 else 1
ratio = emi/monthly_income

if ratio>0.5:
    st.sidebar.error("High EMI burden")
elif ratio>0.3:
    st.sidebar.warning("Moderate EMI")
else:
    st.sidebar.success("EMI manageable")

score_health = 100
if util>70: score_health-=20
if delinq>40: score_health-=20
if dpd>30: score_health-=15
if ratio>0.5: score_health-=25

st.sidebar.metric("Health Score",f"{score_health}/100")

# ---------------- CHART THEME ---------------- #
def apply_dark_chart(fig):
    fig.update_layout(
        paper_bgcolor="#111827",
        plot_bgcolor="#111827",
        font=dict(color="#E5E7EB"),
        margin=dict(l=20,r=20,t=30,b=20)
    )
    return fig


# =====================================================
# DASHBOARD
# =====================================================
if page == "Dashboard":

    st.markdown("## Overview")

    c1,c2,c3 = st.columns(3)

    c1.markdown("<div class='kpi'><h4>Applications</h4><h2>1248</h2></div>",unsafe_allow_html=True)
    c2.markdown("<div class='kpi'><h4>Approval Rate</h4><h2>68%</h2></div>",unsafe_allow_html=True)
    c3.markdown("<div class='kpi'><h4>Defaults</h4><h2>2.8%</h2></div>",unsafe_allow_html=True)

    df = pd.DataFrame({
        "Month":["Jan","Feb","Mar","Apr","May"],
        "Approvals":[50,60,70,65,80],
        "Defaults":[5,10,8,12,9]
    })

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Month"], y=df["Approvals"], mode='lines+markers', line=dict(color="#22C55E")))
    fig.add_trace(go.Scatter(x=df["Month"], y=df["Defaults"], mode='lines+markers', line=dict(color="#EF4444")))

    st.plotly_chart(apply_dark_chart(fig), use_container_width=True)

# =====================================================
# RISK ENGINE
# =====================================================
if page == "Risk":

    st.markdown("## Risk Analysis")

    if st.button("Analyze Applicant"):

        data = {
            "age":age,"income":income,"loan_amount":loan_amount,
            "loan_tenure_months":loan_tenure,
            "avg_dpd_per_delinquency":dpd,
            "delinquency_ratio":delinq,
            "credit_utilization_ratio":util,
            "number_of_open_accounts":accounts,
            "residence_type":residence,
            "loan_purpose":purpose,
            "loan_type":loan_type
        }

        with st.spinner("Analyzing risk..."):
            prob,score,rating = predict_risk(data)

        f1,f2,f3 = st.columns(3)
        f1.selectbox("Purpose Filter",["All","Education","Home","Auto","Personal"])
        f2.selectbox("Residence Filter",["All","Owned","Rented","Mortgage"])
        f3.selectbox("Risk Band",["Low","Medium","High"])

        df_input = prepare_input(data)
        shap_vals = get_shap_values(df_input)
        imp = get_feature_importance(shap_vals,df_input.columns)

        tabs = st.tabs(["Overview","Risk Analysis","Explainability","Actions"])

        with tabs[0]:
            c1,c2,c3,c4 = st.columns(4)
            lti = loan_amount/income if income else 0
            c1.metric("Risk",f"{prob:.2%}")
            c2.metric("Score",score)
            c3.metric("Category",rating)
            c4.metric("LTI",f"{lti:.2f}")

            fig = go.Figure(go.Indicator(mode="gauge+number",value=prob*100))
            st.plotly_chart(apply_dark_chart(fig),use_container_width=True)

        with tabs[1]:
            left,right = st.columns([2,1])

            with left:
                fig = px.bar(imp.head(10),x="importance",y="feature",
                             orientation="h",color="importance",
                             color_continuous_scale="teal")
                st.plotly_chart(apply_dark_chart(fig),use_container_width=True)

            with right:
                decision = "APPROVE" if prob<0.4 else "REVIEW" if prob<0.7 else "REJECT"
                st.metric("Decision",decision)

        with tabs[2]:
            feature = st.selectbox("Select Feature",imp["feature"])
            val = imp[imp["feature"]==feature]["importance"].values[0]

            st.metric("Impact",round(val,3))

            df_drill = pd.DataFrame({
                "Scenario":["Low","Medium","High"],
                "Impact":[val*0.5,val,val*1.5]
            })

            fig = px.line(df_drill,x="Scenario",y="Impact",markers=True,
                          color_discrete_sequence=["#22C55E"])
            st.plotly_chart(apply_dark_chart(fig),use_container_width=True)

        with tabs[3]:
            if prob<0.4:
                st.success("Approve Loan")
            elif prob<0.7:
                st.warning("Manual Review Required")
            else:
                st.error("Reject Application")

        excel = BytesIO()
        wb = xlsxwriter.Workbook(excel, {'in_memory': True})
        ws = wb.add_worksheet("Summary")

        ws.write("A1","FINRISK CREDIT REPORT")
        ws.write("A3","Probability"); ws.write("B3",prob)
        ws.write("A4","Score"); ws.write("B4",score)
        ws.write("A5","Rating"); ws.write("B5",rating)

        wb.close()
        excel.seek(0)

        st.download_button("Download Report",excel,"finrisk_report.xlsx")

# =====================================================
# SIMULATOR
# =====================================================
if page == "Simulator":

    st.markdown("## Scenario Simulator")

    sim_income = st.slider("Income",100000,5000000,income)
    sim_loan = st.slider("Loan",100000,5000000,loan_amount)

    data_sim = {
        "age":age,"income":sim_income,"loan_amount":sim_loan,
        "loan_tenure_months":loan_tenure,
        "avg_dpd_per_delinquency":dpd,
        "delinquency_ratio":delinq,
        "credit_utilization_ratio":util,
        "number_of_open_accounts":accounts,
        "residence_type":residence,
        "loan_purpose":purpose,
        "loan_type":loan_type
    }

    prob_sim,_,_ = predict_risk(data_sim)

    st.metric("Simulated Risk",f"{prob_sim:.2%}")

    df_sim = pd.DataFrame({
        "Type":["Current","Simulated"],
        "Risk":[0.5,prob_sim]
    })

    fig = px.bar(df_sim,x="Type",y="Risk",
                 color="Type",
                 color_discrete_sequence=["#22C55E","#EF4444"])

    st.plotly_chart(apply_dark_chart(fig), use_container_width=True)

# =====================================================
# DATA GUIDE
# =====================================================
if page == "Guide":

    st.markdown("## Input Data Guide")

    st.markdown("This section helps non-financial users understand each input.")

    with st.expander("Age"):
        st.write("Age affects financial stability and credit history.")

    with st.expander("Income"):
        st.write("Higher income means better repayment ability.")

    with st.expander("Loan Amount"):
        st.write("Higher loans increase financial burden.")

    with st.expander("Loan Tenure"):
        st.write("Long tenure reduces EMI but increases total risk duration.")

    with st.expander("Avg DPD"):
        st.write("Days past due indicates payment delays.")

    with st.expander("Delinquency %"):
        st.write("Percentage of missed payments.")

    with st.expander("Utilization %"):
        st.write("How much credit is being used.")

    with st.expander("Accounts"):
        st.write("Number of active credit accounts.")

    with st.expander("Residence"):
        st.write("Owned homes show stability.")

    with st.expander("Purpose"):
        st.write("Loan purpose impacts risk.")

    with st.expander("Loan Type"):
        st.write("Secured loans are safer than unsecured.")