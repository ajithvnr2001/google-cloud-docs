---
url: https://docs.cloud.google.com/recaptcha/docs/troubleshoot-recaptcha-issues/
title: Troubleshoot reCAPTCHA integration issues \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:44:15.579171+00:00
---

# Troubleshoot reCAPTCHA integration issues  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/troubleshoot-recaptcha-issues/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Troubleshoot reCAPTCHA integration issues Stay organized with collections  Save and categorize content based on your preferences. 

This document lists common reCAPTCHA integration issues that developers might encounter when using reCAPTCHA in their environment.

**Note:** If you're an end user experiencing issues with reCAPTCHA visual challenges, ensure that your browser is up to date or try a different browser. If the problem persists, contact the website's support team.

## Invalid site key

If you see the `Invalid site key` error, your reCAPTCHA site key is no longer valid. [Create a new key](https://docs.cloud.google.com/recaptcha/docs/create-key-website) and [install it on your web pages](https://docs.cloud.google.com/recaptcha/docs/instrument-web-pages).

## Keys migration failure

Site keys can fail to migrate in one of the following scenarios:

  * You've exceeded the number of projects that you or your organization can create.

To resolve this, you can reuse an existing project, [request an increase in project creation quota](https://support.google.com/cloud/answer/7283050), or wait for the automated migration to complete.

  * Your workspace organization has restricted creating of new Google Cloud projects.

To turn on the Google Cloud service in the Google Admin console, contact your administrator. For more information, see [Turn Google Cloud on or off for users](https://support.google.com/a/answer/182442).




## SecurityError: blocked a frame with origin "https://www.google.com" from accessing a frame with origin "&ltyour domain&gt"

This typically occurs if the reCAPTCHA widget HTML element is programmatically removed sometime after the end user clicks on the checkbox. We recommend using the [grecaptcha.enterprise.reset()](https://docs.cloud.google.com/recaptcha/docs/api-ref-checkbox-keys#grecaptchaenterprisereset) JavaScript function to reset the reCAPTCHA widget.

## Localhost is not in the list of supported domains

Localhost domains are not supported by default. If you want to continue supporting them for development, you can add them to the list of supported domains for your site key. Go to the [Google Cloud console](https://console.cloud.google.com/security/recaptcha) to update your list of supported domains. We advise to use separate keys for development and production, and to only allow localhost on your development site key.

## reCAPTCHA returned BROWSER_ERROR when creating an assessment

`BROWSER_ERROR` tokens occur when the reCAPTCHA script cannot perform an `execute` operation. In most cases, this is due to a client-side network failure or timeout. You must retry `execute()` using the JavaScript.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
