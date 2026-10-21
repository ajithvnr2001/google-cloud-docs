---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/
title: Policy validation \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:13:26.751202+00:00
---

# Policy validation  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Policy validation Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Businesses are shifting towards infrastructure-as-code, and with that change comes a concern that configuration errors can cause security and governance violations. To address this, security and cloud administrators need to be able to set up guardrails that make sure everyone in their organization follows security best practices. These guardrails are in the form of _constraints_.

Constraints define your organization's source of truth for security and governance requirements. The constraints must be compatible with tools across every stage of the application lifecycle, from development, to deployment, and even to an audit of deployed resources.

[`gcloud beta terraform vet`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/terraform/vet) is a tool for enforcing policy compliance as part of an infrastructure CI/CD pipeline. When you run this tool, `gcloud beta terraform vet` retrieves project data with Google Cloud APIs that are necessary for accurate validation of your plan. You can use `gcloud beta terraform vet` to detect policy violations and provide warnings or halt deployments before they reach production. The same set of constraints that you use with `gcloud beta terraform vet` can also be used with any other tool that supports the same framework.

With `gcloud beta terraform vet` you can:

  * Enforce your organization's policy at any stage of application development
  * Remove manual errors by automating policy validation
  * Reduce learning time by using a single paradigm for all policy management



## Support

Until `gcloud beta terraform vet` is generally available (GA), regular support channels might not be available. For support with `gcloud beta terraform vet`, [open a ticket](https://github.com/GoogleCloudPlatform/terraform-google-conversion/issues/new/choose) on the `terraform-google-conversion` GitHub repository.

## Documentation

`gcloud beta terraform vet` includes the following resources:

  * [Quickstart](https://docs.cloud.google.com/docs/terraform/policy-validation/quickstart) – How to implement a constraint that throws an error, and then modify the constraint so the validation check passes.
  * [Create a policy library](https://docs.cloud.google.com/docs/terraform/policy-validation/create-policy-library) – How to create a centralized policy repository.
  * [Create Terraform constraints](https://docs.cloud.google.com/docs/terraform/policy-validation/create-terraform-constraints) – How to add Terraform-based constraints.
  * [Create CAI constraints](https://docs.cloud.google.com/docs/terraform/policy-validation/create-cai-constraints) – How to add CAI-based constraints.
  * [Validate policies](https://docs.cloud.google.com/docs/terraform/policy-validation/validate-policies) – How to validate policy compliance with `gcloud beta terraform vet`.
  * [Troubleshooting](https://docs.cloud.google.com/docs/terraform/policy-validation/troubleshooting) – Potential problems and solutions to fix them.
  * [Migrate from terraform-validator](https://docs.cloud.google.com/docs/terraform/policy-validation/migrate-from-terraform-validator) \- How to migrate to `gcloud beta terraform vet` from [terraform-validator](https://github.com/GoogleCloudPlatform/terraform-validator).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
