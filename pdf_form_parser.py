from openai import OpenAI
import os
from config import openai_model_name, max_tokens
import json
from llama_parse import LlamaParse
from dotenv import load_dotenv
load_dotenv()
import nest_asyncio
nest_asyncio.apply()

OPENAI_API_KEY = os.environ.get("OPENAI_KEY")
client = OpenAI(api_key=OPENAI_API_KEY)

pdf_parser = LlamaParse(
    result_type="markdown",
    api_key="llx-LDWuTLqPq2cIEQkNloEKs005NxXeOLw8Ri14HWiGsUyv93yy",
    gpt4o_mode=True,
    gpt4o_api_key=OPENAI_API_KEY
)

with open("prompt_form_parser.txt", "r") as f:
    FIELD_EXTRACT_PROMPT = f.read()


DELIMITER = "--------------------------------------"
def pdf_form_parser(pdf_form_link:str):
    
    documents1 = pdf_parser.load_data(pdf_form_link)
    text = documents1[0].get_content()
    prompt = FIELD_EXTRACT_PROMPT.format(TEXT=text)
    model = openai_model_name

    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0,
        max_tokens=max_tokens,
        stream=False,
        stop=None,
        response_format={ "type": "json_object" }
    )

    fields = json.loads(completion.choices[0].message.content)
    answer_token = completion.usage.completion_tokens
    answer_cost = answer_token * 0.0015 / 1000
    prompt_token = completion.usage.prompt_tokens
    prompt_cost = prompt_token * 0.0005 / 1000
    total_token = completion.usage.total_tokens
    total_cost = answer_cost + prompt_cost
    
    response = {
        "fields": fields,
        "token_usage": {
            "answer": answer_token,
            "prompt": prompt_token,
            "total": total_token
        },
        "cost": {
            "answer": answer_cost,
            "prompt": prompt_cost,
            "total": total_cost
        }
    }
    
    return response

if __name__ == "__main__":
    response = pdf_form_parser("form.pdf")
    print(response)
    print(f"Total cost: {response['cost']['total']}")