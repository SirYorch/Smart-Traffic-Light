# Smart-Traffic-Light

This project presents an **AI-based smart traffic light system** designed to optimize traffic flow at intersections by counting vehicles in real time.

## Description

The goal of this system is to **increase the efficiency of traditional traffic lights** by dynamically adjusting their behavior based on current road activity. It uses **two ESP32-CAM modules**, installed on the traffic light poles, to count the number of vehicles on each lane.

The data collected is processed by an AI system that makes real-time decisions about which direction should receive a longer green light duration, helping to reduce wait times and prevent congestion.

##  System Features

-  Real-time traffic monitoring and vehicle counting.
-  Dynamic decision-making based on traffic conditions.
-  Compatible with traditional traffic light infrastructure.
-  Scalable design for multiple intersections.

## Technologies Used

- **Python** and/or **C++** for image processing.
- **Lightweight neural network / AI** for traffic control decisions.
- **MQTT or HTTP** protocols for device communication.
- **Optional IoT dashboard** for remote monitoring.

## Content
- introduccion.ipynb: contains the development of an AI using yolo, usedd for understand how we made it.
- desarrolloIA.ipynb: contains the development the objective AI, using the vehicules dataset from roboflow.
- pruebas.ipynb: contains methos to check how the AI is working, will help us to know if it works properly before using the esp cameras and control.
- funcionamientototal.ipynb: contains the code for working with the esp cameras. this is the final model and functionality. 

<!-- ## Installation -->

### Requirements

- Digitally controllable traffic light.
- Local or cloud server for image processing (if not done on ESP32).

### Soon

- Functional system implemented in a simulation.
- Real time traffic light functionality.
- Dinamic light change on a randomized system.