---
url: https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources/
title: Best practices when working with Google Cloud resources \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:35.381996+00:00
---

# Best practices when working with Google Cloud resources  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/best-practices/working-with-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Best practices when working with Google Cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

Best practices for provisioning Google Cloud resources with Terraform, are integrated into the [Cloud Foundation Toolkit](https://docs.cloud.google.com/foundation-toolkit) modules that Google maintains. This document reiterates some of these best practices.

This guide is not an introduction to Terraform. For an introduction to using Terraform with Google Cloud, see [Get started with Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform).

## Bake virtual machine images

In general, we recommend that you _bake_ virtual machine images [using a tool like Packer](https://docs.cloud.google.com/compute/docs/images/image-management-best-practices#automated_baking). Terraform then only needs to launch machines using the pre-baked images.

If pre-baked images are not available, Terraform can hand off new virtual machines to a configuration management tool with a `provisioner` block. We recommend that you avoid this method and only use it as a [last resort](https://www.terraform.io/language/resources/provisioners/syntax#provisioners-are-a-last-resort). To clean up old state associated with the instance, provisioners that require teardown logic should use a `provisioner` block with `when = destroy`.

Terraform should provide VM configuration information to configuration management with [instance metadata](https://docs.cloud.google.com/compute/docs/metadata/overview).

## Manage Identity and Access Management

When provisioning IAM associations with Terraform, several different resources are available:

  * `google_*_iam_policy` (for example, `google_project_iam_policy`)
  * `google_*_iam_binding` (for example, `google_project_iam_binding`)
  * `google_*_iam_member` (for example, `google_project_iam_member`)



`google_*_iam_policy` and `google_*_iam_binding` create _authoritative_ IAM associations, where the Terraform resources serve as the only source of truth for what permissions can be assigned to the relevant resource.

If the permissions change outside of Terraform, Terraform on its next execution overwrites all permissions to represent the policy as defined in your configuration. This might make sense for resources that are wholly managed by a particular Terraform configuration, but it means that roles that are automatically managed by Google Cloud are removed—potentially disrupting the functionality of some services.

To prevent this, we recommend using either `google_*_iam_member` resources directly or the [IAM module from Google](https://github.com/terraform-google-modules/terraform-google-iam).

## What's next

  * Learn about [best practices for version control](https://docs.cloud.google.com/docs/terraform/best-practices/version-control).
  * Learn about [best practices for Terraform operations](https://docs.cloud.google.com/docs/terraform/best-practices/operations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
