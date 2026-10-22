---
url: https://docs.cloud.google.com/identity-platform/docs/web/microsoft/
title: Signing in users with Microsoft \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:45:03.732120+00:00
---

# Signing in users with Microsoft  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/web/microsoft/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Signing in users with Microsoft

This document shows you how to use Identity Platform to sign in users with Microsoft. Both personal Microsoft accounts and Azure Active Directory (Azure AD) accounts are supported.

## Before you begin

This tutorial assumes you've already enabled Identity Platform, and have a basic web app written using HTML and JavaScript. See the [Quickstart](https://docs.cloud.google.com/identity-platform/docs/sign-in-user-email) to learn how.

## Configuring Microsoft as a provider

To configure Microsoft as an identity provider:

  1. Go to the **Identity Providers** page in the Google Cloud console.

[Go to the Identity Providers page](https://console.cloud.google.com/customer-identity/providers)

  2. Click **Add A Provider**.

  3. Select **Microsoft** from the list.

  4. Enter your Microsoft **App ID** and **App Secret**. If you don't already have an ID and secret, follow the steps in [Quickstart: Register an app with the Azure AD v2.0 endpoint](https://docs.microsoft.com/en-us/azure/active-directory/develop/quickstart-register-app) to obtain one.

This endpoint supports both personal Microsoft accounts and Azure AD accounts. See the [Microsoft identity platform (v2.0) overview](https://docs.microsoft.com/en-us/azure/active-directory/develop/v2-overview) to learn more about Azure AD.

  5. Configure the URI listed under **Configure Microsoft** as the valid OAuth redirect URI for your Microsoft app. If you configured a custom domain in Identity Platform, update the redirect URI in your Microsoft app configuration to use the custom domain instead of the default domain. For example, change `https://myproject.firebaseapp.com/__/auth/handler` to `https://auth.myownpersonaldomain.com/__/auth/handler`. 

  6. Register your app's domains by clicking **Add Domain** under **Authorized Domains**. For development purposes, `localhost` is already enabled by default.

**Important:** In projects created after April 28, 2025, Identity Platform no longer includes `localhost` as an authorized domain by default. Google strongly discourages the use of `localhost` in production projects. If you choose to authorize `localhost`, you can manually add it in the **Settings** page, in **Authorized Domains** , by clicking **Add Domain**.
  7. Under **Configure your application** , click **Setup Details**. Copy the snippet into your app's code to initialize the Identity Platform client SDK.

  8. Click **Save**.




## Signing in users with the client SDK

  1. Create an instance of the `OAuthProvider` object, passing `microsoft.com` as the provider ID:

###  JavaScript 
         
         var provider = new firebase.auth.OAuthProvider('microsoft.com');
         
         [microsoft-oauth.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/microsoft-oauth.js#L11-L11)

  2. **Optional:** Add OAuth scopes. Scopes specify what data you are requesting from Microsoft. More sensitive data may require specific scopes. Consult Microsoft's [documentation](https://docs.microsoft.com/azure/active-directory/develop/v2-permissions-and-consent) to determine what scopes your app needs.

###  JavaScript 
         
         provider.addScope('mail.read');
         provider.addScope('calendars.read');
         

  3. **Optional:** Specify additional custom OAuth parameters. These are specific to Microsoft, and are typically used to customize the authentication experience.

###  JavaScript 
         
         provider.setCustomParameters({
           // Force re-consent.
           prompt: 'consent',
           // Target specific email with login hint.
           login_hint: 'user@firstadd.onmicrosoft.com'
         });
         

You can use the `mkt` parameter to customize the language of the authentication flow. For example:
         
         provider.setCustomParameters({
           mkt: 'fr'
         });
         

You can use the `tenant` property to limit access to users outside a particular Azure AD domain. Specify either the friendly domain name of the tenant, or its GUID identifier. Users who are not within this domain will not be able to sign in. For example:
         
         provider.setCustomParameters({
           // Optional "tenant" parameter in case you are using an Azure AD tenant.
           // eg. '8eaef023-2b34-4da1-9baa-8bc8c9d6a490' or 'contoso.onmicrosoft.com'
           // or "common" for tenant-independent tokens.
           // The default value is "common".
           tenant: 'TENANT_ID'
         });
         

See the [Microsoft OAuth documentation](https://docs.microsoft.com/en-us/azure/active-directory/develop/v1-protocols-oauth-code) for a full list of parameters Microsoft supports. Note that you can't pass parameters reserved by OAuth or Identity Platform.

  4. Use the `OAuthProvider` object to sign in the user. You can either open a pop-up window, or redirect the current page. Redirecting is easier for users on mobile devices.

To show a pop-up, call `signInWithPopup()`:

###  JavaScript 
         
         firebase.auth().signInWithPopup(provider)
           .then((result) => {
             // IdP data available in result.additionalUserInfo.profile.
             // ...
         
             /** @type {firebase.auth.OAuthCredential} */
             var credential = result.credential;
         
             // OAuth access and id tokens can also be retrieved:
             var accessToken = credential.accessToken;
             var idToken = credential.idToken;
           })
           .catch((error) => {
             // Handle error.
           });
         
         [microsoft-oauth.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/microsoft-oauth.js#L41-L55)

To redirect the page, first call `signInWithRedirect()`:

Follow the [best practices](https://docs.cloud.google.com/identity-platform/docs/web/redirect-best-practices) when using `signInWithRedirect`, `linkWithRedirect`, or `reauthenticateWithRedirect`. 

###  JavaScript 
         
         firebase.auth().signInWithRedirect(provider);
         
         [microsoft-oauth.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/microsoft-oauth.js#L61-L61)

Then, retrieve the Microsoft token by calling `getRedirectResult()` when your page loads:

###  JavaScript 
         
         firebase.auth().getRedirectResult()
           .then((result) => {
             // IdP data available in result.additionalUserInfo.profile.
             // ...
         
             /** @type {firebase.auth.OAuthCredential} */
             var credential = result.credential;
         
             // OAuth access and id tokens can also be retrieved:
             var accessToken = credential.accessToken;
             var idToken = credential.idToken;
           })
           .catch((error) => {
             // Handle error.
           });
         
         [microsoft-oauth.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/microsoft-oauth.js#L67-L81)




Once you have an access token, you can use it to call the [Microsoft Graph API](https://docs.microsoft.com/graph/overview) For example:

###  REST 
    
    
    curl -i -H "Authorization: Bearer [ACCESS_TOKEN]" https://graph.microsoft.com/v1.0/me
    

Unlike other providers supported by Identity Platform, Microsoft does not provide a photo URL for users. Instead, you'll need to use the Graph API to request the binary data for the photo.

In addition to the access token, you can also retrieve a user's Microsoft [ID token](https://docs.microsoft.com/en-us/azure/active-directory/develop/id-tokens). The `oid` claim on this token contains a unique ID for the user. You can compare this against the ID located at `user.providerData[0].uid`. If your users are signing in with an Azure AD tenant, these fields will match exactly. If they aren't, the field will be padded with zeroes (for example, the federated ID `4b2eabcdefghijkl` will appear as `00000000-0000-0000-4b2e-abcdefghijkl`).

Do not use the `sub` claim to compare user IDs. The `sub` claim is app-specific, and will not match the ID used by Microsoft.

## Signing in users manually

Some other Identity Platform providers, such as [Google](https://docs.cloud.google.com/identity-platform/docs/web/google), [Facebook](https://docs.cloud.google.com/identity-platform/docs/web/facebook), and [Twitter](https://docs.cloud.google.com/identity-platform/docs/web/twitter), allow you to sign in users manually by calling `signInWithCredential()`.

This capability is not supported for Microsoft. Identity Platform is not able to verify the audience of Microsoft OAuth access tokens, which is a critical security requirement.

If you can't use the Identity Platform client SDK to sign in users, you'll need to use a third-party OAuth library to authenticate with Microsoft. You can then use [Custom authentication](https://docs.cloud.google.com/identity-platform/docs/web/custom) to exchange the Microsoft credential for a custom token.

## What's next

  * Learn more about [Identity Platform users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users).
  * Sign in users with [other identity providers](https://docs.cloud.google.com/identity-platform/docs/how-to#signing-in-users).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
