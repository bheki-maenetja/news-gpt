# Third-Party Imports
import openai

# Standard Imports
import os

# Formatting Inputs and Outputs
def build_headline_list(headlines):
    return "+".join(h["title"] for _, h in headlines.iterrows())

# Building prompts
def build_prompt(headline_list, sum_format):
    main_prompt = "Summarise the following list of news headlines. Each headline is separated by a '+' symbol. The summary should be in the form of "
    
    format_prompt = {
        "1-para": "a single paragraph.",
        "multi-para": "2 or more paragraphs.",
        "s-essay": "a short essay (at least 500 words).",
        "l-essay": "a long essay (at least 1000 words).",
        "s-list": "a bullet-point list. The list must only have between 2 and 5 points.",
        "l-list": "a bullet-point list. The list must only have between 6 and 10 points.",
        "haiku": "a haiku.",
        "sonnet": "a sonnet.",
        "limerick": "a limerick.",
        "rap": "a rap.",
        "shakespeare": "a shakespearean poem or play."
    }[sum_format]

    main_prompt += format_prompt
    main_prompt += f" Headlines: {headline_list}"
    return main_prompt

# Summarisation
def summarise_headlines(headlines, sum_format):
    headline_list = build_headline_list(headlines)
    prompt = build_prompt(headline_list, sum_format)
    summary = gpt_summary(prompt)
    return summary

def gpt_summary(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    messages = [
        {"role": "user", "content": prompt},
    ]

    try:
        res = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages,
            temperature=0,
            max_tokens=6000,
        )

        summary = res.choices[0].message.content
        return summary
    except Exception as e:
        return f"gpt_summary -> {e}"