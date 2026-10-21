---
url: https://docs.cloud.google.com/artifact-registry/docs/go/store-go/
title: Quickstart: Store Go modules in Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:16.644468+00:00
---

# Quickstart: Store Go modules in Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/go/store-go/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Store Go modules in Artifact Registry

Artifact Registry Go repositories let you store, version, and share private Go modules across your projects. In this quickstart, you create a repository, package and upload a sample module, and import the module as a dependency.

## Before you begin

  1. [ Sign in](https://accounts.google.com/Login) to your Google Account.

If you don't already have one, [ sign up for a new account](https://accounts.google.com/SignUp).

  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  9. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  10. Enable the Artifact Registry API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=artifactregistry.googleapis.com)

  11. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  12. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  13. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  14. Install the [latest major version or second-latest major version](https://go.dev/doc/install) of Go. Earlier versions aren't supported.
  15. Install the `package-go-module` gcloud CLI add-on:   

         
         gcloud components install package-go-module




## Required roles

To get the permissions that you need to create and manage Artifact Registry Go module repositories, ask your administrator to grant you the [Artifact Registry Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.admin) (`roles/artifactregistry.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a repository

To create and configure a new repository:

  1. Run the following command to create a new repository.
         
         gcloud artifacts repositories create REPOSITORY \
             --repository-format=go \
             --location=LOCATION \
             --description=DESCRIPTION
         

Replace the following:

     * REPOSITORY is the name of the repository. For each repository location in a project, repository names must be unique.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repositories/repo-locations) for the repository. You can omit this flag if you set a [default](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults#set). To view a list of supported locations, run the command `gcloud artifacts locations list`.
     * DESCRIPTION is an optional description of the repository. Don't include sensitive data, since repository descriptions are not encrypted.
  2. Run the following command to view the repository details.
         
         gcloud artifacts repositories describe --location=LOCATION REPOSITORY
         

The output resembles the following:
         
         Encryption: Google-managed key
           Repository Size: 0.000MB
           createTime: '2022-06-03T20:20:01.644813Z'
           format: GO
           mode: STANDARD_REPOSITORY
           name: projects/my-project/locations/us-west1/repositories/my-repo
           updateTime: '2022-06-03T20:20:01.644813Z'
         




## Set defaults for gcloud commands

You can simplify your `gcloud CLI` commands by [configuring the defaults](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults) for project, repository and location values. Once defaults are configured, `--project`, `--location`, and `--repository` tags aren't needed.

## Package and upload a Go module

The `package-go-module` gcloud CLI add-on packages your Go modules, allowing you to version and upload to Artifact Registry using the `gcloud` command.

### Create a Go module

First, create a simple Go module to upload to your repository.

  1. In your home directory, create a directory named "foo" for your module
         
         mkdir foo
         

  2. Change directories into your module's directory and run `go mod init` to create a go.mod file for your module.
         
         cd foo \
           go mod init example.com/foo
         

Replace `example.com/foo` with the module path. See the [Go Modules Reference](https://go.dev/ref/mod#module-path) for more information.

  3. Create a `foo.go` file in your foo directory with the following contents:
         
         package foo
         
         const HelloWorld = "Hello World!"
         




### Package and upload your module

Package and upload the module to your repository:
    
    
      gcloud artifacts go upload --project=PROJECT \
          --repository=REPOSITORY \
          --location=LOCATION \
          --module-path=example.com/foo \
          --version=VERSION \
          --source=SOURCE_LOCATION
    

Replace the following:

  * PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
  * REPOSITORY with the name of the repository where the package is stored.
  * LOCATION with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
  * `example.com/foo` with the module path. See the [Go Modules Reference](https://go.dev/ref/mod#module-path) for more information.
  * VERSION with the [semantic version](https://pkg.go.dev/golang.org/x/mod/semver) of the module in the form `vX.Y.Z` where `X` is the major version, `Y` is the minor version, and `Z` is the patch version.
  * SOURCE_LOCATION with the path to the root directory of your Go module. If you omit the `--source` flag, the default is the current directory.



The module is uploaded to Artifact Registry.

For more information on creating Go modules, see this [tutorial](https://go.dev/doc/tutorial/create-module).

## List modules

Run the following command to inspect the uploaded Go module in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
      gcloud artifacts packages list
    

The output resembles the following:
    
    
      Listing items under project my-project, location us-west1, repository my-repo.
    
      PACKAGE                   CREATE_TIME          UPDATE_TIME
      example.com/foo           2022-06-03T20:43:39  2022-06-20T20:37:40
    

## View module version details

Run the following command to view the versions of your module in the default project, repository, and location when the [default values are configured](https://docs.cloud.google.com/artifact-registry/docs/repositories/gcloud-defaults):
    
    
      gcloud artifacts versions list --package=MODULE_PATH
    

The output resembles the following:
    
    
      Listing items under project my-project, location us-west1, repository my-repo, package example.com/foo.
    
      VERSION  DESCRIPTION  CREATE_TIME          UPDATE_TIME
      v0.1.0                2022-06-03T20:43:39  2022-06-03T20:43:39
      v0.1.1                2022-06-20T20:37:40  2022-06-20T20:37:40
    

## Download modules

To import modules stored in Artifact Registry, you need to instruct Go to look for dependencies from Artifact Registry, and bypass the [checksum database](https://sum.golang.org/).

### Set up the Go environment

  1. Instruct Go to download modules from Artifact Registry, the public Go module proxy, and then source in that order:
         
         export GOPROXY=https://LOCATION-go.pkg.dev/PROJECT/REPOSITORY,https://proxy.golang.org,direct
         

Replace the following:

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
     * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * REPOSITORY is the name of the repository where the package is stored.
  2. Exclude your module from being checked using the public checksum database:
         
         export GONOSUMDB=MODULE_PATH_REGEX
         

Replace MODULE_PATH_REGEX with your module path or a regex if you want to exclude multiple modules.

To exclude your module `example.com/foo` from being checked using the public checksum database, run the following command:
         
         export GONOSUMDB=example.com/foo
         

If you want all modules with module paths beginning in `example.com` to be excluded from being checked using the public checksum database, run the following command:
         
         export GONOSUMDB=example.com/*
         




### Authenticate to Artifact Registry

When downloading packaged Go modules to use as dependencies from Artifact Registry, the Go binary uses the credentials in your netrc file to authenticate to Artifact Registry. To simplify the authentication process, you can use the Go credential helper to refresh the tokens in your netrc file for authentication to Artifact Registry.

The location of your netrc file can be set with the netrc environment variable. If the `NETRC` variable is not set, then the `go` command will read `$HOME/.netrc` on UNIX-like platforms or `%USERPROFILE%\_netrc` on Windows.

Artifact Registry supports the following authentication methods.

Short-lived credentials (recommended)
    Use the Artifact Registry [Go credential helper tool](https://github.com/GoogleCloudPlatform/artifact-registry-go-tools) to update the authentication tokens in your netrc file.
Use a service account key
    

Use this option when you can't use credentials in your environment for authentication. Add the unencrypted service account key to your netrc file.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

#### Add the Go credential helper to `GONOPROXY`

Before using the Go credential helper you need to add it to the `GONOPROXY` list to force Go to download it directly from GitHub. If you have other modules you want to be downloaded directly from source you can add them in a comma separated list as shown in the following example:
    
    
      export GONOPROXY=MODULE_PATH1, MODULE_PATH2
    

Where MODULE_PATH1 and MODULE_PATH2 are module paths of modules to be downloaded from source.

To add the Go credential helper to your `GONOPROXY` list and run it to set up your credentials:

  1. Add the Go credential helper to your `GONOPROXY`
         
         export GONOPROXY=github.com/GoogleCloudPlatform/artifact-registry-go-tools
         

  2. Run the following command to add your Artifact Registry credentials to your netrc file with the Go module package tool:
         
         GOPROXY=proxy.golang.org \
               go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.4.0 \
               add-locations --locations=LOCATION \
               [--json_key=path/to/service/account/key.json]
         

Where LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository. To add multiple locations, enter them as a comma separated list.

The Go credential helper adds settings to your netrc file for authenticating to Artifact Registry. If you pass the `--json_key` flag the key is added to your netrc file for password authentication.




### Use your module as a dependency

  1. If you are using short-lived credentials for authenticating to Artifact Registry, you will need to refresh your OAuth token by running the following command:
         
         GOPROXY=proxy.golang.org \
           go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.4.0 refresh
         

  2. In your home directory, create a directory named "bar"
         
         mkdir bar
         

  3. Change directories into your module's directory and run `go mod init` to create a `go.mod` file for your package.
         
         cd bar \
           go mod init example.com/bar
         

Replace `example.com/bar` with the module path. See the [Go Modules Reference](https://go.dev/ref/mod#module-path) for more information.

  4. To require the version of foo stored in Artifact Registry, edit your `go.mod` file to resemble the following:
         
         module example.com/bar
         
         go 1.19
         
         require example.com/foo v0.1.0
         

Replace the following:

     * `example.com/foo` is the module path of the required module
     * `v0.1.0` is the version stored in Artifact Registry
  5. Create a `main.go` file in your `bar` directory with the following contents:
         
         
           package main
         
           import (
             "fmt"
         
             foo "example.com/foo"
           )
         
           func main() {
             fmt.Println(foo.HelloWorld)
           }
         
           
         

  6. Run go mod tidy to download dependencies, including the foo package:
         
         go mod tidy
         

  7. Run the bar module:
         
         go run .
         

The output resembles the following:
         
         Hello World!
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. Before you remove the repository, ensure that any modules you want to keep are available in another location.

  1. To delete the repository:
         
         gcloud artifacts repositories delete \
               --location=LOCATION \
               --project=PROJECT \
               REPOSITORY
         

Replace the following:

     * LOCATION with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
     * PROJECT with your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * REPOSITORY with the name of the repository.
  2. If you want to remove the default repository and location settings that you configured for the active gcloud configuration, run the following commands:
         
         gcloud config unset artifacts/repository
           gcloud config unset artifacts/location
         




## What's next

  * [Learn more about configuring authentication](https://docs.cloud.google.com/artifact-registry/docs/go/authentication).
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories).
  * [Learn about managing Go modules](https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules).
  * Read our resources about [DevOps](https://cloud.google.com/devops/) and explore the [DevOps Research and Assessment](https://dora.dev/) research program.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
