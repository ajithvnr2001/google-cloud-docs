---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/quick-start/
title: Quick start: Reinforcement learning fine-tuning using the API \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:09.680015+00:00
---

# Quick start: Reinforcement learning fine-tuning using the API  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/quick-start/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Quick start: Reinforcement learning fine-tuning using the API Stay organized with collections  Save and categorize content based on your preferences. 

This product is a Pre-GA offering, subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1), the "Agentic AI Services" terms in the [Service Specific Terms](https://cloud.google.com/terms/service-terms#1), and the [Additional Terms for Generative AI Preview Products](https://cloud.google.com/trustedtester/aitos). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

These Pre-GA products are in various stages of internal testing and review. As such, **do not use proprietary, sensitive, or other confidential data with these products**. These products are made available to Customers solely for limited testing and evaluation, and may not be used for commercial or production purposes. 

This page walks you through the end-to-end workflow for reinforcement learning fine-tuning of Gemini models by using the Agent Platform API: creating a tuning job, checking its status, retrieving the tuned-model endpoint, and running inference against it. To complete these tasks in the Google Cloud console, see the [Google Cloud console quick start](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/quick-start-console).

Before you begin, see [About reinforcement learning fine-tuning](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning) for an overview of the feature, supported models, and supported regions.

## Create a reinforcement learning fine-tuning job

A reinforcement learning fine-tuning job is created by sending a `POST` request to the [`tuningJobs.create`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/create) endpoint. For the full request schema and all configurable fields, see the [Reinforcement learning fine-tuning job](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job) page.

The examples on this page use `us-central1` as the tuning region. The resulting tuned model is served from the `us` multi-region endpoint. For the full list of supported tuning and serving regions, see the [Supported models and regions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning#supported-models-and-regions) section.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "Content-Type: application/json" \
      "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/us-central1/tuningJobs" \
      -d \
      $'{
        "tunedModelDisplayName": "dai-image-test",
        "baseModel": "gemini-3.5-flash",
        "reinforcementTuningSpec": {
          "trainingDatasetUri": "gs://path/to/my/training_dataset.jsonl",
          "validationDatasetUri": "gs://path/to/my/eval_dataset.jsonl",
          "hyperParameters": {
            "epochCount":15,
            "learningRateMultiplier":1.0,
            "samplesPerPrompt":16,
            "adapterSize":"ADAPTER_SIZE_SIXTEEN",
            "maxOutputTokens":32768,
            "batchSize":32,
            "evaluateInterval":5,
            "checkpointInterval":5,
            "thinkingLevel":"HIGH"
          },
          "singleRewardConfig": {
            "rewardName": "my_reward_function_name",
            "parseResponseConfig": {"parseType":"IDENTITY"},
            "cloudRunRewardScorer": {
              "cloudRunUri":"https://my.cloud.run.uri"
            }
          }
        }
      }'
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.

**Note:** Only the `v1beta1` API version is supported for reinforcement learning fine-tuning.

## Check the reinforcement learning fine-tuning job status

You can monitor the progress, performance, and quality of a running reinforcement learning fine-tuning job in the Google Cloud console on the [**Models > Tuning**](https://console.cloud.google.com/agent-platform/tuning) page. Each tuning job has a dedicated monitoring view that surfaces the underlying tuning status with charts for training and evaluation rewards, generation length, and other tuning metrics. For the full list of emitted metrics and how to interpret them, see the [Metrics and monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/job-status-metrics-monitoring) page.

### Training time

Training time is affected by the following factors:

  * **Training and validation dataset size.** For details, see the [Tuning dataset](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/tuning-dataset) page.
  * **Hyperparameters** — including `samplesPerPrompt`, batch size, epoch count, and learning rate multiplier. For details, see the [Hyperparameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/hyperparameters) page.



Depending on your setup, a Gemini reinforcement learning fine-tuning job can run for hours to days.

## Get the tuned-model endpoint

After the tuning job reaches `JOB_STATE_SUCCEEDED`, retrieve the deployed tuned-model endpoint by issuing a [`tuningJobs.get`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.tuningJobs/get) request and reading the `tunedModel.endpoint` field of the response.
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      "https://us-central1-aiplatform.googleapis.com/v1beta1/projects/PROJECT_ID/locations/us-central1/tuningJobs/TUNING_JOB_ID"
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.
  * TUNING_JOB_ID: The ID of the tuning job.



Example response (abbreviated):
    
    
    {
      "name": "projects/{PROJECT_ID}/locations/us-central1/tuningJobs/{TUNING_JOB_ID}",
      "tunedModelDisplayName": "my-rl-tuned-model",
      "state": "JOB_STATE_SUCCEEDED",
      "tunedModel": {
        "model": "projects/{PROJECT_ID}/locations/us-central1/models/{MODEL_ID}",
        "endpoint": "projects/{PROJECT_ID}/locations/us/endpoints/{ENDPOINT_ID}"
      },
      "reinforcementTuningSpec": { ... }
    }
    

Once the tuning job succeeds, `endpoint` from the last checkpoint is shown in the response.

## Run inference on the tuned-model endpoint

The tuned model serves predictions through the standard `generateContent` API on the returned endpoint. If the tuning job ran in `us-central1`, the tuned model is served from the `us` multi-region endpoint.
    
    
    curl -X POST \
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
      -H "Content-Type: application/json" \
      "https://aiplatform.us.rep.googleapis.com/v1beta1/projects/PROJECT_ID/locations/us/endpoints/ENDPOINT_ID:generateContent" \
      -d \
      $'{
        "contents": [
          {
            "role": "user",
            "parts": [
              { "text": "Why is the sky blue?" }
            ]
          }
        ]
      }'
    

Replace the following:

  * PROJECT_ID: Your Google Cloud project ID.
  * ENDPOINT_ID: The endpoint ID returned in the `tunedModel.endpoint` field of the `GetTuningJob` response.



## What's next

  * Learn more about [reinforcement learning fine-tuning jobs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job).
  * Explore supported [reward functions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/reward-functions).
  * Configure [hyperparameters](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/hyperparameters) for reinforcement learning.
  * Learn how to track [metrics and monitoring](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/reinforcement-tuning-job/job-status-metrics-monitoring).
  * Try the [Google Cloud console quick start](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning/reinforcement-tuning/quick-start-console) to create tuning jobs by using the Google Cloud console.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
