---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-prompt-template-create-generate-save/
title: Create and use a Vertex AI Prompt to generate text \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:48:24.991249+00:00
---

# Create and use a Vertex AI Prompt to generate text  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/generativeaionvertexai-prompt-template-create-generate-save/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Create and use a Vertex AI Prompt to generate text Stay organized with collections  Save and categorize content based on your preferences. 

This sample demonstrates how to create a Prompt instance, generate text using the assembled prompt, and save a version of the Prompt.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
    from vertexai.preview import [prompts](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.html)
    from vertexai.preview.prompts import [Prompt](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.Prompt.html)
    
    # from vertexai.generative_models import GenerationConfig, SafetySetting # Optional
    
    # Initialize vertexai
    [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest).init(project=PROJECT_ID, location="us-central1")
    
    # Create local Prompt
    local_prompt = Prompt(
        prompt_name="movie-critic",
        prompt_data="Compare the movies {movie1} and {movie2}.",
        variables=[
            {"movie1": "The Lion King", "movie2": "Frozen"},
            {"movie1": "Inception", "movie2": "Interstellar"},
        ],
        model_name="gemini-2.0-flash-001",
        system_instruction="You are a movie critic. Answer in a short sentence.",
        # generation_config=GenerationConfig, # Optional,
        # safety_settings=SafetySetting, # Optional,
    )
    
    # Generate content using the assembled prompt for each variable set.
    for i in range(len(local_prompt.variables)):
        response = local_prompt.[generate_content](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.generative_models.GenerativeModel.html#vertexai_preview_generative_models_GenerativeModel_generate_content)(
            contents=local_prompt.[assemble_contents](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.types.Prompt.html#vertexai__genai_types_Prompt_assemble_contents)(**local_prompt.variables[i])
        )
        print(response)
    
    # Save a version
    prompt1 = [prompts](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.prompts.html).create_version(prompt=local_prompt)
    
    print(prompt1)
    
    # Example response
    # Assembled prompt replacing: 1 instances of variable movie1, 1 instances of variable movie2
    # Assembled prompt replacing: 1 instances of variable movie1, 1 instances of variable movie2
    # Created prompt resource with id 12345678910.....
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=generativeaionvertexai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
