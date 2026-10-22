---
url: https://docs.cloud.google.com/artifact-registry/docs/docker/authentication/
title: Authenticate Docker to Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:38:59.593288+00:00
---

# Authenticate Docker to Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/docker/authentication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Authenticate Docker to Artifact Registry Stay organized with collections  Save and categorize content based on your preferences. 

Configuring Docker authentication for Artifact Registry lets you push and pull container images from your local workstation or external environments.

You don't need to configure authentication for Cloud Build or Google Cloud runtime environments such as Google Kubernetes Engine and Cloud Run, but you should verify that you have the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#gcp). 

## Before you begin

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. (Optional) [Configure defaults for gcloud CLI commands](https://docs.cloud.google.com/artifact-registry/docs/gcloud-defaults).
  3. Verify that the account you are using for authentication has [permission](https://docs.cloud.google.com/artifact-registry/docs/access-control) to access Artifact Registry. We recommend using a [service account](https://docs.cloud.google.com/iam/docs/service-accounts) rather than a user account.
  4. [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/) if it is not already installed. Docker is included in Cloud Shell.
  5. Docker requires privileged access to interact with registries. On Linux or Windows, add the user that you use to run Docker commands to the Docker security group. This step is not required on macOS since [Docker Desktop](https://docker-docs.uclv.cu/docker-for-mac/) runs on a virtual machine as the root user. 

### Linux

The Docker security group is called `docker`. To add your username, run the following command: 
         
         sudo usermod -a -G docker ${USER}
               

### Windows

The Docker security group is called `docker-users`. To add a user from the Administrator command prompt, run the following command:
         
         net localgroup docker-users DOMAIN\USERNAME /add
                 

Where:

     * DOMAIN is your Windows domain.
     * USERNAME is your username.

Log out and log back in for group membership changes to take effect. If you are using a virtual machine, you may need to restart the virtual machine for membership changes to take effect.

**Note:** The Docker security group has access that is equivalent to the root or Administrator user. Only add trusted users who require access to Docker. For details about security impacts, see [Docker daemon security](https://docs.docker.com/engine/security/security/#docker-daemon-attack-surface).



## Choosing an authentication method

The following authentication methods are available:

gcloud CLI credential helper
    Configure your Artifact Registry credentials for use with Docker directly in gcloud CLI. This is the simplest authentication method, but can be slower than the standalone credential helper.
Standalone Docker credential helper
    This option is primarily for configuring your credentials for use with Docker in the absence of Google Cloud CLI. It is significantly faster than the gcloud CLI credential helper and uses [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) to automatically find credentials in your environment.
Access token
    You can generate a short-lived access token for a service account and then use the token for password authentication. Since the token only valid for 60 minutes, it is a safer option than a service account key.
Service account key
    A user-managed key-pair that you can use as a credential for a service account. Because the credential is long-lived, it is the least secure option of all the available authentication methods.

When possible, use an access token or a credential helper to reduce the risk of unauthorized access to your container images. If you must use a service account key, ensure that you follow [best practices for managing credentials](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

**Warning:** The Docker credential helper is only supported for Docker 18.03 or later. A bug in earlier versions of the Docker client slows down `docker build` dramatically when credential helpers are configured.

### Authentication settings in the Docker configuration file

Docker saves authentication settings in the configuration file [config.json](https://docs.docker.com/engine/reference/commandline/cli/#configjson-properties).

  * Linux: `~/.docker/config.json`
  * Windows: `%USERPROFILE%\.docker\config.json`



There are separate sections in the file for different authentication methods:

`credHelpers`
    If you use the Docker credential helper for authentication Artifact Registry stores the credential helper settings in the `credHelpers` section of the file.
`auths`
    If you use Docker to sign in with a token or service account key as your password, Docker stores a base64-encoded version of your credentials in the `auths` section of the file.
`credStore`
    If you configured a [credential store](https://docs.docker.com/engine/reference/commandline/login/#credentials-store) to manage your credentials, the settings for the credential store are in the `credStore` section of the file.

When Docker connects to a registry, it checks first for a credential helper that is associated with the host. So if your `config.json` includes Artifact Registry settings in both the `credHelpers` and `auths` sections, the settings in the `auths` section are ignored.

## gcloud CLI credential helper

The gcloud CLI credential helper provides secure, short-lived access to your project resources. It configures Docker to authenticate to Artifact Registry hosts in any environment where the [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs) is installed. [Cloud Shell](https://console.cloud.google.com/?cloudshell=true) includes the Google Cloud CLI and a current version of Docker. 

The gcloud CLI credential helper is the simplest authentication method to set up. It configures Docker with the credentials of the active user or service account in your gcloud CLI session. Since this credential helper depends on gcloud CLI, it can be significantly slower than the standalone credential helper. For automated builds with third-party tools or Docker clients with a large number of configured registry hosts, use the standalone credential helper instead.

To authenticate to Artifact Registry:

  1. Sign in to gcloud CLI as the user that will run Docker commands.

     * To configure authentication with user credentials, run the following command:
           
           gcloud auth login
           

     * To configure authentication with service account credentials, run the following command:
           
           gcloud auth activate-service-account ACCOUNT --key-file=KEY-FILE
           

Replace the following:

       * ACCOUNT: the service account that you want to use with Artifact Registry in the format `USERNAME@PROJECT-ID.iam.gserviceaccount.com`. If you want to use an existing account, you can view a list of service accounts on the [Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts/) page of Google Cloud console or with the command `gcloud iam service-accounts list`
       * KEY-FILE: the service account key file. See the [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) for information about creating a key.
**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

  2. Run the following command:
         
         gcloud auth configure-docker HOSTNAME-LIST
         

Where HOSTNAME-LIST is a comma-separated list of repository hostnames to add to the credential helper configuration.

For example, to add the regions `us-west1` and `asia-northeast1`, run the command:
         
         gcloud auth configure-docker us-west1-docker.pkg.dev,asia-northeast1-docker.pkg.dev
         

The specified hostnames are added to the credential helper configuration. You can add other hostnames to the configuration later by running the command again.

To view a list of supported repository locations, run the command:
         
         gcloud artifacts locations list
         

  3. The command displays the `credHelpers` section of your current Docker configuration and the updated configuration after adding the specified hostnames.

To accept the configuration changes, enter `y`.

Your credentials are saved in your user home directory.

     * Linux: `$HOME/.docker/config.json`
     * Windows: `%USERPROFILE%/.docker/config.json`
  4. Docker requires credential helpers to be in the system `PATH`. Ensure that the `gcloud` command is in the system `PATH`.


**Note:** If you normally run Docker commands on Linux with `sudo`, Docker looks for Artifact Registry credentials in `/root/.docker/config.json` instead of `$HOME/.docker/config.json`. If you want to use `sudo` with `docker` commands instead of using the Docker security group, configure credentials with `sudo gcloud auth configure-docker` instead.

## Standalone credential helper

The standalone Docker credential helper configures Docker to authenticate to Artifact Registry on a system where the gcloud CLI isn't available. The standalone helper, which may be faster than the gcloud CLI credential helper, uses [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) (ADC) to automatically find credentials in the your environment. We recommend using this authentication method for automated builds with third-party tools or Docker clients with a large number of configured registry hosts.

The standalone Docker credential helper fetches your Artifact Registry credentials and writes them to the Docker configuration file. This way, you can use the Docker command-line tool, `docker`, to interact directly with Artifact Registry.

To use the Docker credential helper:

  1. Log on to the machine as the user who will run Docker commands.

  2. Download the standalone Docker credential helper from [GitHub](https://github.com/GoogleCloudPlatform/docker-credential-gcr/releases).

You can optionally use the `curl` command-line utility. For example:
         
         VERSION=2.1.29
         OS=linux  # or "darwin" for OSX, "windows" for Windows.
         ARCH=amd64  # or "386" for 32-bit OSs
         
         curl -fsSL "https://github.com/GoogleCloudPlatform/docker-credential-gcr/releases/download/v${VERSION}/docker-credential-gcr_${OS}_${ARCH}-${VERSION}.tar.gz" \
         | tar xz docker-credential-gcr \
         && chmod +x docker-credential-gcr && sudo mv docker-credential-gcr /usr/bin/
         

  3. Configure Docker to use your Artifact Registry credentials when interacting with Artifact Registry (you are only required to do this once):
         
         docker-credential-gcr configure-docker --registries=HOSTNAME-LIST
         

Where HOSTNAME-LIST is a comma-separated list of repository hostnames to add to the credential helper configuration.

For example, to add the regions `us-west1` and `asia-northeast1`, run the command:
         
         docker-credential-gcr configure-docker --registries=us-west1-docker.pkg.dev,asia-northeast1-docker.pkg.dev
         

The specified hostnames are added to the credential helper configuration. You can add other hostnames to the configuration later by running the command again.

To view a list of supported repository locations, run the command:
         
         gcloud artifacts locations list
         

See the [standalone Docker credential helper documentation](https://github.com/GoogleCloudPlatform/docker-credential-gcr) on GitHub for more information.

**Note:** If you normally run Docker commands on Linux with `sudo`, Docker looks for Artifact Registry credentials in `/root/.docker/config.json` instead of `$HOME/.docker/config.json`. If you want to use `sudo` with `docker` commands instead of using the Docker security group, configure credentials with `sudo docker-credential-gcr configure-docker` instead.

Your credentials are saved in your user home directory.

     * Linux: `$HOME/.docker/config.json`
     * Windows: `%USERPROFILE%/.docker/config.json`
  4. Docker requires credential helpers to be in the system `PATH`. Ensure that the `docker-credential-gcr` command is in the system `PATH`.

  5. To verify that the credential helper can successfully retrieve your credentials, run the following command:
         
         echo "https://HOSTNAME" | docker-credential-gcr get
         

Replace HOSTNAME with a hostname that you added to the configuration. For example:
         
         echo "https://us-west1-docker.pkg.dev" | docker-credential-gcr get
         

If the command is successful, the returned JSON output includes a token in the `Secret` field. For example:
         
         {"ServerURL":"https://us-west1-docker.pkg.dev","Username":"_dcgcr_2_0_0_token","Secret":"ya29..."}
         




Docker is now configured to authenticate with Artifact Registry. To push and pull images, make sure that [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) are correctly configured.

## Access token

You can generate a short-lived OAuth access token to authenticate with Artifact Registry. Since the token is valid for 60 minutes, you should request it less than an hour before you use it to connect with Artifact Registry.

To use an access token with service account credentials:

  1. [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating) to act on behalf of your application, or choose an existing service account that you use for automation.

  2. [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the service account to provide repository access.

  3. Generate an access token for the service account and authenticate:

You must have the permissions in the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to [impersonate](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts) a service account, to obtain a token for it, and then authenticate as the service account.

Run the following command, replacing ACCOUNT with your service account email address and LOCATION with the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository. 

### Linux
         
         gcloud auth print-access-token \
             --impersonate-service-account ACCOUNT | docker login \
             -u oauth2accesstoken \
             --password-stdin https://LOCATION-docker.pkg.dev
         

### Windows
         
         gcloud auth print-access-token --impersonate-service-account ACCOUNT | docker login -u oauth2accesstoken --password-stdin https://LOCATION-docker.pkg.dev
         




Docker is now authenticated with Artifact Registry.

## Service account key

**Note:** When possible, use an access token or credential helper to reduce the risk of unauthorized access to your artifacts. Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

Anyone who has access to a valid private key for a service account will be able to access resources through the service account. Note that the lifecycle of the key's access to the service account (and thus, the data the service account has access to) is independent of the lifecycle of the user who has downloaded the key.

Use the following guidelines to limit access to your repositories:

  * Create dedicated service accounts that are only used to interact with repositories.
  * [Grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the specific [Artifact Registry role](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) for the access required by the service account. For example, a service account that only downloads artifacts only requires the Artifact Registry Reader role.
  * Configure the permissions for your dedicated service accounts on each repository rather than at the project level. You can then specify access based on the repository context. For example, a service account for development builds might have the Artifact Registry Reader role for a production repository and the Artifact Registry Writer role for a staging repository.
  * Follow [best practices for managing credentials](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).



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

  3. Verify that [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control) are correctly configured for the service account. If you are using the Compute Engine service account, you must correctly configure both permissions and access scopes.

  4. Use the service account key to configure integration with Docker:

Run the following command:

### Linux / macOS
         
         cat KEY-FILE | docker login -u KEY-TYPE --password-stdin \
         https://LOCATION-docker.pkg.dev
         

### Windows
         
         Get-Content KEY-FILE |
         docker login -u KEY-TYPE --password-stdin https://LOCATION-docker.pkg.dev
         

Replace the following:

     * KEY-TYPE: one of the following: 
       * `_json_key` if you are using the service account key in JSON format as it was provided when you created the file.
       * `_json_key_base64` if you base64-encoded the all contents of the file.
     * KEY-FILE: the name of the service account key file in JSON format.
     * LOCATION: the regional or multi-regional [location](https://docs.cloud.google.com/artifact-registry/docs/repo-locations) of the repository where the image is stored.



Docker is now authenticated with Artifact Registry.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
