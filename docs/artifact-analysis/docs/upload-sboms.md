---
url: https://docs.cloud.google.com/artifact-analysis/docs/upload-sboms/
title: Upload SBOMs \u00a0|\u00a0 Artifact Analysis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:39:45.298278+00:00
---

# Upload SBOMs  |  Artifact Analysis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-analysis/docs/upload-sboms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Analysis ](https://docs.cloud.google.com/artifact-analysis/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-analysis/docs/ods-quickstart)



Send feedback 

#  Upload SBOMs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to upload a software bill of materials (SBOM) file to Cloud Storage to help track and attest to the components of container images you store in Artifact Registry.

For information on Cloud Storage pricing, see [Pricing](https://cloud.google.com/storage/pricing).

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

  4. Enable the Artifact Registry, Container Analysis APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://artifactregistry.googleapis.com,https://containeranalysis.googleapis.com,)

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

  10. Enable the Artifact Registry, Container Analysis APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=https://artifactregistry.googleapis.com,https://containeranalysis.googleapis.com,)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Have a Docker repository in Artifact Registry with the container image that your SBOM describes. If you are not familiar with Artifact Registry, see the [Docker quickstart](https://docs.cloud.google.com/artifact-registry/docs/docker/store-docker-container-images).
  15. Have an SBOM file ready to upload in one of the [supported formats](https://docs.cloud.google.com/artifact-analysis/docs/upload-sbom#formats).



### Required roles

To get the permissions that you need to create and manage Cloud Storage buckets and SBOM files , ask your administrator to grant you the following IAM roles on the project: 

  * If you are using the default Cloud Storage bucket, to manage storage buckets: Storage Admin(`roles/storage.admin`) 
  * If you are specifying a Cloud Storage bucket, to manage storage buckets: Storage Object Admin(`roles/storage.objectAdmin`) 
  * If a note for the SBOM reference already exists: [Container Analysis Notes Attacher ](https://docs.cloud.google.com/iam/docs/roles-permissions/containeranalysis#containeranalysis.notes.attacher) (`roles/containeranalysis.notes.attacher`) 
  * To create a new note for SBOM reference occurrences in the current project: Container Analysis Notes Editor(`(roles/containeranalysis.notes.editor`) 
  * To create an SBOM reference occurrence: Container Analysis Occurrences Editor(`roles/containeranalysis.occurrences.editor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Supported formats

Your SBOM file must be a JSON file in one of the following formats:

  * [Software Package Data Exchange (SPDX)](https://spdx.dev/) version 2.2 or 2.3
  * [CycloneDX](https://cyclonedx.org/) version 1.4 or 1.5



## Upload your SBOM

Use the following command to upload your SBOM:
    
    
    gcloud artifacts sbom load /
        --source SOURCE /
        --uri URI
    

Where:

  * SOURCE: the path to the SBOM file to upload.
  * URI: the URI for the Docker image that the SBOM file describes. Images can be in either tag format, or digest format. Images provided in tag format will be resolved into digest format.



### Optional flags

  * `--destination`: specifies a Cloud Storage bucket to use instead of the default one.
  * `--kms-key-version`: provides a key version to sign the SBOM reference occurrence payload. You can use this key to verify the origin of the SBOM.



For example, the following command uploads a JSON file `my-sbom.bom.json` that was generated from the tagged image `us-east1-docker.pkg.dev/my-image-repo/my-image`, and signs the SBOM reference occurrence with the KMS key version ending in `my-key/cryptoKeyVersions/1`.
    
    
    gcloud artifacts sbom load /
    --source=my-sbom.bom.json
    --uri=us-east1-docker.pkg.dev/my-image-repo/my-image
    --kms-key-version=projects/my-project/locations/us/keyRings/my-key-ring/cryptoKeys/my-key/cryptoKeyVersions/1
    

The following command uploads a JSON file `my-sbom.spdx.json` that is associated with the image digest `my-local-image@sha256:abcxyz`, and stores the file in the Cloud Storage bucket `gs://my-sbom-bucket`.
    
    
    gcloud artifacts sbom load /
        --source=my-sbom.spdx.json /
        --uri=my-local-image@sha256:abcxyz /
        --destination=gs://my-sbom-bucket
    

Artifact Analysis uploads your SBOM to Cloud Storage and creates an SBOM [reference occurrence](https://docs.cloud.google.com/artifact-analysis/docs/sbom-overview#sbom-ref).

You can view SBOMs by using the Google Cloud console or the gcloud CLI. If you want to locate the Cloud Storage bucket that contains your SBOMs, you must [search for SBOMs using the gcloud CLI](https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies#gcloud).

## What's next

  * [View SBOMs and dependencies](https://docs.cloud.google.com/artifact-analysis/docs/view-sboms-dependencies).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
