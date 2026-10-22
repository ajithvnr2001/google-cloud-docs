---
url: https://docs.cloud.google.com/docs/terraform/best-practices/security/
title: Best practices for security \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:50.093252+00:00
---

# Best practices for security  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/best-practices/security/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Best practices for security Stay organized with collections  Save and categorize content based on your preferences. 

This document provides guidelines and recommendations for securely using Terraform for Google Cloud. Terraform requires sensitive access to your cloud infrastructure to operate. Following security best practices can help to minimize the associated risks and improve your overall cloud security.

This guide is not an introduction to Terraform. For an introduction to using Terraform with Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Use remote state

For Google Cloud customers, we recommend using the [Cloud Storage state backend](https://www.terraform.io/docs/backends/types/gcs.html). This approach locks the state to allow for collaboration as a team. It also separates the state and all the potentially sensitive information from version control.

Make sure that only the build system and highly privileged administrators can access the bucket that is used for remote state.

To prevent accidentally committing development state to source control, use [gitignore](https://github.com/github/gitignore/blob/master/Terraform.gitignore) for Terraform state files.

## Encrypt state

Though Google Cloud buckets are encrypted at rest, you can use [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption#customer-supplied) to provide an added layer of protection. Do this by using the `GOOGLE_ENCRYPTION_KEY` environment variable. Even though no secrets should be in the state file, always encrypt the state as an additional measure of defense.

## Don't store secrets in state

There are many resources and data providers in Terraform that store secret values in plaintext in the state file. Where possible, avoid storing secrets in state. Following are some examples of providers that store secrets in plaintext:

  * [`vault_generic_secret`](https://registry.terraform.io/providers/hashicorp/vault/latest/docs/resources/generic_secret)
  * [`tls_private_key`](https://registry.terraform.io/providers/hashicorp/tls/latest/docs/resources/private_key)
  * [`google_service_account_key`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_service_account_key)
  * [`google_client_config`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/client_config)



## Mark sensitive outputs

Instead of attempting to manually [encrypt sensitive values](https://www.terraform.io/docs/extend/best-practices/sensitive-state.html), rely on Terraform's built-in support for sensitive state management. When exporting sensitive values to output, make sure that the values are marked as [sensitive](https://www.terraform.io/docs/configuration/outputs.html#sensitive-suppressing-values-in-cli-output).

## Ensure separation of duties

If you can't run Terraform from an automated system where no users have access, adhere to a separation of duties by separating permissions and directories. For example, a network project would correspond with a network Terraform service account or user whose access is limited to this project.

## Run pre-apply checks

When running Terraform in an automated pipeline, use a tool like `gcloud terraform vet` to [check plan output against policies](https://docs.cloud.google.com/docs/terraform/policy-validation) before it is applied. Doing so can detect security regressions before they happen.

## Run continuous audits

After the `terraform apply` command has executed, run automated security checks. These checks can help to ensure that infrastructure doesn't drift into an insecure state. The following tools are valid choices for this type of check:

  * [Security Health Analytics](https://docs.cloud.google.com/security-command-center/docs/how-to-use-security-health-analytics)
  * [InSpec](https://inspec.io)
  * [Serverspec](https://serverspec.org/)



## What's next

  * Learn about [general style and structure best practices for Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/best-practices/general-style-structure).
  * Learn about [best practices when using Terraform root modules](https://docs.cloud.google.com/docs/terraform/best-practices/root-modules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
