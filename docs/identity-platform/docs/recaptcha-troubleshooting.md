---
url: https://docs.cloud.google.com/identity-platform/docs/recaptcha-troubleshooting/
title: Troubleshooting the Identity Platform integration with the reCAPTCHA Enterprise API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:23.486397+00:00
---

# Troubleshooting the Identity Platform integration with the reCAPTCHA Enterprise API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/recaptcha-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting the Identity Platform integration with the reCAPTCHA Enterprise API

This document provides guidance for troubleshooting potential issues that might arise when using the Identity Platform integration with the reCAPTCHA Enterprise API, including the reCAPTCHA bot protection and reCAPTCHA SMS defense features.

## Integration onboarding troubleshooting

Your users might be experiencing issues due to mistakes when onboarding with the Identity Platform integration with the reCAPTCHA Enterprise API. Some common reasons might include the following:

  * You might have missed a step in the Identity Platform integration with the reCAPTCHA Enterprise API set up. For example, neglecting to set up the service account or enabling the reCAPTCHA Enterprise API on the project. Ensure you've completed all the integration requirements. For set up instructions, see [Integrate Identity Platform with the reCAPTCHA Enterprise API](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise).
  * If you are [bringing your own key](https://docs.cloud.google.com/identity-platform/docs/recaptcha-byok) to use with reCAPTCHA, the corresponding reCAPTCHA key you uploaded might not be valid or might have stopped working. Verify that the key is working and accessible by Identity Platform.
  * Users might be using an outdated version of your app. Make sure you provide an updated version of your app that uses the client SDK, and ask your users to update their app. To set up the client SDK for your app, see [Configure the client SDK](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise#configure-sdk).



## Users can't authenticate through reCAPTCHA Enterprise API supported flows

If you are experiencing issues with reCAPTCHA Enterprise API supported flows, such as reCAPTCHA bot protection or reCAPTCHA SMS defense, see the following sections for feature specific guidance.

### reCAPTCHA bot protection troubleshooting

The following topics describe possible issues that you might face when using bot protection and how you might solve them.

#### Users can't authenticate when using bot protection for the email-password or phone providers

If you have determined that the Identity Platform integration with the reCAPTCHA Enterprise API was set up correctly, users might be blocked from performing authentication actions through the email-password or phone providers based on your current configuration. For example, users might be unable to perform the following actions:

  * Sign-in, sign-up, or reset a password through an email address.
  * Request an SMS code to sign in through a phone number.
  * Enroll in or sign in with SMS-based multi-factor authentication.



To resolve these authentication issues, try the following:

  * If user requests are failing with `ERROR_CAPTCHA_CHECK_FAILED`, consider a more permissive configuration by adjusting the thresholds you've set for `managedRules`. Any requests that score below the threshold you set will be considered a bot. For example, if you set a threshold of `0.6`, reCAPTCHA will fail any request with a `0.5` or lower. Therefore, the higher you set the score, the stricter the rules will be.
  * Ask the user to try a different device, browser, or network.
  * Revert to audit mode and monitor metrics before re-enabling enforcement mode.



### reCAPTCHA SMS defense troubleshooting

The following topics describe possible issues you might face when using reCAPTCHA SMS defense and how you might solve them.

#### Users can't authenticate when using reCAPTCHA SMS defense for the phone provider

If you have determined that the Identity Platform integration with the reCAPTCHA Enterprise API was set up correctly, users might be blocked from performing SMS-based authentication actions through the phone provider based on your current configuration. For example, users might be unable to request an SMS code to sign in with a phone number or enroll in or sign in with multi-factor authentication. This can happen if the reCAPTCHA SMS defense score you set is too strict.

To resolve this, consider a more permissive configuration by adjusting the threshold you've set for `tollFraudManagedRules`. Any score above the threshold you set will be considered SMS toll fraud. For example, if you set a threshold of `0.3`, reCAPTCHA will fail any request with a `0.4` or higher. Therefore, the lower you set the score, the stricter the rules will be.

If this is an issue, we recommend setting your enforcement mode to audit to test and monitor the reCAPTCHA metrics emitted by your project. This will help you ensure that your app is receiving acceptable user traffic before enabling enforcement again.

## What's next

  * Learn more about [monitoring reCAPTCHA metrics](https://docs.cloud.google.com/identity-platform/docs/recaptcha-metrics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
