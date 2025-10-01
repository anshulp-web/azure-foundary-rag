import os
import streamlit as st
from openai import AzureOpenAI
from dotenv import load_dotenv
# ========================
# Environment / Config
# ========================
load_dotenv()
endpoint = os.getenv("ENDPOINT_URL")
deployment = os.getenv("DEPLOYMENT_NAME")
search_endpoint = os.getenv("SEARCH_ENDPOINT")
search_key = os.getenv("SEARCH_KEY")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY")

# Initialize Azure OpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# ========================
# Streamlit UI
# ========================
st.title("E-commerce Product Info Chatbot")

user_input = st.text_input("Ask about products or company details:")

if st.button("Get Response") and user_input:
    # Prepare chat prompt
    chat_prompt = [
        {
            "role": "system",
            "content": (
                "You are an AI assistant that helps users find information about products suitable for e-commerce. "
                "From the given context, provide only the relevant product-related data. Do not include references or unrelated details. "
                "If no relevant product information is available, respond with: \"Please contact the company administration."
            )
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    try:
        completion = client.chat.completions.create(
            model=deployment,
            messages=chat_prompt,
            max_tokens=1000,
            temperature=0.3,
            top_p=0.3,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False,
            extra_body={
                "data_sources": [{
                    "type": "azure_search",
                    "parameters": {
                        "filter": None,
                        "endpoint": search_endpoint,
                        "index_name": "create-rag-vector",
                        "semantic_configuration": "azureml-default",
                        "authentication": {
                            "type": "api_key",
                            "key": search_key
                        },
                        "query_type": "simple",
                        "in_scope": True,
                        "strictness": 3,
                        "top_n_documents": 5
                    }
                }]
            }
        )

        st.subheader("Response:")
        st.write(completion.choices[0].message.content)

    except Exception as e:
        st.error(f"Error: {e}")
