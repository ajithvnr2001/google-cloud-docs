---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cloud-sdk/
title: Configure the Google Cloud CLI \u00a0|\u00a0 GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:08.214910+00:00
---

# Configure the Google Cloud CLI  |  GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-cloud-sdk/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Configure the Google Cloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

Before using GKE on AWS, you must install the Google Cloud CLI and enable required APIs.

To configure Google Cloud CLI, run the following commands:

  1. Check your Google Cloud CLI installation with the following command:
         
         gcloud version
         

  2. If the Google Cloud CLI is not installed, or if its version is earlier than 412.0.0, [Install the latest version of the Google Cloud CLI](https://cloud.google.com/sdk/docs/install).

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

  * [Configure the AWS CLI](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/how-to/configure-aws-cli)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
