---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/migrate-from-terraform-validator/
title: Migrate from terraform-validator \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:32.435788+00:00
---

# Migrate from terraform-validator  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/migrate-from-terraform-validator/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Migrate from terraform-validator Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

`gcloud beta terraform vet` is a replacement for the open-source [`terraform-validator`](https://github.com/GoogleCloudPlatform/terraform-validator/) project, with a few minor differences. If you are migrating your CI/CD pipeline to use `gcloud beta terraform vet`, you will need to make the following changes.

## 1\. Update the command and args

  * Replace `terraform-validator validate` with `gcloud beta terraform vet`
  * Replace `--policy-path` with `--policy-library`



Basic example:
    
    
    # Old
    terraform-validator validate ./tfplan.json --policy-path=/path/to/policy-library
    
    # New
    gcloud beta terraform vet ./tfplan.json --policy-library=/path/to/policy-library
    

With [service account impersonation](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account):
    
    
    # Old
    GOOGLE_IMPERSONATE_SERVICE_ACCOUNT=account@project.iam.gserviceaccount.com
    terraform-validator validate ./tfplan.json --policy-path=/path/to/policy-library
    
    # New
    gcloud beta terraform vet ./tfplan.json --policy-library=/path/to/policy-library \
      --impersonate-service-account=account@project.iam.gserviceaccount.com
    

## 2\. (Optional) Upgrade constraint templates

`terraform-validator` documentation historically gave instructions on how to write `v1alpha1` Constraint Framework policies; there is a newer format that we recommend for [writing new policies](https://github.com/GoogleCloudPlatform/policy-library/blob/main/docs/constraint_template_authoring.md). You can also [upgrade existing policies to use the new format](https://github.com/GoogleCloudPlatform/policy-library/blob/main/docs/constraint_template_authoring.md#updating-from-v1alpha1-templates)

For policies sourced from [github.com/GoogleCloudPlatform/policy-library](https://github.com/GoogleCloudPlatform/policy-library), we recommend staying in sync with the remote repository.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
