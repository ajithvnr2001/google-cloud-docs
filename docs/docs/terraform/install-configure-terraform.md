---
url: https://docs.cloud.google.com/docs/terraform/install-configure-terraform/
title: Install Terraform \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:15.772120+00:00
---

# Install Terraform  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/install-configure-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Install Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to install Terraform for Google Cloud in [Cloud Shell](https://docs.cloud.google.com/shell/docs) and in a local shell. Cloud Shell is an interactive shell environment for Google Cloud that lets you learn and experiment with Google Cloud and manage your projects and resources from your web browser.

For a introductory guide to using Terraform with Google Cloud, see the [Terraform for Google Cloud Quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

###  Cloud Shell 

  1. To use an online terminal with the gcloud CLI already set up, activate Cloud Shell:

At the bottom of this page, a Cloud Shell session starts and displays a command-line prompt. It can take a few seconds for the session to initialize.

  2. To install the Terraform CLI, follow the [HashiCorp instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).

You can [customize your environment](https://docs.cloud.google.com/shell/docs/configuring-cloud-shell#environment_customization) to install the Terraform CLI on environment startup, or install the binary to your home directory to persist the install between sessions.

  3. Run the following command to verify that Terraform is available:
         
         terraform
         

The output should be similar to the following:
         
         Usage: terraform [global options] <subcommand> [args]
         
         The available commands for execution are listed below.
         The primary workflow commands are given first, followed by
         less common or more advanced commands.
         
         Main commands:
           init          Prepare your working directory for other commands
           validate      Check whether the configuration is valid
           plan          Show changes required by the current configuration
           apply         Create or update infrastructure
           destroy       Destroy previously-created infrastructure
         
         

  4. To use Terraform with Google Cloud, you should ensure the following tasks are completed within Google Cloud:

     * [Create or have a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * [Enable billing](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project) for the Google Cloud project.
     * [Enable APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for the Google Cloud services you intend to work with.
     * [Set up authentication](https://docs.cloud.google.com/docs/terraform/authentication) for Terraform.



###  Local shell 

  1. Use the [installation instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli) provided by Terraform.

  2. Run the following command to verify that Terraform is available:
         
         terraform
         

The output should be similar to the following:
         
          Usage: terraform [global options] <subcommand> [args]
         
         The available commands for execution are listed below.
         The primary workflow commands are given first, followed by
         less common or more advanced commands.
         
         Main commands:
           init          Prepare your working directory for other commands
           validate      Check whether the configuration is valid
           plan          Show changes required by the current configuration
           apply         Create or update infrastructure
           destroy       Destroy previously-created infrastructure
         

  3. To use Terraform with Google Cloud, you should ensure the following tasks are completed within Google Cloud:

     * [Create or have a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).
     * [Enable billing](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project) for the Google Cloud project.
     * [Enable APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for the Google Cloud services you intend to work with.
     * [Set up authentication](https://docs.cloud.google.com/docs/terraform/authentication) for Terraform.



## What's next

  * Work through the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance)
  * Learn about the [basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
