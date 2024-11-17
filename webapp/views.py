import os

import cv2
import numpy as np
from django.shortcuts import redirect, render
from keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img

from .models import *


def index(request):
    return render(request, "index.html")

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        c_password = request.POST['c_password']
        if password == c_password:
            if Users.objects.filter(email=email).exists():
                return render(request, 'register.html', {'message': 'User with this email already exists'})
            new_user = Users(name=name, email=email, password=password)
            new_user.save()

            return render(request, 'login.html', {'message': 'Successfully Registerd!'})
        return render(request, 'register.html', {'message': 'Password and Conform Password does not match!'})
    return render(request, 'register.html')
 

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password1 = request.POST['password']

        try:
            user_obj = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return render(request, 'login.html', {'message': 'Invalid Username or Password!'})
        
        password2 = user_obj.password
        if password1 == password2:
            user_id = user_obj.id
            request.session['user_id'] = user_id
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'message': 'Invalid Username or Password!'})
    return render(request, 'login.html')

def about(request):
    return render(request, "about.html")

def home(request):
    return render(request, "home.html")



IMG_HEIGHT = 128
IMG_WIDTH = 128
IMG_CHANNELS = 3

def load_and_preprocess_image(path, is_label=False):
    try:
        if is_label:
            img = load_img(path, target_size=(IMG_HEIGHT, IMG_WIDTH), color_mode='grayscale')
            img_array = img_to_array(img)
            img_array = img_array / 255.0  # Normalize to [0, 1]
            img_array = np.round(img_array)  # Ensure binary
            return img_array
        else:
            img = load_img(path, target_size=(IMG_HEIGHT, IMG_WIDTH))
            img_array = img_to_array(img)
            img_array = img_array / 255.0  # Normalize to [0, 1]
            return img_array
    except Exception:
        
        return None

def prediction(request):
    if request.method == 'POST':
        file = request.FILES['file1']
        file1 = request.FILES['file2']

        fn1 = Images(path1=file, path2=file1)
        fn1.save()

        path1 = os.path.join(r'webapp/static/image1/', fn1.path1_filename())
        path2 = os.path.join(r'webapp/static/image2/', fn1.path2_filename())
        image_output = "webapp/static/output/result.jpg"

   
        model_path = 'final_cnn_model2.h5'
        model = load_model(model_path)  
        
        img1 = load_and_preprocess_image(path1)
        img2 = load_and_preprocess_image(path2)

        if img1 is None or img2 is None:
            return render(request, "prediction.html", {'message': 'Error loading images.'})

        # Simulate preparing input for the model
        combined_img = np.concatenate([img1, img2], axis=-1)

        _ = combined_img  # To avoid unused variable warning

        # Continue  processing logic
        img1 = cv2.imread(path1, 0)
        img2 = cv2.imread(path2, 0)

        h, w = img2.shape

        res1 = np.zeros((h, w, 1), np.uint8)

        disappear = cv2.subtract(img1, img2)
        appear = cv2.subtract(img2, img1)

        # Apply Gaussian blur and Otsu's threshold
        blur1 = cv2.GaussianBlur(disappear, (5, 5), 0)
        _, disappear = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        blur2 = cv2.GaussianBlur(appear, (5, 5), 0)
        _, appear = cv2.threshold(blur2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        cv2.imwrite(image_output, appear)

        threshold_area = 3000.0
        image_src = cv2.imread(image_output)

        gray = cv2.cvtColor(image_src, cv2.COLOR_BGR2GRAY)
        _, gray = cv2.threshold(gray, 250, 255, 0)

        contours, _ = cv2.findContours(gray, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        mask = np.zeros(image_src.shape, np.uint8)
        cnts = sorted(contours, key=cv2.contourArea)

        for c in cnts:
            area = cv2.contourArea(c)
            if area > threshold_area:
                cv2.drawContours(mask, [c], -1, (255, 255, 255), -1)

        img_out = "webapp/static/output/refined.jpg"
        cv2.imwrite(img_out, mask)

        return render(request, "prediction.html", {'path': "static/output/refined.jpg"})
    return render(request, "prediction.html")








