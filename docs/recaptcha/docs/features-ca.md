---
url: https://docs.cloud.google.com/recaptcha/docs/features-ca/
title: Features for integration with Google Cloud Armor \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:00.367497+00:00
---

# Features for integration with Google Cloud Armor  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/features-ca/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Features for integration with Google Cloud Armor Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you understand the features of reCAPTCHA for Google Cloud Armor and determine which feature best matches your use case.

reCAPTCHA offers the following features that you can use to integrate with Google Cloud Armor:

  * [reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/features-ca#action-token)
  * [reCAPTCHA session-tokens](https://docs.cloud.google.com/recaptcha/docs/features-ca#session-token)
  * [reCAPTCHA challenge page](https://docs.cloud.google.com/recaptcha/docs/features-ca#redirect)



## Features overview

reCAPTCHA for Google Cloud Armor integrations support action-tokens, session-tokens and challenge page.

You can use one or more reCAPTCHA for Google Cloud Armor features in a single application. For example, you can choose to apply a session-token for all pages, and based on the session-token's score, you can redirect suspicious requests to the reCAPTCHA challenge page. Also, you can use an action-token for high-profile actions, such as checkout. For more information, see [examples](https://docs.cloud.google.com/recaptcha/docs/examples-ca). 

The following table shows a brief comparison of the available reCAPTCHA for Google Cloud Armor features:

**Note:** Only reCAPTCHA action-tokens are supported for the integration of mobile applications with Google Cloud Armor. Comparison category | reCAPTCHA action-tokens | reCAPTCHA session-tokens | reCAPTCHA challenge page  
---|---|---|---  
Use case | Use to protect user actions, such as **login** or **comment posts**. | Use to protect the whole user session on the site's domain. | Use when you suspect spam activity directed to your site and you need to screen out bots. **This method interrupts a user's activity because the user has to verify a CAPTCHA challenge.**  
Supported platforms | Websites and mobile applications | Websites | Websites  
Client integration effort  | **Medium** Manual client-side integration. | **Medium** Install reCAPTCHA JavaScript manually or through injection on the WAF. | **Low** Interstitial triggered by security policies.  
Detection accuracy  | **Highest** Client, server, and action specific signals are available. | **High** Client and server speicific signals are available. | **Medium** Client and server speicific signals are available. Client signals are only available in an interstitial page.  
Supported reCAPTCHA version  | [reCAPTCHA score-based and checkbox keys](https://docs.cloud.google.com/recaptcha/docs/keys) | [reCAPTCHA score-based keys](https://docs.cloud.google.com/recaptcha/docs/keys) | [reCAPTCHA challenge-based keys embedded in an interstitial page](https://docs.cloud.google.com/recaptcha/docs/keys)  
  
## reCAPTCHA action-tokens

You can use reCAPTCHA action-tokens to protect important user interactions, such as checkout on web pages and on mobile applications.

**Note:** Only reCAPTCHA action-tokens are supported for integrating reCAPTCHA with Google Cloud Armor on mobile applications.

The reCAPTCHA action-tokens workflow consists of the following steps:

  1. When an end user triggers an action protected by reCAPTCHA, the web page or the mobile application sends signals that are collected in the browser to reCAPTCHA for analysis.
  2. reCAPTCHA sends an action-token to the web page or the mobile application.
  3. You attach this action-token to the header of the request that you want to protect.
  4. When the end user requests access with the action-token, Google Cloud Armor decodes and validates the action-token attributes instead of your backend application.
  5. Google Cloud Armor applies actions based on your configured security policy rules.



The following sequence diagram shows the reCAPTCHA action-tokens workflow for websites:

![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_action_token.svg)![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_action_token.svg)

The following sequence diagram shows the reCAPTCHA action-tokens workflow for mobile applications:

![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_action_token_mobile.svg)

![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_action_token_mobile.svg)

## reCAPTCHA session-tokens

You can use reCAPTCHA session-tokens when you want to protect the whole user session on the site's domain. A session token lets you reuse a valid token across requests for a specified period, so that you don't need to call `execute()` for every user action, reducing user friction and the number of calls to `execute()`.

To enable reCAPTCHA to learn about the browsing pattern of your end users, we recommend that you use a reCAPTCHA session-token on all the web pages of your site.

reCAPTCHA session-tokens workflow consists of the following steps:

  1. The browser loads the reCAPTCHA JavaScript from reCAPTCHA.
  2. The reCAPTCHA JavaScript sets a session-token as a cookie on the end-user's browser after calling `execute()`.
  3. The end-user's browser stores the cookie and reCAPTCHA JavaScript refreshes the cookie every 30 minutes as long as the reCAPTCHA JavaScript remains active.
  4. When the user requests access with the cookie, Google Cloud Armor validates this cookie and applies actions based on the security policy rules.



The following sequence diagram shows the reCAPTCHA session-tokens workflow:

![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_session_token.svg)![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_session_token.svg)

## reCAPTCHA challenge page

You can use the reCAPTCHA challenge page feature to redirect incoming requests to reCAPTCHA to determine whether each request is potentially fraudulent or legitimate.

This application of a redirect and possible CAPTCHA challenge interrupts a user's activity. We recommend using it to screen out bots when you suspect spam activity directed to your site.

When an end user (user) visits your site for the first time, the following events take place:

  1. At the Google Cloud Armor layer, the user's request is redirected to the reCAPTCHA challenge page.
  2. reCAPTCHA responds with an HTML page embedded with the reCAPTCHA JavaScript.
  3. When the challenge page is rendered, reCAPTCHA assesses the user interaction. If necessary, reCAPTCHA serves a CAPTCHA challenge to the user.
  4. Depending on the result of the assessment, reCAPTCHA does the following:

     1. If the user interaction passes the assessment, reCAPTCHA issues an exemption cookie. The browser attaches this exemption cookie to the user's subsequent requests to the same site until the cookie expires. By default, the exemption cookie expires after three hours.
     2. If the user interaction does not pass the assessment, reCAPTCHA does not issue an exemption cookie.
  5. reCAPTCHA reloads the web page with the exemption cookie if the user accesses the web page using a GET/HEAD call. If the user accesses the web page using a POST/PUT call, then the user needs to click the reload link on the page.

  6. Google Cloud Armor exempts requests that have a valid exemption cookie from being redirected again and grants access to your site.




The following sequence diagram shows the reCAPTCHA challenge page workflow:

![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_redirect.svg)![](https://docs.cloud.google.com/static/recaptcha/images/sequence_diagram_redirect.svg)

## What's next

  * Learn about the [token attributes for Cloud Armor](https://docs.cloud.google.com/recaptcha/docs/token-attr-ca).
  * [Integrate reCAPTCHA with Cloud Armor on websites](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca).
  * [Integrate reCAPTCHA with Cloud Armor on mobile applications](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca-mobile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
