import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="KEAM Score Card Calculator",
    layout="wide"
)

st.title("🎯 KEAM Score Card Calculator")
st.markdown("Calculate your Plus Two score and Index Mark based on KEAM normalization formula")

# -------------------------------------------------
# Maximum Marks Database
# -------------------------------------------------

MAX_MARKS_DATA = pd.DataFrame({
    'BOARD': ['CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB',
              'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB', 'CB',
              'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS',
              'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS', 'HS',
              'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS', 'IS',
              'IS', 'IS', 'IS'],
    'YEAR': [1996, 2000, 2001, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017,
             2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026,
             1992, 1993, 1994, 2000, 2001, 2002, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014,
             2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026,
             1993, 2005, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023,
             2024, 2025, 2026],
    'CHEMAXMARK': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                   100, 100, 100, 100, 100, 100, 100, 100, 100,
                   150, 150, 150, 150, 150, 150, 100, 100, 100, 100, 100, 100, 120, 120, 120, 120, 120, 120, 120,
                   120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                   100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    'MATMAXMARK': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                   100, 100, 100, 100, 100, 100, 100, 100, 100,
                   150, 150, 150, 150, 150, 150, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                   100, 100, 100, 100, 120, 120, 120, 120, 120, 120,
                   100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100],
    'PHYMAXMARK': [100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
                   100, 100, 100, 100, 100, 100, 100, 100, 100,
                   150, 150, 150, 150, 150, 150, 100, 100, 100, 100, 100, 100, 120, 120, 120, 120, 120, 120, 120,
                   120, 120, 120, 120, 120, 120, 120, 120, 120, 120,
                   100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100]
})

# -------------------------------------------------
# Input Section
# -------------------------------------------------

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📝 Enter Your Details")

    # Board Selection
    board = st.selectbox(
        "Select Board",
        options=["HS", "CB", "IS"],
        format_func=lambda x: {"HS": "HSE", "CB": "CBSE", "IS": "ICSE"}.get(x, x),
        help="Select your qualifying examination board"
    )

    # Year of Passing - Dynamic dropdown based on available years for selected board
    available_years = sorted(MAX_MARKS_DATA[MAX_MARKS_DATA['BOARD'] == board]['YEAR'].unique())

    year_pass = st.selectbox(
        "Year of Passing",
        options=available_years,
        index=len(available_years) - 1 if available_years else 0,
        help="Select your year of passing"
    )

    # Get maximum marks for selected board and year
    max_marks_row = MAX_MARKS_DATA[(MAX_MARKS_DATA['BOARD'] == board) & (MAX_MARKS_DATA['YEAR'] == year_pass)]

    if not max_marks_row.empty:
        chem_max = float(max_marks_row['CHEMAXMARK'].iloc[0])
        math_max = float(max_marks_row['MATMAXMARK'].iloc[0])
        phy_max = float(max_marks_row['PHYMAXMARK'].iloc[0])
    else:
        st.error(f"No maximum marks data found for {board} - {year_pass}")
        st.stop()

    # Display maximum marks for information
    st.info(f"📊 **Maximum Marks for {board} ({year_pass}):**\nMath: {math_max:.0f} | Physics: {phy_max:.0f} | Chemistry: {chem_max:.0f}")

    # Subject Marks
    st.subheader("📊 Subject Marks")

    maths_mark = st.number_input(
        "Mathematics Mark",
        min_value=0.0,
        max_value=float(math_max),
        value=float(math_max * 0.5),
        step=0.5,
        help=f"Enter your Mathematics mark (maximum: {math_max:.0f})"
    )

    physics_mark = st.number_input(
        "Physics Mark",
        min_value=0.0,
        max_value=float(phy_max),
        value=float(phy_max * 0.5),
        step=0.5,
        help=f"Enter your Physics mark (maximum: {phy_max:.0f})"
    )

    chemistry_mark = st.number_input(
        "Chemistry Mark",
        min_value=0.0,
        max_value=float(chem_max),
        value=float(chem_max * 0.5),
        step=0.5,
        help=f"Enter your Chemistry mark (maximum: {chem_max:.0f})"
    )

    # Enter normalized score
    st.subheader("🎓 Entrance Score")

    norm_score = st.number_input(
        "KEAM Normalized Score",
        min_value=0.0,
        max_value=300.0,
        value=150.0,
        step=0.5,
        help="Your normalized entrance score (out of 300)"
    )

with col2:
    st.subheader("📋 Maximum Marks Reference")

    # Show the complete maximum marks table for reference
    with st.expander("📊 View Maximum Marks Database", expanded=False):
        # Show filtered data for selected board
        board_data = MAX_MARKS_DATA[MAX_MARKS_DATA['BOARD'] == board].sort_values('YEAR')

        st.dataframe(
            board_data,
            use_container_width=True,
            hide_index=True,
            column_config={
                "BOARD": st.column_config.TextColumn("Board"),
                "YEAR": st.column_config.NumberColumn("Year", format="%d"),
                "CHEMAXMARK": st.column_config.NumberColumn("Chem Max", format="%.0f"),
                "MATMAXMARK": st.column_config.NumberColumn("Math Max", format="%.0f"),
                "PHYMAXMARK": st.column_config.NumberColumn("Phy Max", format="%.0f")
            }
        )

        st.caption(f"Showing maximum marks for {board} board")

# -------------------------------------------------
# Calculation Section
# -------------------------------------------------

if st.button("🧮 Calculate Score Card", type="primary", use_container_width=True):

    # Validate inputs
    if maths_mark > math_max:
        st.error(f"❌ Mathematics mark ({maths_mark:.2f}) cannot exceed maximum marks ({math_max:.0f})")
        st.stop()

    if physics_mark > phy_max:
        st.error(f"❌ Physics mark ({physics_mark:.2f}) cannot exceed maximum marks ({phy_max:.0f})")
        st.stop()

    if chemistry_mark > chem_max:
        st.error(f"❌ Chemistry mark ({chemistry_mark:.2f}) cannot exceed maximum marks ({chem_max:.0f})")
        st.stop()

    # -------------------------------------------------
    # Calculations
    # -------------------------------------------------

    # Normalization (YB = (100 * XjB) / HjB)
    norm_math = (100 * maths_mark) / math_max
    norm_phy = (100 * physics_mark) / phy_max
    norm_chem = (100 * chemistry_mark) / chem_max

    # Weightage (5:3:2)
    # Maths = 150, Physics = 90, Chemistry = 60
    math_weighted = (norm_math * 150) / 100
    phy_weighted = (norm_phy * 90) / 100
    chem_weighted = (norm_chem * 60) / 100

    # Plus Two Score (out of 300)
    plus_two_score = math_weighted + phy_weighted + chem_weighted

    # Final Index Mark (out of 600)
    index_mark = plus_two_score + norm_score

    # Round to 4 decimals
    norm_math = round(norm_math, 4)
    norm_phy = round(norm_phy, 4)
    norm_chem = round(norm_chem, 4)
    plus_two_score = round(plus_two_score, 4)
    index_mark = round(index_mark, 4)
    norm_score = round(norm_score, 4)

    # -------------------------------------------------
    # Display Results
    # -------------------------------------------------

    st.divider()

    # Title
    st.subheader("📋 Score Card Results")

    # Display board and year info
    board_display = {"HS": "HSE", "CB": "CBSE", "IS": "ICSE"}.get(board, board)
    st.success(f"✅ Calculated for {board_display} - {year_pass}")

    # Create metrics grid
    rcol1, rcol2, rcol3 = st.columns(3)

    with rcol1:
        st.metric(
            label="📐 Plus Two Score",
            value=f"{plus_two_score:.4f}",
            delta="Out of 300",
            delta_color="off"
        )

    with rcol2:
        st.metric(
            label="🎓 Entrance Score",
            value=f"{norm_score:.4f}",
            delta="Out of 300",
            delta_color="off"
        )

    with rcol3:
        st.metric(
            label="🏆 Final Index Mark",
            value=f"{index_mark:.4f}",
            delta="Out of 600",
            delta_color="off"
        )

    st.divider()

    # Detailed breakdown
    st.subheader("📊 Detailed Breakdown")

    # Create detailed table
    detailed_results = pd.DataFrame({
        "Subject": ["Mathematics", "Physics", "Chemistry", "Total"],
        "Raw Mark": [f"{maths_mark:.2f}", f"{physics_mark:.2f}", f"{chemistry_mark:.2f}", ""],
        "Max Mark": [f"{math_max:.0f}", f"{phy_max:.0f}", f"{chem_max:.0f}", ""],
        "Normalized Score": [f"{norm_math:.4f}", f"{norm_phy:.4f}", f"{norm_chem:.4f}", ""],
        "Weighted Score": [
            f"{math_weighted:.4f}",
            f"{phy_weighted:.4f}",
            f"{chem_weighted:.4f}",
            f"{plus_two_score:.4f}"
        ],
        "Weightage": ["150", "90", "60", "300"]
    })

    st.dataframe(
        detailed_results,
        use_container_width=True,
        hide_index=True
    )

    # Show formula breakdown
    with st.expander("📖 View Formula Breakdown", expanded=False):
        st.markdown("""
        ### KEAM Normalization Formula

        **Step 1: Normalization**
        Normalized Score = (Raw Mark × 100) / Maximum Mark

        **Step 2: Weightage (5:3:2)**
        - Mathematics: 150 marks (50%)
        - Physics: 90 marks (30%)
        - Chemistry: 60 marks (20%)
        - Total: 300 marks

        **Step 3: Weighted Score Calculation**
        Mathematics Weighted = (Normalized_Math × 150) / 100
        Physics Weighted = (Normalized_Phy × 90) / 100
        Chemistry Weighted = (Normalized_Chem × 60) / 100
        Plus Two Score = Math_Weighted + Phy_Weighted + Chem_Weighted

        **Step 4: Final Index Mark**
        Index Mark = Plus Two Score + Entrance Normalized Score
        """)

    # Show calculations in detail
    with st.expander("🔍 View Calculation Details", expanded=False):
        st.write(f"**Board:** {board_display}")
        st.write(f"**Year:** {year_pass}")
        st.write(f"**Maximum Marks:** Math={math_max:.0f}, Physics={phy_max:.0f}, Chemistry={chem_max:.0f}")

        st.write("\n**Normalized Scores:**")
        st.write(f"- Mathematics: {norm_math:.4f}")
        st.write(f"- Physics: {norm_phy:.4f}")
        st.write(f"- Chemistry: {norm_chem:.4f}")

        st.write("\n**Weighted Scores:**")
        st.write(f"- Mathematics: {math_weighted:.4f} (150 marks weightage)")
        st.write(f"- Physics: {phy_weighted:.4f} (90 marks weightage)")
        st.write(f"- Chemistry: {chem_weighted:.4f} (60 marks weightage)")

        st.write("\n**Final Scores:**")
        st.write(f"- Plus Two Score: {plus_two_score:.4f}/300")
        st.write(f"- Entrance Score: {norm_score:.4f}/300")
        st.write(f"- **Index Mark: {index_mark:.4f}/600**")

    # Additional information
    st.info("ℹ️ This calculator uses the official KEAM normalization and weighting formula. The Index Mark is used for ranking candidates in the engineering admission process.")

    # Download results option
    results_df = pd.DataFrame({
        "Parameter": [
            "Board",
            "Year of Passing",
            "Mathematics Maximum",
            "Physics Maximum",
            "Chemistry Maximum",
            "Mathematics Raw Mark",
            "Physics Raw Mark",
            "Chemistry Raw Mark",
            "Mathematics Normalized",
            "Physics Normalized",
            "Chemistry Normalized",
            "Mathematics Weighted",
            "Physics Weighted",
            "Chemistry Weighted",
            "Plus Two Score (out of 300)",
            "Entrance Normalized Score (out of 300)",
            "Final Index Mark (out of 600)"
        ],
        "Value": [
            board_display,
            year_pass,
            f"{math_max:.0f}",
            f"{phy_max:.0f}",
            f"{chem_max:.0f}",
            f"{maths_mark:.2f}",
            f"{physics_mark:.2f}",
            f"{chemistry_mark:.2f}",
            f"{norm_math:.4f}",
            f"{norm_phy:.4f}",
            f"{norm_chem:.4f}",
            f"{math_weighted:.4f}",
            f"{phy_weighted:.4f}",
            f"{chem_weighted:.4f}",
            f"{plus_two_score:.4f}",
            f"{norm_score:.4f}",
            f"{index_mark:.4f}"
        ]
    })

    csv = results_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📥 Download Score Card Results",
        data=csv,
        file_name=f"KEAM_ScoreCard_{board}_{year_pass}.csv",
        mime="text/csv",
        use_container_width=True
    )

# -------------------------------------------------
# Footer Information
# -------------------------------------------------

st.divider()
st.caption("""
**KEAM Score Card Calculator** | Based on official KEAM normalization and weighting formula
- Mathematics: 150 marks weightage
- Physics: 90 marks weightage
- Chemistry: 60 marks weightage
- Total Plus Two Score: 300 marks
- Total Index Mark: 600 marks (Plus Two + Entrance)
""")
