---
url: https://docs.cloud.google.com/appengine/docs/flexible/authenticating-users/
title: Authenticating users \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:43.500021+00:00
---

# Authenticating users  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/authenticating-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Authenticating users Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby .NET Custom

To authenticate users in Google Cloud applications, Google offers the following user authentication methods:

Authentication Service | Summary  
---|---  
Identity Platform **(recommended)** | Authenticate users using passwords, phone numbers, popular federated identity providers like Google, Facebook, Twitter, and any provider that supports SAML or OpenID Connect protocol. It offers enterprise features including multi-factor authentication, OIDC and SAML SSO support, multi-tenancy, 99.95% SLA, and more.   
  
The recommended method when starting a new project, so you can use [the capabilities of Identity Platform as well as the legacy features from Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison).  
Firebase Authentication | Authenticate users by using different authentication options including with Google, Facebook, and Twitter. Firebase Authentication supports the largest number of users while maintaining the smallest amount of code.   
  
The recommended method for deploying a solution in the fewest steps.  
Google Identity Services for Web | Authenticate users by using Google user accounts from Gmail and Google Workspace.   
  
The recommended method for supporting Google-only accounts, or supporting Google accounts in an existing sign-in system.  
OAuth 2.0 and OpenID Connect | Provides federated identity from the [provider](https://en.wikipedia.org/wiki/OpenID_Connect#Adoption) of your choice, including Google.   
  
The recommended method if you want to build the user authentication protocol yourself.  
Identity-Aware Proxy (IAP) | Provides authentication by adding an Identity and Access Management (IAM) verification layer above your App Engine app. IAP lets you control access to your App Engine services, before requests reach your application resources. This makes IAP unsuitible for protecting against activity within the same Google Cloud project.   
  
The recommended method if you want to use Google accounts and IAM to control user access.   
  
## Identity Platform

[Identity Platform](https://cloud.google.com/identity-platform) is a customer identity and access management (CIAM) platform that lets organizations customize identity and authentication for user sign-up and sign-in in their applications. Identity Platform supports multiple authentication methods (SAML, OIDC, email/password, social, phone, and custom auth) to provide flexible integration options for any identity solution. Identity Platform is built on Google Cloud's global scale, performance, network, and security, and comes with an enterprise-grade support and SLA to meet the demands of virtually any app or service.

This solution is best for most users who want flexible authentication options based on reliable, enterprise-grade features and SLAs.

Identity Platform offers its own user identity system. If you're already using Google Workspace for your domain and want to authenticate users based on that login, you should use Google Identity Services for Web.

To learn about integrating Identity Platform with App Engine, try the how-to guide for [signing in users on App Engine](https://docs.cloud.google.com/identity-platform/docs/web/app-engine).

## Firebase Authentication

[Firebase Authentication](https://firebase.google.com/docs/auth/) provides a drop-in, customizable identity and authentication service for user sign-up and sign-in. Similar to Identity Platform, Firebase Authentication supports multiple authentication methods (SAML, OIDC, email/password, social, mobile, and custom auth) to provide flexible integration options for any identity solution.

Firebase Authentication differs from Identity Platform in that it lacks certain enterprise features. For more information, see [Differences between Identity Platform and Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison).

This solution is best if you want the most lightweight way to set up user authentication for an App Engine app. For many users, Firebase Authentication is the fastest way to implement or test authentication.

To learn more about Firebase Authentication, try the following:

  * [Firebase Web Tutorial](https://codelabs.developers.google.com/codelabs/firebase-web/) highlights how to use Firebase on a website, including user sign-in with Google as the Identity Provider.

  * [Firebase Quickstart Apps](https://firebase.google.com/docs/samples/) show how to integrate Firebase across platforms, using both federated sign-in and username/password sign-in examples. Samples demonstrate Firebase Authentication using the [JavaScript SDK](https://github.com/firebase/quickstart-js/tree/master/auth) as well as on [iOS](https://github.com/firebase/quickstart-ios/tree/master/authentication) and [Android](https://github.com/firebase/quickstart-android/tree/master/auth).




## Google Identity Services for Web

[Google Identity Services for Web](https://developers.google.com/identity/gsi/web/guides/overview) is a sign-in client library for Google built on the OAuth 2.0 and OpenID Connect protocols. It allows for quick and easy sign-in by providing a Sign in With Google button that appears on your website or app.

This solution is best if you want to authenticate users based on their Google Account, or if you are using Google Admin console for your domain.

## OAuth 2.0 and OpenID Connect

OpenID Connect is an identity layer on top of the OAuth 2.0 protocol. Google offers an [implementation](https://developers.google.com/identity/protocols/oauth2) of OAuth 2.0 that conforms to the [OpenID Connect specification](http://openid.net/connect/) and is [OpenID Certified](http://openid.net/certification/). There are also several [other providers](https://en.wikipedia.org/wiki/OpenID_Connect#Adoption) available.

This solution is best if you want total customization and control of your authentication implementation.

For more information, see [OpenID Connect](https://developers.google.com/identity/openid-connect/openid-connect).

## Identity-Aware Proxy (IAP)

Unlike the other authentication options that implement authentication within your app, [IAP](https://docs.cloud.google.com/iap/docs/concepts-overview) protects and secures your application by adding an IAM authentication and authorization layer in front of your resources. This layer verifies inbound external requests before the app can be reached. Users who are not authorized access to your app can't have access to reach your App Engine app.

You can enable IAP for your whole app, or for specific services or versions of your app. IAP-protected services or applications can only be accessed by [principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) which have the correct [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles). When a user tries to access an IAP-secured resource, IAP performs authentication and authorization checks for you. Learn how IAP secures your application resources on the [IAP overview](https://docs.cloud.google.com/iap/docs/concepts-overview).

IAP doesn't protect against activity within a project, such as one App Engine service accessing another service in the same project.

This solution is best if you want to use Google user accounts and IAM to authorize user access.

To learn how to configure IAP for your App Engine resources, see the [IAP quickstart](https://docs.cloud.google.com/iap/docs/authenticate-users-google-accounts).

## Other authentication services

[Auth0](https://auth0.com/) provides authentication with various identity providers and single sign-on features.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
