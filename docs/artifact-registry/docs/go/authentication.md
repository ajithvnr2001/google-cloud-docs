---
url: https://docs.cloud.google.com/artifact-registry/docs/go/authentication/
title: Set up authentication for Go \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:02.572241+00:00
---

# Set up authentication for Go  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/go/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Set up authentication for Go Stay organized with collections  Save and categorize content based on your preferences. 

Authentication to Artifact Registry is different for upload and download of packaged Go modules. When packaging and uploading a Go module to Artifact Registry, the gcloud CLI tool looks for credentials in your environment to set up authentication in the following order unless the `--json_key`flag is passed to use a service account key.

  1. [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production) (ADC), a strategy that looks for credentials in the following order:

     1. Credentials defined in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

     2. Credentials that the default service account for Compute Engine, Google Kubernetes Engine, Cloud Run, App Engine, or Cloud Run functions provides.

  2. Credentials provided by the Google Cloud CLI, including user credentials from the command `gcloud auth application-default login`.




The `GOOGLE_APPLICATION_CREDENTIALS` variable makes the account for authentication explicit, which makes troubleshooting easier. If you do not use the variable, verify that any accounts that ADC might use have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control). For example the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for Compute Engine VMs, Google Kubernetes Engine nodes, and Cloud Run revisions has read-only access to repositories. If you intend to upload from these environments using the default service account, you must modify the permissions.

When downloading packaged Go modules to use as dependencies from Artifact Registry, the Go binary uses the credentials in your netrc file to authenticate to Artifact Registry. To simplify the authentication process, you can use the Go credential helper to refresh the tokens in your netrc file for authentication to Artifact Registry.

The location of your netrc file can be set with the netrc environment variable. If the `NETRC` variable is not set, then the `go` command will read `$HOME/.netrc` on UNIX-like platforms or `%USERPROFILE%\_netrc` on Windows.

Artifact Registry supports the following authentication methods when using credentials in your netrc file:

Short-lived credentials (recommended)
    Use the Artifact Registry [Go credential helper tool](https://github.com/GoogleCloudPlatform/artifact-registry-go-tools) to update the authentication tokens in your netrc file using the credentials in your environment, or manually add your Artifact Registry credentials to the netrc file.
Use a service account key
    Use this option when you can't use credentials in your environment for authentication. You can use the Artifact Registry [Go credential helper tool](https://github.com/GoogleCloudPlatform/artifact-registry-go-tools) to add the unencrypted service account key to your netrc file or manually add it to the file.
**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

## Before you begin

  1. [Install Go](https://go.dev/doc/install) 1.15 or later.
  2. Install the package-go-module gcloud CLI add-on:
         
         gcloud components install package-go-module




## Set up the Go environment

  1. Instruct Go to download modules from Artifact Registry, the public Go module proxy, and then source in that order:
         
         export GOPROXY=https://LOCATION-go.pkg.dev/PROJECT/REPOSITORY,https://proxy.golang.org,direct
         

Replace the following:

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository.
     * PROJECT is your Google Cloud [project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).
     * REPOSITORY is the name of the repository where the package is stored.
  2. Exclude your module from being checked using the public checksum database:
         
         export GONOSUMDB=MODULE_PATH_REGEX
         

Replace MODULE_PATH_REGEX with your module path or a regular expression if you want to exclude multiple modules.

For example, To exclude module `example.com/foo` from being checked using the public checksum database, run the following command:
         
         export GONOSUMDB=example.com/foo
         

The following command excludes all modules with module paths beginning in `example.com` from being checked using the public checksum database:
         
         export GONOSUMDB=example.com/*
         




## Add Artifact Registry credentials to your netrc file

  1. Run the following command to add your Artifact Registry credentials to your netrc file with the Go credential helper:
         
         GOPROXY=proxy.golang.org \
               go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.4.0 \
               add-locations --locations=LOCATION \
               --json_key=PATH_TO_JSON_KEY
         

Where:

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository. To add multiple locations, enter them as a comma separated list.
     * PATH_TO_JSON_KEY Optional. The path to your service account key.

The Go credential helper adds settings to your netrc file for authenticating to Artifact Registry. If you pass the `--json_key` flag the key is added to your netrc file for password authentication.

  2. If you are using short-lived credentials for authenticating to Artifact Registry, you will need to refresh your OAuth token by running the following command before using your module as a dependency:
         
         GOPROXY=proxy.golang.org \
           go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.4.0 refresh
         




## Authenticating with a service account key

Use this approach when you require authentication with a username and password.

Service account keys are long-lived credentials. Use the following guidelines to limit access to your repositories:

  * Consider using a dedicated service account for interacting with repositories.
  * Grant the minimum [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control) required by the service account. For example, assign Artifact Registry Reader to a service account that only downloads artifacts.
  * If groups in your organization require different levels of access to specific repositories, grant access at the repository level rather than the project level.
  * Follow [best practices for managing credentials](https://docs.cloud.google.com/docs/authentication/production#best_practices_for_managing_credentials).



To configure authentication:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the appropriate Artifact Registry role to the service account to provide repository access.

  3. Run the following command to add your service account credentials to your netrc file with the Go credential helper:
         
         GOPROXY=proxy.golang.org \
               go run github.com/GoogleCloudPlatform/artifact-registry-go-tools/cmd/auth@v0.4.0 \
               add-locations --locations=LOCATION \
               --json_key=PATH_TO_JSON_KEY
         

Where:

     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository. To add multiple locations, enter them as a comma separated list.
     * PATH_TO_JSON_KEY is the path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

The Go credential helper adds the service account key to your netrc file for password authentication.




It's also possible to manually add your service account key to the netrc file in the following format:
    
    
    machine LOCATION.pkg.dev
    login _json_key_base64
    password KEY
    

Replace the following:

  * LOCATION with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository.
  * KEY with the base64-encoded key in your service account key file.



## Add the Go credential helper to `GONOPROXY`

Before using the Go credential helper you need to add it to the `GONOPROXY` list to force Go to download it directly from GitHub. If you have other modules you want to be downloaded directly from source you can add them in a comma-separated list as shown in the following example:
    
    
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
         

Where LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of your repository. To add multiple locations, enter them as a comma-separated list.

The Go credential helper adds settings to your netrc file for authenticating to Artifact Registry. If you pass the `--json_key` flag the key is added to your netrc file for password authentication.




## What's next

  * Try the [Quickstart](https://docs.cloud.google.com/artifact-registry/docs/go/store-go).
  * [Manage Go modules](https://docs.cloud.google.com/artifact-registry/docs/go/manage-modules).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
