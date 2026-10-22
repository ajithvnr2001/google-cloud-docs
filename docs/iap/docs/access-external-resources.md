---
url: https://docs.cloud.google.com/iap/docs/access-external-resources/
title: Accessing non-Google resources programmatically \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:27:59.192066+00:00
---

# Accessing non-Google resources programmatically  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/access-external-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Accessing non-Google resources programmatically Stay organized with collections  Save and categorize content based on your preferences. 

This article shows you how to programmatically access a resource protected by Identity-Aware Proxy (IAP) using external identities.

There are several situations where you might want to do this:

  * Your frontend application leverages Identity Platform directly. Your backend API server is built using App Engine, and protected by IAP using external identities.

  * Your application is designed for use in a non-traditional browser environment, such as on Android, iOS, or the command-line, where using a browser redirect to authenticate users is infeasible.




## Accessing resources

To access a resource programmatically using a service account JWT, see [Authenticating with a service account JWT](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating_with_a_service_account_jwt).

To access a resource programmatically using an ID token, follow these steps:

  1. Retrieve the user's ID token.

###  Node.js 

Ensure the user is signed in. The code below shows a simple example of signing in a user with an email and password:
         
         // If signing in using project-level email/password IdP.
         // auth.tenantId = null; // This is null by default.
         // For signing in to a specific tenant using email/password.
         auth.tenantId = 'myTenantId';
         auth.signInWithEmailAndPassword(email, password)
           .then((user) => {
             // User signed in. ID token can now be retrieved.
           })
           .catch((error) => {
             // Handler error.
           });
         

You can then retrieve an ID token on the `user` object:
         
         user.getIdToken()
           .then((idToken) => {
             // idToken is now available and can be sent to API server.
           })
           .catch((error) => {
             // Handler error.
           });
         

###  REST 

Calling `signInWithPassword` returns an ID token in the response:
         
         curl 'https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=API-KEY' \
         -H 'Content-Type: application/json' \
         --data-binary '{
           "email":"EMAIL",
           "password":"PASSWORD",
           "returnSecureToken":true,
           "tenantId":"TENANT-ID" # Only used in multi-tenancy
           }'

  2. Include the ID token in the authorization header when calling an endpoint protected by IAP.
         
         curl -H "Authorization: Bearer GCIP-ID-TOKEN" "https://example.appspot.com/api"




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
