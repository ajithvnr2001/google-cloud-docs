---
url: https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-compute-vm/
title: Create a Compute Engine VM \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:08.840281+00:00
---

# Create a Compute Engine VM  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-compute-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

# Create a Compute Engine VM

This page describes how to create a Compute Engine VM.

As the first step to create a connector VM, create a Compute Engine VM. 
  1. To create a Compute Engine VM in your Google Cloud project, run the following gcloud command: 
         
         gcloud compute instances create VM_NAME --zone=ZONE --project=PARTNER_PROJECT
           

  2. To create an SSH connection to the created VM, run the following gcloud command: 
         
         gcloud compute ssh --zone ZONE VM_NAME --project PARTNER_PROJECT
           

Ensure that the firewall allows TCP ingress on port 22 of the VM. 




## What's next

  * Learn how to [create a web service and deploy it on a Compute Engine VM instance](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-webservice).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
