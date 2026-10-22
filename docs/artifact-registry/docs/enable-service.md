---
url: https://docs.cloud.google.com/artifact-registry/docs/enable-service/
title: Enable and disable the service \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:29.004096+00:00
---

# Enable and disable the service  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/enable-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Enable and disable the service Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store, manage and secure container images and artifacts from builds. You can enable or disable Artifact Registry based on workload needs.

See [Pricing](https://docs.cloud.google.com/artifact-registry/pricing) for information about charges for Artifact Registry.

See the Artifact Analysis documentation for information about enabling [Artifact Analysis](https://docs.cloud.google.com/artifact-analysis/docs/enabling-disabling-artifact-analysis) APIs and [pricing](https://cloud.google.com/artifact-analysis/pricing) for vulnerability scanning.

## Enabling service

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Install and initialize [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) if it is not already installed. For an existing installation, update components of the Google Cloud CLI with the command: `gcloud components update`. 

To check your version of the gcloud CLI, run the command:
         
         gcloud version

**Note:** On Ubuntu, use the [Debian package](https://docs.cloud.google.com/sdk/docs/install#deb) to install gcloud CLI. The gcloud CLI snap package does not include `kubectl` or extensions to authenticate with Artifact Registry using the gcloud CLI.
  7. Enable the API from [Google Cloud console](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com) or with the following `gcloud` command: 
         
         gcloud services enable artifactregistry.googleapis.com




## Disabling service

Before you disable the Artifact Registry API, ensure that any artifacts that you want to keep are available in another location. It is recommended that you [delete](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos) repositories before disabling the API.

When you disable the Artifact Registry API, the following conditions apply:

  * Repositories and artifacts in repositories become inaccessible.
  * Data might be deleted within 7 days after the API is disabled.



To disable the API from the Google Cloud console:

### console

  1. Go to the [API Overview](https://console.cloud.google.com/apis/library/artifactregistry.googleapis.com) page for Artifact Registry.
  2. Select the project where the API is enabled.
  3. Click **Manage**.
  4. Click **Disable API**.



### gcloud

Run the following command to disable the API for your current project:
    
    
    gcloud services disable artifactregistry.googleapis.com
    

## What's next

  * Configure [access permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for repositories
  * Configure authentication to repositories: 
    * [Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication)
    * [Java](https://docs.cloud.google.com/artifact-registry/docs/java/authentication)
    * [Node.js](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication)
    * [Python](https://docs.cloud.google.com/artifact-registry/docs/python/authentication)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
