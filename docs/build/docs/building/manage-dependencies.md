---
url: https://docs.cloud.google.com/build/docs/building/manage-dependencies/
title: Manage build dependencies \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:56.084918+00:00
---

# Manage build dependencies  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/building/manage-dependencies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Manage build dependencies Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how you can specify build dependencies. Cloud Build lets you manage source-code dependencies separately from the build process.

In your build configuration file, you can list one or more repositories to clone for your build, and the order in which to fetch them. Specifying dependencies in this way separates dependency fetching from the build process itself.

If you don't include any dependencies in your build configuration file, Cloud Build clones the source code repository that contains your build configuration file (for triggered builds) or the repository that contains your source code (for builds that you invoke from the command line). If you include dependencies in your build configuration file, Cloud Build clones only repositories that are specified in the `dependencies` field.

Dependencies are cloned in the order that you specify them. Also, dependency fetching occurs before any user-specified logic is executed. Thus, dependency fetching is trusted.

Dependencies are shown in the **Build dependencies** tab of the **Build details** page.

## Before you begin

The instructions on this page assume that you have at least one of the following two repository types:

  * A Git repository that is either a public repository or [linked](https://docs.cloud.google.com/developer-connect/docs/connect-github-repo) to Cloud Build using Developer Connect.

  * A [generic repository](https://docs.cloud.google.com/artifact-registry/docs/generic/store-generic).




To ensure that has the necessary permissions to add a Developer Connect repository as a dependency, ask your administrator to grant the Developer Connect Read Token Accessor (`developerconnect.readTokenAccessor`) IAM role to on your service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

Your administrator might also be able to give the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Specify dependencies

You specify dependencies by adding a `dependencies` field to your build configuration file. `dependencies` is a top-level property in the build config, but you can put it anywhere in the file.

### Specify GitHub dependencies

To specify a dependency on a GitHub repository, add the following `dependencies` configuration to your build config file:

###  YAML 
    
    
     dependencies:
     - gitSource:
         repository:
           url: 'URL'
           developerConnect: 'DC_RESOURCE_PATH'
         revision: 'REVISION'
         recurseSubmodules: 'true|false'
         fetchTags: 'true|false'
         depth: 'DEPTH'
         destPath: 'DEST_PATH'
    

###  JSON 
    
    
     {
         "dependencies": {
             "gitSource": {
                 "repository": {
                     "url": "URL"
                     "developerConnect": "DC_RESOURCE_PATH"
                 },
                 "revision": "REVISION",
                 "recurseSubmodules": true|false,
                 "fetchTags": true|false,
                 "depth": "DEPTH",
                 "destPath": "DEST_PATH",
             },
         },
     }
    

Replace the following values:

  * URL: The HTTPS URL of the repository to fetch. Required unless your repository is connected to Cloud Build using Developer Connect.

  * DC_RESOURCE_PATH: The Google Cloud resource path to a Developer Connect repository. For example, `projects/my-project/locations/us-central1/connections/my-connection/gitRepositoryLinks/my-repo`. Required if your repository is connected to Cloud Build using Developer Connect.

If your repository is connected using Developer Connect, you need the following:

    * The Cloud Build service account must have the [`Developer Connect Read Token Accessor`](https://docs.cloud.google.com/developer-connect/docs/access-control#roles) role.
  * REVISION: Required. The version, commit hash, tag, or branch name to fetch from the repository.

  * `recurseSubmodules`: 'true|false': Whether to fetch submodules.

  * `fetchTags`: 'true|false': Optional. True if remote tags should be fetched too (default `false`). Note: when `depth` is `1` (default), `git fetch` only retrieves tags pointing to commits within the shallow boundary. Set `depth` to `-1` to fetch all historical tags.

  * DEPTH: Optional, how deep into the repository history to fetch. If not specified, the latest commit is fetched.

    * `1`: the latest commit
    * `2`: the last two commits
    * `3`: the last three commits
    * `-1`: all commits
  * DEST_PATH: Required. The path to the directory into which the repository is cloned. For example, `my/repo`.

When you set the `dest_path` the repository is fetched in `/workspace/<dest_path>`. The `dest_path` value must be a path relative to the working directory of the build.




### Specify a generic artifact as a dependency

To specify a [generic artifact](https://docs.cloud.google.com/build/docs/build-config-file-schema#generic-artifacts) as a dependency, add the following `dependencies` configuration to your build config file:

###  YAML 
    
    
    dependencies:
    - genericArtifact:
        resource: RESOURCE
        destPath: PATH
    

###  JSON 
    
    
    {
      "dependencies": [
        {
          "genericArtifact": {
            "resource": "RESOURCE",
            "destPath": "PATH"
          }
        }
      ]
    }
    

Where:

  * RESOURCE is the full address of the generic artifact within your Artifact Registry generic repository, formatted as follows:

`projects/PROJECT/locations/LOCATION/repositories/REPOSITORY/packages/PACKAGE/versions/VERSION`

We strongly recommend including your artifact's fingerprint in the resource address so that Cloud Build can verify that the artifact reference is immutable. A package version with an appended fingerprint is formatted as follows:

`VERSION@dirsum_sha256=HASH_VALUE`

To find the fingerprint of an artifact in an Artifact Registry repository, see [Retrieve the fingerprint of a package version in your repository](https://docs.cloud.google.com/artifact-registry/docs/fingerprint#get-fingerprint).

  * PATH is the address to the folder to which Cloud Build downloads the package from your repository. If the folder doesn't exist yet, Cloud Build creates it automatically.




## What's next

  * Learn how to [connect a repository to Cloud Build using Cloud Build repositories](https://docs.cloud.google.com/build/docs/repositories).

  * Learn how to [connect a repository to Cloud Build using Developer Connect](https://docs.cloud.google.com/developer-connect/docs/overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
