---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/how-tos/authorizing/
title: Authorize requests \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:19.883264+00:00
---

# Authorize requests  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/how-tos/authorizing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Authorize requests Stay organized with collections  Save and categorize content based on your preferences. 

Your application needs to identify itself every time it sends a request to the Cloud SQL Admin API, by including an [API key](https://cloud.google.com/docs/authentication/api-keys) with each request.

##  Acquiring and using an API key 

To acquire an API key:

  1. Open the [Credentials page](https://console.cloud.google.com/apis/credentials) in the Google Cloud console.
  2. This API supports two types of credentials. Create whichever credentials are appropriate for your project: 
     * **OAuth 2.0:** Whenever your application requests private user data, it must send an OAuth 2.0 token along with the request. Your application first sends a client ID and, possibly, a client secret to obtain a token. You can generate OAuth 2.0 credentials for web applications, service accounts, or installed applications.

**Note:** Since this API doesn't have any methods that require OAuth 2.0 authorization, you might only need to obtain API keys, which are described below. However, if your application calls other APIs that require user authorization, then you still need OAuth 2.0 credentials.

For more information, see the [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).

     * **API keys:** A request that does not provide an OAuth 2.0 token must send an API key. The key identifies your project and provides API access, quota, and reports.

The API supports several types of restrictions on API keys. If the API key that you need doesn't already exist, then create an API key in the Console by clicking **[Create credentials](https://console.cloud.google.com/apis/credentials) > API key**. You can restrict the key before using it in production by clicking **Restrict key** and selecting one of the **Restrictions**.




To keep your API keys secure, follow the [best practices for securely using API keys](https://cloud.google.com/docs/authentication/api-keys).

After you have an API key, your application can append the query parameter `key=yourAPIKey` to all request URLs.

The API key is safe for embedding in URLs; it doesn't need any encoding.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
