---
url: https://docs.cloud.google.com/resource-manager/docs/authorizing/
title: Authorize requests \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:41.489776+00:00
---

# Authorize requests  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/authorizing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Authorize requests Stay organized with collections  Save and categorize content based on your preferences. 

When your application requests private data, the request must be authorized by an authenticated user who has access to that data.

When your application requests public data, the request doesn't need to be authorized, but does need to be accompanied by an identifier, such as an API key.

Every request your application sends to the Cloud Resource Manager API needs to identify your application to Google. There are two ways to identify your application: using an OAuth 2.0 token (which also authorizes the request) and/or using the application's API key. Here's how to determine which of those options to use:

  * If the request requires authorization (such as a request for an individual's private data), then the application must provide an OAuth 2.0 token with the request. The application may also provide the API key, but it doesn't have to.
  * If the request doesn't require authorization (such as a request for public data), then the application must provide either the API key or an OAuth 2.0 token, or both—whatever option is most convenient for you.



## About authorization protocols

Your application must use [OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2) to authorize requests. No other authorization protocols are supported. If your application uses [Sign In With Google](https://developers.google.com/identity/gsi/web), some aspects of authorization are handled for you.

## Authorizing requests with OAuth 2.0

Requests to the Cloud Resource Manager API for non-public user data must be authorized by an authenticated user.

The details of the authorization process, or "flow," for OAuth 2.0 vary somewhat depending on what kind of application you're writing. The following general process applies to all application types:

  1. When you create your application, you register it using the [Google Cloud console](https://console.cloud.google.com/). Google then provides information you'll need later, such as a client ID and a client secret.
  2. Activate the Cloud Resource Manager API in the Google Cloud console. (If the API isn't listed in the Google Cloud console, then skip this step.)
  3. When your application needs access to user data, it asks Google for a particular **scope** of access.
  4. Google displays a **consent screen** to the user, asking them to authorize your application to request some of their data.
  5. If the user approves, then Google gives your application a short-lived **access token**.
  6. Your application requests user data, attaching the access token to the request.
  7. If Google determines that your request and the token are valid, it returns the requested data.



Some flows include additional steps, such as using **refresh tokens** to acquire new access tokens. For detailed information about flows for various types of applications, see Google's [OAuth 2.0 documentation](https://developers.google.com/identity/protocols/OAuth2).

Here's the OAuth 2.0 scope information for the Cloud Resource Manager API:

Scope | Meaning  
---|---  
`https://www.googleapis.com/auth/cloud-platform` | Read/write access.  
  
To request access using OAuth 2.0, your application needs the scope information, as well as information that Google supplies when you register your application (such as the client ID and the client secret).

**Tip:** The Google APIs client libraries can handle some of the authorization process for you. They are available for a variety of programming languages; check the [page with libraries and samples](https://docs.cloud.google.com/resource-manager/docs/libraries) for more details.

##  Acquiring and using an API key 

Requests to the Cloud Resource Manager API for public data must be accompanied by an identifier, which can be an [API key](https://developers.google.com/console/help/generating-dev-keys) or an [access token](https://developers.google.com/accounts/docs/OAuth2).

To acquire an API key:

  1. Open the [Credentials page](https://console.cloud.google.com/apis/credentials) in the Google Cloud console.
  2. This API supports two types of credentials. Create whichever credentials are appropriate for your project: 
     * **OAuth 2.0:** Whenever your application requests private user data, it must send an OAuth 2.0 token along with the request. Your application first sends a client ID and, possibly, a client secret to obtain a token. You can generate OAuth 2.0 credentials for web applications, service accounts, or installed applications.

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
