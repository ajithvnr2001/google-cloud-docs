---
url: https://docs.cloud.google.com/docs/authentication/gcloud/
title: Authenticate for the gcloud CLI \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:39:40.304878+00:00
---

# Authenticate for the gcloud CLI  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Authenticate for the gcloud CLI Stay organized with collections  Save and categorize content based on your preferences. 

This document is only about authentication for the Google Cloud CLI to access Google Cloud resources. If you need to authenticate workloads using Cloud Client Libraries or Google API Client Libraries, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## Before you begin

If you're new to Google Cloud and just want to get started using gcloud CLI commands in your local development environment, you can [initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize) with the following command:
    
    
    gcloud init
    

Initializing walks you through an authentication flow, sets up a [gcloud CLI configuration](https://docs.cloud.google.com/sdk/docs/configurations), and authorizes the gcloud CLI to act on your behalf. There's no need to perform a separate authentication step.

The rest of this document covers more complex scenarios such as using the gcloud CLI with different principal types, appropriate authentication methods for different environments, switching principals, and managing stored credentials.

## Authentication methods

All gcloud CLI commands need to authenticate to Google Cloud APIs. You can authenticate in the following ways:

  * **Authorize and store credentials** : Suitable for humans to use in a local development environment. You can authorize the gcloud CLI to act on behalf of a principal using the `gcloud auth login` command. After initial authentication, this command stores credentials in the gcloud CLI configuration directory. The gcloud CLI uses these stored credentials to authenticate automatically for subsequent commands until your session expires, or you revoke the authorization.

  * **Authenticate with a credential file** : Suitable for workloads running outside of Google Cloud. You can use environment variables or gcloud CLI configuration properties to specify a credential file for automatic authentication. This file can be one of the following:

    * A Workload Identity Federation credential configuration file.

    * A service account key.

  * **Provide an access token** : Suitable for highly isolated automated workflows or stateless sessions on shared machines. You can bypass credential storage by providing an access token directly to the gcloud CLI. You can do this by setting a specific environment variable to the raw access token string, or by pointing the gcloud CLI to a file containing the access token.




After authenticating, you can optionally let the gcloud CLI impersonate a service account by providing the service account's email address.

You can use multiple authentication methods in a single environment. However, only one principal is used for any given `gcloud` command. To determine which principal to use, the gcloud CLI follows a priority order.

### When you don't need to authenticate

You don't need to authenticate for the gcloud CLI in the following situations:

  * **Immediately after you've[ initialized the gcloud CLI](https://docs.cloud.google.com/sdk/docs/initialize)**. Authentication and authorizing the gcloud CLI to act on your behalf are included in the initialization process. You might still need to authenticate again if you need to access different resources using a different principal, or if you need to reauthenticate your principal. 
  * **When using the gcloud CLI from a resource that exposes a Compute Engine[ metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview)**. This includes resources such as Compute Engine VM instances, Cloud Run services, and Cloud Build builds. The gcloud CLI authenticates using the service account attached to the VM, and can access the same resources as that service account within the limits of any [ access scopes](https://docs.cloud.google.com/compute/docs/access/service-accounts#accesscopesiam) that have been applied. 
  * **When using Cloud Shell**. The gcloud CLI automatically authenticates using the principal you signed in to the Google Cloud console with. When you run a gcloud CLI command for the first time in a new Cloud Shell session, you are prompted to [ authorize Cloud Shell](https://docs.cloud.google.com/shell/docs/auth) using that principal. 



## Choose the right principal for the task

There are different types of principals for human use and automated workloads. The principal type you need to use affects how you authenticate.

  * **User accounts** : These are [Google Accounts](https://docs.cloud.google.com/iam/docs/principals-overview#google-account) that are for humans to do interactive work, such as incidental administrative tasks, non-programmatic configuration of Google Cloud services, testing, experimenting, and observability. 

You authenticate as a user account with user credentials, such as a password and one-time code. 

  * **Service accounts** : These are accounts specific to Google Cloud that workloads can use to access services or resources. You typically don't authenticate as a service account directly. Instead, you attach a service account to a resource such as a Compute Engine VM, or use service account impersonation. 

  * **Federated principals** : These are identities that reference user or service accounts in an external identity provider. There are two types of federated principals supported by Google Cloud, which have similar names: 

    * ****Workforce Identity Federation**** : Lets human users sign in to Google Cloud with identities managed by an external identity provider. If your organization already has single sign-on (SSO) set up, you might use this type of identity to authenticate to Google Cloud. 

Your identity provider must support [OpenID Connect (OIDC)](https://openid.net/connect/) or [ SAML 2.0](http://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html) to use Workforce Identity Federation. 

    * ****Workload Identity Federation**** : Lets workloads running outside of Google Cloud operate on Google Cloud resources. 

You can use Workload Identity Federation with workloads that authenticate using [ X.509 client certificates](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-x509-certificates); that run on [ Amazon Web Services (AWS) or Azure](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds); on-premises [ Active Directory](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-active-directory); deployment services, such as [ GitHub and GitLab](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-deployment-pipelines); and with any identity provider that supports [ OpenID Connect (OIDC) or Security Assertion Markup Language (SAML) V2.0](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers). 




## Use the gcloud CLI as a human

For interactive tasks, you typically authenticate with one of the following:

  * A user account

  * A federated user identity, using Workforce Identity Federation




### User accounts

How you authenticate with a user account for the gcloud CLI depends on whether a web browser is installed on your device.

###  My device has a web browser 

To authenticate with a user account on a device with a web browser, complete the following steps:

  1. Run the following command to start the process:
         
         gcloud auth login
         

  2. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands.




The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

###  My device doesn't have a web browser 

If the device you need to use the gcloud CLI on doesn't have a web browser, you can authenticate with your user account on another trusted device. This process changes depending on the software installed on the other trusted device.

#### Authenticate using another trusted device

Select which software is available on the other trusted device.

###  The gcloud CLI and a web browser 

Use the `--no-browser` flag to complete the authentication process on another device with a web browser and the gcloud CLI installed:

  1. Run the following command on the original device you want to use the gcloud CLI on:

###  Linux and macOS 
         
         gcloud auth login \
             --no-browser
         

###  Windows (PowerShell) 
         
         gcloud auth login `
             --no-browser
         

  2. Copy the `gcloud` command that begins with `gcloud auth login --remote-bootstrap="` to use on the other device.

  3. Go to a different, trusted device that has both a web browser and the gcloud CLI version 372.0.0 or later installed.

  4. In the terminal, run the command you copied earlier that begins with `gcloud auth login --remote-bootstrap="`, and complete the browser-based flow.

  5. In the terminal, copy the URL that begins with `https://localhost` to use on the original device.

  6. Return to the original device.

  7. In the terminal, at the prompt, paste the `https://localhost` URL that you copied earlier. Press `Enter` or `Return` on your keyboard to complete the process.




The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

###  Web browser only 

Use the `--no-launch-browser` flag to complete the authentication process using another device's web browser:

  1. Run the following command on the original device you want to use the gcloud CLI on:

###  Linux and macOS 
         
         gcloud auth login \
             --no-launch-browser
         

###  Windows (PowerShell) 
         
         gcloud auth login `
             --no-launch-browser
         

  2. Copy the URL that begins with `https://accounts.google.com/o/oauth2/auth` to use on the other device.

  3. Go to a different, trusted device that has a web browser installed.

  4. Open a web browser, go to the URL you copied earlier, and complete the browser-based flow.

  5. Copy the verification code to use on the original device.

  6. Return to the original device.

  7. In the terminal, at the prompt, paste the verification code you copied earlier. Press `Enter` or `Return` on your keyboard to complete the process.




The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

### Federated user identities

You can use the gcloud CLI with a federated user identity that's managed in an external identity provider (IdP). You do this with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

Before you begin, ensure you have a Workforce Identity Federation pool and provider set up to work with your IdP. For more information, see [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation).

To sign in to the gcloud CLI with a federated user identity, complete the following steps:

  1. Create a login configuration file:

Run the following command to create a login configuration file:

### Linux and macOS
         
         gcloud iam workforce-pools create-login-config \
             locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
             --output-file=LOGIN_CONFIG_PATH

### Windows (PowerShell)
         
         gcloud iam workforce-pools create-login-config `
             locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID `
             --output-file=LOGIN_CONFIG_PATH

**Note:** You can optionally activate the login configuration file as the default for the gcloud CLI by adding the [ `--activate`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/create-login-config#--activate) flag. You can then run `gcloud auth login` to authorize the gcloud CLI without specifying the login configuration file path each time. 

Replace the following:

     * `WORKFORCE_POOL_ID`: The Workforce Identity Federation pool ID.
     * `WORKFORCE_PROVIDER_ID`: The Workforce Identity Federation provider ID.
     * `LOGIN_CONFIG_PATH`: The path to write the login configuration file to. For example, `login-config.json`. 

The login configuration file contains the endpoints used by the gcloud CLI to enable the browser-based authentication flow and set the audience to the IdP that was configured in the workforce identity pool provider. The file doesn't contain confidential information. 

The login configuration file content looks similar to the following:
    
    {
      "universe_domain": "googleapis.com",
      "universe_cloud_web_domain": "cloud.google",
      "type": "external_account_authorized_user_login_config",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "auth_url": "https://auth.cloud.google/authorize",
      "token_url": "https://sts.googleapis.com/v1/oauthtoken",
      "token_info_url": "https://sts.googleapis.com/v1/introspect"
    }

**Caution:** We recommend that you first ensure that the contents of this file are correct and then safeguard the file—for example, by making it read-only and restricting access with an ACL. The file isn't validated; a malicious actor with write access to this file can change the endpoints and intercept credentials. 

  2. Sign in using browser-based authentication:

Point to the login configuration file with an environment variable, a property in the active gcloud CLI configuration, or use it directly with the `gcloud auth login` command: 

### Environment variable

To use the login configuration file with an environment variable, complete the following instructions: 

     1. Set the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable to the path of the login configuration file. 
     2. Run the following command:
            
            gcloud auth login

     3. The gcloud CLI references the environment variable to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 

To stop using the login configuration file for `gcloud auth login` commands, clear the `CLOUDSDK_AUTH_LOGIN_CONFIG_FILE` environment variable. 

### gcloud CLI configuration

To use the login configuration file with a gcloud CLI configuration property, complete the following instructions: 

     1. Set the active gcloud CLI configuration's `auth/login_config_file` property to the login configuration file's path with the following command: 
            
            gcloud config set auth/login_config_file LOGIN_CONFIG_PATH

     2. Run the following command:
            
            gcloud auth login

     3. The gcloud CLI references the configuration property to find the login configuration file, and then starts the authentication process. Follow the browser-based flow to authenticate and authorize the gcloud CLI to access resources on your behalf for future commands. 

To stop using the login configuration file for `gcloud auth login` commands, unset the property with the following command: 
    
    gcloud config unset auth/login_config_file

### gcloud auth login

To use the login configuration file directly with the `gcloud auth login` command, complete the following instructions: 

     * If you used the `--activate` flag when you created the login configuration file, run the following command: 
           
           gcloud auth login

     * If you didn't use the `--activate` flag when you created the login configuration file, run the following command: 

### Linux and macOS
           
           gcloud auth login \
               --login-config=LOGIN_CONFIG_PATH

### Windows (PowerShell)
           
           gcloud auth login `
               --login-config=LOGIN_CONFIG_PATH

Replace LOGIN_CONFIG_PATH with the path of your login configuration file. 

The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 




For more information, see [Sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud).

## Use the gcloud CLI with workloads

For automated workloads, you typically authenticate with one of the following:

  * A federated workload identity, using Workload Identity Federation

  * A service account, using impersonation




### Federated workload identities

You can use the gcloud CLI with a federated workload identity. You do this with [Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation).

A workload can either access Google Cloud resources directly by acting as a principal defined by a workload identity pool, or impersonate a service account attached to a workload identity pool.

We recommend using the direct access method to avoid over-permissioned service accounts, and to log resource access using the federated principal's identifier. Only use service account impersonation when [Google Cloud APIs don't support Workload Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services).

The following instructions assume you already have a Workload Identity Federation pool and provider set up to work with your IdP.

  1. [Create a credential configuration file for Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-providers#create-credential-config) by following the directions for your supported identity provider.

  2. Define the path to the credential configuration file in an environment variable, as a property in the active gcloud CLI configuration, or with the `gcloud auth login` command:

###  Environment variable 

Set the `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` environment variable to the path of the credential configuration file. The gcloud CLI references the file each time it runs a command, and obtains a credential from your IdP. This credential is exchanged for an access token to Google Cloud.

To stop using the credential configuration file, clear the `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` environment variable.

###  gcloud CLI configuration 

Set the active gcloud CLI configuration's `auth/credential_file_override` property to the credential configuration file's path with the following command:
         
         gcloud config set auth/credential_file_override CONFIGURATION_PATH
         

Replace `CONFIGURATION_PATH` with the path to the credential configuration file.

To stop using the credential configuration file by default for `gcloud` commands, unset the property with the following command:
         
         gcloud config unset auth/credential_file_override
         

###  gcloud auth login 

Run the following command using the [`--cred-file`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login#--cred-file) flag:

###  Linux and macOS 
         
         gcloud auth login \
             --cred-file=CONFIGURATION_PATH
         

###  Windows (PowerShell) 
         
         gcloud auth login `
             --cred-file=CONFIGURATION_PATH
         

Replace `CONFIGURATION_PATH` with the path to a credential configuration file.

The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 




### Service accounts

You can use the gcloud CLI with a service account in the following ways:

  * On a resource that exposes a Compute Engine [metadata server](https://docs.cloud.google.com/compute/docs/metadata/overview), such as a Compute Engine VM instance or Cloud Run service. The gcloud CLI uses whatever service account is attached to the resource to authenticate by default.

  * By using another principal to impersonate a service account.

  * By using a service account key.




###  Service account impersonation 

For resource access that isn't ordinarily available to your principal, we recommend you manage privilege escalation with [Privileged Access Manager](https://docs.cloud.google.com/iam/docs/pam-overview) instead of using [service account impersonation](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation).

If Privileged Access Manager doesn't fit your use case, complete the following steps to use the gcloud CLI with a service account: 

  1. To impersonate a service account, make sure the Service Account Credentials API is enabled in your project.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com)

  2. Choose a principal to use to impersonate a service account.

  3. To ensure that the principal has the necessary permission to impersonate a service account, ask your administrator to grant the [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role to the principal on the service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `iam.serviceAccounts.getAccessToken` permission, which is required to impersonate a service account. 

Your administrator might also be able to give the principal this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

  4. Authenticate for the gcloud CLI with the principal you chose earlier, whether a user account, federated user identity, federated workload identity, or another service account.

  5. Choose a service account to impersonate. Either [find an existing service account](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit), or [create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).

  6. Copy the service account's **Email** address.

  7. Choose whether to impersonate the service account for all commands, or only a single command:

###  All commands 

To use service account impersonation with the gcloud CLI for future commands, you can set an environment variable, or set a property in the active gcloud CLI configuration:

     * **Environment variable** : Set the `CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT` environment variable to the service account email address.

To stop using the service account, clear the `CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT` environment variable.

     * **gcloud CLI configuration** : Set the active gcloud CLI configuration's `auth/impersonate_service_account` property with the following command:
           
           gcloud config set auth/impersonate_service_account SERVICE_ACCOUNT_EMAIL
           

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of the service account.

To stop using service account impersonation by default for `gcloud` commands, unset the property with the following command:
           
           gcloud config unset auth/impersonate_service_account
           

###  Single command 

To use service account impersonation with the gcloud CLI for a single command, you can add the [`--impersonate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) flag to a gcloud CLI service command.

For example, to list Compute Engine VM instances using service account impersonation, run the following command:

###  Linux and macOS 
    
    gcloud compute instances list \
        --impersonate-service-account=SERVICE_ACCOUNT_EMAIL
    

###  Windows (PowerShell) 
    
    gcloud compute instances list `
        --impersonate-service-account=SERVICE_ACCOUNT_EMAIL
    

Replace `SERVICE_ACCOUNT_EMAIL` with the email address of the service account.




###  Service account key 

We recommend that you use Workload Identity Federation for most workloads that run outside of Google Cloud. Only use service account keys if your workload runs in an isolated external environment that doesn't support Workload Identity Federation.

Workload Identity Federation offers the following advantages:

  * Access to resources is granted through Identity and Access Management (IAM), with workloads treated as individual principals. This means you don't need to over-permission a service account for multiple use cases.

  * You can audit what workload is performing what task; actions aren't hidden behind a service account email address.

  * Workload Identity Federation uses short-lived access tokens to reduce the risk of exfiltration. Service account keys don't expire unless revoked manually.


**Caution:** Service account keys introduce [risks that need to be managed carefully](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

To use a service account with the gcloud CLI for future commands, do the following:

  1. [Create a service account key](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys#creating), and store it as a file in a secure location in your environment.

  2. Define the path to the service account key file in an environment variable, as a property in the active gcloud CLI configuration, or with the `gcloud auth login` command:

     * **Environment variable** : Set the `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` environment variable to the path of the service account key file.

To stop using the service account key, clear the `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` environment variable.

     * **gcloud CLI configuration** : Set the active gcloud CLI configuration's `auth/credential_file_override` property to the service account key's path with the following command:
           
           gcloud config set auth/credential_file_override KEY_PATH
           

Replace `KEY_PATH` with the path to the service account key file.

To stop using the service account key by default for `gcloud` commands, unset the property with the following command:
           
           gcloud config unset auth/credential_file_override
           

     * **`gcloud auth login`** : Run the following command using the [`--cred-file`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login#--cred-file) flag:

###  Linux and macOS 
           
           gcloud auth login \
               --cred-file=KEY_PATH
           

###  Windows (PowerShell) 
           
           gcloud auth login `
               --cred-file=KEY_PATH
           

Replace `KEY_PATH` with the path to the service account key file.

The [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command stores access credentials in your home directory. The authenticated principal becomes the active principal in your active gcloud CLI configuration. Unless overridden, the gcloud CLI uses these stored credentials to access Google Cloud. 

**Caution** : Any user with access to your file system can use the stored access credentials created by `gcloud auth login`. To reduce the consequences of a system being compromised, strictly separate human and workload use, and don't use `gcloud auth login` for automated workloads on remote systems with persistent storage. Where possible, use a secret manager in combination with environment variables instead. 

For more guidance on hardening remote systems, see [ Best practices for protecting developer credentials](https://docs.cloud.google.com/docs/security/bps-for-protecting-developer-credentials). 

**Note:** For P12 legacy format service account keys, use the [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) command.



## Use the gcloud CLI with an access token

If you've already authenticated for the gcloud CLI on another device, you can obtain an access token for that device's active principal with the following command:
    
    
    gcloud auth print-access-token
    

You can then use this access token on another device to access Google Cloud resources. Using an access token bypasses the need to set an active principal, and overrides any active principal set in the active gcloud CLI configuration.

Access tokens for user accounts have a default lifespan of one hour.

You can use an access token with the gcloud CLI for future commands, or only a single command.

###  All commands 

To use an access token with the gcloud CLI for future commands, you can set an environment variable, or set a property in the active gcloud CLI configuration:

  * **Environment variable** : Set the `CLOUDSDK_AUTH_ACCESS_TOKEN` environment variable to the access token string.

To stop using the access token, clear the `CLOUDSDK_AUTH_ACCESS_TOKEN` environment variable.

  * **gcloud CLI configuration** : Store the access token in a file, and then set the active gcloud CLI configuration's `auth/access_token_file` property to the file's path with the following command:
        
        gcloud config set auth/access_token_file ACCESS_TOKEN_PATH
        

Replace `ACCESS_TOKEN_PATH` with the path to the access token file.

To stop using an access token by default for `gcloud` commands, unset the property with the following command:
        
        gcloud config unset auth/access_token_file
        




###  Single command 

To use an access token with the gcloud CLI for a single command, you can add the [`--access-token-file`](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file) flag to a gcloud CLI service command:

  1. Store the access token in a file.

  2. Use the `--access-token-file` flag with any `gcloud` service command.

For example, to list Compute Engine VM instances using an access token, run the following command:

###  Linux and macOS 
         
         gcloud compute instances list \
             --access-token-file ACCESS_TOKEN_PATH
         

###  Windows (PowerShell) 
         
         gcloud compute instances list `
             --access-token-file ACCESS_TOKEN_PATH
         

Replace `ACCESS_TOKEN_PATH` with the path to the access token file.




## Credentials priority

Because multiple authentication methods might be used in one environment, the gcloud CLI evaluates the methods in a specific order to determine which principal to use. The gcloud CLI starts with provided credentials, and then assesses if service account impersonation has been requested.

The order of evaluation for provided credentials is as follows:

  1. The `CLOUDSDK_AUTH_ACCESS_TOKEN` environment variable, set to the access token string.

  2. Access token files. The methods used to define the access token file paths are evaluated in the following order:

     1. The [`--access-token-file`](https://docs.cloud.google.com/sdk/gcloud/reference#--access-token-file) command-line flag, used with any gcloud CLI command.

     2. The `CLOUDSDK_AUTH_ACCESS_TOKEN_FILE` environment variable.

     3. The [`auth/access_token_file`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#auth) property in the active gcloud CLI configuration.

  3. Credential files. The methods used to define the credential file paths are evaluated in the following order: 

     1. The `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE` environment variable.

     2. The [`auth/credential_file_override`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#auth) property in the active gcloud CLI configuration.

  4. The active principal set by the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command, or by setting the [`core/account`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#core) property.




### Service account impersonation priority

If service account impersonation has been requested, the gcloud CLI checks which service account to impersonate _after_ credentials have been provided for the principal that is doing the impersonation. The methods used to define service accounts for impersonation are evaluated in the following order:

  1. The [`--impersonate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) command-line flag.

  2. The `CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT` environment variable.

  3. The service account defined by the [`auth/impersonate_service_account`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#auth) property in the active configuration.




## Add Google Drive to your scope

The gcloud CLI scope can be expanded to include Google Drive access in addition to Google Cloud. This means you can use Google Cloud access tokens with Google Drive.

To expand the scope to include Google Drive, you add the `--enable-gdrive-access` flag when authorizing the gcloud CLI to act on your behalf:

###  Linux and macOS 
    
    
    gcloud auth login \
        --enable-gdrive-access
    

###  Windows (PowerShell) 
    
    
    gcloud auth login `
        --enable-gdrive-access
    

You can then make calls to Google Drive APIs using the gcloud CLI to provide an access token. For example, to list all files in your Google Drive, you can make the following request:

###  Linux and macOS 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://www.googleapis.com/drive/v3/files"
    

###  Windows (PowerShell) 
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers @{ "Authorization" = "Bearer $(gcloud auth print-access-token)" } `
      -ContentType "application/json; charset=utf-8" `
      -UseBasicParsing `
      -Uri "https://www.googleapis.com/drive/v3/files" | Select-Object -Expand Content
    

You can then, for example, use a file ID from the previous command's response to extract text from a Google Docs file:

###  Linux and macOS 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         "https://www.googleapis.com/drive/v3/files/FILE_ID/export?mimeType=text/plain"
    

###  Windows (PowerShell) 
    
    
    Invoke-WebRequest `
      -Method GET `
      -Headers @{ "Authorization" = "Bearer $(gcloud auth print-access-token)" } `
      -ContentType "application/json; charset=utf-8" `
      -UseBasicParsing `
      -Uri "https://www.googleapis.com/drive/v3/files/FILE_ID/export?mimeType=text/plain" | Select-Object -Expand Content
    

A common use case for Google Drive access is to [use BigQuery with data stored in Google Sheets](https://docs.cloud.google.com/bigquery/docs/external-data-drive).

To learn more about the Google Drive API, see [Google Drive API overview](https://developers.google.com/workspace/drive/api/guides/about-sdk). 

## Add the gcloud CLI as a credential helper to Docker

To pull from Artifact Registry container registries, you can [add the gcloud CLI as a credential helper](https://docs.cloud.google.com/artifact-registry/docs/docker/authentication#gcloud-helper) to your Docker configuration.

To do so, run the [`gcloud auth configure-docker`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/configure-docker) command:
    
    
    gcloud auth configure-docker REGION-docker.pkg.dev
    

## Manage principals and credentials

You can use the `gcloud auth login` command to authenticate multiple principals in the same environment, and authorize the gcloud CLI to access resources on their behalf. However, only one principal can be active at any time. The following sections cover managing the principals in your gcloud CLI configuration, including listing them, switching between them, and revoking their credentials.

### List principals

To list the principals whose access credentials are stored on the local system (that is, who have been authenticated using `gcloud auth login`), run the [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list) command:
    
    
    gcloud auth list
    

The gcloud CLI lists the principals and shows which principal is active:
    
    
    Credentialed Accounts
    ACTIVE  ACCOUNT
            alex@altostrat.com
    *       bola@altostrat.com
            principal://iam.googleapis.com/locations/global/workforcePools/POOL_ID/subject/cruz@cymbalgroup.com
    

Overrides for the active principal aren't included in this list. These include the following environment variables:

  * `CLOUDSDK_AUTH_ACCESS_TOKEN`
  * `CLOUDSDK_AUTH_CREDENTIAL_FILE_OVERRIDE`
  * `CLOUDSDK_AUTH_IMPERSONATE_SERVICE_ACCOUNT`



To check if these environment variables are set, run the following command for your operating system:

###  Linux and macOS 
    
    
    echo "$ENVIRONMENT_VARIABLE"
    

###  Windows (PowerShell) 
    
    
    echo $env:ENVIRONMENT_VARIABLE
    

Replace `ENVIRONMENT_VARIABLE` with the environment variable you want to check.

Overrides for the active principal also include the following configuration properties:

  * `auth/access_token_file`
  * `auth/credential_file_override`
  * `auth/impersonate_service_account`



To check if these configuration properties are set, run the following command:
    
    
    gcloud config list
    

### Switch active principals

To switch to an active principal that has stored credentials (that is, they previously completed the `gcloud auth login` flow), run [`gcloud config set`](https://docs.cloud.google.com/sdk/gcloud/reference/config/set):
    
    
    gcloud config set account PRINCIPAL_IDENTIFIER
    

Replace `PRINCIPAL_IDENTIFIER` with the full identifier of the principal.

You can also switch principals in the following ways:

  * [Create a separate configuration](https://docs.cloud.google.com/sdk/docs/configurations#creating_a_configuration) that specifies a different active principal, and then [activate that configuration](https://docs.cloud.google.com/sdk/docs/configurations#activating_a_configuration).

  * Use the [`--account`](https://docs.cloud.google.com/sdk/gcloud/reference#--account) command-line flag to specify a principal for a single command.

  * Use an override like a command-line flag, an environment variable, or configuration property.




### Set session lengths

Administrators can control how long different users can access the gcloud CLI without having to re-authenticate. For example, you can force users with elevated privileges to re-authenticate more frequently than regular users.

For more information, see [Set session length for Google Cloud services](https://support.google.com/a/answer/9368756).

### Revoke credentials for a principal

You can revoke credentials for principals who have authenticated with `gcloud auth login` so that the gcloud CLI can't act on their behalf. Revoking invalidates the credentials on Google's authorization servers, and removes the principal from the active gcloud CLI configuration.

To revoke credentials, run [`gcloud auth revoke`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/revoke):
    
    
    gcloud auth revoke PRINCIPAL_IDENTIFIER
    

Replace `PRINCIPAL_IDENTIFIER` with the full identifier of the principal.

To revoke access for the gcloud CLI on all devices associated with your Google Account, go to [Third-party apps & services](https://security.google.com/settings/security/permissions) in your Google Account settings, and delete all connections with the **Google Cloud SDK**. 

### Manage stored credentials

The gcloud CLI stores the credential files it uses in the gcloud CLI configuration directory. To find the location of the credential files, run [`gcloud info`](https://docs.cloud.google.com/sdk/gcloud/reference/info):
    
    
    gcloud info
    

The gcloud CLI prints information about your installation. Credential files are stored in the **User Config Directory** defined in the output:
    
    
    User Config Directory: [/home/USERNAME/.config/gcloud]
    

For Linux and macOS, the gcloud CLI configuration directory is typically `/home/USERNAME/.config/gcloud`. For Windows, it's `%APPDATA%\gcloud`.

## What's next

  * To learn more about customizing the gcloud CLI, see [gcloud CLI properties](https://docs.cloud.google.com/sdk/docs/properties).

  * To learn more about managing named sets of gcloud CLI properties, see [gcloud CLI configurations](https://docs.cloud.google.com/sdk/docs/configurations).

  * To authenticate code-based workloads that use Cloud Client Libraries or Google API Client Libraries, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
