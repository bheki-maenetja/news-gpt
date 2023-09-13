# NewsGPT
NewsGPT is a web-based news application that uses OpenAI's GPT-4 model to glean additional insights from news articles.

## Getting Started
### Installation
- Clone this repository by running the terminal command `git clone git@github.com:bheki-maenetja/news-gpt.git`.
- In the root folder run the terminal command `pipenv shell`. Ensure that you have Python 3.9 installed on your device.
- In the root folder run the terminal command `pipenv install` to install all necessary packages and modules for the backend.
- Create an `.env` file to store your own keys for the OpenAI completions API and News API; assign these keys to `OPENAI_API_KEY` and `NEWS_API_KEY` respectively.
- To view the site locally run the terminal command `python app.py` and navigate to localhost:8050 in your web browser.

### Deployment
- You can view the deployed version of the site [here](https://news-gpt-production.up.railway.app/).

## Technologies Used
- Python 3.9
- Plotly/Dash
- CSS (incl. Bootstrap)
- Third-party APIs
  * [OpenAI (GPT-4)](https://openai.com/blog/openai-api/)
  * [News API](https://newsapi.org/)

## Overview
NewsGPT is a web-based news application powered by OpenAI's GPT-4 model. Designed to provide deeper insights from news articles, NewsGPT goes beyond simply displaying the news. The system analyses news headlines to offer users context, background, and a clearer understanding of the information. Users are able to glean insights from these headlines by utlising chatbots, creating summaries or opinionated editorials and generating word clouds.

### Headline Analysis
<figcaption>Users can use natural language queries to extract information and create text summaries in a various formats</figcaption>
<kbd>
<img src="/assets/analysisSection.png" width="100%" />
</kbd>

### Keywords
<figcaption>Users can generate word clouds to highlight key words and phrases in the day's news stories</figcaption>
<kbd>
<img src="/assets/keywordsSection.png" width="100%" />
</kbd>

### Editorial
<figcaption>Users can create heavily opinionated editorials based on the current news headlines</figcaption>
<kbd>
<img src="/assets/editorialSection.png" width="100%" />
</kbd>

### NewsBot
<figcaption>Users can interact with a chatbot tool that uses a corpus of over 2 million news articles to answer natural language queries</figcaption>
<kbd>
<img src="/assets/newsbotSection.gif" width="100%" />
</kbd>

## Development
This project is a purely frontend web application; it has no backend. The frontend was built using Dash and styled with regular CSS as well as the Bootstrap CSS framework. The system is hosted on a Linux cloud server from [Railway](https://railway.app/).

### User Interface
- Whilst the application logic (including the API calls to get news articles and use GPT-4) was written in “standard” python, the user interface was developed with a python library called Dash.
- Dash allows for the seamless integration of application logic with the user interface. The is done through special functions known as “callbacks”. Callbacks are a way of retrieving the values of UI components, such as the text inside of a form or the numerical value of a slider. These functions are automatically called whenever an input UI component's property changes, in order to update some property in another UI component (the output).
- NewsGPT uses Cascading Style Sheets (CSS) to style and properly lay out the system’s various UI components. Dash has a built-in integration that allows it to work with CSS files. The styling of the UI also makes use of [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/) – a library of CSS styles and custom UI components from the popular Bootstrap CSS framework.

### GPT-4
- As mentioned above, NewsGPT uses OpenAI's GPT-4 model to analyse news headlines. This is done through OpenAI's completions API and python client. Each time a user sends a chatbot message or creates a summary/editorial, a prompt is automatically generated and sent through the API; the output is then retrieved and rendered on the UI.
- Whilst GPT-4 is used to power both chatbots and the system's summary and editorial generator, it is not used for the creation of word clouds.
```
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
        err_str = f"Error: gpt_call -> {e}"
        if "rate limit" in err_str.lower():
            err_str = f"Error: gpt_call -> Rate limit reached. Please try again."
        return err_str
```

## Reflection
### Challenges
- There were no serious obstacles during the development of NewsGPT. This project was more of an exercise and small expansion of the skills I had developed while working on [LAME](https://github.com/bheki-maenetja/LAME-app/tree/master).

### Room for Improvement
- **Chatbot accuracy:** whilst the system does a serviceable job of answering basic natural language queries, it is still prone to providing wildly inaccurate information; this stems from the "hallucination" problem common in many LLMs. There are many solutions to this problem. Prompt construction can be improved by parsing and refining user queries to ensure more accurate results and that the model answers exactly what it has been asked. Fine-tuning the model on recent news articles is also an option. And finding ways to provide additional context in the prompts supplied to the model — such as pulling additional information about a topic from Wikipedia — may also improve the accuracy of the chatbots.

## Future Features
- **User accounts:** NewsGPT currently does not feature any authentication mechanism or user accounts. To make the system viable for serious personal and possible commercial use, NewsGPT will need to have some sort of authentication layer coupled with the provision of user accounts that can associate individual users with their preffered news publishers and categories of news. This will require the creation of a database and backend for the system.