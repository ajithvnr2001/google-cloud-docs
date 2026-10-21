---
url: https://docs.cloud.google.com/docs/authentication/use-cases/
title: Authentication and authorization use cases \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:53:06.111706+00:00
---

# Authentication and authorization use cases  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/authentication/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Authentication ](https://docs.cloud.google.com/docs/authentication)
  * [ Guides ](https://docs.cloud.google.com/sdk/docs/overview)



Send feedback 

#  Authentication and authorization use cases Stay organized with collections  Save and categorize content based on your preferences. 

This page lists some common authentication and authorization use cases, with links to more information about how to implement each use case. 

For an overview of authentication at Google, see [Authentication at Google](https://docs.cloud.google.com/docs/authentication).

## Authenticate to Google APIs

Google APIs require a valid access token or API key with every request. How you provide these required credentials depends on where your code is running and what types of credentials the API accepts.

### Use the client libraries and Application Default Credentials

The recommended way to use Google APIs is to use a client library and [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials).

Application Default Credentials (ADC) is a strategy used by the authentication libraries to automatically find credentials based on the application environment. The authentication libraries make those credentials available to [Cloud Client Libraries and Google API Client Libraries](https://docs.cloud.google.com/apis/docs/client-libraries-explained). When you use ADC, your code can run in either a development or production environment without changing how your application authenticates to Google Cloud services and APIs. 

How you [set up ADC](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc) depends on where your code is running. ADC supports both [authenticating as a service account](https://docs.cloud.google.com/docs/authentication/application-default-credentials#attached-sa) and [authenticating as a user](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal).

### Authenticate from Google Kubernetes Engine (GKE)

You use [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/workload-identity) to enable your workloads running on GKE to securely access Google APIs. Workload Identity Federation for GKE lets a GKE service account in your GKE cluster act as an Identity and Access Management (IAM) service account.

### Authenticate from Knative serving

You authenticate your Knative serving services by using [Workload Identity Federation for GKE](https://docs.cloud.google.com/anthos/run/docs/securing/workload-identity), which lets you access Google APIs.

### Use an API that accepts API keys

If an API supports [API keys](https://docs.cloud.google.com/docs/authentication/api-keys), an API key can be provided with a request instead of the access token. API keys associate the request with a Google Cloud project for billing and quota purposes.

To determine whether an API supports API keys, see the documentation for your API.

### Use self-signed JSON Web Tokens (JWTs)

Some Google APIs support self-signed JSON Web Tokens (JWTs) instead of access tokens. Using a self-signed JWT lets you avoid making a network request to Google's authorization server. This approach requires that you [create your own signed JWT](https://developers.google.com/identity/protocols/oauth2/service-account#jwt-auth). For more information about tokens, see [Tokens overview](https://docs.cloud.google.com/docs/authentication/tokens).

### Use the authentication libraries and packages

If ADC and the OAuth implementation provided by the Cloud Client Libraries or Google API Client Libraries isn't available in your environment, you can use the authentication libraries and packages.

The following authentication libraries and packages are available:

  * [C#](https://developers.google.com/api-client-library/dotnet/guide/aaa_oauth)
  * [Go](https://pkg.go.dev/google.golang.org/api/transport)
  * [Java](https://github.com/googleapis/google-auth-library-java)
  * [Node.js](https://github.com/googleapis/google-auth-library-nodejs)
  * [PHP](https://github.com/googleapis/google-auth-library-php)
  * [Python](https://github.com/googleapis/google-cloud-python/tree/main/packages/google-auth)
  * [Ruby](https://github.com/googleapis/google-auth-library-ruby)



You can also implement the OAuth 2.0 flow using Google's OAuth 2.0 endpoints. This approach requires a more detailed understanding of how [OAuth 2.0](https://datatracker.ietf.org/doc/html/rfc6749) and [OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect) work. For more information, see [Using OAuth 2.0 for Web Server Applications](https://developers.google.com/identity/protocols/oauth2/web-server).

## Google Cloud service-specific use cases

Some Google Cloud services support authentication flows specific to that service.

### Provide time-limited access to a Cloud Storage resource using signed URLs

[Signed URLs](https://docs.cloud.google.com/storage/docs/access-control/signed-urls) provide [time-limited access to a specific Cloud Storage resource](https://docs.cloud.google.com/storage/docs/access-control/signing-urls-with-helpers).

### Authenticate to GKE Enterprise clusters

You can authenticate to GKE Enterprise clusters using Google Cloud identities or by using a third-party identity provider:

  * [Authenticate with Google Cloud identities, by using the Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway).
  * [Authenticate with a third-party identity provider that supports OIDC or LDAP, by using GKE Identity Service](https://docs.cloud.google.com/anthos/identity).



### Configure an API deployed with API Gateway or Cloud Endpoints for authentication

API Gateway and Cloud Endpoints support service-to-service authentication and user authentication with Firebase, [Google-signed ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens), Okta, Auth0, and JWTs.

For information, see the product documentation:

  * [Choosing an authentication method for API Gateway](https://docs.cloud.google.com/api-gateway/docs/authentication-method)
  * [Choosing an authentication method for Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/authentication-method)



## Authentication for applications hosted on Cloud Run or Cloud Run functions

Applications hosted on Cloud Run and Cloud Run functions require [ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens) for authentication.

For information about other ways to acquire an ID token, see [Get an ID token](https://docs.cloud.google.com/docs/authentication/get-id-token). For more information about ID tokens, see [Identity tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens).

### Cloud Run

There are various ways to [set up a Cloud Run service](https://docs.cloud.google.com/run/docs/authenticating/overview), depending on how the service will be invoked. You might also need to [authenticate to other services from a Cloud Run service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service), which requires an OIDC ID token.

To [authenticate users to your service from a web or mobile app](https://docs.cloud.google.com/run/docs/authenticating/end-users), you use Identity Platform or Firebase Authentication. You can also use Identity-Aware Proxy (IAP) to [authenticate internal users](https://docs.cloud.google.com/run/docs/authenticating/end-users).

### Cloud Run functions

When you invoke a function, you must [authenticate your invocation](https://docs.cloud.google.com/functions/docs/securing/authenticating). You can use user credentials or an OIDC ID token.

## Authenticate application users

There are various options for authenticating the end users of your application, depending on the rest of your application environment. Use the following descriptions to help you understand the option that's suitable for your application.

Authentication service | Description  
---|---  
[Google Identity Services](https://developers.google.com/identity/) |  Google Identity Services includes Sign In With Google, Google's user sign-in button, and Identity Services APIs and SDK. Google Identity Services is based on the OAuth 2.0 and OpenID Connect (OIDC) protocols.  If you're creating a mobile application, and you want to authenticate users using Gmail and Google Workspace accounts, Sign In With Google could be a good option. Sign In With Google also supports using Google Accounts with an existing sign-in system.  More information Sign In With Google provides Gmail and Google Workspace account sign-in, and support for one-time passwords (OTP). Sign in with Google is targeted toward Google-only accounts, or Google Accounts in an existing sign-in system, for mobile applications.  Sign in With Google is available for [iOS](https://developers.google.com/identity/sign-in/ios/), [Android](https://developers.google.com/identity/one-tap/android), and [web applications](https://developers.google.com/identity/gsi/web).   
[Firebase Authentication](https://firebase.google.com/docs/auth/) |  Firebase Authentication provides authentication services and libraries to authenticate users to your application for a wide array of user account types.  If you want to accept user sign-ins from multiple platforms, Firebase Authentication could be a good option.  More information Firebase Authentication provides authentication support for many user account types. Firebase Authentication supports password authentication and federated sign-in with Google, Facebook, Twitter, and other platforms.  Firebase Authentication uses Identity Platform as its backend but serves a different audience: 

  * Firebase Authentication is aimed at consumer applications, and offers a subset of features compared to Identity Platform. 
  * Identity Platform is intended for building enterprise-focused SaaS applications. It lets you integrate with enterprise IdPs using inbound OIDC or SAML. 

For more information about the differences between these products, see [ Differences between Identity Platform and Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison).  The following links provide more information: 

  * [Where do I start with Firebase Authentication?](https://firebase.google.com/docs/auth/where-to-start) helps you understand some ways of using Firebase Authentication. 
  * For Python applications running in the App Engine standard environment, see [Authenticating users with Firebase](https://docs.cloud.google.com/appengine/docs/standard/python3/building-app/authenticating-users). 

  
[Identity Platform](https://docs.cloud.google.com/identity-platform) |  Identity Platform is a customer identity and access management (CIAM) platform that helps organizations add enterprise-grade identity management capability to their applications.  More information [Identity Platform](https://docs.cloud.google.com/identity-platform) provides a drop-in, customizable identity and authentication service for user sign-up and sign-in. Identity Platform supports multiple authentication methods: SAML, OIDC, email/password, social, phone, and custom options.  Firebase Authentication uses Identity Platform as its backend but serves a different audience: 

  * Firebase Authentication is aimed at consumer applications, and offers a subset of features compared to Identity Platform. 
  * Identity Platform is intended for building enterprise-focused SaaS applications. It lets you integrate with enterprise IdPs using inbound OIDC or SAML. 

For more information about the differences between these products, see [ Differences between Identity Platform and Firebase Authentication](https://docs.cloud.google.com/identity-platform/docs/product-comparison).   
[OAuth 2.0 and OpenID Connect](https://developers.google.com/identity/protocols/oauth2/openid-connect) |  OpenID Connect lets you handle and use authentication tokens with the most customization.  If you want maximum control over your OAuth 2.0 implementation, and you're comfortable implementing OAuth 2.0 flows, consider this option.  More information Google's OAuth 2.0 implementation conforms to the [OpenID Connect specification](http://openid.net/connect/) and is [OpenID Certified](http://openid.net/certification/). OpenID Connect is an identity layer on top of the OAuth 2.0 protocol. Your application can use OpenID Connect to [validate the ID token](https://developers.google.com/identity/protocols/oauth2/openid-connect#validatinganidtoken) and [retrieve user profile information](https://developers.google.com/identity/protocols/oauth2/openid-connect#obtaininguserprofileinformation).  OAuth 2.0 can be used to implement programmatic authentication to an [Identity-Aware Proxy-secured resource](https://docs.cloud.google.com/iap/docs/authentication-howto).   
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap) |  IAP lets you control access to your application before requests reach your application resources.  Unlike the other authentication services in this table, which are implemented within your application, IAP performs authentication before your application can be reached.  More information With IAP, you establish a central authorization layer for applications and use [signed headers](https://docs.cloud.google.com/iap/docs/signed-headers-howto) to secure your app. IAP-protected applications can be accessed only by [principals](https://docs.cloud.google.com/iam/docs/overview#concepts_related_identity) that have the correct [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles). When an end user tries to access an IAP-secured resource, IAP performs authentication and authorization checks for you. IAP doesn't protect against activity within a project, such as another service in the same project.  For Google identities, IAP uses [ ID tokens](https://docs.cloud.google.com/docs/authentication/token-types#identity-tokens). For more information, see [Programmatic authentication](https://docs.cloud.google.com/iap/docs/authentication-howto).  For information about how IAP secures your application resources, see the [IAP overview](https://docs.cloud.google.com/iap/docs/concepts-overview).  The following language-specific tutorials are available for IAP: 

  * [Authenticating users with Go](https://docs.cloud.google.com/go/getting-started/authenticate-users-with-iap)
  * [Authenticating users with Node.js](https://docs.cloud.google.com/nodejs/getting-started/authenticate-users)
  * [Authenticating users with PHP](https://docs.cloud.google.com/php/getting-started/authenticate-users)
  * [Authenticating users with Python](https://docs.cloud.google.com/python/docs/getting-started/authenticate-users)
  * [Authenticating users with Ruby](https://docs.cloud.google.com/ruby/getting-started/authenticate-users-with-iap)

  
[App Engine Users API](https://docs.cloud.google.com/appengine/docs/standard/python/users) |  For applications running in the App Engine standard environment, the Users API is available to provide user authentication for some languages.   
[Authorizing access for end-user resources](https://developers.google.com/identity/protocols/oauth2/web-server) |  If your application accesses resources that are owned by your end user, you must secure their permission to do so. This use case is sometimes called _three-legged OAuth_ or _3LO_ , because there are three entities involved: the application, the authorization server, and the user.   
  
## Authentication and authorization options for Google Cloud and Google Workspace

Google Cloud and Google Workspace provide various options for setting up access, enhancing account security, and administering accounts.

### Grant access to Google Cloud resources for external workloads

[Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) lets you grant on-premises or multi-cloud workloads access to Google Cloud resources. Historically, this use case required the use of service account keys, but Workload Identity Federation avoids the maintenance and [security burden of using service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). Workload Identity Federation supports [OIDC-compatible or SAML 2.0-compatible identity providers](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers).

### Set up an identity provider

You can [use Google as your identity provider](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#google_for_organizations), by using Cloud Identity or Google Workspace. You can also [federate a Cloud Identity or Google Workspace account with an external identity provider](https://docs.cloud.google.com/architecture/identity/overview-google-authentication#external_identities). This approach uses SAML, enabling your employees to use their existing identity and credentials to sign in to Google services.

### Set up two-factor authentication

Requiring two-factor authentication is a best practice that helps to prevent bad actors from accessing an account when they have gained access to the credentials for that account. With two-factor authentication, a second piece of information or identification from the user is required before that user is authenticated. Google's provides several solutions that support the [FIDO (Fast IDentity Online)](https://fidoalliance.org/certification/fido-certified-products/) standard.

Identity Platform supports two-factor authentication for [web](https://docs.cloud.google.com/identity-platform/docs/web/mfa), [iOS](https://docs.cloud.google.com/identity-platform/docs/ios/mfa), and [Android](https://docs.cloud.google.com/identity-platform/docs/android/mfa) apps.

Google Identity Services supports [FIDO (Fast IDentity Online) authentication](https://developers.google.com/identity/fido).

Google supports various hardware solutions for two-factor authentication, such as [Titan Keys](https://cloud.google.com/security/products/titan-security-key).

### Set up certificate-based access

Part of the Chrome Enterprise Premium zero trust solution, certificate-based access [limits access to only authenticated users on a trusted device](https://docs.cloud.google.com/chrome-enterprise-premium/docs/securing-resources-with-certificate-based-access), identifying devices through their X.509 certificates. Certificate-based access is also sometimes referred to as mutual Transport Layer Security (mTLS).

## General account and authentication information

### Get help with accessing a Google Account

If you need help with accessing or managing a Google Account, see the [Google Account support page](https://support.google.com/accounts#topic=).

### Handle compromised credentials

If you believe that your credentials have been compromised, there are steps you or your administrator can take to mitigate the situation. For more information, see [Handling compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials).

### Get help with certificate authority issues

If you see errors related to an issue with your certificate or certificate authority (CA), including your root CA, see the [Google Trust Services FAQ](https://pki.goog/faq) for more information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
