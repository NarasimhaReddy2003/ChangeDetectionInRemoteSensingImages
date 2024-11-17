
# Change Detection in Remote Sensing images

This project implements a change detection system using machine learning techniques integrated with a Django web application. The system processes two remote sensing images taken at different times from the same geographical area and highlights areas where changes have occurred.



## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
## Features

- Upload and process two images (before and after) for change detection.
- Machine learning model (.h5) for image processing.
- Display of the difference image highlighting changes.
- Django-based web interface for user interaction.

## Requirements

### Python Dependencies
- Python 3.x
- Django 3.x+
- TensorFlow or Keras (for loading the ML model)
- OpenCV (for image processing)
- Git LFS (for managing large model files)

You can install the required Python packages by running:
```bash
pip install -r requirements.txt
 ```



## Installation

### Clone the Repository:
```bash
git clone https://github.com/username/CDRSI.git
cd CDRSI
```
- Set up the Virtual Environment: Create and activate a virtual environment (optional but recommended):
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

```

- Run the Development Server:

```bash
python manage.py runserver
```
Access the Web Application: Open a web browser and go to http://127.0.0.1:8000/ to access the application.


## Usage

- Upload two remote sensing images.
- Click on "Process" to detect changes between the images.
- The output will display the difference image highlighting the detected changes.


## Screenshots

![Home Page](https://github.com/IASNAVAP/CDRSI/blob/main/webapp/static/image/home.png)
![Login Page](https://github.com/IASNAVAP/CDRSI/blob/main/webapp/static/image/login.png)
![Predection Page](https://github.com/IASNAVAP/CDRSI/blob/main/webapp/static/image/prediction.png)



