---
url: https://docs.cloud.google.com/identity-platform/docs/concepts-admin-auth-api/
title: Introduction to the Admin Auth API \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:58.958334+00:00
---

# Introduction to the Admin Auth API  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/concepts-admin-auth-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to the Admin Auth API

Identity Platform is built on an enhanced infrastructure that supports authentication of users to your apps and services. You can use the Firebase Admin SDK to integrate your own servers with Identity Platform and manage your users or authentication tokens. There are a number of reasons you would want to do this:

**User Management**

It is not always convenient to have to visit the Google Cloud console (Google Cloud console) to manage your Identity Platform users. The admin user management API provides programmatic access to those same users. It even allows you to do things the Google Cloud console cannot, such as retrieving a user's full data and changing a user's password, email address, or phone number.

**Custom Authentication**

You can integrate an external user system with Identity Platform. For example, you may already have a pre-existing user database or you may want to integrate with a third-party identity provider that Identity Platform doesn’t natively support.

To do this, you can create custom tokens with arbitrary claims identifying the user. These custom tokens can then be used to sign into the Identity Platform service on a client application and assume the identity described by the token's claims. This identity will then be used when accessing other Identity Platform services, such as Cloud Storage.

**Identity Verification**

Identity Platform is primarily used to identify users of your app in order to restrict access to other services, like Cloud Storage. You can also use the service to identify these users on your own server. This lets you securely perform server-side logic on behalf of users that have signed in with Identity Platform.

To do this, you can retrieve an ID token from a client application signed in with Identity Platform and include the token in a request to your server. Your server then verifies the ID token and extracts the claims that identify the user (including their `uid`, the identity provider they logged in with, etc.). This identity information can then be used by your server to carry out actions on behalf of the user.

The Firebase Admin SDK provides methods for accomplishing the authentication tasks above by enabling you to manage your users, generate custom tokens, and verify ID tokens.

**Custom User Claims**

In some cases, you may want to implement fine-grained access control for users already signed in with one of the supported Identity Platform auth providers such as Email/Password, Google, Facebook, phone, etc. A combination of custom user claims and application security rules provides this capability. For example, a user signed in with the Identity Platform Email and Password provider can have access control defined using custom claims.

## User management

The Firebase Admin SDK provides an API for managing your Identity Platform users with elevated privileges. The admin user management API gives you the ability to programmatically retrieve, create, update, and delete users without requiring a user's existing credentials and without worrying about client-side rate limiting.

[Manage users](https://docs.cloud.google.com/identity-platform/docs/concepts-manage-users)

## Custom token creation

The primary use for creating custom tokens is to allow users to authenticate against an external or legacy authentication mechanism. This could be one you control, such as your LDAP server, or a third-party OAuth provider which Identity Platform does not natively support, such as Instagram or LinkedIn.

The Firebase Admin SDK has a built-in method for creating custom tokens. You can also programmatically create custom tokens in any language using third-party JWT libraries.

Your server should create a custom token with a unique identifier (`uid`) and pass that token to a client app, which will use it to sign in to Identity Platform. See [Create custom tokens](https://firebase.google.com/docs/auth/admin/create-custom-tokens) for code samples and more details about the custom token creation process.

## ID token verification

If your Identity Platform client app communicates with your backend server, you might need to identify the currently signed-in user on your server so you can perform server-side logic on their behalf. You can do this securely by using ID tokens, which are created by Identity Platform when a user signs into an Identity Platform app. ID tokens conform to the [OpenID Connect spec](http://openid.net/specs/openid-connect-core-1_0.html) and contain data to identify a user, as well as some other profile and authentication related information. You can send, verify, and inspect these tokens from your own backends. This allows you to securely identify the currently signed in user and authorize them into your own backend resources.

The Firebase Admin SDK has a built-in method for verifying ID tokens. You can also programmatically verify ID tokens in any language using third-party JWT libraries. See [Verify ID tokens](https://firebase.google.com/docs/auth/admin/verify-id-tokens) for more details and code samples about the ID token verification process.

## Custom user claims

The Firebase Admin SDK lets you set custom attributes on user accounts. With custom user claims, you can give users different levels of access (roles), which are then enforced in an application's security rules.

After custom claims are modified on a user via the Firebase Admin SDK, they are propagated to the authenticated users on the client side via their ID tokens. The ID token is a trusted mechanism for delivering these custom claims, and all authenticated access must validate the ID token before processing the associated request.

[Control Access with Custom Claims](https://firebase.google.com/docs/auth/admin/custom-claims)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
