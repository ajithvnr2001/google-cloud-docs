---
url: https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules/
title: Manage Go modules \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:18:38.874076+00:00
---

# Manage Go modules  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Go modules Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store, version, and share private Go modules across your repositories. You can upload new releases, inspect package details, import dependencies in your code, and delete unused versions.

## Before you begin

  1. If the target repository does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos). Choose Go as the repository format.
  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.
  3. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  4. [Install Go](https://go.dev/doc/install) 1.15 or later.
  5. Install the package-go-module gcloud CLI add-on:
         
         gcloud components install package-go-module

  6. Configure Go to [authenticate](https://docs.cloud.google.com/artifact-registry/docs/go/authentication) with Artifact Registry.




### Required Roles

To get the permissions that you need to manage modules, ask your administrator to grant you the following IAM roles on the repository: 

  * View modules: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Download or install modules: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Add modules to a repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete modules: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Upload a module

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

To package and upload a module to your repository run the following command:
    
    
      gcloud artifacts go upload --project=PROJECT \
          --repository=REPOSITORY \
          --location=LOCATION \
          --module-path=MODULE_PATH \
          --version=VERSION \
          --source=SOURCE_LOCATION
    

Replace the following:

  * PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * REPOSITORY with the name of the repository where the package is stored.
  * LOCATION with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * MODULE_PATH with the module path. For example: `example.com/foo` See the [Go Modules Reference](https://go.dev/ref/mod#module-path) for more information.
  * VERSION with the [semantic version](https://pkg.go.dev/golang.org/x/mod/semver) of the module in the form `vX.Y.Z` where `X` is the major version, `Y` is the minor version, and `Z` is the patch version.
  * SOURCE_LOCATION with the path to the root directory of your Go module. If you omit the `--source` flag, the default is the current directory.



The module is uploaded to Artifact Registry.

For more information on creating Go modules, see this [tutorial](https://go.dev/doc/tutorial/create-module).

### Upload a new module version

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

To upload a new version of your module to the default project, repository and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults), run the following command with the new version number:
    
    
      gcloud artifacts go upload \
          --module-path=MODULE_PATH \
          --version=VERSION \
          --source=SOURCE_LOCATION
    

Replace VERSION with the version of your updated module. For example, to upload version `0.1.1` of a module with the path `example.com/foo`, run the following command:
    
    
      gcloud artifacts go upload \
          --module-path=example.com/foo \
          --version=v0.1.1 \
          --source=SOURCE_LOCATION
    

To mark a module as a pre-release version, add a dash after the VERSION and append your module's pre-release identifiers:
    
    
      gcloud artifacts go upload \
          --module-path=MODULE_PATH \
          --version=VERSION-PRE_RELEASE_IDENTIFIERS \
          --source=SOURCE_LOCATION
    

Replace PRE_RELEASE_IDENTIFIERS with dot separated ASCII alphanumeric characters and hyphens. For example, to upload a pre-release of a module with the path `example.com/foo` module identified by `alpha.x.12m.5`, run the following command:
    
    
      gcloud artifacts go upload \
          --module-path=example.com/foo \
          --version=v1.0.0-alpha.x.12m.5 \
          --source=SOURCE_LOCATION
    

**Note:** Pre-release identifiers must be dot separated ASCII alphanumeric characters and hyphens. Metadata is not supported. For more information on versioning see [Semantic versioning 2.0.0](https://semver.org/) and this [blog post](https://go.dev/blog/v2-go-modules) for Go specific details.

### Upload a new major version

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

Major versions are not backwards compatible with previous versions. To prevent users from importing a breaking change, major versions after `v1` must have different module paths than previous versions. Starting with `v2`, the major version is added to the end of the module path.

For example, the module path for `v2.0.0` of `example.com/foo` would be `example.com/foo/v2`.

The recommended best practice is to develop major versions after `v1` in separate directories named after their major version suffix.

To upload a new major version `2.0.0` of a module with the path `example.com/foo` to the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
      gcloud artifacts go upload --module-path=example.com/foo/v2 --version=v2.0.0
    

## List modules

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

Run the following command to inspect an uploaded Go module in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
      gcloud artifacts packages list
    

The output will resemble the following:
    
    
      Listing items under project my-project, location us-west1, repository my-repo.
    
      PACKAGE                   CREATE_TIME          UPDATE_TIME
      example.com/foo           2022-06-03T20:43:39  2022-06-20T20:37:40
    

## View module version details

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

Run the following command to view the versions of a module in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
      gcloud artifacts versions list --package=MODULE_PATH
    

The output will resemble the following:
    
    
      Listing items under project my-project, location us-west1, repository my-repo, package example.com/foo.
    
      VERSION  DESCRIPTION  CREATE_TIME          UPDATE_TIME
      v0.1.0                2022-06-03T20:43:39  2022-06-03T20:43:39
      v0.1.1                2022-06-20T20:37:40  2022-06-20T20:37:40
    

## Use a module as a dependency

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

To import modules stored in Artifact Registry, you need to instruct Go to look for dependencies from Artifact Registry and bypass the checksum database. Follow the instructions to set up authentication and the Go environment in [Set up authentication for Go](https://docs.cloud.google.com/artifact-registry/docs/go/authentication).

  1. If you are using short-lived credentials for [authenticating to Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/go/authentication), then you must refresh your OAuth token by running the following command:
         
         GOPROXY=proxy.golang.org \
           go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@latest refresh
         

  2. If your module doesn't have a `go.mod` file yet, change directories into your module's folder and run `go mod init` to create a `go.mod` file for your package.
         
         go mod init MODULE_PATH
         

Replace MODULE_PATH with the module path for the module stored in Artifact Registry. See the [Go Modules Reference](https://go.dev/ref/mod#module-path) for more information.

  3. To require the version of your module stored in Artifact Registry, edit your `go.mod` file to resemble the following:
         
         module example.com/bar
         
         go 1.19
         
         require example.com/foo v0.1.0
         

Replace the following:

     * `example.com/foo` is the module path of the required module
     * `v0.1.0` is the version stored in Artifact Registry
  4. Include the module path as normal in the `import` section of your `main.go` file.

For example, to import a module with the path `example.com/foo` stored in Artifact Registry, your import section might resemble the following:
         
         
           package main
         
           import (
             foo "example.com/foo"
           )
         
           func main() {
         
             ...
         
           }
         
           
         

  5. Run `go mod tidy` to download dependencies:
         
         go mod tidy
         

  6. Run your module as normal:
         
         go run .
         

The module stored in Artifact Registry is downloaded and used as a dependency.




## Delete packaged Go modules

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can delete a package and all its versions, or delete a specific version.

  * Once you delete a package, you cannot undo the action.



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

## What's next

  * Try the [Go Quickstart](https://docs.cloud.google.com/artifact-registry/docs/go/store-go). 
  * [Download individual files](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files) associated with a module or version without using Go commands. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
