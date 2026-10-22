---
url: https://docs.cloud.google.com/binary-authorization/docs/run/overview/
title: Set up overview for Cloud Run \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:36.169012+00:00
---

# Set up overview for Cloud Run  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/run/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Set up overview for Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of how to set up Binary Authorization for use with Cloud Run services and jobs.

## How Binary Authorization policies are applied to Cloud Run

You can set a Binary Authorization policy on Cloud Run services and jobs. However, policy enforcement varies slightly between Cloud Run services and jobs.

### Policies applied to Cloud Run services

When you set a Binary Authorization policy on a service, Cloud Run checks the policy each time you deploy a new revision. If the new revision does not conform to the policy, the deployment will fail. However, if this happens, you can use the [breakglass](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run) feature to bypass the Binary Authorization policy and deploy a revision using a non-compliant container.

Changes in the Binary Authorization policy _do not_ retroactively apply to existing revisions.

### Policies applied to Cloud Run jobs

When you set a Binary Authorization policy on a job, Cloud Run checks the policy each time you execute the job. If a job has a non-compliant container:

  * You can still update the job successfully.
  * Executing the job will fail. You can use the [breakglass](https://docs.cloud.google.com/binary-authorization/docs/run/using-breakglass-cloud-run) feature to bypass the Binary Authorization policy in these situations.



Changes in the Binary Authorization policy _do not_ retroactively apply to already-running executions.

## Before you begin

Before you use Binary Authorization for Cloud Run, we recommend that you [set up your Cloud Run environment](https://docs.cloud.google.com/run/docs/setup).

## Setup Steps

To set up Binary Authorization for Cloud Run, perform the following steps:

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).
  2. Recommended: [Require Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/requiring-binauthz-cloud-run) using an organization policy.
  3. [Enable Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run).
  4. Configure the Binary Authorization policy.

**Note:** Skip this step if you want to use attestations.

You can configure the following features in your policy:

     * [Default rule](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#default-rule).
     * [Exempt images](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#exempt_images). [Learn more about exempt images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images).

To deploy functions in Cloud Run, the Binary Authorization policy administrator must configure the Binary Authorization policy to exempt all images from the `REGION-docker.pkg.dev/PROJECT_ID/cloud-run-source-deploy/**` repository and its subdirectories.

  5. Optional: Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build) ([Preview](https://cloud.google.com/products#product-launch-stages)).

  6. Optional: [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).

  7. [View Binary Authorization for Cloud Run events in Cloud Audit Logs](https://docs.cloud.google.com/binary-authorization/docs/run/viewing-audit-logs-cloud-run).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
