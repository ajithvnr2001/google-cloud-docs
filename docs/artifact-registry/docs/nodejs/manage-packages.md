---
url: https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages/
title: Manage Node.js packages \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:23.542165+00:00
---

# Manage Node.js packages  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Manage Node.js packages Stay organized with collections  Save and categorize content based on your preferences. 

Artifact Registry lets you publish, organize, and install Node.js packages in npm-format repositories using `npm` or `yarn`. You can view stored packages and files, manage version tags, install dependencies in your projects, and delete or deprecate unused versions.

## Before you begin

  1. If the target repository does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. Verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the repository.
  3. [Configure authentication for npm](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication).
  4. (Optional) [Configure defaults for gcloud commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  5. If you are using the npm [credential helper](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#auth-helper) to for authentication, obtain an access token before connecting to a repository with npm.



### Required roles

To get the permissions that you need to manage packages, ask your administrator to grant you the following IAM roles on the repository: 

  * View packages, files in packages, and tags: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Download or install packages: [Artifact Registry Reader ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader) (`roles/artifactregistry.reader`) 
  * Add packages to a repository: [Artifact Registry Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer) (`roles/artifactregistry.writer`) 
  * Delete packages: [Artifact Registry Repository Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.repoAdmin) (`roles/artifactregistry.repoAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Obtaining an access token

Access tokens are valid for 60 minutes. Generate an access token shortly before running commands that interact with repositories.

To obtain a token, use one of these options:

  * Use the `npx` command to refresh the access token.

    1. Ensure that credentials for connecting to the public npm registry are in your user npm configuration file, `~/.npmrc`.

    2. Run the following command in your Node.js project directory.
           
           npx google-artifactregistry-auth
           

If your Artifact Registry repository is set as your global registry and your packages are not scoped, use the following command instead so that the command can download the credential helper from the public npm registry instead of your Artifact Registry repository.
           
           npm_config_registry=https://registry.npmjs.org npx google-artifactregistry-auth
           

  * Add a script to the `package.json` file in your project.
        
        "scripts": {
         "artifactregistry-login": "npx google-artifactregistry-auth"
        }
        

Run the script in your Node.js project directory.
        
        npm run artifactregistry-login
        




Artifact Registry reads Artifact Registry repository settings in your project `.npmrc` file and uses them to add token credentials to your user `.npmrc` file. Storing the token in your user `.npmrc` file isolates your credentials from your source code and your source control system.

## Adding packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You can only publish a specific version of a package once. This is an [npm restriction](https://blog.npmjs.org/post/77758351673/npm-publish-f) to ensure that the contents of a published package version are always the same. As a result, you cannot:

  * Overwrite a package version by publishing it again to the repository
  * Remove a package or its version from the repository, and then publish a package with the same name and version number



If you don't specify a tag when you publish a package, npm adds the `latest` tag. To simplify installation of your packages at a specific development stage, consider publishing your packages with a tag, such as `beta` or `dev`.

Artifact Registry enforces alphanumeric lowercase package names for npm packages.

To add a package:

  1. Ensure that the package name in `package.json` includes the [scope](https://docs.cloud.google.com/artifact-registry/docs/nodejs#scopes) configured for your repository. The following example shows a package with the scope `dev-repo`.
         
         "name": "@dev-repo/my-package"
         

  2. If you are using the [credential helper](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#auth-helper) to authenticate with an access token, obtain a new token.

  3. Add packages to the repository. You can use an `npm` or `yarn` command.

To tag the package, include the `--tag` flag and replace TAG with the tag you want to use. If you do not include the `--tag` flag, npm automatically sets the tag to `latest`.
         
         npm publish --tag=TAG
         
         
         yarn publish --tag TAG
         




## Viewing packages and versions

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

To get package information with `npm` or `yarn`:

  1. If you are using the [credential helper](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#auth-helper) to authenticate with an access token, obtain a new token.

  2. Run the appropriate command:
         
         npm view
         
         
         yarn info
         




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



Viewing packages and versions from Google Cloud console or gcloud CLI in only available for standard and remote repositories.

For remote repositories, the returned list should include all direct and transitive dependencies that are cached in the repository.

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
  * `PACKAGE`: the name of the package.
  * `VERSION`: the version of the package.
  * `TAG`: the tag associated with the package.



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
    

The following command lists files in the version of the package with the tag `1.0-dev`
    
    
    gcloud artifacts files list \
        --project=my-project \
        --location=us-west1 \
        --repository=my-repo \
        --package=my-app \
        --tag=1.0-dev
    

## Tagging packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard

You can view, add, update, and delete tags. Tags can help you manage semantic versions of your packages and streamline installation of packages at a specific stage of development.

For example, you can tag the current release candidate build with `rc`. Your team can then install the correct version based on the tag instead of a version specifier, and unpublishing unused pre-release versions won't break your dependencies on the release candidate package.

### Viewing tags

To view tags for a package:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the package to view versions and the associated tags.

  3. Select the package version to tag.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Type new tags into the field and then click **SAVE**.




###  gcloud 

Run the command:
    
    
    gcloud artifacts tags list --package=PACKAGE \
        [--repository=REPOSITORY] [--location=LOCATION]
    

Where

  * PACKAGE is the name of the package in the repository.
  * REPOSITORY is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.
  * LOCATION is a regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, you can omit this flag to use the default.



For example, to view tags for the package `my-package` in the repository `my-repo` in the default location, run the command:
    
    
    gcloud artifacts tags list --package=my-pkg --repository=my-repo
    

### Creating tags

You can create a tag for a specific version of a package.

To tag an existing image in a repository:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the package to view versions of the package.

  3. Select the package version to tag.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Type new tags into the field and then click **SAVE**.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts tags create TAG --package=PACKAGE \
        version=VERSION [--location=LOCATION] [--repository=REPOSITORY]
    

Where

  * TAG is the tag you want to apply to the package.
  * PACKAGE is the name of the package in the repository.
  * VERSION is version of the package that you want to tag.
  * LOCATION is a regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, you can omit this flag to use the default.
  * REPOSITORY is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.



For example, to create the tag `release-candidate` for version `1.0.0` of package `my-package` in the repository `my-repo` in the default location, run the command:
    
    
    gcloud artifacts tags create release-candidate --version=1.0.0 \
        --package=my-pkg --repository=my-repo
    

### Updating tags

You can change a tag associated with a package version.

To change an existing tag:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the package to view versions of the package.

  3. Select the package version with the tag to change.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Edit the tag and then click **SAVE**.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts tags update TAG --package=PACKAGE \
        version=VERSION [--location=LOCATION] [--repository=REPOSITORY]
    

Where

  * TAG is the tag you want to apply to the package.
  * PACKAGE is the name of the package in the repository.
  * VERSION is version of the package that you want to tag.
  * LOCATION is a regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, you can omit this flag to use the default.
  * REPOSITORY is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.



For example, to change the tag for version `1.0.0` of package `my-package` to `production` in the repository `my-repo` in the default location, run the command:
    
    
    gcloud artifacts tags update production --version=1.0.0 \
        --package=my-pkg --repository=my-repo
    

### Untagging package versions

You can remove an existing tag from a package version.

To remove a tag:

###  Console 

  1. Open the **Repositories** page in the Google Cloud console.

[Open the Repositories page](https://console.cloud.google.com/artifacts)

  2. Click the image to view versions of the image.

  3. Select the image version to untag.

  4. In the row of the selected version, click **More actions** (![More actions](https://docs.cloud.google.com/static/artifact-registry/docs/images/more-actions.png)), and then click **Edit tags**.

  5. Delete the tag and then click **SAVE**.




###  gcloud 

Run the following command:
    
    
    gcloud artifacts tags delete TAG --package=PACKAGE \
        [--location=<LOCATION] [--repository=REPOSITORY]
    

Where

  * TAG is the tag you want to apply to the package.
  * PACKAGE is the name of the package in the repository.
  * LOCATION is a regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations). Use this flag to view repositories in a specific location. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) location, you can omit this flag to use the default.
  * REPOSITORY is the name of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) repository, you can omit this flag to use the default.



For example, to remove the tag `release-candidate` from package `my-package` in the repository `my-repo` in the default location, run the command:
    
    
    gcloud artifacts tags delete release-candidate --package=my-pkg \
        --repository=my-repo
    

## Installing packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote, virtual

To install a package from the Node.js package repository:

  1. If you are using the [credential helper](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#auth-helper) to authenticate with an access token, obtain a new token.

  2. Use the `npm install` or `yarn add` command.

###  npm 

To install version with the `latest` tag:
         
         npm install @SCOPE/PACKAGE
         

To install version with a different tag:
         
         npm install @SCOPE/PACKAGE@TAG
         

To install a specific version:
         
         npm install @SCOPE/PACKAGE@VERSION
         

###  yarn 

To install version with the `latest` tag:
         
         yarn add @SCOPE/PACKAGE
         

To install version with a different tag:
         
         yarn add @SCOPE/PACKAGE@TAG
         

To install a specific version:
         
         yarn add @SCOPE/PACKAGE@VERSION
         

Replace the following values:

     * SCOPE is the [scope](https://docs.cloud.google.com/artifact-registry/docs/nodejs#scopes) associated with the repository. If your Node.js package repository is not configured with a scope, omit `@SCOPE/` from the command.
     * PACKAGE is the name of the package in the repository.
     * TAG is tag for the version you want to install.
     * VERSION is the version number you want to install.



When you specify a package as a dependency in `package.json`, ensure that you include the scope for the repository. The following example shows the `@dev-repo` scope for a package named `my-package`.
    
    
    "dependencies": {
      "@dev-repo/my-package": ">=1.0.0"
    }
    

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

## Deleting packages

**[Repository modes](https://docs.cloud.google.com/artifact-registry/docs/repositories#mode):** standard, remote

You can delete a package and all its versions, or delete a specific version.

  * Once you delete a package, you cannot undo the action.
  * For remote repositories, only the cached copy of the package is deleted. The upstream source is unaffected. If you delete a cached package, Artifact Registry will download and cache it again the next time the repository receives a request for the same package version.



After a package version is published, you cannot republish a package with the same name and version combination, even after deleting the version. This is an [npm restriction](https://blog.npmjs.org/post/77758351673/npm-publish-f) to ensure that the contents of a published package version are always the same.

If you want to encourage users to install an updated package version, use the [npm deprecate](https://docs.npmjs.com/cli/deprecate) command to mark the old version of the package as deprecated. When a user tries to install the deprecated package, Artifact Registry returns a deprecation warning.

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

  * [Learn about managing Maven packages](https://docs.cloud.google.com/artifact-registry/docs/manage-packages)
  * [Learn about managing container images](https://docs.cloud.google.com/artifact-registry/docs/manage-images)
  * [Download individual files within a package](https://docs.cloud.google.com/artifact-registry/docs/repositories/download-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
