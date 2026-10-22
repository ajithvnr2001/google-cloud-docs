---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/names/
title: Repository and image names \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:56.120726+00:00
---

# Repository and image names  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/names/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Repository and image names Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry uses a naming convention to identify repositories and images when you use the API, `gcloud`, and `docker` commands to interact with repositories.

## Docker repositories

The full name for a docker repository is in the following format:
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY
    

Where:

  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository.
  * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `REPOSITORY` is the name of the repository.



For example, consider an image with the following characteristics:

  * Repository location: `us-west1`
  * Repository format: `docker`
  * Repository name: `my-repo`
  * Project ID: `my-project`



The repository is specified as:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo
    

## Container image names

The full name for a container image is one of the following formats: 
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE
    

or
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE:TAG
    

or
    
    
    LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY/IMAGE@IMAGE-DIGEST
    

where:

  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) of the repository.
  * `PROJECT` is your Google Cloud console [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 
  * `REPOSITORY` is the name of the repository where the image is stored.
  * `IMAGE` is the name of the image in the repository.
  * `TAG` is the tag for the image version that you want to pull.
  * `IMAGE-DIGEST` is the sha256 hash value of the image contents. In Google Cloud console, click the specific image to see its metadata. The digest is listed as the **Image digest**. If you don't specify a tag or a digest, Artifact Registry looks for the image with the default tag `latest`. See Container image versions for information about versions.



For example, consider an image with the following characteristics:

  * Repository location: `us-west1`
  * Repository name: `my-repo`
  * Project ID: `my-project`
  * Image name: `test`
  * Tag: `staging`



This version of the image tagged with staging is specified as:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo/test:staging
    

## Container image versions

A repository can contain many container images, and these images can have different versions. To identify a specific version of an image, you can specify the image digest or tag.

Digest
    An image digest is an automatically generated hash of the image index or image manifest. Each image digest is a unique identifier for an image version and cannot be changed. The digest is the sha256 hash value of the image contents.
Tag
    

An image tag is a label and is often a human-readable string such as `v1.1` or `development`. A tag can only point to only one version of an image. In Artifact Registry, you can configure a Docker repository to allow mutable image tags or enforce immutable image tags.

  * **Mutable** : A tag points to only one version of an image, but the specific digest that it references can change.

A common approach is to tag images with a version identifier, such as `v1.1` at build time. When the build pushes multiple versions of the image to the registry with the same `v1.1` tag, the tag references the digest of the last version pushed to the registry. Although mutable image tags provide a convenient way to label versions, they can also be manipulated by a bad actor to associate a tag with a malicious version of an image.

  * **Immutable** : In the repository, a tag always points to the same image digest. If an Artifact Registry repository is configured for immutable image tags, the following actions are not permitted:

    * Delete a tagged image. Deleting untagged images is still permitted.
    * Remove a tag from an image.
    * Push an image with a tag that is already used by another version of the image in the repository.



For example, consider an image with the following characteristics:

  * Repository location: `us-west1`
  * Repository name: `my-repo`
  * Project ID: `my-project`
  * Image name: `test`
  * Tag: `staging`
  * Digest: `sha256:4d11e24ba8a615cc85a535daa17b47d3c0219f7eeb2b8208896704ad7f88ae2d`



To identify the image with the tag, append `:staging` to the image name:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo/test:staging
    

To identify it with the digest, append `@` to the image name, followed by the digest:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo/test@sha256:4d11e24ba8a615cc85a535daa17b47d3c0219f7eeb2b8208896704ad7f88ae2d
    

If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 

In the console, on the **Images** screen, the **Tags** column lists the image's tags. Click the version of the image to see metadata, including the **Image digest**.

See [Tagging Images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images#tag) for more information about tagging.

## Domain-scoped projects

If your project is scoped to your domain, the project ID includes the name of the domain followed by a colon (`:`). Because of how Docker treats colons, you must replace the colon character with a forward slash when you specify an image digest in Artifact Registry. Identify images in these types of projects using the following format:
    
    
    LOCATION-docker.pkg.dev/DOMAIN/PROJECT-ID/REPOSITORY/IMAGE@IMAGE-DIGEST
    

For example, the project with ID `example.com:my-project` could have the following image:
    
    
    us-west1-docker.pkg.dev/example.com/my-project/my-repo/image-name
    

**Note:** Scoping projects to a domain is a legacy feature. You cannot create new domain-scoped projects.

## Repository names as URLs

To access a repository or artifact in a repository in Google Cloud console, prepend `https://` to its full name.

For example, to view the repository `us-west1-maven.pkg.dev/my-project/my-repo`, use the following URL:
    
    
    https://us-west1-maven.pkg.dev/my-project/my-repo
    
    

To view the image `us-west1-docker.pkg.dev/example.com/my-project/my-repo/my-image`, use the following URL:
    
    
    https://us-west1-docker.pkg.dev/example.com/my-project/my-repo/my-image
    

Any authenticated user who has permission to access the repository can use these links.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
