---
url: https://docs.cloud.google.com/looker/docs/looker-core-mobile-app/
title: View Looker content using the Looker mobile application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:34.272922+00:00
---

# View Looker content using the Looker mobile application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-mobile-app/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  View Looker content using the Looker mobile application Stay organized with collections  Save and categorize content based on your preferences. 

Access your Looker (Google Cloud core) or Looker (original) content directly from your mobile device with the Looker mobile application.

## Download the app

To download the Looker mobile app, search for **Looker** in the Apple App Store or the Google Play Store, or use the following links:

  * [App Store](https://apps.apple.com/us/app/looker-studio/id1644381985) (for iOS)
  * [Play Store](https://play.google.com/store/apps/details?id=com.google.android.apps.cloud.cloudbi) (for Android)



The Looker mobile application lets you access your Looker and Data Studio Pro content from a single app. You can view Looks and dashboards on a mobile device.

## Enable and use the app

Note that while you can access content from a Looker (original) instance with either the Looker app or the [Looker Mobile (Legacy) app](https://docs.cloud.google.com/looker/docs/mobile-app-legacy), you can only access content from a Looker (Google Cloud core) instance with the Looker app. The app also supports Private IP Looker (Google Cloud core) instances, but it requires a VPN configuration.

The following documentation pages walk you through setting up and using the Looker mobile application:

  * [Enabling the mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-enablement): For admins: Enabling users to sign in to your instance using the app
  * [Installing the mobile application on your mobile device](https://docs.cloud.google.com/looker/docs/mobile-app-installation): Installing the app on an Android or iOS device
  * [Signing in to the mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-sign-in): Signing in to the app with email or with a QR code, and signing out of the app
  * [Navigating to content in the mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content): Accessing your most recently viewed and favorite Looks and dashboards, viewing content on boards, navigating to content from folders, searching recently viewed and favorite content, sorting lists of content, and using the three-dot menu of a Look or a dashboard
  * [Viewing Looks in the mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-viewing-looks): Opening and viewing Looks, switching between portrait and landscape mode, adding or removing a Look from your favorites, sharing or copying the link to a Look, and viewing information about a Look
  * [Viewing dashboards in the mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-viewing-dashboards): Opening and viewing dashboards, switching between portrait and landscape mode, temporarily changing filter values, adding or removing a dashboard from your favorites, sharing or copying the link to a dashboard, and viewing information about a dashboard
  * [Creating mobile alerts](https://docs.cloud.google.com/looker/docs/mobile-app-alerts): Creating alerts on dashboard tiles, configuring alerts to send push notifications



### Using the mobile application with a corporate VPN and IP allowlisting

If your Looker instance has [IP allowlisting](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist) enabled, users can still access the Looker mobile application by connecting through a corporate VPN that has a static IP address. This static IP address must be added to your Looker instance's IP allowlist.

When you connect your mobile device through a VPN with a static IP that is on the allowlist, the Looker instance will see the connection as originating from the VPN server's static IP. This allows access, even though the mobile device's underlying cellular IP might be dynamic and not on the allowlist.

To test this setup, follow these steps:

  1. Connect the mobile device to the corporate VPN.
  2. Open a web browser on the mobile device.
  3. Try navigating to the Looker instance URL.



If the Looker login page is reachable in the browser, then the network routing and IP allowlisting are functioning correctly through the VPN. The Looker mobile app should then also be able to connect under the same conditions.

Note that any issues with your own infrastructure and network are out of scope for [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details).

### Using the mobile application with Private IP instances

The Looker mobile application supports Private IP Looker (Google Cloud core) instances (including those with VPC Service Controls enabled), but it requires a VPN configuration.

To connect to a Private IP instance, use one of the following methods:

  * **Per-app VPN** : Configure a per-app VPN to allow VPN access specifically for the following applications: 
    * The Looker mobile app
    * Safari (on iOS devices)
    * Chrome (on Android devices)
  * **Full-device VPN** : Use a full-device VPN, which enables the connection for the Looker mobile app and all necessary browser components automatically.



## Differences between the Looker and Looker Mobile (Legacy) apps

You can also access Looker content using the [Looker Mobile (Legacy) application](https://docs.cloud.google.com/looker/docs/mobile-app-legacy). The key differences between the two apps are as follows:

  * The Looker app supports Google OAuth, SAML, LDAP, and OpenID Connect. The Looker Mobile (Legacy) app supports only email and QR authentication.
  * The Looker Mobile (Legacy) doesn't support accessing content from a Looker (Google Cloud core) instance or from Data Studio.

Feature | Looker app support | Looker Mobile (Legacy) app support  
---|---|---  
Supported Looker instance types | 

  * Looker (Google Cloud core)
  * Looker original

| 

  * Looker original

  
Access Data Studio Pro content | Supported | Not supported  
Authentication methods | 

  * Google OAuth
  * SAML
  * LDAP
  * OpenID Connect
  * Email

| 

  * Email
  * QR code

  
Biometric verification | Supported | Supported  
Drilling | Supported | Supported on iOS devices only  
Alerts | Supported | Supported on iOS devices only  
Content search | Not supported | Supported  
Mobile friendly rendering of dashboards and Looks | Supported | Supported  
Private IP and IP allowlist support | Supported (requires VPN) | Not supported  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
