---
url: https://docs.cloud.google.com/recaptcha/docs/verify/
title: Verify user response tokens with legacy SiteVerify \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:50:30.855613+00:00
---

# Verify user response tokens with legacy SiteVerify  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/verify/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Verify user response tokens with legacy SiteVerify Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** For all new and custom integrations, use the [`CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website) method instead of the legacy `SiteVerify` endpoint (`https://www.google.com/recaptcha/api/siteverify`). The `CreateAssessment` method provides granular risk analysis, reason codes, and access to advanced Google Cloud Fraud Defense features. To upgrade an existing `SiteVerify` integration, see [Use Fraud Defense features after migration](https://docs.cloud.google.com/recaptcha/docs/using-features). 

This page explains how to verify a user's response to a reCAPTCHA challenge from your application's backend using the legacy `SiteVerify` API endpoint (`https://www.google.com/recaptcha/api/siteverify`). Use this endpoint only if you're maintaining a legacy integration or third-party plugin that can't use [`CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).

## Before you begin

To call the `SiteVerify` endpoint, you need your key's legacy **secret key**. To find the secret key in the Google Cloud console, see [Retrieve the secret key in the Google Cloud console](https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology#retrieve-secret-key-in-console). Keep your secret key safe on your backend server and never expose it in client-side code.

## Retrieve the user's response token

Legacy web integrations load the non-enterprise JavaScript API (`https://www.google.com/recaptcha/api.js`), which provides methods on the `grecaptcha` object instead of `grecaptcha.enterprise`. You can retrieve the user's response token on your frontend in one of the following ways:

  * From the `g-recaptcha-response` POST parameter when the user submits a form on your site.
  * By calling `grecaptcha.getResponse(opt_widget_id)` after the user completes a reCAPTCHA v2 challenge. This method returns the response token as a string, or an empty string if the challenge isn't completed. The optional `opt_widget_id` parameter specifies the widget ID returned by `grecaptcha.render()`; if omitted, it defaults to the first widget created.
  * As a string argument passed to your callback function when the user completes a challenge, if you specify the callback function name in either the `data-callback` attribute of the `g-recaptcha` HTML element or the `callback` parameter of the `grecaptcha.render(container, parameters)` method.
  * From the resolved value of the `Promise` returned by `grecaptcha.execute(site_key, {action: action_name})` for score-based (v3) keys.



The legacy `grecaptcha` methods (`render`, `getResponse`, `execute`, `ready`, and `reset`) and `g-recaptcha` tag attributes use the same parameters as the `grecaptcha.enterprise` equivalents. For parameter details, see the [JavaScript API reference for reCAPTCHA](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys).

To migrate to the updated reCAPTCHA JavaScript API, see [Migrate the reCAPTCHA JavaScript API](https://docs.cloud.google.com/recaptcha/docs/using-features#instrument-site).

## Token restrictions

Each reCAPTCHA user response token is valid for two minutes, and you can verify each token only _once_ to prevent replay attacks. Verify the response token with reCAPTCHA within two minutes of receiving it. If you need a new token, run the reCAPTCHA verification again.

## API request

Send a request with the following endpoint and method:

  * **URL** : `https://www.google.com/recaptcha/api/siteverify` (or `https://www.recaptcha.net/recaptcha/api/siteverify` if `www.google.com` isn't accessible; see [Use reCAPTCHA globally](https://docs.cloud.google.com/recaptcha/docs/faq#can-i-use-recaptcha-enterprise-globally))
  * **Method** : `POST`



Include the following POST parameters in the request:

POST parameter | Description  
---|---  
`secret` | Required. The shared secret key between your site and reCAPTCHA.  
`response` | Required. The user response token provided by the reCAPTCHA client-side integration on your site.  
`remoteip` | Optional. The user's IP address.  
  
## API response

The `SiteVerify` endpoint returns a JSON object.

For web integrations (score-based v3, checkbox v2, or invisible v2 keys), the response has the following format:
    
    
    {
      "success": true|false,      // whether this request was a valid reCAPTCHA token for your site
      "score": number,            // the score for this request (0.0 - 1.0) for score-based (v3) keys
      "action": string,           // the action name for this request (important to verify)
      "challenge_ts": timestamp,  // timestamp of the challenge load (ISO format yyyy-MM-dd'T'HH:mm:ssZZ)
      "hostname": string,         // the hostname of the site where the reCAPTCHA was solved
      "error-codes": [...]        // optional
    }
    

**Important:** If you specify an `action` name on the client, verify that the `action` field in the `SiteVerify` response matches the expected action name on your server. If you disable domain or package name verification in your key settings, you **must** check the `hostname` or `apk_package_name` field on your server and reject tokens from unexpected sources.**Note:** When a project without an active billing account exceeds the monthly free quota of 10,000 assessments, `SiteVerify` fails open by returning HTTP `200 OK` with `success: true`, a static `score` of `0.9`, and an error message `"Over free quota."`. For details, see [Endpoint behavior when exceeding the monthly free quota](https://docs.cloud.google.com/recaptcha/quotas#quota_exceeded_behavior).

### Error code reference

The following table describes the error codes that can appear in the `error-codes` array:

Error code | Description  
---|---  
`missing-input-secret` | The `secret` parameter is missing.  
`invalid-input-secret` | The `secret` parameter is invalid or malformed.  
`missing-input-response` | The `response` parameter is missing.  
`invalid-input-response` | The `response` parameter is invalid or malformed.  
`bad-request` | The request is invalid or malformed.  
`timeout-or-duplicate` | The response is no longer valid because it expired or was already used.  
  
## What's next

  * [Migrate from `SiteVerify` to `CreateAssessment`](https://docs.cloud.google.com/recaptcha/docs/using-features)
  * [Create assessments for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)
  * [Interpret assessments for websites](https://docs.cloud.google.com/recaptcha/docs/interpret-assessment-website)
  * [Reconcile Admin Console and Google Cloud console terminology](https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
