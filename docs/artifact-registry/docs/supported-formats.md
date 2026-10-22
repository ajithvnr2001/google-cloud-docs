---
url: https://docs.cloud.google.com/artifact-registry/docs/supported-formats/
title: Supported formats \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:45.195186+00:00
---

# Supported formats  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/supported-formats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Supported formats Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store and manage container images, language packages, operating system packages, and generic files in format-specific repositories. You can push and pull artifacts using client tools and integrate with Google Cloud services across the following supported formats:

Formats  
---  
Docker | Store Docker container images and Helm charts packaged in OCI format. For more information on container image formats, see Container images.   
Ruby (Preview) | Store Ruby gems that you build with RubyGems or Bundler. For more information on storing Ruby packages in Artifact Registry, see [Get started with Ruby gems](https://docs.cloud.google.com/artifact-registry/docs/ruby).  
Conda (Preview) | Store Conda packages. For more information on storing Conda packages in Artifact Registry, see [Get started with Conda packages](https://docs.cloud.google.com/artifact-registry/docs/conda).  
Maven | Store Java packages that you build with Maven or Gradle. For more information on storing Java packages in Artifact Registry, see [Get started with Java packages](https://docs.cloud.google.com/artifact-registry/docs/java).  
npm | Store Node.js packages that you manage with npm. For more information on storing Node.js packages in Artifact Registry, see [Get started with Node.js packages](https://docs.cloud.google.com/artifact-registry/docs/nodejs).  
Python | Store Python packages. For more information on storing Python packages in Artifact Registry, see [Get started with Python packages](https://docs.cloud.google.com/artifact-registry/docs/python).  
Apt | Store Debian packages that you manage with Apt. For more information on storing Debian packages in Artifact Registry, see [Get started with Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian).  
Yum | Store RPM packages that you manage with Yum and DNF. For more information on storing RPM packages, see [Get started with RPM packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm).  
Kubeflow | Store Kubeflow pipeline templates. A pipeline template lets you reuse ML workflow definitions when you're managing ML workflows in [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform).  Vertex AI is the Google Cloud ML platform for building, deploying, and managing ML models. To learn about creating pipeline templates and using them with Artifact Registry, see [Create, upload, and use a pipeline template](https://docs.cloud.google.com/vertex-ai/docs/pipelines/create-pipeline-template#use-the-template-in-kfp-client).   
Go | Store Go modules. For more information on storing Go modules in Artifact Registry, see [Get started with Go modules](https://docs.cloud.google.com/artifact-registry/docs/go).  
Generic | Store generic artifacts. Generic artifacts are versioned, immutable artifacts that don't adhere to any specific package format. For more information on storing generic artifacts in Artifact Registry, see [Work with other artifact formats](https://docs.cloud.google.com/artifact-registry/docs/generic).   
  
## Container images

Artifact Registry supports the following container image formats:

  * [Docker Image Manifest V2, Schema 1](https://docs.docker.com/registry/spec/manifest-v2-1/)
  * [Docker Image Manifest V2, Schema 2](https://docs.docker.com/registry/spec/manifest-v2-2/)
  * [Open Container Initiative (OCI) Image Format Specifications](https://github.com/opencontainers/image-spec)



### Docker V2

[Docker V2 image manifest](https://docs.docker.com/registry/spec/manifest-v2-2/) is a specification for container images that allows multi-architecture images and supports content-addressable images.

Docker V2 images supersede Docker V1 images, which are [deprecated](https://docs.cloud.google.com/container-registry/docs/support/deprecation-notices#docker_registry_v1_api_and_docker_clients_below_version_16).

### OCI Image Format

The OCI image format is a specification for container images based on the Docker Image Manifest Version 2, Schema 2 format. Artifact Registry implements the [OCI Specification](https://github.com/opencontainers/distribution-spec/blob/main/spec.md), an API protocol to help standardize distribution of content.

You can store artifacts that support the OCI image format in Artifact Registry Docker repositories. For example:

  * [Helm 3 charts](https://helm.sh/docs/topics/registries/) can be packaged in OCI format. For more information, see the Artifact Registry [Helm overview](https://docs.cloud.google.com/artifact-registry/docs/helm).
  * Singularity supports pulling [Docker and OCI images](https://docs.sylabs.io/guides/3.10/user-guide/singularity_and_docker.html) from private registries and pushing and pulling images in [Singularity Image File](https://github.com/apptainer/sif) (SIF) format with private registries.

    * Authentication is similar to authentication for [Docker clients](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication). Singularity can read settings that the credential helper added to the Docker client `config.json`. If you are using a token or service account key for password authentication, you can use the [singularity remote login](https://docs.sylabs.io/guides/3.10/user-guide/cli/singularity_remote_login.html) command to sign in with your credentials.
    * Use the [singularity pull](https://docs.sylabs.io/guides/3.10/user-guide/cli/singularity_pull.html) command with the `oras://` URI to pull images.
    * Use the [singularity push](https://docs.sylabs.io/guides/3.10/user-guide/cli/singularity_push.html) command with the `oras://` URI to push images.

For example, the following command pulls `my-app:latest` from the repository `us-west1.pkg.dev/my-project/sif-repo`.
    
    singularity pull oras://us-west1.pkg.dev/my-project/sif-repo/my-app:latest`
    




In Cloud Build, you can also set up your build config file so that OCI images are uploaded to Artifact Registry during the build process. For more information, see [`oci`](https://docs.cloud.google.com/build/docs/build-config-file-schema#oci) in the build config file schema documentation.

### Manifest lists and image indexes

[Manifest lists](https://docs.docker.com/registry/spec/manifest-v2-2/#manifest-list) are part of the Docker V2, Schema 2 and OCI images.

Manifest lists allow a single digest or tag to represent multiple forms of an image.

[Image indexes](https://github.com/opencontainers/image-spec/blob/28462ef6944123de00cf27e812309cbf5d82da71/image-index.md) are the equivalent of manifest lists in OCI images.

Like manifest lists, an image index manifest refers to multiple image manifests. Image indexes are useful for multi-platform images.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
