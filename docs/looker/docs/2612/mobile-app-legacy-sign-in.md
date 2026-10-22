---
url: https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-sign-in/
title: Signing in to the Looker Mobile (Legacy) application \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:54.628165+00:00
---

# Signing in to the Looker Mobile (Legacy) application  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-sign-in/

You are viewing documentation for Looker 26.12. Click this link to see the [most recent documentation](https://docs.cloud.google.com/looker/docs/intro). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Signing in to the Looker Mobile (Legacy) application Stay organized with collections  Save and categorize content based on your preferences. 

**Warning:** The Looker Mobile (Legacy) application will be deprecated on August 31, 2026. Use the [Looker application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) instead.

If mobile application access is [enabled](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-enablement) for your Looker instance and you have [installed](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-installation) the Looker app on your mobile device, you can sign in to the app using either an email address or a QR code.

The first time you sign in to the app, an onboarding screen is displayed. Select **Next** , or swipe left on each onboarding screen, and then select **Let's go!** on the final screen. You can also select **Skip** to navigate directly to the [**Recently Viewed** screen](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content).

## Signing in with email

You can sign in to the Looker Mobile (Legacy) app by providing the URL for your instance and the email address and password for your Looker account.

  1. Select **Sign in with email** on the sign-in screen of the app.

![](https://docs.cloud.google.com/static/looker/docs/images/mobile-sign-in-email-716.png)

  2. Enter the URL for your Looker instance in the format `instance_name.looker.com` (don't use `http://www.` or `https://www.`), and then select **Continue**.

  3. On the **Log In** page that is embedded in the app, enter the email address and password that are associated with your account, and select **LOG IN**.




When you sign in to the Looker Mobile (Legacy) app with your email and password for the first time, the app displays the **Authorization Request** screen. To confirm that you want to authorize the app to access data through your Looker account, select **Approve**.

Once you have signed in, you can navigate to your [favorite and most recently viewed Looks and dashboards](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), view [boards](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-navigating-to-content#navigating_to_content_from_boards), browse [content in folders](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-navigating-to-content#browsing_content_in_folders), and [share content](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-sharing-content).

## Signing in with a QR code

**Note:** The Looker Mobile (Legacy) app requires access to your mobile device's camera to let you sign in with a QR code.

To sign in to your instance in the Looker Mobile (Legacy) app by scanning a QR code, follow these steps:

  1. In the Looker web app, select the user menu icon and choose the [**Account** option](https://docs.cloud.google.com/looker/docs/2612/user-account) from the user menu.
  2. On the **Account** page, in the **Mobile App Login** section, select the **QR Code** button.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-account-page-716.png)

  3. On the landing page for the Looker Mobile (Legacy) app, select **Sign in with QR Code**.

  4. At the bottom of the sign-in screen of the app, select **Scan QR Code**.

  5. Point your mobile device's camera at the QR code that is displayed in the **Mobile App Login** section of the Looker web app.




QR codes are valid for five minutes after they are generated. If you are unable to sign in to the app with a QR code because your QR code has expired, repeat these steps:

  1. Refresh the **Mobile App Login** page in the Looker web app.
  2. Select **Try again** in the mobile application.
  3. Point your camera at the QR code on your computer to scan the newly generated QR code.



## Signing in with biometrics

If your Looker admin has [required users to sign in to Looker every time they open the mobile app](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-enablement#requiring_mobile_app_authentication), you can configure biometric sign-in for your Looker account on the Looker Mobile (Legacy) app.

  1. Select **Sign in with email** on the sign-in screen of the app.
  2. Enter the URL for your Looker instance, and then enter your email and password on the **Log In** screen.
  3. In the **Set up Fingerprints** pop-up, select **Enable**.



Once you have configured the app to allow biometric sign-in, you can sign in to the app by selecting **Sign in with Fingerprint** on the sign-in screen.

## Signing out of the app

To sign out of the Looker Mobile (Legacy) app, follow these steps:

  1. Select **More** from the app's [navigation menu](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-navigating-to-content#using_the_navigation_menu).
  2. Select **Sign out**.



## Troubleshooting

If you are unable to sign in, ensure that the Looker Mobile (Legacy) app is [enabled for your instance](https://docs.cloud.google.com/looker/docs/2612/mobile-app-legacy-enablement).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
