---
url: https://docs.cloud.google.com/iap/docs/manage-iap-wif-sessions/
title: Manage IAP with Workforce Identity Federation sessions \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:52.680664+00:00
---

# Manage IAP with Workforce Identity Federation sessions  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/manage-iap-wif-sessions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Manage IAP with Workforce Identity Federation sessions Stay organized with collections  Save and categorize content based on your preferences. 

This page provides guidance for managing Identity-Aware Proxy (IAP) with Workforce Identity Federation sessions.

When you set up a workforce pool, you can specify the session duration between Google Cloud and an IdP. You can specify the session duration to be between 15 minutes and 12 hours. This setting is also the length of the IAP session cookie. The default session duration time is one hour.

When a session expires, the end user is redirected to third-party IdP to sign in. If the third-party IdP session is still active, sign-in is silent.

For more information about setting the session duration time, see [Manage workforce identity pool providers](https://docs.cloud.google.com/iam/docs/manage-workforce-identity-pools-providers).

## Establish a session using an AJAX request

When working with Workforce Identity Federation, you can also make AJAX requests to establish a session.

IAP relies on cookies to manage user sessions and a sequence of redirects to establish a session during sign-in. If your application uses Cross-Origin Resource Sharing (CORS) to make AJAX requests from a source domain to a target domain that hosts an IAP-secured application, you must first establish an IAP session on the target domain out of band. Cookies can't be shared between the source domain and the target domain.

After a session is established on the target domain, configure your requests to include credentials because JavaScript methods don't attach cookies by default:

  * For [`XMLHttpRequest`](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest/withCredentials) objects, set the `withCredentials` property to `true`.
  * For the [`Fetch API`](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch#Sending_a_request_with_credentials_included), set the `credentials` option to `include` or `same-origin`.



For expired or unauthenticated AJAX requests, IAP returns an HTTP `401: Unauthorized` status code. If your AJAX requests receive a `302` status code instead of `401`, add an `X-Requested-With` header with a value of `"XMLHttpRequest"` to indicate that the request originates from JavaScript. To establish or refresh the session after receiving an HTTP `401` response, open a new window for the target domain URL with `?gcp-iap-mode=DO_SESSION_REFRESH` appended.

For more information and code samples, see [AJAX requests](https://docs.cloud.google.com/iap/docs/sessions-howto#ajax-requests). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
