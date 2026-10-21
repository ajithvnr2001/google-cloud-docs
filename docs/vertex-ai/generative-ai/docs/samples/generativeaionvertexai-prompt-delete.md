---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-prompt-delete/
title: Delete a prompt \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:39:44.284014+00:00
---

# Delete a prompt  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-prompt-delete/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Delete a prompt Stay organized with collections  Save and categorize content based on your preferences. 

This code sample demonstrates how to delete the specified prompt.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview.prompts import [Prompt](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.Prompt.html)
    from vertexai.preview import [prompts](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.html)
    
    # Initialize vertexai
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location="us-central1")
    
    # Create local Prompt
    prompt = Prompt(
        prompt_name="movie-critic",
        prompt_data="Compare the movies {movie1} and {movie2}.",
        variables=[
            {"movie1": "The Lion King", "movie2": "Frozen"},
            {"movie1": "Inception", "movie2": "Interstellar"},
        ],
        model_name="gemini-2.0-flash-001",
        system_instruction="You are a movie critic. Answer in a short sentence.",
    
    )
    # Save a version
    prompt1 = [prompts](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.html).create_version(prompt=prompt)
    prompt_id = prompt1.prompt_id
    
    # Delete prompt
    [prompts](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.html).delete(prompt_id=prompt_id)
    print(f"Deleted prompt with ID: {prompt_id}")
    
    # Example response:
    # Deleted prompt resource with id 12345678910

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
