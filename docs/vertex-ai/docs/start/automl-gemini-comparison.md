---
url: https://docs.cloud.google.com/vertex-ai/docs/start/automl-gemini-comparison/
title: Gemini for AutoML text users \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:28.994052+00:00
---

# Gemini for AutoML text users  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/start/automl-gemini-comparison/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Gemini for AutoML text users Stay organized with collections  Save and categorize content based on your preferences. 

[AutoML Text is deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). This page provides comparisons between AutoML Text and Gemini to help AutoML text users understand how to use Gemini.

Check the tables that apply to your use case, and review the changes that are likely to impact your workflow.

## General usage

These differences are applicable to all Gemini users.

Operation  |  AutoML text  |  Gemini  | Training data formats | You can use CSV or JSON Lines files, except for text entity extraction, to include inline text snippets or to reference documents that are of type `TXT`. Entity extraction supports only JSON Lines files. | You can only use JSON Line files. Each line in the file should represent a [single training example](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-supervised-tuning-about#example_single_turn). You can download a [sample dataset](https://storage.googleapis.com/cloud-samples-data/vertex-ai/model-evaluation/gemini_pro_peft_train_sample.jsonl) for fine-tuning Gemini models. Files should be stored in Cloud Storage.  
---|---|---  
Dataset annotation |  Annotations are grouped together as an `AnnotationSet` object. You can use different annotation sets with the same dataset.  | Dataset annotations are not applicable with Gemini.  
Dataset import | You specify ML use values in an optional column for CSV, in the same row as the data; or as a tag in JSON Lines in the same JSON object as the data. If you don't specify ML use values, your data is split automatically for training, testing, and validation.  
For sentiment analysis, CSV files must include the sentiment max value in the last column of each row. | You need to have two separate JSONL files, one for training and one for validation. The validation file is optional. The validation file should have 10-256 examples.  
Storage costs |  When you create a dataset, your data is loaded into Cloud Storage in your project. You are charged for this storage. [Learn more](https://docs.cloud.google.com/vertex-ai/pricing#cloud-storage).  | When you create a dataset, your data is loaded into Cloud Storage in your project. You are charged for this storage. [Learn more](https://docs.cloud.google.com/vertex-ai/pricing#cloud-storage)  
Data labeling |  You provide labeling instructions by using a URL. Annotations are part of the `Dataset` object and can't be manipulated by using the API.  | Data labeling is not applicable with Gemini.  
Model deployment |  You create an _Endpoint_ object, which provides resources for serving online inferences. You then deploy the model to the endpoint. To request inferences, you call the [`predict()`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) method.  | After fine-tuning Gemini, the model is stored in [Vertex AI Model Registry](https://docs.cloud.google.com/vertex-ai/docs/model-registry/introduction), and an Endpoint is automatically created. Online inferences from the tuned model [can be requested](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#test_the_tuned_model_with_a_prompt) using the Python SDK, REST API, or the console. You request inferences by first fetching the tuned endpoint and then using the `generate_content()` method.   
Using project number or project ID |  Both `project-number` and `project-id` work in Vertex AI.  | Gemini uses `project-id`.  
Confidence scores |  AutoML text supports confidence scores.  | Gemini doesn't support confidence scores.  
  
## API users

For detailed information about the API, see the [Vertex AI Generative AI Tuning API reference documentation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/tuning).

Operation or entity  |  AutoML text  |  Gemini  | Model Creation |  You create a `TrainingPipeline` object, which returns a training job.  | You create a [Supervised Fine Tuning job](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#create_a_text_model_supervised_tuning_job) which returns the tuning job.  
---|---|---  
Using the client library | There are different API clients for each API resource. | You can create a Supervised Fine-tuning Job for Gemini using the Python SDK, REST API or the Console.  
Requesting inferences |  You request inferences by calling the [`predict()`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.endpoints/predict) method on the Endpoint resource.  | You request inferences by first fetching the tuned endpoint and then using the [`generate_content`](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-use-supervised-tuning#test_the_tuned_model_with_a_prompt) method.   
Online inference endpoint | In the following, replace REGION with the region that your inference model is in.  
`REGION-aiplatform.googleapis.com`. For example:  
`us-central1-aiplatform.googleapis.com` | In the following, replace TUNING_JOB_REGION with the region where your tuning job runs.  
`TUNING_JOB_REGION-aiplatform.googleapis.com`. For example:  
`us-central1-aiplatform.googleapis.com`  
Schema and definition files |  Some request and response fields are defined in schema and definition files. Data formats are defined using predefined schema files. This enables flexibility for the API and data formats.  | The [request body](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#request), [model parameters](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#parameters), and [response body](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#response) are the same as with the untuned Gemini models. See [sample requests](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#sample-requests).  
Hostname | `aiplatform.googleapis.com` | `aiplatform.googleapis.com`  
Regional hostname | Required. For example:  
`us-central1-aiplatform.googleapis.com` | Required. For example:  
`us-central1-aiplatform.googleapis.com`  
  
## What's next

  * To get started with tuning, see [Model tuning for Gemini text models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune_gemini/tune-gemini-learn)

  * [Migrate from AutoML text to Gemini](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-gemini).

  * [Introduction to tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/tune-models).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
