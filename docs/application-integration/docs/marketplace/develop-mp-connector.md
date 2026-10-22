---
url: https://docs.cloud.google.com/application-integration/docs/marketplace/develop-mp-connector/
title: Develop a Marketplace connector \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:48.948808+00:00
---

# Develop a Marketplace connector  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/marketplace/develop-mp-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Develop a Marketplace connector

**Preview — BigQuery Connector**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes the tasks that you need to perform to develop and publish a Marketplace connector.

The following are the high-level tasks to develop and publish a Marketplace connector:

  * Comply with the requirements for Google Cloud Marketplace.
  * Develop your connector.
  * Submit a request to publish the connector.



## Develop and publish a Marketplace connector

You must ensure that the connector that you develop isn't part of the list of connectors that are available in Integration Connectors and Marketplace connectors.

  1. Register as a partner in Google Cloud. For information, see [Partner Advantage](https://partners.cloud.google.com/). 
  2. Verify that you meet the [requirements to list your product on Cloud Marketplace](https://cloud.google.com/marketplace/docs/partners/offer-products#requirements). 
  3. [Accept the Cloud Marketplace agreement](https://cloud.google.com/marketplace/docs/partners/offer-products#vendor-agreement). 
  4. Create a connector virtual machine (VM) and submit the connector VM on the Marketplace. You must complete the following tasks to create and submit a connector VM: 
     1. [Create a web service and deploy it on a Compute Engine VM instance](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-webservice).
     2. [Create an OpenAPI spec for the web service](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-custom-connector#create-openapi-spec).
     3. [Create a custom connector](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-custom-connector) and then a connection and then validate the web service by using the connection in Application Integration.
     4. [Create a startup script for the VM and validate the script](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-startup-script).
     5. [Create the licensed VM image and a Terraform module for the VM deployment](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-vm-deploy-tf). Also, you must [add a label for Application Integration and Integration Connectors](https://docs.cloud.google.com/marketplace/docs/partners/vm/partner-consumption-tracking).
     6. [Submit the VM product for review in Producer Portal](https://docs.cloud.google.com/integration-connectors/docs/marketplace/submit-vm) and select [your pricing model](https://docs.cloud.google.com/marketplace/docs/partners/vm/select-pricing). When you submit the VM product for review, you must mention that this VM is for Integration Connectors in the **Product name** and **Product overview**.
  5. [Publish the custom connector](https://docs.cloud.google.com/integration-connectors/docs/marketplace/publish-custom-connector) to Google Cloud Marketplace. You can view the progress of your connector review process. After your request for publishing the Marketplace connector is approved, you can view the connector in the list of published connectors.



## What's next

  * Learn how to [create a Compute Engine VM instance](https://docs.cloud.google.com/integration-connectors/docs/marketplace/create-compute-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
