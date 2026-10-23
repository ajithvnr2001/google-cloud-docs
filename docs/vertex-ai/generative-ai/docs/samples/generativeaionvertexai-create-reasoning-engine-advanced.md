---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-reasoning-engine-advanced/
title: Build, test, and deploy a Langchain chatbot on Reasoning Engine \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:54.373540+00:00
---

# Build, test, and deploy a Langchain chatbot on Reasoning Engine  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-create-reasoning-engine-advanced/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Build, test, and deploy a Langchain chatbot on Reasoning Engine Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to build, test, and deploy a Langchain chatbot on Reasoning Engine.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import reasoning_engines
    
    # TODO(developer): Update and un-comment below lines
    # PROJECT_ID = "your-project-id"
    # staging_bucket = "gs://YOUR_BUCKET_NAME"
    
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(
        project=PROJECT_ID, location="us-central1", staging_bucket=staging_bucket
    )
    
    class LangchainApp:
        def __init__(self, project: str, location: str) -> None:
            self.project_id = project
            self.location = location
    
        def set_up(self) -> None:
            from langchain_core.prompts import ChatPromptTemplate
            from langchain_google_vertexai import ChatVertexAI
    
            system = (
                "You are a helpful assistant that answers questions "
                "about Google Cloud."
            )
            human = "{text}"
            prompt = ChatPromptTemplate.from_messages(
                [("system", system), ("human", human)]
            )
            chat = ChatVertexAI(project=self.project_id, location=self.location)
            self.chain = prompt | chat
    
        def query(self, question: str) -> Union[str, List[Union[str, Dict]]]:
            """Query the application.
            Args:
                question: The user prompt.
            Returns:
                str: The LLM response.
            """
            return self.chain.invoke({"text": question}).content
    
    # Locally test
    app = LangchainApp(project=PROJECT_ID, location="us-central1")
    app.set_up()
    print(app.query("What is Vertex AI?"))
    
    # Create a remote app with Reasoning Engine
    # Deployment of the app should take a few minutes to complete.
    reasoning_engine = reasoning_engines.ReasoningEngine.create(
        LangchainApp(project=PROJECT_ID, location="us-central1"),
        requirements=[
            "google-cloud-aiplatform[langchain,reasoningengine]",
            "cloudpickle==3.0.0",
            "pydantic==2.7.4",
        ],
        display_name="Demo LangChain App",
        description="This is a simple LangChain app.",
        # sys_version="3.10",  # Optional
        extra_packages=[],
    )
    # Example response:
    # Model_name will become a required arg for VertexAIEmbeddings starting...
    # ...
    # Create ReasoningEngine backing LRO: projects/123456789/locations/us-central1/reasoningEngines/...
    # ReasoningEngine created. Resource name: projects/123456789/locations/us-central1/reasoningEngines/...
    # ...
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
