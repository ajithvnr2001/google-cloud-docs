---
url: https://docs.cloud.google.com/identity-platform/docs/web/apple/
title: Signing in users with Apple \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:03.862826+00:00
---

# Signing in users with Apple  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/apple/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Apple

This document shows you how to use Identity Platform to add _Sign in with Apple_ to your web app.

## Before you begin

  * Enable Identity Platform and have a basic web app written using HTML and JavaScript. To learn about how to enable Identity Platform and sign in, see [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email).

  * Join the [Apple Developer Program](https://developer.apple.com/programs).




## Configuring your app with Apple

On the Apple Developer site:

  1. Follow the steps in [Configure Sign in with Apple for the web](https://developer.apple.com/help/account/configure-app-capabilities/configure-sign-in-with-apple-for-the-web). This includes:

     1. Registering a _Return URL_ , which looks like:
            
            https://project-id.firebaseapp.com/__/auth/handler
            

     2. Temporarily hosting a file at the following URL to verify your domain:
            
            https://project-id.firebaseapp.com/.well-known/apple-developer-domain-association.txt
            

Additionally, take note of your _Services ID_ and _Apple team ID_ — you'll need them in the next section.

  2. [Use an Apple private key to create a sign in](https://developer.apple.com/help/account/configure-app-capabilities/create-a-sign-in-with-apple-private-key). You'll need the _key_ and its _ID_ in the next section.

  3. If you use Identity Platform to send emails to your users, [configure your project with Apple's private email relay service](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service) using the following email:
         
         noreply@project-id.firebaseapp.com
         

You can also use a custom email template, if your app has one.




## Complying with Apple's anonymized data requirements

Apple gives users the option of anonymizing their data, including their email address. Apple assigns users who select this option an obfuscated email address with the domain `privaterelay.appleid.com`.

Your app must comply with any applicable developer policies or terms from Apple regarding anonymized Apple IDs. This includes obtaining user consent before associating any personally identifying information (PII) with an anonymized Apple ID. Actions that involve PII include, but are not limited to:

  * Linking an email address to an anonymized Apple ID, or vice versa.
  * Linking a phone number to an anonymized Apple ID, or vice versa
  * Linking a non-anonymous social credential, such as Facebook or Google, to to anonymized Apple ID, or vice versa.



For more information, refer to the _Apple Developer Program License Agreement_ for your Apple developer account.

## Configuring Apple as a provider

To configure Apple as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add A Provider**.

  3. Select **Apple** from the list.

  4. Under **Platform** , select **Web**.

  5. Enter your **Services ID** , **Apple team ID** , **Key ID** , and **private key**.

  6. Register your app's domains by clicking **Add Domain** under **Authorized Domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  7. Under **Configure your application** , click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




## Signing in users with the client SDK

To sign in a user:

  1. Create an instance of the `OAuthProvider` provider object, using the ID `apple.com`:

### Web version 9
         
         import { OAuthProvider } from "firebase/auth";
         
         const provider = new OAuthProvider('apple.com');
         
         [auth_apple_provider_create.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_provider_create.js#L8-L10)

### Web version 8
         
         var provider = new firebase.auth.OAuthProvider('apple.com');
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L11-L11)

  2. **Optional:** Add OAuth scopes. Scopes specify what data you are requesting from Apple. More sensitive data may require specific scopes. By default, when **One account per email address** is enabled, Identity Platform requests the `email` and `name` scopes.

### Web version 9
         
         provider.addScope('email');
         provider.addScope('name');
         
         [auth_apple_provider_scopes.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_provider_scopes.js#L8-L9)

### Web version 8
         
         provider.addScope('email');
         provider.addScope('name');
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L15-L16)

  3. **Optional:** Localize the authentication flow. You can specify a language, or use the device's default language. See the [Sign In with Apple docs](https://developer.apple.com/documentation/signinwithapplejs/incorporating_sign_in_with_apple_into_other_platforms#3332112) for the supported locales.

### Web version 9
         
         provider.setCustomParameters({
           // Localize the Apple authentication screen in French.
           locale: 'fr'
         });
         
         [auth_apple_provider_params.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_provider_params.js#L8-L11)

### Web version 8
         
         provider.setCustomParameters({
           // Localize the Apple authentication screen in French.
           locale: 'fr'
         });
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L20-L23)

  4. Use the provider object to sign in the user. You can either open a pop-up window, or redirect the current page. Redirecting is easier for users on mobile devices.

To show a pop-up, call `signInWithPopup()`:

### Web version 9
         
         import { getAuth, signInWithPopup, OAuthProvider } from "firebase/auth";
         
         const auth = getAuth();
         signInWithPopup(auth, provider)
           .then((result) => {
             // The signed-in user info.
             const user = result.user;
         
             // Apple credential
             const credential = OAuthProvider.credentialFromResult(result);
             const accessToken = credential.accessToken;
             const idToken = credential.idToken;
         
             // IdP data available using getAdditionalUserInfo(result)
             // ...
           })
           .catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The credential that was used.
             const credential = OAuthProvider.credentialFromError(error);
         
             // ...
           });
         
         [auth_apple_signin_popup.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_signin_popup.js#L8-L34)

### Web version 8
         
         firebase
           .auth()
           .signInWithPopup(provider)
           .then((result) => {
             /** @type {firebase.auth.OAuthCredential} */
             var credential = result.credential;
         
             // The signed-in user info.
             var user = result.user;
         
             // You can also get the Apple OAuth Access and ID Tokens.
             var accessToken = credential.accessToken;
             var idToken = credential.idToken;
         
             // IdP data available using getAdditionalUserInfo(result)
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
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L29-L56)

To redirect the page, first call `signInWithRedirect()`:

Follow the [best practices](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`. 

### Web version 9
         
         import { getAuth, signInWithRedirect } from "firebase/auth";
         
         const auth = getAuth();
         signInWithRedirect(auth, provider);
         
         [auth_apple_signin_redirect.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_signin_redirect.js#L8-L11)

### Web version 8
         
         firebase.auth().signInWithRedirect(provider);
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L62-L62)

Then, call `getRedirectResult()` to retrieve the Apple token when your page loads:

### Web version 9
         
         import { getAuth, getRedirectResult, OAuthProvider } from "firebase/auth";
         
         // Result from Redirect auth flow.
         const auth = getAuth();
         getRedirectResult(auth)
           .then((result) => {
             const credential = OAuthProvider.credentialFromResult(result);
             if (credential) {
               // You can also get the Apple OAuth Access and ID Tokens.
               const accessToken = credential.accessToken;
               const idToken = credential.idToken;
             }
             // The signed-in user info.
             const user = result.user;
           })
           .catch((error) => {
             // Handle Errors here.
             const errorCode = error.code;
             const errorMessage = error.message;
             // The email of the user's account used.
             const email = error.customData.email;
             // The credential that was used.
             const credential = OAuthProvider.credentialFromError(error);
         
             // ...
           });
         
         [auth_apple_signin_redirect_result.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/apple/auth_apple_signin_redirect_result.js#L8-L33)

### Web version 8
         
         // Result from Redirect auth flow.
         firebase
           .auth()
           .getRedirectResult()
           .then((result) => {
             if (result.credential) {
               /** @type {firebase.auth.OAuthCredential} */
               var credential = result.credential;
         
               // You can get the Apple OAuth Access and ID Tokens.
               var accessToken = credential.accessToken;
               var idToken = credential.idToken;
         
               // IdP data available in result.additionalUserInfo.profile.
               // ...
             }
             // The signed-in user info.
             var user = result.user;
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
         
         [apple.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/apple.js#L68-L97)

This is also where you can catch and handle errors. For a list of error codes, see the [API reference](https://firebase.google.com/docs/reference/js/auth#autherrorcodes).




Unlike many other identity providers, Apple does not provide a photo URL.

If a user chooses not to share their real email with your app, Apple provisions a unique email address for that user to share instead. This email takes the form `xyz@privaterelay.appleid.com`. If you configured the private email relay service, Apple forwards emails sent to the anonymized address to the user's real email address.

Apple only shares user information, such as display names, with apps the first time a user signs in. In most cases, Identity Platform stores this data, which lets you fetch it using `firebase.auth().currentUser.displayName` during future sessions. However, if you allowed users to sign into your app using Apple before integrating with Identity Platform, user information is not available.

## What's next

  * Learn how to [link Apple accounts to other providers](https://docs.cloud.google.com/identity-platform/docs/link-accounts). Note that Apple requires you to get explicit consent from users before you link their Apple accounts to other data.
  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
