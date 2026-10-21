---
url: https://docs.cloud.google.com/recaptcha/docs/select-challenge-types/
title: Challenge types \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:49:18.677910+00:00
---

# Challenge types  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/select-challenge-types/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Guides ](https://docs.cloud.google.com/recaptcha/docs/implementation-workflow)



Send feedback 

#  Challenge types Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the types of Fraud Defense verification challenges that you can integrate into your websites or applications to help you distinguish humans from automated threats. Fraud Defense provides visual, audio, and QR code challenges.

## Visual challenges

Visual challenges require users to identify and select specific objects within a grid of images.

To complete a visual challenge, users read the prompt and select image squares that match it (for example, with traffic lights). Users might be presented with additional images.

## Audio challenges

Audio challenges are an accessibility option for users who cannot or prefer not to complete a visual challenge. Audio challenges work with major screen readers such as ChromeVox, JAWS, NVDA, and VoiceOver.

Users play or download an audio snippet and enter the numbers that they hear in the text field.

## QR code challenges

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The QR code challenge is an AI-resistant, mobile-centric verification mechanism. Visual or audio challenges can sometimes be circumvented by sophisticated automation or click farms. The QR code challenge offers enhanced security by shifting the verification process to the user's mobile phone. This separation makes it more difficult for attackers to launch scaled attacks.

When a QR code challenge is triggered, two devices work together to complete verification:

  1. **Browsing device:** Displays a QR code in the browser or application window.
  2. **Mobile device:** The user scans the displayed QR code using their mobile phone and perform verification in the trusted execution environment of the mobile device.



The verification process requires minimal user setup on Android and iOS devices. Android devices have the verification software built-in. iOS devices use [Apple App Clips](https://developer.apple.com/documentation/appclip), which eliminates the need to install a separate application. QR code challenges also work directly on mobile browsers and WebViews, where the QR code is replaced with a button that directly starts the mobile verification flow.

**Note:** To use the QR code feature, contact the Fraud Defense team at [fraud-defense@google.com](mailto:fraud-defense@google.com) and provide the Universal key for your project so that it can be added to the QR code allowlist.

When you integrate QR code challenges into your websites or applications, users complete the following high-level steps to get access:

### Android

**Prerequisite** : Google Play services version 25.41.30 or later.

**Steps** :

  1. Scan the QR code using an Android device.
  2. Press **Confirm verification**.
  3. Press **Done**.



### iOS

**Prerequisites** :

  * iOS 16 or later.
  * [reCAPTCHA app](https://apps.apple.com/ca/app/recaptcha/id6746882749) (Apple App Store) or iOS App Clip.



**Steps** :

  1. Scan the QR code using an iOS device.
  2. Press **Done**.



## Challenge difficulty levels

Visual and audio challenges offer difficulty levels to balance user friction with security. When a challenge is triggered (for example, when a challenge policy rule matches), Fraud Defense begins by presenting a visual challenge. You cannot choose to serve an audio challenge initially when a rule matches because challenge type selection is not supported. Users can choose to switch to an audio challenge directly from the verification widget.

**Note:** Challenge difficulty levels don't apply to QR code challenges.

Because challenges start as visual by default, the difficulty level that you configure applies directly to visual challenges. If a user switches to an audio challenge during verification, the configured difficulty level maps to the audio challenge as follows:

  * **Easy (`USABILITY`)**: Serves an easy visual challenge. If the user switches to an audio challenge, an easy audio challenge is presented.
  * **Medium (`BALANCE`)**: Serves a medium visual challenge. If the user switches to an audio challenge, an easy audio challenge is presented because a medium difficulty level is not available for audio challenges.
  * **Hard (`SECURITY`)**: Serves a hard visual challenge. If the user switches to an audio challenge, a hard audio challenge is presented.



## Configure challenges with Policy Engine

If your organization uses Fraud Defense [Policy Engine](https://docs.cloud.google.com/recaptcha/docs/policy-engine), you can create custom rules ([`challenge_rule_groups`](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/Policy#ChallengeRuleGroup)) to deterministically trigger challenges based on specific [request conditions](https://docs.cloud.google.com/recaptcha/docs/challenge-policies#condition-syntax).

## What's next

  * [Set up Policy Engine with a Universal key](https://docs.cloud.google.com/recaptcha/docs/policy-engine).
  * To assess the Fraud Defense response token, see [Create assessments for websites](https://docs.cloud.google.com/recaptcha/docs/create-assessment-website).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
