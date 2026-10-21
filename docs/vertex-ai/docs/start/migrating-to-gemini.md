---
url: https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-gemini/
title: Migrate to Gemini from AutoML text \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:31:28.379215+00:00
---

# Migrate to Gemini from AutoML text  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/start/migrating-to-gemini/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Migrate to Gemini from AutoML text Stay organized with collections  Save and categorize content based on your preferences. 

Gemini is a family of generative AI models developed by Google that is designed for multimodal use cases. If you haven't used Gemini models on Vertex AI before, see the [Generative AI introduction](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview).

Key advantages of Gemini include the following:

  * **Enhanced performance** : The latest large language models (LLMs), such as Gemini Flash 1.5, demonstrate better understanding across a range of natural language tasks than the AutoML text model. For more information, see the publicly available [technical report](https://arxiv.org/pdf/2403.05530) from the Gemini team.

  * **Flexibility** : Gemini allows for both prompting (quick adaptation) and fine-tuning (deeper customization), catering to different project needs. This flexibility allows for rapid prototyping, testing, and deployment using prompting, with the option to fine-tune the Gemini model weights for optimal performance on specific tasks. Vertex AI offers both console-based fine-tuning and SDK and API options for programmatic control.

  * **Multipurpose and multimodal capabilities** : Gemini offers the ability to process text, images, and other modalities. This approach enables consistent use of a single format and model across various tasks. This flexibility allows the process to be easily adapted for different applications, streamlining and accelerating development efforts.




Gemini supports most features available in AutoML text. However, there are [differences](https://docs.cloud.google.com/vertex-ai/docs/start/automl-gemini-comparison), and the client libraries don't support client integration backward compatibility. In other words, you must plan to migrate your resources to benefit from Gemini features.

If you are planning a new project, you should build your code, job, dataset, or model with Gemini. This lets you take advantage of the new features and service improvements as they become available.

## Recommended steps for migrating to Gemini

**Note:** AutoML Text is no longer supported.

Use the following recommended steps to update your existing code, jobs, datasets, and models from AutoML text to Gemini.

  1. Read about the major differences between Gemini and AutoML text at [Gemini for AutoML text users](https://docs.cloud.google.com/vertex-ai/docs/start/automl-gemini-comparison).

  2. Review any potential changes in pricing (see Gemini migration pricing).

  3. Take inventory of your Google Cloud projects, code, jobs, datasets, models, and users with access to AutoML text. Use this information to determine which resources to migrate and ensure that the correct users have access to the migrated resources.

  4. Review any changes to IAM roles, and then update service accounts and authentication for your resources.

  5. Migrate your resources using either of these two methods:

     * [Prompting](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-tuning#gemini-prompts)

     * [Fine-tuning](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini-tuning#fine-tuning-gemini)

  6. View the [locations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations) available for Gemini.

  7. Identify usage of AutoML text APIs to help determine which of your applications use them and to identify the method calls that you want to migrate.

  8. Update your applications and workflows to use Gemini.

  9. Plan your request quota monitoring. See [Quotas and limits](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/quotas).




## Gemini migration pricing

Migration is free. After migration, legacy resources are still available to use in AutoML text until the service shuts down in June 2025. To avoid unnecessary costs, shut down or delete legacy resources after you have verified that your objects have migrated successfully.

## Gemini pricing compared to AutoML text pricing

Gemini pricing is generally cheaper compared to equivalent tasks in AutoML text. Gemini pricing is determined by whether you're using the model for prompt engineering only, fine-tuning only, or a combination of both. For more information, you can compare [AutoML text pricing](https://cloud.google.com/vertex-ai/pricing#automl_models) with [Gemini pricing](https://docs.cloud.google.com/vertex-ai/generative-ai/pricing).

For entity extraction models, consider that the model serving output may be higher as the output is the complete structured data.

## Identify usage of AutoML text APIs

You can determine which of your applications use AutoML APIs, as well as which methods they are using. Use this information to help determine whether these API calls need to be migrated to Gemini:

  * For each of your projects, go to the [APIs & Services Dashboard](https://console.cloud.google.com/apis/dashboard) to see a list of which products' API the project uses. To learn more, see [Monitoring API usage](https://docs.cloud.google.com/apis/docs/monitoring).

  * If enabled, you can check the audit logs created by [AutoML text](https://docs.cloud.google.com/vertex-ai/docs/general/audit-logging) as part of [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

  * To see usage of specific AutoML text methods, go to the [AutoML text Metrics page](https://console.cloud.google.com/apis/api/aiplatform.googleapis.com/metrics).




## Manage changes to IAM roles and permissions

Vertex AI provides the following Identity and Access Management (IAM) roles:

  * `aiplatform.admin`
  * `aiplatform.user`
  * `aiplatform.viewer`



Using Vertex AI datasets is no longer required. Data for fine-tuning in Gemini can only be stored in Cloud Storage.

For more information on IAM roles, see [Access control](https://docs.cloud.google.com/vertex-ai/docs/general/access-control).

## What's next

  * Read [Introduction to tuning](https://docs.cloud.google.com/vertex-ai/docs/start/migrating-applications) in Gemini.

  * See [Gemini for AutoML text users](https://docs.cloud.google.com/vertex-ai/docs/start/automl-gemini-comparison) for a comparison of Gemini and AutoML text.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
