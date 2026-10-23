---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cloud-sdk/
title: Configure the Google Cloud CLI \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:48.790234+00:00
---

# Configure the Google Cloud CLI  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-cloud-sdk/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the Google Cloud CLI

Before using GKE on Azure, you must install the Google Cloud CLI and enable required APIs.

To configure Google Cloud CLI, run the following commands:

  1. Check your Google Cloud CLI installation with the following command:
         
         gcloud version
         

  2. If the Google Cloud CLI is not installed, or if its version is earlier than 402.0.0, [Install the latest version of the Google Cloud CLI](https://cloud.google.com/sdk/docs/install).

  3. Install the `kubectl` [additional component](https://cloud.google.com/sdk/docs/components#additional_components).

  4. If you haven't already done so, [create your Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project). Save your project's name, you'll use it later.

  5. Run the following command to authenticate with your Google Cloud account:
         
         gcloud auth login
         

  6. Enable the GKE Multi-Cloud API and its service dependencies with the following commands. These commands will enable the APIs for the project configured in your Google Cloud CLI.
         
         gcloud services enable gkemulticloud.googleapis.com
         gcloud services enable gkeconnect.googleapis.com
         gcloud services enable gkehub.googleapis.com
         gcloud services enable connectgateway.googleapis.com
         gcloud services enable cloudresourcemanager.googleapis.com
         gcloud services enable anthos.googleapis.com
         gcloud services enable logging.googleapis.com
         gcloud services enable monitoring.googleapis.com
         gcloud services enable opsconfigmonitoring.googleapis.com
         gcloud services enable kubernetesmetadata.googleapis.com
         




## What's next

  * [Configure the Azure CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/configure-azure-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
