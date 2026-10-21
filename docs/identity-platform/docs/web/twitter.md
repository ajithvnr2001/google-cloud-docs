---
url: https://docs.cloud.google.com/identity-platform/docs/web/twitter/
title: Sign in users with Twitter \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:17.729479+00:00
---

# Sign in users with Twitter  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/twitter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Sign in users with Twitter

This document shows you how to use Identity Platform to sign in users with Twitter. 

## Before you begin

This tutorial assumes you've already enabled Identity Platform, and have a basic web app written using HTML and JavaScript. To learn about how to enable Identity Platform and sign in, see [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email). 

## Configure Twitter as a provider

To configure Twitter as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console. 

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add A Provider**.
  3. Select **Twitter** from the list.
  4. Enter your Twitter **App ID** and **App Secret**. If you don't already have an ID and secret, you can obtain one from the [ Twitter Apps](https://apps.twitter.com/) page. 
  5. Configure the URI listed under **Configure Twitter** as a valid OAuth redirect URI for your Twitter app. If you configured a custom domain in Identity Platform, update the redirect URI in your Twitter app configuration to use the custom domain instead of the default domain. For example, change `https://myproject.firebaseapp.com/__/auth/handler` to `https://auth.myownpersonaldomain.com/__/auth/handler`. 
  6. In the **Project settings** side pane, click **Add Domain** , and add your app's domain. 

We recommend that you don't include `localhost` in your production projects.

**note:** For projects that are created before April 28, 2025, `localhost` is enabled by default. 
  7. In the **Configure your application** section, click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK. 
  8. Click **Save**.



## Sign in users with the client SDK

  1. Create an instance of the Twitter provider object: 

### Web version 9
         
         import { TwitterAuthProvider } from "firebase/auth";
         
         const provider = new TwitterAuthProvider();
         
         [auth_twitter_provider_create.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/twitter/auth_twitter_provider_create.js#L8-L10)

### Web version 8
         
         var provider = new firebase.auth.TwitterAuthProvider();
         
         [twitter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/twitter.js#L9-L9)

  2. **Optional:** Localize the authentication flow. You can specify a language, or use the device's default language: 

### Web version 9
         
         import { getAuth } from "firebase/auth";
         
         const auth = getAuth();
         auth.languageCode = 'it';
         // To apply the default browser preference instead of explicitly setting it.
         // auth.useDeviceLanguage();
         
         [auth_set_language_code.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_set_language_code.js#L8-L13)

### Web version 8
         
         firebase.auth().languageCode = 'it';
         // To apply the default browser preference instead of explicitly setting it.
         // firebase.auth().useDeviceLanguage();
         
         [index.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/index.js#L73-L75)

  3. **Optional:** Specify additional custom OAuth parameters. These are specific to Twitter, and are typically used to customize the authentication experience. You can't pass parameters reserved by OAuth or Identity Platform. 

### Web version 9
         
         provider.setCustomParameters({
           'lang': 'es'
         });
         
         [auth_twitter_provider_params.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/twitter/auth_twitter_provider_params.js#L8-L10)

### Web version 8
         
         provider.setCustomParameters({
           'lang': 'es'
         });
         
         [twitter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/twitter.js#L13-L15)

  4. Use the Twitter provider object to sign in the user. You can either open a pop-up window, or redirect the current page. Redirecting is easier for users on mobile devices. 

To show a pop-up, call `signInWithPopup()`:

### Web version 9
         
         import { getAuth, signInWithPopup, TwitterAuthProvider } from "firebase/auth";
         
         const auth = getAuth();
         signInWithPopup(auth, provider)
           .then((result) => {
             // This gives you a the Twitter OAuth 1.0 Access Token and Secret.
             // You can use these server side with your app's credentials to access the Twitter API.
             const credential = TwitterAuthProvider.credentialFromResult(result);
             const token = credential.accessToken;
             const secret = credential.secret;
         
             // The signed-in user info.
             const user = result.user;
             // IdP data available using getAdditionalUserInfo(result)
             // ...
           }).catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The AuthCredential type that was used.
             const credential = TwitterAuthProvider.credentialFromError(error);
             // ...
           });
         
         [auth_twitter_signin_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/twitter/auth_twitter_signin_popup.js#L8-L32)

### Web version 8
         
         firebase
           .auth()
           .signInWithPopup(provider)
           .then((result) => {
             /** @type {firebase.auth.OAuthCredential} */
             var credential = result.credential;
         
             // This gives you a the Twitter OAuth 1.0 Access Token and Secret.
             // You can use these server side with your app's credentials to access the Twitter API.
             var token = credential.accessToken;
             var secret = credential.secret;
         
             // The signed-in user info.
             var user = result.user;
             // IdP data available in result.additionalUserInfo.profile.
               // ...
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
         
         [twitter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/twitter.js#L21-L46)

To redirect the page, first call `signInWithRedirect()`.

Follow the [best practices](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`. 

### Web version 9
         
         import { getAuth, signInWithRedirect } from "firebase/auth";
         
         const auth = getAuth();
         signInWithRedirect(auth, provider);
         
         [auth_signin_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_signin_redirect.js#L8-L11)

### Web version 8
         
         firebase.auth().signInWithRedirect(provider);
         
         [index.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/index.js#L101-L101)

Then, retrieve the Twitter token by calling `getRedirectResult()` when your page loads: 

### Web version 9
         
         import { getAuth, getRedirectResult, TwitterAuthProvider } from "firebase/auth";
         
         const auth = getAuth();
         getRedirectResult(auth)
           .then((result) => {
             // This gives you a the Twitter OAuth 1.0 Access Token and Secret.
             // You can use these server side with your app's credentials to access the Twitter API.
             const credential = TwitterAuthProvider.credentialFromResult(result);
             const token = credential.accessToken;
             const secret = credential.secret;
             // ...
         
             // The signed-in user info.
             const user = result.user;
             // IdP data available using getAdditionalUserInfo(result)
             // ...
           }).catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The AuthCredential type that was used.
             const credential = TwitterAuthProvider.credentialFromError(error);
             // ...
           });
         
         [auth_twitter_signin_redirect_result.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/twitter/auth_twitter_signin_redirect_result.js#L8-L33)

### Web version 8
         
         firebase.auth()
           .getRedirectResult()
           .then((result) => {
             if (result.credential) {
               /** @type {firebase.auth.OAuthCredential} */
               var credential = result.credential;
         
               // This gives you a the Twitter OAuth 1.0 Access Token and Secret.
               // You can use these server side with your app's credentials to access the Twitter API.
               var token = credential.accessToken;
               var secret = credential.secret;
               // ...
             }
         
             // The signed-in user info.
             var user = result.user;
             // IdP data available in result.additionalUserInfo.profile.
               // ...
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
         
         [twitter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/twitter.js#L52-L79)




After you have an access token, you can use it to call the Twitter API. For example: 

### REST
    
    
    curl --request POST
      --url 'https://api.twitter.com/1.1/statuses/update.json?status=Hello%20world'
      --header 'authorization: OAuth oauth_consumer_key="CONSUMER_API_KEY",
      oauth_nonce="OAUTH_NONCE", oauth_signature="OAUTH_SIGNATURE",
      oauth_signature_method="HMAC-SHA1", oauth_timestamp="OAUTH_TIMESTAMP",
      oauth_token="ACCESS_TOKEN", oauth_version="1.0"'

## Sign in users manually

If you don't want to use the client SDK, you can also handle the sign-in flow manually: 

  1. Integrate Twitter authentication into your app by following the steps in their [developer documentation](https://developer.twitter.com/en/docs/basics/authentication/guides/log-in-with-twitter). 
  2. Sign in the user with Twitter using the flow you implemented in the previous step. 
  3. Exchange the token you receive from Twitter for an Identity Platform credential: 

### Web version 9
         
         import { TwitterAuthProvider } from "firebase/auth";
         
         const credential = TwitterAuthProvider.credential(accessToken, secret);
         
         [auth_twitter_provider_credential.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/twitter/auth_twitter_provider_credential.js#L8-L10)

### Web version 8
         
         var credential = firebase.auth.TwitterAuthProvider.credential(accessToken, secret);
         
         [twitter.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/twitter.js#L85-L85)

  4. Use the credential to sign in the user with Identity Platform: 

### Web version 9
         
         import { getAuth, signInWithCredential } from "firebase/auth";
         
         // Sign in with the credential from the user.
         const auth = getAuth();
         signInWithCredential(auth, credential)
           .then((result) => {
             // Signed in 
             // ...
           })
           .catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // ...
           });
         
         [auth_signin_credential.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_signin_credential.js#L8-L24)

### Web version 8
         
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
         
         [index.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/index.js#L81-L95)




## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users). 
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
