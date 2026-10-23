---
url: https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables/
title: Set build environment variables (source deploy) \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:56:57.942435+00:00
---

# Set build environment variables (source deploy)  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/build-environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Set build environment variables (source deploy) Stay organized with collections  Save and categorize content based on your preferences. 

Build environment variables are key-value pairs that let you pass configuration information to [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) when deploying from source code. For example, at build time, you might want to customize compiler options, specify build-time certificates, configure parameters, and so forth.

This page shows how to set build environment variables that are available at build time, and is relevant for platform developers who are deploying Cloud Run [services](https://docs.cloud.google.com/run/docs/deploying-source-code) or [functions](https://docs.cloud.google.com/run/docs/deploy-functions) from source. The build environment variable gcloud CLI flags are supported for [source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) (`--source`), and not supported for [container image deployments](https://docs.cloud.google.com/run/docs/deploying) (`--image`).

You can use environment variables for service or function configuration, but we don't recommend them as a way to store secrets such as database credentials or API keys. Store sensitive values outside both your source code and environment variables. To store secrets, we recommend using Secret Manager. To configure services that access secrets stored in Secret Manager, see [Configure secrets](https://docs.cloud.google.com/run/docs/configuring/secrets).

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

## Maximum number of build environment variables and limits

You can define up to 100 build environment variables, with a total key and value limit of 64 KiB.

## Set build environment variables

You can set build environment variables to establish new variables or completely replace existing build variables.

**Note:** Keys must start with an uppercase ASCII letter, and consist of uppercase ASCII letters, digits, and underscores. You should avoid creating variable keys with a `GOOGLE_*` prefix. [View all supported buildpacks environment variables](https://docs.cloud.google.com/docs/buildpacks/service-specific-configs).

###  gcloud 

To set build environment variables when deploying a service from source code, use the `--set-build-env-vars` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --set-build-env-vars KEY1=VALUE1,KEY2=VALUE2

Replace:

  * SERVICE with name of your Cloud Run service.
  * KEY1=VALUE1,KEY2=VALUE2 with the comma-separated list of variable names and their values that are deployed alongside a function that let you pass configuration information to buildpacks.



If you are deploying a function, add the `--function` flag with the function entry point from your source code.

## Update build environment variables

You can update build environment variables for existing services. This is a non-destructive approach that changes or adds build environment variables, but does not delete the build environment variables.

###  gcloud 

To update build environment variables for existing services, use the `--update-build-env-vars` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --update-build-env-vars KEY1=VALUE1,KEY2=VALUE2

If you are deploying a function, add the `--function` flag with the function entry point from your source code.

## Delete build environment variables

You can delete build environment variables for existing services.

###  gcloud 

To remove build environment variables for existing services, use the `--remove-build-env-vars` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --remove-build-env-vars KEY1=VALUE1,KEY2=VALUE2

Alternatively, you can clear build environment variables by using the `--clear-build-env-vars` for existing services:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --clear-build-env-vars KEY1=VALUE1,KEY2=VALUE2

If you are deploying a function, add the `--function` flag with the function entry point from your source code.

## Use a build environment variables file

You can use a build environment variables file for existing functions.

###  gcloud 

To set build environment variables from a file, use the `--build-env-vars-file` flag:
    
    
    gcloud run deploy SERVICE \
        --source . \
        --build-env-vars-file FILE_NAME.yaml

Replace FILE_NAME.yaml where the contents of the file, which should look as follows:
    
    
     KEY1: VALUE1
     KEY2: VALUE2
    

If you are deploying a function, add the `--function` flag with the function entry point from your source code.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
