---
url: https://docs.cloud.google.com/artifact-registry/docs/conda/manage-packages/
title: Manage Conda packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:22.693594+00:00
---

# Manage Conda packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/conda/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Conda packages Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you create a Conda repository in Artifact Registry, you'll be ready to install Conda packages in your new repository. This page describes how to install, view, and delete your Conda packages.

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI.

Google Cloud CLI version 354.0.0 or newer is required to run commands for Conda repositories. You can check the version with the command:
         
         gcloud version
         

  2. To use the Conda CLI within your Google Cloud environment, install one of the following Conda package managers:

     * [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
     * [Mamba](https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html)
     * [Micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html)
     * [Miniforge](https://conda-forge.org/download/)
  3. If you don't have a Conda repository in Artifact Registry, then [create a Conda package repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).

  4. (Optional) [Set defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).




Artifact Registry supports [standard](https://docs.cloud.google.com/artifact-registry/docs/repositories) and [remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-overview) Conda repositories. You can use any of the following addresses for your remote repositories.

  * `https://repo.anaconda.com/pkgs/main`
  * `https://repo.anaconda.com/pkgs/r`
  * `https://repo.anaconda.com/pkgs/msys2`
  * `https://conda.anaconda.org/conda-forge`
  * `https://conda.anaconda.org/bioconda`



### Required roles

To get the permissions that you need to manage Conda packages, ask your administrator to grant you the following IAM roles on the repository: 

  * View packages or files in packages: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Download or install packages: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Add packages to a repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete packages: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Manage Conda packages

After you add a Conda package to your Artifact Registry repository, you can install the package to your Conda environment and view details about the package using Google Cloud.

### Add packages to an Artifact Registry repository

To add a Conda package to your Artifact Registry repository, run the following command:
    
    
    gcloud artifacts files upload \
        --source=PACKAGE_NAME \
        --repository=REPO_NAME\
        --project=PROJECT \
        --location=LOCATION
    

Where:

  * REPO_NAME is the ID of the repository.
  * PROJECT is the ID of the project containing the repository.
  * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.



To add multiple packages at one time:
    
    
    gcloud artifacts files upload \
        --source-directory=DIRECTORY \
        --repository=REPO_NAME\
        --project=PROJECT \
        --location=LOCATION
    

Where:

  * DIRECTORY is the address of a local folder containing your Conda packages.



### Install packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

To install the latest stable release of a package into your Conda environment, run the following command:

### Conda
    
    
    conda install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Miniforge
    
    
    conda install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Mamba
    
    
    mamba install -n ENVIRONMENT_NAME PACKAGE_NAME
    

### Micromamba
    
    
    micromamba install -n ENVIRONMENT_NAME PACKAGE_NAME
    

Where:

  * ENVIRONMENT_NAME is the name of your Conda environment. If you already have an environment activated and are installing the package in the environment directly, you can leave out `-n ENVIRONMENT_NAME`.
  * PACKAGE_NAME is the name of your Conda package.

To install a specific version of a package in your Conda environment, include the VERSION after the package name.




For standard repositories, you download a package directly from the repository.

For a remote repository, you download a cached copy of the package and its dependencies. If a cached copy does not exist, the remote repository downloads the package from the upstream source and caches it before serving it to you. You can verify that the remote repository retrieved the packages from the upstream source by viewing the list of packages in the repository.

### View packages and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

To view packages and package versions using the Google Cloud console or `gcloud`:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the appropriate repository.

The **Packages** page lists the packages in the repository.

  3. Click a package to view versions of the package.




###  gcloud 

To list packages in a repository, run the following command:
    
    
    gcloud artifacts packages list [--repository=REPOSITORY] [--location=LOCATION]
    

Replace the following:

  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.



To view versions of a package, run the following command:
    
    
    gcloud artifacts versions list --package=PACKAGE \
        [--repository=REPOSITORY] [--location=LOCATION]
    

Replace the following:

  * `PACKAGE` is the ID of the package or fully qualified identifier for the package.
  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, then you can omit this flag to use the default.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.



For remote repositories, the returned list shows only cached packages.

### List files

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

For remote repositories, the returned list shows only cached Conda packages and index files.

You can list files in a repository, files in all versions of a specified package, or files in a specific version of a package.

For all the following commands, you can set a maximum number of files to return by adding the `--limit` flag to the command.

To list all files in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
    gcloud artifacts files list
    

To list files in a specified project, repository, and location, run the command:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION
    

To list files for all versions of a specific package:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION \
        --package=PACKAGE
    

To list files for a specific package version:
    
    
    gcloud artifacts files list \
        --project=PROJECT \
        --repository=REPOSITORY \
        --location=LOCATION \
        --package=PACKAGE \
        --version=VERSION
    

Replace the following values:

  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `REPOSITORY`: the name of the repository where the image is stored.
  * `PACKAGE`: the name of the package.
  * `VERSION`: the version of the package.



#### Examples

Consider the following package information:

  * Project: `my-project`
  * Repository: `my-repo`
  * Repository location: `us-west1`
  * Package: `my-app`



The following command lists all files in the repository `my-repo` in the location `us-west1` within the [default project](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
    gcloud artifacts files list \
        --location=us-west1 \
        --repository=my-repo
    

The following command lists files in version `1.0` of the package. 
    
    
    gcloud artifacts files list \
        --project=my-project \
        --location=us-west1 \
        --repository=my-repo \
        --package=my-app \
        --version=1.0
    

### Delete packages and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can delete a package and all its versions, or delete a specific version. Deleted packages can't be restored.

Before you delete a package or package version, verify that any you have communicated or addressed any important dependencies on it.

To delete a package:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the appropriate repository.

The **Packages** page lists the packages in the repository.

  3. Select the package that you want to delete.

  4. Click **DELETE**.

  5. In the confirmation dialog box, click **DELETE**.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts packages delete PACKAGE \
        [--repository=REPOSITORY] [--location=LOCATION] [--async]
    

Replace the following:

  * `PACKAGE` is the name of the package in the repository.
  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, then you can omit this flag to use the default.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.



The `--async` flag causes the command to return immediately, without waiting for the operation in progress to complete.

To delete versions of a package:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, click the appropriate repository.

The **Packages** page lists the packages in the repository.

  3. Click a package to view versions of that package.

  4. Select versions that you want to delete.

  5. Click **DELETE**.

  6. In the confirmation dialog box, click **DELETE**.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts versions delete VERSION \
        --package=PACKAGE \
        [--repository=REPOSITORY] [--location=LOCATION] \
        [--async]
    

Replace the following:

  * `VERSION` is the name of the version to delete.
  * `PACKAGE` is the name of the package in the repository.
  * `REPOSITORY` is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, then you can omit this flag to use the default.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, then you can omit this flag to use the default.



The `--async` flag causes the command to return immediately, without waiting for the operation in progress to complete.

For remote repositories, Artifact Registry deletes the caching data for the selected packages, including package versions and files.

## What's next

  * [Learn about managing container images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
