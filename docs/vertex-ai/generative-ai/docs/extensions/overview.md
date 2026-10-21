---
url: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview/
title: Extensions overview \u00a0|\u00a0 Generative AI on Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:57.278306+00:00
---

# Extensions overview  |  Generative AI on Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/overview/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)
  * [ Generative AI on Vertex AI ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)



Send feedback 

#  Extensions overview Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Extensions has been deprecated as of May 26, 2026. After November 26, 2026, Vertex AI Extensions will be shut down and no longer function. For equivalent functionality, see the [Extensions migration guide](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/migrate). 

**Preview**

Vertex AI Extensions is a Preview offering, subject to the "Pre-GA Offerings Terms" of the [Google Cloud Service Specific Terms](https://cloud.google.com/terms/service-terms). Pre-GA products and features may have limited support, and changes to pre-GA products and features may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages). Further, by using Vertex AI Extensions, you agree to the Generative AI Preview [terms and conditions](https://cloud.google.com/trustedtester/aitos) ("Preview Terms"). 

A Vertex AI [`extension`](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1beta1/projects.locations.extensions) is a structured API wrapper that connects a model to an API for processing real-time data or performing real-world actions.

The difference between Extensions and [Functions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling) is in the execution of the _Tool_. Extensions are automatically executed by Vertex AI. Whereas functions must be [manually executed by the user or client](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/multimodal/function-calling#invoke-api).

To streamline the extension creation process, we provide prebuilt _Extensions by Google_ for common use cases, such as [code interpretation](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/code-interpreter) and [Vertex AI Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/vertex-ai-search). If your use case doesn't align with these templates, you can create your own [custom extension](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/create-extension).

## Use-cases and benefits

The following are some possible extensions use cases:

  * Generate and run code. 
  * Query websites and synthesize information. 
  * Answer questions based on information within a collection of enterprise-specific data. 
  * Query and analyze datastores. 



Vertex AI extensions provide the following benefits:

  * **Enterprise controls** : [Identity and Access Management (IAM)](https://cloud.google.com/iam) permissions and security controls.
  * **Data security** : Contractual agreements that your private data won't be leaked or used in model training
  * **Performance agreements** : Contractual agreements that the platform delivers specific features and uptimes.
  * **Private extensions** : Authorized users in your organization or a trusted partner can use extensions to access sensitive internal data and actions, such as searching internal knowledge bases or completing HR actions.
  * **Google product integrations** : Integration with Google products like Agent Search, BigQuery and specialized models.



## Extensions by Google

Google provides the following prebuilt extensions:

  * [Code Interpreter](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/code-interpreter)
  * [Vertex AI Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/vertex-ai-search)



## What's next

  * [Create, register, and run extensions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/create-extension).
  * [Register and use Google-provided extensions](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/extensions/google-extensions)
  * [Use Reasoning Engine](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/overview). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
