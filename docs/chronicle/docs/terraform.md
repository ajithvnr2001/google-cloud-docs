---
url: https://docs.cloud.google.com/chronicle/docs/terraform/
title: Provision Google SecOps resources with Terraform \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:56:45.626948+00:00
---

# Provision Google SecOps resources with Terraform  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  Provision Google SecOps resources with Terraform Stay organized with collections  Save and categorize content based on your preferences. 

HashiCorp Terraform is an infrastructure-as-code (IaC) tool that lets you provision and manage cloud infrastructure. Terraform provides plugins called _providers_ that let you interact with cloud providers and other APIs. You can use the _Terraform provider for Google Cloud_ to provision and manage Google Cloud resources, including Google SecOps.

This page introduces you to using Terraform with Google SecOps, including an introduction to how Terraform works and some resources to help you get started using Terraform with Google Cloud. You'll also find links to Terraform reference docs for Google SecOps, code examples, and guides for using Terraform to provision Google SecOps resources.

For instructions on how to get started with Terraform for Google Cloud, see [Install and configure Terraform](https://docs.cloud.google.com/docs/terraform/install-configure-terraform) or the [Terraform for Google Cloud quickstart](https://docs.cloud.google.com/docs/terraform/create-vm-instance).

## How Terraform works

Terraform has a declarative and configuration-oriented syntax, which you can use to describe the infrastructure that you want to provision in your Google Cloud project. After you author this configuration in one or more Terraform configuration files, you can use the Terraform CLI to apply this configuration to your Google SecOps resources.

The following steps explain how Terraform works:

  1. You describe the infrastructure you want to provision in a _Terraform configuration file_. You don't need to write code describing how to provision the infrastructure. Terraform provisions the infrastructure for you.
  2. You run the `terraform plan` command, which evaluates your configuration and generates an execution plan. You can review the plan and make changes as needed.
  3. You run the `terraform apply` command, which performs the following actions:

     1. It provisions your infrastructure based on your execution plan by invoking the corresponding Google SecOps APIs in the background.
     2. It creates a _Terraform state file_ , which is a JSON file that maps the resources in your configuration file to the resources in the real-world infrastructure. Terraform uses this file to keep a record of the most recent state of your infrastructure, and to determine when to create, update, and destroy resources.
     3. When you run `terraform apply`, Terraform uses the mapping in the state file to compare the existing infrastructure to the code, and make updates as necessary:

        * If a resource object is defined in the configuration file, but doesn't exist in the state file, Terraform creates it.
        * If a resource object exists in the state file, but has a different configuration from your configuration file, Terraform updates the resource to match your configuration file.
        * If a resource object in the state file matches your configuration file, Terraform leaves the resource unchanged.



## Terraform resources for Google SecOps

_Resources_ are the fundamental elements in the Terraform language. Each resource block describes one or more infrastructure objects, such as virtual networks or compute instances.

The following table lists the Terraform resources available for Google SecOps:

Google SecOps service | Terraform resources  
---|---  
Chronicle API - v1beta | 

  * `[google_chronicle_custom_list](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_custom_list)`
  * `[google_chronicle_dashboard_chart](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_dashboard_chart)`
  * `[google_chronicle_data_access_label](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_data_access_label)`
  * `[google_chronicle_data_access_scope](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_data_access_scope)`
  * `[google_chronicle_data_export](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_data_export)`
  * `[google_chronicle_environment](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_environment)`
  * `[google_chronicle_environment_group](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_environment_group)`
  * `[google_chronicle_feed](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_feed)`
  * `[google_chronicle_findings_refinement](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_findings_refinement)`
  * `[google_chronicle_findings_refinement_deployment](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_findings_refinement_deployment)`
  * `[google_chronicle_native_dashboard](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_native_dashboard)`
  * `[google_chronicle_parser](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_parser)`
  * `[google_chronicle_parser_extension](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_parser_extension)`
  * `[google_chronicle_reference_list](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_reference_list)`
  * `[google_chronicle_retrohunt](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_retrohunt)`
  * `[google_chronicle_rule](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_rule)`
  * `[google_chronicle_rule_deployment](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_rule_deployment)`
  * `[google_chronicle_soar_domain](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_soar_domain)`
  * `[google_chronicle_soar_network](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_soar_network)`
  * `[google_chronicle_watchlist](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_watchlist)`
  * `[google_chronicle_data_table](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/chronicle_data_table)`
  * `[google_chronicle_data_table_row](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_table_row)`

  
Chronicle API - v1 | 

  * `[google_chronicle_custom_list](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_custom_list)`
  * `[google_chronicle_data_access_label](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_access_label)`
  * `[google_chronicle_data_access_scope](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_access_scope)`
  * `[google_chronicle_data_export](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_export)`
  * `[google_chronicle_environment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_environment)`
  * `[google_chronicle_environment_group](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_environment_group)`
  * `[google_chronicle_feed](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_feed)`
  * `[google_chronicle_findings_refinement](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_findings_refinement)`
  * `[google_chronicle_findings_refinement_deployment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_findings_refinement_deployment)`
  * `[google_chronicle_parser](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_parser)`
  * `[google_chronicle_parser_extension](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_parser_extension)`
  * `[google_chronicle_reference_list](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_reference_list)`
  * `[google_chronicle_retrohunt](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_retrohunt)`
  * `[google_chronicle_rule](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_rule)`
  * `[google_chronicle_rule_deployment](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_rule_deployment)`
  * `[google_chronicle_soar_domain](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_soar_domain)`
  * `[google_chronicle_soar_network](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_soar_network)`
  * `[google_chronicle_watchlist](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_watchlist)`
  * `[google_chronicle_data_table](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_table)`
  * `[google_chronicle_data_table_row](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_data_table_row)`
  * `[chronicle_native_dashboard](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_native_dashboard)`
  * `[chronicle_dashboard_chart](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/chronicle_dashboard_chart)`

  
  
## What's next

  * [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform)
  * [Google Cloud provider documentation in HashiCorp](https://registry.terraform.io/providers/hashicorp/google/latest/docs)
  * [Infrastructure as code for Google Cloud](https://docs.cloud.google.com/docs/terraform/iac-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
