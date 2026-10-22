---
url: https://docs.cloud.google.com/recaptcha/docs/using-features/
title: Use Fraud Defense features after migration \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:13.246430+00:00
---

# Use Fraud Defense features after migration  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/using-features/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Use Fraud Defense features after migration Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Fraud Defense features, such as Multi-factor authentication (MFA) and Password defense, by migrating your existing reCAPTCHA integration from the legacy `SiteVerify` method to the `CreateAssessment` method. Migrating to the `CreateAssessment` method involves instrumenting the web pages and migrating the backend calls.

## Explore Fraud Defense features

After you migrate to using the `CreateAssessment` method, you can use additional Fraud Defense features, such as the following:

  * **Account defense** : Helps you protect user accounts from compromise and fraudulent activities, such as account takeover (ATO) attempts.
  * **Transaction defense** : Helps you protect payment transactions from online fraud, such as carding attacks and use of stolen payment instruments.
  * **Password defense** : Lets you check if a username and password combination that is provided by a user has appeared in a known data breach or password leak database.
  * **Multi-factor authentication (MFA)** : Helps you verify your users' identities by sending a verification code by email.



## Instrument the web pages

To instrument the web pages with the correct reCAPTCHA scripts and calls, do the following:

  1. Verify that you have the following script included in your web pages: `https://www.google.com/recaptcha/api.js`.
  2. In your web pages, replace `https://www.google.com/recaptcha/api.js` with `https://www.google.com/recaptcha/enterprise.js`.

**Note:** If your web pages have the `https://www.recaptcha.net/recaptcha/api.js` script, then replace it with `https://www.recaptcha.net/recaptcha/enterprise.js`.
  3. If you programmatically invoke the API, then replace the following calls:

     * `grecaptcha.execute()` -> `grecaptcha.enterprise.execute()`
     * `grecaptcha.getResponse()` -> `grecaptcha.enterprise.getResponse()`
     * `grecaptcha.ready()` -> `grecaptcha.enterprise.ready()`
     * `grecaptcha.render()` -> `grecaptcha.enterprise.render()`
     * `grecaptcha.reset()` -> `grecaptcha.enterprise.reset()`



## Migrate the backend calls

To use Fraud Defense features, you must migrate your backend calls to the new endpoints and set up authentication:

  1. Replace backend calls to `https://www.google.com/recaptcha/api/siteverify` with equivalent calls to `recaptchaenterprise.googleapis.com`. For the complete URL and the POST data format, see [Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).

  2. Set up authentication to Fraud Defense. 

The authentication method you choose depends on the environment where Fraud Defense is set up. The following table helps you choose the appropriate authentication method and the supported interface to set up authentication:

Environment | Interface | Authentication method  
---|---|---  
Google Cloud | 
     * REST
     * Client libraries
| Use [attached service accounts](https://docs.cloud.google.com/recaptcha/docs/authentication#on-gcp).  
On-premises or a different cloud provider | REST | Use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).  
Client libraries | Use the following:
     * For Python or Java, use [API keys](https://docs.cloud.google.com/docs/authentication/api-keys) or [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises). If you want to use API keys, then we recommend securing the API keys by [applying API key restrictions](https://docs.cloud.google.com/docs/authentication/api-keys#api_key_restrictions).
     * For other languages, use [Workload Identity Federation](https://docs.cloud.google.com/docs/authentication/set-up-adc-on-premises).  



## What's next

  * [Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)
  * [Monitor reCAPTCHA keys](https://docs.cloud.google.com/recaptcha/docs/monitor-keys)
  * [Detect password leaks and breached credentials](https://docs.cloud.google.com/recaptcha/docs/check-passwords)
  * [Detect and prevent account-related fraudulent activities on websites](https://docs.cloud.google.com/recaptcha/docs/account-defender)
  * [Protect payment transactions with Transaction defense](https://docs.cloud.google.com/recaptcha/docs/fraud-prevention)
  * [Configure multi-factor authentication](https://docs.cloud.google.com/recaptcha/docs/integrate-account-verification)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
