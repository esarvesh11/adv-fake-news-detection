# Advance Fake News Detection System

## Prerequisites

* [Node.js](https://nodejs.org/en/download) >=17.x (or yarn)
* [Python](https://www.python.org/downloads/) 3.x
* virtualenv (or conda)
* Basic understanding of Chrome Extension development

## Installation

### **Part 1: React Application**

1. Clone the Repository:
   ```bash
   git clone git@github.com:esarvesh11/adv-fake-news-detection.git
   ````

2. Backend Setup:
    ```bash
    cd server
    npm install
    ```

3. Frontend Setup:
    ```bash
    cd client
    npm install
    ```

4. Environment Variables:
    * Create a .env file in the backend directory.
    * Add any necessary environment variables (database credentials, API keys, etc.) For example:

    ```bash
    MONGODB_URI=mongodb://localhost:27017/your-database
    ```

### **Part 2: Chrome Extension**

1. Chrome Extension, Backend Setup:

    * Create virtual environment:
    ```Bash
    cd flask
    python3 -m venv venv  # Or use conda if preferred
    source venv/bin/activate 
    ```

    * Install dependencies
    ```Bash
    pip install -r requirements.txt
    ```

    * Environment Variables:
        * Create a .env file in the backend directory.
        * Add any necessary environment variables (database credentials, API keys, etc.) For example:

    ```bash
    OPENAI_API_KEY=
    ```
   
2. Load in Chrome:

    * In Chrome, navigate to `chrome://extensions`
    * Enable "Developer mode" in the top right corner.
    * Click "Load unpacked" and select the `chrome-extension` directory of your project.

## Running the Application

### **React Application:**

1. Start the Backend Server

    ```bash
    cd server
    npm start
    ```

2. Start the Frontend Server

    ```bash
    cd client
    npm start
    ```

### **Chrome Extension:**

*The extension should be loaded in Chrome. Interact with it as designed.*

## Contributing

1. Fork the repository.
2. Create a new branch `git checkout -b feature/your-feature`
3. Make your changes.
4. Commit your changes `git commit -am 'Add new feature`
5. Push to the branch `git push origin feature/your-feature`
6. Create a new Pull Request.