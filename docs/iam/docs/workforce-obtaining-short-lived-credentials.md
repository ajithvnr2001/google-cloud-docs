---
url: https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials/
title: Obtain short-lived tokens for Workforce Identity Federation \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:55.740331+00:00
---

# Obtain short-lived tokens for Workforce Identity Federation  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Identity and Access Management (IAM) ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Obtain short-lived tokens for Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

You can use a workforce identity pool and workforce identity pool provider to obtain short-lived tokens from Security Token Service or the [Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview). These tokens let you access Google Cloud resources that [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services) and for which you have permissions.

You can use the methods described in this document on headless machines.

To obtain short-lived tokens, follow this high-level process:

  1. Obtain a credential from the trusted identity provider (IdP), or redirect users to the authorization endpoint (`https://auth.cloud.google/authorize`) to sign in with the IdP and obtain an authorization code.
  2. Exchange the credential or authorization code for a token from Security Token Service or the Cloud OAuth API.



## Before you begin

  1. [Configure Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/configuring-workforce-identity-federation) or, for IdP-specific instructions, see the following guides:

     * [Configure Microsoft Entra ID-based Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-sign-in-microsoft-entra-id)
     * [Configure Okta-based Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-sign-in-okta)

Note your workforce identity pool ID and workforce identity pool provider ID.

  2. Ensure that every principal for which tokens are exchanged using Security Token Service has the Identity and Access Management (IAM) permission `serviceusage.services.use`. The least-privileged role that contains this permission is Service Usage Consumer (`roles/serviceusage.serviceUsageConsumer`).

  3. Enable the IAM, Security Token Service, and the Cloud OAuth API APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,sts.googleapis.com,cloudoauth.googleapis.com,iamcredentials.googleapis.com&redirect=https%3A//console.cloud.google.com)

  4. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 



## Exchange external credentials for a Google Cloud access token

This section shows you how to use [Security Token Service](https://docs.cloud.google.com/iam/docs/reference/sts/rest) or the [Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-api-overview) to exchange your external credentials for an access token that grants access to Google Cloud. You can do this by using the gcloud CLI, the REST API, and the Cloud Client Libraries as described later in this document.

For instructions about how to obtain an authorization code from the authorization endpoint (`https://auth.cloud.google/authorize`) and exchange authorization codes and refresh tokens using the Cloud OAuth API, see [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens).

If you need long-lived access, you can configure a long-running process to continuously refresh credentials on that machine. Alternatively, you can run a local server in the background with an endpoint that returns the credentials.

### Browser-based sign-in with the gcloud CLI

This section describes how to configure gcloud CLI to use a browser-based sign-in flow. To do so, you create a sign-in configuration file and then either reference the file in calls to `gcloud auth login` or activate the file so that it is used by default.

#### Create the login configuration file

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

#### Sign in using browser-based authentication

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

### Use configuration files for sign-in

As an alternative to browser-based sign-in, this section shows you different ways to use credential configuration files to provide access to authenticated Google Cloud actions. Setting up the configuration files does not require you to be logged in to the gcloud CLI.

How you set up your configuration file depends on whether your IdP uses OIDC or SAML.

### OIDC

You can source the credentials that you use to set up your configuration file from the following sources:

  * File-sourced credentials
  * URL-sourced credentials
  * Non-interactive executable-sourced credentials
  * Interactive executable-sourced credentials



#### File-sourced credentials

When you use file-sourced credentials, tokens are loaded from a file. Another process must refresh this file with a new OIDC token before the old token expires. For example, if the token has a lifetime of one hour, you must refresh the file before it is one hour old.

To generate the configuration file with a file-sourced credential, execute the following command:
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:id_token \
        --credential-source-file=PATH_TO_OIDC_ID_TOKEN \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file=config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
  * `PATH_TO_OIDC_TOKEN`: the path to the OIDC IdP credential file
  * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID associated with the [workforce pools user project](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-pools-user-project).



The principal must have `serviceusage.services.use` permission on this project.

Running the command produces an OIDC IdP config file similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "file": "PATH_TO_OIDC_CREDENTIALS_FILE"
      }
    }
    

#### URL-sourced credentials

When you use URL-sourced credentials, tokens are loaded from a local server with an endpoint that responds to `HTTP GET` requests. The response must be an OIDC ID token, either in plain text or in JSON format.

To generate a configuration file with a URL-sourced credential, execute the following command:
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:id_token \
        --credential-source-url=URL_TO_RETURN_OIDC_ID_TOKEN \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file=config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `URL_TO_RETURN_OIDC_ID_TOKEN`: the URL to call to retrieve the OIDC credentials, such as an OIDC ID token—for example: `http://localhost:5000/token`.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number used for quota and billing. The principal needs to have `serviceusage.services.use` permission on this project.



Running the command produces an OIDC IdP config file similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "url": "URL_TO_RETURN_OIDC_ID_TOKEN"
      }
    }
    

#### Non-interactive executable-sourced credentials

When you use non-interactive executable-sourced credentials, tokens are loaded from a local executable. The executable must provide a valid, unexpired OIDC ID token in JSON format to `stdout`:
    
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:id_token",
      "id_token": "HEADER.PAYLOAD.SIGNATURE",
      "expiration_time": 1620499962
    }
    

These fields are required for a successful response, with the exception of `expiration_time`. The `expiration_time` field is only required when an output file has been specified in the credential configuration.

The executable must surface any errors to `stdout` in the following JSON format:
    
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

These fields are all required for an error response. The code and message fields are used by the client libraries when raising the appropriate error.

The command can return the following fields:

  * `version`: the version of the JSON output. Only version `1` is supported.
  * `success`: the status of the response. When the status is `true`, the executable must exit with exit code `0` and the response must contain the following fields:

    * `token_type`: `id_token`
    * `expiration_time` field, if an output file is specified in the credential configuration

When the status is `false`, the executable must exit with a non-zero value and the response must contain the following fields:

    * `code`
    * `message`
  * `token_type`: the third-party subject token type, which must be `urn:ietf:params:oauth:token-type:id_token`

  * `id_token`: the third-party OIDC token

  * `expiration_time`: the third-party OIDC token expiration time in seconds (Unix epoch time)

  * `code`: the error code string

  * `message`: the error message




The client libraries set the following environment variables when the executable is run:

  * `GOOGLE_EXTERNAL_ACCOUNT_AUDIENCE`: the audience field from the credential configuration. This variable is always set.
  * `GOOGLE_EXTERNAL_ACCOUNT_TOKEN_TYPE`: the expected subject token type. This variable is always set.
  * `GOOGLE_EXTERNAL_ACCOUNT_OUTPUT_FILE`: the output file location from the credential configuration. This variable is only present when it is specified in the credential configuration.



These environment variables can be used by the executable to avoid hardcoding these values.

To enable this credential sourcing method with the client libraries, the `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` environment variable must be set to `1`.

To generate the configuration file with an executable-sourced credential, run the following command:
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:id_token  \
        --executable-command=EXECUTABLE_COMMAND \
        --executable-timeout-millis=EXECUTABLE_TIMEOUT \
        --executable-output-file=EXECUTABLE_OUTPUT_FILE \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `EXECUTABLE_COMMAND`: the full command, including arguments, to run to retrieve the subject token, such as an OIDC ID token, in the following format: `--executable-command="/path/to/command --foo=bar"`.
  * `EXECUTABLE_TIMEOUT`: Optional. A duration, in milliseconds, to wait for the executable to run (defaults to 30s).
  * `EXECUTABLE_OUTPUT_FILE`: Optional. A path to the third-party credentials generated by the executable. This is useful for caching the credentials. The Auth libraries first check for this path before running the executable.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID that is used for quota and billing. The principal must have the `serviceusage.services.use` permission set on this project.



Running the command produces an OIDC IdP config file similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "executable": {
          "command": "EXECUTABLE_COMMAND",
          "timeout_millis": "EXECUTABLE_TIMEOUT",
          "output_file": "EXECUTABLE_OUTPUT_FILE"
        }
      }
    }
    

#### Interactive executable-sourced credentials

When you use interactive executable-sourced credentials, you can provide an executable that interacts with the user through `stdin` and `stdout`. If the user successfully signs in, the executable writes a valid, unexpired credential to the specified file.

To use this mode, the following flags are required:

  * `--executable-output-file`: the file that the executable writes the credential information to
  * `--exeutable-interactive-timeout-millis`: a non-zero value that indicates _interactive mode_ and sets the timeout—for example, `60000` for a 60-second timeout



The following fields are required for a successful response, with the exception of `expiration_time`:
    
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:id_token",
      "id_token": "HEADER.PAYLOAD.SIGNATURE",
      "expiration_time": 1620499962
    }
    

The executable must write any errors to the file specified in `--executable-output-file` in the following JSON format. The following fields are all required when returning an error response.
    
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

The `code` and `message` fields must indicate the appropriate error. These fields are used by the client libraries when raising the error.

Upon successful execution, the command returns the same fields for interactive and non-interactive executable-sourced credentials.

The environment variables are also the same for interactive and non-interactive executable-sourced credentials.

To generate an interactive executable-sourced credential, add the parameter `--executable-interactive-timeout-millis` and the parameter `--executable-output-file`.
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:id_token  \
        --executable-command=EXECUTABLE_COMMAND \
        --executable-interactive-timeout-millis=EXECUTABLE_INTERACTIVE_TIMEOUT \
        --executable-output-file=EXECUTABLE_OUTPUT_FILE \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `EXECUTABLE_COMMAND`: the full command, including arguments, to run to retrieve the subject token, formatted as follows: `--executable-command="/path/to/command --arg1=val1 --arg2=val2"`
  * `EXECUTABLE_INTERACTIVE_TIMEOUT`: a duration, in milliseconds, to wait for the executable to run.
  * `EXECUTABLE_OUTPUT_FILE`: a path to the third-party credentials generated by the executable. This path is useful for caching the credentials. The authentication libraries first check for this path before running the executable.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID used for quota and billing. The principal must have the `serviceusage.services.use` permission on this project.



Running the command produces an OIDC IdP config file similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:id_token",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "executable": {
          "command": "EXECUTABLE_COMMAND",
          "interactive_timeout_millis": "EXECUTABLE_INTERACTIVE_TIMEOUT",
          "timeout_millis": "EXECUTABLE_TIMEOUT",
          "output_file": "EXECUTABLE_OUTPUT_FILE",
        }
      }
    }
    

The `timeout_millis` field is returned because an interactive executable can also run in non-interactive mode, in some cases. In interactive mode, the command returns a default timeout.

### SAML

You can source the credentials that you use to set up your configuration file from the following sources:

  * File-sourced credentials
  * URL-sourced credentials
  * Executable-sourced credentials
  * Executable-sourced credentials for gcloud interactive mode



#### File-sourced credentials

Assertions are loaded from a file. Another process must refresh this file with a new base64-encoded SAML assertion before the old assertion expires. For example, if the assertion has a lifetime of one hour, you must refresh the file before it is one hour old.

**Note:** You must pass the `--subject-token-type=urn:ietf:params:oauth:token-type:saml2` flag when you generate the configuration file.
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --output-file=federation_config.json \
        --credential-source-file=CREDENTIAL_FILE \
        --subject-token-type=urn:ietf:params:oauth:token-type:saml2 \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `CREDENTIAL_FILE`: the path to the credential file that is generated by the IdP.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID that is used for quota and billing. The principal must have `serviceusage.services.use` permission on this project.



#### URL-sourced credentials

Assertions are loaded from a local server with an endpoint that responds to HTTP `GET` requests. The response must be either a [base64-encoded](https://toolbox.googleapps.com/apps/encode_decode/) SAML assertion or JSON containing a base64-encoded SAML assertion. To use URL-sourced credentials, use the `--credential-source-url` flag: ```sh gcloud iam workforce-pools create-cred-config \ locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \ \--output-file=federation_config.json \ \--credential-source-url=CREDENTIAL_URL \ \--subject-token-type=urn:ietf:params:oauth:token-type:saml2 \ \--workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT ``` Replace the following: * `WORKFORCE_POOL_ID`: the workforce identity pool ID. * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID. * `CREDENTIAL_URL`: the URL of the local server endpoint. * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID used for quota and billing. The principal needs to have `serviceusage.services.use` permission on this project. 

#### Executable-sourced credentials

Assertions are loaded from a local executable. The executable must provide a valid, unexpired SAML assertion in JSON format to `stdout`.
    
    
    {
      "version": 1,
      "success": true,
      "token_type": "urn:ietf:params:oauth:token-type:saml2",
      "saml_response": "...",
      "expiration_time": 1620499962
    }
    

These fields are required for a successful response, with the exception of `expiration_time`. The `expiration_time` field is required only when an output file is specified in the credential configuration.

If an error occurs, it must be surfaced by the executable in the following JSON format to stdout:
    
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

These fields are all required for an error response. The code and message fields are used by the client libraries when raising the appropriate error.

The command can return the following fields:

  * `version`: the version of the JSON output. Only version `1` is supported.
  * `success`: the status of the response. When the status is `true`, the executable must exit with exit code `0` and the response must contain the following fields:

    * `token_type`: `saml_response`
    * `expiration_time` field, if an output file is specified in the credential configuration

When the status is `false`, the executable must exit with a non-zero value and the response must contain the following fields: \+ `code` \+ `message`

  * `token_type`: the third-party subject token type, which must be `urn:ietf:params:oauth:token-type:saml2`

  * `saml_response`: the third-party SAML response

  * `expiration_time`: the third-party SAML response expiration time in seconds (Unix epoch time)

  * `code`: the error code string

  * `message`: the error message




The client libraries set the following environment variables when the executable is run:

  * `GOOGLE_EXTERNAL_ACCOUNT_AUDIENCE`: the audience field from the credential configuration. This variable is always set.
  * `GOOGLE_EXTERNAL_ACCOUNT_TOKEN_TYPE`: the expected subject token type. This variable is always set.
  * `GOOGLE_EXTERNAL_ACCOUNT_OUTPUT_FILE`: the output file location from the credential configuration. This variable is only present when it is specified in the credential configuration.

**Note:** The executable can use these environment variables to avoid hardcoding these values.

To enable this credential sourcing method with the client libraries, set the `GOOGLE_EXTERNAL_ACCOUNT_ALLOW_EXECUTABLES` environment variable to `1`.

To generate the configuration file with a executable-sourced credential, execute the following command:
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:saml2  \
        --executable-command=EXECUTABLE_COMMAND \
        --executable-timeout-millis=EXECUTABLE_TIMEOUT \
        --executable-output-file=EXECUTABLE_OUTPUT_FILE \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `EXECUTABLE_COMMAND`: the full command, including arguments, to run to retrieve the subject token, in the following format: `--executable-command="/path/to/command --foo=bar"`.
  * `EXECUTABLE_TIMEOUT`: Optional. The duration in milliseconds to wait for the executable to run (defaults to 30s).
  * `EXECUTABLE_OUTPUT_FILE`: Optional. The path to the third-party identity (3PI) credentials generated by the executable. This is useful for caching the credentials. The authorization libraries check for its existence before running the executable.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number used for quota and billing. The principal must have the `serviceusage.services.use` permission on this project.



Running the command produces a SAML IdP config file that is similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID",
      "subject_token_type": "urn:ietf:params:oauth:token-type:saml2",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "WORKFORCE_POOL_USER_PROJECT",
      "credential_source": {
        "executable": {
          "command": "EXECUTABLE_COMMAND",
          "timeout_millis": "EXECUTABLE_TIMEOUT",
          "output_file": "EXECUTABLE_OUTPUT_FILE"
        }
      }
    }
    

#### Executable-sourced credentials for gcloud interactive mode

When you use executable-sourced credentials for gcloud interactive mode, an executable interacts with the user through the command line interface.

In the previous command, replace the following:

  * `EXECUTABLE_OUTPUT_FILE`: Required. The path to the file that provides the credentials generated by the executable.
  * `EXECUTABLE_TIMEOUT`: Required. A non-zero timeout value also signals the command to use interactive mode.


    
    
        {
          "version": 1,
          "success": true,
          "token_type": "urn:ietf:params:oauth:token-type:saml2",
          "saml_response": "...",
          "expiration_time": 1620499962
        }
    

These fields are required for a successful response, with the exception of `expiration_time`. When `expiration_time` is omitted, the executable is still run.

The executable must surface any errors to the `executable-output-file` in the following JSON format. When the executable reports an error, these fields are all required. The code and message fields are used by the client libraries when raising the appropriate error.
    
    
    {
      "version": 1,
      "success": false,
      "code": "401",
      "message": "Caller not authorized."
    }
    

Successful command execution returns the same fields as non-interactive executable-sourced credentials.

The environment variables are also the same as a non-interactive executable-sourced credentials.

To generate an interactive executable-sourced credential, add the parameter `--executable-interactive-timeout-millis`.
    
    
    gcloud iam workforce-pools create-cred-config \
        locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID \
        --subject-token-type=urn:ietf:params:oauth:token-type:saml2  \
        --executable-command=EXECUTABLE_COMMAND \
        --executable-interactive-timeout-millis=EXECUTABLE_INTERACTIVE_TIMEOUT \
        --executable-output-file=EXECUTABLE_OUTPUT_FILE \
        --workforce-pool-user-project=WORKFORCE_POOL_USER_PROJECT \
        --output-file /path/to/generated/config.json
    

Replace the following:

  * `WORKFORCE_POOL_ID`: the workforce identity pool ID.
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID.
  * `EXECUTABLE_COMMAND`: the full command, including arguments, to run to retrieve the subject token, formatted as follows: `--executable-command="/path/to/command --foo=bar")`.
  * `EXECUTABLE_INTERACTIVE_TIMEOUT`: a duration, in milliseconds, to wait for the executable to run.
  * `EXECUTABLE_OUTPUT_FILE`: a path to the third-party credentials generated by the executable. This is useful for caching the credentials. The authentication libraries first check for this path before running the executable.
  * `WORKFORCE_POOL_USER_PROJECT`: the project number or ID used for quota and billing. The principal must have the `serviceusage.services.use` permission on this project.



Running the command produces a SAML IdP config file similar to the following:
    
    
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/locations/global/workforcePools/<var>WORKFORCE_POOL_ID<var>/providers/<var>WORKFORCE_PROVIDER_ID</var>",
      "subject_token_type": "urn:ietf:params:oauth:token-type:saml2",
      "token_url": "https://sts.googleapis.com/v1/token",
      "workforce_pool_user_project": "<var>WORKFORCE_POOL_USER_PROJECT</var>",
      "credential_source": {
        "executable": {
          "command": "<var>EXECUTABLE_COMMAND</var>",
          "interactive_timeout_millis": "<var>EXECUTABLE_INTERACTIVE_TIMEOUT</var>",
          "timeout_millis": "<var>EXECUTABLE_TIMEOUT</var>",
          "output_file": "<var>EXECUTABLE_OUTPUT_FILE</var>",
        }
      }
    }
    

**Note:** `timeout_millis` is included in the configuration because an interactive executable-sourced credential can also run in non-interactive mode in some cases. The gcloud CLI configuration generator auto fills that field with default timeout setting of 30 seconds.

To sign in, run the following command:
    
    
    gcloud auth login --cred-file=/path/to/config.json
    

Note that neither the gcloud CLI nor the bq command-line tool support executable-sourced credential types.

For headless flows, the gcloud CLI automatically uses the following scope: `https://www.googleapis.com/auth/cloud-platform`. The gcloud CLI then transparently posts your credentials to the Security Token Service endpoint, where it is exchanged for temporary Google Cloud access tokens.

You can now execute `gcloud` commands using the gcloud CLI.

### Use the Google Cloud client libraries

If you use a supported client library, you can configure the client library so that it generates Google credentials automatically. When possible, we recommend that you generate credentials automatically, so that you don't need to implement the token-exchange process yourself.

Google Cloud client libraries support workforce pools in the following languages: Node.js, Java, Python, Go, and C++ (gRPC).

To use client libraries with these services or languages, do the following:

###  bq tool 

To authenticate using Workforce Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command:
    
    
    gcloud auth login --cred-file=FILEPATH.json
    

where `FILEPATH` is the path to the credential configuration file.

Support for Workforce Identity Federation in the bq tool is available in [version 390.0.0 and later versions of the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

### C++

Most of the [Google Cloud Client Libraries for C++](https://github.com/googleapis/google-cloud-cpp) support Workforce Identity Federation by using a `ChannelCredentials` object, which is created by calling `grpc::GoogleDefaultCredentials()`. To initialize this credential, you must build the client libraries with version 1.42.0 or later of [gRPC](https://github.com/grpc/grpc).

The Cloud Storage Cloud Client Libraries for C++ uses the REST API, not gRPC, so it doesn't support Workforce Identity Federation.
    
    
    auto creds = grpc::GoogleDefaultCredentials();
    
    // Create a channel, stub and make RPC calls (same as in the previous example)
    auto channel = grpc::CreateChannel("greeter.googleapis.com", creds);
    std::unique_ptr<Greeter::Stub> stub(Greeter::NewStub(channel));
    grpc::Status s = stub->sayHello(&context, *request, response);
    

###  gcloud 

To authenticate using Workforce Identity Federation, use the [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) command:
    
    
    gcloud auth login --cred-file=FILEPATH.json
    

Replace `FILEPATH` with the path to the credential configuration file.

Support for Workforce Identity Federation in the gcloud CLI is available in [version 392.0.0 and later versions of the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/components#updating_components).

### Go

Cloud Client Libraries for Go support Workforce Identity Federation when you use version v0.0.0-20211005180243-6b3c2da341f1 or later of the `golang.org/x/oauth2` module.
    
    
    import (
      "context"
      "fmt"
      "log"
    
      "cloud.google.com/go/storage"
      "google.golang.org/api/iterator"
      "google.golang.org/api/option"
      "io/ioutil"
    )
    ctx := context.Background()
    client, err := storage.NewClient(ctx)
    # Explicit initialization can also be used.
    # var jsonPath = "/path/to/3p-credentials.json"
    # client, err := storage.NewClient(ctx, option.WithCredentialsFile(jsonPath))
    if err != nil {
      log.Fatal(err)
    }
    fmt.Println("Buckets:")
    it := client.[Buckets](https://docs.cloud.google.com/go/docs/reference/cloud.google.com/go/storage/latest/index.html#cloud_google_com_go_storage_Client_Buckets)(ctx, projectID)
    for {
      battrs, err := it.Next()
      if err == iterator.Done {
        break
      }
      if err != nil {
        log.Fatal(err)
      }
      fmt.Println(battrs.Name)
    }
    

### Java

Cloud Client Libraries for Java support Workforce Identity Federation when you use version 1.2.0 or later of the [`com.google.auth:google-auth-library-oauth2-http` artifact](https://search.maven.org/artifact/com.google.auth/google-auth-library-oauth2-http).
    
    
    import com.google.auth.oauth2.[GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html);
    import com.google.cloud.storage.[Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html);
    import com.google.cloud.storage.[StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html);
    
    [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) credentials = [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html).[getApplicationDefault](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html#com_google_auth_oauth2_GoogleCredentials_getApplicationDefault__)();
    [GoogleCredentials](https://docs.cloud.google.com/java/docs/reference/google-auth-library/latest/com.google.auth.oauth2.GoogleCredentials.html) sourceCredentials = credentials
        .createScoped(Arrays.asList("https://www.googleapis.com/auth/devstorage.read_only"));
    
    [Storage](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.Storage.html) storageService = [StorageOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.StorageOptions.html).newBuilder().setProjectId("project-id")
        .setCredentials(sourceCredentials).build().[getService](https://docs.cloud.google.com/java/docs/reference/google-cloud-storage/latest/com.google.cloud.storage.transfermanager.TransferManagerConfig.html#com_google_cloud_storage_transfermanager_TransferManagerConfig_getService__)();
    

### Node.js

Cloud Client Libraries for Node.js support Workforce Identity Federation when you use version 7.10.0 or later of the [`google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs).

Unlike workload identity pools, workforce identity pools are associated with an organization and not a Google Cloud project. When you create a `GoogleAuth` object, you must specify a project ID. For more information, see the [README for the `google-auth-library` package](https://github.com/googleapis/google-auth-library-nodejs#using-external-identities).
    
    
    const auth = new GoogleAuth({
      scopes: 'https://www.googleapis.com/auth/cloud-platform',
      // Specify a project ID.
      projectId: 'CLOUD_RESOURCE_PROJECT_ID',
    });
    
    # API request using Auth library.
    const client = await auth.getClient();
    const url =
        `https://storage.googleapis.com/storage/v1/b?projects=${projectId}`;
    const res = await client.request({url});
    console.log(res.data);
    

### Python

Cloud Client Libraries for Python support Workforce Identity Federation when you use version 2.3.0 or later of the [`google-auth` package](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth).
    
    
    from google.cloud import [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest)
    import google.auth
    
    credentials, project = google.auth.default(
        scopes=['https://www.googleapis.com/auth/devstorage.read_only'])
    
    client = [storage](https://docs.cloud.google.com/python/docs/reference/storage/latest).[Client](https://docs.cloud.google.com/python/docs/reference/storage/latest/google.cloud.storage.client.Client.html)(
        project="project-id", credentials=credentials)
    
    

In the example code, the `project` value can be `None` if the library is unable to automatically discover the project ID. You can pass the project ID explicitly when using a service instance, as the storage client example does, or set the project ID through the environment variable `GOOGLE_CLOUD_PROJECT`.

For details, see the [user guide for the `google-auth` package](https://github.com/googleapis/google-cloud-python/blob/main/packages/google-auth/docs/user-guide.rst#using-external-identities).

### Use the REST API

To obtain an authorization code from the authorization endpoint (`https://auth.cloud.google/authorize`) and exchange authorization codes or refresh tokens using the Cloud OAuth API (`cloudoauth.googleapis.com`), see [Exchange tokens with the Cloud OAuth API](https://docs.cloud.google.com/iam/docs/cloud-oauth-exchange-tokens).

You can also call the Google Cloud Security Token Service API to exchange your external credentials for Google Cloud access tokens by running the following command:
    
    
    curl https://sts.googleapis.com/v1/token \
        --data-urlencode "audience=//iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/providers/WORKFORCE_PROVIDER_ID" \
        --data-urlencode "grant_type=urn:ietf:params:oauth:grant-type:token-exchange" \
        --data-urlencode "requested_token_type=urn:ietf:params:oauth:token-type:access_token" \
        --data-urlencode "scope=https://www.googleapis.com/auth/cloud-platform" \
        --data-urlencode "subject_token_type=SUBJECT_TOKEN_TYPE" \
        --data-urlencode "subject_token=EXTERNAL_SUBJECT_TOKEN"  \
        --data-urlencode "options={\"userProject\":\"BILLING_PROJECT_NUMBER\"}"
    

Replace the following:

  * `AUDIENCE`: the full [resource name](https://docs.cloud.google.com/apis/design/resource_names) of the provider that issues the subject token.
  * `WORKFORCE_POOL_ID`: the workforce identity pool ID
  * `WORKFORCE_PROVIDER_ID`: the workforce identity pool provider ID
  * `SUBJECT_TOKEN_TYPE`: set to one of the following:

    * `urn:ietf:params:oauth:token-type:id_token` for OIDC ID tokens
    * `urn:ietf:params:oauth:token-type:saml2` for SAML assertions
  * `EXTERNAL_SUBJECT_TOKEN`: the IdP-issued token that represents the identity of the principal for whom the access token is requested.

If you configured an OIDC provider, the token must be JWT formatted.

  * `BILLING_PROJECT_NUMBER`: the project number or ID used for quota and billing. The principal must have the `serviceusage.services.use` permission on this project.




The response is similar to the following:
    
    
    {
      "access_token": "ya29.dr.AaT61Tc6Ntv1ktbGkaQ9U_MQfiQw...",
      "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
      "token_type": "Bearer",
      "expires_in": 3600
    }
    

### Manage sessions using the gcloud CLI

The temporary Google Cloud tokens that the gcloud CLI obtains from the Security Token Service endpoint expire after a specified time interval. When the token is about to expire, the gcloud CLI inspects the credentials file you provided and inspects the validity of the credentials you received from your IdP. If your credentials are still valid, the gcloud CLI proceeds to transparently obtain a new Google Cloud access token, and your current session runs without interruption.

If your credentials have expired, then no new Google Cloud tokens are issued, and any calls you make with those credentials fail. At this point, you must re-authenticate.

You can terminate your session by executing the following command:
    
    
    gcloud auth revoke
    

To revoke all active sessions and short-lived credentials for a workforce pool subject across all clients as an administrator, follow the instructions on [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions). 

`gcloud` supports multiple user sessions. To get the list of sessions, including the session that is currently active, execute the following command:
    
    
    gcloud auth list
    

The output of the command is similar to the following:
    
    
    Credentialed Accounts
    ACTIVE    ACCOUNT
    *         bola@example.com
              principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/kalani@example.com

To switch to a different session and set it as active, execute the following command:
    
    
    gcloud config set account principal://iam.googleapis.com/locations/global/workforcePools/WORKFORCE_POOL_ID/subject/SUBJECT_ID
    

## What's next

  * [Delete Workforce Identity Federation users and their data](https://docs.cloud.google.com/iam/docs/workforce-delete-user-data)
  * [Revoke Workforce Identity Federation user sessions](https://docs.cloud.google.com/iam/docs/workforce-revoke-sessions)
  * Learn which Google Cloud products [support Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)
  * [Set up user access to console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
