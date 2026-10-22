---
url: https://docs.cloud.google.com/armor/docs/bot-management/
title: Bot management overview \u00a0|\u00a0 Google Cloud Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:31.532046+00:00
---

# Bot management overview  |  Google Cloud Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/armor/docs/bot-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Google Cloud Armor ](https://docs.cloud.google.com/armor/docs)
  * [ Guides ](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)



Send feedback 

#  Bot management overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Armor and [reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/overview) provide tools to help you evaluate and act on incoming requests that might be from automated clients.

reCAPTCHA uses advanced risk analysis techniques to distinguish between human users and automated clients. reCAPTCHA assesses the user based on the configuration of the reCAPTCHA WAF site keys. It then issues an encrypted token with attributes that represent the associated risk. Cloud Armor deciphers this token inline, without an additional request or response to the reCAPTCHA service. Based on the token attributes, Cloud Armor lets you allow, deny, rate-limit or redirect the incoming requests. For more information, see the [Cloud Armor and reCAPTCHA integration overview](https://docs.cloud.google.com/recaptcha/docs/setup-overview-ca).

Cloud Armor's bot management includes the following integrated capabilities.

  * Manual challenge (reCAPTCHA challenge page)

    * You must configure a security policy rule to redirect a request for reCAPTCHA assessment.
    * You can create your own reCAPTCHA WAF site key and associate it with your security policy. We strongly recommend that you do this. For more information, see [Implement a reCAPTCHA challenge](https://docs.cloud.google.com/recaptcha/docs/implement-tokens#redirect).
    * You can permit only end-users who pass the reCAPTCHA manual challenge by redirecting end-users for reCAPTCHA assessment.
  * Enforce reCAPTCHA frictionless assessment

    * You can take different actions on incoming requests based on reCAPTCHA's assessment of the risk that the request originates from a bot. You can write security policy rules to evaluate and filter traffic based on the token score and other token attributes.
    * You must implement reCAPTCHA action-tokens, session-tokens, or both. reCAPTCHA action-tokens are supported on applications running on websites, iOS, and Android. reCAPTCHA session-tokens are supported only on websites. For more information about reCAPTCHA tokens, see [reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/waf-features#action-token) and [reCAPTCHA session-tokens](https://docs.cloud.google.com/recaptcha/docs/waf-features#session-token).
    * You must configure a security policy rule that evaluates reCAPTCHA tokens.
    * To prevent token theft, we recommend that you associate your own reCAPTCHA keys for WAF with your security policy rule.



Cloud Armor bot management also includes the following capabilities.

  * Redirect (302) 
    * You can redirect requests to your configured alternative URL by configuring Cloud Armor to serve an HTTP 302 response to the client.
  * Decorate request 
    * You can insert custom headers in requests, and static values into those headers, before proxying a requests to your backends.

**Note:** For mobile applications, only reCAPTCHA action-tokens are supported. The manual challenge (reCAPTCHA challenge page), and session-tokens aren't supported.

## Use cases

This section describes how you can use Cloud Armor bot management capabilities to mitigate bot risk and to control access from automated clients.

### Use a manual challenge to distinguish between legitimate users and automated clients

You can redirect a request to reCAPTCHA to assess the end-client and serve manual challenges if necessary, without any additional reCAPTCHA implementation. When human users share the same signature (such as URL paths or other L7 signatures) as a bot or an abusive system, this action provides a way for them to prove that they are human. Only users who pass the assessment can gain access to your service.

The following diagram shows how a manual challenge distinguishes whether a request comes from a human or an automated client:

[ ![Example of redirecting to reCAPTCHA.](https://docs.cloud.google.com/static/armor/images/redirect-to-recaptcha.svg)](https://docs.cloud.google.com/static/armor/images/redirect-to-recaptcha.svg) Example of redirecting to reCAPTCHA (click to enlarge).

Suppose a user Maya and a bot are both browsing the login page (`/login.html`) on your site. To allow access to Maya without granting access to the bot, you can configure a security policy rule with the advanced match expression `request.path.matches("/login.html")`, with a `redirect` action of type `GOOGLE_RECAPTCHA`. The end-to-end user experience is as follows:

  1. An end user visits your site for the first time.
  2. Cloud Armor evaluates the request, and determines to redirect it to reCAPTCHA.
  3. reCAPTCHA responds with an HTML page with the reCAPTCHA JavaScript embedded.
  4. When the response is rendered, the embedded JavaScript runs to assess the user, and serves manual challenges if necessary. 
     * If the user passes the assessment, reCAPTCHA issues an exemption cookie, which is auto-attached by the browser to each of the subsequent requests to the same site until the cookie expires.
     * Otherwise, reCAPTCHA does not issue an exemption cookie.



In this example, only Maya passes reCAPTCHA assessment and receives an exemption cookie, gaining access to your site.

When you use manual challenges, we recommend that you create your own reCAPTCHA WAF site key and associate it with the security policy. This lets you view reCAPTCHA metrics associated with the site key and train a security model specific to the site key. For more information, see [Create reCAPTCHA WAF challenge site key](https://docs.cloud.google.com/recaptcha/docs/implement-tokens#redirect).

If you don't create and associate a site key, reCAPTCHA uses a Google-managed site key during assessment. You cannot view reCAPTCHA metrics associated with site keys that you don't own, including Google-managed site keys.

### Enforce reCAPTCHA assessment

When there is a reCAPTCHA token attached to an incoming request, Cloud Armor evaluates the request and applies the configured action based on the individual attributes in the token. Cloud Armor security policy evaluation happens at the edge of Google's network, so your backends are not involved in deciphering the token.

#### reCAPTCHA tokens

reCAPTCHA issues two types of tokens: action-tokens and session-tokens. Both types of token return a score for each request based on the interactions with your site or app. Both types of tokens contain attributes, including a score that represents the risk associated with the user. They also contain information about the reCAPTCHA key that you used when the token was generated.

Before you configure security policy rules, you must decide whether to use action-tokens, session-tokens, or both. We recommend reading the reCAPTCHA documentation to inform your decision. For more information, see the [reCAPTCHA use case comparison](https://docs.cloud.google.com/recaptcha/docs/usecase).

After determining which type of token you want to use, you implement reCAPTCHA for the token to be attached with a request. For information about implementing tokens in reCAPTCHA, see the following pages:

  * Web applications 
    * [Implement reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca#action-token)
    * [Implement reCAPTCHA session-tokens](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca#session-token)
  * Mobile applications 
    * [Implement reCAPTCHA action-tokens](https://docs.cloud.google.com/recaptcha/docs/implement-waf-ca-mobile#action-token)



Finally, use the Cloud Armor rules language to configure security policy rules to evaluate reCAPTCHA tokens that are attached with the request. To prevent token theft, we strongly recommend that you associate your reCAPTCHA keys with your security policy rules. When you associate reCAPTCHA keys with a security policy rule, Cloud Armor performs additional validation on the token by comparing the reCAPTCHA key in the token against reCAPTCHA keys that are associated with the rule. Cloud Armor considers a token with an unknown reCAPTCHA key as invalid. For more information, see [enforce reCAPTCHA frictionless assessment](https://docs.cloud.google.com/armor/docs/configure-bot-management#enforce-assessment).

The following figure demonstrates the reCAPTCHA token enforcement flow.

[ ![reCAPTCHA token enforcement flow.](https://docs.cloud.google.com/static/armor/images/enforce-recaptcha-token.svg)](https://docs.cloud.google.com/static/armor/images/enforce-recaptcha-token.svg) reCAPTCHA token enforcement flow (click to enlarge).

### Redirect (302 response)

You can use a URL-based redirect action to externally redirect requests to a different endpoint. You supply a redirect target in the form of a URL, and Cloud Armor redirects the request by serving an HTTP 302 response to the client.

### Decorate request

Cloud Armor can insert custom request headers with static user-defined values before proxying the requests to your application. This option lets you tag suspicious requests for alternative downstream processing, like serving a honey-pot, or for additional analysis and monitoring. Note that this action parameter must be added to an existing `allow` action.

### Custom headers

If you have configured Cloud Armor to insert a custom header or value with the same header name as one of the custom headers for the global external Application Load Balancer or the classic Application Load Balancer, then the header value is overwritten by the load balancer. For more information, see [Creating custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#variables).

In addition, if you choose a header name that already exists in the request, including standard HTTP headers, then the original value in that header is overwritten by the user-defined value provided to the Cloud Armor rule.

## Integrate with rate limiting

Cloud Armor rate limiting rules are compatible with bot management capabilities. For example, you can redirect a request for reCAPTCHA assessment or redirect to a different URL when the number of requests exceeds the configured threshold. In addition, you can identify clients for rate limiting based on reCAPTCHA exemption cookies or tokens, to throttle requests or ban clients that reuse or abuse the same cookie or token at a rate exceeding the user-configured threshold.

### Rate limit reCAPTCHA exemption cookies or tokens

For security, we recommend that you configure rate limiting rules to prevent token abuse through multiple uses per unique reCAPTCHA action-token, session-token, or exemption cookie. The following table illustrates how you can identify a reCAPTCHA exemption cookie or token as the key in a rate limiting rule.

Resource | `enforce_on_key` | `enforce_on_key_name`  
---|---|---  
Exemption cookie | `HTTP-COOKIE` | `recaptcha-ca-e`  
Action-token | `HTTP-HEADER` | `X-Recaptcha-Token`  
Session-token | `HTTP-COOKIE` | `recaptcha-ca-t`  
  
You can throttle requests or ban clients that depend on the same exemption cookie or token, and that exceed the configured threshold. For more information about rate limiting parameters, see [Apply rate limiting](https://docs.cloud.google.com/armor/docs/rate-limiting-overview).

#### Rate limiting examples

First, suppose that you only use manual challenges on selected URLs (`/login.html`, for example) on your site. To accomplish this, configure security policy rules as follows:

  * Rule 1: If there is a valid exemption cookie attached with the request and the number of uses for the exemption cookie is under your defined threshold, allow the request.
  * Rule 2: Redirect the request for reCAPTCHA assessment.

[ ![Flowchart for enforcing manual challenges.](https://docs.cloud.google.com/static/armor/images/recaptcha-redirect.svg)](https://docs.cloud.google.com/static/armor/images/recaptcha-redirect.svg) Enforce manual challenges (click to enlarge).

Second, suppose that you only use action-tokens or session-tokens on your site. For example, you might use action-tokens to protect high-profile user actions, like `/login.html`. To do this, take actions based on the score from the action-token as follows:

  * Rule 1: When the score from the action-token is higher than a predefined threshold (`0.8`, for example), allow the request if the number of uses for the action-token is under your defined threshold.
  * Rule 2: Deny the request.

[ ![Enforce reCAPTCHA action-token assessment.](https://docs.cloud.google.com/static/armor/images/recaptcha-action.svg)](https://docs.cloud.google.com/static/armor/images/recaptcha-action.svg) Enforce reCAPTCHA action-token assessment (click to enlarge).

You can configure similar security policy rules to enforce reCAPTCHA session-token assessment.

Third, suppose that you combine action-tokens or session-tokens with manual challenges on selected URLs (like `/login.html`) on your site, and you want to take actions based on the score from the action-token. And you want to give the user a second chance by solving challenges if the score is not satisfactory enough. To do this, configure security policy rules as follows:

  * Rule 1: When the score from the action-token is higher than a predefined threshold (`0.8`, for example), allow the request if the number of uses for the action-token is under your defined threshold.
  * Rules 2 and 3: When the score from the action-token is higher than a different predefined threshold (`0.5`, for example), redirect the request for reCAPTCHA assessment unless there is a valid exemption cookie attached to the request and the number of uses for the exemption cookie is under your defined threshold.
  * Rule 4: Deny the request.

[ ![Enforce reCAPTCHA action-token assessment with manual challenges.](https://docs.cloud.google.com/static/armor/images/recaptcha-action-and-redirect.svg)](https://docs.cloud.google.com/static/armor/images/recaptcha-action-and-redirect.svg) Enforce reCAPTCHA action-token assessment with manual challenges (click to enlarge).

You can configure similar security policy rules to enforce reCAPTCHA session-token assessment with manual challenges.

If you don't tune the rate limiting rules, Cloud Armor imposes no limit on the number of uses for each reCAPTCHA exemption cookie, action-token, and session-token. For action-tokens, we recommend using a low threshold (`1`, for example) and a high time interval (`30` minutes for example, since action-tokens are valid for 30 minutes). We recommend that you derive the threshold based on your traffic statistics.

## What's next

  * [Configure bot management](https://docs.cloud.google.com/armor/docs/configure-bot-management)
  * [View the rules language reference](https://docs.cloud.google.com/armor/docs/rules-language-reference)
  * [View logs](https://docs.cloud.google.com/armor/docs/request-logging)
  * [Troubleshoot problems](https://docs.cloud.google.com/armor/docs/troubleshooting#recaptcha)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
