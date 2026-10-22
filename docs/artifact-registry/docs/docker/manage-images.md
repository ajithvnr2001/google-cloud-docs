---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images/
title: Manage images \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:56.044785+00:00
---

# Manage images  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage images Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you organize and maintain container images across your Docker repositories. You can inspect repository contents, update or remove version tags, and delete unused versions to reduce storage costs.

For information about pushing and pulling images, see [Pushing and pulling images](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).

## Before you begin

  1. If the target repository doesn't exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.
  3. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).



### Required roles

To get the permissions that you need to manage images, ask your administrator to grant you the following IAM roles on the repository: 

  * View images, files in images, and tags: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Tag images or edit tags using Artifact Registry: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete images or remove tags: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Listing images

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can list the images using the [Google Cloud console](https://console.cloud.google.com/) or gcloud CLI.

The repository list includes both Artifact Registry and Container Registry repositories. To work with images in a Container Registry repository, see the Container Registry documentation for [managing images](https://docs.cloud.google.com/container-registry/docs/managing). 

###  Console 

To view images in a repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the repository with the container image.

  3. Click an image to see its versions.




###  gcloud 

To list all images in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults):
    
    
    gcloud artifacts docker images list
    

To list images in a repository in a specific location, run the command:
    
    
    gcloud artifacts docker images list LOCATION-docker.pkg.dev/PROJECT/REPOSITORY
    

To list all digests and tags for a specific image, run the command:
    
    
    gcloud artifacts docker images list LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE \
    --include-tags
    

Replace the following values:

  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * REPOSITORY is the name of the repository where the image is stored.
  * IMAGE is the name of the image in the repository.
  * `--include-tags` shows all versions of images, including digests and tags. If this flag is omitted, the returned list only includes top level container images.



For example, consider an image with the following characteristics:

  * Repository location: `us-west1`
  * Repository name: `my-repo`
  * Project ID: `my-project`
  * Image name: `my-image`



The full repository name is:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo
    

The full image name is:
    
    
    us-west1-docker.pkg.dev/my-project/my-repo/my-image
    

For details about the image name format, see [Repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names).

## Listing files

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can list files in a repository, files in all versions of a specified container image, or files in a specific version of an image.

For all the following commands, you can set a maximum number of files to return by adding the `--limit` flag to the command.

To list all files in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
    gcloud artifacts files list
    

To list files in a specified project, repository, and location, run the command:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION
    

To list files for all versions of a specific container image:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION \
        --package=PACKAGE
    

To list files for a specific container image version:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION \
        --package=PACKAGE \
        --version=VERSION
    

To list files for a specific tag: 
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION \
        --package=PACKAGE \
        --tag=TAG
    

Replace the following values:

  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `REPOSITORY`: the name of the repository where the image is stored.
  * `PACKAGE`: the name of the image.
  * `VERSION`: the image digest, a string starting with `sha256:`.
  * `TAG`: the tag associated with the container image.



### Examples

Consider the following image information:

  * Project: `my-project`
  * Repository: `my-repo`
  * Repository location: `us-west1`
  * Image: `my-app`



The following command lists all files in the repository `my-repo` in the location `us-west1` within the [default project](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
    gcloud artifacts files list \
        --location=us-west1 \
        --repository=my-repo
    

The following command lists files in the version of the image with the digest `sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356`
    
    
    gcloud artifacts files list \
        --project=my-project \
        --location=us-west1 \
        --repository=my-repo \
        --package=my-app \
        --version=sha256:88b205d7995332e10e836514fbfd59ecaf8976fc15060cd66e85cdcebe7fb356
    

The following command lists files in the version of the image with the tag `1.0-dev`
    
    
    gcloud artifacts files list \
        --project=my-project \
        --location=us-west1 \
        --repository=my-repo \
        --package=my-app \
        --tag=1.0-dev
    

## Tagging images

You can tag existing images in an Artifact Registry repository or you can tag them before you push them to a repository.

### Tagging images in a repository

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You can add a tag to an image in an Artifact Registry repository using the [Google Cloud console](https://console.cloud.google.com/) or the command line. In a repository, tags are unique to a version of an image. So if you have multiple versions of an image, each tag only applies to one of the versions. If you tag an image with a tag that's already in use, you will move the tag from the original version to the newly tagged version.

###  Console 

To tag an image in a repository:

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the image to view versions of the image.

  3. Select the image version to tag.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Type new tags into the field and then click **SAVE**.




###  gcloud 

To tag images in a repository, specify the image version using the image digest or tag, and then specify the tag to add. Run one of the following commands:
    
    
    gcloud artifacts docker tags add IMAGE-VERSION TAG
    

Where

  * `IMAGE-VERSION` is the [full name](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions) of the image version to tag, using either the image digest or an existing tag on the image version.
  * `TAG` is the [full name](https://docs.cloud.google.com/artifact-registry/docs/docker/names#versions) of the tag that you want to add.



For example, consider an image with the following characteristics:

  * Repository location: `us-west1`
  * Repository name: `my-repo`
  * Project ID: `my-project`
  * Image name: `my-image`
  * Existing tag: `iteration6-final`
  * Tag to add: `release-candidate`



To add the tag `release-candidate` to the version of the image with the tag `iteration6-final`, run the following command:
    
    
    gcloud artifacts docker tags add \
    us-west1-docker.pkg.dev/my-project/my-repo/my-image:iteration6-final \
    us-west1-docker.pkg.dev/my-project/my-repo/my-image:release-candidate
    

For details about the image name format, including domain-scoped projects, see [Repository and image names](https://docs.cloud.google.com/artifact-registry/docs/docker/names). 

### Tagging local images

To push any local image to Artifact Registry, you need to first tag it with the repository name and then push the image. For instructions, see [Pushing and pulling](https://docs.cloud.google.com/artifact-registry/docs/docker/pushing-and-pulling).

## Untagging images

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You can remove a tag from an image in Artifact Registry using the [Google Cloud console](https://console.cloud.google.com/) or the command line.

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the image to view versions of the image.

  3. Select the image version to untag.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Delete the tag and then click **SAVE**.




###  gcloud 

To delete a tag and remove it from the image, run the following command:
    
    
     gcloud artifacts docker tags delete LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE:TAG
    

Replace the following:

  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PROJECT` is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `REPOSITORY` is the name of the repository where the image is stored.
  * `IMAGE` is the name of the image in the repository.
  * `TAG` is the tag for the version you want to delete.



## Deleting images

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can delete an entire container image or delete a specific image version associated with a tag or digest. Removing unused images can help you to reduce storage costs.

  * Once you delete an image, you cannot undo the action.
  * Deleting images doesn't immediately delete the referenced layers. Unreferenced layers are deleted daily. 
  * For remote repositories, the cached copy of the image is removed. The image remains available from the upstream source. If the remote repository receives a new request for the same image, the repository will download and cache it again. 

You can use [cleanup policies](https://docs.cloud.google.com/artifact-registry/docs/repositories/cleanup-policy) to control when and how your artifacts are saved or deleted. 

To delete an images from Google Cloud console or the gcloud CLI:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the image name to see versions of that image.

  3. Select versions that you want to delete.

  4. Click **DELETE**.

  5. In the confirmation dialog, click **DELETE**.




###  gcloud 

To delete an image and all its tags, run the command:
    
    
    gcloud artifacts docker images delete LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE --delete-tags
    

To delete a specific image version, use one of the following commands.
    
    
    gcloud artifacts docker images delete LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE:TAG [--delete-tags]
    

or
    
    
    gcloud artifacts docker images delete LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE@IMAGE-DIGEST [--delete-tags]
    

Where

  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * REPOSITORY is the name of the repository where the image is stored.
  * IMAGE is the name of the image in the repository.
  * TAG is the tag for the version you want to delete. If multiple tags are associated with the same image version, you must include `--delete-tags` to delete the image version without removing the tags first.
  * IMAGE-DIGEST is the sha256 hash value for the version you want to delete. If a tag is associated with the image digest, you must include `--delete-tags` to delete the image version without removing the tag first.
  * `--delete-tags` removes all tags applied to the image version. This flag lets you force deletion of an image version when: 
    * You specified a tag, but there are other tags associated with the image version.
    * You specified an image digest that has at least one tag.



## What's next

  * [Download individual files](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files) stored within an image without using Docker commands. This can be useful for quickly inspecting manifest files. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
