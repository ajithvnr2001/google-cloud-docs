---
url: https://docs.cloud.google.com/run/docs/configuring/services/build-service-account/
title: Set build service account (source deploy) \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:55.600654+00:00
---

# Set build service account (source deploy)  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/build-service-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set build service account (source deploy) Stay organized with collections  Save and categorize content based on your preferences. 

During source deployments, Cloud Run leverages Cloud Build when building and deploying your Cloud Run service.

This page shows how to set a [user-specified service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account#user_access_to_triggers) for Cloud Build to use when executing builds of the service on your behalf. This guide is relevant for platform developers who are deploying Cloud Run [services](https://docs.cloud.google.com/run/docs/deploying-source-code) or [functions](https://docs.cloud.google.com/run/docs/deploy-functions) using the Google Cloud CLI and need to customize the build service account used by Cloud Build. The build service account gcloud CLI flag is supported for [source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) (`--source`), and not supported for [container image deployments](https://docs.cloud.google.com/run/docs/deploying) (`--image`).

## Before you begin

  1. Enable the Cloud Build API:
         
         gcloud services enable cloudbuild.googleapis.com

  2. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create), or have an existing service account, to use as the Cloud Build service account.




### Required roles

You or your administrator must grant the deployer account and the Cloud Build service account the following IAM roles.

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



#### Click to view required roles for the Cloud Build service account

To allow the Cloud Build service account to perform the build when deploying a function, ask your administrator to grant the [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) role to the Cloud Build service account on the project.

**Note:** If you need to use a service account from a different project, you or your administrator must grant additional access to the service account. See [Cross-project set up](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts#cross-project_set_up) for more details. 

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Specify a Cloud Build service account

By default, if a Cloud Build service account isn't specified when deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#gcloud_1) from source, Cloud Build uses the [default Cloud Build service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account).

As a best practice for following the principle of least privilege to improve the security posture of your service, we recommend that you specify your own service account to run your builds when deploying a service from source.

###  gcloud 

To specify the Cloud Build service account when deploying a service from source code, use the `--build-service-account` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --build-service-account projects/PROJECT_ID/serviceAccounts/BUILD_SERVICE_ACCOUNT

Replace:

  * SERVICE with name of your Cloud Run service.
  * PROJECT_ID the project ID where the build service account is created.
  * BUILD_SERVICE_ACCOUNT with a user-specified service account.



If you are deploying a function, add the `--function` flag with the function entry point from your source code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
