---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/cookies/
title: Cookies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:27:24.896950+00:00
---

# Cookies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/cookies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Cookies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Background

Apigee customers can provide API products to customers (app developers) with a developer portal. This document describes how cookies are used to deliver this experience for portal users. 

**Note:** Unless otherwise specified, cookies may be assumed to to have at least the following attributes: Attribute | Value  
---|---  
HttpOnly | true  
Secure | true  
  
## Cookies for all visitors

  * **JSESSIONID** : A random value that is used to correlate web requests with sessions. 
  * **X-Apigee-CSRF2** : Used for all visitors to a site, but is only populated after a user authenticates. It helps to protect against cross-site request forgeries. **Note:** This cookie intentionally sets the `HttpOnly` attribute to `false`, as its only purpose is to be read by the client. 



## Additional cookies for authenticated users

  * **portalSession** : A JWT session token used to authenticate requests. It is cleared on logout. 
  * **portalRefresh** : A JWT refresh token used to generate a new session token. It is cleared on logout. 



## Cookies specific to the identity service 

  * **SSO_JSESSIONID** : Used by the identity service to maintain a logged in session for the user and to maintain state during login. 
  * **route** : Used to route a user to an identity instance for their session. 
  * **X-Uaa-Csrf** : Used by the identity service to protect against cross-site request forgeries 



## Use of reCAPTCHA

reCAPTCHA is used by the identity service to protect against robot actors, which may utilize additional cookies, including the google.com domain. See [ reCAPTCHA documentation](https://developers.google.com/recaptcha/docs/faq#does-recaptcha-use-cookies) regarding their use of cookies. 

The integration with reCAPTCHA generates the **recaptcha-ca-t** cookie, which is used to provide security integration and protection against robot actors. 

## Deprecated Cookies

  * **portalDefaultDomain**(deprecated): Was used for portals where the custom domain was enabled before February 18, 2020. It determined which domain to send requests to, and it has since been deprecated. Disabling and re-enabling the custom domain of any portal will remove it. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
