---
url: https://docs.cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions/
title: Blocking functions reference \u00a0|\u00a0 Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:04.802952+00:00
---

# Blocking functions reference  |  Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/reference/gcip-cloud-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Blocking functions reference

This page describes the `AdditionalUserInfo` and `AuthCredential` interfaces that are available when using Identity Platform [blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions).

## AdditionalUserInfo
    
    
    interface AdditionalUserInfo {
      // The provider ID, such as saml.provider, oidc.provider, google.com,
      // facebook.com, etc.
      providerId: string;
      // Raw user info. This is the raw user info also returned in client SDK.
      profile?: any;
      // This is the Twitter screen_name.
      username?: string;
      // Whether the user is new or existing.
      // This is true for beforeCreate, false for others.
      isNewUser: boolean;
    }
    

## AuthCredential

See [Supported OAuth credentials and data](https://docs.cloud.google.com/identity-platform/docs/blocking-functions#supported_credentials) for more information.
    
    
    interface AuthCredential {
      // All user SAML or OIDC claims. These are in plain object format but should
      // be verified and parsed from SAML response, IdP ID token, etc.
      // This is empty for all other providers.
      claims?: {[key: string]: any};
      // Optional OAuth ID token if available and enabled in the project config.
      idToken?: string;
      // Optional OAuth access token if available and enabled in the project config.
      accessToken?: string;
      // Optional OAuth refresh token if available and enabled in the project config.
      refreshToken?: string;
      // Optional OAuth expiration if available and enabled in the project config.
      expirationTime?: string;
      // Optional OAuth token secret if available and enabled in the project config.
      secret?: string;
      // eg. saml.provider, oidc.provider, google.com, facebook.com, etc.
      providerId: string;
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
