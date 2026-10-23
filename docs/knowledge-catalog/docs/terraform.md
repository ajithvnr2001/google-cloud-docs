---
url: https://docs.cloud.google.com/knowledge-catalog/docs/terraform/
title: Provision Knowledge Catalog resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:58.103183+00:00
---

# Provision Knowledge Catalog resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/terraform/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/knowledge-catalog/docs/reference)



Send feedback 

#  Provision Knowledge Catalog resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

With Terraform, you can manage your Knowledge Catalog resources as code. Instead of setting up resources like aspect types and entry groups by hand, you write declarative configuration files that you can reuse across all your environments. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Knowledge Catalog.

This page introduces you to using Terraform with Knowledge Catalog, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Knowledge Catalog, code examples, and guides for using Terraform to provision Knowledge Catalog resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Knowledge Catalog resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Knowledge Catalog APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Knowledge Catalog

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Knowledge Catalog:

Service | Terraform resources | Data sources  
---|---|---  
Knowledge Catalog | 

  * [ google_dataplex_aspect_type](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_aspect_type)
  * [ google_dataplex_aspect_type_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_aspect_type_iam)
  * [ google_dataplex_asset](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_asset)
  * [ google_dataplex_asset_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_asset_iam)
  * [ google_dataplex_datascan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_datascan)
  * [ google_dataplex_datascan_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_datascan_iam)
  * [ google_dataplex_entry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry)
  * [ google_dataplex_entry_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry_group)
  * [ google_dataplex_entry_group_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry_group_iam)
  * [ google_dataplex_entry_type](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry_type)
  * [ google_dataplex_entry_type_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_entry_type_iam)
  * [ google_dataplex_lake](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_lake)
  * [ google_dataplex_lake_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_lake_iam)
  * [ google_dataplex_task](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_task)
  * [ google_dataplex_task_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_task_iam)
  * [ google_dataplex_zone](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_zone)
  * [ google_dataplex_zone_iam](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataplex_zone_iam)
  * [ google_data_lineage_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/data_lineage_config)

| 

  * [ google_dataplex_aspect_type_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_aspect_type_iam_policy)
  * [ google_dataplex_asset_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_asset_iam_policy)
  * [ google_dataplex_datascan_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_datascan_iam_policy)
  * [ google_dataplex_entry_group_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_entry_group_iam_policy)
  * [ google_dataplex_entry_type_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_entry_type_iam_policy)
  * [ google_dataplex_lake_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_lake_iam_policy)
  * [ google_dataplex_task_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_task_iam_policy)
  * [ google_dataplex_zone_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/dataplex_zone_iam_policy)

  
  
## Terraform-based guides for Knowledge Catalog

The following table lists Terraform-based how-to guides and tutorials for Knowledge Catalog:

**Guide** | **Details**  
---|---  
[ Manage data quality rules as code with Terraform](https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code) |  This tutorial explains how to manage Knowledge Catalog data quality rules as code with Terraform, Cloud Build, and GitHub.   
[Codelab: Build the data foundation with Knowledge Catalog metadata](https://codelabs.developers.google.com/governance-context-part1) |  This codelab explains how to build the data foundation with Knowledge Catalog metadata.   
  
## Terraform modules and blueprints for Knowledge Catalog

Modules and blueprints help you automate provisioning and managing of Google Cloud resources at scale. A _module_ is a reusable set of Terraform configuration files that creates a logical abstraction of Terraform resources. A _blueprint_ is a package of deployable and reusable modules, and a policy that implements and documents a specific solution.

The following table lists modules and blueprints related to Knowledge Catalog:

Module or blueprint | Details  
---|---  
[ dataplex-auto-data-quality](https://github.com/GoogleCloudPlatform/terraform-google-dataplex-auto-data-quality) |  This module shows how to deploy data quality rules on BigQuery tables across development and production environments using Cloud Build.   
  
## What's next

  * [Terraform code samples for Knowledge Catalog](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
