import streamlit as st
import pandas as pd

# App title
st.title("Student Daily Timetable Planner")

st.write("Plan your day effectively by creating a personalized timetable. Fill in the details below and view your timetable.")

# Input for timetable
st.subheader("Timetable Inputs")

# Number of time slots
num_slots = st.number_input("Number of time slots:", min_value=1, max_value=24, value=5)

# Initialize timetable data
timetable_data = {"Time Slot": [], "Activity": []}

for i in range(num_slots):
    col1, col2 = st.columns(2)
    with col1:
        time_slot = st.text_input(f"Time Slot {i + 1} (e.g., 9:00 AM - 10:00 AM)", key=f"time_{i}")
    with col2:
        activity = st.text_input(f"Activity for Slot {i + 1}", key=f"activity_{i}")
    
    timetable_data["Time Slot"].append(time_slot)
    timetable_data["Activity"].append(activity)

# Button to display the timetable
if st.button("Generate Timetable"):
    # Convert data into a DataFrame
    timetable_df = pd.DataFrame(timetable_data)
    
    # Display the timetable
    st.subheader("Your Daily Timetable")
    st.dataframe(timetable_df)
    
    # Option to download the timetable
    csv = timetable_df.to_csv(index=False)
    st.download_button(
        label="Download Timetable as CSV",
        data=csv,
        file_name="daily_timetable.csv",
        mime="text/csv"
    )
