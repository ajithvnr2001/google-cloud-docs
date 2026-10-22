---
url: https://docs.cloud.google.com/artifact-registry/docs/helm/manage-charts/
title: Manage Helm charts \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:33.608661+00:00
---

# Manage Helm charts  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/helm/manage-charts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Helm charts Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage Helm 3 charts saved as [OCI container images](https://helm.sh/docs/topics/registries/), including pushing (uploading), pulling (downloading), listing, tagging, and deleting charts.

## Before you begin

  1. If the target repository doesn't exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos). Choose Docker as the repository format.
  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.
  3. (Optional) [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  4. [Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/). In previous versions of Helm, support for charts in OCI format is an experimental feature.

Run `helm version` to verify your version.

  5. Configure Helm to [authenticate](https://docs.cloud.google.com/artifact-registry/docs/helm/authentication) with Artifact Registry.




## Creating or obtaining a chart

This documentation focuses on managing your chart images and assumes that you have existing charts or are familiar with creating charts. To learn more about creating charts or obtaining publicly available charts in Artifact Hub, see the following information in the Helm documentation.

  * [Using Helm](https://helm.sh/docs/intro/using_helm/) describes obtaining charts from the public Artifact Hub and customizing a chart before installing it.
  * [Charts](https://helm.sh/docs/topics/charts/) describes charts and creating charts.
  * [Chart Best Practices Guide](https://helm.sh/docs/chart_best_practices/) describes conventions and best practices.



## Packaging a chart

Before you can push a chart to Artifact Registry, you must [package](https://helm.sh/docs/helm/helm_package/) it as a chart archive.

  1. Change to the directory that contains your chart.

  2. Package the chart.
         
         helm package CHART-PATH
         

Replace CHART-PATH with the path to the directory that contains your `Chart.yaml` file.




Helm uses the chart name and version for the archive filename. For example, if you have a chart with the name `my-chart` and version number `0.1.0`, the package name is `my-chart-0.1.0.tgz`.

You can now push the chart to Artifact Registry.

## Pushing a chart

After you have packaged your chart, you can push it to Artifact Registry.

To push the chart, run the following command:
    
    
    helm push my-chart-0.1.0.tgz oci://LOCATION-docker.pkg.dev/PROJECT/REPOSITORY
    

Replace the following values:

  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * REPOSITORY is the name of the repository.



Helm uses information from `Chart.yaml` for the OCI container image name and tag. Consider the following example command:
    
    
    helm push my-chart-0.1.0.tgz oci://us-west1-docker.pkg.dev/my-project/my-repo
    

Helm uploads the chart archive as the image `my-chart` with the tag `0.1.0`.

To verify that the push operation was successful, list the images in the repository.
    
    
    gcloud artifacts docker images list LOCATION-docker.pkg.dev/PROJECT/REPOSITORY
    

## Pulling charts

To pull a chart:

  1. Run the following command to pull the chart archive:
         
         helm pull oci://LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE \
             --version VERSION
         

If you want to pull the chart archive and extract its contents, add the `--untar` flag.
         
         helm pull oci://LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE \
             --version VERSION \
             --untar
         

Replace the following values:



  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain). 
  * REPOSITORY is the name of the repository where the image is stored.
  * IMAGE is the name of the image in the repository.
  * VERSION is semantic version of the chart. This flag is required. Helm does not support pulling a chart using a tag.



## Installing a chart

Install a chart stored in Artifact Registry with the [helm install](https://helm.sh/docs/helm/helm_install/) command.
    
    
    helm install RELEASE \
        oci://LOCATION-docker.pkg.dev/PROJECT/REPOSITORY/IMAGE \
        --version VERSION
    

The following example installs a release named `release1` using version `0.1.0` of the chart `us-west1-docker.pkg.dev/nyap-test/helm-repo/my-chart`:
    
    
    helm install release1 oci://us-west1-docker.pkg.dev/nyap-test/helm-repo/my-chart --version 0.1.0
    

## Listing charts

You can list charts using the [Google Cloud console](https://console.cloud.google.com/) or the command line. If you store container images and charts in the same Docker repository, then both artifact types appear in the list.

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



## Deleting images

In an Artifact Registry repository, you can delete an entire container image or delete a specific image version associated with a tag or digest. Once you have deleted an image, you cannot undo the action.

To delete an image stored in Artifact Registry:

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

  * [Learn about managing Docker images](https://docs.cloud.google.com/artifact-registry/docs/docker). 
  * [Download individual files](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files) from your repository without using Helm commands. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
