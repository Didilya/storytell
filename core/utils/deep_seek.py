# install OpenAI SDK first: `pip3 install openai`
from core.settings import core_settings
from openai import OpenAI, APIStatusError

client = OpenAI(api_key=core_settings.LLM_NODEL_API_KEY, base_url="https://api.deepseek.com")

def get_first_llm_response(question: str) -> str| None:
    try:
        if isinstance(question, str):
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": question},
                ],
                stream=False
            )

            return response.choices[0].message.content
    except APIStatusError as e:
        print(f" openai error {e}")
    finally:
        return None