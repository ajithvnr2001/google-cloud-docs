---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-tune-code-generation-model/
title: Tune Code Generation Model \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:24.100926+00:00
---

# Tune Code Generation Model  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/samples/googlegenaisdk-tune-code-generation-model/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
  * [ Vertex AI Cookbook ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/cookbook)



#  Tune Code Generation Model Stay organized with collections  Save and categorize content based on your preferences. 

Tune a pre-trained code generation model.

## Code sample

### Python

Before trying this sample, follow the Python setup instructions in the [Vertex AI quickstart using client libraries](https://docs.cloud.google.com/vertex-ai/docs/start/client-libraries). For more information, see the [Vertex AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest). 

To authenticate to Vertex AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import os
    
    from google import genai
    
    # TODO (Developer) Set environment variables
    PROJECT_ID = os.getenv("GOOGLE_CLOUD_PROJECT")
    LOCATION_ID = os.getenv("LOCATION_ID", "us-central1")
    
    # Resource format: 'publishers/google/models/{model_id}'
    BASE_MODEL_RESOURCE = "publishers/google/models/gemini-2.5-flash"
    TRAINING_DATASET = (
        "gs://cloud-samples-data/ai-platform/generative_ai/gemini/text/sft_train_data.jsonl"
    )
    
    
    def tune_code_generation_model() -> genai.types.TuningJob:
        """Submits a supervised fine-tuning job for a Gemini model on code/text tasks."""
    
        client = genai.Client(
            enterprise=True,
            project=PROJECT_ID,
            location=LOCATION_ID,
        )
    
        tuning_job = client.tunings.tune(
            base_model=BASE_MODEL_RESOURCE,
            training_dataset=genai.types.TuningDataset(
                gcs_uri=TRAINING_DATASET,
            ),
            config=genai.types.CreateTuningJobConfig(
                tuned_model_display_name="tuned_gemini_code_model",
                epoch_count=2,
                learning_rate_multiplier=1.0,
            ),
        )
    
        print(f"Tuning job submitted successfully: {tuning_job.name}")
        print(f"Current State: {tuning_job.state}")
    
        return tuning_job
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=googlegenaisdk). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
