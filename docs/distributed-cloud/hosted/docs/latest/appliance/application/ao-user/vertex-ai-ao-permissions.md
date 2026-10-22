---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:15:40.469725+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ao-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page describes all the roles and their respective permissions for using Vertex AI services.

Google Distributed Cloud (GDC) air-gapped appliance offers Identity and Access Management (IAM) for granular access to specific GDC air-gapped appliance resources and prevents unwanted access to other resources. IAM operates on the security principle of least privilege and controls who can access given resources using IAM roles and permissions.

A role is a collection of specific permissions mapped to certain actions on resources and assigned to individual subjects, such as users, groups of users, or service accounts. Therefore, you must have the proper IAM roles and permissions to use Vertex AI services on GDC air-gapped appliance.

To grant permissions or receive role access to resources, see [Grant and revoke access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings).

**Important:** If you can't access or use a Vertex AI service, contact your administrator to grant you the necessary roles. Request the appropriate permissions from your Project IAM Admin for a given project. If you require permissions at the organization level, ask your Organization IAM Admin instead.

## Predefined roles at the organization level

Request the appropriate permissions from your Organization IAM Admin to set up Vertex AI in an organization and manage the lifecycle of a project that uses AI services.

The following table provides details about the permissions assigned to each predefined role:

Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---  
AI Platform Admin | `ai-platform-admin` | Grant permissions to manage pre-trained services. | `ClusterRole`  
Project Creator | `project-creator` | Create new projects. | `ClusterRole`  
  
## Predefined roles at the project level

Request the appropriate permissions from your Project IAM Admin to use Vertex AI services in a project. All Vertex AI roles must bind to the project namespace where you are using the service.

The following table provides details about the permissions assigned to each predefined role:

Vertex AI service | Role name | Kubernetes resource name | Permission description | Type  
---|---|---|---|---  
_N/A_ | Project IAM Admin | `project-iam-admin` | Manage the IAM allow policies of projects and create service accounts. | `Role`  
Optical Character Recognition (OCR) | AI OCR Developer | `ai-ocr-developer` | Access the OCR service to detect text in images. | `Role`  
Speech-to-Text | AI Speech Developer | `ai-speech-developer` | Access the Speech-to-Text service to recognize speech and transcribe audio. | `Role`  
Vertex AI Translation | AI Translation Developer | `ai-translation-developer` | Access the Vertex AI Translation service to translate text. | `Role`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
