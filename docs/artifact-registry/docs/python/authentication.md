---
url: https://docs.cloud.google.com/artifact-registry/docs/python/authentication/
title: Configure authentication to Artifact Registry for Python package repositories \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:23.617217+00:00
---

# Configure authentication to Artifact Registry for Python package repositories  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/python/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Configure authentication to Artifact Registry for Python package repositories Stay organized with collections  Save and categorize content based on your preferences. 

You must authenticate to Artifact Registry when you use a third-party application to connect to a repository.

You don't need to configure authentication for Cloud Build or Google Cloud runtime environments such as Google Kubernetes Engine and Cloud Run, but you should verify that the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp) are configured.

Artifact Registry supports the following authentication methods for Python package repositories:

  * Access tokens: Use access tokens in automation, CI/CD pipelines, container builds, or environments where installing the key ring library is not supported.
  * Python key ring library (Recommended for local development): Use this option on developer workstations to automatically handle credential refreshing.
  * Password authentication: Use this option when an application doesn't support Application Default Credentials but does support authentication with a username and password.



## Before you begin

  1. If the target repository does not exist, [create a new Python package repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos).
  2. Verify that Python 3 is installed. For installation instructions, see the Google Cloud [tutorial for setting up Python](https://docs.cloud.google.com/python/docs/setup).
  3. Verify that the user account or service account you are using has the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) to access the repository.
  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  5. (Optional) [Configure defaults for gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).



## Generate tokens for authentication

To authenticate your package in Artifact Registry, you must first generate an authentication token. You can then use this token when you make requests from your package to Artifact Registry.

You can generate an `oauth2` access token using Google Cloud or an `oauth2l` token outside of Google Cloud.

Access tokens are valid for 60 minutes. Generate an access token shortly before running commands that interact with repositories. If your access token has expired, you must generate a new access token.

### Generate a token using gcloud

To generate an `oauth2` access token using Google Cloud, run the following command:
    
    
    export ACCESS_TOKEN="oauth2accesstoken:$(gcloud auth print-access-token)"
    

You can now reference `ACCESS_TOKEN` when you make requests from your Python package to Artifact Registry.

### Generate a token without using gcloud

To generate an access token using only the `oauth2l` CLI, do the following:

  1. Install the latest version of `oauth2l` by running the following command:
         
         go install github.com/google/oauth2l@latest
         

  2. Run the following command:
         
         export ACCESS_TOKEN="oauth2l fetch --scope cloud-platform"
         

Google Cloud generates an SHA256 hash token and stores it in the `ACCESS_TOKEN` variable. You can now reference `ACCESS_TOKEN` when you make requests from your Python package to Artifact Registry.




### Authenticate with pip

After exporting `ACCESS_TOKEN`, you can pass it to `pip` to install packages:
    
    
    pip install PACKAGE --index-url https://$ACCESS_TOKEN@LOCATION-python.pkg.dev/PROJECT/REPOSITORY/simple/
    

## Authenticate with key ring

The Python [key ring](https://pypi.org/project/keyring/) library provides applications with a way to access _key ring backends_ , meaning operating system and third-party credential stores. Artifact Registry provides the [keyrings.google-artifactregistry-auth](https://pypi.org/project/keyrings.google-artifactregistry-auth) key ring backend to handle authentication with Artifact Registry repositories.

The instructions in this section describe configuring pip as the only package index that pip searches for packages. We recommend using [virtual repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories/virtual-repo) to search packages across your private packages in Artifact Registry and public packages from PyPI instead of configuring multiple package indexes in the pip configuration file. The pip tool does not search package indexes in any particular order, so your consumers might mistakenly download or install a public package with the same name as one of your private packages. Virtual repositories let you configure priorities for upstream sources to mitigate this dependency confusion risk.

### Credential search order

When you use the Artifact Registry key ring backend, your credentials are not stored in your Python project. Instead, Artifact Registry searches for credentials in the following order:

  1. [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/production) (ADC), a strategy that looks for credentials in the following order:

     1. Credentials defined in the `GOOGLE_APPLICATION_CREDENTIALS` environment variable.

     2. Credentials that the default service account for Compute Engine, Google Kubernetes Engine, Cloud Run, App Engine, or Cloud Run functions provides.

  2. Credentials provided by the Google Cloud CLI, including user credentials from the command `gcloud auth application-default login`.




The `GOOGLE_APPLICATION_CREDENTIALS` variable makes the account for authentication explicit, which makes troubleshooting easier. If you do not use the variable, verify that any accounts that ADC might use have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control). For example the [default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for Compute Engine VMs, Google Kubernetes Engine nodes, and Cloud Run revisions has read-only access to repositories. If you intend to upload from these environments using the default service account, you must modify the permissions.

### Set up key ring

To set up authentication with the Artifact Registry key ring backend:

  1. Install the key ring library.
         
         pip install keyring
         

  2. Install the Artifact Registry backend.
         
         pip install keyrings.google-artifactregistry-auth
         

  3. List backends to confirm the installation.
         
         keyring --list-backends
         

The list should include

     * `ChainerBackend(priority:10)`
     * `GooglePythonAuth(priority: 9)`
  4. Run the following command to print the repository configuration to add to your Python project.
         
         gcloud artifacts print-settings python --project=PROJECT \
             --repository=REPOSITORY \
             --location=LOCATION
         

Replace the following values:

     * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  5. Add the following settings to the `.pypirc` file. The default location is:

     * Linux and macOS: `$HOME/.pypirc`
     * Windows: `%USERPROFILE%\.pypirc`
    
    [distutils]
    index-servers =
        PYTHON-REPO-ID
    
    [PYTHON-REPO-ID]
    repository = https://LOCATION-python.pkg.dev/PROJECT/REPOSITORY/
    

Replace the following values:

     * PYTHON-REPO-ID is an ID for the repository that you can reference with tools like Twine.
     * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
  6. Add your repository to the pip configuration file. The [file location](https://pip.pypa.io/en/stable/user_guide/#config-file) depends on whether you want to update the per-user file or the file specific to a virtual environment that you are using.

For the file associated with your operating system user:

     * Unix: `$HOME/.config/pip/pip.conf` or `$HOME/.pip/pip.conf`
     * macOS: `/Library/Application Support/pip/pip.conf` or `$HOME/.config/pip/pip.conf`
     * Windows: `%APPDATA%\pip\pip.ini` or `%USERPROFILE%\pip\pip.ini`

For virtual environments:

     * Unix and macOS: `$VIRTUAL_ENV/pip.conf`
     * Windows: `%VIRTUAL_ENV%\pip.ini`

To configure pip to only search your repository, use the `index-url` setting and make sure there are no other package indexes configured with the `extra-index-url` setting.
    
    [global]
    index-url = https://LOCATION-python.pkg.dev/PROJECT/REPOSITORY/simple/
    

The `/simple/` string at the end of the repository path indicates that the repository implements the [Python Simple Repository API](https://www.python.org/dev/peps/pep-0503/).




Your Python environment is now configured to authenticate with Artifact Registry.

### key ring authentication with user credentials

After you have set up key ring, you can use key ring with your user credentials in the gcloud CLI. Sign in to Google Cloud CLI before connecting to a Python package repository.

Run the following command:
    
    
    gcloud auth login
    

**Note:** Artifact Registry searches for credentials in a specific order. If service account credentials are found first, those credentials are used instead of your user credentials.

### key ring authentication with service account credentials

After you have set up key ring, you can set up a service account for authentication.

  1. [Create](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) a service account, or choose an existing service account that you use for automation.
  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the service account to provide repository access.
  3. Use one of the following options to authenticate with your service account:

     * **Application Default Credentials (Recommended)**

Assign the service account key file location to the variable `GOOGLE_APPLICATION_CREDENTIALS` so that the Artifact Registry credential helper can obtain your key when connecting with repositories.
           
           export GOOGLE_APPLICATION_CREDENTIALS=KEY-FILE
           

     * **gcloud CLI credentials**

Before connecting to a repository, sign in as the service account. Avoid this option if you are connecting to repositories from Compute Engine VMs since Artifact Registry finds the VM service account credentials before credentials in the gcloud CLI.
           
           gcloud auth activate-service-account --key-file=KEY-FILE
           

Replace KEY-FILE with the path to the service account [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).




## Configure password authentication with service account keys

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

  3. Run the following command to print the repository configuration to add to your Python project.
         
         gcloud artifacts print-settings python --project=PROJECT \
             --repository=REPOSITORY \
             --location=LOCATION \
             --json-key=KEY-FILE
         

Replace the following values:

     * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     * KEY-FILE is path to the service account JSON [key file](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).
  4. Add the following settings to the `.pypirc` file. The default location is for the per-user pip configuration file is:

     * Linux and macOS: `$HOME/.pypirc`
     * Windows: `%USERPROFILE%\.pypirc`
    
    [distutils]
    index-servers =
        PYTHON-REPO-ID
    
    [PYTHON-REPO-ID]
    repository = https://LOCATION-python.pkg.dev/PROJECT/REPOSITORY/
    username: _json_key_base64
    password: KEY
    

Replace the following values:

     * PYTHON-REPO-ID is an ID for the repository that you can reference with tools like Twine.
     * PROJECT is the project ID. If this flag is omitted, the current or [default project](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults#project) is used.
     * REPOSITORY is the ID of the repository. If you configured a [default](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults) Artifact Registry repository, it is used when this flag is omitted from the command.
     * LOCATION is the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) for the repository.
     * KEY is the base64-encoded key in your service account key file.
  5. Add your repository to the pip configuration file. The [pip configuration file location](https://docs.cloud.google.com/artifact-registry/docs/python/\(https:/pip.pypa.io/en/stable/user_guide#config-file) depends on whether you want to update the per-user file or the file specific to a virtual environment that you are using.

For the file associated with your operating system user:

     * Unix: `$HOME/.config/pip/pip.conf` or `$HOME/.pip/pip.conf`
     * macOS: `/Library/Application Support/pip/pip.conf` or `$HOME/.config/pip/pip.conf`
     * Windows: `%APPDATA%\pip\pip.ini` or `%USERPROFILE%\pip\pip.ini`

For virtual environments:

     * Unix and macOS: `$VIRTUAL_ENV/pip.conf`
     * Windows: `%VIRTUAL_ENV%\pip.ini`

Add the following line to the pip configuration file:
    
    [global]
    index-url = https://_json_key_base64:KEY@LOCATION-python.pkg.dev/PROJECT/REPOSITORY/simple/
    

     * KEY the private key in your service account key file.
     * The `/simple/` string at the end of the repository path indicates that the repository implements the [Python Simple Repository API](https://www.python.org/dev/peps/pep-0503/).



## What's next

  * [Configure access to repositories](https://docs.cloud.google.com/artifact-registry/docs/access-control)
  * [Learn about managing repositories](https://docs.cloud.google.com/artifact-registry/docs/repositories)
  * [Learn about managing packages](https://docs.cloud.google.com/artifact-registry/docs/python/manage-packages)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
