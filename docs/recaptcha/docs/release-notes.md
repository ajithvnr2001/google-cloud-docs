---
url: https://docs.cloud.google.com/recaptcha/docs/release-notes/
title: Fraud Defense release notes \u00a0|\u00a0 Google Cloud Fraud Defense \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:37:41.482634+00:00
---

# Fraud Defense release notes  |  Google Cloud Fraud Defense  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recaptcha/docs/release-notes/

reCAPTCHA is a part of Google Cloud Fraud Defense. For more information, see [Google Cloud Fraud Defense](https://docs.cloud.google.com/security/products/fraud-defense). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Cloud Fraud Defense ](https://docs.cloud.google.com/recaptcha/docs)
  * [ Resources ](https://docs.cloud.google.com/recaptcha/docs/resources)



Send feedback 

#  Fraud Defense release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Fraud Defense. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/recaptcha-enterprise-release-notes.xml) directly. 

## September 01, 2026

Change

Fraud Defense Mobile SDK v18.9.3 is available for Android. This version includes detection and performance enhancements.

## August 25, 2026

Change

Fraud Defense Mobile SDK v18.10.0-beta01 is available for iOS. This version includes the following:

  * Adds support for macOS desktop and tvOS.
  * Improvements to networking consumption.
  * Improvements to latency and reliability.



## July 29, 2026

Feature

The Agent overview dashboard is available on the Google Cloud Fraud Defense home page. This dashboard helps you monitor and analyze automated agent traffic on your site by distinguishing verified agents from suspected agents.

For more information, see [Monitor agent traffic](https://docs.cloud.google.com/recaptcha/docs/monitor-agents).

## July 24, 2026

Feature

**Preview** : [Policy Engine](https://docs.cloud.google.com/recaptcha/docs/policy-engine), [Universal keys](https://docs.cloud.google.com/recaptcha/docs/install-universal-keys-web-pages), and [challenge policies](https://docs.cloud.google.com/recaptcha/docs/challenge-policies) are available in [Preview](https://docs.cloud.google.com/products#product-launch-stages) for Google Cloud Fraud Defense.

  * Policy Engine lets you perform frontend JavaScript integration using AutoExecute and configure custom rules to selectively trigger CAPTCHA challenges based on risk score, IP addresses, user agents, ASNs, or verified bot identities.
  * A new AI-resistant [QR code challenge](https://docs.cloud.google.com/recaptcha/docs/select-challenge-types#qr-code-challenges) is available.



For more information about the types of challenges that are available, see [Challenge types](https://docs.cloud.google.com/recaptcha/docs/select-challenge-types).

## June 29, 2026

Change

reCAPTCHA Mobile SDK v18.9.2 is available for Android. This version includes minor bug fixes.

## June 04, 2026

Change

reCAPTCHA Mobile SDK v18.9.1 is available for iOS. This version fixes symbol collisions with libraries using Objective-C protos.

## June 01, 2026

Change

reCAPTCHA Mobile SDK v18.9.1 is available for Android. This version fixes an issue that caused package name collisions when building projects using Android Gradle Plugin version 9.0 or higher.

## May 13, 2026

Change

reCAPTCHA Mobile SDK v18.9.0 is available for Android. This version includes the following updates:

  * Improvements to SDK latency and reliability.

  * Score distribution calibration improvements.

  * Removes the need for desugaring and raises the minimum supported Android API level to 24 (Android 7.0).




## May 01, 2026

Change

reCAPTCHA Mobile SDK v18.9.0 is available for iOS. This version includes the following:

  * Reliability improvements and bug fixes.

  * Score distribution calibration and improvements for better bot detection. We recommend that you review your score threshold and adjust it if you experience a high number of false positives.

  * Beta support for visionOS.

  * Beta support for arm64e and Enhanced Security Features.




## April 22, 2026

Feature

reCAPTCHA is part of Google Cloud Fraud Defense, a suite of security products designed to protect your websites and applications from fraud and abuse. This change does not affect existing reCAPTCHA functionality. For more information, see [Google Cloud Fraud Defense](https://cloud.google.com/security/products/fraud-defense).

## April 01, 2026

Change

reCAPTCHA Mobile SDK v18.9.0-beta02 is available for iOS. This version includes the following:

  * Reliability improvements and bug fixes.
  * Score distribution calibration and improvements for enhanced bot detection.
  * Beta support for visionOS.
  * Beta support for the arm64e architecture and enhanced security features.



## March 27, 2026

Change

reCAPTCHA Mobile SDK v18.9.0-beta02 is available for Android. This version includes the following:

  * Reliability improvements and bug fixes
  * Score distribution calibration and improvements



## January 30, 2026

Change

The updated reCAPTCHA Mobile SDK improves the risk score. You should review and adjust your reCAPTCHA action thresholds as needed.

## January 14, 2026

Change

reCAPTCHA Mobile SDK v18.9.0-beta01 is available for iOS. This version includes improvements to SDK latency and reliability.

## January 06, 2026

Change

reCAPTCHA Mobile SDK v18.9.0-beta01 is available for Android. This version includes improvements to SDK latency and reliability.

## December 01, 2025

Change

reCAPTCHA Mobile SDK v18.8.2 is available for iOS. This version fixes a race condition affecting multiple simultaneous calls to execute.

## October 28, 2025

Feature

reCAPTCHA policy-based challenge keys are available in [GA](https://cloud.google.com/products#product-launch-stages). With policy-based challenge keys, you can configure reCAPTCHA to deterministically trigger CAPTCHA challenges based on a score threshold and challenge difficulty. For more information about the policy-based challenge keys, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).

## October 22, 2025

Change

reCAPTCHA Mobile SDK v18.8.1 is available for iOS. This version fixes an issue with iOS 26 screen time showing use from recaptcha.net

## September 17, 2025

Change

reCAPTCHA Mobile SDK v18.8.0 is available for Android. This version contains reliability improvements and bug fixes.

## September 15, 2025

Change

reCAPTCHA Mobile SDK 18.8.0 is available for iOS. This version contains the following changes:

  * Reliability improvements and bug fixes
  * Swift 6 and Xcode 26.0 support
  * The minimum supported version is iOS 15. This is in accordance with the [compatibility guidelines for Xcode 16](https://developer.apple.com/support/xcode/).



## September 04, 2025

Change

reCAPTCHA Mobile SDK 18.8.0-beta02 is now available for iOS. This version contains reliability improvements and bug fixes.

Change

reCAPTCHA Mobile SDK v18.8.0-beta03 is available for Android. This version contains reliability improvements and bug fixes.

## August 28, 2025

Feature

We've enhanced the reCAPTCHA Admin console to provide a more intuitive interface for configuring risk score thresholds. These improvements help you define how to act on different risk scores. You can also get a better understanding of the transactions that will exceed the threshold which can help in deciding what you allow, block or further reviewing transactions. 

For more information, see [Protect payment transactions with Fraud Prevention](https://docs.cloud.google.com/recaptcha/docs/fraud-prevention).

Feature

Transaction Defense Reasons [is generally available](https://cloud.google.com/products#product-launch-stages). This feature enhances transparency by providing clear, human-readable explanations for why a particular transaction receives a high transaction risk score. The reasons help you better understand the risk assessments and take more informed actions to protect against fraud.

For more information, see [Risk reason](https://docs.cloud.google.com/recaptcha/docs/reference/rest/v1/projects.assessments#riskreason).

## July 31, 2025

Feature

reCAPTCHA policy-based challenge keys are now available in [Preview](https://cloud.google.com/products#product-launch-stages). With policy-based challenge keys, you can configure reCAPTCHA to deterministically trigger CAPTCHA challenges based on a score threshold and challenge difficulty. For more information about the policy-based challenge keys, see [reCAPTCHA keys overview](https://docs.cloud.google.com/recaptcha/docs/keys).

Change

reCAPTCHA Mobile SDK v18.8.0-beta02 is available for Android.

This version contains the following changes:

  * Reliability improvements and bug fixes.
  * The minimum supported version of Android is 23.



## July 02, 2025

Change

reCAPTCHA Mobile SDK 18.8.0-beta01 is now available for iOS.

This version contains the following changes:

  * Support for Swift 6 and Xcode 26.0 beta01.
  * Minimum supported version is set to iOS 15 in accordance with <https://developer.apple.com/support/xcode/> for Xcode 16.



## June 04, 2025

Change

reCAPTCHA Mobile SDK v18.8.0-beta01 is now available for Android

This version contains reliability improvements and bug fixes.

## May 12, 2025

Change

reCAPTCHA Mobile SDK v18.7.1 is now available for Android

This version contains reliability improvements in the `execute()` method.

## February 20, 2025

Announcement

reCAPTCHA SMS defense (formerly SMS toll fraud protection) is now available in [GA](https://cloud.google.com/products#product-launch-stages). For more information, see [Detect and prevent SMS fraud](https://docs.cloud.google.com/recaptcha-enterprise/docs/sms-fraud-detection).

## January 29, 2025

Change

reCAPTCHA Mobile SDK v18.7.0 is now available for iOS.

This version contains the following changes:

  * Public API is moved to Swift along with support for Objective-C.
  * New integration architecture with `RecaptchaInterop` for Firebase clients.



Change

reCAPTCHA Mobile SDK v18.7.0 is now available for Android.

This version contains a dependency on `com.google.android.gms:play-services-recaptchabase` for enhanced detection.

## January 15, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some reCAPTCHA resources. For more information, see [Use custom organization policies for reCAPTCHA keys and firewall policies](https://docs.cloud.google.com/recaptcha/docs/custom-constraints).

## January 08, 2025

Announcement

reCAPTCHA express is now available in [GA](https://cloud.google.com/products#product-launch-stages). For more information, see [Set up reCAPTCHA express](https://docs.cloud.google.com/recaptcha/docs/express-standalone).

## December 16, 2024

Announcement

Configuring allowlists for IP addresses is now available in [GA](https://cloud.google.com/products#product-launch-stages). This feature lets you add the trusted IP addresses to an allowlist to exclude them from reCAPTCHA enforcement. For more information, see [Configure an IP address allowlist](https://docs.cloud.google.com/recaptcha/docs/allowlist-ip).

## December 11, 2024

Change

reCAPTCHA Mobile SDK v18.7.0-beta01 is now available for iOS.

This version contains the following changes:

  * Mitigation for an issue that caused a [crash after updating to v18.6.0](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/129).
  * Public API is moved to Swift along with support for Objective-C.
  * New integration architecture with `RecaptchaInterop` for Firebase clients.



## October 10, 2024

Change

reCAPTCHA Mobile SDK v18.7.0-beta01 is now available for Android.

This version contains a dependency on `com.google.android.gms:play-services-recaptchabase` for enhanced detection.

## September 10, 2024

Change

reCAPTCHA Mobile SDK v18.6.1 is now available for Android.

This version contains the compatibility fix for Android 6 and earlier.

## August 29, 2024

Change

reCAPTCHA Mobile SDK v18.6.0 is now available for iOS.

This version contains the following changes:

  * A new API, `fetchClient`, is available that provides built-in retries for network issues.
  * Bug fixes and improvements.



## August 21, 2024

Change

reCAPTCHA Mobile SDK v18.6.0 is now available for Android.

This version contains the following changes:

  * A new API, `fetchClient`, is available that provides built-in retries for network issues.
  * Bug fixes and improvements.



## August 16, 2024

Change

reCAPTCHA Mobile SDK v18.6.0-beta02 is now available for iOS.

This version contains bug fixes and improvements.

## August 09, 2024

Change

reCAPTCHA Mobile SDK v18.6.0-beta01 is now available for iOS.

This version contains the following changes:

  * A new API, `fetchClient`, is available that provides built-in retries for network issues.
  * Bug fixes and improvements.



## July 26, 2024

Feature

Docker container for password leak detection is now available in [Preview](https://cloud.google.com/products#product-launch-stages). 

You can now use Docker container client to detect password leaks and breached credentials to prevent account takeovers (ATOs) and credential stuffing attacks. For more information, see [check for breached and leaked credentials using Docker container](https://docs.cloud.google.com/recaptcha/docs/check-passwords#docker-container).

Change

reCAPTCHA Mobile SDK v18.6.0-beta02 is now available for Android.

This version contains Java support for the `fetchClient` API.

## July 11, 2024

Feature

reCAPTCHA for WAF integration with Akamai is now available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate reCAPTCHA for WAF with Akamai ](https://docs.cloud.google.com/recaptcha-enterprise/docs/implement-waf-akamai).

## June 19, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.6.0-beta01 is now available for Android.

This version contains the following changes:

  * A new API, `fetchClient`, is available that provides built-in retries for network issues.
  * Bug fixes and improvements.



## June 01, 2024

Announcement

reCAPTCHA launches three usage-based tiers: Enterprise, Standard, and Essentials. For more information about these tiers, see [Compare features between reCAPTCHA tiers](https://docs.cloud.google.com/recaptcha-enterprise/docs/compare-tiers).

## May 29, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.1 is now available for iOS.

This version contains improvement in the detection of network errors.

Feature

reCAPTCHA SMS toll fraud protection is now available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Detect and prevent SMS fraud](https://docs.cloud.google.com/recaptcha-enterprise/docs/sms-fraud-detection).

Change

reCAPTCHA Enterprise Mobile SDK v18.5.1 is now available for Android.

This version contains improvement in the detection of network errors.

## May 15, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0 is now available for iOS.

This version contains the following changes:

  * Performance and reliability improvements in `getClient()` and `execute()`.
  * Support for Apple Privacy Manifest.
  * The minimum iOS version is now iOS 12 to align with Xcode 15 dropping support for iOS 11.
  * New exception type is added for devices without a network connection.



Change

reCAPTCHA Enterprise Mobile SDK v18.5.0 is now available for Android.

This version contains the following changes:

  * Performance and reliability improvements in `getClient()` and `execute()`.
  * Support for Android API 19 is dropped.
  * New exception type is added for devices without a network connection.



## May 01, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta03 is now available for Android.

This version contains the following changes:

  * Performance and reliability improvements in `getClient()` and `execute()` .
  * Dependency from OkHttp is removed.



## April 29, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta04 is now available for iOS.

This version contains the workaround for the [bug in Xcode 15.3](https://developer.apple.com/forums/thread/749554) that prevents apps from being published in AppStore.

## April 18, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta03 is now available for iOS.

This version contains the following changes:

  * Support for Apple Privacy Manifest.
  * The minimum supported version of Xcode is 15.3.
  * The minimum supported version of client's CocoaPods version is 1.12.0.



## March 28, 2024

Announcement

[reCAPTCHA Enterprise account defender for mobile applications](https://docs.cloud.google.com/recaptcha-enterprise/docs/account-defender-mobile) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

You can use this feature to detect and prevent account-related fraudulent activities on mobile applications.

## March 21, 2024

Feature

reCAPTCHA Enterprise platform logs are now available in Chronicle. Users can now view their reCAPTCHA assessment and annotation data in a structured and searchable data format in Chronicle. For more information, see [Collect reCAPTCHA Enterprise logs](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/collect-gcp-recaptcha-logs).

## March 20, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta02 is now available for Android and iOS.

This version contains changes to improve the performance and reliability of `getClient()` and `execute()`.

## March 06, 2024

Feature

reCAPTCHA Enterprise for WAF integration with Cloudflare is now available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate reCAPTCHA Enterprise for WAF with Cloudflare ](https://docs.cloud.google.com/recaptcha-enterprise/docs/implement-waf-cloudflare).

## February 29, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta01 is now available for iOS.

This version contains the following changes:

  * The new minimum iOS version is iOS 12.
  * New exception type is added for devices without a network connection: NO_NETWORK_FOUND.



## February 21, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.5.0-beta01 is now available for Android.

This version contains the following changes:

  * Support for Android API 19 is removed.
  * Dependency on OkHttp 4.11.0 is added.
  * New exception type is added for devices without a network connection: `NO_NETWORK_FOUND`.



Change

reCAPTCHA Enterprise Mobile SDK v18.4.2 is now available for iOS.

This version contains fixes for the following stability issues:

  * [Issue 1](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/88)
  * [Issue 2](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/89)
  * [Issue 3](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/90)



## February 05, 2024

Change

reCAPTCHA Enterprise Mobile SDK v18.4.1 is now available for iOS.

This version contains fixes for the following issues:

  * [Apps become unresponsive while iterating files with NSFileManager ](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/84)
  * [Apps crash due to WKWebView deallocation from a background thread](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/83)



## February 02, 2024

Feature

reCAPTCHA Enterprise mobile SDKs now support 11 levels of scores along with the [reason codes](https://docs.cloud.google.com/recaptcha-enterprise/docs/interpret-assessment-mobile#understand_reason_codes). This enhancement requires a security review. To request access, [contact our sales team](https://go.chronicle.security/recaptchaupgrade).

## December 21, 2023

Feature

reCAPTCHA Enterprise for WAF and Google Cloud Armor integration is now available for mobile applications in [GA](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate with Google Cloud Armor for mobile applications](https://docs.cloud.google.com/recaptcha-enterprise/docs/implement-waf-ca-mobile).

## December 13, 2023

Feature

[reCAPTCHA Enterprise account defender for mobile applications](https://docs.cloud.google.com/recaptcha-enterprise/docs/account-defender-mobile) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

You can use this feature to detect and prevent account-related fraudulent activities on mobile applications.

Change

reCAPTCHA Enterprise Mobile SDK v18.4.0 is now available for Android.

This version contains the following changes:

  * Fix for a security issue affecting Android SDK versions 18.0.0 to 18.3.0.
  * Internal networking improvements.
  * [Sample codes](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/tree/main/examples/android) for the Android SDK in GitHub and visual reCAPTCHA in GitHub.
  * The default timeout value of `execute()` is changed to 10 seconds.



## November 13, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.4.0 is now available for iOS.

This version contains the following changes:

  * Internal networking improvements.
  * [Sample codes](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/tree/main/examples) for the iOS SDK and visual reCAPTCHA in GitHub.
  * The `-ObjC` flag is not required when integrating with reCAPTCHA Enterprise on iOS.



## August 31, 2023

Feature

reCAPTCHA Enterprise for WAF and Google Cloud Armor integration is now available for mobile applications in [Public Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate with Google Cloud Armor for mobile applications](https://docs.cloud.google.com/recaptcha-enterprise/docs/implement-waf-ca-mobile).

## August 16, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.3.0 is now available for Android.

This version is compiled with Kotlin 1.9.0 and contains the bug fix for better regional support of end-users. For information about the issue, see the [platform exception error](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/60).

Change

reCAPTCHA Enterprise Mobile SDK v18.3.0 is now available for iOS.

This version contains the following changes:

  * The SDK is now built with Xcode 14.2. It requires Xcode 14.2 or later.
  * Bug fix for better regional support of end-users. For information, see the [platform exception error](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/60).
  * Documentation update of `RecaptchaError` in the [API reference documentation](https://docs.cloud.google.com/recaptcha-enterprise/docs/reference/ios/client/api/Classes/RecaptchaError).



## July 05, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.2.2 is now available for iOS.

This version contains a speculative fix for the race condition that was occurring in `execute()`. For more information about the issue, see [Crash when executing token request](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/44).

## June 14, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.2.1 is now available for iOS.

In this version, the internal error that occurred on iOS 11, 12, and 13 devices when calling `execute()` is fixed. For information about the issue, see [internal error when calling `execute()`](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/53).

## May 29, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.2.1 is now available for Android. 

This version fixed the issue that caused `Failed to parse the message` or `Protocol message contained an invalid tag (zero)` error. For more information about the issue, see [unhandled exception in Android SDK 18.2.0](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/52).

## May 11, 2023

Feature

reCAPTCHA Enterprise Fraud Prevention is [generally available](https://cloud.google.com/products#product-launch-stages).

You can use reCAPTCHA Enterprise Fraud Prevention to protect payment transactions against attacks such as carding, stolen instrument fraud, and account takeover payment fraud. For more information, see [Protect payment transactions with Fraud Prevention](https://docs.cloud.google.com/recaptcha-enterprise/docs/fraud-prevention).

## May 08, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.2.0 is now available for Android.

This version contains the following changes:

  * The `execute` and `getClient` public APIs have a timeout parameter with a default value of 10 seconds. Users can modify the timeout value for slower networks. 
  * If a client is called with a different site key than the site key that was initialized, an exception is returned to prevent the misuse of the SDK.



## May 04, 2023

Feature

Users can now see how reCAPTCHA Enterprise works on the Google Cloud console. For more information, see [Test reCAPTCHA Enterprise in a demo website](https://docs.cloud.google.com/recaptcha-enterprise/docs/quickstart-app).

## May 01, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.2.0 is now available for iOS.

This version contains the following changes:

  * The SDK is now built with Xcode 14. 
  * A few [parameters](https://docs.cloud.google.com/recaptcha-enterprise/docs/reference/ios/client/api/Classes/RecaptchaAction#deprecated-apis-and-properties) in the `RecaptchaAction` class are deprecated and will be removed in the major release. 
  * New parameters are added in the `RecaptchaAction` class and they have the following effects: 
    * A `String` is returned instead of `RecaptchaToken` in `execute()` calls.
    * A timeout parameter is added to both `execute` and `getClient` APIs.
  * Fixed a bug where the client becomes unusable in some [scenarios](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/43).
  * Added a speculative fix for a [rare crash](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/44).
  * Added a new interoperability pod dependency in support of future Firebase integration.



## April 06, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.1.2 is now available for Android.

This version contains the following changes:

  * Returns network error instead of internal error in cases where the network is extremely slow, but doesn't fail by the timeout. 
  * Removed non sdk api violation.



## March 30, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.1.2 is now available for iOS.

This version contains the following changes:

  * Fix for the [memory corruption bug](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/38).
  * Refinement of fix for the bug affecting `execute()` on the devices running iOS 11, 12 and 13.
  * Returns network error instead of internal error in cases where the network is extremely slow, but not doesn't fail by the timeout.



## March 20, 2023

Announcement

reCAPTCHA WAF express protection is now available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information about this feature, see [Features for integration with WAF service providers](https://docs.cloud.google.com/recaptcha-enterprise/docs/waf-features).

## March 17, 2023

Announcement

reCAPTCHA Enterprise for WAF integration with Fastly is now available in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Integrate with Fastly](https://docs.cloud.google.com/recaptcha-enterprise/docs/implement-waf-fastly).

## March 16, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.1.1 is now available for iOS.

This version contains the following changes:

  * Fixed the [issue](https://github.com/GoogleCloudPlatform/recaptcha-enterprise-mobile-sdk/issues/33) that generated multiple warnings when archiving apps.
  * Fixed an issue affecting `execute()` on iOS 11, 12, and 13.
  * Removed Protobuf as a dependency on CocoaPods.



## February 16, 2023

Announcement

reCAPTCHA Enterprise Fraud Prevention is available in [Preview](https://cloud.google.com/products#product-launch-stages).

You can use reCAPTCHA Enterprise Fraud Prevention to protect payment transactions against attacks such as carding, stolen instrument fraud, and account takeover payment fraud. For more information, see [Protect payment transactions](https://docs.cloud.google.com/recaptcha-enterprise/docs/payment-flows).

## February 15, 2023

Feature

[reCAPTCHA Enterprise account defender](https://docs.cloud.google.com/recaptcha-enterprise/docs/account-defender) is now generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

You can use this feature to detect and prevent account-related fraudulent activities.

## February 09, 2023

Feature

reCAPTCHA Enterprise password leak detection Node.js library is now available. For more information, see [GitHub repo](https://github.com/GoogleCloudPlatform/typescript-recaptcha-password-check-helpers/) and [npm module](https://www.npmjs.com/package/recaptcha-password-check-helpers).

## February 08, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.1.1 is now available for Android.

This version contains the following changes:

  * General stability fixes
  * Errors due to a race condition while calling `init()` repeatedly are fixed
  * (BREAKING CHANGE): custom events are no longer prepended with `custom_`
  * Clients now return `RecaptchaErrorCode.NETWORK_ERROR` instead of `RecaptchaErrorCode.INTERNAL_ERROR` on network errors



## February 01, 2023

Change

reCAPTCHA Enterprise Mobile SDK v18.1.0 is now available for iOS.

This version contains the following changes:

  * General stability fixes
  * Errors due to a race condition while calling `init()` repeatedly are fixed
  * iOS minimum is now iOS 11
  * `getClient` no longer crashes when called on a background thread



## December 08, 2022

Feature

You can now enable the email verification feature of MFA from the Google Cloud console. For instructions, see [Configure Multi-factor authentication](https://docs.cloud.google.com/recaptcha-enterprise/docs/integrate-account-verification).

## November 30, 2022

Change

reCAPTCHA Enterprise Mobile SDK iOS v18.0.3 is now available. This version contains the following changes:

  * Performance improvements
  * Dependency of the Protobuf library is removed
  * Build support for Xcode13
  * Bug fixes



Change

reCAPTCHA Enterprise Mobile SDK Android v18.0.1 is now available. This version contains performance improvements.

## November 08, 2022

Change

reCAPTCHA Enterprise Mobile SDK iOS v18.0.2 is now available. This version contains build (not runtime) support for older versions of iOS and some bug fixes.

## November 07, 2022

Feature

reCAPTCHA Enterprise offers the recommended score threshold system that allows users to calculate the best threshold value to take action against suspected bots based on the key's score history. Users can see this information on the reCAPTCHA Enterprise metrics page on the Google Cloud console.

## November 04, 2022

Change

reCAPTCHA Enterprise Mobile SDK iOS v18.0.1 is now available. This version contains build support for Xcode14 disabling bitcode and some bug fixes.

## October 31, 2022

Announcement

reCAPTCHA Enterprise Mobile SDK v18.0.0 is now generally available. This native SDK supports [iOS](link:%20https://cloud.google.com/recaptcha-enterprise/docs/instrument-ios-apps) and [Android](link:%20https://cloud.google.com/recaptcha-enterprise/docs/instrument-android-apps) devices.

## July 19, 2022

Feature

You can now find legacy secret keys for all reCAPTCHA Enterprise keys in the Google Cloud console. These keys can be useful if you are using a third-party plug-in/implementation that does not yet call the reCAPTCHA Enterprise API. For more information, see [FAQs](https://docs.cloud.google.com/recaptcha-enterprise/docs/faq).

## June 28, 2022

Feature

You can now enable platform logging for reCAPTCHA Enterprise API calls. For more information, see [Working with platform logs](https://docs.cloud.google.com/recaptcha-enterprise/docs/platform-logging).

## May 26, 2022

Announcement

reCAPTCHA Enterprise for WAF and Google Cloud Armor integration is now generally available (GA). For more information, see the [Overview of reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha-enterprise/docs/integration-overview) and Cloud Armor [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management).

## April 25, 2022

Change

The `v1` version of the reCAPTCHA Enterprise API now supports API key authentication. The `v1beta1` version of the API will continue to be available only for the existing users.

## April 06, 2022

Feature

You can now create reCAPTCHA WAF site keys to implement the reCAPTCHA Enterprise for WAF and Google Cloud Armor integration. For more information, see [Implement the reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://cloud.google.com/recaptcha-enterprise/docs/implement-tokens).

## March 07, 2022

Announcement

You can now enable and use reCAPTCHA Enterprise on Google Cloud without enabling billing for your Google Cloud project. For more information, see [Billing information](https://docs.cloud.google.com/recaptcha-enterprise/docs/billing-information).

## January 21, 2022

Feature

You can now use [reCAPTCHA Enterprise account defender](https://docs.cloud.google.com/recaptcha-enterprise/docs/account-defender) to detect and prevent account-related fraudulent activities. This feature is in Public Preview.

## August 16, 2021

Feature

reCAPTCHA Enterprise for WAF and Google Cloud Armor integration is now available in Public Preview. For more information, see the [Overview of reCAPTCHA Enterprise for WAF and Google Cloud Armor integration](https://docs.cloud.google.com/recaptcha-enterprise/docs/integration-overview) and Cloud Armor [bot management overview](https://docs.cloud.google.com/armor/docs/bot-management).

## January 10, 2020

Change

reCAPTCHA Enterprise features GA release.

## March 31, 2019

Feature

reCAPTCHA Enterprise features Beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
