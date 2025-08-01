import streamlit as st

# Hardcoded gym plan data
gym_plan = [
    {
        "day_name": "Day 1 - Monday (Legs & Posterior Chain Focus)",
        "exercises": [
            {"name": "Barbell Back Squat", "sets": "4", "reps": "5-8", "rpe": "8", "image_url_placeholder": "https://www.google.com/imgres?q=Seated%20Calf%20Raises&imgurl=https%3A%2F%2Fweighttraining.guide%2Fwp-content%2Fuploads%2F2016%2F10%2FLever-Seated-Calf-Raise-plate-loaded-resized.png"},
            {"name": "Romanian Deadlift", "sets": "3", "reps": "8-10", "rpe": "8", "image_url_placeholder": "https://i0.wp.com/physicalculturestudy.com/wp-content/uploads/2016/01/romaniandeadlift1.jpg?resize=563%2C331&ssl=1"},
            {"name": "Bulgarian Split Squat", "sets": "3", "reps": "10-12", "rpe": "7", "image_url_placeholder": "https://www.gymshark.com/_next/image?url=https%3A%2F%2Fimages.ctfassets.net%2F8urtyqugdt2l%2Fan332LVc89C33kZl3zNAp%2Fcc364829dedecb7dde2ef092c289c2bc%2Fdesktop-bulgarian-split-squats.jpg&w=1664&q=85"},
            {"name": "Lying Leg Curl (Machine)", "sets": "3", "reps": "12-15", "rpe": "7", "image_url_placeholder": "https://www.burnthefatinnercircle.com/members/images/1255.jpg?cb=20250102035845"},
            {"name": "Seated Calf Raises", "sets": "3", "reps": "15-20", "rpe": "8", "image_url_placeholder": "https://www.google.com/imgres?q=Seated%20Calf%20Raises&imgurl=https%3A%2F%2Fweighttraining.guide%2Fwp-content%2Fuploads%2F2016%2F10%2FLever-Seated-Calf-Raise-plate-loaded-resized.png"},
        ]
    }, 
    {
        "day_name": "Day 2 - Wednesday (Upper Push & Posture Correction)",
        "exercises": [
            {"name": "Incline Barbell Bench Press", "sets": "4", "reps": "6-8", "rpe": "8", "image_url_placeholder": "URL for Incline Barbell Bench Press image"},
            {"name": "Standing Overhead Press", "sets": "3", "reps": "8-10", "rpe": "8", "image_url_placeholder": "URL for Standing Overhead Press image"},
            {"name": "Cable Chest Fly", "sets": "3", "reps": "12-15", "rpe": "7", "image_url_placeholder": "URL for Cable Chest Fly image"},
            {"name": "Dumbbell Lateral Raises", "sets": "3", "reps": "15-20", "rpe": "7", "image_url_placeholder": "URL for Dumbbell Lateral Raises image"},
            {"name": "Wall-Facing Dumbbell Y-Raise", "sets": "2", "reps": "12-15", "rpe": "6", "image_url_placeholder": "URL for Wall-Facing Dumbbell Y-Raise image"},
        ]
    },
    {
        "day_name": "Day 3 - Friday (Upper Pull & Leg Strength Complement)",
        "exercises": [
            {"name": "Weighted Pull-Ups (or Lat Pulldown)", "sets": "4", "reps": "6-10", "rpe": "8", "image_url_placeholder": "URL for Weighted Pull-Ups image"},
            {"name": "Bent Over Barbell Row", "sets": "4", "reps": "8-10", "rpe": "8", "image_url_placeholder": "URL for Bent Over Barbell Row image"},
            {"name": "Chest-Supported Dumbbell Row", "sets": "3", "reps": "10-12", "rpe": "7", "image_url_placeholder": "URL for Chest-Supported Dumbbell Row image"},
            {"name": "Barbell Hip Thrust", "sets": "3", "reps": "8-10", "rpe": "8", "image_url_placeholder": "URL for Barbell Hip Thrust image"},
            {"name": "Hanging Leg Raise", "sets": "3", "reps": "12-15", "rpe": "8", "image_url_placeholder": "URL for Hanging Leg Raise image"},
        ]
    },
    {
        "day_name": "Day 4 - Optional Saturday (Accessory & Mobility / Active Recovery)",
        "exercises": [
            {"name": "Sled Push or Farmer Carries", "sets": "3-5 rounds", "reps": "~30m", "rpe": "7", "image_url_placeholder": "URL for Sled Push/Farmer Carries image"},
            {"name": "Goblet Squat", "sets": "3", "reps": "10-12", "rpe": "6-7", "image_url_placeholder": "URL for Goblet Squat image"},
            {"name": "Face Pulls", "sets": "3", "reps": "15-20", "rpe": "6-7", "image_url_placeholder": "URL for Face Pulls image"},
            {"name": "Cable External Rotations", "sets": "3", "reps": "15 reps per arm", "rpe": "6", "image_url_placeholder": "URL for Cable External Rotations image"},
            {"name": "Stretching + Mobility Work", "sets": "1", "reps": "10-15 min", "rpe": "N/A", "image_url_placeholder": "URL for Stretching/Mobility image"},
        ]
    }
]

st.set_page_config(layout="wide", page_title="Gym Planning")

st.title("My Gym Plan")
st.markdown("---")

# Display the plan
for day in gym_plan:
    st.header(day["day_name"])
    for i, exercise in enumerate(day["exercises"]):
        st.subheader(f"{i+1}. {exercise['name']}")
        
        col1, col2 = st.columns([3, 1]) # Column for details and image
        
        with col1:
            st.markdown(f"**Sets:** {exercise['sets']} | **Reps:** {exercise['reps']} | **RPE:** {exercise['rpe']}")
            
            # Use exercise["image_url_placeholder"] as the default value for the text input.
            # The user can still change it.
            default_img_url = exercise.get("image_url_placeholder", "")
            
            current_img_url = st.text_input(
                "Image URL:", 
                value=default_img_url, 
                key=f"{day['day_name']}_{exercise['name']}_url", 
                placeholder="Enter direct image URL (e.g., ends with .jpg, .png)"
            )
            
            if current_img_url:
                # Attempt to display the image from the current_img_url (either default or user-entered)
                # Add error handling in case the URL is invalid or image can't be loaded
                try:
                    st.image(current_img_url, width=300, caption=exercise['name'])
                except Exception as e:
                    st.warning(f"Could not load image from URL. Please check the link. Error: {e}")
        
        with col2:
            if not current_img_url: # Show placeholder text if no image URL yet
                 st.markdown("_Enter image URL to display picture_")

        st.markdown("---")

st.sidebar.info("Enter the URL of an image for each exercise to see it displayed.")

# To run this app:
# 1. Save the code as gym_planning_app.py
# 2. Open your terminal
# 3. Navigate to the directory where you saved the file
# 4. Run the command: streamlit run gym_planning_app.py 