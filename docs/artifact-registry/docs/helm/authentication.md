---
url: https://docs.cloud.google.com/artifact-registry/docs/helm/authentication/
title: Set up authentication for Helm \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:06.647782+00:00
---

# Set up authentication for Helm  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/helm/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Set up authentication for Helm Stay organized with collections  Save and categorize content based on your preferences. 

Configuring Helm authentication for Artifact Registry lets you push, pull, and manage charts in Docker-format repositories. Authenticate by reusing your existing Docker credentials, generating a short-lived access token, or providing a service account key file.

## Before you begin

  1. If a repository for your charts does not exist, [create a new repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos). Choose Docker as the repository format.
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. (Optional) [Configure defaults for Google Cloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  4. [Install Helm 3.8.0 or later](https://helm.sh/docs/intro/install/). In previous versions of Helm, support for charts in OCI format is an experimental feature.

Run `helm version` to verify your version.




## Choosing an authentication method

In most situations, we recommend using a service account for authenticating to Artifact Registry.

The following authentication methods are available:

Use Artifact Registry credentials configured for Docker
    By default, Helm can authenticate with the same credentials that you use for Docker.
Access token
    [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) provide short-lived access tokens that a service account uses to access your Google Cloud resources.
JSON key file
    

A user-managed key-pair that you can use as a credential for a service account. Because the credential is long-lived, it is the least secure option of all the available authentication methods.

When possible, use an access token to reduce the risk of unauthorized access to your artifacts.

## Using your Docker configuration

By default, Helm supports registry settings in the Docker configuration file [config.json](https://docs.docker.com/engine/reference/commandline/login/#privileged-user-requirement). Helm finds registry settings in either the default location or the location specified by the [DOCKER_CONFIG](https://docs.docker.com/engine/reference/commandline/cli/#change-the-docker-directory) environment variable.

If you [configured Docker](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication) with a credential helper to authenticate with Artifact Registry, Helm uses your existing configuration for Artifact Registry Docker repositories.

## Using an access token

Access tokens are short-lived tokens that provide access to your Google Cloud resources. Since the token is short-lived, you should request it less than an hour before you use it to connect with Artifact Registry repositories.

Google Cloud obtains an access token using [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

To use an access token:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the appropriate Artifact Registry role to the service account to provide repository access.

  3. Assign the service account key file location to the variable `GOOGLE_APPLICATION_CREDENTIALS` so that the Artifact Registry credential helper can obtain your key when connecting with repositories.
         
         export GOOGLE_APPLICATION_CREDENTIALS=KEY-FILE
         

Where KEY-FILE is path to the service account [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

  4. Obtain an access token as credentials when you authenticate to Artifact Registry with Docker.

### Linux / macOS

Run the following command:
         
         gcloud auth application-default print-access-token | helm registry login -u oauth2accesstoken \
         --password-stdin LOCATION-docker.pkg.dev
         

### Windows

Run the following command:
         
         gcloud auth application-default print-access-token
         ya29.8QEQIfY_...
         
         helm registry login -u oauth2accesstoken -p "ya29.8QEQIfY_..." \
         LOCATION-docker.pkg.dev
         

Where

     * `oauth2accesstoken` is the username to use when authenticating with an access token.
     * `gcloud auth application-default print-access-token` is the Google Cloud CLI command to obtain the access token for the service account. Your access token is the password for authentication.
     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 



Helm is now authenticated with Artifact Registry.

## Using a JSON key file

**Note:** When possible, use an access token or to reduce the risk of unauthorized access to your artifacts. Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

Anyone who has access to a valid private key for a service account will be able to access resources through the service account. Note that the lifecycle of the key's access to the service account (and thus, the data the service account has access to) is independent of the lifecycle of the user who has downloaded the key.

Use the following guidelines to limit access to your repositories:

  * Create dedicated service accounts that are only used to interact with repositories.
  * Grant the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control) for the access required by the service account. For example, a service account that only downloads artifacts only requires the Artifact Registry Reader role.
  * Configure the permissions for your dedicated service accounts on each repository rather than at the project level. You can then specify access based on the repository context. For example, a service account for development builds might have the Artifact Registry Reader role for a production repository and the Artifact Registry Writer role for a staging repository.
  * Follow [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



To create a new service account and a service account key for use with Artifact Registry repositories only:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. You can optionally base64-encode all the contents of the key file.

### Linux
         
         base64 FILE-NAME > NEW-FILE-NAME
         

### macOS
         
         base64 -i FILE-NAME -o NEW-FILE-NAME
         

### Windows
         
         Base64.exe -e FILE-NAME > NEW-FILE-NAME
         

Where FILE-NAME is the original key filename and NEW-FILE-NAME is your base64-encoded key file.

  3. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the appropriate Artifact Registry role to the service account to provide repository access.

  4. Use the service account key to authenticate:

### Linux / macOS

Run the following command:
         
         cat KEY-FILE | helm registry login -u KEY-TYPE --password-stdin \
         LOCATION-docker.pkg.dev
         

### Windows

Run the following command:
         
         helm registry login -u KEY-TYPE --password-stdin LOCATION-docker.pkg.dev < KEY-FILE
         

Where

     * KEY-TYPE is one of the following: 
       * `_json_key` if you are using the service account key in JSON format as it was provided when you created the file.
       * `_json_key_base64` if you base64-encoded the all contents of the file.
     * KEY-FILE is the name of the service account key file in JSON format.
     * `LOCATION` is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 



Helm is now authenticated with Artifact Registry.

## What's next

  * [Learn about managing Helm charts saved as images](https://docs.cloud.google.com/artifact-registry/docs/helm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
