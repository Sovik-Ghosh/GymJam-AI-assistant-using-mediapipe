<img src="/assets/app.logomakr.com28ja6E-ezgif.com-crop.gif" style="width: 1000px;">

<div style="display: flex; justify-content: center;">
  <img src="assets/combo.jpg" alt="Squats" style="width: 100%; height: auto; margin-right: 5px;">
</div>

## Project Overview

Welcome to GymJam, a cutting-edge web application designed to enhance your fitness journey and help you achieve your fitness goals. It is your comprehensive companion, providing a diverse range of exercises tailored to target different body parts. With an intuitive user interface and a library of exercise variations, an immersive fitness experience that caters to users of all levels.

## Getting Started

### Prerequisites

1. Backend Framework: python >= 3.9, flask, mediapipe
   - Other Software Dependencies: Package managers (e.g. pip), version control system (e.g. Git)

2. Client-Side:
   - Operating System: Windows, macOS, or Linux
   - Web Browser: Google Chrome, Mozilla Firefox, Safari, Microsoft Edge, or equivalent
   - Browser Plugins: JavaScript enabled, support for HTML5 and CSS3
   - Internet Connectivity: Broadband or high-speed internet connection


### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Sovik-Ghosh/GymJam.git
   ```

2. Navigate to the project directory:

   ```bash
   cd backend
   ```

3. Create a virtual environment:
    ```bash
    python3 -m venv my_env
    ```

4. Activate the virtual environment:
    ```bash
    source my_env/bin/activate
    ```

5. Install dependencies (if any) and set up your development environment.
   ```bash
   pip3 -r requirements.txt
   ```
## Framework

### Mediapipe:

![](assets/pipe.jpeg)

MediaPipe is an open-source framework developed by Google that provides a comprehensive solution for building machine learning (ML) pipelines to process multimedia data, including video, audio, and image streams. It is designed to facilitate the development of real-time perception and processing pipelines, particularly for tasks related to computer vision and media processing.

## Running the Simulation

1. Go to backend directory

2. Activate the virtual environment:
    ```bash
    source my_env/bin/activate
    ```
    

3. Run the code:
    ```bash
    python app.py
    ```

4. Copy and paste anyone of the url in a browser.
    - Left Bicep Curl:
        ```
        http://localhost:5000/video_feed_left
        ```
    - Right Bicep Curl:
        ```
        http://localhost:5000/video_feed_right
        ```
    - Pushup:
        ```
        http://localhost:5000/video_feed_pushup
        ```
    - Squat:
        ```
        http://localhost:5000/video_feed_squat
        ```

5. Observe and follow the instructions on the browser for the correct form of exercise.

## Exercise Overview

<div style="display: flex; justify-content: center;">
  <img src="assets/squats.jpg" alt="Squats" style="width: 55%; height: 240px; margin-right: 5px;">
  <img src="assets/pushup.png" alt="Pushup" style="width: 43%; margin-left: 5px;">
</div>

## Customizing and Extending

Feel free to customize the project to implement your strategies and behaviors for extending exercise variations.

You can modify the existing controllers or create new ones.
1. [PoseModule.py](backend/PoseModule.py) is the base file containing different functions for calculating angle, tracking position, capturing video feed.
2. [app.py](backend/app.py) uses flask to render captured webcame frames to webpage
3. [pose_left.py](backend/pose_left.py) calculates and corrects left arm bicep curl
4. [pose_right.py](backend/pose_right.py) calculates and corrects right arm bicep curl
5. [pose_pushup.py](backend/pose_pushup.py) calculates and corrects pushup using coordinates from the left side
6. [pose_squat.py](backend/pose_squat.py) calculates and corrects squat using coordinates from the left side

Additionally, you can explore advanced features provided by [Mediapipe](https://developers.google.com/mediapipe).

## Contributing

If you would like to contribute to this project, please follow our [contribution guidelines](CONTRIBUTING.md). We welcome bug reports, feature requests, and pull requests.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
