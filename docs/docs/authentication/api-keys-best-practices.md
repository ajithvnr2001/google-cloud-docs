---
url: https://docs.cloud.google.com/docs/authentication/api-keys-best-practices/
title: Best practices for managing API keys \u00a0|\u00a0 Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:54.190926+00:00
---

# Best practices for managing API keys  |  Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/api-keys-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Best practices for managing API keys Stay organized with collections  Save and categorize content based on your preferences. 

When you use API keys in your applications, ensure that they are kept secure during both storage and transmission. Publicly exposing your API keys can lead to unexpected charges on your account or unauthorized access to your data. To help keep your API keys secure, implement the following best practices. 

## Add API key restrictions to your key

By adding restrictions, you can limit the ways an API key can be used, reducing the impact of a compromised API key.

For more information, see [Apply API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).

## Avoid using query parameters to provide your API key to Google APIs

Providing your API key to APIs as a query parameter includes your API key in the URL, exposing your key to theft through URL scans. Use the [`x-goog-api-key` HTTP header](https://docs.cloud.google.com/docs/authentication/api-keys-use#using-with-rest) or a [client library](https://docs.cloud.google.com/docs/authentication/api-keys-use#using-with-client-libs) instead.

## Delete unneeded API keys to minimize exposure to attacks

Retain only the API keys you are actively using to keep your attack surface as small as possible.

## Don't include API keys in client code or commit them to code repositories

API keys hardcoded in the source code or stored in a repository are open to interception or theft by bad actors. The client should pass requests to the server, which can add the credential and issue the request.

## Don't use authorization keys in production

[Authorization keys](https://docs.cloud.google.com/docs/authentication/api-keys#introduction) are designed to accelerate the initial experience for developers exploring Google Cloud APIs. For most APIs, we recommend you don't use authorization keys in production environments.

Instead, plan to migrate to more secure alternatives such as [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/grant-role-console) policies and [short-lived service account credentials](https://docs.cloud.google.com/iam/docs/service-account-creds#short-lived-credentials), following least-privilege security practices.

**Note:** The exception is using authorization keys with [Gemini API](https://ai.google.dev/api) in production, because Gemini API doesn't create resources in Google Cloud projects. When moving a Gemini API project into production, make sure that the service account the authorization key is bound to isn't granted any IAM roles.

Here's why you should migrate from using an authorization key to more secure practices as soon as possible:

  * API keys are sent alongside requests. This makes it more likely that the key might be exposed or logged.

  * API keys are bearer credentials. This means that if someone steals an authorization key, they can use it to authenticate as that service account and access the same resources that service account can.

  * Authorization keys obscure the identity of the end user in audit logs. To track the actions of individual users, make sure each user has their own set of credentials.




## Implement strong monitoring and logging

Monitoring API usage can help alert you to unauthorized usage. For more information, see [Cloud Monitoring overview](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and [Cloud Logging overview](https://docs.cloud.google.com/logging/docs/overview).

## Isolate API keys

Provide each team member with their own API key for each application. This can help control access, provide an audit trail, and reduce the impact of a compromised API key.

## Rotate your API keys periodically

Periodically create new API keys, update your applications to use the new API keys, and delete the old keys.

For more information, see [Rotate an API key](https://docs.cloud.google.com/docs/authentication/api-keys#rotate).

## Consider a more secure method of authorizing access

For help with choosing an authentication method, see [Authentication methods](https://docs.cloud.google.com/docs/authentication). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
