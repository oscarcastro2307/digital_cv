from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Oscar Castro 3CFO.pdf"
profile_pic = current_dir / "assets" / "OC_Photo_F.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Oscar Castro"
PAGE_ICON = ":wave:"
NAME = "Oscar Castro"
DESCRIPTION = """
Senior Finance Executive, provides value and consulting to organizations
through financial and strategic deep dive data-driven analytics for decision-making.
"""
EMAIL = "oscarcastro0723@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/oscarcastromba",
    "Oscar Castro Video": "https://github.com",
}
PROJECTS = {
    "🏆 Finance Newsletters - Constant communication throgout finance department and organization": "https://youtu.be/Sb0A9i6d320",
    "🏆 App for Reporting Intelligence - Innovative app for reporting, forecasting, budget and results (inlcudes podcast)": "https://youtu.be/3egaMfE9388",
    "🏆 Board Binder - Sample of presentation of results or strategy to Board Members": "https://youtu.be/LzCfNanQ_9c",
    "🏆 Financial Overview - Automated country overview": "https://pythonandvba.com/mytoolbelt/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ +20 Years finance expereince, Oversees company accounting and financial practices to count with useful accurate financial information for management
- ✔️ Direct the financial strategy – control budget, forecast, capital budget, policies, planning, and drive corrective actions
- ✔️ Supervise investment and manage cash to maximize returns, create capital and borrow money when needed.
- ✔️ Analyze and counsel on strategy, trends, add value across organizations, and partner with CEO, Board & business leaders.
- ✔️ Actively support business partners and contribute with innovation, growth strategies and decision support
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, VBA, C+
- 📊 Data Visulization: PowerBi, MS Excel, Tableau, Microstrategy
- 📚 Modeling: Forecasting and Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, Periscope, Access, MySQL
- 📊 ERP: Essbase, Oracle, TM1, Anaplan, SAP, Netsuite, Quickbooks
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Head of Finance - FP&A | Upbound group**")
st.write("06/2021 - Present")
st.write(
    """
- ► Created, and led the annual operating plan process, partnered with LOB’s functional leaders to align strategies to
company’s goals, provided data-focused deep dive analysis, trends modeling & counseled on business growth decisions.
- ► Built dashboards and scorecards to present monthly, quarterly and annual financials (income statement, cash flow,
balance sheet), strategy progress (KPI’s, segment metrics) to Board of Directors, CEO, Executive and functional leaders.
Supported IR, prepared guidance model for 10Q earnings and presented company insights, roadshows for investors.
- ► Assisted CEO, CFO and Executives in formulating company future direction and double digit growth strategies, through
building and modeling the Long-Range Plan, supported organic growth of 4% - 8% with diligent control of sales market
share and cost. Managed integration of 3 acquisitions, negotiated deal, due diligence as well as monitored ROI.
- ► Used PowerBI and SQL to redeﬁne and track KPIs surrounding operation, marketing and technology initiatives, and supplied recommendations to boost revenues, margins and mitigate risk
- ► Hired, trained and developed a team of 12 high performing finance members, promoted 4 Managers and 2 Directors
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Global Head of FP&A | DZS (technology)**")
st.write("01/2020 - 06/2021")
st.write(
    """
- ► Partnered with all functional and business leaders, led company rolling forecast, annual plan, 3-year target model and
weekly-monthly financial performance, capital investment, reviewed progress and opportunities to mitigate gaps.
- ► Developed, and managed a product profitability yield analysis “PPYA” model to drive business decisions, projects,
tracked performance (scorecards), revenues opportunities, economic trends and led variance analysis.
- ► Managed the day-to-day activity to support sales, operating activities and FTE’s for all countries, regions and corporate
functions. Consolidated process, and reduced expenses by 12%, identified waste and transformed it to efficiencies.
- ► Ensured compliance and coordination of regulatory requirements as (US GAAP - FASB, Labor Unions, Attorneys, etc.)
- ► Coordinated, led HR operations, payroll, recruiting, organizational structure. Managed finance personnel of 12 FTE.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**CFO North America | Solera Holdings**")
st.write("04/2015 - 01/2018")
st.write(
    """
- ► Devised KPIs using SQL across company website in collaboration with cross-functional teams to achieve a 120% jump in organic traﬃc
- ► Analyzed, documented, and reported user survey results to improve customer communication processes by 18%
- ► Collaborated with analyst team to oversee end-to-end process surrounding customers' return data
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")