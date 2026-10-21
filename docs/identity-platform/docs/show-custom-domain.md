---
url: https://docs.cloud.google.com/identity-platform/docs/show-custom-domain/
title: Showing a custom domain during sign in \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:18.012206+00:00
---

# Showing a custom domain during sign in  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/show-custom-domain/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Showing a custom domain during sign in

This document shows you how to customize the Identity Platform authentication handler so users see your domain when signing in.

## Understand the default authentication handler

When you enable Identity Platform for your project, a unique subdomain powered by Firebase Hosting is created automatically. The domain takes the form of `https://[PROJECT-ID].firebaseapp.com`. By default, Identity Platform uses this domain to handle all OAuth, OIDC, and SAML sign-in redirects.

Using the default domain has several benefits:

  * Use multiple domains with the same federated providers

  * Share a single callback URL across different services and domains

  * Works with providers that only support one callback URL per app




The downside of the default handler is that users will briefly see the `https://[PROJECT-ID].firebaseapp.com` URL when signing in.

## Customize the authentication handler

To override the default handler with your custom handler, do the following:

  1. From the Firebase console, [connect your project to a custom domain](https://firebase.google.com/docs/hosting/custom-domain).

  2. In the Google Cloud console, go to the **Identity Platform > Identity providers** page.  
[Go to Identity providers](https://console.cloud.google.com/customer-identity/providers)  


  3. Select your identity provider.

  4. In the **Project settings** side pane, click **Add Domain** , and add your custom domain.

  5. Click **Save**.

  6. In your app configuration, update the callback URL with your custom domain instead of the default domain. For example, change `https://myproject.firebaseapp.com/__/auth/handler` to `https://auth.mycustomdomain.com/__/auth/handler`.




## Update your client SDK configuration

### Web

You can copy the initialization code for the client SDK from the Google Cloud console. If you customize the authentication handler, you'll need to update the `authDomain` field to your custom domain:

### Web version 9
    
    
    import { initializeApp } from "firebase/app";
    
    const firebaseConfig = {
      apiKey: "...",
      // By default, authDomain is '[YOUR_APP].firebaseapp.com'.
      // You may replace it with a custom domain.
      authDomain: '[YOUR_CUSTOM_DOMAIN]'
    };
    const firebaseApp = initializeApp(firebaseConfig);
    
    [auth_init_custom_domain.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/snippets/auth-next/index/auth_init_custom_domain.js#L8-L16)

### Web version 8
    
    
    firebase.initializeApp({
      apiKey: '...',
      // By default, authDomain is '[YOUR_APP].firebaseapp.com'.
      // You may replace it with a custom domain.
      authDomain: '[YOUR_CUSTOM_DOMAIN]'
    });
    
    [index.js](https://github.com/firebase/snippets-web/blob/7055a148689c9a4631824e2b880482e16151e4fb/auth/index.js#L107-L112)

### Android and iOS

To customize the authentication handler, use the following code:

###  Java
    
    
    FirebaseAuth.getInstance().setCustomAuthDomain("[YOUR_CUSTOM_DOMAIN]");
    

###  Kotlin+KTX
    
    
    Firebase.auth.setCustomAuthDomain("[YOUR_CUSTOM_DOMAIN]")
    

###  Swift 
    
    
    let auth = Auth.auth()
    auth.customAuthDomain = "[YOUR_CUSTOM_DOMAIN]"
    

###  Objective-C 
    
    
    FIRAuth *auth = [FIRAuth auth];
    auth.customAuthDomain("[YOUR_CUSTOM_DOMAIN]");
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
