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
