---
url: https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment/
title: Set up ADC for a local development environment \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:42:40.103389+00:00
---

# Set up ADC for a local development environment  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Set up ADC for a local development environment Stay organized with collections  Save and categorize content based on your preferences. 

You can provide either your user credentials or service account credentials to ADC in a local development environment.

## User credentials

When your code is running in a local development environment, such as a development workstation, the best option is to use the credentials associated with your [user account](https://docs.cloud.google.com/docs/authentication#user-accounts).

How you configure ADC with your user account depends on whether your [user account](https://docs.cloud.google.com/docs/authentication#user-accounts) is managed by Google—in other words, it is a Google Account—or by another identity provider (IdP), and federated by using [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 

###  Google Account 

To configure ADC with a Google Account, you use the Google Cloud CLI:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** To add scopes for services outside of Google Cloud, such as Google Drive, [create an OAuth Client ID](https://support.google.com/cloud/answer/6158849) and provide it to the `gcloud auth application-default login` command by using the [ `--client-id-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--client-id-file), specifying your scopes with the [ `--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--scopes). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




###  External IdP 

To configure ADC for a user account managed by an external IdP and federated with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation):

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




### Tips for configuring ADC with your user credentials

When you configure ADC with your user account, you should be aware of the following facts:

  * ADC configured with a user account might not work for some APIs without extra configuration steps. If you see an error message about the API not being enabled in the project, or that there is no quota project available, see [User credentials not working](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc#user-creds-client-based).

  * The local ADC file contains your refresh token. Any user with access to your file system can use it to get a valid access token. If you no longer need these local credentials, you can revoke them by using the [`gcloud auth application-default revoke` command](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/revoke).

  * Your local ADC file is associated with your user account, not your gcloud CLI configuration. Changing to a different gcloud CLI configuration might change the identity used by the gcloud CLI, but it does not affect your local ADC file or the ADC configuration.




## Service account credentials

You can configure ADC with credentials from a [service account](https://docs.cloud.google.com/docs/authentication#service-accounts) by using service account impersonation or by using a service account key.

### Service account impersonation

You can use service account impersonation to set up a local Application Default Credentials (ADC) file. Client libraries that support impersonation can use those credentials automatically. Local ADC files created by using impersonation are supported in the following languages: 

  * C#
  * C++
  * Go
  * Java
  * Node.js
  * PHP
  * Python
  * Ruby
  * Rust



You must have the Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) IAM role on the service account you are impersonating. For more information, see [Required roles](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation#required-roles). 

Use service account impersonation to create a local ADC file: 
    
    
    gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL
    

You can now use client libraries using the supported languages the same way you would after setting up a local ADC file with user credentials. Credentials are automatically found by the authentication libraries. For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries). 

Credentials from a local ADC file generated by using service account impersonation are not supported by all of the authentication libraries. For more information, see [ Error returned for local credentials from service account impersonation](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc#local-impersonated). 

### Service account keys

If you cannot use a user account or service account impersonation for local development, you can use a service account key.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

To create a service account key and make it available to ADC:

  1. Create a service account with the roles your application needs, and a key for that service account, by following the instructions in [Creating a service account key](https://docs.cloud.google.com/iam/docs/keys-create-delete#creating). 
  2. Set the environment variable `GOOGLE_APPLICATION_CREDENTIALS` to the path of the JSON file that contains your credentials. This variable applies only to your current shell session, so if you open a new session, set the variable again. 

**Example:** Linux or macOS
         
         export GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         export GOOGLE_APPLICATION_CREDENTIALS="/home/user/Downloads/service-account-file.json"

**Example:** Windows

For PowerShell:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="KEY_PATH"

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

For example:
         
         $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\username\Downloads\service-account-file.json"

For command prompt:
         
         set GOOGLE_APPLICATION_CREDENTIALS=KEY_PATH

Replace `KEY_PATH` with the path of the JSON file that contains your credentials.

**Note:** When you set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, ADC checks this location first, then checks other locations only if necessary. 


## What's next

  * Understand best practices for using [service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

  * Learn more about [how ADC finds credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

  * [Authenticate for using Cloud Client Libraries](https://docs.cloud.google.com/docs/authentication/client-libraries).

  * [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest).

  * Explore [authentication methods](https://docs.cloud.google.com/docs/authentication).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
