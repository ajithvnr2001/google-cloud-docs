---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/manage-packages/
title: Manage Debian packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:35.853993+00:00
---

# Manage Debian packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Debian packages Stay organized with collections  Save and categorize content based on your preferences. 

This page describes adding, viewing, and deleting Debian packages in Apt repositories.

## Before you begin

  1. If the target Apt repository doesn't exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. [Configure VMs](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure) to access the repository.
  3. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  4. Ensure your package names in metadata meet the [Debian package name standards](https://www.debian.org/doc/debian-policy/ch-controlfields.html#package).



## Adding packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You must have both read and write [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository to add packages.

You can upload a package to a repository using the Google Cloud CLI, or you can import a package that is stored in Cloud Storage. If you build packages using Cloud Build, the build can store the packages in Cloud Storage for you to import.

Very long import or upload operations might exceed the expiry period for the token that gcloud CLI uses to call the API. If you have a very large number of packages to add, consider adding them in smaller batches so that each upload or import operation can complete in a shorter amount of time. See [OS packages troubleshooting](https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot#missing-artifacts) documentation for more information.

###  Direct upload 

Use the [`gcloud artifacts apt upload` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/apt/upload) to upload a package to an Apt repository:
    
    
    gcloud artifacts apt upload REPOSITORY \
        --location=LOCATION \
        --source=PACKAGES
    

Replace the following values:

  * `REPOSITORY` is the Artifact Registry repository name.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PACKAGES` is the path to the package.



For example, to upload the package `my-package.deb` to the Apt repository `my-repo` in the location `us-west1`, run:
    
    
    gcloud artifacts apt upload my-repo \
        --location=us-west1 \
        --source=my-package.deb
    

###  Cloud Storage 

  1. Upload the packages to Cloud Storage by doing the following: 
     * [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) packages directly to a Cloud Storage bucket
     * Build packages with [Cloud Build](https://docs.cloud.google.com/build/docs/building/store-build-artifacts#store-artifact-storage) and store the packages in a bucket
  2. Run the following command: 
         
         gcloud artifacts apt import REPOSITORY \
           --location=LOCATION \
           --gcs-source=PACKAGES
         

Replace the following values:

     * `REPOSITORY` is the Artifact Registry repository name.
     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
     * `PACKAGES` is a comma separated list of packages in Cloud Storage. To upload all packages from a directory, use a directory wildcard (`*`) or use a recursive directory wildcard (`**`) to upload all packages in all subdirectories.

For example, to upload a the package `package.deb` and all packages in the `directory` directory from the bucket `my-bucket` to the Apt repository `my-repo` in the location `us-west1`, run:
    
    gcloud artifacts apt import my-repo \
      --location=us-west1 \
      --gcs-source=gs://my-bucket/path/to/package.deb,gs://my-bucket/directory*
    




When the upload or import operation is complete, you can use the Google Cloud console or gcloud CLI to view packages in the repository and confirm that they were uploaded successfully.

If you have a large repository with a lot of packages, it might take several minutes to regenerate the package index so that the new packages are visible to the Apt client.

## Viewing packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote (preview) 

To view packages, you must have the permissions in the Artifact Registry Reader [role](https://docs.cloud.google.com/artifact-registry/docs/access-control). Artifact Registry does not list files inside packages.

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



## Installing packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote (preview) 

Before you install packages, verify that you have [configured](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/configure) the package manager and repository correctly.

To install a package in the repository:

  1. Update the list of available packages:
         
         sudo apt update
         

  2. Install the package, specifying the name of the repository configured in Apt.
         
         sudo apt install PACKAGE/REPOSITORY
         

Replace the following values:

     * `PACKAGE` is the package name.
     * `REPOSITORY` is the name of the Artifact Registry repository. For remote repositories, use the name of the standard upstream repository.

For example, to install the package `my-package` from the repository `my-repo`, run the command:
    
    sudo apt install my-package -t my-repo
    


**Note:** After adding or deleting packages, it can take several minutes to regenerate the package index, particularly if the repository is large. If you are unable to install a package that was recently added to the repository, wait a few minutes and then try again. For additional information, see the [OS packages troubleshooting](https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot) documentation.

## Deleting packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

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

For large repositories, it can take a few minutes to regenerate the Apt package index to reflect deletions.

## What's next

  * [Learn about managing RPM packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/manage-packages)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
