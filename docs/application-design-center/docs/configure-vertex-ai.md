---
url: https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai/
title: Configure Vertex AI APIs \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:00:20.527787+00:00
---

# Configure Vertex AI APIs  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-vertex-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure Vertex AI APIs Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI is a machine learning (ML) platform that lets you train and deploy ML models and AI applications. Vertex AI combines data engineering, data science, and ML engineering workflows, letting teams collaborate using a common toolset. For more information, see [Introduction to Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).

This document describes the connections and parameters you can configure when using App Design Center to enable Vertex AI APIs. The configuration parameters are based on the [terraform-google-project-factory](https://github.com/terraform-google-modules/terraform-google-project-factory/tree/main/modules/project_services) Terraform module.

## Component connections

The following table includes the components that you can connect to a Vertex AI component, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instances can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the Compute Engine instance template service account.

| [Vertex AI access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)  
[Service account](https://docs.cloud.google.com/application-design-center/docs/configure-service-account) | 

  * The service account can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the service account.

| [Vertex AI access control with IAM](https://docs.cloud.google.com/vertex-ai/docs/general/access-control)  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The Cloud Run service can interact with Vertex AI services.
  * The `roles/aiplatform.user` role is added to the Cloud Run service account.

| [Host AI apps and agents on Cloud Run](https://docs.cloud.google.com/run/docs/ai-agents)  
  
## Required configuration parameters

If your template includes a Vertex AI component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to enable Vertex AI APIs. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **Enable APIs** | Enabled by default. To skip API enablement, clear the checkbox. | [Set up a project and a development environment](https://docs.cloud.google.com/vertex-ai/docs/start/cloud-environment)  
| **Activate APIs** | By default, the Vertex AI API is activated. If you add other APIs in the _Activate API Identities_ section, the additional APIs are appended to this list. | [Service agents](https://docs.cloud.google.com/iam/docs/service-agents)  
Activate API Identities | **API** | An additional API that you want to activate. A service agent will be created for this API. | [Service agents](https://docs.cloud.google.com/iam/docs/service-agents)  
**Roles** | The roles that you want to grant to the service agent. | [Role list](https://docs.cloud.google.com/iam/docs/roles-permissions)  
| **Disable Service on Destroy** | By default, the service is disabled when the Terraform resource is destroyed. | [disable_on_destroy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service.html#disable_on_destroy-1)  
| **Disable Service Dependent Services** | By default, dependent services are disabled when the Terraform resource is destroyed. | [disable_dependent_services](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service.html#disable_dependent_services-1)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
