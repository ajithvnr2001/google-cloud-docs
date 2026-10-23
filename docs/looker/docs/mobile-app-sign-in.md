---
url: https://docs.cloud.google.com/looker/docs/mobile-app-sign-in/
title: Signing in to the mobile application \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:21.741996+00:00
---

# Signing in to the mobile application  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/mobile-app-sign-in/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Signing in to the mobile application Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The Looker application doesn't support signing in with a QR code.

If mobile application access is [enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement) for your instance and you have [installed](https://docs.cloud.google.com/looker/docs/mobile-app-installation) the app on your mobile device, you can sign in to the app using the same authentication method that you use to sign in to your Looker instance (Google OAuth, SAML, LDAP, OpenID Connect, or email and password).

The first time you sign in to the app, an onboarding screen is displayed. Select **Next** , or swipe left on each onboarding screen, and then select **Let's go!** on the final screen. You can also select **Skip** to navigate directly to the [**Recently Viewed** screen](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content).

## Signing in with Google Auth, SAML, LDAP, OpenID Connect, or email address

You can sign in using the same authentication method as your Looker instance by following these steps:

  1. Open the Looker mobile application.
  2. When prompted to choose between Looker and Data Studio Pro, choose Looker.
  3. Enter the URL for your Looker instance in the format `instance_name.looker.com` (don't use `http://www.` or `https://www.`), and then select **Continue**.
  4. The mobile application will direct you to sign in using your Google Auth, SAML, LDAP, OpenID Connect, or email credentials.



When you sign in to the Looker app for the first time, the app displays the **Authorization Request** screen. To confirm that you want to authorize the app to access data through your Looker account, select **Approve**.

Once you have signed in, you can navigate to your [favorite and most recently viewed Looks and dashboards](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#viewing_your_most_recently_viewed_or_favorite_content), view [boards](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#navigating_to_content_from_boards), and browse [content in folders](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#browsing_content_in_folders).

## Signing in with biometrics

You can configure biometric sign-in for your Looker or Data Studio Pro account.

The first time you sign in to the app, the app will prompt you to set up biometric verification.

**Note:** You must enable biometrics on your device in order to enable biometric verification in the app. If you disable biometrics on your device, biometrics will also be disabled for the app.

To enable or disable biometric verification, open the **Settings** menu of the app, and then toggle the **Biometric verification** option in the **Security** section.

## Signing out of the app

To sign out of the Looker mobile app, follow these steps:

  1. Select **More** from the app's [navigation menu](https://docs.cloud.google.com/looker/docs/mobile-app-navigating-to-content#using_the_navigation_menu).
  2. Select **Sign out**.



## Troubleshooting

If you're unable to sign in, verify the following:

  * Verify that your administrator has [enabled the Looker mobile app](https://docs.cloud.google.com/looker/docs/mobile-app-enablement) for your instance.
  * If your instance uses a Private IP, connect to your corporate VPN. For more information, see [Using the mobile application with Private IP instances](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app#using-the-mobile-application-with-private-ip-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
