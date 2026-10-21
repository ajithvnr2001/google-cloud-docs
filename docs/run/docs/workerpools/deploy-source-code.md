---
url: https://docs.cloud.google.com/run/docs/workerpools/deploy-source-code/
title: Deploy worker pools from source code \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:58.668502+00:00
---

# Deploy worker pools from source code  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/workerpools/deploy-source-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deploy worker pools from source code Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to deploy a new worker pool or worker pool revision to Cloud Run directly from source code using a single gcloud CLI command, `gcloud run worker-pools deploy` with the [`--source`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--source) flag. **Note:** The deploy command defaults to source deployment if you don't supply `--image` or `--source` flags. Behind the scenes, this command uses [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) and Cloud Build to automatically build container images from your source code without having to install Docker on your machine or set up buildpacks or Cloud Build. By default, Cloud Run uses the [default machine type provided by Cloud Build](https://cloud.google.com/build/pricing). Running [`gcloud run worker-pools deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy) eliminates the need to also run the [`gcloud builds submit`](https://docs.cloud.google.com/sdk/gcloud/reference/builds/submit) command. 

Note that source deployments use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs) to store built containers. If your project doesn't already have an Artifact Registry repository with the name `cloud-run-source-deploy` in the region you are deploying to, this feature automatically creates an Artifact Registry repository with the name `cloud-run-source-deploy`.

If a Dockerfile is present in the source code directory, the uploaded source code is built using that Dockerfile. If no Dockerfile is present in the source code directory, Google Cloud's buildpacks automatically detects the language you are using and fetches the dependencies of the code to make a production-ready container image, using a secure base image managed by Google.

## Before you begin

  * Make sure you have set up a new project for Cloud Run as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page. 
  * Enable the Cloud Run Admin API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

After the Cloud Run Admin API is enabled, the Compute Engine default service account is automatically created.




### Required roles

To deploy from source, you or your administrator must grant the deployer account the following IAM roles.

#### Click to view required roles for the deployer account

To get the permissions that you need to build and deploy from source, ask your administrator to grant you the following IAM roles:

  * [Cloud Run Source Developer](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.sourceDeveloper) (`roles/run.sourceDeveloper`) on your project
  * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your project
  * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the Cloud Run service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Supported languages

In addition to sources with a Dockerfile, deploying from source supports the following languages using [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview):

  * Go
  * Node.js
  * Python
  * Java
  * Kotlin
  * Groovy
  * Scala
  * .NET
  * Ruby
  * PHP



Read more details about [supported language versions](https://docs.cloud.google.com/run/docs/runtime-support).

## Deploy from source with build

This section describes how to use [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) and Cloud Build to automatically build container images from your source code without having to install Docker on your machine or set up buildpacks or Cloud Build.

### Limitations

  * Deploy from source uses Artifact Registry and Cloud Build, so this feature is only available in [regions supported by Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/repo-locations#location-r) and [Cloud Build](https://docs.cloud.google.com/build/docs/locations).
  * Deploying from source is a convenience feature, and does not allow full customization of the build. For more control, build the container image using Cloud Build, for example, using `gcloud builds submit`, and then [deploy the container image](https://docs.cloud.google.com/run/docs/deploy-worker-pools) using, for example, `gcloud run worker-pools deploy --image`. 
  * Deploying from source with Google Cloud's buildpacks sets the Last Modified Date of source files to Jan 1, 1980. This is the default behavior of buildpacks and is designed to support [reproducible builds](https://reproducible-builds.org/). Depending on your language framework, this can affect browser-side caching of static files. If your application is affected by this, Google recommends disabling `etag` and `Last-Modified` HTTP headers in your application.
  * Deploying from source with Google Cloud's buildpacks always uses `gcr.io/buildpacks/builder:latest`. If your preferred language or OS configuration is not available in `latest`, [use a specific builder](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder) to create an application image using your preferred builder.
  * You can deploy your worker pool from source using Kotlin and other JVM languages such as [Java](https://docs.cloud.google.com/docs/buildpacks/java). The language you use must conform to the following rules:

    * You can build the application using Maven or Gradle.
    * The build file contains all the plugins required to produce classes.



### Before you deploy with build

Before you deploy from source with build:

  * Follow the steps in Before you begin.

  * Enable the Cloud Build API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com)




#### Required roles

To deploy from source with build, you or your administrator must grant the Cloud Build service account the following IAM roles.

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

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Deploy with build

To deploy from source code:

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Change to your source directory. The source directory uses a Dockerfile if present, although it's not required.

  3. Build and deploy your worker pool:
         
         gcloud run worker-pools deploy WORKERPOOL --source .

Replace `WORKERPOOL` with the name you want for your worker pool.
  4. Respond to any prompts to install required APIs by responding `y` when prompted. You only need to do this once for a project. Respond to other prompts by supplying the platform and region, if you haven't set defaults for these as described in the [setup](https://docs.cloud.google.com/run/docs/setup) page.

  5. Wait for the build and deploy to complete. When finished, Cloud Run displays a success message.




## Automating building from source

As a best practice for avoiding unversioned changes in local source, Google recommends that you automatically deploy when changes are pushed to your Git repository. To make this easier, you can connect and configure continuous deployment to your Cloud Run worker pool. By connecting your GitHub repositories to Cloud Run, you can configure builds and deploy your repositories without writing Dockerfiles or build files.

## What's next

After you deploy a Cloud Run worker pool, you can do the following:

  * [View worker pool logs](https://docs.cloud.google.com/run/docs/logging)
  * [Monitor worker pools](https://docs.cloud.google.com/run/docs/monitoring)
  * [Set memory limits](https://docs.cloud.google.com/run/docs/configuring/workerpools/memory-limits)
  * [Set environment variables](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables)
  * [Manage the worker pool](https://docs.cloud.google.com/run/docs/workerpools/managing/workerpools)
  * [Manage worker pool revisions](https://docs.cloud.google.com/run/docs/workerpools/managing/revisions)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
