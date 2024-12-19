from ollama import chat
from pydantic import BaseModel, RootModel

def with_structured_output(
    prompt: str,
    schema: type[BaseModel] | type[RootModel],
    model: str = "llama3.1") -> BaseModel | RootModel:
    """
    Decodes the provided prompt using the specified model and validates the response against the given schema.

    Args:
        `prompt` (str): The prompt to decode
        `schema` (BaseModel | RootModel): The schema to structure the output with
        `model` (str, optional): The model to use. Defaults to "llama3.1".

    Returns:
        BaseModel | RootModel: A Pydantic model containing the structured output.
    """
    
    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format=schema.model_json_schema()
    )
    return schema.model_validate_json(response.message.content)