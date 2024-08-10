### Task Summary

   **Web Application Development:**
    - Using the Angelcam Developer Portal, I built a web application that met these requirements:
    
    - **Login Functionality:**
      - Implemented login using the provided Personal Access Token.
      - Developed a [Login Page](http://localhost:3000/login/) as per the provided screenshots.
        
    - **Camera Listing:**
      - Listed shared cameras and displayed them on a [Camera List Page](http://localhost:3000/cameras/).
        
    - **Live Video Streaming:**
      - Showed live video from the selected camera.
      - Created pages for [Sample/112860](http://localhost:3000/camera/112860/) and [Street/112859](http://localhost:3000/camera/112859/).
---

### 1. **Project Structure**
The project structure is organized as follows:

```
angelcam/
├── backend/
│   ├── config/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── camera/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── requirements.txt
│   └── venv/
└── frontend/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── components/
    │   │   ├── CameraList.js
    │   │   ├── CameraView.js
    │   │   └── VideoPlayer.js
    │   ├── App.js
    │   ├── index.js
    │   └── styles.css
    ├── .gitignore
    ├── package.json
    └── README.md
```
### 2. **Backend**
The backend is built using Django and Django REST Framework. It provides an API for managing camera data.

#### 2.1. **Installation**
To set up the backend, follow these steps:
1. Clone the repository:
2. Navigate to the backend directory:
3. Run development server:
4. python manage.py runserver
5. The backend should now be running at http://localhost:8000/.

### 3. **Frontend**
The frontend is built using React. It provides a user interface for managing camera data.

#### 3.1. **Installation**
To set up the frontend, follow these steps:
1. Clone the repository:
2. Navigate to the frontend directory:
3. Run development server:
4. npm start
5. The frontend should now be running at http://localhost:3000/.

