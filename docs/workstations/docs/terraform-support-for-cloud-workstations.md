---
url: https://docs.cloud.google.com/workstations/docs/terraform-support-for-cloud-workstations/
title: Terraform support for Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:07:06.495930+00:00
---

# Terraform support for Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/terraform-support-for-cloud-workstations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Terraform support for Cloud Workstations Stay organized with collections  Save and categorize content based on your preferences. 

[Terraform](https://www.terraform.io/) is an infrastructure-as-code (IaC) tool that you can use to provision resources and permissions for Cloud Workstations. To use Terraform with Cloud Workstations, you need to [create a configuration file](https://developer.hashicorp.com/terraform/language) to describe your infrastructure, and then [apply the configuration file](https://developer.hashicorp.com/terraform/cli/commands/apply) to create an execution plan and perform operations to provision your infrastructure.

For example, you can use Terraform to create workstations, create various workstation configurations (templates), and create workstation configurations for public or private workstation clusters.

## Terraform resources for Cloud Workstations

The following table lists Cloud Workstations configuration samples that appear in the [Terraform registry](https://developer.hashicorp.com/terraform/language/resources) and from [GitHub](https://github.com/terraform-google-modules/docs-examples).

**Cloud Workstations resource** | **Terraform registry sample**  
---|---  
Cluster | Basic [google_workstations_workstation_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_cluster#example-usage---workstation-cluster-basic)  
Private [google_workstations_workstation_cluster](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_cluster#example-usage---workstation-cluster-private)  
Basic workstation configuration | [google_workstations_workstation_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_config#example-usage---workstation-config-basic)  
Workstation configuration with additional features | From a container: [google_workstations_workstation_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_config#example-usage---workstation-config-container)  
With persistent directories: [google_workstations_workstation_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_config#example-usage---workstation-config-persistent-directories)  
With shielded instance configuration: [google_workstations_workstation_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_config#example-usage---workstation-config-shielded-instance-config)  
With customer-managed encryption keys (CMEK) [google_workstations_workstation_config](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation_config#example-usage---workstation-config-encryption-key)  
Workstation | [google_workstations_workstation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/workstations_workstation)  
  
## What's next

Learn more about Terraform:

  * [What is Terraform?](https://developer.hashicorp.com/terraform/intro)

  * [Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/)

  * [Terraform Developer website](https://developer.hashicorp.com/terraform/)

  * [Terraform Language Documentation](https://developer.hashicorp.com/terraform/language)

  * [Terraform CLI Documentation](https://developer.hashicorp.com/terraform/cli)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
