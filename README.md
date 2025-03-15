# MediChat: Next-Gen Healthcare Assistant

![The MediChat's Interface](https://github.com/Vickey-VJ/Healthcare-ChatBot/blob/main/templates/image.png)

## Overview

MediChat is a healthcare chatbot built using **LangChain**, **Pinecone**, **Groq**, and **LLM**. It provides users with instant medical advice, symptom analysis, and general healthcare information. The web interface is powered by **Flask**, ensuring an interactive and user-friendly experience.

## Features

- **Conversational AI**: Utilizes **Groq's LLM** for natural language understanding and medical query responses.
- **Semantic Search**: Integrates **Pinecone** for fast and efficient retrieval of medical knowledge.
- **Web Application**: Built with **Flask** for a smooth and responsive user experience.
- **Secure & Scalable**: Designed to handle multiple user queries efficiently.
- **24/7 Availability**: Provides instant responses to health-related queries anytime, anywhere.
- **HIPAA Compliance Ready**: Can be enhanced for secure handling of medical data.

## Tech Stack

- **Backend**: Flask, LangChain, Groq LLM
- **Vector Database**: Pinecone
- **Frontend**: HTML, CSS, JavaScript (or Flask templates)

## Installation & Setup

### Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)
- API keys for **Groq**, **Pinecone**

### Clone the Repository

```sh
git clone https://github.com/vickey-vj/healthcare-chatbot.git
cd healthcare-chatbot
```

### Install Dependencies

```sh
pip install -r requirements.txt
```

### Set Up Environment Variables

Create a `.env` file in the root directory and add:

```sh
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

### Run the Flask Application

```sh
python app.py
```

The application will be available at `http://127.0.0.1:5000/`.

## Usage

1. Open the web app in your browser.
2. Type in your healthcare-related query.
3. Receive AI-generated responses based on **Groq LLM** and **Pinecone** knowledge retrieval.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add new feature"`)
4. Push to the branch (`git push origin feature-name`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

