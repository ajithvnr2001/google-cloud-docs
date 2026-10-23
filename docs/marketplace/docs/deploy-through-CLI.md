---
url: https://docs.cloud.google.com/marketplace/docs/deploy-through-CLI/
title: Deploy virtual machine (VM) products using the command-line interface (CLI) \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:56.570980+00:00
---

# Deploy virtual machine (VM) products using the command-line interface (CLI)  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/deploy-through-CLI/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Deploy virtual machine (VM) products using the command-line interface (CLI) Stay organized with collections  Save and categorize content based on your preferences. 

Virtual machine (VM) products offered through Google Cloud Marketplace are custom VM instances that you can run on Compute Engine. For an overview of Compute Engine concepts, visit the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs).

Some VM products on Google Cloud Marketplace support deployment through the command-line interface (CLI) using [Terraform](https://www.terraform.io/), an open-source tool for provisioning and managing infrastructure. For more information on Terraform, visit [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Overview

This page describes the steps for deploying VM products through the CLI by using Terraform. At a high level, you:

  1. Visit the relevant section of the product's Google Cloud Marketplace listing.

  2. Optionally, select or create the service account that you want to use for your command-line deployment.

  3. Optionally, set up service account impersonation.

  4. Configure your `gcloud` environment for Terraform.

  5. Download the Terraform module or code snippet that you use to deploy the VM product through the CLI.

  6. Use the module or code snippet to deploy the VM product.




## Visit the command-line deployment tab

To start deploying a VM product through the CLI:

  1. In Cloud Marketplace, visit the product listing page for the VM product that you want to deploy through the CLI.

[Go to Marketplace](https://console.cloud.google.com/marketplace)

  2. Click the **Launch** button, or click **Deploy with CLI** to visit the **Command-line deployment** tab.




## (Optional) Select or create your service account

Within the **Command-line deployment** tab, you can choose to select or create the service account that you want to use for your command-line deployment. If you haven't selected or created a service account in the **Command-line deployment** tab when you generate your code snippet, you must manually edit the generated Terraform snippet to add a service account before you use it. For more information about service accounts, visit [Creating and managing service accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

If you want to deploy a Cloud Marketplace VM product through the CLI, the service account that you use must have the [Compute Admin (`roles/compute.admin`) Identity and Access Management (IAM) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin). If you create a new service account from the **Command-line deployment** tab, Google Cloud Marketplace automatically grants this role to the new service account. If you select an existing service account from the **Command-line deployment** tab, you must verify that the service account has this role.

To select or create your service account:

  1. From the **Command-line deployment** tab of the VM product's Google Cloud Marketplace listing, under **Configure a service account (optional)** , click the **Configure** button.

  2. Under **Service account requesting permissions** , you can click to **Select an existing service account** , or **Create a new service account**.




### Select an existing service account

To select an existing service account:

  1. Under **Select a service account** , select the service account that you want to use. The list contains all of your existing service accounts that have the [Compute Admin (`roles/compute.admin`) role](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin).

If none of your existing service accounts have the Compute Admin (`roles/compute.admin`) role, the list is empty. If the list is empty, you can grant this role to one of your existing service accounts and then return to this tab, or you can choose to create a new service account instead.

  2. Click the **Submit** button.




### Create a new service account

To create a new service account:

  1. Choose a name for your service account, and add it in the **Service account name** field.

  2. Choose an ID for your service account, and add it in the **Service account ID** field.

  3. Add a description for your service account to the **Service account description** field.

  4. Click the **Create service account** button.




After you've created your service account, you can continue to [manage the service account's access control](https://docs.cloud.google.com/iam/docs/overview) by using IAM.

## (Optional) Set up service account impersonation

We recommend that you use _service account impersonation_ to manage access to your command-line deployment. If you use impersonation, instead of creating service account keys that anyone can use to access your deployment, you manage access by granting or revoking the [Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) IAM role](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) to specific principals.

To learn how to grant and revoke roles on a service accounts, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts). To learn more about service account impersonation, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

## Configure your gcloud environment for Terraform

In the **Command-line deployment** tab, under **Configure gcloud** , you see a series of commands. To configure your `gcloud` environment for Terraform, you can copy and run the provided commands.

## Download the Terraform module

You use either an included Terraform module or a generated code snippet to deploy a VM product through the CLI, depending on how the VM product is configured. To verify whether you use an included module or a generated code snippet to deploy a VM product, visit the **Command-line deployment** tab of the product's Cloud Marketplace listing. If you use an included module to deploy the product, you see a **Download** button. If you use a generated code snippet to deploy the product, you see a **Generate code** button.

To download the included module or generated code snippet, complete the following steps:

### Included Terraform module

  1. From the **Command-line deployment** tab of the VM product's Cloud Marketplace listing, click the **Download** button. This downloads a zip file that contains the Terraform module you use.

  2. Extract the Terraform module from the zip file that you downloaded.




### Generated code snippet

  1. From the **Command-line deployment** tab of the VM product's Cloud Marketplace listing, click the **Generate code** button. This generates a code snippet that you can copy and use with Terraform to deploy a VM with Terraform.

  2. To copy the generated code snippet, click **Copy to clipboard**.




## Use the included module or generated code snippet to deploy the VM product

To use the included module or generated code snippet to deploy the VM product through the CLI, complete the following steps:

### Included Terraform module

  1. In the Terraform module that you downloaded, locate the `README.md` file .

  2. Follow the product-specific instructions from the `README.md` file.

While you follow the product-specific instructions, if you experience issues, you can optionally try to deploy the module by running the following commands:

     * `terraform init`

     * `terraform apply`




### Generated code snippet

  1. Verify that the generated code snippet includes the service account that you want to use. If you've configured a service account for your command-line deployment, that service account's information is included in the generated code snippet. If you haven't configured a service account, you must edit the generated code snippet to specify the service account that you want to use.

  2. Create a new file named `main.tf` on the machine where you've installed Terraform.

  3. Paste the generated code snippet, with any edits you've made to it, into the `main.tf` file that you created.

  4. Run the following commands:

     * `terraform init`

     * `terraform apply`




## Next steps

For information on managing your CLI deployments of VM products, visit [Manage CLI deployments of VM products](https://docs.cloud.google.com/marketplace/docs/manage-cli-deployments).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
