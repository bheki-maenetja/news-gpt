# Third-Party Imports
import openai

# Standard Imports
import os

# Formatting Inputs and Outputs

# Building prompts
def build_prompt(headlines, sum_format):
    main_prompt = "Summarise the following list of news headlines. Each headline is separated by a '+' symbol. The summary should be in the form of "
    
    format_prompt = {
        "1-para": "a single paragraph.",
        "multi-para": "2 or more paragraphs.",
        "s-essay": "a short essay (at least 500 words).",
        "l-essay": "a long essay (at least 1000 words).",
        "s-list": "a bullet-point list of between 2 and 5 points.",
        "l-list": "a bullet-point list of between 6 and 10 points.",
        "haiku": "a haiku.",
        "rap": "a rap.",
        "shakespeare": "a shakespearean poem or play."
    }[sum_format]

    main_prompt += format_prompt
    main_prompt += f" Headlines: {headlines}"
    return main_prompt

# Summarisation
def summarise_headlines(headlines, sum_format):
    prompt = build_prompt(headlines, sum_format)
    print(prompt)