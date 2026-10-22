---
url: https://docs.cloud.google.com/docs/quotas/quota-project/
title: Quota project overview \u00a0|\u00a0 Cloud Quotas \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:44.160305+00:00
---

# Quota project overview  |  Cloud Quotas  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/quotas/quota-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Quotas ](https://docs.cloud.google.com/docs/quotas)
  * [ Guides ](https://docs.cloud.google.com/docs/quotas/overview)



Send feedback 

#  Quota project overview Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the _quota project_ and how the quota project is determined. Make sure that your quota project is set correctly to help avoid errors and failed requests to the Cloud APIs.

You must specify a quota project because every request to a Google Cloud API is counted against a quota and because quotas are enforced by project. For more information, see [How to set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project) .

Note for gcloud CLI users: the _quota project_ is sometimes referred to as the _billing project_. This is because the [`billing_project` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project) takes precedence over the [`billing/quota_project` property](https://docs.cloud.google.com/sdk/gcloud/reference/config/set#quota_project) in your gcloud CLI configuration.

## How the quota project is determined

How the quota project is determined depends on the type of API method that you use: _resource-based API_ or _client-based API_. In rare cases, a service might have both types of API methods.

### Resource-based APIs

For resource-based Cloud APIs, the project that provides quota for an API call is also the project that contains the resource that is being accessed. For example, when you create a Compute Engine instance, you must specify the project for that new instance. The project then contains the newly created instance. Later, if you perform operations on the Compute Engine instance, the project that contains the instance provides the quota for the request. This applies regardless of whether you use the Google Cloud CLI, REST API, or client libraries.

You cannot change the quota project used by a request to a resource-based API. The request always uses the project that contains the resource that the request is operating on.

### Client-based APIs

If an API is not a resource-based API, it's a client-based API. For example, the Cloud Translation API is a commonly used client-based API.

Requests can fail if you make a request to a client-based API and the quota project cannot be identified. The quota project can be set in multiple ways and is verified by checking the following options. They appear in the order of precedence:

  * **Specified in request** : The quota project that was specified in the [request](https://docs.cloud.google.com/docs/quotas/set-quota-project#set-project-programmatically). (When using client libraries, you can also use [environment variables](https://docs.cloud.google.com/docs/quotas/set-quota-project#set-project-variable) in your requests.)

  * **API key** : If you use an API key to provide credentials for a request, the project associated with the API key is used as the quota project.

  * **Google Cloud CLI credentials** : If you use the gcloud CLI to get your access token, and you've authenticated to the gcloud CLI with your user credentials, the gcloud CLI shared project is sometimes used as the quota project. However, not all client-based APIs fall back on the shared project.

  * **Service account** : If the principal for the API call is a service account, including by impersonation, the project associated with the service account is used as the quota project.

  * **Workforce identity federation** : If the principal for the API is a workforce identity federation user, the [workforce pools user project](https://docs.cloud.google.com/iam/docs/workforce-identity-federation#workforce-pools-user-project) is used as the quota project.




If none of the previous checks yield a quota project, the request fails.

#### About the gcloud CLI shared project for client-based APIs

If you use the gcloud CLI to make a request to a client-based API without setting the quota project, the request might fall back on the _gcloud CLI shared project_ , or the request might fail. The gcloud CLI shared project is used by all gcloud CLI requests in all projects, so if many other gcloud CLI requests are also using this project as their quota project, the quota for the shared project might temporarily be depleted. If this happens, your request fails with an out-of-quota error message.

#### Identify the current quota project for client-based APIs

The method for identifying the quota project depends on how your project is configured:

  * If an API method is configured to use a resource-based API, the client project uses the resource project as the quota project.

  * If a user project override is in place, use the [`gcloud [command] --log-http` command](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http) to print a log and check the quota project that appears in the `x-goog-user-project` field.

  * If an API key was used for authentication, use the [`gcloud [command] --log-http` command](https://docs.cloud.google.com/sdk/gcloud/reference#--log-http) to print a log and check the quota project that appears in the `x-goog-api-key` field.




For other configurations, the quota project doesn't appear in HTTP headers.

## Determine if an API is resource-based or client-based

It can be difficult to determine which type of API you're using. However, activation and quotas are enforced in the same way. For example, if a service account from project A calls a read method in project B, and neither project has the API enabled, the `API not enabled` error message indicates which project is checked for activation. The project checked for activation is the same project checked for [rate quota](https://docs.cloud.google.com/docs/quotas/overview#types_of_quota).

## What's next

  * Learn how to set the [quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project)

  * Learn more about [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials)

  * Get more information about [authentication](https://docs.cloud.google.com/docs/authentication)

  * Understand [quotas](https://docs.cloud.google.com/docs/quotas/overview)

  * For gcloud CLI users:

    * For more information about gcloud CLI configurations, see the [`gcloud config`](https://docs.cloud.google.com/sdk/gcloud/reference/config) reference documentation
    * For more information about the `--billing_project` flag, see the [ Google Cloud SDK reference](https://docs.cloud.google.com/sdk/gcloud/reference#--billing-project)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
