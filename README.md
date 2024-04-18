# English

# Comment Moderator

This project is a web application for classifying text comments as positive, negative, or neutral using a pre-trained Support Vector Machine (SVM) model.

![app_interface](https://github.com/rafael-rod/Comment-Moderator/blob/main/comment_moderator.png)

## Installation

1. Clone this repository to your local machine:

```
git clone https://github.com/your_username/your_project.git
```

2. Install project dependencies:

```
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```
python app.py
```

2. Access the application in your web browser by visiting [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. You can interact with the application in two ways:

   - **Classify Individual Comment**: Enter a comment in the text field and click the "Classify Comment" button.
   
   - **Classify Comments from a JSON File**: Drag and drop a JSON file with a list of comments into the designated area or click to select a file. Ensure the file follows the specified format.

## Project Structure

- **app.py**: Contains the Flask application code, including route definitions and comment classification logic.
  
- **index.html**: The user interface of the web application, written in HTML and CSS. It provides a field for entering comments, an area for displaying classified comments, and buttons for interacting with the application.

## Requirements

- Python 3.x
- Flask
- Flask-Cors
- scikit-learn
- joblib

## Contribution

Contributions are welcome. If you want to improve this project, please create a pull request detailing the proposed changes.

## Credits

This project was created by Rafael R.
