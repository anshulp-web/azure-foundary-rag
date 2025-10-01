# E-commerce Product Info Chatbot

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange)
![Azure OpenAI](https://img.shields.io/badge/Azure-OpenAI-purple)

---

## Project Description
The **E-commerce Product Info Chatbot** is an AI-powered assistant built with **Streamlit** and **Azure OpenAI**. It helps users quickly find product and company information suitable for e-commerce platforms. By combining **RAG (Retrieval-Augmented Generation)** with **Azure Cognitive Search**, it delivers accurate, context-aware answers while filtering out irrelevant data.  

If no relevant information is available, it prompts users with:  
*"Please contact the company administration."*

---

## Features
- Interactive web interface using **Streamlit**  
- AI responses powered by **Azure OpenAI**  
- Semantic search integration using **Azure Cognitive Search**  
- Handles dynamic queries about products and company details  
- Provides concise answers with a fallback message for missing data  

---

## Tech Stack
- **Python 3.11+**  
- **Streamlit** – Web UI framework  
- **Azure OpenAI** – Natural language responses  
- **Azure Cognitive Search** – Semantic retrieval of product information  
- **python-dotenv** – Secure management of environment variables  

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ecommerce-chatbot.git
cd ecommerce-chatbot

---
```
## Create a virtual environment and activate it
```bash
python -m venv venv
# Activate the environment:
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```
## Install all required dependencies

```bash
pip install streamlit openai python-dotenv

```
## Create a .env file

```ini
ENDPOINT_URL=your_azure_openai_endpoint
DEPLOYMENT_NAME=your_model_deployment_name
SEARCH_ENDPOINT=your_azure_search_endpoint
SEARCH_KEY=your_azure_search_api_key
AZURE_OPENAI_API_KEY=your_azure_openai_api_key

```
## Run the chatbot

```bash
streamlit run app.py





