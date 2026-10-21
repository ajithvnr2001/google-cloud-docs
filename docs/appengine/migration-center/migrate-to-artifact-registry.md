---
url: https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry/
title: Migrate App Engine container images to Artifact Registry \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:40.568209+00:00
---

# Migrate App Engine container images to Artifact Registry  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/migrate-to-artifact-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate App Engine container images to Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

### Region ID

The `REGION_ID` is an abbreviated code that Google assigns based on the region you select when you create your app. The code does not correspond to a country or province, even though some region IDs may appear similar to commonly used country and province codes. For apps created after February 2020, `REGION_ID.r` is included in App Engine URLs. For existing apps created before this date, the region ID is optional in the URL.

Learn more [about region IDs](https://docs.cloud.google.com/appengine/docs/standard/python/how-requests-are-routed#region-id). 

OK

Container Registry is deprecated and was [shutdown](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown) on March 18, 2025. We recommend that you use [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) for storing and managing container images. By default, new deployments created after March 5, 2025 use Artifact Registry instead of Container Registry for storing application images. Artifact Registry provides the same container management features as Container Registry and includes additional features and benefits. As a fully managed service with support for both container images and non-container artifacts, Artifact Registry extends the capabilities of Container Registry.

For projects created before May 2024 or that haven't yet run the [automated migration tooling](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar), follow the steps in this guide to enable App Engine to automatically migrate your deployment flows.

## App Engine standard environment

Most of your application components in the standard environment follow an automated migration process. However, for a smooth transition to Artifact Registry, ensure that your service account has the following required permissions:

  * For existing standard deployments, the deploying service account (either the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts#assign_an_app-level_default_service_account) (_`PROJECT_ID @appspot.gserviceaccount.com`_) or your [custom service account](https://docs.cloud.google.com/appengine/docs/standard/configure-service-accounts)) must have a role that grants the explicit Artifact Registry write permission `artifactregistry.repositories.uploadArtifacts`. To find the roles associated with your deploying service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).

  * New deployments can use Artifact Registry if any of the following roles are present in the service account associated with deployments:

    * [Editor role](https://docs.cloud.google.com/appengine/docs/standard/roles#basic_roles)

    * [Pre-defined Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) with write access, such as Artifact Registry Writer (`roles/artifactregistry.writer`).

    * Custom role that grants `artifactregistry.repositories.uploadArtifacts` permission. You can verify custom roles access from the [Google Cloud console](https://docs.cloud.google.com/iam/docs/creating-custom-roles#get-metadata) or by running the [`gcloud iam roles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe) command.

If none of these roles are present, grant the Artifact Registry Writer role (`roles/artifactregistry.writer`) to your deploying service account.




Failing to provide the required permissions prevents you from deploying new versions in the standard environment.

During automated migrations, Google Cloud might create new repositories and copy images from Container Registry to Artifact Registry.

## App Engine flexible environment

Most of your application components in the flexible environment follow an automated migration process. However, for a smooth transition to Artifact Registry, ensure that your service account has the following required permissions:

  * For existing flexible deployments to work as expected with Artifact Registry, the deploying service account (either the [App Engine default service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-accounts#assign_an_app-level_default_service_account) (_`PROJECT_ID @appspot.gserviceaccount.com`_) or your [custom service account](https://docs.cloud.google.com/appengine/docs/flexible/configure-service-account)) must have a role that grants the explicit Artifact Registry permissions such as `artifactregistry.repositories.downloadArtifacts` for read and `artifactregistry.repositories.uploadArtifacts` for write. To find the roles associated with your deploying service account, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#view-access).

  * New deployments can use Artifact Registry, if any of the following roles are present in the service account associated with deployments:

    * [Editor role](https://docs.cloud.google.com/appengine/docs/flexible/roles#basic_roles)

    * [Pre-defined Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#roles) with read and write access, such as Artifact Registry Writer (`roles/artifactregistry.writer`).

    * Custom role that grants `artifactregistry.repositories.downloadArtifacts` and `artifactregistry.repositories.uploadArtifacts` permissions. You can verify custom roles access from the [Google Cloud console](https://docs.cloud.google.com/iam/docs/creating-custom-roles#get-metadata) or by running the [`gcloud iam roles describe`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/roles/describe) command.

If none of these roles are present, grant the Artifact Registry Repository Administrator role (`roles/artifactregistry.repoAdmin`) to your deploying service account.




Failing to provide the required permissions prevents you from deploying applications in the flexible environment. Scaling and restarting instances also fail.

During automated migrations, Google Cloud might create new repositories and copy images from Container Registry to Artifact Registry.

### Migrate to Artifact Registry for manually built container images

The automated migration process doesn't apply if you previously deployed your apps by using [prebuilt or manually built container images](https://docs.cloud.google.com/appengine/docs/flexible/testing-and-deploying-your-app?tab=python#remote-container-build) from [Container Registry](https://docs.cloud.google.com/container-registry/docs/pushing). For example, the automated migration process doesn't work if you built container images with Docker, pushed these images to the Container Registry, and deployed your apps by using the `gcloud app deploy --image-url` command.

If you use prebuilt or manually built container images from Container Registry to deploy your apps, choose one of the following options to migrate to Artifact Registry:

  * Use the automatic migration tool to migrate from Container Registry to `gcr.io` repositories that are hosted on Artifact Registry. You don't need to redeploy new versions of your service if you use this tool. For more information, see [Automatically migrate from Container Registry to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar).

  * Manually move the container images from Container Registry to Artifact Registry and redeploy new versions of your service. For more information, see [Manual migration to `gcr.io` repositories in Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/manual-gcr-repositories).

  * Use the [`copy-only`](https://docs.cloud.google.com/artifact-registry/docs/transition/auto-migrate-gcr-ar#copy_images) flag to copy your container images to Artifact Registry and redeploy new versions of your service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
