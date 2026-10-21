---
url: https://docs.cloud.google.com/apis/docs/client-libraries-best-practices/
title: Client libraries best practices \u00a0|\u00a0 Google Cloud SDK \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:37:09.528702+00:00
---

# Client libraries best practices  |  Google Cloud SDK  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/client-libraries-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Client libraries best practices Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some best practices when using the _Cloud Client Libraries_ and the _Google API Client Libraries_ , which help you optimize performance and maintain reliable production builds.

## Reuse client objects and sessions

When making requests with the same library, you should reuse the same client object for many requests when possible, instead of creating a new one for every request. Requests from the same instance will share authentication credential instances.

The initial request made by an instance of a session client performs authentication, authorization, and access token generation. This processing can take multiple seconds, as it happens over the network. For additional calls on the same client instance, the session client reuses the same access token for as long as it is valid (typically one hour). After it expires, the session client refreshes the access token automatically, For optimal performance, you should reuse the same session client instance for all requests made by your application, and allow the client to refresh the access token as needed for all requests needing to run under the same set of credentials.

In addition, some authentication strategies used by the client libraries have rate limits associated with them. Since each instance of the client has its own credential cache, creating too many in a small period of time may incur rate limiting causing library requests to fail authentication.

## Pin dependencies for production

When installing the libraries from a package manager such as `npm` or `pip` it is important to pin the versions using their built-in versioning for production usage. This ensures builds will consistently use the same versions of these libraries. This is especially important if you opt to use beta clients which can have their API surface change. The documentation for the relevant library notes this on the library package documentation.

## Stay up to date

As Google Cloud's capabilities and APIs change, so do the client libraries. Client libraries change often with many of them seeing daily updates and releases. In order to get the best possible support experience possible, you should stay up to date with the releases. Many of the libraries support semantic versioning to make it easy to determine how much work an upgrade will be. If you are experiencing a degraded performance (or an issue) and you are using an older version of a client library, consider upgrading it to take advantage of all improvements in newer versions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
