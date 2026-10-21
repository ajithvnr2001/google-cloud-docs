---
url: https://docs.cloud.google.com/docs/terraform/terraform-overview/
title: Overview of Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:13:23.849851+00:00
---

# Overview of Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/terraform-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Overview of Terraform on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Hashicorp Terraform is an Infrastructure as code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that lets you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud infrastructure.

## Benefits of using Terraform

This section explains some of the benefits of using Terraform to provision and manage Google Cloud infrastructure:

  * Terraform is the most commonly used tool to provision and automate Google Cloud infrastructure. You can use the [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) to configure and manage all Google Cloud resources using the same declarative syntax and tooling.
  * Terraform lets you specify your preferred end state for your infrastructure. You can then deploy the same configuration multiple times to create reproducible development, test, and production environments.
  * Terraform lets you generate an execution plan that shows what Terraform will do when you apply your configuration. This lets you avoid any surprises when you modify your infrastructure through Terraform.
  * Terraform lets you package and reuse common code in the form of [modules](https://registry.terraform.io/namespaces/terraform-google-modules). Modules present standard interfaces for creating cloud resources. They simplify projects by increasing readability and allow teams to organize infrastructure in readable blocks. Additionally, Google Cloud publishes a number of opinionated deployable modules as [blueprints](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) and getting-started examples as [Jump Start Solutions](https://docs.cloud.google.com/solutions?jump-start-solutions#section-3).
  * Terraform records the current state of your infrastructure and lets you manage state effectively. The Terraform state file keeps track of all resources in a deployment.



## Using Terraform

Terraform has a declarative and configuration-oriented syntax, which you can use to [author the infrastructure](https://developer.hashicorp.com/terraform/language) that you want to provision. Using this syntax, you'll define your preferred end-state for your infrastructure in a _Terraform configuration file_. You'll then use the [Terraform CLI](https://docs.cloud.google.com/docs/terraform/basic-commands) to provision infrastructure based on the configuration file.

The following steps explain how Terraform works:

  1. You describe the Google Cloud infrastructure you want to provision in a Terraform configuration file. You don't need to author code describing _how_ to provision this configuration.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. Then, you run the `terraform apply` command, which performs the following actions: 
     * It provisions your infrastructure based on your execution plan by invoking the corresponding Google Cloud APIs in the background.
     * It creates a _Terraform state file_ , which is a JSON formatted mapping of resources in your configuration file to the resources in the real world infrastructure. Terraform uses this file to know the latest state of your infrastructure, and to determine when to create, update, and destroy resources.
  4. Subsequently, when you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary: 
     * If a resource object defined in the configuration file does not exist in the state file, Terraform creates it.
     * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
     * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Google Cloud providers

There are two providers that let you provision and manage Google Cloud infrastructure:

  * `google`: Use this provider to provision and manage Google Cloud APIs.
  * `google-beta`: Use this provider to provision and manage Google Cloud beta APIs.



For instructions on using these providers, see the [Google Cloud provider configuration reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/provider_reference).

`google` and `google-beta` providers are developed using a tool called _Magic Modules_. Magic Modules allows contributors to make changes against a single codebase and develop both `google` and `google-beta` providers simultaneously.

You can contribute to the Google Cloud providers using Magic Modules by following the instructions in the [Magic Modules contribution guide](https://googlecloudplatform.github.io/magic-modules/get-started/generate-providers/).

## What's next

  * Learn how to [create a basic web server on Compute Engine using Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform)
  * Learn how to [store Terraform state in a Cloud Storage bucket](https://docs.cloud.google.com/docs/terraform/resource-management/store-state)
  * Look through the [Terraform modules and blueprints for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * Look through the various [Terraform for Google Cloud samples](https://docs.cloud.google.com/docs/samples?language=terraform)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
