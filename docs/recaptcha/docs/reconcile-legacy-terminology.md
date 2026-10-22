---
url: https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology/
title: Reconcile Admin Console and Google Cloud console terminology \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:21.398883+00:00
---

# Reconcile Admin Console and Google Cloud console terminology  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/reconcile-legacy-terminology/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Reconcile Admin Console and Google Cloud console terminology Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the differences in terminology and key management between the legacy reCAPTCHA Admin Console and the Google Cloud console. It also explains how to retrieve reCAPTCHA site keys and secret keys required by third-party plugins like WordPress integrations.

## Map legacy terminology to the Google Cloud console

Many content management system (CMS) plugins refer to reCAPTCHA types using legacy naming conventions, like `v2 Checkbox`, `v2 Invisible`, and `v3`. The Google Cloud console uses platform-based descriptors, instead of version numbers.

The following table maps legacy terminology to the Google Cloud console terminology:

Admin Console terminology | Google Cloud console terminology | Verification mechanism  
---|---|---  
Score based (v3) | Website • score | Frictionless, score-based verification.  
Challenge (v2) | Website • checkbox | Requires user to click an "I'm not a robot" challenge.  
N/A | Website • policy-based challenge | Challenge configured based on user-defined threshold.  
N/A | iOS | iOS mobile key without challenge.  
N/A | Android | Android mobile key without challenge.  
Invisible (v2) | Website • Invisible with challenge fallback | May show captcha challenges after risk analysis.  
**Note:** You cannot create new Invisible (v2) keys using the Google Cloud console. Create a standard Web key instead.

### Verify your key type in the Google Cloud console

To verify the type of a key in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. Switch from **Cards** view to **Table** view.

  4. Locate the **Platform details** column to see descriptors such as `Website • score`.




Alternatively, in the default **Cards** view, click **Key details** for a specific key, and then select **Edit key**. The **Type** field displays the configuration.

## Find the site key and secret key

Third-party plugins often require a site key and a secret key for reCAPTCHA integration.

  * **Site key** : In the Google Cloud console, the **Key ID** corresponds to the site key.
  * **Secret key** : The Google Cloud console doesn't display the secret key by default because Google Cloud authentication typically uses API keys or Identity and Access Management roles. However, you can retrieve the legacy secret key for plugins that require it. Some third-party libraries or documentation might refer to the legacy secret key as a **private key**.



### Retrieve the secret key in the Google Cloud console

To retrieve the secret key, do the following:

  1. In the Google Cloud console, go to the **Fraud Defense** page.

[Go to Fraud Defense](https://console.cloud.google.com/security/recaptcha)

  2. Select the **Keys** tab.

  3. In the **reCAPTCHA Keys** section, go to the key that you need the secret key for.

     * If you're in the **Cards** view, click **Key details** on the key card. The **Key ID** is displayed at the top of the page.
     * If you're in the **Table** view, the **Key ID** is visible in the table. Click the key to go to its details page.
  4. The **Key ID** displayed at the top of the page is your **site key**.

  5. Go to the **Integration** tab.

  6. Depending on the key's status:

     * If the key is configured for legacy use, click **Use Legacy Key**.
     * If the key isn't integrated with a legacy service, click **Integrate with a third-party service or plugin**.
  7. A dialog appears with your **secret key**. Copy this value securely. Treat this secret as sensitive data.




## Integrate using assessments

**Important:** For custom integrations that don't use third-party plugins, use the `CreateAssessment` method instead of the legacy `SiteVerify` method. 

The `CreateAssessment` method provides detailed risk analysis and reason codes, and enables access to advanced Fraud Defense features. You can call the `CreateAssessment` method using the [reCAPTCHA client libraries](https://docs.cloud.google.com/recaptcha/docs/libraries) or the REST API.

For more information, see [Create an assessment for your website](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).

### Legacy `SiteVerify` method

Although we recommend the `CreateAssessment` method for new and custom integrations, some existing systems or third-party plugins still rely on the legacy `SiteVerify` method. This method requires a **secret key** associated with your reCAPTCHA key.

If you need to integrate with a system that requires the legacy `SiteVerify` API, see [Verify user response tokens with legacy SiteVerify](https://docs.cloud.google.com/recaptcha/docs/verify).

## What's next

  * [Create keys for websites](https://docs.cloud.google.com/recaptcha/docs/create-key-website)
  * [Create an assessment for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
