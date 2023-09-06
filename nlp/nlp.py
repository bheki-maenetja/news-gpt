# Third-Party Imports
import openai
from wordcloud import WordCloud

# Standard Imports
import os

# Formatting Inputs and Outputs
def build_headline_list(headlines):
    return "+".join(
        h["title"]
        if h["title"] is not None
        else "UNTITLED" 
        for _, h in headlines.iterrows()
    )

# Building prompts
def build_headline_bot_prompt(headline_list, user_prompt):
    main_prompt = "You will be given a user-generated prompt and a list of news headline. Each headline is separated by a '+' symbol. Answer the prompt using the list of headlines. YOU MAY ONLY USE THE HEADLINES FOR CONTEXT!\n\n"
    main_prompt += f"Prompt: {user_prompt}\n\n"
    main_prompt += f"Headlines: {headline_list}"
    return main_prompt

def build_summary_prompt(headline_list, sum_format):
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

def build_editorial_prompt(headline_list, opinion_choice):
    main_prompt = "Write an editorial based on the following set of news headlines. Each headline is separated by a '+' symbol. The editorial should "
    opinions = [
        "be extremely far left.",
        "lean heavily progressive.",
        "be liberal or centre-left.",
        "be neutral/centrist.",
        "be conservative or centre-right.",
        "lean heavily right wing.",
        "be extremely far right."
    ]

    main_prompt += opinions[opinion_choice + 3]
    main_prompt += f" Headlines: {headline_list}"
    return main_prompt

# GPT-4 API Call
def gpt_call(prompt):
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
        return f"gpt_call -> {e}"

# Summarisation
def summarise_headlines(headlines, sum_format):
    headline_list = build_headline_list(headlines)
    prompt = build_summary_prompt(headline_list, sum_format)
    summary = gpt_call(prompt)
    return summary

# Chatbots
def headline_chatbot(headlines, prompt):
    headline_list = build_headline_list(headlines)
    prompt = build_headline_bot_prompt(headline_list, prompt)
    message = gpt_call(prompt)
    return message

# Word Cloud
def get_word_cloud(headlines):
    words = build_headline_list(headlines)
    word_cloud = WordCloud(
        width=1000,
        height=1000,
        background_color="#fdf0d5",
    ).generate(words)
    word_cloud_img = word_cloud.to_image()
    return word_cloud_img

# Editorial
def get_headline_editorial(headlines, opinion_choice):
    headline_list = build_headline_list(headlines)
    prompt = build_editorial_prompt(headline_list, opinion_choice)
    editorial = gpt_call(prompt)
    return editorial
