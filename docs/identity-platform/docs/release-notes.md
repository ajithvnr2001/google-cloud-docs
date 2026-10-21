---
url: https://docs.cloud.google.com/identity-platform/docs/release-notes/
title: Identity Platform release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:38:37.416728+00:00
---

# Identity Platform release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Resources ](https://docs.cloud.google.com/identity-platform/docs/resources)



Send feedback 

#  Identity Platform release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Identity Platform. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/identityplatform-release-notes.xml) directly. 

## December 03, 2024

Feature

The Identity Platform integration with reCAPTCHA Enterprise API now supports [bot protection](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise) and [SMS toll fraud protection](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp) for SMS-based flows on iOS platforms.

## October 31, 2024

Feature

Support for SMS-based authentication flows in the Identity Platform integration with reCAPTCHA Enterprise API is now in Preview. In addition, the integration now supports reCAPTCHA's SMS toll fraud protection and the ability to bring your own reCAPTCHA keys.

For more information, see the following pages:

  * [Integrate Identity Platform with the reCAPTCHA Enterprise API](https://docs.cloud.google.com/identity-platform/docs/recaptcha-enterprise)
  * [Enable SMS toll fraud protection for SMS-based authentication](https://docs.cloud.google.com/identity-platform/docs/recaptcha-tfp)
  * [Bring your own reCAPTCHA keys](https://docs.cloud.google.com/identity-platform/docs/recaptcha-byok)



## September 30, 2024

Feature

Custom organization policies for Identity Platform are generally available (GA). You can use custom organization policies to allow or deny specific operations on Identity Platform resources for the security, compliance, or governance requirements of your application.

For more information, see [Use custom organization policies](https://docs.cloud.google.com/identity-platform/docs/admin/org-policy-custom-constraints).

## April 15, 2024

Announcement

[Automatic, anonymous account deletion](https://firebase.google.com/docs/auth/web/anonymous-auth#auto-cleanup) is now enforced for all projects that have [`autodelete_anonymous_users`](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/Config) enabled.

## September 21, 2023

Change

[Time-based one-time password (TOTP)](https://docs.cloud.google.com/identity-platform/docs/admin/enabling-totp-mfa) as an additional multi-factor authentication option is generally available (GA).

## September 15, 2023

Announcement

[Email enumeration protection](https://docs.cloud.google.com/identity-platform/docs/admin/email-enumeration-protection) is enabled by default for all new projects. With email enumeration protection enabled, the Firebase Auth SDK method `fetchSignInMethodsForEmail` returns null, for added security.

## May 30, 2023

Announcement

[Password policies](https://docs.cloud.google.com/identity-platform/docs/password-policy) are generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## May 08, 2023

Feature

[Firebase App Check](https://docs.cloud.google.com/identity-platform/docs/admin/app-check-integration) is available in Preview.

## April 19, 2023

Feature

[Time-based one-time password (TOTP)](https://docs.cloud.google.com/identity-platform/docs/admin/enabling-totp-mfa) as an additional multi-factor authentication option is available in Preview.

## April 13, 2023

Change

Added SDK support to meet Apple's [user deletion requirements](https://docs.cloud.google.com/identity-platform/docs/ios/apple#user_account_deletion).

## March 28, 2023

Change

Play Integrity is now supported for client-side authentication on Android applications. For more information, see [Authenticate with Firebase on Android using a Phone Number](https://firebase.google.com/support/release-notes/android#auth_v21-2-0).

## March 14, 2023

Change

Identity Platform has updated several quotas. View the updated quotas from Identity **Toolkit API** > **Quotas** on the [APIs & Services page in the Google Cloud console](https://docs.cloud.google.com/apis).

## September 26, 2022

Feature

Added the ability to set up SMS region policies to help protect your applications from potential SMS abuse. For more information, see [Using SMS regions to protect your app from SMS abuse](https://docs.cloud.google.com/identity-platform/docs/admin/sms-regions).

## July 11, 2022

Feature

[Activity logging](https://docs.cloud.google.com/identity-platform/docs/activity-logging) can now be enabled on a per-tenant basis. The feature is generally available.

## June 29, 2022

Change

Identity Platform Web v9 modular SDK is now available at the [GA stage](https://cloud.google.com/products#product-launch-stages). For details, see [Upgrade to the modular Web SDK (v9) ](https://docs.cloud.google.com/identity-platform/docs/web/modular-sdk-upgrade).

## May 01, 2022

Change

[Session cookies](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/projects/createSessionCookie) are now supported for tenants. The feature is generally available.

## September 28, 2021

Change

[Facebook Limited Login](https://docs.cloud.google.com/identity-platform/docs/ios/facebook) is supported at the GA stage.

## June 30, 2021

Change

Identity Platform supports [Argon2 for password hashing algorithms](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v1/Argon2Parameters), and [SMTP- and template-customized settings for tenant projects](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects.tenants) at the GA stage.

## May 11, 2021

Change

Support for OIDC [sign in](https://docs.cloud.google.com/identity-platform/docs/web/oidc) and [management](https://docs.cloud.google.com/identity-platform/docs/managing-providers-programmatically) for Identity Platform is released at the GA stage.

## December 09, 2020

Change

[Blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions) are released at the GA stage.

Blocking functions let you execute custom code that modifies the result of a user registering or signing in to your app.

## October 14, 2020

Feature

[Sign in with Apple](https://docs.cloud.google.com/identity-platform/docs/web/apple) is now supported.

## August 14, 2020

Feature

Multi-factor authentication (MFA) is now GA!

## November 18, 2019

Feature

[Multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy) for Identity Platform is now GA!

## April 09, 2019

Feature

Identity Platform is now GA!

## December 13, 2018

Feature

Welcome to the Identity Platform beta!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
