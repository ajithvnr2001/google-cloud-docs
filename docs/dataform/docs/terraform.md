---
url: https://docs.cloud.google.com/dataform/docs/terraform/
title: Use Terraform with Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:04.993797+00:00
---

# Use Terraform with Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Guides ](https://docs.cloud.google.com/dataform/docs/overview)



Send feedback 

#  Use Terraform with Dataform Stay organized with collections  Save and categorize content based on your preferences. 

This document describes Terraform support for Dataform. 

[Terraform](https://www.terraform.io/) is an infrastructure-as-code (IaC) tool that you can use to provision resources and permissions for the following Dataform resources:

  * [Repository](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository)
  * [Release configuration](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_release_config)
  * [Workflow configuration](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_workflow_config)



For example, you can use Terraform to create and configure Dataform repositories, release configurations, and workflow configurations.

To use Terraform with Dataform, you need to [create a configuration file](https://developer.hashicorp.com/terraform/language) to describe your infrastructure, and then [apply the configuration file](https://developer.hashicorp.com/terraform/cli/commands/apply) to create an execution plan and perform operations to provision your infrastructure.

The following table lists Dataform configuration samples that appear in the [Terraform registry](https://developer.hashicorp.com/terraform/language/resources) and in [GitHub](https://github.com/terraform-google-modules/docs-examples).

**Dataform resource** | **Terraform registry sample**  
---|---  
Repository | `[google_dataform_repository](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository#example-usage---dataform-repository)`  
Release configuration | `[google_dataform_repository_release_config](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_release_config#example-usage---dataform-repository-release-config)`  
Workflow configuration | `[google_dataform_repository_workflow_config](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_workflow_config#example-usage---dataform-repository-workflow-config)`  
  
## Manage IAM access in Terraform

You can use Terraform to set and manage the [`dataform_repository_iam` policy](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_iam) for the [repository](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository) resource.

The following resources help you manage the `dataform_repository_iam` policy:

  * [`google_dataform_repository_iam_policy`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_iam#google_dataform_repository_iam_policy)
  * [`google_dataform_repository_iam_binding`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_iam#google_dataform_repository_iam_binding)
  * [`google_dataform_repository_iam_member`](https://registry.terraform.io/providers/hashicorp/google-beta/latest/docs/resources/dataform_repository_iam#google_dataform_repository_iam_member)



For best practices for managing IAM in Terraform, see [Manage Identity and Access Management](https://cloud.google.com/docs/terraform/best-practices-for-terraform#iam).

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
