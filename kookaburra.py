from langchain.llms import OpenAI


def get_llm() -> OpenAI:
    print("Here2")
    return OpenAI(temperature=0.9)
