---
url: https://docs.cloud.google.com/model-armor/access-control/service-accounts/
title: Model Armor service accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:34.665667+00:00
---

# Model Armor service accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/access-control/service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Guides ](https://docs.cloud.google.com/model-armor/overview)



Send feedback 

#  Model Armor service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the service accounts that are relevant to Model Armor.

## User-managed service accounts

A [service account](https://docs.cloud.google.com/iam/docs/service-account-overview) is a special type of account designed to provide an identity for non-human workloads, such as applications running on Compute Engine, virtual machines, containerized apps, or other automated services. These accounts enable non-human workloads to programmatically authenticate and make authorized API calls to Google Cloud services. 

User-managed service accounts are typically created and managed by you, but some are created by default when you enable a Google Cloud service. You still manage default service accounts directly. 

Service accounts act as both principals _and_ resources. [As a principal](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-identities), you can grant service accounts access to Google Cloud resources. [As a resource](https://docs.cloud.google.com/iam/docs/service-account-overview#service-accounts-resources), you can give other principals permission to access the service account. 

### Permissions to interact with Model Armor

Applications or services calling the Model Armor API should use a service account. This service account must be granted IAM roles that include the necessary `modelarmor.*` permissions to perform actions like using templates to sanitize prompts and responses. 

  * The predefined role `roles/modelarmor.user` is suitable for service accounts that only need to use existing Model Armor templates for sanitization. It includes permissions like `modelarmor.templates.useToSanitizeUserPrompt` and `modelarmor.templates.useToSanitizeModelResponse`.
  * Other roles like `roles/modelarmor.admin` or `roles/modelarmor.editor` grant broader permissions for managing Model Armor resources (templates and floor settings) and are typically granted to human users or automation tools rather than application service accounts.



## Service agents

Service agents are service accounts that are created and managed by Google. Service agents act as an identity for Google Cloud services to access resources within your project on your behalf. 

Service agents are created at some point after you enable and use a Google Cloud API. Upon creation, Google often grants a specific, predefined IAM role to the service agent on your project. These roles contain the minimum permissions required for the service agent to function correctly. For a full list of service agents that are granted roles, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents) in the IAM documentation. 

### Service Extensions service agent

When using Model Armor as a service extension with Cloud Load Balancing, the Service Extensions service agent is involved.

The Service Extensions service agent has an email format like `service-SERVICE_EXTENSION_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com`.

Grant the Service Extensions service agent the following roles in your project to allow the service extension to call Model Armor:

  * `roles/modelarmor.calloutUser`
  * `roles/modelarmor.user`
  * `roles/serviceusage.serviceUsageConsumer`



Example commands to grant these roles:
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:service-SERVICE_EXTENSION_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
      --role=roles/modelarmor.calloutUser
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:service-SERVICE_EXTENSION_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
      --role=roles/modelarmor.user
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
      --member=serviceAccount:service-SERVICE_EXTENSION_PROJECT_NUMBER@gcp-sa-dep.iam.gserviceaccount.com \
      --role=roles/serviceusage.serviceUsageConsumer
    

Replace the following:

  * `PROJECT_ID`: the ID of the project.
  * `SERVICE_EXTENSION_PROJECT_NUMBER`: the Service Extensions project number.



## What's next

  * To learn more about service accounts, see [Service account overview](https://docs.cloud.google.com/iam/docs/service-account-overview) in the IAM documentation. 
  * To learn more about service agents, see [Service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) in the IAM documentation. 
  * To learn how to use service accounts securely, see [Best practices for using service accounts securely](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) in the IAM documentation. 
  * Learn more about [roles and permissions for Model Armor](https://docs.cloud.google.com/model-armor/access-control/roles-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
