# Virtual White Board 

## Project Structure


``` bash
~/virtual-whiteboard/
.
├── app
│   ├── assets
│   │   └── styles.css
│   ├── components
│   │   ├── capture.html
│   │   └── index.html
│   ├── __init__.py
│   ├── __pycache__
│   │   └── .... 
│   └── routes.py
├── LICENSE
├── README.md
├── requirements.txt
└── run.py

5 directories, 11 files

```

## Overview

This is a Flask web application that utilizes OpenCV to create a virtual whiteboard. The virtual whiteboard allows users to draw, write, and interact with a digital canvas in real-time. This project serves as a collaborative tool for remote communication, brainstorming, and creative collaboration.

## Todo's 

- **Real-time Drawing:** Users can draw on the virtual whiteboard in real-time using a variety of colors and brush sizes.

## Dependency

- Python 3.x
- Flask
- OpenCV

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Himanshu-Parangat/virtual-whiteboard
    ```

2. Navigate to the project directory:

    ```bash
    cd virtual-whiteboard
    ```

3. Create a virtual environment (optional but recommended):

    ```bash
    python3 -m venv .env
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        .env\Scripts\activate
        ```

    - On Unix or MacOS:

        ```bash
        source .env/bin/activate
        ```

5. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Flask application:

    ```bash
    python run.py
    ```

2. Open your web browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to access the virtual whiteboard.



## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 MIT License - see the [LICENSE](LICENSE) file for details.
