---
url: https://docs.cloud.google.com/oracle/database/docs/terraform/
title: Provision Oracle Database@Google Cloud resources with Terraform \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:26:10.222153+00:00
---

# Provision Oracle Database@Google Cloud resources with Terraform  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Provision Oracle Database@Google Cloud resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Oracle Database@Google Cloud.

This page introduces you to using Terraform with Oracle Database@Google Cloud, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Oracle Database@Google Cloud, code examples, and guides for using Terraform to provision Oracle Database@Google Cloud resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Oracle Database@Google Cloud resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Oracle Database@Google Cloud APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Oracle Database@Google Cloud

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Oracle Database@Google Cloud:

Terraform configuration sample | Terraform resource | Data sources  
---|---|---  
[Exadata Infrastructure](https://docs.cloud.google.com/oracle/database/docs/create-instances) |  [`google_oracle_database_cloud_exadata_infrastructure`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/oracle_database_cloud_exadata_infrastructure) |  [`google_oracle_database_cloud_exadata_infrastructure`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_cloud_exadata_infrastructure) [`google_oracle_database_cloud_exadata_infrastructures`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_cloud_exadata_infrastructures) [`google_oracle_database_db_servers`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_db_servers)  
[Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters) |  [`google_oracle_database_cloud_vm_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/oracle_database_cloud_vm_cluster) |  [`google_oracle_database_cloud_vm_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_cloud_vm_cluster) [`google_oracle_database_cloud_vm_clusters`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_cloud_vm_clusters) [`google_oracle_database_db_nodes`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_db_nodes)  
[Autonomous AI Database](https://docs.cloud.google.com/oracle/database/docs/create-databases) |  [`google_oracle_database_autonomous_database`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/oracle_database_autonomous_database) |  [`google_oracle_database_autonomous_database`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_autonomous_database) [`google_oracle_database_autonomous_databases`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/oracle_database_autonomous_databases)  
  
## What's next

  * [Terraform code samples for Oracle Database@Google Cloud](https://docs.cloud.google.com/docs/samples?language=terraform)
  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
