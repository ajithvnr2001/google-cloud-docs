---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/migrate-code/
title: Migrate from OpenAI SDK to Google Gen AI SDK \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:45:47.585568+00:00
---

# Migrate from OpenAI SDK to Google Gen AI SDK  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/migrate-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Migrate from OpenAI SDK to Google Gen AI SDK Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to migrate code designed for the OpenAI SDK to the Google Gen AI SDK to utilize Gemini models on Gemini Enterprise Agent Platform.

**Note:** If you prefer to continue using OpenAI libraries without rewriting your code, see [Using OpenAI libraries with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview).

## Migration Overview

The following notebook demonstrates a practical migration from the `openai` library to the `google-genai` library:

To see an example of migrating from OpenAI SDK to Google GenAI SDK, run the "Migrate OpenAI SDK code to Google GenAI SDK code" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/migration/migrate_from_openai_to_gemini.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/colab-enterprise-logo-32px.png)Open in Colab Enterprise](https://console.cloud.google.com/agent-platform/colab/import/https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fmigration%2Fmigrate_from_openai_to_gemini.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/vertex-ai-workbench-logo-32px.png)Open in Agent Platform Workbench](https://console.cloud.google.com/agent-platform/workbench/deploy-notebook?download_url=https%3A%2F%2Fraw.githubusercontent.com%2FGoogleCloudPlatform%2Fgenerative-ai%2Fmain%2Fmigration%2Fmigrate_from_openai_to_gemini.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/migration/migrate_from_openai_to_gemini.ipynb)

### API & Syntax Mapping

The following table compares the core components, methods, and parameters of the OpenAI SDK with the Google Gen AI SDK.

Feature | OpenAI SDK (`openai`) | Google Gen AI SDK (`google-genai`)  
---|---|---  
**Client Initialization** | `client = OpenAI(api_key=...)` | `client = genai.Client(vertexai=True, ...)`  
**Generation Method** | `client.chat.completions.create` | `client.models.generate_content`  
**Streaming Method** | `stream=True` (parameter) | `client.models.generate_content_stream` (method)  
**User Input** | `messages=[{"role": "user", "content": "..."}]` | `contents="..."` (str) or `contents=[...]` (list)  
**System Instructions** | `messages=[{"role": "system", "content": "..."}]` | `config=types.GenerateContentConfig(system_instruction=...)`  
**Response Access** | `response.choices[0].message.content` | `response.text`  
**Chat History** | Manual list management (`messages.append`) | `client.chats.create()` (Stateful object)  
**Max Tokens** | `max_tokens` | `max_output_tokens` (inside `config`)  
**Temperature** | `temperature` | `temperature` (inside `config`)  
**JSON Mode** | `response_format={"type": "json_object"}` | `response_mime_type="application/json"` (inside `config`)  
  
### Installation and Setup

Uninstall the OpenAI library and install the Google Gen AI SDK.
    
    
    pip install google-genai
    

### 2\. Authentication & Initialization

While OpenAI uses an API Key, Agent Platform uses [Identity and Access Management (IAM) credentials (Application Default Credentials)](https://docs.cloud.google.com/docs/authentication/application-default-credentials). You must explicitly define your Project ID and Location.

OpenAI SDK | Google Gen AI SDK  
---|---  
`
    
    
    from openai import OpenAI
    import os
    
    # Relies on OPENAI_API_KEY environment variable
    client = OpenAI()
            

` |  `
    
    
    from google import genai
    
    # Use vertexai=True to use Agent Platform
    client = genai.Client(
        vertexai=True,
        project='your-project-id',
        location='us-central1'
    )
            

`  
  
**Tip:** You can also set environment variables to initialize the client without arguments, similar to how the OpenAI client reads the API key from the environment. 

Set `GOOGLE_GENAI_USE_ENTERPRISE`, `GOOGLE_CLOUD_PROJECT` and `GOOGLE_CLOUD_LOCATION`, as shown:
    
    
    export GOOGLE_GENAI_USE_ENTERPRISE=true
    export GOOGLE_CLOUD_PROJECT='your-project-id'
    export GOOGLE_CLOUD_LOCATION='global'
    

Once configured, you can initialize the client without passing parameters:
    
    
    from google import genai
    
    client = genai.Client()
    

### Code Examples

The following code samples show the differences between the OpenAI SDK and Google Gen AI SDK for common tasks.

#### Single-turn text generation

The following code samples show how to generate text. Note that in the Google Gen AI SDK, system instructions are handled as a configuration parameter rather than a message role in the input list.

OpenAI SDK | Google Gen AI SDK  
---|---  
`
    
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain quantum physics."}
        ]
    )
    print(response.choices[0].message.content)
            

` |  `
    
    
    from google.genai import types
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain quantum physics.",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant."
        )
    )
    print(response.text)
            

`  
  
#### Text generation with parameters

The following code samples show the differences in defining configuration parameters. In the Google Gen AI SDK, parameters like `temperature`, `max_output_tokens` (previously `max_tokens`), and JSON formatting are grouped into a `GenerateContentConfig` object.

OpenAI SDK | Google Gen AI SDK  
---|---  
`
    
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "List 3 types of apples in JSON."}
        ],
        temperature=0.7,
        max_tokens=1000,
        response_format={"type": "json_object"}
    )
    
    print(response.choices[0].message.content)
            

` |  `
    
    
    from google.genai import types
    
    config = types.GenerateContentConfig(
        temperature=0.7,
        max_output_tokens=1000,
        response_mime_type="application/json"
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="List 3 types of apples in JSON.",
        config=config
    )
    
    print(response.text)
            

`  
  
#### Chat (Multi-turn)

The following code samples show the differences in managing chat history. Google Gen AI SDK simplifies this by providing a stateful `chat` object, whereas OpenAI requires manually appending messages to a list.

OpenAI SDK | Google Gen AI SDK  
---|---  
`
    
    
    # You must manually manage the list state
    messages = [{"role": "user", "content": "Hi"}]
    
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    
    # Append the response to history manually
    messages.append(response.choices[0].message)
    messages.append({"role": "user", "content": "Next question"})
    
    response2 = client.chat.completions.create(
        model="gpt-4",
        messages=messages
    )
    print(response2.choices[0].message.content)
            

` |  `
    
    
    # The SDK manages history for you
    chat = client.chats.create(
        model="gemini-2.5-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a helpful assistant."
        )
    )
    
    response1 = chat.send_message("Hi")
    print(response1.text)
    
    # History is retained automatically in the chat object
    response2 = chat.send_message("Next question")
    print(response2.text)
            

`  
  
#### Streaming

The following code samples show the differences in streaming responses. Google Gen AI SDK uses a specific method (`generate_content_stream`) rather than a boolean flag.

OpenAI SDK | Google Gen AI SDK  
---|---  
`
    
    
    stream = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Write a story."}],
        stream=True
    )
    
    for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="")
            

` |  `
    
    
    stream = client.models.generate_content_stream(
        model="gemini-2.5-flash",
        contents="Write a story."
    )
    
    for chunk in stream:
        print(chunk.text, end="")
            

`  
  
## What's next

  * Learn how to [Use OpenAI libraries with Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/migrate/openai/overview).
  * See code examples for [OpenAI compatibility](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/openai).
  * Get started with [Google Gen AI SDK quickstart](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
