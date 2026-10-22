---
url: https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication/
title: Configure authentication to Artifact Registry for npm \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:25.050579+00:00
---

# Configure authentication to Artifact Registry for npm  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure authentication to Artifact Registry for npm Stay organized with collections  Save and categorize content based on your preferences. 

You must authenticate to Artifact Registry when you use a third-party application to connect to a repository.

You don't need to configure authentication for Cloud Build or Google Cloud runtime environments such as Google Kubernetes Engine and Cloud Run, but you should verify that the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) are configured.

Node.js supports two methods for authenticating requests to your Artifact Registry repository:

  * [Access tokens](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#token-auth): Use access tokens when authentication in your application is managed by a human user.
  * [Password authentication](https://docs.cloud.google.com/artifact-registry/docs/nodejs/authentication#auth-password): Use this option when an application doesn't support Application Default Credentials but does support authentication with a username and password.



## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  2. (Optional) [Configure defaults for gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  3. If you are connecting to repositories from Windows, install [PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell).
  4. Create a service account to act on behalf of your application.
  5. If you are new to npm, read the [overview](https://docs.cloud.google.com/artifact-registry/docs/nodejs) to learn about scoped packages and the configuration file for your authentication settings.



## Generate tokens for authentication

To authenticate your package in Artifact Registry, you must first generate an authentication token. You can then use this token when you make requests from your package to Artifact Registry.

You can generate an `oauth2` access token using Google Cloud or an `oauth2l` token outside of Google Cloud.

Access tokens are valid for 60 minutes. Generate an access token shortly before running commands that interact with repositories. If your access token has expired, you must generate a new access token.

### Generate a token using gcloud

To generate an `oauth2` access token using Google Cloud, run the following command:
    
    
    export ACCESS_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
    

You can now reference `ACCESS_TOKEN` when you make requests from your Node.js package to Artifact Registry.

### Generate a token without using gcloud

To generate an access token using only the `oauth2l` CLI, do the following:

  1. Install the latest version of `oauth2l` by running the following command:
         
         go install github.com/google/oauth2l@latest
         

  2. Run the following command:
         
         export ACCESS_TOKEN="oauth2l fetch --scope cloud-platform"
         

Google Cloud generates an SHA256 hash token and stores it in the `ACCESS_TOKEN` variable. You can now reference `ACCESS_TOKEN` when you make requests from your Node.js package to Artifact Registry.




## Configure password authentication with service account keys

Use this approach when your Node.js application requires authentication with a specified username and password.

Service account keys are long-lived credentials. Use the following guidelines to limit access to your repositories:

  * Consider using a dedicated service account for interacting with repositories.
  * Grant the minimum [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control) required by the service account. For example, assign Artifact Registry Reader to a service account that only downloads artifacts.
  * If groups in your organization require different levels of access to specific repositories, grant access at the repository level rather than the project level.
  * Follow [best practices for managing credentials](https://docs.cloud.google.com/docs/authentication/production#best_practices_for_managing_credentials).



To create a service account and configure authentication:

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account to act on behalf of your application, or choose an existing service account that you use for automation.

You will need the location of the service account key file to set up authentication with Artifact Registry. For existing accounts, you can view keys and create new keys on the Service Accounts page.

[Go to the Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts)

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the service account to provide repository access.

  3. If you want to activate the service account in the current gcloud CLI session, run the command:
         
         gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
         

Where

     * ACCOUNT is the user or service account.
     * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).
  4. Run the following command to print the repository configuration:
         
         gcloud artifacts print-settings npm [--project=PROJECT] \
         [--repository=REPOSITORY] [--location=LOCATION] --scope=@SCOPE-NAME --json-key=KEY-FILE
         

Where

     * PROJECT is the project ID. If this flag is omitted, the current or default project is used.
     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     * SCOPE-NAME is the name of the npm [scope](https://docs.cloud.google.com/artifact-registry/docs/nodejs#scopes) to associate with the repository.

Using scopes ensures that you always publish and install packages from the correct repository.

Unscoped packages are associated with your default npm registry, typically the [npm public registry](https://www.npmjs.com/). If you don't specify a scope, the returned configuration sets your Artifact Registry repository as the default registry. This can cause problems if your Node.js projects need to install packages from both the public npm registry and your Artifact Registry repository.

     * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).

**Note:** The returned configuration settings includes a placeholder email address. An email address is required in the npm configuration to publish npm packages. The placeholder email address is not used by Artifact Registry for authentication.
  5. Add the returned configuration settings to the [.npmrc](https://docs.cloud.google.com/artifact-registry/docs/nodejs#npmrc) configuration file in your Node.js projects. This file is usually in the same directory as `package.json`. Make sure that you include these settings in Node.js projects for packages that you publish as well as projects that will install dependencies from your npm repository.

  6. If you have other Node.js repositories to connect to, repeat the previous steps to obtain the settings and add them to the `.npmrc` file.




## What's next

  * [Configure access to repositories](https://docs.cloud.google.com/artifact-registry/docs/access-control)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/nodejs/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
