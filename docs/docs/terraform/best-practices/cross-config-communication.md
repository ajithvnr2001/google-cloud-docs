---
url: https://docs.cloud.google.com/docs/terraform/best-practices/cross-config-communication/
title: Best practices for cross-configuration communication \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:52.712884+00:00
---

# Best practices for cross-configuration communication  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/best-practices/cross-config-communication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Best practices for cross-configuration communication Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidelines and recommendations for cross-configuration communication when using Terraform for Google Cloud.

This guide is not an introduction to Terraform. For an introduction to using Terraform with Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

A common problem that arises when using Terraform is how to share information across different Terraform configurations (possibly maintained by different teams). Generally, information can be shared between configurations without requiring that they be stored in a single configuration directory (or even a single repository).

The recommended way to share information between different Terraform configurations is by using remote state to reference other root modules. [Cloud Storage](https://www.terraform.io/docs/backends/types/gcs.html) or [Terraform Enterprise](https://www.terraform.io/docs/backends/types/terraform-enterprise.html) are the preferred state backends.

For querying resources that are not managed by Terraform, use data sources from the [Google provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs). For example, the default Compute Engine service account can be retrieved [using a data source](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_default_service_account). Don't use data sources to query resources that are managed by another Terraform configuration. Doing so can create implicit dependencies on resource names and structures that normal Terraform operations might unintentionally break.

## What's next

  * Learn about [best practices for version control](https://docs.cloud.google.com/docs/terraform/best-practices/version-control).
  * Learn about [best practices when working with Google Cloud resources](https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
