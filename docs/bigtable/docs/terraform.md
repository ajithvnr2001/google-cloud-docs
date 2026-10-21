---
url: https://docs.cloud.google.com/bigtable/docs/terraform/
title: Provision Bigtable resources with Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:29:20.276134+00:00
---

# Provision Bigtable resources with Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback 

#  Provision Bigtable resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Before you use Terraform to provision Bigtable resources, you must enable the deletion protection mechanism either in Terraform or Bigtable. For more information about Bigtable deletion protection, see [Modify deletion protection](https://docs.cloud.google.com/bigtable/docs/managing-tables#modify-deletion-protection). 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Bigtable.

This page introduces you to using Terraform with Bigtable, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Bigtable, code examples, and guides for using Terraform to provision Bigtable resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Bigtable resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Bigtable APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Bigtable

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Bigtable:

Service | Terraform resources | Data sources  
---|---|---  
Bigtable | 

  * [google_bigtable_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance)
  * [google_bigtable_table](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table)
  * [google_bigtable_garbage_collection_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_garbage_collection_policy)
  * [google_bigtable_instance_iam_binding](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance_iam_binding)
  * [google_bigtable_instance_iam_member](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance_iam_member)
  * [google_bigtable_instance_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_instance_iam_policy)
  * [google_bigtable_table_iam_binding](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table_iam_binding)
  * [google_bigtable_table_iam_member](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table_iam_member)
  * [google_bigtable_table_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_table_iam_policy)
  * [google_bigtable_authorized_view](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigtable_authorized_view)

| 

  * [google_bigtable_instance_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/bigtable_instance_iam_policy)
  * [google_bigtable_table_iam_policy](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/bigtable_table_iam_policy)

  
  
## Terraform-based guides for Bigtable

The following table lists Terraform-based how-to guides and tutorials for Bigtable:

**Guide** | **Details**  
---|---  
[Migrate from Aerospike to Bigtable](https://docs.cloud.google.com/bigtable/docs/migrate-aerospike-to-bigtable) | Use Terraform to provision resources that are migrated from Aerospike to Bigtable.  
  
## What's next

  * [Terraform code samples for Bigtable](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
