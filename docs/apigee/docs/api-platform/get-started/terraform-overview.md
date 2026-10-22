---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview/
title: Use Terraform with Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:54:52.340939+00:00
---

# Use Terraform with Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/terraform-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Use Terraform with Apigee Stay organized with collections  Save and categorize content based on your preferences. 

[HashiCorp Terraform](https://www.terraform.io/) is an Infrastructure as Code (IaC) tool that you can use to provision and configure Apigee using code. 

When you use Terraform with Apigee, you create [Terraform files](https://developer.hashicorp.com/terraform/language) that describe your desired configuration for provisioning or a feature. When you [ apply the configuration](https://developer.hashicorp.com/terraform/cli/commands/apply), Terraform creates an execution plan and performs the operations needed to configure Apigee. 

This page summarizes the Terraform functionality available for Apigee. For general information about using Terraform with Google Cloud, see [Terraform on Google Cloud documentation](https://cloud.google.com/docs/terraform). 

**Note:** See [Get support for Terraform issues](https://docs.cloud.google.com/docs/terraform/getting-support) for information on getting help with Terraform.

## Before you begin

In order to set up Terraform for your Apigee project:

  1. Prepare your development environment, either Cloud Shell or a local shell:

### Cloud Shell

To use an online terminal with the gcloud CLI and Terraform already set up, activate Cloud Shell.

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

Note that Cloud Shell has Terraform already integrated.

### Local shell

To use a local development environment, follow these steps:

     1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  3. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  4. [Install Terraform](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).


* [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

* Enable the Cloud Resource Manager and Identity, Access Management (IAM) APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable cloudresourcemanager.googleapis.com  iam.googleapis.com

* Ensure that your Google Cloud project doesn't have the `Google Cloud Platform - Resource Location Restriction` [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints) added. 

## Terraform resources for Apigee

The following table summarizes the features and functionality you can manage using Terraform resources for Apigee. This list might not be exhaustive. Find all of the Terraform resources for Apigee in the [ Google Cloud Platform Cloud Foundation Fabric GitHub repository](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/modules/apigee) and the [ HashiCorp Google Provider documentation for Apigee](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/apigee_organization). Always check these resources for the latest functionality. 

Apigee feature or functionality | Terraform support summary | More information  
---|---|---  
Provision Apigee | Provision Apigee instances using Terraform. | [Provisioning options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-options)  
Provision Apigee API hub | Configure and manage API hub using Terraform. | [Provision API hub with Terraform](https://docs.cloud.google.com/apigee/docs/apihub/provision-terraform)  
Configure Advanced API Security | Configure risk assessment security profiles and monitoring conditions (v2)  
  
Configure abuse detection exclusion lists  
Configure security actions |  [ Configure Advanced API Security with Terraform](https://docs.cloud.google.com/apigee/docs/api-security/enable-security#configure-advanced-api-security-using-terraform)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
