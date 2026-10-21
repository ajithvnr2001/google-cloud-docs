---
url: https://docs.cloud.google.com/functions/docs/securing/gen-org-policy/
title: Restrict new deployments by product version \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:31.115997+00:00
---

# Restrict new deployments by product version  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/securing/gen-org-policy/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Reference ](https://docs.cloud.google.com/functions/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Restrict new deployments by product version

**Note:** In this document, "Cloud Run functions (2nd gen)" refers to Cloud Run functions created with the Google Cloud Functions v2 APIs.

Cloud Run functions offers two product versions: Cloud Run functions (1st gen) and Cloud Run functions created through the Google Cloud Functions v2 APIs. If your organization wants to enforce a restriction specifying that only one of the versions can be used to deploy new functions, you can define a new [organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) with the [constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#constraints) `constraints/cloudfunctions.restrictAllowedGenerations`. You use this constraint to specify the generation (version) you want to allow or deny in the folder or project the policy is applied to.

The restriction will only apply to new functions being deployed for the first time. You will still be able to redeploy existing functions even if they don't comply with the policy.

## Before you begin

To create or change organization policies, your account must have the role [`roles/orgpolicy.policyAdmin`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#required-roles).

## Use a policy to set and enforce restrictions

You can use Google Cloud CLI to create a policy restricting new Cloud Run functions from being deployed for the first time within a given organization to the specified environment.

Note that setting a policy does not apply to existing functions. All functions that were deployed before the policy can be redeployed, updated, or deleted without restriction.

To create a policy that restricts new Cloud Run functions, run the following command:
    
    
    gcloud resource-manager org-policies \
      allow cloudfunctions.restrictAllowedGenerations \
      --organization=ORGANIZATION_NUMBER VERSION

where `ORGANIZATION_NUMBER` is the number of the organization to which you want to apply the policy, and `VERSION` is the Cloud Run functions version that must be used for new deployments. `VERSION` can be one of the following:

  * `1stGen`: Allow the use of Cloud Run functions (1st gen) only.
  * `2ndGen`: Allow the use of Cloud Run functions (2nd gen) only.
  * To explicitly allow both environments, specify `1stGen` and `2ndGen` together. By default, both environments are allowed when no policy is set.

**Note:** you can also set the policy on a project or folder by replacing the `--organization` flag with `--project=<PROJECT_ID>` or `--folder= respectively.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
