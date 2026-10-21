---
url: https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments/
title: Store artifact metadata in attachments \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:19.018679+00:00
---

# Store artifact metadata in attachments  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/store-artifact-metadata-in-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Store artifact metadata in attachments Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to store metadata related to an artifact stored in Artifact Registry as an _attachment_.

Metadata stored in attachments can include information about artifact vulnerabilities, build provenance, package contents, certification, vulnerability assessment, Software Bill of Materials (SBOM) and more. Information stored in Artifact Registry attachments can be used by policy systems and inspected by users to ensure compliance.

For more information about working with attachments, see [Manage metadata with attachments](https://docs.cloud.google.com/artifact-registry/docs/manage-metadata-with-attachments).

## Before you begin

  1. If you don't already have one, [create a standard-mode repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. (Optional) [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).



### Required roles

To get the permissions that you need to create attachments, ask your administrator to grant you the [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) IAM role on the repository. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an attachment

For Docker repositories, attachments must be [OCI artifacts](https://github.com/opencontainers/image-spec/blob/main/manifest.md#guidelines-for-artifact-usage). For all formats other than Docker, attachments can be any file type.

To create an attachment, complete the following steps:

###  gcloud (all formats) 

Before using any of the command data below, make the following replacements: 

  * `ATTACHMENT`: the fully qualified name of the attachment, such as `projects/my-project/locations/us-west1/repositories/my-repo/attachments/my-attachment`. Alternatively, provide only the attachment ID and use the `--location` and `--repository` flags.
  * `TARGET`: the fully qualified version name. For Docker images only, you can also use the Artifact Registry URI of the artifact the attachment refers to. In the URI, you can use the digest or, for Docker images, the tag—for example, `us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1`.
  * `TYPE`: the attachment's `type` attribute. For Docker images, the `type` must comply with [OCI specifications for the `artifactType` property](https://github.com/opencontainers/image-spec/blob/main/manifest.md#image-manifest-property-descriptions).
  * `ATTACHMENT_NAMESPACE`: a variable specific to attachments that identifies the attachment data source, such as `example.com`.
  * `FILES`: a comma-separated list of local files to include in the attachment.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud artifacts attachments create ATTACHMENT \
        --target=TARGET \
        --attachment-type=TYPE \
        --attachment-namespace=ATTACHMENT_NAMESPACE \
        --files=FILES

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud artifacts attachments create ATTACHMENT `
        --target=TARGET `
        --attachment-type=TYPE `
        --attachment-namespace=ATTACHMENT_NAMESPACE `
        --files=FILES

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    gcloud artifacts attachments create ATTACHMENT ^
        --target=TARGET ^
        --attachment-type=TYPE ^
        --attachment-namespace=ATTACHMENT_NAMESPACE ^
        --files=FILES

For more information, see the [`gcloud artifacts attachments create`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/attachments/create) command. 


###  Oras (Docker only) 

When creating an attachment with Oras, Artifact Registry generates a random UUID to use as the attachment name.

Before using Oras, complete the following steps:

  1. [Install Oras 1.2 or later](https://oras.land/docs/installation/). To verify your version, run the `oras version` command.

  2. Configure Oras to [authenticate](https://oras.land/docs/how_to_guides/authentication/) with Artifact Registry.




Before running the command, make the following replacements:

  * `ARTIFACT_TYPE`: the [`artifactType`](https://github.com/opencontainers/image-spec/blob/main/manifest.md#image-manifest-property-descriptions) of the attachment.

  * `IMAGE_URI`: the URI for the image container the attachment refers to.

  * `FILE`: a local file to include as metadata in the attachment.

  * `MEDIA_TYPE`: the [`mediaType`](https://github.com/opencontainers/image-spec/blob/main/media-types.md) of the layer.



    
    
      oras attach --artifact-type ARTIFACT_TYPE IMAGE_URI FILE:MEDIA_TYPE
    

The following example creates an attachment consisting of a file, `hello-world.txt`, that refers to a container image, `my-image`, identified by its URI and tag:
    
    
      oras attach --artifact-type doc/example \
      us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1 \
      hello-world.txt:application/vnd.me.hi
    

Where:

  * `doc/example` defines the `artifactType` property of the attachment.

  * `us-west1-docker.pkg.dev/my-project/my-repo/my-image:tag1` is the URI including the tag of the container image version the attachment will refer to.

  * `hello-world.txt` is the local file that the attachment will hold as its data.

  * `application/vnd.me.hi` defines the `mediaType` of the layer.




For a full guide and more examples, see the [`oras attach` documentation](https://oras.land/docs/commands/oras_attach/).

## Manage attachments with cleanup policies

Docker repository attachments, including build provenance, are deleted when artifacts they're attached to are deleted. If you use [cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy-overview) to delete images from your repository, then by default, the attachments on those images will be deleted as well.

To ensure that attachments you want to keep aren't accidentally deleted by a cleanup policy, you can assign a [tag](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos) to an image that has attachments you want to keep. Then, you can configure a cleanup policy to retain images with those tags. For example, you could assign a `production-signed` tag to images with attached build provenance.

## what's next

  * [Manage artifact metadata](https://docs.cloud.google.com/artifact-registry/docs/manage-metadata-with-attachments).
  * Learn how to [generate and store SBOMs](https://docs.cloud.google.com/artifact-analysis/docs/generate-store-sboms) for container images.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
