Prerequisites

Backend:
Python 3.x + and above
Django
Django REST Framework
A Gmail account (for testing with SMTP)

Frontend:
Nodejs
npm 10.x.x + above


Setup

Backend:
Open a terminal and navigate to your project backend directory

Activate the virtual environment.
Run:
    macOS/Linux:
    source venv/bin/activate

    Windows(cmd):
    backend\Scripts\activate or backend\Scripts\activate.bat

    Windows(powershell):
    backend\Scripts\activate.psl

Run the following commands to install the required packages:
    pip install django djangorestframework
    pip install django-cors-headers


When activated, Start the Django development server:
    python manage.py runserver  


Frontend:
Open a terminal and navigate to your project frontend directory
Run:
    npm install

Run development project:
    npm run dev



Purpose for backend:
 * Only for sending emails to the inquirers
 * Host email was only for testing not actual working/business email


