---
url: https://docs.cloud.google.com/looker/docs/api-overview/
title: Looker API overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:12:40.231348+00:00
---

# Looker API overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/api-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Looker API overview Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** As of Looker 22.4, the [Looker API 4.0 is generally available](https://docs.cloud.google.com/looker/docs/api-4-ga). The API 3.1 is deprecated.

Looker's API provides access to the vast majority of Looker functionality over a convenient JSON-oriented REST API. It includes a diversity of endpoints, from running of queries in a variety of formats, to managing users, content, schedules, instance configurations, and more.

The API can be used as a part of many use cases. Some examples include internal operational tools, highly custom customer-facing embedded analytics, mobile app integrations, specialized Looker administrative tools, and more.

## Using the API

You can use the API either directly using HTTPS requests or through the convenience of a language-specific SDK.

In addition, the API provides for a few authentication modes, which may help inform your architectural choices. Backend services can authenticate with API credentials, can use the API with a service account, and can conveniently impersonate API requests on behalf of end users. Alternatively, frontend clients can leverage [OAuth authentication (Authorization Code PKCE)](https://oauth.net/2/pkce/), without the need to handle sensitive client secrets.

Here is a sample of the most common ways that the API is used end-to-end:

  * Backend only 
    * Authenticate with [API credentials](https://docs.cloud.google.com/looker/docs/api-auth): Common for command-line scripts, administrative tasks, or sandbox environments
  * Frontend and backend 
    * Provide an application server with single service account and credentials, and make API calls through the service account
    * Provide an application server with single service account and credentials, but use Looker's `sudo` or `login_as_user` functionality to make calls on behalf of the end user
    * Authenticate with an application server, use sudo/login_as_user, send the resulting token back to the user, and make frontend API calls with [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS)
  * Frontend only 
    * Authenticate with [OAuth](https://docs.cloud.google.com/looker/docs/api-cors), and make frontend API calls with CORS
    * Implicit authentication and invocation from within Looker extensions



## Try it out

Want to see the API in action before writing any code? You can explore API endpoints and make sample API calls against your Looker instance using the [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
