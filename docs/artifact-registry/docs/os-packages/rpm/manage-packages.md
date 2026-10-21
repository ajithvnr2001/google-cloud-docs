---
url: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/manage-packages/
title: Manage RPM packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:25.362137+00:00
---

# Manage RPM packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage RPM packages Stay organized with collections  Save and categorize content based on your preferences. 

This page describes adding, viewing, and deleting RPM packages in Yum repositories. Artifact Registry Yum repositories support Yum and DNF.

## Before you begin

  1. If the target Yum repository doesn't exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. [Configure VMs](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure) to access the repository.
  3. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  4. Ensure your package names in metadata meet the [Fedora package naming guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Naming/#_general_naminge) and the [Fedora package versioning guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/).



## Adding packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You must have both read and write [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository to add packages.

You can upload a package to a repository using the Google Cloud CLI, or you can import a package that is stored in Cloud Storage.

If you build packages using Cloud Build, the build can store the packages in Cloud Storage for you to import. 

Very long import or upload operations might exceed the expiry period for the token that gcloud CLI uses to call the API. If you have a very large number of packages to add, consider adding them in smaller batches so that each upload or import operation can complete in a shorter amount of time. See [OS packages troubleshooting](https://docs.cloud.google.com/artifact-registry/docs/os-packages/troubleshoot#missing-artifacts) documentation for more information.

###  Direct upload 

Use the [`gcloud artifacts yum upload` command](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/yum/upload) to upload a package to an Yum repository:
    
    
    gcloud artifacts yum upload REPOSITORY \
        --location=LOCATION \
        --source=PACKAGES
    

Replace the following values:

  * `REPOSITORY` is the Artifact Registry repository name.
  * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
  * `PACKAGES` is the path to the package.



For example, to upload the package `my-package.rpm` to the Yum repository `my-repo` in the location `us-west1`, run:
    
    
    gcloud artifacts yum upload my-repo \
        --location=us-west1 \
        --source=my-package.rpm
    

###  Cloud Storage 

  1. Upload the packages to Cloud Storage in one of the following ways: 
     * [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) packages directly to a Cloud Storage bucket
     * Build packages with [Cloud Build](https://docs.cloud.google.com/build/docs/building/store-build-artifacts#store-artifact-storage) and store it in a bucket
  2. Run the following command: 
         
         gcloud artifacts yum import REPOSITORY \
           --location=LOCATION \
           --gcs-source=PACKAGES
         

Replace the following values:

     * `REPOSITORY` is the Artifact Registry repository name.
     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 
     * `PACKAGES` is a comma separated list of packages in Cloud Storage. To upload all packages from a directory, use a directory wildcard (`*`) or use a recursive directory wildcard (`**`) to upload all packages in all subdirectories.

For example, the following command uploads the package `package.rpm` and all packages in the `directory` directory from the bucket `my-bucket` to the Yum repository `my-repo` in the location `us-west1`:
    
    gcloud artifacts yum import my-repo \
      --location=us-west1 \
      --gcs-source=gs://my-bucket/path/to/package.rpm,gs://my-bucket/directory*
    




When the upload or import operation is complete, you can use the Google Cloud console or gcloud CLI to view packages in the repository and confirm that they were uploaded successfully.

If you have a large repository with a lot of packages, it might take several minutes to regenerate the package index so that the new packages are visible to the Yum client.

## Viewing packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote (preview)

To view packages, you must have the permissions in the [Artifact Registry Reader role](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader). Artifact Registry does not list files inside packages.

**Note:** Artifact Registry formats RPM package versions with a leading epoch value of `0:`. For example, if an RPM package has version `1.2.3`, that version appears in Artifact Registry as `0:1.2.3`.

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

Before you install packages, verify that you have [configured](https://docs.cloud.google.com/artifact-registry/docs/os-packages/rpm/configure) the VM to install packages from your Artifact Registry repository.

To install a package, run the following command:
    
    
    sudo yum --enablerepo=REPOSITORY install PACKAGE
    

Replace the following values:

  * `PACKAGE` is the package name
  * `REPOSITORY` is the name of the repository configured in the `.repo` file.



For example, to install the package `my-package` from the repository `my-repo`, run the command:
    
    
    sudo yum --enablerepo=my-repo install my-package
    

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

For large repositories, it can take a few minutes to regenerate the Yum package index to reflect deletions.

## What's next

  * [Learn about managing Debian packages](https://docs.cloud.google.com/artifact-registry/docs/os-packages/debian/manage-packages)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
