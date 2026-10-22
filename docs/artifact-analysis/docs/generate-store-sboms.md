---
url: https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms/
title: Generate and store SBOMs \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:19:07.398353+00:00
---

# Generate and store SBOMs  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Generate and store SBOMs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create and store a software bill of materials (SBOM) listing the dependencies in your container images.

When you store container images in Artifact Registry and scan them for vulnerabilities with Artifact Analysis, you can then generate an SBOM using the Google Cloud CLI.

For information on using vulnerability scanning, see [Automatic scanning](https://docs.cloud.google.com/artifact-analysis/docs/artifact-analysis#automatic_scanning) and [Pricing](https://cloud.google.com/artifact-analysis/pricing).

Artifact Analysis stores SBOMs in Cloud Storage. For more information on Cloud Storage costs, see [Pricing](https://cloud.google.com/storage/pricing).

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry, Container Analysis, Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://artifactregistry.googleapis.com,https://containeranalysis.googleapis.com,https://containerscanning.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Artifact Registry, Container Analysis, Container Scanning APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://artifactregistry.googleapis.com,https://containeranalysis.googleapis.com,https://containerscanning.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Create a Docker repository in Artifact Registry and push a container image to the repository. If you are not familiar with Artifact Registry, see the [Docker quickstart](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).



### Required roles

To get the permissions that you need to manage Cloud Storage buckets and upload SBOM files, ask your administrator to grant you the [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Generate an SBOM file

To generate an SBOM file, use the following command:
    
    
    gcloud artifacts sbom export --uri=LOCATION-docker.pkg.dev/PROJECT_ID/REPOSITORY/IMAGE_NAME
    

Where

  * LOCATION is the location of the Artifact Registry repository.
  * PROJECT_ID is the ID of the project that contains the Artifact Registry repository.
  * REPOSITORY is the name of the Artifact Registry repository that contains the image.
  * IMAGE_NAME is the name of the image. Images can be in either [tag format](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#tags), or [digest format](https://docs.cloud.google.com/artifact-registry/docs/container-concepts#manifests). Images provided in tag format will be resolved into digest format.



Artifact Analysis stores your SBOM in Cloud Storage. If you don't yet have a Cloud Storage bucket for the same region as your image, Cloud Storage creates one for you with a name of `artifactanalysis-<var>REGION</var>-<var>PROJECT_NUMBER</var>` and sends your SBOM to that bucket. Additional SBOMs in that region are sent to the same bucket.

You can view SBOMs by using the Google Cloud console or the gcloud CLI. If you want to locate the Cloud Storage bucket that contains your SBOMs, you must [search for SBOMs using the gcloud CLI](https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies#gcloud).

**Note:** If you're using images with `gcr.io` domain names, SBOMs might not appear immediately. SBOM generation takes at least 24 hours from the time when you set up hostname redirection.

## Generate an SBOM without vulnerability scanning

If you want to generate an SBOM, but you don't want ongoing vulnerability scanning for your project, you can still export an SBOM if you enable the Container Scanning API before you push the image to Artifact Registry. After your image is pushed to Artifact Registry, and you have exported an SBOM, you must disable the Container Scanning API to prevent being billed for further vulnerability scanning.

## What's next

  * [Upload your own SBOM](https://docs.cloud.google.com/artifact-analysis/docs/upload-sbom)
  * [View SBOMs and dependencies](https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
