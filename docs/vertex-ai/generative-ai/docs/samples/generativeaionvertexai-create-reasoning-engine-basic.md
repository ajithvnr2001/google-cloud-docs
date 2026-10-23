---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-reasoning-engine-basic/
title: Build, test, and deploy a custom app on Reasoning Engine \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:50.546680+00:00
---

# Build, test, and deploy a custom app on Reasoning Engine  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-reasoning-engine-basic/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Build, test, and deploy a custom app on Reasoning Engine Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to build, test, and deploy a custom app on Reasoning Engine. It includes a local test of the app and the steps to deploy the app on the Reasoning Engine.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import reasoning_engines
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # staging_bucket = "gs://YOUR_BUCKET_NAME"
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
        project=PROJECT_ID, location="us-central1", staging_bucket=staging_bucket
    )
    
    class SimpleAdditionApp:
        def query(self, a: int, b: int) -> str:
            """Query the application.
            Args:
                a: The first input number
                b: The second input number
            Returns:
                int: The additional result.
            """
            return f"{int(a)} + {int(b)} is {int(a + b)}"
    
    # Locally test
    app = SimpleAdditionApp()
    app.query(a=1, b=2)
    
    # Create a remote app with Reasoning Engine.
    # This may take 1-2 minutes to finish.
    reasoning_engine = reasoning_engines.ReasoningEngine.create(
        SimpleAdditionApp(),
        display_name="Demo Addition App",
        description="A simple demo addition app",
        requirements=["cloudpickle==3"],
        extra_packages=[],
    )
    # Example response:
    # Using bucket YOUR_BUCKET_NAME
    # Writing to gs://YOUR_BUCKET_NAME/reasoning_engine/reasoning_engine.pkl
    # ...
    # ReasoningEngine created. Resource name: projects/123456789/locations/us-central1/reasoningEngines/123456
    # To use this ReasoningEngine in another session:
    # reasoning_engine = vertexai.preview.reasoning_engines.ReasoningEngine('projects/123456789/locations/...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
