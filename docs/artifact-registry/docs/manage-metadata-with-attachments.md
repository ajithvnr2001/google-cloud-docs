---
url: https://docs.cloud.google.com/artifact-registry/docs/manage-metadata-with-attachments/
title: Manage artifact metadata \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:04.598697+00:00
---

# Manage artifact metadata  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/manage-metadata-with-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage artifact metadata Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Artifact Registry attachments let you store and manage metadata files associated with your artifacts. You can list, inspect, download, and delete attachments using the Google Cloud console, the gcloud CLI, or Oras for Docker container images.

To learn how to create an attachment, see [Store artifact metadata in attachments](https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments).

## Before you begin

Optional: [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).

### Required roles

To get the permissions that you need to manage attachments, ask your administrator to grant you the following IAM roles on the repository: 

  * View and download attachments: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Create attachments: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete attachments: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List attachments

An artifact in Artifact Registry can have any number of attachments that refer to it. You can list attachments by using the Google Cloud console, the gcloud CLI, or, for Docker-format container images only, Oras.

###  Console 

**Note:** Viewing attachments for non-Docker Artifact Registry repositories in the Google Cloud console is in [public preview](https://cloud.google.com/products/#product-launch-stages).

  1. In the Google Cloud console, open the **Repositories** page.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the repository name to see images in your repository.

  3. To see the versions of an image, click the image name.

  4. Click the appropriate image version.

  5. To see the attachments for that version, click the **Attachments** tab.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `TARGET`: the fully qualified version name. For Docker images only, you can also use the Artifact Registry URI of the artifact the attachment refers to. In the URI, you can use the digest or, for Docker images, the tag—for example, `us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments list \
        --target=TARGET

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments list `
        --target=TARGET

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments list ^
        --target=TARGET

For more information, see the [`gcloud artifacts attachments list`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/list) command. 

###  Oras (Docker only) 

Before running the command, make the following replacement:

  * `IMAGE_URI`: the URI of the target image referred to by any listed attachments.


    
    
    oras discover --distribution-spec v1.1-referrers-api IMAGE_URI
    

The following example lists attachments for a container image, `my-image`, identified by its URI and tag:
    
    
    oras discover --distribution-spec v1.1-referrers-api \
    us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1
    

Where:

  * `v1.1-referrers-api` is the Referrer API used. For more information, see the details in the [distribution spec](https://github.com/opencontainers/distribution-spec/blob/main/spec.md#listing-referrers).

  * `us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1` is the URI including the tag of the container image version to list attachments for.




For a full guide and more examples, see the [`oras discover` documentation](https://oras.land/docs/commands/oras_discover/).

## Describe attachments

Before using any of the command data below, make the following replacements: 

  * `ATTACHMENT`: the fully qualified name of the attachment, such as `projects/my-project/locations/us-west1/repositories/my-repo/attachments/my-attachment`. Alternatively, provide only the attachment ID and use the `--location` and `--repository` flags.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments describe ATTACHMENT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments describe ATTACHMENT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments describe ATTACHMENT

For more information, see the [`gcloud artifacts attachments describe`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/describe) command. 

## Download attachments

You can download attachments by using the gcloud CLI or, for Docker-format container images only, Oras.

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `ATTACHMENT`: the fully qualified name of the attachment, such as `projects/my-project/locations/us-west1/repositories/my-repo/attachments/my-attachment`. Alternatively, provide only the attachment ID and use the `--location` and `--repository` flags.
  * `DESTINATION`: the path in your local file system to download the attachment to.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments download ATTACHMENT \
        --destination=DESTINATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments download ATTACHMENT `
        --destination=DESTINATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments download ATTACHMENT ^
        --destination=DESTINATION

For attachments in Docker-format repositories, as an alternative to providing `ATTACHMENT`, you can provide the `--oci-version-name` flag followed by the attachment's full version name or Artifact Registry URI. You can use either the digest or the tag—for example, `projects/my-project/locations/us-west1/repositories/my-repo/packages/my-package/versions/sha256:abc123`.  
  
For more information, see the [`gcloud artifacts attachments download`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/download) command. 

###  Oras (Docker only) 

Before running the command, make the following replacements:

  * `DESTINATION`: the destination directory for your attachment.

  * `ATTACHMENT_URI`: the URI of the attachment to download. This is the URI for the image container the attachment refers to, followed by the attachment's unique SHA.



    
    
    oras pull -o DESTINATION ATTACHMENT_URI
    

The following example downloads an attachment identified by its URI and digest:
    
    
    oras pull -o . us-west1-docker.pkg.dev/my-project/my-repo/my-image@sha256:xxxx
    

Where:

  * `-o .` names the current directory as the download destination.

  * `us-west1-docker.pkg.dev/my-project/my-repo/my-image@sha256:xxxx` is the image URI including the digest of the attachment to download.




For a full guide and more examples, see the [`oras pull` documentation](https://oras.land/docs/commands/oras_pull/).

## Delete attachments

You can delete attachments directly by using the Google Cloud console or the gcloud CLI. You can delete attachments indirectly by deleting the artifact it refers to.

### Delete attachments directly

You can delete attachments directly with one of the following options:

###  Console (Docker only) 

  1. In the Google Cloud console, open the **Repositories** page.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the repository name to see images in your repository.

  3. Click the image name to see versions of that image.

  4. Click the version of the image you to see attachments for.

  5. Click the **Attachments** tab to see attachments for that version.

  6. Click the digest of the attachment to delete.

  7. Click **DELETE**.

  8. In the confirmation dialog, click **DELETE**.




###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `ATTACHMENT`: the fully qualified name of the attachment, such as `projects/my-project/locations/us-west1/repositories/my-repo/attachments/my-attachment`. Alternatively, provide only the attachment ID and use the `--location` and `--repository` flags.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments delete ATTACHMENT

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments delete ATTACHMENT

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts attachments delete ATTACHMENT

For more information, see the [`gcloud artifacts attachments delete`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/delete) command. 

### Delete attachments indirectly

If an artifact is deleted, all attachments with the deleted artifact's version name as their `target` are also deleted. This applies to both the manual deletion of artifacts and to deletions caused by cleanup policies.

**Note:** Cleanup policies don't apply directly to attachments. However, if a cleanup policy deletes an artifact, all attachments that have the deleted artifact's version as their `target` are deleted.

## What's next

  * Read about [Software supply chain security](https://docs.cloud.google.com/software-supply-chain-security/docs/overview).
  * Learn more about [Software Bill of Materials (SBOM)](https://www.cisa.gov/sbom)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
