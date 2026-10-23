---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-chat-completions-function-calling-config/
title: Use function calling with Gemini using OpenAI SDK \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:59.843430+00:00
---

# Use function calling with Gemini using OpenAI SDK  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-gemini-chat-completions-function-calling-config/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Use function calling with Gemini using OpenAI SDK Stay organized with collections  Save and categorize content based on your preferences. 

This code sample demonstrates how to do function calling in Gemini using Chat Completions API in the OpenAI SDK.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Function calling reference](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/function-calling)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    import openai
    
    from google.auth import default, transport
    
    # TODO(developer): Update & uncomment below line
    # PROJECT_ID = "your-project-id"
    location = "us-central1"
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location=location)
    
    # Programmatically get an access token
    credentials, _ = default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    auth_request = transport.[requests](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateResourceRequirementsDict.html#vertexai__genai_types_SandboxEnvironmentTemplateResourceRequirementsDict_requests).Request()
    credentials.refresh(auth_request)
    
    # OpenAI Client
    client = openai.OpenAI(
        base_url=f"https://{location}-aiplatform.googleapis.com/v1beta1/projects/{PROJECT_ID}/locations/{location}/endpoints/openapi",
        api_key=credentials.token,
    )
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA or a zip code e.g. 95616",
                        },
                    },
                    "required": ["location"],
                },
            },
        }
    ]
    
    messages = []
    messages.append(
        {
            "role": "system",
            "content": "Don't make assumptions about what values to plug into functions. Ask for clarification if a user request is ambiguous.",
        }
    )
    messages.append({"role": "user", "content": "What is the weather in Boston, MA?"})
    
    response = client.chat.completions.create(
        model="google/gemini-2.0-flash-001",
        messages=messages,
        tools=tools,
        tool_choice="auto",
    )
    
    print("Function:", response.choices[0].message.tool_calls[0].[id](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.StructuredMemorySchemaConfigDict.html#vertexai__genai_types_StructuredMemorySchemaConfigDict_id))
    print("Arguments:", response.choices[0].message.tool_calls[0].function.[arguments](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.SchemaPromptInstancePromptExecutionDict.html#vertexai__genai_types_SchemaPromptInstancePromptExecutionDict_arguments))
    # Example response:
    # Function: get_current_weather
    # Arguments: {"location":"Boston"}

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
