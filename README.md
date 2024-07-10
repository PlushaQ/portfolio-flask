# Portfolio Flask App

This is a simple portfolio application built with Flask, using pure HTML, CSS, and JavaScript.

## Features

- Showcase your projects and skills
- Responsive design
- Simple and clean UI
- Easy to customize

## Technologies Used

- Flask (Python)
- HTML
- CSS
- JavaScript
- SQLAlchemy (for database handling)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/PlushaQ/portfolio-flask.git
    cd portfolio-flask
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    flask run
    ```

5. Open your browser and go to `http://127.0.0.1:5000` to view the app.

## Project Structure

portfolio-flask/
│
├── database/
│ └── database.py
├── static/
│ └── css/
│ └── styles.css
├── templates/
│ ├── base.html
│ └── index.html
├── .gitignore
├── LICENSE
├── README.md
├── app.py
└── requirements.txt

markdown
Skopiuj kod

- `database/`: Contains the database script.
- `static/css/`: Contains CSS files for styling.
- `templates/`: Contains HTML templates.
- `.gitignore`: Specifies files and directories to be ignored by git.
- `LICENSE`: License file for the project.
- `README.md`: This file.
- `app.py`: Main Flask application file.
- `requirements.txt`: Lists the Python packages required for the project.

## Usage

- Customize the HTML in `templates/` to update your portfolio content.
- Modify the CSS in `static/css/styles.css` to change the styles.

## Contributing

Feel free to fork this project and submit pull requests. Any contributions, issues, and feature requests are welcome.

## License

This project is open source and available under the [MIT License](LICENSE).
