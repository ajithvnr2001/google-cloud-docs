---
url: https://docs.cloud.google.com/docs/quotas/terraform-support-for-cloud-quotas/
title: Terraform support for Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:04.488394+00:00
---

# Terraform support for Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/terraform-support-for-cloud-quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Terraform support for Cloud Quotas Stay organized with collections  Save and categorize content based on your preferences. 

[Terraform](https://www.terraform.io/) is an Infrastructure as code (IaC) tool that you can use to provision resources and permissions for Cloud Quotas. To learn how to use Terraform to provision infrastructure on Google Cloud, refer to the [Terraform on Google Cloud documentation](https://docs.cloud.google.com/docs/terraform).

You can use Terraform to do the following with Cloud Quotas:

  * Retrieve the `QuotaInfo` data source of a quota for a project, folder or organization.
  * List `QuotaInfos` data source of all quotas for a given project, folder or organization.
  * Create a new, or update an existing, `QuotaPreference` quota configuration that specifies the preferred value for a quota.



## Before you begin

Before you begin, you need access to Terraform:

  * If you're getting started, note that [Cloud Shell](https://docs.cloud.google.com/shell/docs) has Terraform already integrated, and you can follow this step by step tutorial, [Deploy a basic Flask web server](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform) using Terraform and Cloud Shell.

  * If you'd prefer to install Terraform yourself, see HashiCorp's [Terraform installation instructions](https://developer.hashicorp.com/terraform/tutorials/gcp-get-started/install-cli).




To use Terraform with Cloud Quotas, [create a configuration file](https://developer.hashicorp.com/terraform/language) to describe your infrastructure, and then [apply the configuration file](https://developer.hashicorp.com/terraform/cli/commands/apply) to create an execution plan and perform operations to provision your infrastructure.

## Terraform resources and data sources

The following lists contain links to Cloud Quotas Terraform resources and data source samples that appear in the [Terraform registry](https://registry.terraform.io/providers/hashicorp/google/latest/docs/).

### Resources

Cloud Quotas provides the following Terraform resources:

  * [google_cloud_quotas_quota_preference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_quotas_quota_preference)
  * [google_cloud_quotas_quota_adjuster_settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_quotas_quota_adjuster_settings) ([Preview](https://cloud.google.com/products#product-launch-stages))



### Data sources

Cloud Quotas provides the following Terraform data sources:

  * [google_cloud_quotas_quota_info](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloud_quotas_quota_info)
  * [google_cloud_quotas_quota_infos](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/cloud_quotas_quota_infos)



## What's next

Learn more about Terraform:

  * [What is Terraform?](https://developer.hashicorp.com/terraform/intro)

  * [Terraform Developer website](https://developer.hashicorp.com/terraform/)

  * [Terraform Language Documentation](https://developer.hashicorp.com/terraform/language)

  * [Terraform CLI Documentation](https://developer.hashicorp.com/terraform/cli)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
