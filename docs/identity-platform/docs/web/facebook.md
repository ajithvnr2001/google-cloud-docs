---
url: https://docs.cloud.google.com/identity-platform/docs/web/facebook/
title: Signing in users with Facebook \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:16.668282+00:00
---

# Signing in users with Facebook  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/facebook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Facebook

This document shows you how to use Identity Platform to sign in users with Facebook.

## Before you begin

This tutorial assumes you've already enabled Identity Platform, and have a basic web app written using HTML and JavaScript. See the [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email) to learn how.

## Configuring Facebook as a provider

To configure Facebook as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add A Provider**.

  3. Select **Facebook** from the list.

  4. Enter your Facebook **App ID** and **App Secret**. If you don't already have an ID and secret, you can obtain one from the [Facebook for Developers](https://developers.facebook.com/apps) page.

  5. Configure the URI listed under **Configure Facebook** as a valid OAuth redirect URI for your Facebook app. If you configured a custom domain in Identity Platform, update the redirect URI in your Facebook app configuration to use the custom domain instead of the default domain. For example, change `https://myproject.firebaseapp.com/__/auth/handler` to `https://auth.myownpersonaldomain.com/__/auth/handler`. 

  6. Register your app's domains by clicking **Add Domain** under **Authorized Domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  7. Under **Configure your application** , click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




## Signing in users with the client SDK

  1. Create an instance of the Facebook provider object:

###  JavaScript 
         
         var provider = new firebase.auth.FacebookAuthProvider();
         

  2. **Optional:** Add OAuth scopes. Scopes specify what data you are requesting from Facebook. More sensitive data may require specific scopes. Consult the provider's [documentation](https://developers.facebook.com/docs/facebook-login/permissions) to determine what scopes your app needs.

###  JavaScript 
         
         provider.addScope('user_birthday');
         

  3. **Optional:** Localize the authentication flow. You can specify a language, or use the device's default language:

###  JavaScript 
         
         firebase.auth().languageCode = 'it';
         // To apply the default browser preference instead of explicitly setting it.
         // firebase.auth().useDeviceLanguage();
         

  4. **Optional:** Specify additional custom OAuth parameters. These are specific to Facebook, and are typically used to customize the authentication experience. You can't pass parameters reserved by OAuth or Identity Platform.

###  JavaScript 
         
         provider.setCustomParameters({
         'display': 'popup'
         });
         

  5. Use the Facebook provider object to sign in the user. You can either open a pop-up window, or redirect the current page. Redirecting is easier for users on mobile devices.

**Note:** Facebook requires HTTPS for production apps, and does not allow login with insecure hosts. If you're developing locally using the `http://localhost` origin, ensure your Facebook app is in development mode, and that you're signing in with a registered test account. 

To show a pop-up, call `signInWithPopup()`:

###  JavaScript 
         
         firebase
           .auth()
           .signInWithPopup(provider)
           .then((result) => {
             /** @type {firebase.auth.OAuthCredential} */
             var credential = result.credential;
         
             // The signed-in user info.
             var user = result.user;
         
             // This gives you a Facebook Access Token. You can use it to access the Facebook API.
             var accessToken = credential.accessToken;
         
             // ...
           })
           .catch((error) => {
             // Handle Errors here.
             var errorCode = error.code;
             var errorMessage = error.message;
             // The email of the user's account used.
             var email = error.email;
             // The firebase.auth.AuthCredential type that was used.
             var credential = error.credential;
         
             // ...
           });
         

To redirect the page, first call `signInWithRedirect()`.

Follow the [best practices](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`. 

###  JavaScript 
         
         firebase.auth().signInWithRedirect(provider);
         

Then, retrieve the Facebook token by calling `getRedirectResult()` when your page loads:

###  JavaScript 
         
         firebase.auth()
           .getRedirectResult()
           .then((result) => {
             if (result.credential) {
               /** @type {firebase.auth.OAuthCredential} */
               var credential = result.credential;
         
               // This gives you a Facebook Access Token. You can use it to access the Facebook API.
               var token = credential.accessToken;
               // ...
             }
             // The signed-in user info.
             var user = result.user;
           }).catch((error) => {
             // Handle Errors here.
             var errorCode = error.code;
             var errorMessage = error.message;
             // The email of the user's account used.
             var email = error.email;
             // The firebase.auth.AuthCredential type that was used.
             var credential = error.credential;
             // ...
           });
         




Once you have an access token, you can use it to call the Facebook API. For example:

### REST
    
    
    curl "https://graph.facebook.com/me?fields=id,name&access_token=[TOKEN]"

## Signing in users manually

If you don't want to use the client SDK, you can also handle the sign-in flow manually.

This sign-in method also supports Facebook Login for Gaming as an IdP. Identity Platform doesn't support [manually implementing Facebook Login for Gaming](https://developers.facebook.com/docs/games/social-and-retention/features/login-for-gaming#manually-implement-facebook-login-for-gaming). It only accepts the tokens for exchanging Identity Platform credentials.

  1. Integrate Facebook or Facebook Login for Gaming authentication into your app by following the steps in their developer documentation:

     * [Facebook developer documentation](https://developers.facebook.com/docs/facebook-login/web)
     * [Facebook Login for Gaming developer documentation](https://developers.facebook.com/docs/games/social-and-retention/features/login-for-gaming#using-facebook-sdk)
  2. Sign in the user with Facebook or Facebook Login for Gaming using the flow you implemented in the previous step.

  3. Exchange the token you receive from Facebook or Facebook Login for Gaming for an Identity Platform credential:

###  JavaScript 
         
         var credential = firebase.auth.FacebookAuthProvider.credential(accessToken);
         

  4. Use the credential to sign in the user with Identity Platform:

###  JavaScript 
         
         // Sign in with the credential from the user.
         firebase.auth()
           .signInWithCredential(credential)
           .then((result) => {
             // Signed in
             // ...
           })
           .catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.email;
             // ...
           });
         




## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
