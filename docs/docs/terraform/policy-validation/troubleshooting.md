---
url: https://docs.cloud.google.com/docs/terraform/policy-validation/troubleshooting/
title: Troubleshoot gcloud beta terraform vet \u00a0|\u00a0 Terraform on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:54.527979+00:00
---

# Troubleshoot gcloud beta terraform vet  |  Terraform on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/policy-validation/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Terraform on Google Cloud ](https://docs.cloud.google.com/docs/terraform)
  * [ Guides ](https://docs.cloud.google.com/docs/terraform/terraform-overview)



Send feedback 

#  Troubleshoot gcloud beta terraform vet Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Why is a violation I expected not throwing an error?

If you test your validation logic and find that the constraint isn't throwing an error when it should be, this might be a result of one or more of the following:

  * **Is your policy-library set up correctly?** Verify that your policy library contains a `policies/constraints` directory, which contains the constraint you are expecting to cause a violation.
  * **Is the Terraform resource that contains the violation a supported resource?** `gcloud beta terraform vet` can only check for violations for resources that are supported in its version. Re-run your command with `--verbosity=debug` and look for a message like: `unsupported resource: google_resource_name`. Or you can check whether your resource is in the list of [supported resources](https://docs.cloud.google.com/docs/cloud-asset-inventory/overview#supported_resource_types).
  * **Is your constraint targeting the correct Terraform resource?**

    1. Check the `kind` field of the constraint. It should be something like: `GCPAppengineLocationConstraintV1`
    2. Search the `policies/templates` directory for a policy that has the same value for `spec.crd.spec.names.kind`
    3. In the `rego` field, look for something like: `asset.asset_type == "appengine.googleapis.com/Application"`. This is the [CAI Asset Type](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types) that the constraint targets.
    4. Make sure that the CAI Asset Type is in the list of [supported resources](https://docs.cloud.google.com/docs/cloud-asset-inventory/overview#supported_resource_types).



## Why am I getting an error saying that no project is defined?

Resource Ancestry is used to build an accurate CAI Asset Name. If `gcloud beta terraform vet` can't automatically determine the ancestry for a CAI Asset, it will return an error saying: `project: required field is not set`. You can provide a default project with the `--project` flag or by setting one using [`gcloud config`](https://docs.cloud.google.com/sdk/gcloud/reference/config).

## Why am I getting an error saying `getting resource ancestry for project PROJECT_ID: googleapi: Error 403: The caller does not have permission, forbidden`?

Run the command with `--verbosity=debug` and look for a message like `Terraform is using this identity:`. It should be followed by an email address, which is the account being used for API requests.

  * If there is no email address, then [make sure that your authentication is working properly](https://docs.cloud.google.com/sdk/gcloud/reference/auth).
  * If there is an email address, but it's not the service account that you wanted to impersonate, then [make sure that your service account impersonation is set up correctly](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)
  * If the correct email address is showing, make sure that it has the following permissions on the project: 
    * `getIamPolicy`
    * `resourcemanager.projects.get`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
