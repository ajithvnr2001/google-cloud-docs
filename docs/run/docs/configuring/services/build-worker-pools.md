---
url: https://docs.cloud.google.com/run/docs/configuring/services/build-worker-pools/
title: Set build worker pools (source deploy) \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:04.232300+00:00
---

# Set build worker pools (source deploy)  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/build-worker-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set build worker pools (source deploy) Stay organized with collections  Save and categorize content based on your preferences. 

When you deploy your source code to Cloud Run, that source is stored in a Cloud Storage bucket. Cloud Build then automatically builds your code into a container image and pushes that image to an image registry. Each build runs on its own worker. Cloud Run imports the built image when deploying.

If you wanted to customize the build worker pool that Cloud Build uses for a VPC Service Controls secured build context, you would customize the worker pool. This page is relevant for platform developers who are deploying Cloud Run [services](https://docs.cloud.google.com/run/docs/deploying-source-code) or [functions](https://docs.cloud.google.com/run/docs/deploy-functions) from source using the Google Cloud CLI, and configuring private pools that are used by Cloud Build. The build worker pools gcloud CLI flags are supported for [source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) (`--source`), and not supported for [container image deployments](https://docs.cloud.google.com/run/docs/deploying) (`--image`).

## Before you begin

  * Enable the Cloud Run Admin API and Cloud Build APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com,cloudbuild.googleapis.com)

After the Cloud Run Admin API is enabled, the Compute Engine default service account is automatically created.




### Required roles

You or your administrator must grant the deployer account and the Cloud Build service account the following IAM roles.

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



#### Click to view required roles for the Cloud Build service account

Cloud Build automatically uses the [Compute Engine default service account](https://docs.cloud.google.com/build/docs/cloud-build-service-account) as the default Cloud Build service account to build your source code and Cloud Run resource, unless you override this behavior. For Cloud Build to build your sources, ask your administrator to grant [Cloud Run Builder](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.builder) (`roles/run.builder`) to the Compute Engine default service account on your project:
    
    
      gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com \
          --role=roles/run.builder
      

Replace `PROJECT_NUMBER` with your Google Cloud project number, and `PROJECT_ID` with your Google Cloud project ID. For detailed instructions on how to find your project ID, and project number, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

Granting the Cloud Run builder role to the Compute Engine default service account takes a couple of minutes to [propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

**Note:**

The [ `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) prevents the Editor role from being automatically granted to default service accounts. If you created your organization after May 3, 2024, this constraint is enforced by default. 

We strongly recommend that you enforce this constraint to disable the automatic role grant. If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Secure your build with private pools

By default, Cloud Build has unlimited internet access during the build process. If you have set up a VPC Service Controls (VPC SC) perimeter and want to limit the build's access only to dependencies stored inside the perimeter (for example, npm packages), you can use the [Cloud Build private worker pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) feature.

In general, follow these steps to set up your private pool:

  1. Create your private worker pool. See [Creating and managing private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).
  2. Configure your VPC Service Controls perimeter. See [Using VPC Service Controls](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).

  3. If your private worker pool is in a different project than your Cloud Run service, you need to grant the Cloud Run [Service Agent](https://docs.cloud.google.com/iam/docs/service-agents) (`service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com`) the [Cloud Build WorkerPool User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.workerPoolUser) (`cloudbuild.workerPoolUser`) role so that the Cloud Build service can access the worker pool.
         
         gcloud projects add-iam-policy-binding PRIVATE_POOL_PROJECT_ID \
             --member serviceAccount:service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com \
             --role roles/cloudbuild.workerPoolUser

Replace:

     * PROJECT_NUMBER with the project number where the service runs.
     * PRIVATE_POOL_PROJECT_ID with the _ID_ of the project in which the worker pool is located. See [Running builds in a private pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool#permissions) for more information.
  4. Deploy your service from source to build using a private pool:

###  gcloud 

To specify a private pool to build when deploying from source code, use the `--build-worker-pool` flag:
         
         gcloud run deploy SERVICE \
             --source . \
             --build-worker-pool WORKER_POOL

Replace:

     * SERVICE with name of your service.
     * WORKER_POOL with the name of the private pool.

If you are deploying a function, add the `--function` flag with the function entry point from your source code.




## Delete build worker pools

You can delete build worker pools for existing services.

###  gcloud 

To clear the Cloud Build worker pool for source deployments, use the `--clear-build-worker-pool` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --clear-build-worker-pool WORKER_POOL

Replace:

  * SERVICE with name of your service.
  * WORKER_POOL with the name of the private pool you would like to delete.



If you are deploying a function, add the `--function` flag with the function entry point from your source code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
