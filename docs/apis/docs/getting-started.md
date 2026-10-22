---
url: https://docs.cloud.google.com/apis/docs/getting-started/
title: Getting started \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:17.886170+00:00
---

# Getting started  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/getting-started/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  Getting started Stay organized with collections  Save and categorize content based on your preferences. 

Setting up a Google Cloud project and configuring authentication lets you call Google Cloud APIs from your applications. In this document, you get started with Google Cloud APIs by creating a project, discovering and enabling services in the API Library, linking a billing account, setting up credentials, and exploring client libraries.

If you're new to Google Cloud, [create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads.

## Creating a Google Cloud project

To use Google Cloud APIs, you need to have a user account (a Google account or an account from an [external identity provider](https://docs.cloud.google.com/iam/docs/workforce-identity-federation)) and a Google Cloud project. A project is equivalent to a developer account. It serves as a resource container for your Google Cloud resources. It also provides an isolation boundary for your usage of Google Cloud services, so you can manage quota limits and billing independently at the project level. Usage telemetry and dashboards are grouped by projects as well. If you don't already have a project, you can create one using the [Google Cloud console](https://console.cloud.google.com/).

A project can own a wide range of resources, including API keys, OAuth clients, service accounts, Compute Engine VMs, Cloud Storage buckets, and BigQuery datasets. When an application calls a Google Cloud API, the project that owns the application credentials is called the _client project_ , and the project that owns the target resource is called the _resource project_. Some API requests can touch multiple resources, in which case more than one resource project can be involved in the request.

If you want to stop using Google Cloud for any reasons, you can use [Google Cloud console](https://console.cloud.google.com/) to delete your project. Your project and all resources in the project will be deleted after the retention window. Note that different types of data have different retention periods.

## Discovering APIs

Before using any Google Cloud APIs, you should use the Google Cloud console [API Library](https://console.cloud.google.com/apis/library) to browse available Google Cloud APIs and discover the ones that best meet your business needs.

## Enabling APIs

Some Google Cloud APIs are enabled by default. To use a Google Cloud API that is not enabled by default, you must enable it for your project. Depending on which services and which projects are involved from your application, including the client project and resource projects, you might need to enable an API for multiple projects. When you enable an API that depends on other APIs, those APIs are also enabled at the same time.

Enabling an API requires you to accept the Terms of Service and billing responsibility for the API. You need permission `serviceusage.services.enable` on the project to enable APIs. For more information, see Service Usage [Access Control](https://docs.cloud.google.com/service-usage/docs/access-control).

In addition, the service to enable must either be public, or else the service owner must grant the user the `servicemanagement.services.bind` permission on the private service. For more information, see [Service Management Access Control](https://docs.cloud.google.com/service-infrastructure/docs/service-management/access-control).

To enable an API for a project using the console:

  1. Go to the [Google Cloud console API Library](https://console.cloud.google.com/apis/library?project=_).
  2. From the projects list, select the project you want to use.
  3. In the API Library, select the API you want to enable. If you need help finding the API, use the search field and the filters.
  4. On the API page, click **ENABLE**.



From the same page you can disable an API for your project if you no longer use it to avoid misuse and accidental billing charges. You can also enable and disable Cloud APIs using the [gcloud CLI](https://docs.cloud.google.com/sdk/docs) and the [Service Usage API](https://docs.cloud.google.com/service-usage/docs/reference/rest/v1/services/enable):
    
    
    gcloud services enable pubsub.googleapis.com
    gcloud services disable pubsub.googleapis.com
    

## Enabling billing

Some Cloud APIs charge for usage. You need to enable billing for your project before you can start using these APIs in your project. The API usage in a project is charged to the billing account associated with the project.

If you don't have a billing account, go to the [Google Cloud console billing page](https://console.cloud.google.com/billing) and follow the instructions to create one. Then [link your billing account](https://console.cloud.google.com/billing/linkedaccount?project=_) to your project.

## Authenticating to APIs

How you authenticate to an API depends on your development environment and what authentication methods the API supports.

Setting up [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) for use in a variety of environments is the most common approach, and is recommended for most applications. If the API supports [API keys](https://docs.cloud.google.com/docs/authentication/api-keys), that is another option. If your application needs to access Cloud resources owned by your end users, you [create an OAuth 2.0 Client ID and use the authentication libraries](https://developers.google.com/identity/protocols/oauth2/web-server).

For general information about authentication, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).

## Building applications

If you are building an application using Cloud APIs, we recommend that you use [Google Cloud client libraries](https://docs.cloud.google.com/apis/docs/cloud-client-libraries) if available. The client libraries can handle common API features for your convenience, such as authentication, error handling, retry, and payload validation. You need to pass your application credentials to the client libraries during initialization, so the client libraries can make calls to Google Cloud APIs on behalf of your application.

See the following step-by-step guides that use the client libraries for some popular APIs:

  * [Cloud Billing Budget API with Node.js](https://console.cloud.google.com/?tutorial=billing--budget--billing-budget-api-nodejs).
  * [Cloud Billing Budget API with Python](https://console.cloud.google.com/?tutorial=billing--budget--billing-budget-api-python).
  * [Cloud Logging with Node.js](https://console.cloud.google.com/?tutorial=logging--logging-nodejs).
  * [Cloud Logging with Python](https://console.cloud.google.com/?tutorial=logging--logging-python).
  * [Cloud Logging with Go](https://console.cloud.google.com/?tutorial=logging--logging-go).
  * [Cloud Logging with Java](https://console.cloud.google.com/?tutorial=logging--logging-java).
  * [Speech-to-Text with Node.js](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-nodejs).
  * [Speech-to-Text with Python](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-python).
  * [Speech-to-Text with Go](https://console.cloud.google.com/?tutorial=speech-to-text--speech-to-text-go).
  * [Speech-to-Text with Java](https://console.cloud.google.com/?tutorial=speech-to-text__speech-to-text-java).



For more information, see [Client Libraries Explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

## More information

  * For more information about authentication, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).


  * For more information about billing, see [Create, modify, or close your billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account).

  * For more information about enabling billing on your project, see [Modify a project's billing settings](https://docs.cloud.google.com/billing/docs/how-to/modify-project).



  * For more information about enabling and disabling APIs, see [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
