---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-extension/
title: Create a code interpreter extension \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:06.617274+00:00
---

# Create a code interpreter extension  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-extension/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Create a code interpreter extension Stay organized with collections  Save and categorize content based on your preferences. 

Create a code interpreter extension from the prebuilt extensions by Google.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Extensions API](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/extension)



## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest)
    from vertexai.preview import extensions
    
    # TODO(developer): Update and un-comment below line
    # PROJECT_ID = "your-project-id"
    [vertexai](https://docs.cloud.google.com/python/docs/reference/vertexai/latest).init(project=PROJECT_ID, location="us-central1")
    
    extension = extensions.Extension.create(
        display_name="Code Interpreter",
        description="This extension generates and executes code in the specified language",
        manifest={
            "name": "code_interpreter_tool",
            "description": "Google Code Interpreter Extension",
            "api_spec": {
                "open_api_gcs_uri": "gs://vertex-extension-public/code_interpreter.yaml"
            },
            "auth_config": {
                "google_service_account_config": {},
                "auth_type": "GOOGLE_SERVICE_ACCOUNT_AUTH",
            },
        },
    )
    print(extension.resource_name)
    # Example response:
    # projects/123456789012/locations/us-central1/extensions/12345678901234567
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
