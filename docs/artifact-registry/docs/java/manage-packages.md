---
url: https://docs.cloud.google.com/artifact-registry/docs/java/manage-packages/
title: Manage Java packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:01.696757+00:00
---

# Manage Java packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/java/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Java packages Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you store, version, and manage Java packages in Maven-format repositories using Maven or Gradle. You can publish build artifacts, inspect stored versions and files, declare packages as project dependencies, and delete unused versions.

If you want to use [sbt](https://www.scala-sbt.org/1.x/docs/Getting-Started.html) as a build tool for Scala and Java instead of Maven or Gradle, you can use a [community-created sbt plugin](https://index.scala-lang.org/abdolence/sbt-gcs-resolver/sbt-gcs-plugin/). This document doesn't cover configuring or using Scala clients.

## Before you begin

  1. If the target repository does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.
  3. Verify that you have configured [authentication](https://docs.cloud.google.com/artifact-registry/docs/java/authentication). If you are using an access token, make sure that you refresh the token before connecting to the repository.
  4. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).



### Required roles

To get the permissions that you need to manage packages, ask your administrator to grant you the following IAM roles on the repository: 

  * View packages or files in packages: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Download or install packages: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Add packages to a repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete packages: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Adding packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** Standard

To add packages to the repository:

### Maven

Use `mvn deploy` and `mvn release` to add packages to the repository.

To successfully deploy a Maven project that references a parent, the project must include the Artifact Registry Wagon provider in a core extensions file as described in the [authentication](https://docs.cloud.google.com/artifact-registry/docs/java/authentication) instructions.

Use `mvn deploy:deploy-file` to upload artifacts that were built outside of Maven.

For example, this example command deploys `example/external.jar` and its project file `example/pom.xml` to the repository `us-central1-maven.pkg.dev/my-project/my-repo`
    
    
    mvn deploy:deploy-file \
    -Durl=artifactregistry://us-central1-maven.pkg.dev/my-project/my-repo \
    -DpomFile=example/pom.xml -Dfile=example/external.jar
    

**Note:** The `mvn archetype` command is not supported if used exclusively from the Artifact Registry repository.

To configure integration with Cloud Build, see [Integrating with Cloud Build](https://docs.cloud.google.com/artifact-registry/docs/configure-cloud-build).

### Gradle

To successfully publish to the repository, your `build.gradle` file must include a [publications](https://docs.gradle.org/current/userguide/publishing_maven.html#publishing_maven:publications) section that defines files to upload.

Use the `gradle publish` command to upload a package to the repository.

## Viewing packages and versions

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



For remote repositories, the returned list should include all direct and transitive dependencies.

## Listing files

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

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
    

## Downloading packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

To download an artifact as a part of your build, you declare the artifact as a dependency.

### Maven

  1. Declare the packages you want to download in the project `pom.xml` file. The following example declares version 1.0 of the package `artifact` as a dependency.
         
         <dependencies>
             <dependency>
                 <groupId>group</groupId>
                 <artifactId>artifact</artifactId>
                 <version>1.0</version>
             </dependency>
         </dependencies>
         

To learn more about Maven dependencies, see the Maven [introduction to dependencies](https://maven.apache.org/guides/introduction/introduction-to-dependency-mechanism.html) and [dependency reference](https://maven.apache.org/pom.html#Dependencies).

  2. Build the Java project.
         
         mvn compile
         




### Gradle

  1. Declare the packages you want to download in the project `build.gradle` file. The following example declares version 1.0 of the package `artifact` as an external compile dependency.

To learn more about Gradle dependencies, see the [Gradle documentation](https://docs.gradle.org/current/userguide/declaring_dependencies.html).
         
         dependencies {
             compile group: 'group', name: 'artifact', version: '1.0'
         }
         

  2. Build the Java project.
         
         gradle build
         




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

## Deleting packages and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

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

## What's next

  * [Learn about managing Node.js packages](https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages)
  * [Learn about managing Python packages](https://docs.cloud.google.com/artifact-registry/docs/python/manage-packages)
  * [Learn about managing container images](https://docs.cloud.google.com/artifact-registry/docs/docker/manage-images)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
