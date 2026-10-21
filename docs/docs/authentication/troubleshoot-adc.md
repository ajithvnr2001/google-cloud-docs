---
url: https://docs.cloud.google.com/docs/authentication/troubleshoot-adc/
title: Troubleshoot your ADC setup \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:53:01.590095+00:00
---

# Troubleshoot your ADC setup  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/troubleshoot-adc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Troubleshoot your ADC setup Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some common problems you might encounter when using Application Default Credentials (ADC). 

For information about how ADC works, including where credentials are found, see [How Application Default Credentials works](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

## User credentials not working

If your API request returns an error message about user credentials not being supported by this API, the API not being enabled in the project, or no quota project being set, review the following information.

There are two kinds of Google Cloud APIs:

  * _Resource-based APIs_ , which use the project associated with the resources being accessed for billing and quota.

  * _Client-based APIs_ , which use the project associated with the client accessing the resources for billing and quota.




When you provide user credentials to authenticate to a client-based API, you must specify the project to use for billing and quota. This project is called the _quota project_.

There are a number of ways to specify a quota project, including the following options:

  * Update your ADC file to use a different project as the quota project:
        
        gcloud auth application-default set-quota-project YOUR_PROJECT
        

  * If you are using the gcloud CLI to call the API, you can set your quota project in your gcloud CLI config:
        
        gcloud config set billing/quota_project YOUR_PROJECT
        

  * If you are calling the REST or RPC API directly, use the `x-goog-user-project` HTTP header to specify a quota project in each request. For details, see [Set the quota project with a REST request](https://docs.cloud.google.com/docs/authentication/rest#set-billing-project).


**Note:** The API you are trying to use must be enabled in whatever project you specify.

You must have the `serviceusage.services.use` IAM permission for a project to be able to designate it as your billing project. The `serviceusage.services.use` permission is included in the Service Usage Consumer IAM role. If you don't have the `serviceusage.services.use` permission for any project, contact your security administrator or a project owner who can give you the Service Usage Consumer role in the project. 

For more information about quota projects, see [Quota project overview](https://docs.cloud.google.com/docs/quotas/quota-project). For information about additional ways to set the quota project, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

## Incorrect credentials

If your credentials don't seem to be providing the access you expect, or aren't found, check the following:

  * If you are using the gcloud CLI to access Google Cloud in a local environment, make sure you understand which credentials you are using. When you use the gcloud CLI, you are using the credentials you provided to the gcloud CLI by using the `gcloud auth login` command. You are not using the credentials you provided to ADC. For more information about these two sets of credentials, see [gcloud CLI authentication configuration and ADC configuration](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc#gcloud-credentials).

  * Make sure that the `GOOGLE_APPLICATION_CREDENTIALS` environment variable is set _only_ if you are using a service account key or other JSON file for ADC. The credentials pointed to by the environment variable take precedence over other credentials, including for Workload Identity Federation for GKE. 

  * Confirm that the principal making the request has the required IAM roles. If you are using user credentials, then the roles must be granted to the email address associated with the user account. If you are using a service account, then that service account must have the required roles.

  * If you provide an API key with the API request, the API key takes precedence over ADC in any location. If you have set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable and you are using an API key, the API might return a warning telling you that the credentials you provided to ADC are being ignored. To stop the warning, unset the `GOOGLE_APPLICATION_CREDENTIALS` environment variable. 




## Unrecognized credential type

If your API request returns an error that includes `Error creating credential from JSON. Unrecognized credential type`, make sure you are using a valid credential. Client ID files are not supported to provide credentials for ADC.

## Error returned for local credentials from service account impersonation

Credentials from a local ADC file generated by using service account impersonation are not supported by all of the authentication libraries. If your call returns an error similar to `Neither metadata server or valid service account credentials are found`, you can't use local impersonated credentials for this task.

To avoid this error, create your ADC file from your user credentials or run your code in an environment that has a metadata server available (such as Compute Engine).

## Unknown project `764086051850` used for request

Project `764086051850` is the project used by the gcloud CLI. If you see authentication errors referencing this project, you are trying to use a client-based API and you have not set both your project and your quota project for your configuration.

For more information, see User credentials not working.

## Access blocked when using scopes

When you attempt to create a local ADC file, and an error similar to `This app is blocked` or `Access blocked: Authorization Error` is returned, you might be attempting to use scopes that aren't supported by the [default ADC setup command](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#google-idp). Typically, this issue is caused by adding scopes for applications outside of Google Cloud, such as Google Drive.

By default, the access tokens generated from a local ADC file created with user credentials include the [ cloud-wide scope `https://www.googleapis.com/auth/cloud-platform`](https://docs.cloud.google.com/docs/authentication#authorization-gcp). To specify scopes explicitly, you use the [ `--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--scopes) with the `gcloud auth application-default login` command. 

To add scopes for services outside of Google Cloud, such as Google Drive, you can do one of the following: 

  * **OAuth authentication** : [Create an OAuth client ID](https://support.google.com/cloud/answer/6158849). Provide the client ID to the `gcloud auth application-default login` command by using the [ `--client-id-file` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--client-id-file), and specify your scopes with the [ `--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--scopes). 
  * **Service account authentication** : Create a service account. [ Impersonate the service account](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation) by providing its email address to the `gcloud auth application-default login` command with the `--impersonate-service-account` flag, and specify your scopes with the [ `--scopes` flag](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login#--scopes). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
