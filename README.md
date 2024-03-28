# POSE CORRECTOR


This code COUNTS and CORRECTS pose using MediaPipe framework:-

1. PoseModule.py is the base file containing different functions for calculating angle, tracking position, capturing video feed.
2. app.py uses flask to rendering captured webcame frames to webpage
3. pose_left.py calculates and corrects left arm bicep curl
4. pose_right.py calculates and corrects right arm bicep curl
5. pose_pushup.py calculates and corrects pushup using coordinates from the left side
6. pose_squat.py calculates and corrects squat using coordinates from the left side
