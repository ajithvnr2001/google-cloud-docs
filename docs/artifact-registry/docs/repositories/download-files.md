---
url: https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files/
title: Download files \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:10.577470+00:00
---

# Download files  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Download files Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to download individual files from Artifact Registry [standard](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos) repositories and [remote](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo) repositories. The repository can be of any artifact [format](https://docs.cloud.google.com/artifact-registry/docs/supported-formats).

Downloading files can be useful when you want to get files into your local environment without format-specific tooling. Note that you must still authenticate to Artifact Registry before downloading files.

**Note:** Files can't be downloaded from virtual repositories.

## Downloadable files

You can download any individual data or metadata file found in your repository. For example, a Maven repository will store Java packages as artifacts. Any files within a Java package, such as jar files and pom.xml files, are individually available for download.

Using this feature is not recommended for artifacts that depend heavily on client tooling for download operations, such as Docker images.

## Before you begin

  * (Optional) [Set defaults for gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults).



### Required roles

To get the permissions that you need to download files stored in a repository, ask your administrator to grant you the [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) IAM role on the repository. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List files

You can list files in a repository to see what is available for download.

###  console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. In the repository list, select the repository.

  3. Click the name of the package.

  4. To view downloadable files for all package versions, click the **Files** tab.

  5. To view downloadable files for a specific version of your package, click the version name, and then click the **Files** tab. 




###  gcloud 

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



For Docker repositories, you can list files for a specific container image tag by adding the `--tag` flag to the command.

For more information, see [gcloud artifacts files list](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/list). 

## Download files

To download individual files from a repository, run the following command:

###  gcloud 

Before using any of the command data below, make the following replacements: 

  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository where the artifact is stored.
  * `DESTINATION`: the path to the destination folder in your local file system. The destination folder must already exist or the command will fail.
  * `FILE`: the full filename. You can find this value by running the [`gcloud artifacts files list`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/list) command and copying the value for `FILE`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts files download \
        --project=PROJECT \
        --location=LOCATION \
        --repository=REPOSITORY \
        --destination=DESTINATION \
        FILE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts files download `
        --project=PROJECT `
        --location=LOCATION `
        --repository=REPOSITORY `
        --destination=DESTINATION `
        FILE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud artifacts files download ^
        --project=PROJECT ^
        --location=LOCATION ^
        --repository=REPOSITORY ^
        --destination=DESTINATION ^
        FILE

You should see the download begin right away. 

###  API 

Before using any of the request data, make the following replacements: 

  * `PROJECT`: your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects). If your project ID contains a colon (`:`), see [Domain-scoped projects](https://docs.cloud.google.com/artifact-registry/docs/docker/names#domain).
  * `LOCATION`: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `REPOSITORY`: the name of the repository where the artifact is stored.
  * `DESTINATION`: the path to the destination folder in your local file system. The destination folder must already exist or the command will fail.
  * `FILE`: the url-encoded filename. You can find this value by running the [`gcloud artifacts files list`](https://docs.cloud.google.com/sdk/gcloud/reference/artifacts/files/list) command and copying the value for `FILE`. It must be converted to URL-encoded format for this command—for example, `path/to/file.jar` would need to be input as `path%2Fto%2Ffile.jar`.



HTTP method and URL: 
    
    
    GET https://artifactregistry.googleapis.com/download/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/files/FILE:download?alt=media

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         --output DESTINATION \  
         "https://artifactregistry.googleapis.com/download/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/files/FILE:download?alt=media"

#### PowerShell (Windows)

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -OutFile DESTINATION `  
        -Uri "https://artifactregistry.googleapis.com/download/v1/projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/files/FILE:download?alt=media"

You should see the download begin right away. 

## What's next

  * [View and list repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/list-repos)
  * [Label repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/label-repos)
  * [Tag repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/tag-repos)
  * [Delete repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/delete-repos)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
