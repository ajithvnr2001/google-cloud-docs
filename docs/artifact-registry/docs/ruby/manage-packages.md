---
url: https://docs.cloud.google.com/artifact-registry/docs/ruby/manage-packages/
title: Manage Ruby gems \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:24.622287+00:00
---

# Manage Ruby gems  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/ruby/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Ruby gems Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes adding, viewing, and deleting Ruby gems and gem versions.

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) and [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the Google Cloud CLI.

Google Cloud CLI version 354.0.0 or newer is required to run commands for Ruby repositories. You can check the version with the command:
         
         gcloud version
         

  2. If the target repository doesn't exist, then [create a Ruby package repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).

  3. Verify that Ruby is installed. For installation instructions, see the Google Cloud [tutorial for setting up Ruby](https://docs.cloud.google.com/ruby/docs/setup).

  4. (Optional) [Set defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).




### Required roles

To get the permissions that you need to manage gems, ask your administrator to grant you the following IAM roles on the repository: 

  * View gems or files in gems: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Download or install gems: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Add gems to a repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete gems: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add gems

Packages in Ruby are called _gems_ , where each gem contains a name, version and platform. A Ruby project must also contain a _gemfile_ , which is a configuration file that specifies required gem dependencies.

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

When you build a Ruby project, distribution files are saved in a `lib` subdirectory in your project. You can then use RubyGems to upload gems to a standard repository.

To add a gem to your Artifact Registry repository:
    
    
    gem push GEM_NAME --host https://LOCATION-ruby.pkg.dev/PROJECT/REPOSITORY
    

Where:

  * GEM_NAME is the name of the gem to push to your repository.
  * LOCATION is the location of your repository.
  * PROJECT is the project ID. If this flag is omitted, then the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
  * REPOSITORY is the name of your repository in Artifact Registry.



## View gems and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

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



For remote repositories, the returned list should include all direct and transitive dependencies.

## List files

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

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



### Examples

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
    

## Install gems

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

To install the latest stable release of a package:
    
    
    gem install GEM_NAME
    

For standard repositories, you download a package directly from the repository.

For a remote repository, you download a cached copy of the package and its dependencies. If a cached copy does not exist, the remote repository downloads the package from the upstream source and caches it before serving it to you. You can verify that the remote repository retrieved the packages from the upstream source by viewing the list of packages in the repository.

For a virtual repository, Artifact Registry searches upstream repositories for the requested package.

  * Upstream remote repositories will download and cache the requested package if a cached copy does not exist. Virtual repositories only serve requested packages, they do not store them.
  * If you request a version that is available in more than one upstream repository, Artifact Registry chooses an upstream repository to use based on the priority settings configured for the virtual repository.



For example, consider a virtual repository with the following priority settings for upstream repositories:

  * `main-repo`: Priority set to `100`
  * `secondary-repo1`: Priority set to `80`.
  * `secondary-repo2`: Priority set to `80`.
  * `test-repo`: Priority set to `20`.



`main-repo` has the highest priority value, so the virtual repository always searches it first.

Both `secondary-repo1` and `secondary-repo2` have priority set to `80`. If a requested package is not available in `main-repo`, Artifact Registry searches these repositories next. Since they both have the same priority value, Artifact Registry can choose to serve a package from either repository if the version is available in both of them.

`test-repo` has is lowest priority value and will serve a stored artifact if none of the other upstream repositories has it.

### Additional information

When you push gems to or pull gems from an Artifact Registry repository, if the requested gem or its dependencies aren't found in your specified repository, then your `gem` client uses any other source that is defined in the gemfile for your gem. If you want to only fetch and install directly from Artifact Registry, then run the following command to remove a non-Artifact Registry source from your gemfile:
    
    
    gem sources --remove SOURCE
    

To add rubygems.org back as a source:
    
    
    gem sources --add SOURCE
    

Where SOURCE is the address of the source, such as `https://rubygems.org`.

## Delete packages and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You can delete a package and all its versions, or delete a specific version.

  * Once you delete a package, you cannot undo the action.
  * For remote repositories, only the cached copy of the package is deleted. The upstream source is unaffected. If you delete a cached package, Artifact Registry will download and cache it again the next time the repository receives a request for the same package version.



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

## Limitations

  * Artifact Registry doesn't support adding repositories as sources by using the `gem sources -add` command. However, you can manually add sources to your `.gemrc` file, or pass the `--source` flag directly in your `gem` command.

  * Artifact Registry doesn't support pulling gems by using `gem fetch`.




## What's next

  * [Learn about managing container images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
