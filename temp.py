import openai

# Set your OpenAI API key
openai.api_key = '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'

def code_converter(source_code, source_language, target_language, max_tokens=150):
    prompt = f"convert the following code into {target_language} code:\n\n {source_code}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a Python code."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=max_tokens,
        stop=["\n```"]
    )
    converted_code = response.choices[0].message['content']
    return converted_code

# Example usage:
source_code = """
def greet():
    print("Hello, world!")

greet()
"""
source_language = "python"
target_language = "java"

converted_code = code_converter(source_code, source_language, target_language)
print("Converted code:")
print(converted_code)
