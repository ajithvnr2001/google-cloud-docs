---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions/
title: Prepare IAM permissions \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:18.354387+00:00
---

# Prepare IAM permissions  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/vertex-ai-ao-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Prepare IAM permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page outlines the Identity and Access Management (IAM) roles and permissions necessary for requesting resource access from your Organization and Project IAM administrators. You can use this information to make sure you have the appropriate access for developing applications with Vertex AI features in Google Distributed Cloud (GDC) air-gapped environments. 

This page is for application developers within application operator groups who are responsible for integrating AI features into secure air-gapped applications. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

GDC air-gapped uses IAM roles and permissions to manage access to resources at the organizational and project level. An IAM role is a collection of specific permissions mapped to actions on resources. A role is assigned by the organizational or project administrator to a user or service account.

You must request IAM roles and permissions before you can begin integrating Vertex AI features into your air-gapped applications:

  * **To request organizational-level access** : Contact your IAM Org Admin. They grant roles and permissions for setting up Vertex AI within an organization and managing the lifecycle of projects that use AI services.

  * **To request project-level access** : Contact your Project IAM administrator to request project-specific roles and permissions. All Vertex AI roles must bind to the project namespace where you're using the service.




For details, see 

**Tip:** It's important to grant and request access using the [principle of least privilege](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/permissions#preinciple-of-least-privilege), to verify you have access to only the minimum necessary permissions for your task. This keeps your resources secure and protects it from unwanted access.

## Predefined roles at the organization level

The following table provides details about the permissions assigned to each predefined role:

Role name | Kubernetes resource name | Permission description  
---|---|---  
AI Platform Admin | `ai-platform-admin` | Grant permissions to manage AI services.  
Project Creator | `project-creator` | Create new projects.  
User Cluster Admin | `user-cluster-admin` | Create, update, and delete a Kubernetes cluster, and manage the cluster's lifecycle.  
  
## Predefined roles at the project level

The following table provides details about the permissions assigned to each predefined role:

Vertex AI service or model | Role name | Kubernetes resource name | Permission description  
---|---|---|---  
_N/A_ | IAM Project Admin | `project-iam-admin` | Manage the IAM allow policies of projects and create service accounts.  
Online Prediction | Vertex AI Prediction User | `vertex-ai-prediction-user` | Access the Online Prediction service to make requests to your model endpoint.  
Vertex AI Prediction Admin | `vertex-ai-prediction-admin` | Manage resources used to deploy models with Online Prediction.  
Optical Character Recognition (OCR) | AI OCR Developer | `ai-ocr-developer` | Access the OCR service to detect text in images.  
Speech-to-Text | AI Speech Chirp Developer | `ai-speech-chirp-developer` | Access the Chirp model of the Speech-to-Text service to recognize speech and transcribe audio.  
AI Speech Developer | `ai-speech-developer` | Access the Speech-to-Text service to recognize speech and transcribe audio.  
Text Embedding | AI Text Embedding Developer | `ai-text-embedding-developer` | Access the Text Embedding model to convert English natural language into numerical vectors.  
AI Text Embedding Multilingual Developer | `ai-text-embedding-multilingual-developer` | Access the Text Embedding Multilingual model to convert multilingual natural language into numerical vectors.  
Gemini | AI Gemini Flash Developer | `ai-gemini-flash-developer` | Access the Gemini Flash service in the project namespace using the AICS inference gateway. Apply as a zonal RoleBinding on the management API server.  
AI Large Gemini Developer | `ai-large-gemini-developer` | Access the Large Gemini service in the project namespace using the AICS inference gateway. Apply as a zonal RoleBinding on the management API server.  
AI Multimodal Embedding Developer | `ai-multimodal-embedding-developer` | Access the Multimodal Embedding model (gemini-embedding-2) to generate numerical embeddings. Apply as a zonal RoleBinding on the management API server.  
Vertex AI Search | Discovery Engine Admin | `vaisearch-admin` | Get full access to all Discovery Engine resources.  
Discovery Engine Developer | `vaisearch-developer` | Get read and write access to all Discovery Engine resources.  
Discovery Engine Reader | `vaisearch-reader` | Get read access to all Discovery Engine resources.  
Vertex AI Translation | AI Translation Developer | `ai-translation-developer` | Access the Vertex AI Translation service to translate text.  
Vertex AI Workbench | GDC Restricted Service Policy Admin | `gdchrestrictedservice-policy-admin` | Get full access to the `GDCHRestrictedService` policy type to control access to Vertex AI Workbench.  
Workbench Notebooks Admin | `workbench-notebooks-admin` | Get read and write access to all notebook resources within a project namespace.  
Create, update, and delete notebooks.  
Workbench Notebooks Viewer | `workbench-notebooks-viewer` | Get read-only access to all notebook resources within a project namespace and view the Vertex AI Workbench user interface.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
