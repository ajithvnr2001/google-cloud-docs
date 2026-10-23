---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-claude-3-tool-use/
title: Use function calling with Anthropic to enhance the capabilities of Claude \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:44.836948+00:00
---

# Use function calling with Anthropic to enhance the capabilities of Claude  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-claude-3-tool-use/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Use function calling with Anthropic to enhance the capabilities of Claude Stay organized with collections  Save and categorize content based on your preferences. 

Use function calling with Anthropic Claude to query external tools, such as the Google Places API. The sample calls the Text Search Places API directly from your Claude prompt to retrieve information about places based on a user's query.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Request predictions with Claude models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/partner-models/claude/use-claude)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    # TODO(developer): Vertex AI SDK - uncomment below & run
    # pip3 install --upgrade --user google-cloud-aiplatform
    # gcloud auth application-default login
    # pip3 install -U 'anthropic[vertex]'
    from anthropic import AnthropicVertex
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    
    client = AnthropicVertex(project_id=PROJECT_ID, region="us-east5")
    message = client.messages.create(
        model="claude-3-5-sonnet-v2@20241022",
        max_tokens=1024,
        tools=[
            {
                "name": "text_search_places_api",
                "description": "returns information about a set of places based on a string",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "textQuery": {
                            "type": "string",
                            "description": "The text string on which to search",
                        },
                        "priceLevels": {
                            "type": "array",
                            "description": "Price levels to query places, value can be one of [PRICE_LEVEL_INEXPENSIVE, PRICE_LEVEL_MODERATE, PRICE_LEVEL_EXPENSIVE, PRICE_LEVEL_VERY_EXPENSIVE]",
                        },
                        "openNow": {
                            "type": "boolean",
                            "description": "whether those places are open for business.",
                        },
                    },
                    "required": ["textQuery"],
                },
            }
        ],
        messages=[
            {
                "role": "user",
                "content": "What are some affordable and good Italian restaurants open now in San Francisco??",
            }
        ],
    )
    print(message.model_dump_json(indent=2))
    # Example response:
    # {
    #   "id": "msg_vrtx_018pk1ykbbxAYhyWUdP1bJoQ",
    #   "content": [
    #     {
    #       "text": "To answer your question about affordable and good Italian restaurants
    #       that are currently open in San Francisco....
    # ...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
