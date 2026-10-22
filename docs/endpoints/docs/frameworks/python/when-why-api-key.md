---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/python/when-why-api-key/
title: Why and When to Use API Keys \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:25.113578+00:00
---

# Why and When to Use API Keys  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/python/when-why-api-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)



Send feedback 

#  Why and When to Use API Keys Stay organized with collections  Save and categorize content based on your preferences. 

This page provides background information on API keys and authentication: how each of these are used, the differences between them, and the scenarios where you should consider using API keys.

## API keys are for projects, authentication is for users

Cloud Endpoints handles both API keys and authentication schemes, such as Firebase or Auth0. The main distinction between these two is:

  * API keys identify the calling project — the application or site — making the call to an API.

  * Authentication tokens identify a user — the person — that is using the app or site.

![API keys overview](https://docs.cloud.google.com/static/endpoints/docs/images/api_keys_overview.png)




## API keys provide project authorization

To decide which scheme is most appropriate, it's important to understand what API keys and authentication can provide.

API keys provide

  * **Project identification** — Identify the application or the project that's making a call to this API

  * **Project authorization** — Check whether the calling application has been granted access to call the API and has enabled the API in their project




API keys aren't as secure as authentication tokens (see Security of API keys), but they identify the application or project that's calling an API. They are generated on the project making the call, and you can restrict their use to an environment such as an IP address range, or an Android or iOS app.

By identifying the calling project, you can use API keys to associate usage information with that project. API keys allow Cloud Endpoints Frameworks to reject calls from projects that haven't been granted access or enabled in the API. 

## Authentication of users

By contrast, authentication schemes typically serve two purposes:

  * **User authentication** — Securely verify that the calling user is who they claim to be.

  * **User authorization** — Check whether the user should have access to make this request.




Authentication schemes provide a secure way of identifying the calling user. Endpoints also checks the authentication token to verify that it has permission to call an API. Based on that authentication, the API server decides on authorizing a request.

If you need the ability to identify the user making the call, see [Authenticating users](https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users).

While API keys identify the calling project, they don't identify the calling user. For instance, if you have created an application that is calling an API, an API key can identify the application that is making the call, but not the identity of the person who is using the application.

If you need a more secure way to limit which projects or services can call your API, see [Authentication between services](https://docs.cloud.google.com/endpoints/docs/frameworks/python/service-account-authentication).

## Security of API keys

API keys are generally not considered secure; they are typically accessible to clients, making it easy for someone to steal an API key. Once the key is stolen, it has no expiration, so it may be used indefinitely, unless the project owner revokes or regenerates the key. While the restrictions you can set on an API key mitigate this, there are better approaches for authorization.

For examples, see [Authenticating users](https://docs.cloud.google.com/endpoints/docs/frameworks/python/authenticating-users).

## When to use API keys

An API may restrict some or all of its methods to require API keys. It makes sense to do this if:

  * You do want to block anonymous traffic. API keys identify an application's traffic for the API producer, in case the application developer needs to work with the API producer to debug an issue or show their application's usage.

  * You want to control the number of calls made to your API.

  * You want to identify usage patterns in your API's traffic. You can see application usage in [APIs & services](http://console.developers.google.com).

  * You want to filter logs by API key.




API keys cannot be used for:

  * Identifying individual users — API keys don't identify users, they identify projects.

  * Secure authorization.

  * Identifying the creators of a project.




[Service Infrastructure](https://docs.cloud.google.com/service-infrastructure/docs/overview) doesn't provide a method to directly look up projects from API keys.

## How to use API keys

To learn how to set up and use API key access, see [Restricting access with API keys](https://docs.cloud.google.com/endpoints/docs/frameworks/python/restricting-api-access-with-api-keys-frameworks). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
