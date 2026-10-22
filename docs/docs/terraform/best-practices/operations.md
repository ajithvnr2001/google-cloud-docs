---
url: https://docs.cloud.google.com/docs/terraform/best-practices/operations/
title: Best practices for Terraform operations \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:47.324799+00:00
---

# Best practices for Terraform operations  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/best-practices/operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Best practices for Terraform operations Stay organized with collections  Save and categorize content based on your preferences. 

This document provides guidelines and recommendations for Terraform operations.

This guide is not an introduction to Terraform. For an introduction to using Terraform with Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Always plan first

Always generate a plan first for Terraform executions. [Save the plan to an output file](https://learn.hashicorp.com/tutorials/terraform/automate-terraform). After an infrastructure owner approves it, execute the plan. Even when developers are locally prototyping changes, they should generate a plan and review the resources to be added, modified, and destroyed before applying the plan.

## Implement an automated pipeline

To ensure consistent execution context, execute Terraform through automated tooling. If a build system (like Jenkins) is already in use and widely adopted, use it to run the `terraform plan` and `terraform apply` commands automatically. If no existing system is available, adopt either [Cloud Build](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code) or [Terraform Cloud](https://cloud.hashicorp.com/products/terraform).

## Use service account credentials for continuous integration

When Terraform is executed from a machine in a CI/CD pipeline, it should inherit the service account credentials from the service executing the pipeline. Wherever possible, run CI pipelines on Google Cloud because Cloud Build, Google Kubernetes Engine, or Compute Engine inject credentials without downloading service account keys.

For pipelines that run outside of Google Cloud, prefer [workload identity federation](https://docs.cloud.google.com/iam/docs/using-workload-identity-federation) to obtain credentials without downloading service account keys.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## Avoid importing existing resources

Where possible, avoid importing existing resources (using [`terraform import`](https://www.terraform.io/cli/import)), because doing so can make it challenging to fully understand the provenance and configuration of manually created resources. Instead, create new resources through Terraform and delete the old resources.

In cases where deleting old resources would create significant toil, use the `terraform import` command with explicit approval. After a resource is imported into Terraform, manage it exclusively with Terraform.

Google provides a tool that you can use to import your Google Cloud resources into Terraform state. For more information, see [Import your Google Cloud resources into Terraform state](https://docs.cloud.google.com/docs/terraform/resource-management/import).

## Don't modify Terraform state manually

The Terraform state file is critical for maintaining the mapping between Terraform configuration and Google Cloud resources. Corruption can lead to major infrastructure problems. When modifications to the Terraform state are necessary, use the [`terraform state`](https://www.terraform.io/cli/state) command.

## Regularly review version pins

Pinning versions ensures stability but prevents bug fixes and other improvements from being incorporated into your configuration. Therefore, regularly review version pins for Terraform, Terraform providers, and modules.

To automate this process, use a tool such as [Dependabot](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/about-dependabot-version-updates#supported-repositories-and-ecosystems).

## Use application default credentials when running locally

When developers are locally iterating on Terraform configuration, they should authenticate by running [`gcloud auth application-default login`](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login) to generate application default credentials. Don't download service account keys, because downloaded keys are harder to manage and secure.

## Set aliases to Terraform

To make local development easier, you can add aliases to your command shell profile:

  * `alias tf="terraform"`
  * `alias terrafrom="terraform"`



## What's next

  * Learn about [best practices to securely use Terraform](https://docs.cloud.google.com/docs/terraform/best-practices/security).
  * Learn about [best practices for testing Terraform modules and configurations](https://docs.cloud.google.com/docs/terraform/best-practices/testing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
