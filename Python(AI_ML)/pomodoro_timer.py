import streamlit as st
import time
import winsound


def beep(frequency=1000, duration=500):
    winsound.Beep(frequency, duration)


def countdown(t, phase):
    placeholder = st.empty()

    while t > 0:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"

        placeholder.markdown(f"### {phase}: {timer}")

        if t == 10:
            beep(600, 1000)

        time.sleep(1)
        t -= 1

    placeholder.success(f"{phase} Over!")

    # Completion alarm
    beep(800, 1500)


def run_timer(study_time, break_time, cycles):
    for current_cycle in range(1, int(cycles) + 1):
        st.success(
            f"Cycle {current_cycle}/{int(cycles)}: "
            f"Study for {int(study_time)} minutes"
        )

        countdown(int(study_time) * 60, "Study Time")

        st.warning("Study finished! Take a break.")

        countdown(int(break_time) * 60, "Break Time")

        st.info("Break finished! Back to study.")

    st.balloons()
    st.success("Great work! All cycles completed.")


st.title("Study-Break Timer with Alarm")

study_time = st.number_input(
    "Enter study time (minutes):",
    min_value=1,
    value=1,
    step=1,
)

break_time = st.number_input(
    "Enter break time (minutes):",
    min_value=1,
    value=1,
    step=1,
)

cycle = st.number_input(
    "Enter number of cycles:",
    min_value=1,
    value=1,
    step=1,
)

if st.button("Start Timer"):
    run_timer(study_time, break_time, cycle)