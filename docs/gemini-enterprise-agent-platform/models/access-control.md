---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/access-control/
title: Access control \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:46:23.097305+00:00
---

# Access control  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/access-control/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Access control Stay organized with collections  Save and categorize content based on your preferences. 

To use the generative AI features on Gemini Enterprise Agent Platform, the principals (for example, users, groups, and [service accounts](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#service-agents)) in your project need to be granted the appropriate IAM role. You can also create custom roles to grant a user-defined set of permissions to a principal. This page shows you the applicable IAM roles to grant and the specific permissions needed for each operation so you can create custom roles.

## Predefined roles

You can grant the users or groups in your project one of the following predefined roles to give them access to the generative AI features on Gemini Enterprise Agent Platform:

  * [Gemini Enterprise Agent Platform Administrator (`roles/aiplatform.admin`)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.admin)
  * [Gemini Enterprise Agent Platform User (`roles/aiplatform.user`)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#aiplatform.user)



To learn more about Gemini Enterprise Agent Platform IAM roles, see [Gemini Enterprise Agent Platform access control with IAM](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control).

## Permissions

The following table maps generative AI operations to the permissions required for the operation. If you need fine-grained access control, you can refer to these mappings to create custom roles.

Operation | Permissions needed  
---|---  
Make prompt requests | 

  * `aiplatform.endpoints.predict`

  
Save, view, update, and delete prompts in Vertex AI Studio | 

  * `aiplatform.datasets.create`
  * `aiplatform.datasets.update`
  * `aiplatform.datasets.delete`
  * `aiplatform.datasets.list`
  * `aiplatform.datasets.get`

  
Model tuning | 

  * `aiplatform.pipelineJobs.*`
  * `aiplatform.customJobs.*`
  * `aiplatform.datasets.export`
  * `aiplatform.datasets.get`
  * `aiplatform.models.upload`
  * `aiplatform.models.get`
  * `aiplatform.endpoints.create`
  * `aiplatform.endpoints.get`
  * `aiplatform.endpoints.deploy`
  * `aiplatform.metadataStores.get`
  * `storage.objects.create`
  * `storage.objects.update`
  * `storage.objects.get`
  * `storage.objects.list`

  
  
To learn more about Gemini Enterprise Agent Platform IAM permissions, see [IAM permissions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/iam-permissions).

## What's next

Guide 

###  [ Enable Data Access audit logs ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/enable-audit-logs)

Enable Data Access audit logs in Agent Platform so that you can monitor usage of your model endpoints. 

Guide 

###  [ Control access with IAM ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control)

Learn how to use Identity and Access Management (IAM) to manage access to Agent Platform resources. 

Overview 

###  [ Introduction to tuning ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/start/get-started-with-gemini-3)

Learn how to tune a model by providing a training dataset that contains a set of examples of specific downstream tasks. 

Overview 

###  [ Responsible AI ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/responsible-ai)

Learn about some of the limitations to generative AI and recommended practices for using generative AI. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
