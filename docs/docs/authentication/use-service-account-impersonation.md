---
url: https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation/
title: Use service account impersonation \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:23.344875+00:00
---

# Use service account impersonation  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Use service account impersonation Stay organized with collections  Save and categorize content based on your preferences. 

When the principal you are using doesn't have the permissions you need to accomplish your task, or you want to use a service account in a development environment, you can use _service account impersonation_. 

When you use service account impersonation, you start with an authenticated principal (your user account or a service account) and request short-lived credentials for a service account that has the authorization that your use case requires. The authenticated principal must have the necessary permissions to impersonate the service account.

Service account impersonation is more secure than using a service account key because service account impersonation requires a prior authenticated identity, and the credentials that are created by using impersonation do not persist. In comparison, authenticating with a service account key requires no prior authentication, and the persistent key is a high risk credential if exposed.

For more information about service account impersonation, see [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

## Before you begin

Before you use service account impersonation, you need to enable the required APIs and ensure that you have the required roles.

### Enable APIs

To impersonate a service account, you need to enable the Service Account Credentials API in your project.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=iamcredentials.googleapis.com)

**Note:** If you're using the Google Cloud CLI, ensure that this API is enabled in the project that you're operating in.

### Required roles

To get the permission that you need to impersonate a service account, ask your administrator to grant you the [Service Account Token Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountTokenCreator) (`roles/iam.serviceAccountTokenCreator`) IAM role on the service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `iam.serviceAccounts.getAccessToken` permission, which is required to impersonate a service account. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

You must grant these roles to your account, even when you are working in a project that you created.

For more information about roles required for impersonation, see [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions#directly-impersonate).

You can use service account impersonation using the following methods:

  * Use the gcloud CLI
  * Set up Application Default Credentials for using client libraries
  * Generate and manage short-lived credentials



## Use the gcloud CLI

The gcloud CLI provides a straightforward way to use service account impersonation. This method works well when you need to use a service account to access Google Cloud resources or services by using the gcloud CLI.

You can impersonate a service account for a specific gcloud CLI command or set up the gcloud CLI to use impersonation for every command automatically.

### Use impersonation for a specific gcloud CLI command

To use impersonation for a specific gcloud CLI command, you use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account). For example, the following command lists storage buckets, using the identity and access provided by the specified service account:
    
    
    gcloud storage buckets list --impersonate-service-account=SERVICE_ACCT_EMAIL
    

When you use this flag, the gcloud CLI requests short-lived credentials for the specified service account and uses them to authenticate to the API and authorize the access. The principal that is logged in to the gcloud CLI (usually your user account) must have the required permission on the service account.

### Use impersonation with the gcloud CLI by default

To set up the gcloud CLI to use the identity and access provided by a service account by default, you use the [gcloud CLI config command](https://docs.cloud.google.com/sdk/gcloud/reference/config):
    
    
    gcloud config set auth/impersonate_service_account SERVICE_ACCT_EMAIL
    

With this config property set, the gcloud CLI requests short-lived credentials for the specified service account and uses them to authenticate to the API and authorize the access to the resource for every command. The principal that is logged in to the gcloud CLI must have the required permission on the service account.

To stop using service account impersonation by default for `gcloud` commands, unset the property with the following command:
    
    
    gcloud config unset auth/impersonate_service_account
    

## Set up Application Default Credentials for using client libraries

You can use service account impersonation to set up a local Application Default Credentials (ADC) file. Client libraries that support impersonation can use those credentials automatically. Local ADC files created by using impersonation are supported in the following languages: 

  * C#
  * Go
  * Java
  * Node.js
  * Python



Use service account impersonation to create a local ADC file: 
    
    
    gcloud auth application-default login --impersonate-service-account SERVICE_ACCT_EMAIL
    

You can now use client libraries using the supported languages the same way you would after setting up a local ADC file with user credentials. Credentials are automatically found by the authentication libraries. For more information, see [Authenticate for using client libraries](https://docs.cloud.google.com/docs/authentication/client-libraries). 

Credentials from a local ADC file generated by using service account impersonation are not supported by all of the authentication libraries. For more information, see [ Error returned for local credentials from service account impersonation](https://docs.cloud.google.com/docs/authentication/troubleshoot-adc#local-impersonated). 

## Generate and manage short-lived credentials

If neither of the previous methods address your use case, you need to generate and manage short-lived tokens. For example, if you need a different type of short-lived credential (something other than an access token), or if you need to use impersonation in a production environment, use this method.

For information about generating short-lived tokens, see [Create short-lived credentials for a service account](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct).

## What's next

  * Learn more about [how ADC finds credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials).
  * Explore [authentication methods](https://docs.cloud.google.com/docs/authentication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
