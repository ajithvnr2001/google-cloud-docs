---
url: https://docs.cloud.google.com/iap/docs/identity-howto/
title: Getting the user's identity \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:24.732874+00:00
---

# Getting the user's identity  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/identity-howto/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Getting the user's identity Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to get a user's identity with Identity-Aware Proxy (IAP). Getting the user's identity enables your application to verify that a request came through IAP. To properly secure your app, you must always use one of the following mechanisms to get the IAP-authenticated user identity.

## Getting the user's identity with signed headers

To make sure a request to your Compute Engine, GKE, Cloud Run, App Engine standard environment, or App Engine flexible environment app was authorized by IAP, your app must validate every request by checking the `x-goog-iap-jwt-assertion` HTTP request header. Learn about [securing your app with signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto). 

IAP also passes the user's identity to your backend service in the following HTTP headers. These headers should have the namespace prefix `accounts.google.com`. These headers are available for compatibility, but you shouldn't rely on them as a security mechanism. If you use these headers, you must compare them against the identity information from the authenticated JWT header listed above.

Header name | Description | Example value  
---|---|---  
`X-Goog-Authenticated-User-Email` | The user's email address |  `accounts.google.com:example@example.com`  
`X-Goog-Authenticated-User-Id` | A persistent, unique identifier for the user. |  `accounts.google.com:userIDvalue`  
  
## Getting the user's identity with the App Engine standard environment Users API

Alternatively, if you have an App Engine standard environment app, the [Users API](https://docs.cloud.google.com/appengine/docs/standard/python/users) can be used to get the user's identity in your app code.

If your application already uses this API, you don't need to change anything. IAP provides the user's identity, but the value for each user's Users API user ID will change when IAP is turned on.

To get the IAP-verified user identity for a request, call the Users API to return the current user. If the function returns a user, such as `req.getUserPrincipal() != null` in Java, the user was authenticated by IAP.

## Consent screen

When IAP is enabled, the first time a user accesses your app, they're redirected to a consent screen to confirm that they want to share their identity with your app. This occurs even if the user granted consent to this app before you enabled IAP, and will occur again if you disable IAP and then re-enable it.

If you're using the Users API, it normally suppresses the consent screen for apps and users that are within the same Google Workspace domain. When you enable IAP, the consent screen isn't automatically suppressed. To suppress the consent screen with IAP enabled, follow these steps:

  1. Go to your [Google Admin console](https://admin.google.com/).

[Go to the Admin console](https://admin.google.com/)

  2. On the list of controls, select **Security**.

     1. If you don't see **Security** listed, select **More controls** from the gray bar at the bottom of the page, then select **Security** from the list of controls.

     2. If you can't see the controls, make sure you're signed in as an administrator for the domain.

  3. On the list of options, select **Access and data control** and then **API Controls**.

  4. In the **Authentication** section, select **Manage API client access**.

  5. In the **Client Name** field, enter the IAP OAuth 2.0 client ID. You can find the IAP client ID on the [Credentials page](https://console.cloud.google.com/apis/credentials).

[Go to the IAP credentials page](https://console.cloud.google.com/apis/credentials)

  6. In the **One or More API Scopes** field, enter `email, openid`.

  7. Click **Authorize**.




To simplify this process, you can use an [API call](https://docs.cloud.google.com/iap/docs/reference/compute-engine-apis) to use a single IAP OAuth 2.0 client ID for all apps. You can't use the Google Cloud console to specify the client ID to use with IAP. 

## What's next

  * Learn more about [Identity and Access Management](https://docs.cloud.google.com/iam/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
