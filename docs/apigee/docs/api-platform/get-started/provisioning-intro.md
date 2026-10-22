---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro/
title: Introduction to provisioning \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:53.042847+00:00
---

# Introduction to provisioning  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Introduction to provisioning Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes the prerequisites and process for installing and configuring Apigee with either an eval organization or a paid (non-evaluation) organization. A paid organization can use Subscription or Pay-as-you-go pricing. We refer to the installation and configuration process for any organization as _provisioning_.

**Note:** For instructions on installing Apigee hybrid, see [What is Apigee hybrid?](https://docs.cloud.google.com/apigee/docs/hybrid/latest/what-is-hybrid)

#### Apigee provisioning process flow diagram

![flow diagram illustrating the steps in this topic](https://docs.cloud.google.com/static/apigee/docs/api-platform/get-started/images/apigee-provisioning-high-level.svg)

## Get ready

  * If you are [ new to Google Cloud](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#new-to-cloud), review Cloud getting-started documentation.
  * If you are [ new to Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#new-to-apigee), review Apigee getting-started documentation.



## Before you begin

  1. Ensure that you have met all of the following [ prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites): 
     * A Google Cloud account with active billing
     * A new Google Cloud project
     * Google Cloud SDK software installed (required for command line provisioning steps)
     * curl software installed (recommended)
     * Google Cloud IAM permissions sufficient to provision
  2. Determine if you want to use a paid org or eval org. See [ Compare evaluation and paid organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval). 
  3. Determine if you want to specify data residency for your organization. See [ Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). 
  4. Review any Google Cloud organization policy resource location constraints in your Google Cloud project. See [ Data residency and organization policy constraints](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts#data-residency-and-google-cloud-organization-policy-constraints). 
  5. Select one of the provisioning options listed in [ Provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options). 
  6. If you selected command line instructions as your provisioning option, select a [ networking option](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options). 



## Provision

Follow the provisioning steps based on the option you selected in [ Provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options). We also support using Terraform to provision Apigee. See [Terraform overview](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview).

**Note:** When you submit the completed configuration for provisioning Apigee, you cannot go back and change the hosting region and encryption key selections. Apigee does not support updating the hosting region or encryption key selections after provisioning is complete. 

## Next steps

The final provisioning step for each org type (eval, Subscription, or Pay-as-you-go) and method (Cloud console or command line) is to deploy a sample proxy. 

## New to Google Cloud?

If you are new to Google Cloud, familiarize yourself with the following:

Title | Description  
---|---  
[Google Cloud essentials](https://docs.cloud.google.com/docs/get-started) | Provides quickstarts, tutorials, interactive walkthroughs, technical documentation, videos, and architectural diagrams to help you get started using Google Cloud.  
[Google Cloud overview](https://docs.cloud.google.com/docs/overview) | Provides a brief description on regions, zones, services, resources (global, regional, zonal), projects, the Google Cloud console, command-line interface, and client libraries.  
[Google Cloud billing](https://docs.cloud.google.com/billing/docs) | A collection of tools that help you track and understand your Google Cloud spending, pay your bill, and optimize your costs  
[Manage your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account) | Provides instructions on creating a Cloud Billing account which is required to use Apigee  
[ Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects) | Provides instructions on how to create a project. Google Cloud projects form the basis for creating, enabling, and using all Google Cloud services including Apigee.  
Data encryption options |  Select Google-managed (default) or customer-managed encryption.

  * [ Google-owned and Google-managed encryption keys](https://docs.cloud.google.com/docs/security/encryption/default-encryption) encrypt your data on the server side, before it is written to disk.
  * [Customer-managed encryption keys](https://docs.cloud.google.com/kms/docs/cmek) are created and managed using Cloud Key Management Service (Cloud KMS), and you store the keys as software keys, in an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally](https://docs.cloud.google.com/kms/docs/ekm). 

  
  
## New to Apigee?

If you are new to Apigee, familiarize yourself with the following:

Title | Description  
---|---  
[ What is Apigee?](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee) | Describes Apigee architecture, discusses making services available to users, API products, and Apigee components  
[ Apigee terminology](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts) | Explains some basic Apigee terminology.  
[Apigee glossary](https://docs.cloud.google.com/apigee/docs/api-platform/reference/glossary) | Defines concepts and terms that have a unique meaning in Apigee.  
[ Introduction to data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts) | Describes data residency, discusses regions and multi-regions, and describes how the region is part of the service endpoint.  
[ Introduction to CMEK](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/cmek-concepts) | Describes using customer-managed encryption keys (CMEK) with Apigee  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
