# Flask-Google-Form

This Flask application provides a form submission feature where users can submit their information. The submitted form data is stored in a SQLite database and can be viewed through the provided API endpoints.

## Features

- User-friendly web interface for submitting information via a form.
- Automatic email notification sent to the user upon successful form submission.
- Storage of submitted form data in a SQLite database.
- API endpoint to retrieve all form data in JSON format.

## Prerequisites

- Python 3.10
- Flask
- SQLite

## Installation

1. Clone the repository: `git clone https://github.com/shubham21155102/Flask-Google-Form/`
2. Install the required dependencies: `pip install -r requirements.txt`

## Configuration

1. Set up a Gmail account for sending email notifications.
2. Open the `app.py` file and update the following variables with your Gmail account credentials:
   - `sender_email`
   - `password`

## Usage

1. Run the Flask application: `python app.py`
2. Access the application in your web browser: `http://localhost:5000`

## API Endpoints

- `GET /alldatas`: Retrieves all form data in JSON format.

## Database

The application uses a SQLite database (`data.db`) to store the submitted form data. You can view the data by accessing the API endpoint or through the provided web interface at `/displayall`.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow the guidelines outlined in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).
