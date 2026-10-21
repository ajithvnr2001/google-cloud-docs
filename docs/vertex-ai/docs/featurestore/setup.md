---
url: https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup/
title: Setup \u00a0|\u00a0 Vertex AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:36:47.168305+00:00
---

# Setup  |  Vertex AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vertex-ai/docs/featurestore/setup/

### **Vertex AI documentation is no longer being updated**

Vertex AI's services are now part of Gemini Enterprise Agent Platform. See the most up-to-date information in the [Agent Platform documentation](https://docs.cloud.google.com/gemini-enterprise-agent-platform).

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Vertex AI ](https://docs.cloud.google.com/vertex-ai/docs)



Send feedback 

#  Setup Stay organized with collections  Save and categorize content based on your preferences. 

Vertex AI Feature Store (Legacy) is [deprecated](https://docs.cloud.google.com/vertex-ai/docs/deprecations). Beginning on May 17, 2026, no new features will be added and only critical patches will be provided. On February 17, 2027, the service will be fully sunset and APIs will no longer be available. 

For continued support and faster innovation, migrate to [Vertex AI Feature Store (V2)](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview), our integrated platform for machine learning (ML) feature management introduced on November 17, 2023\. 

Setup includes information about setting up a project for Vertex AI Feature Store (Legacy) and the required permissions for using Vertex AI Feature Store (Legacy).

## Configure project

The following procedure describes how to create a new project and enable the Vertex AI API. This API is required to use Vertex AI Feature Store (Legacy). If you already have an existing project with the Vertex AI API enabled, you can use that project instead of creating a new project.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Vertex AI API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com)




## Vertex AI Feature Store (Legacy) service agent

In addition to user permissions, Vertex AI Feature Store (Legacy) acts on your behalf to perform operations such as accessing source data. To do so, Vertex AI Feature Store (Legacy) uses a service agent: `service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`. By default, the service agent grants Vertex AI Feature Store (Legacy) access to source data in the same project where your featurestore is located. If the source data is in a different project from your featurestore, you must grant the service agent permission to access the project where the source data is located.

For more information, see [Grant Vertex AI service agents access to other resources](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#grant_service_agents_access_to_other_resources).

## IAM permissions

Vertex AI admins have Vertex AI Feature Store (Legacy) administrator privileges. If you require more granularity, Vertex AI Feature Store (Legacy) provides a set of predefined IAM roles. These roles provide different sets of permissions that are based on the following personas:

IT operations and DevOps
    IT operations and DevOps manage Google Cloud resources and are responsible for creating featurestores and tuning their performance. You can use the `featurestoreAdmin` or `featurestoreInstanceCreator` role. The instance creator role lets you manage featurestores but prevents you from viewing data or writing data to the featurestores.
Data scientists and data engineers
    Data scientists and data engineers create features and write data to featurestores. You can use the `featurestoreResourceEditor` role to manage entity types and features, and use the `featurestoreDataWriter` role to read and write feature values.
ML researchers and business analysts
    ML researchers and business analysts search for features and export values for training models or making predictions; they don't need to create new features or write data. You can use the `featurestoreResourceViewer` role to search or browse for features and the `featurestoreDataViewer` role to read feature values.

For descriptions of each role and their associated permissions, see [Predefined roles for Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#predefined-roles).

## Quotas and limits

Vertex AI Feature Store (Legacy) enforces quotas and limits to help you manage resources by setting your own usage limits and to protect the community of Google Cloud users by preventing unforeseen spikes in usage. To prevent you from hitting unplanned constraints, review Vertex AI Feature Store (Legacy) quotas on the [Quotas and limits](https://docs.cloud.google.com/vertex-ai/quotas#featurestore) page. For example, Vertex AI Feature Store (Legacy) sets a quota on the number of online serving nodes and a quota on the number of online serving requests that you can make per minute.

## What's next

  * Learn about [Manage featurestores](https://docs.cloud.google.com/vertex-ai/docs/featurestore/managing-featurestores).
  * Learn about [best practices](https://docs.cloud.google.com/vertex-ai/docs/featurestore/best-practices) for using Vertex AI Feature Store (Legacy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
