from openai import OpenAI
from pydantic import BaseModel, RootModel
import os

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
        response_format=schema,
        temperature=0,
        top_p=0.1
    )
    
    return response.choices[0].message.parsed