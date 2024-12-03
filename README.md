
# SMS Messaging Application

This Django application provides functionality to send SMS messages using a third-party SMS gateway. It is designed to be user-friendly and easy to integrate into existing projects.

## Features
- Send SMS messages to specified phone numbers.
- Configurable settings for SMS gateway integration.
- Basic form interface for testing SMS functionality.

## Requirements
- Python 3
- Django 4 or higher
- A third-party SMS gateway account (e.g., Twilio, Nexmo, or other providers).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jeluayan28/Django_SMS.git
   cd Django_SMS
   ```

2. Set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Configure the SMS gateway credentials:
   - Open the `settings.py` file and add the necessary SMS gateway credentials:
     ```python
     SMS_GATEWAY_API_KEY = 'your_api_key_here'
     SMS_GATEWAY_API_SECRET = 'your_api_secret_here'
     SMS_GATEWAY_SENDER_ID = 'your_sender_id_here'
     ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

1. Access the application in your web browser at `http://127.0.0.1:8000/`.

2. Use the SMS form to input the recipient's phone number and the message you want to send.

3. Click "Send" to deliver the SMS.

## File Structure
- `sms/`: Contains the core SMS application logic.
  - `views.py`: Defines the views for sending SMS.
  - `forms.py`: Manages the input form for SMS details.
  - `models.py`: Stores SMS-related data (if needed).
- `templates/sms/`: Contains HTML templates for the SMS form interface.

## Contributing
Feel free to submit issues or contribute via pull requests. Please ensure your code follows Django's coding standards.

## License
This project is licensed under the MIT License.
