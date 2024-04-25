# uPark: Online Parking Pay System

## About uPark

uPark is an online payment management system built with Python and Django, designed to simplify the payment process of the parking service in any entity that provides this service.


## Features

* **User Registration and Authentication**: Users can securely register for an account and log in.<br>
* **Payment Integration**: Integration with payment gateways to facilitate online payments for parking reservations.<br>
* **Admin Dashboard:** Administrators can manage user accounts and handle rates per type of vehycle.<br>
* **Reporting and Analytics:** Generate reports and analyze parking usage data for better resource management.<br>


## Installation

1. **Clone the repository:** _git clone https://github.com/jmonto98/uPark.git_

2. **Navigate to the project directory:** _cd uPark_

3. **Create a virtual environment (Optional)*:** _python -m venv env_ <br>
3.1 **Activate the virtual environment:** <br>
3.1.1 **On Windows:** _.\env\Scripts\activate_ <br>
3.1.2 **On macOS/Linux:** _source env/bin/activate_

4. **Install dependencies:** _pip install -r requirements.txt_

5. **Apply migrations:**<br>
* _python manage.py makemigrations_<br>
* _python manage.py migrate_

6. **Start the development server:** _python manage.py runserver_


## Usage

* Access the application by navigating to the provided URL in your web browser. (http://127.0.0.1:8000/)<br>
* Register for an account or log in if you already have one.<br>
* Recharge your card or Buy a ticket.<br>
* Admins can access the dashboard to manage rates, view reports, and handle user accounts.<br>

## Contact
For any inquiries or support, please contact admin@upark.com.