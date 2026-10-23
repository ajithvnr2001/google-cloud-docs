---
url: https://docs.cloud.google.com/recaptcha/docs/deprecation-policy-mobile/
title: Deprecation and shutdown policy for mobile SDKs \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:53.284089+00:00
---

# Deprecation and shutdown policy for mobile SDKs  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/deprecation-policy-mobile/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Deprecation and shutdown policy for mobile SDKs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the deprecation and shutdown policy, and schedule for reCAPTCHA Mobile SDK versions. With the release of a new SDK, earlier versions will be deprecated and given a shutdown date. When an SDK version is shut down, calls to `projects.assessments.create` will start to receive an error message indicating that this version is no longer usable. Additionally, submissions to the Google Play Store can be blocked if they contain a shutdown SDK version. The iOS App Store does not have such a mechanism.

The latest SDKs offer the best protection and highest performance, and they address bugs that might exist in previous versions. Although Google makes every effort to enhance the detection offered by previous SDK versions, some capabilities and enhancements require a new SDK. For information about the enhancements and fixes, see the [release notes](https://docs.cloud.google.com/recaptcha/docs/release-notes).

## Definitions

  * **Supported:** These SDK versions will continue to function in production for deployed applications. Due to possible changes in the iOS App Store, Google Play Store, and other mobile distribution platforms, supported versions might not be submittable in new versions of an app. This includes changes to required compilers and privacy or disclosure rules.

  * **Deprecated:** These SDKs will continue to function, but they will be shut down in the future. We recommend upgrading to a new version of the SDK as soon as possible.

  * **Shut down:** When an SDK is shut down, it might return errors in calls to `projects.assessments.create`, `getClient()`, `execute()`, and other SDK methods. You should upgrade immediately to a supported version.




## Schedule

The following table lists the shutdown date for each version. We recommend that you migrate to the newest version as soon as possible after its release.

Version | Status | First release | Last release | Deprecation | Shut down  
---|---|---|---|---|---  
18.10 | Supported | Aug 24, 2026 | Aug 24, 2026 | Q4 2027 | Q1 2030  
18.9 | Supported | Jan 07, 2026 | [Jun 25, 2026](https://docs.cloud.google.com/recaptcha/docs/release-notes#June_25_2026) | Q4 2027 | Q1 2030  
18.8 | Supported | Jun 04, 2025 | [Nov 15, 2025](https://docs.cloud.google.com/recaptcha/docs/release-notes#December_01_2025) | Q4 2026 | Q1 2029  
18.7 | Supported | Oct 10, 2024 | [May 12, 2025](https://docs.cloud.google.com/recaptcha/docs/release-notes#May_12_2025) | Q3 2026 | Q3 2028  
18.6 | Deprecated | Jun 19, 2024 | [Sep 10, 2024](https://docs.cloud.google.com/recaptcha/docs/release-notes#September_10_2024) | Q4 2025 | Q1 2028  
18.5 | Deprecated | Feb 21, 2024 | [May 29, 2024](https://docs.cloud.google.com/recaptcha/docs/release-notes#May_29_2024) | Q2 2025 | Q2 2027  
18.4 | Deprecated | Nov 13, 2023 | [Feb 21, 2024](https://docs.cloud.google.com/recaptcha/docs/release-notes#February_21_2024) | Q1 2025 | Q1 2027  
18.3 | Deprecated | Aug 16, 2023 | [Aug 16, 2023](https://docs.cloud.google.com/recaptcha/docs/release-notes#August_16_2023) | Q1 2024 | Q1 2027  
18.2 | Deprecated | May 01, 2023 | [Jul 05, 2023](https://docs.cloud.google.com/recaptcha/docs/release-notes#July_05_2023) | Q1 2024 | Q1 2027  
18.1 | Shutdown | Feb 01, 2023 | [Apr 06, 2023](https://docs.cloud.google.com/recaptcha/docs/release-notes#April_06_2023) | Q1 2024 | Q2 2026  
18.0 | Shutdown | Oct 31, 2022 | [Nov 30, 2022](https://docs.cloud.google.com/recaptcha/docs/release-notes#November_30_2022) | Q1 2024 | Q2 2026  
17.1 | Shutdown | May 29, 2024 | May 29, 2024 | Q3 2024 | Q2 2026  
17.0 | Shutdown | Dec 09, 2021 | May 18, 2022 | Q3 2024 | Q2 2026  
16.1 | Shutdown | Jun 01, 2021 | Jun 01, 2021 | Q3 2024 | Q2 2026  
16.0 | Shutdown | Apr 15, 2020 | Jun 16, 2021 | Q3 2024 | Q2 2026  
SafetyNet reCAPTCHA | Shutdown |  | [Jan 05, 2022](https://developer.android.com/privacy-and-security/safetynet/recaptcha) | Q3 2024 | Q3 2025  
  
## Visual challenges

reCAPTCHA SDK versions 16 and higher don't have visual challenges (reCAPTCHA v2) such as those found in reCAPTCHA SafetyNet. We no longer recommend the use of visual challenges in mobile applications, but for customers that still want to enable them we provide [sample code](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/tree/main/examples) to use visual challenges in a WebView.

## Pricing

Upgrading from SDK versions v16, v17, or v18 does not affect your pricing. Unlike reCAPTCHA SafetyNet, which was subject to strict quota limits with no option to exceed them, Google Cloud Fraud Defense lets you enable billing to scale beyond standard quotas.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
