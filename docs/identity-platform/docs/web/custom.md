---
url: https://docs.cloud.google.com/identity-platform/docs/web/custom/
title: Signing in users with a custom authentication system \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:57.408669+00:00
---

# Signing in users with a custom authentication system  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/custom/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Signing in users with a custom authentication system 

This document shows you how to use Identity Platform to sign in users with a custom authentication system. In custom authentication, you use an authentication server to produce custom signed tokens when a user successfully signs in. Your app receives this token and uses it to authenticate with Identity Platform.

**Note:** If your app uses a sign-in method that Identity Platform supports (such as email and password), consider [migrating users](https://docs.cloud.google.com/identity-platform/docs/migrating-users) instead of implementing custom authentication.

## Before you begin

  * [Install the client SDK](https://docs.cloud.google.com/identity-platform/docs/quickstart-email-password).

  * Configure your server to accept user credentials and [mint custom tokens](https://docs.cloud.google.com/identity-platform/docs/admin/create-custom-tokens).




## Signing in users

  1. Collect sign-in credentials from the user.

  2. Send the credentials to your server. Your server validates the request, and returns a custom JWT.

  3. Pass the JWT to [`signInWithCustomToken()`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/accounts/signInWithCustomToken) to authenticate the user with Identity Platform:

### Web version 9
         
         import { getAuth, signInWithCustomToken } from "firebase/auth";
         
         const auth = getAuth();
         signInWithCustomToken(auth, token)
           .then((userCredential) => {
             // Signed in
             const user = userCredential.user;
             // ...
           })
           .catch((error) => {
             const errorCode = error.code;
             const errorMessage = error.message;
             // ...
           });
         
         [auth_sign_in_custom.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/custom/auth_sign_in_custom.js#L8-L21)

### Web version 8
         
         firebase.auth().signInWithCustomToken(token)
           .then((userCredential) => {
             // Signed in
             var user = userCredential.user;
             // ...
           })
           .catch((error) => {
             var errorCode = error.code;
             var errorMessage = error.message;
             // ...
           });
         
         [custom.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/custom.js#L10-L20)




# What's next

  * [Configure custom claims](https://docs.cloud.google.com/identity-platform/docs/how-to-configure-custom-claims) on users.
  * [Use the REST API](https://docs.cloud.google.com/identity-platform/docs/use-rest-api) to integrate Identity Platform with other parts of your custom authentication system.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
