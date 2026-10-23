---
url: https://docs.cloud.google.com/run/docs/authenticating/end-users/
title: Authenticating users \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:50.125142+00:00
---

# Authenticating users  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/authenticating/end-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Authenticating users Stay organized with collections  Save and categorize content based on your preferences. 

If your application handles requests from users, it's a best practice to restrict access to only the allowed users. Users do not typically have IAM permission on your Google Cloud project or Cloud Run service.

We distinguish two types of users:

  * **End users**: Users of your application who do not necessarily belong to your organization. They typically need to register an account for themselves.
  * **Internal users**: Users who are explicitly granted access to your application by an administrator in your organization. They typically belong to your organization.

**Note:** Cloud Run does not assist in the sharing of sessions between instances and does not guarantee session affinity to a specific instance.

## Authenticating end users

If you want to authenticate users using email/password, phone number, social providers like Google, Facebook or GitHub, or a custom authentication mechanism, you can use [Identity Platform](https://docs.cloud.google.com/identity-platform/docs). Using [Firebase Authentication](https://firebase.google.com/docs/auth) is similar to using Identity Platform.

You need a public web or mobile app that handles the sign-in flow and then makes authenticated API calls to a Cloud Run service. This public web app can itself be hosted on a [public Cloud Run service](https://docs.cloud.google.com/run/docs/authenticating/public).

For a complete tutorial on using Identity Platform for end user authentication, refer to the [End user authentication for Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/identity-platform) tutorial.

  1. Add code to your Cloud Run service to [verify ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens#verify_id_tokens_using_the_firebase_admin_sdk).

  2. [Deploy your Cloud Run service publicly](https://docs.cloud.google.com/run/docs/authenticating/public).

  3. [Set up Identity Platform in your project](https://docs.cloud.google.com/identity-platform/docs/how-to)

  4. Do the following in your web or mobile app:

     1. Use the appropriate Firebase Auth client library to get an ID token: 
        * **Android** : Use the [`GetTokenResult().getToken()`](https://firebase.google.com/docs/reference/android/com/google/firebase/auth/GetTokenResult) method.
        * **iOS** : Use the [`User.getIDTokenResult(completion:)`](https://firebase.google.com/docs/reference/swift/firebaseauth/api/reference/Classes/User#getidtokenresultcompletion) method.
        * **Web** : Use the [`firebase.User.getIdToken()`](https://firebase.google.com/docs/reference/js/auth.user.md#usergetidtoken) method.
     2. Include the ID token in an `Authorization: Bearer ID_TOKEN` header in the request to the service.



You can use any of the following methods to access user profile information:

  * Use the Firebase Admin SDK to make a network request to [retrieve user data](https://firebase.google.com/docs/auth/admin/manage-users#retrieve_user_data).
  * Use a [Google API Client Library](https://developers.google.com/identity/sign-in/web/backend-auth#using-a-google-api-client-library) to retrieve user data using the method best suited for your chosen runtime.



For an end-to-end walkthrough of an application using this authentication technique, follow the [end user authentication for Cloud Run tutorial](https://docs.cloud.google.com/run/docs/tutorials/identity-platform).

## Authenticating internal users

For internal user authentication, use [Identity-Aware Proxy](https://docs.cloud.google.com/iap).

To set up Identity-Aware Proxy for a Cloud Run service, see [Configure Identity-Aware Proxy for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run).

For preflighted [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) requests with authenticated Cloud Run services, we recommend that you [Configure IAP for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) instead of using IAM authentication. This lets you configure IAP to [allow unauthenticated OPTIONS requests](https://docs.cloud.google.com/iap/docs/customizing#allowing_http_options_requests_cors_preflight), which satisfies the browser's preflight check while ensuring that all other requests are authenticated.

Even when IAP allows the OPTIONS request, the application code you deploy to Cloud Run must still handle the CORS preflight request and the actual request that follows by sending the appropriate CORS headers.

To learn how to authenticate users or service accounts to an Identity-Aware Proxy-secured Cloud Run service using OAuth 2.0, refer to the documentation for [Programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
