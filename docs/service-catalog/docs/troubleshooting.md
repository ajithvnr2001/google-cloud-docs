---
url: https://docs.cloud.google.com/service-catalog/docs/troubleshooting/
title: Troubleshoot Terraform solutions for Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:50.742975+00:00
---

# Troubleshoot Terraform solutions for Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Terraform solutions for Service Catalog

This page shows you how to resolve issues that you might encounter when you create or update Terraform solutions with Service Catalog, and provides suggestions for how to fix each of them.

## Permission denied error

The following issue occurs when you see this validation error:
    
    
    Permission denied; please check you have the correct IAM permissions and APIs
    enabled.
    

To resolve this issue, take the following actions, depending on whether or not you're providing your own service account:

### Provide your own service account

Verify that the service account that you're using appears in the Identity and Access Management (IAM) service accounts page of the Google Cloud project that you're using.

If the service account appears, verify that you have the correct IAM permissions to use it. You must have the permission `iam.serviceAccounts.actAs` for the Google Cloud project that's using the service account. If you don't have this role, contact the project owner or an administrator who can grant you access.

If the service account is in a different Google Cloud project from your Terraform solution, you must perform the following additional [steps for cross-project configuration](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#cross-project_set_up).

### Default service account

Verify that you have the IAM permission `iam.serviceAccounts.actAs` for the Compute Engine default service account that your Google Cloud project is using. If you don't have this role, contact the project owner or an administrator who can grant you access. For more information, see [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).

## Error creating artifacts bucket

The following issue occurs when you see this validation error:
    
    
    Error creating artifacts bucket.
    

To resolve this issue, verify that you have the Storage Admin (`roles/storage.admin`) role in the current Google Cloud project. If you don't have this role, contact the project owner or an administrator who can grant you access.

## Failed to create build error

The following issue occurs when you see this validation error:
    
    
    Failed to create build.
    

To resolve this issue, verify that the service account that you're using has the Logs Writer (`roles/logging.logWriter`) and Storage Admin (`roles/storage.admin`) roles in the current Google Cloud project. If it doesn't have these roles, contact the project owner or an administrator who can grant the required access to the service account.

## Error reading Cloud Storage bucket

The following issue occurs when you see this validation error:
    
    
    Error reading GCS bucket: GCS_SOURCE.
    

To resolve this issue, verify that the service account that you're using has the Storage Object Viewer (`roles/storage.objectViewer`) role in the current Google Cloud project. If it doesn't have this role, contact the project owner or an administrator who can grant the required access to the service account.

## No Terraform module

The following issue occurs when you see this validation error:
    
    
    unable to process terraform module - no terraform module detected. Only TF or
    TF.JSON files are currently supported.
    

To resolve this issue, verify that your Terraform module follows [the expected format](https://docs.cloud.google.com/service-catalog/docs/terraform-configuration#create_module), and has been created by zipping a sequence of Terraform files.

**Note:** Service Catalog doesn't support Terraform modules in subdirectories or folders other than the root directory.

## Invalid status without validation errors

The following issue occurs when you see a validation status of `INVALID`, but you don't see any specific validation errors. This can occur if there's an issue with your Terraform config.

To resolve this issue, verify the Terraform config by using the command [`Terraform apply`](https://developer.hashicorp.com/terraform/cli/commands/apply), and resolve any specific issues that you encounter.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
