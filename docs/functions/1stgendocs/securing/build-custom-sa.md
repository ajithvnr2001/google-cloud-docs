---
url: https://docs.cloud.google.com/functions/1stgendocs/securing/build-custom-sa/
title: Custom Service Account for Cloud Build (1st gen) \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:42.444946+00:00
---

# Custom Service Account for Cloud Build (1st gen)  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/securing/build-custom-sa/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Custom Service Account for Cloud Build (1st gen)

Cloud Run functions leverages Cloud Build when building and deploying your Cloud Run function. By default, Cloud Run functions uses the default Cloud Build service account as the principal when performing your build. Starting in July 2024, Cloud Build has changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates). As a result of this change, new projects deploying functions for the first time may be using a default Cloud Build service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) for building a function. If you are impacted by this change you can do one of the following:

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).

  * Add the Cloud Build Account role (`roles/cloudbuild.builds.builder`) to the default Compute Engine service account.

  * Create a custom Cloud Build service account for function deployments.




This document describes how to pass in a user-created service account, to be used by Cloud Build, when deploying your function.

You can deploy functions with custom service accounts using the Google Cloud CLI, Google Cloud console, or the Cloud Run functions API.

Here are some scenarios where you may want to provide a different service account to be used when Cloud Build builds your function:

  * You want more control of which service accounts to add to your VPC-SC perimeter.

  * You want Cloud Build to run with different [permissions](https://docs.cloud.google.com/build/docs/cloud-build-service-account#default_permissions_of_service_account) than what the default service account has without having to revoke each permission individually.

  * You want to set granular Cloud Build permissions specifically for your functions, not share a Cloud Build service account that is optimized for other purposes.

  * Your organization disabled the usage of the default service account.




## Enable APIs

This feature requires the IAM API to be enabled.

Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference) to enable the APIs needed to deploy a Cloud Run function, or use [Google Cloud console](https://docs.cloud.google.com/endpoints/docs/openapi/enable-api#console):
    
    
    gcloud services enable iam.googleapis.com
    

## Configure Service Account

This document describes how to create a new service account and grant the required permissions. If you want to use an existing service account, you need the email address of the service account you plan to use. See [configuring user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) for details.

You can view your existing service accounts as follows, or use Google Cloud console:
    
    
    gcloud iam service-accounts list
    

### Create Service Account

Use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference) to create your service account or use Google Cloud console:
    
    
    gcloud iam service-accounts create SA_EMAIL
    

Replace SA_EMAIL with the email address of your [service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

### Grant Permissions

The service account you use will need the following roles:

  * [`roles/logging.logWriter`](https://docs.cloud.google.com/iam/docs/roles-permissions/logging)— Required to store build logs in Cloud Logging.
  * [`roles/artifactregistry.writer`](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant)— Required to store build images in Artifact Registry. For the default behavior, the service account needs access to repositories named "gcf-artifacts" and "cloud-run-source-deploy". Access to the repositories can be set on the repository's IAM policy. You can alternatively provide your own artifact repository through `dockerRepository` field.
  * [`roles/storage.objectViewer`](https://docs.cloud.google.com/iam/docs/roles-permissions/storage)— Required to retrieve the function source from the Cloud Storage bucket, and to store build images in Container Registry. For the default behavior, the service account needs access to buckets named "gcf-sources-*". This can be accomplished by adding an IAM condition to the role grant such as: `(resource.type == "storage.googleapis.com/Object" && (resource.name.startsWith("gcf-sources-")))`

  * [`roles/storage.objectAdmin`](https://docs.cloud.google.com/iam/docs/roles-permissions/storage)— Required for container registry (now deprecated). It needs access to buckets named `*.artifacts.PROJECT_ID.appspot.com` is needed to access the container registry.




Grant the following roles using the [Google Cloud CLI](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-grant-single-role-gcloud), or use [Google Cloud console](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-grant-single-role-console).
    
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SA_EMAIL \
        --role=roles/logging.logWriter
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SA_EMAIL \
    --role=roles/artifactregistry.writer
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SA_EMAIL \
    --role=roles/storage.objectViewer
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
    --member=serviceAccount:SA_EMAIL \
    --role=roles/storage.objectAdmin
    

Replace the following:

  * PROJECT_ID: Your [Google Cloud project ID](https://docs.cloud.google.com/sdk/gcloud/reference/projects).
  * SA_EMAIL: The email address of your [service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

**Note:** If you are using a service account from a different project, see [Configure user-specified service accounts](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

## VPC Service Controls considerations

If you have a VPC Service Controls perimeter protecting both your project and the Cloud Run functions API, and if you're using the Compute Engine default service account as the **Cloud Build Service Account** role for Cloud Run functions, you must create the following ingress rules:

  * Allow Compute Engine default service account ingress to all methods on both Cloud Storage and Cloud Logging APIs.
  * Allow the service account `service-[PROJECT_NUMBER]@gcf-admin-robot.iam.gserviceaccount.com` ingress to all methods on both Cloud Storage and Cloud Logging APIs.



## Deploy a function with a custom service account

You can use the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) to deploy a function that uses a custom service account for Cloud Build:

  * The `--build-service-account` flag specifies an IAM service account whose credentials will be used for the build step. If a custom service account is not provided, the function uses the project's default service account for Cloud Build.
  * You can optionally use a [private pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool), which you specify using the [`--build-worker-pool`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--build-worker-pool) flag.


    
    
    gcloud functions deploy FUNCTION_NAME \
       --no-gen2 \
       --region=REGION \
       --project=PROJECT_ID \
       --runtime=RUNTIME \
       --entry-point=CODE_ENTRYPOINT \
       --build-service-account=projects/PROJECT_ID/serviceAccounts/SA_EMAIL \
       --memory=256Mi \
       --trigger-http \
       --source=.
    

Replace the following:

  * FUNCTION_NAME: The name under which you deployed your function.
  * REGION: The name of the [Google Cloud region](https://docs.cloud.google.com/functions/1stgendocs/locations) where you want to deploy your function (for example, `us-west1`).
  * PROJECT_ID: Your [Google Cloud project ID](https://docs.cloud.google.com/sdk/gcloud/reference/projects).
  * RUNTIME: The runtime ID of a [supported runtime version](https://docs.cloud.google.com/static/functions/docs/runtime-support#node.js) to run your function, for example, `nodejs18`.
  * CODE_ENTRYPOINT: The [entry point](https://docs.cloud.google.com/functions/1stgendocs/writing#entry-point) to your function in your source code. This is the code that will be executed when your function runs.
  * SA_EMAIL: The email address of your [service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

**Note:** There is no way to set a single service account across all functions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
