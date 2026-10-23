---
url: https://docs.cloud.google.com/software-supply-chain-security/docs/enable-api/
title: Enable services \u00a0|\u00a0 Software supply chain security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:02.748883+00:00
---

# Enable services  |  Software supply chain security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/software-supply-chain-security/docs/enable-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Software supply chain security ](https://docs.cloud.google.com/software-supply-chain-security/docs)
  * [ Guides ](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)



Send feedback 

#  Enable services Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to enable APIs for products and features that help to protect your software supply chain.

To collect and view software supply chain insights, you must enable the following APIs:

  * Artifact Analysis API to store metadata that other Google Cloud services generate and use.
  * Container Scanning API to scan container images stored in Artifact Registry for vulnerabilities and other metadata. Enabling this API automatically enables the Artifact Analysis API.
  * Artifact Registry to store your build artifacts.
  * Cloud Build to generate build provenance metadata.
  * (GKE only) Container Security API to scan running workloads for OS vulnerabilities.



You must run the Container Scanning API in the same Google Cloud project as Artifact Registry. You can run other Google Cloud services that use the registry in separate projects.

## Enable APIs required for insights

To enable APIs required to generate and view insights:

###  Console 

**Use all services in the same project**

Enable the required APIs together.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=containerscanning.googleapis.com,cloudbuild.googleapis.com,artifactregistry.googleapis.com,containersecurity.googleapis.com)

**Use separate projects**

  1. Enable Container Scanning and Artifact Registry in the project where you want to run Artifact Registry.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=containerscanning.googleapis.com,artifactregistry.googleapis.com)

  2. Enable the Cloud Build API in projects where you are running Cloud Build.

[Enable Cloud Build](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)

  3. Enable the Container Security API in projects where you are running GKE.

[Enable Container Security](https://console.cloud.google.com/apis/enableflow?apiid=containersecurity.googleapis.com)




###  Google Cloud CLI 

**Use all services in the same project**

Enable the required APIs together.
    
    
    gcloud services enable containerscanning.googleapis.com \
        cloudbuild.googleapis.com \
        artifactregistry.googleapis.com \
        containersecurity.googleapis.com
    

**Use separate projects**

  1. Enable Container Scanning and Artifact Registry in the project where you want to run Artifact Registry. Replace `AR_PROJECT` with the appropriate Google Cloud project ID.
         
         gcloud services enable containerscanning.googleapis.com \
             artifactregistry.googleapis.com \
             --project=AR_PROJECT
         

  2. Enable the Cloud Build API in projects where you are running Cloud Build. Replace `BUILD_PROJECT` with the appropriate Google Cloud project ID.
         
         gcloud services enable cloudbuild.googleapis.com \
             --project=BUILD_PROJECT
         

  3. Enable the Container Security API in projects where you are running GKE. Replace `GKE_PROJECT` with the appropriate Google Cloud project ID.
         
         gcloud services enable containersecurity.googleapis.com \
              --project=GKE_PROJECT
         




You have enabled the minimum required APIs to generate and view insights in Google Cloud console panels and in the GKE security posture dashboard.

You can enable APIs for other services from the [API library](https://console.cloud.google.com/apis/library) or with the [gcloud services enable](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command.

## What's next

  * Learn about the [IAM permissions](https://docs.cloud.google.com/software-supply-chain-security/docs/configure-access) that are required to view security insights.
  * Learn more about software supply chain security in the [overview](https://docs.cloud.google.com/software-supply-chain-security/docs/overview)
  * Learn about [software supply chain security practices](https://docs.cloud.google.com/software-supply-chain-security/docs/practices) and how Google Cloud products help you to implement them.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
