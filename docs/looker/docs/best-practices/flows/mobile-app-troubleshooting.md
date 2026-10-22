---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/mobile-app-troubleshooting/
title: Troubleshooting the Looker mobile application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:39.203538+00:00
---

# Troubleshooting the Looker mobile application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/mobile-app-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting the Looker mobile application Stay organized with collections  Save and categorize content based on your preferences. 

The Looker mobile application lets you access your Looker and Data Studio Pro content on Android and iOS devices, view Looks and dashboards, and collaborate on the go. If you encounter issues while using the mobile application—such as sign-in problems, rendering errors, application crashes, performance delays, or display discrepancies—this guide helps you troubleshoot and resolve them.

**Note:** If you are using the older **Looker Mobile (Legacy)** app, support will end on **January 31, 2027** , and the app will be delisted. We strongly recommend migrating to the [current Looker mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-installation). For a feature comparison, see the [Feature Parity Matrix](https://docs.cloud.google.com/looker/docs/mobile-app-legacy#differences-between-the-mobile-applications).

## Prerequisites and common configuration requirements

Before you begin troubleshooting, ensure that your environment and account meet the prerequisites for using the Looker mobile application:

  * **Mobile application access enabled:** A Looker administrator must [enable mobile application access](https://docs.cloud.google.com/looker/docs/mobile-app-enablement) for your instance.
  * **User permissions:** Your user account must have the `mobile_app_access` Looker permission assigned directly or through a user group.
  * **Supported instances:** The Looker mobile application supports Looker (Google Cloud core) (public IP, or private IP using private services access or Private Service Connect accessible through a corporate VPN) and Looker (original) instances (Looker-hosted and customer-hosted).
  * **Corporate VPN and IP allowlists:** If your Looker instance enforces [IP allowlisting](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist), your mobile device must connect through a corporate VPN with a static IP address on the instance IP allowlist.
  * **Supported authentication:** The Looker mobile application supports Google OAuth, SAML, LDAP, OpenID Connect, and email and password credentials. Signing in with QR codes is only supported on the [Looker Mobile (Legacy) application](https://docs.cloud.google.com/looker/docs/mobile-app-legacy) and requires Embed SSO to be enabled.



## Debugging tree

Use the following decision tree to begin troubleshooting Looker mobile application issues:

The following sections describe the scenarios in the tree in further detail.

## Identify which mobile application is installed

Because both the **Looker** mobile application and the **Looker Mobile (Legacy)** application are available in app stores, the first troubleshooting step is to determine which application is installed on your mobile device. Support's initial triage step relies on this distinction to prevent misrouted or delayed investigations:

  * **Looker:** The current unified mobile application for Looker and Data Studio Pro content. On your device home screen and in app stores, this app is named **Looker**. It supports standard authentication methods (such as Google OAuth, SAML, OpenID Connect, LDAP, and email and password credentials) and doesn't support QR code login. This troubleshooting guide primarily covers this application.
  * **Looker Mobile (Legacy):** The older mobile application. On your device home screen and in app stores, this app is named **Looker Mobile (Legacy)** (or **Looker Mobile**). It supports QR code and email and password login, but doesn't support Google OAuth, SAML, or Looker (Google Cloud core) instances.



To determine which application is installed on your device:

  1. Check the application name displayed beneath the app icon on your device home screen or in your app launcher.
  2. In the mobile application, select **More** in the bottom navigation menu or open **Settings** , and locate the application name and version number at the bottom of the menu.
  3. Check your installed apps list in the Apple App Store (iOS) or Google Play Store (Android).



If you have **Looker Mobile (Legacy)** installed, support for this application ends on **January 31, 2027** , and the application will be delisted. Google strongly recommends migrating to the [current Looker mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-installation). For documentation and troubleshooting for the legacy application, see the [Looker Mobile (Legacy) application](https://docs.cloud.google.com/looker/docs/mobile-app-legacy) guide.

If you have the **Looker** mobile application installed, proceed with the troubleshooting steps in the following sections.

## Verify if the issue reproduces outside the mobile application

The first step in troubleshooting is to determine whether the issue is isolated to the mobile application or if it also affects the Looker web application.

Open a desktop or mobile web browser, sign in to your Looker instance, and attempt to perform the same action:

  * **Can you sign in through a web browser?** If you cannot sign in from a web browser, the issue isn't specific to the mobile application. Check your credentials, identity provider (IdP) configuration, or user account status.
  * **Do queries or dashboards load in a web browser?** If the dashboard or Look fails to load, returns a database error, or times out in the browser, the issue stems from the underlying query, database connection, or LookML model rather than the mobile application.
  * **Do you have permission to access the content?** If you cannot view the content in the web interface, verify that you have the appropriate folder, model, and explore access permissions.



If the issue also reproduces in a web browser, troubleshoot the issue on your Looker instance.

If the issue occurs only in the mobile application, proceed to the relevant section in this guide.

## Troubleshoot sign-in issues

If you cannot sign in to the Looker mobile application, investigate the following common causes:

  * **Instance URL format:** When entering your instance URL in the mobile app, use the format `instance_name.looker.com` or your custom domain. Don't include `https://`, `http://`, or trailing slashes.
  * **Instance enablement:** Verify with your Looker administrator that mobile application access is [enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement#enabling_the_app) under **Admin > General > Mobile Application**.
  * **User permissions:** Verify with your administrator that your user role or group includes the `mobile_app_access` permission.
  * **Corporate VPN and IP allowlists:** If your instance enforces IP allowlists, ensure that your mobile device is connected to your organization's VPN and that the VPN server's static IP address is on the instance's [IP allowlist](https://docs.cloud.google.com/looker/docs/admin-panel-server-ip-allowlist). Test this by opening the instance URL in a web browser on the same mobile device while connected to the VPN.
  * **Customer-hosted API configuration:** If you use a customer-hosted Looker (original) instance, verify that your instance's **[API Host URL](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url)** under **Admin > Platform > API** matches your instance hostname. Also verify that your network allows mobile traffic on port 443 or port 19999. For more information, see the [considerations for customer-hosted instances](https://docs.cloud.google.com/looker/docs/mobile-app-enablement#considerations_for_customer-hosted_instances) and [Looker API troubleshooting](https://docs.cloud.google.com/looker/docs/api-troubleshooting) documentation pages.
  * **Biometric sign-in:** If biometric verification (fingerprint or face recognition) fails, sign in using your standard username and password. You can reconfigure biometric verification in the app's **Settings** menu under **Security**. Note that biometrics must also be enabled in your mobile device's system settings.



## QR code sign-in issues

The unified Looker mobile application doesn't support signing in with a QR code. Use standard authentication (Google OAuth, SAML, LDAP, OpenID Connect, or email and password) instead.

If you are using the [Looker Mobile (Legacy) application](https://docs.cloud.google.com/looker/docs/mobile-app-legacy) and cannot sign in with a QR code, investigate the following:

  * **Embed SSO Authentication:** In the Looker web interface, navigate to **Admin > Platform > Embed** and confirm that **Embed SSO Authentication** is enabled. This setting enables the QR code login option.
  * **Refresh the QR code:** QR codes are time-sensitive. Refresh the web page displaying the QR code, and then try scanning the newly generated QR code.
  * **Camera permissions and visibility:** Ensure that the mobile application has permission to access your device camera, and ensure adequate lighting when scanning the screen.
  * **Alternative sign-in:** If QR code authentication continues to fail, use email and password credentials to sign in, or migrate to the updated Looker mobile application.



## Troubleshoot content rendering issues

If dashboards or Looks fail to render, display blank cards, or show error messages in the mobile application, investigate the following:

  * **Scope of the issue:** Determine whether the rendering failure affects all content or only specific Looks or dashboards: 
    * **All content fails:** Check your mobile device network connection, verify that your session has not expired, and try signing out and signing back in to the application.
    * **Specific content fails:** Check if the content uses custom visualizations or unsupported layout formats. Also verify that you have access to the underlying model and explores.
  * **Inspect error messages:** If an error banner or tile error appears, note the specific message. Common issues include database connection errors, query timeouts, or missing field references.
  * **Intermittent versus consistent failures:** If content fails intermittently, the issue might be related to database load or temporary network fluctuations.
  * **Pull to refresh:** Use the pull-to-refresh gesture (pull down on the screen) to reload the dashboard or Look and run fresh queries.



## Troubleshoot application crashes

If the Looker mobile application crashes or unexpectedly closes, follow these troubleshooting steps:

  * **Identify crash triggers:** Note when the crash occurs. Does the app crash immediately upon launch, when opening a specific dashboard, when rotating the device between portrait and landscape modes, or after a specific user interaction?
  * **Update the application:** Check the Apple App Store or Google Play Store to ensure you are running the latest version of the Looker mobile app. Updates frequently include stability improvements and bug fixes.
  * **Update device operating system:** Ensure your mobile device is running a supported version of iOS or Android. Outdated operating systems can lead to compatibility issues.
  * **Clear cache and restart:**
    * Force close the application and reopen it.
    * Restart your mobile device.
    * On Android, clear the application cache under **Settings > Apps > Looker > Storage > Clear Cache**.
  * **Reinstall the application:** Uninstall the app, restart the device, and reinstall the application from the official app store.



## Troubleshoot performance and latency issues

If the Looker mobile application is slow, unresponsive, or taking an extended time to load content, investigate the following:

  * **Identify the slow component:** Determine whether the delay occurs when launching the app, navigating folders and boards, loading cached lists of content, or executing queries for dashboard tiles.
  * **List caching:** The mobile application caches lists of recently viewed and favorite content to speed up navigation. The list automatically refreshes on app launch, but you can pull down to refresh manually if the list appears out of date.
  * **Dashboard complexity and tile count:** Dashboards with many tiles or complex visualization types require substantial memory and processing resources on mobile devices. Test whether smaller dashboards or individual Looks load more quickly.
  * **Network speed and latency:** Mobile networks might experience high latency or packet loss. Test whether performance improves when connected to a reliable, high-speed Wi-Fi network.
  * **Database query performance:** If individual tiles take a long time to render, check the query duration in the Looker web interface or System Activity. The delay might be due to long-running database queries.



## Troubleshoot display and styling issues

If you encounter visual defects—such as misaligned elements, broken icons, distorted images, or unexpected padding—investigate the following:

  * **Screen orientation:** Test the dashboard or Look in both portrait and landscape orientations. Some complex dashboards and tables are optimized for wider landscape viewing.
  * **Dashboard layout:** Mobile-friendly dashboards dynamically adjust tile positions for small screens. If tiles overlap or truncate text, verify the tile sizing and configuration in the dashboard edit mode on the web application.
  * **Device display settings:** Accessibility settings such as custom system font sizes, display zoom, or third-party dark mode inversion tools can alter how content is rendered. Test with default system display settings.
  * **Visual documentation:** Take screenshots or screen recordings that clearly show the rendering discrepancy to share with your administrator or Support.



## Gather diagnostic information

If you cannot resolve the issue after following the troubleshooting steps, gather the following information before contacting Support:

  1. **Looker instance information:**
     * Instance URL (for example, `instance_name.looker.com`).
     * Looker release version (in the web application, select **Help > About**).
     * Instance hosting type (Looker-hosted or customer-hosted; Looker (Google Cloud core) or Looker (original)).
  2. **Mobile application information:**
     * **Which app is installed:** Specify whether you have installed the **Looker** mobile app or **Looker Mobile (Legacy)**.
     * Application version number (found at the bottom of the in-app **More** menu or in **Settings**).
     * App store from which the application was installed (Apple App Store or Google Play Store).
  3. **Device and operating system details:**
     * Device manufacturer and model (for example, Google Pixel 8, iPhone 15 Pro).
     * Operating system version (for example, Android 14, iOS 17.5).
  4. **Scope and impact:**
     * Does the issue affect all users or only specific user accounts?
     * Does the issue occur on all mobile devices or only specific device models or operating system versions?
  5. **Visual examples and logs:**
     * Screenshots or screen recordings showing the unexpected behavior or error message.
     * Exact steps to reproduce the issue.



## Contact Support

If you have verified all the previous steps and the issue is still not resolved:

  * [Contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and provide the diagnostic information gathered in the previous section. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
