from ollama import chat
from openai import OpenAI
from pydantic import BaseModel, RootModel
from dotenv import load_dotenv
import os

def decode_with_ollama(
    prompt: str,
    schema: type[BaseModel] | type[RootModel],
    model: str = "llama3.1") -> (BaseModel | RootModel):
    """
    Decodes the provided prompt using the specified model and validates the response against the given schema.

    Args:
        `prompt` (str): The prompt to decode
        `schema` (BaseModel | RootModel): The schema to structure the output with
        `model` (str, optional): The model to use. Defaults to "llama3.1".

    Returns:
        dict: The formatted JSON output.
    """
    
    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format=schema.model_json_schema(),
        options={
            "temperature": 0,
            "num_ctx": 4096
        }
    )
    
    return schema.model_validate_json(response.message.content)


load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def decode_with_openai(
    prompt: str,
    schema: type[BaseModel] | type[RootModel],
    model: str = "gpt-4o-mini") -> (BaseModel | RootModel):
    """
    Uses OpenAI Structured Output to decode the prompt against the provided schema

    Args:
        `prompt` (str): The prompt to decode
        `schema` (BaseModel | RootModel): The schema to structure the output with
        `model` (str, optional): The model to use. Defaults to "gpt-4o-mini".

    Returns:
        dict: The formatted JSON output.
    """
    
    response = client.beta.chat.completions.parse(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        response_format=schema
    )
    
    return response.choices[0].message.parsed