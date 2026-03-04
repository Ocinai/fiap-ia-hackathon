import streamlit as st
from pathlib import Path
from src.diagram_parser.parser import DiagramParser
from src.stride_report.report import STRIDEReportGenerator
from src.ai_analysis.analyzer import AIAnalyzer
import tempfile

# ----- Page config -----
st.set_page_config(
    page_title="STRIDE Threat Model",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ----- Custom CSS -----
st.markdown("""
<style>
    /* Header */
    .main-header {
        font-size: 1.85rem;
        font-weight: 700;
        color: #1e3a5f;
        margin-bottom: 0.25rem;
        letter-spacing: -0.02em;
    }
    .main-subtitle {
        color: #5a6c7d;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    /* Upload area emphasis */
    [data-testid="stFileUploader"] {
        background: linear-gradient(135deg, #f8fafc 0%, #f1f5f9 100%);
        border: 2px dashed #94a3b8;
        border-radius: 12px;
        padding: 1.5rem;
    }
    [data-testid="stFileUploader"]:hover {
        border-color: #3b82f6;
        background: linear-gradient(135deg, #eff6ff 0%, #dbeafe 100%);
    }
    /* Cards */
    .result-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1.25rem;
        margin: 0.5rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .stride-badge {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 6px;
        font-size: 0.75rem;
        font-weight: 600;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
    }
    .stride-s { background: #dbeafe; color: #1e40af; }
    .stride-t { background: #fce7f3; color: #9d174d; }
    .stride-r { background: #fef3c7; color: #92400e; }
    .stride-i { background: #d1fae5; color: #065f46; }
    .stride-d { background: #e0e7ff; color: #3730a3; }
    .stride-e { background: #f3e8ff; color: #5b21b6; }
</style>
""", unsafe_allow_html=True)

# ----- Header -----
st.markdown('<p class="main-header">🛡️ STRIDE Threat Modeling</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="main-subtitle">Upload an architecture diagram to identify components and generate a threat report.</p>',
    unsafe_allow_html=True,
)

# ----- Image upload -----
uploaded = st.file_uploader(
    "Drop your architecture diagram here or click to browse",
    type=["png", "jpg", "jpeg", "webp"],
    help="Supported: PNG, JPG, JPEG, WEBP",
)

if uploaded is not None:
    col_img, col_info = st.columns([1, 1])
    with col_img:
        st.image(uploaded, use_container_width=True, caption="Uploaded diagram")
    with col_info:
        st.success("Image received")
        st.caption(f"Filename: **{uploaded.name}** · Size: {uploaded.size / 1024:.1f} KB")
        st.markdown('</br>', unsafe_allow_html=True)
    
    st.divider()

    with st.spinner("Analysing diagram and generating report..."):
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded.getvalue())
            tmp_path = Path(tmp.name)
        
        try:
            # AI-Powered Analysis
            ai_analyzer = AIAnalyzer()
            ai_report = ai_analyzer.analyze_diagram(tmp_path)

            # Traditional Analysis
            parser = DiagramParser()
            components = parser.parse(tmp_path)
            
            report_generator = STRIDEReportGenerator()
            report = report_generator.generate(components, ai_threats=ai_report)
            
            st.markdown(report, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"An error occurred: {e}")
        finally:
            tmp_path.unlink()

else:
    st.info("👆 Upload or drop an architecture diagram image to start.")
