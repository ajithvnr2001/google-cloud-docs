---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-maas/
title: Use open models using Model as a Service (MaaS) \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:42:15.285746+00:00
---

# Use open models using Model as a Service (MaaS)  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-maas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Use open models using Model as a Service (MaaS) Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to use open models through Model as a Service (MaaS) on Gemini Enterprise Agent Platform. MaaS provides serverless access to selected partner and open-source models, eliminating the need to provision or manage infrastructure.

[Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) is a centralized library of AI and ML models from Google, Google Partners, and open models (open-weight and open-source), including MaaS models. Model Garden provides multiple ways to deploy [available models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-garden/explore-models) on Gemini Enterprise Agent Platform, including [models from Hugging Face](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-hugging-face-models).

For more information about MaaS, see the [partner models documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/use-partner-models).

## Before you begin

To use MaaS models, you must enable the Agent Platform API in your Google Cloud project.
    
    
    gcloud services enable aiplatform.googleapis.com
    

## Enable the model's API

Before you can use a MaaS model, you must enable its API. To do this, go to the model page in Model Garden. Some models available through MaaS are also available for self-deployment. The Model Garden model cards for both offerings differ. The MaaS model card includes **API Service** in its name.

## Call the model using the Google Gen AI SDK for Python

The following example calls the Llama 3.3 model using the Google Gen AI SDK for Python.
    
    
    from google import genai
    from google.genai import types
    
    PROJECT_ID="PROJECT_ID"
    LOCATION="LOCATION"
    MODEL="meta/llama-3.3-70b-instruct-maas"  # The model ID from Model Garden with "API Service"
    
    # Define the prompt to send to the model.
    prompt = "What is the distance between earth and moon?"
    
    # Initialize the Google Gen AI SDK client.
    client = genai.Client(
        vertexai=True,
        project=PROJECT_ID,
        location=LOCATION,
    )
    
    # Prepare the content for the chat.
    contents: types.ContentListUnion = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt)
            ]
        )
    ]
    
    # Configure generation parameters.
    generate_content_config = types.GenerateContentConfig(
        temperature = 0,
        top_p = 0,
        max_output_tokens = 4096,
    )
    
    try:
        # Create a chat instance with the specified model.
        chat = client.chats.create(model=MODEL)
        # Send the message and print the response.
        response = chat.send_message(contents)
        print(response.text)
    except Exception as e:
        print(f"{MODEL} call failed due to {e}")
    

## What's next

  * [Choose an open model serving option](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/choose-serving-option)
  * [Deploy open models from Model Garden](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-model-garden)
  * [Deploy open models with prebuilt containers](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/use-prebuilt-containers)
  * [Deploy open models with a custom vLLM container](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/open-models/deploy-custom-vllm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
