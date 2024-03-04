# Running the Rasa Chatbot Project Locally

This document provides instructions on how to get your Rasa chatbot project up and running on your local machine. Please follow the steps carefully to ensure a successful setup.

## Prerequisites

Before proceeding, ensure that you have Python installed on your machine. This project requires a specific Python version. Failure to meet the Python version requirements will result in the project not running correctly.

## Installation

1. **Install Requirements**: First, you need to install the project dependencies. Navigate to the project directory in your terminal and run the following command:

    ```bash
    pip install -r requirements.txt
    ```

    This command assumes that you have a `requirements.txt` file in your project directory. If your dependencies are listed in another file, replace `requirements.txt` with the name of your file.

2. **Python Version Requirement**: Make sure that your Python version matches the project's requirement. You can check your Python version by running:

    ```bash
    python --version
    ```

    If your Python version does not meet the project's requirements, you will need to install the correct version of Python.

## Running the Chatbot

To run the Rasa chatbot, you will need to use the Rasa command line interface. Here are the most commonly used Rasa commands:

- **Train Your Model**: Before running your chatbot for the first time, you need to train your model with:

    ```bash
    rasa train
    ```

- **Interactive Training**: To improve your model by training it interactively, you can use:

    ```bash
    rasa interactive
    ```

- **Shell Mode**: To talk to your chatbot directly in the terminal, you can start it in shell mode:

    ```bash
    rasa shell
    ```
## Running the Chatbot with API Access

For scenarios where you need to provide external applications with access to your Rasa chatbot, the Rasa server can be started with additional options to enable API access and configure Cross-Origin Resource Sharing (CORS). This is particularly useful when integrating your chatbot with web applications or when the chatbot needs to be accessed from different domains.

```bash
rasa run --enable-api --cors "*"
```

These commands are essential for running and training your Rasa chatbot project. Make sure to execute them in your project directory.

## Troubleshooting

If you encounter any issues while running your Rasa chatbot, please refer to the [Rasa Documentation](https://rasa.com/docs/) or check the project's FAQ section.

## Conclusion

By following these instructions, you should be able to run your Rasa chatbot project locally on your machine. Remember to install all requirements and ensure your Python version meets the project's requirements. Happy developing!
