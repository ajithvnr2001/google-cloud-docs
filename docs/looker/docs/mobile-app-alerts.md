---
url: https://docs.cloud.google.com/looker/docs/mobile-app-alerts/
title: Alerts in the mobile application \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:48.893173+00:00
---

# Alerts in the mobile application  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/mobile-app-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Alerts in the mobile application Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** The [Looker Mobile (Legacy) application](https://docs.cloud.google.com/looker/docs/mobile-app-legacy) supports alerts, but only on iOS devices.

The [Looker mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) supports alerts on dashboard tiles. You can configure an alert to send push notifications when the alert's conditions are met or exceeded to recipients that you specify and to the alert's followers.

This page discusses how to view and share alerts that were [created on the Looker instance](https://docs.cloud.google.com/looker/docs/creating-alerts) from the mobile application and what information is conveyed through the alert notifications.

When someone configures an alert to [send alert notifications to email](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_email), each recipient will also receive a [push notification](https://docs.cloud.google.com/looker/docs/mobile-app-alerts#push-notifications) to their mobile device if the following is true:

  * The Looker instance has the [Looker mobile application enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement).
  * The Looker instance is on Looker 26.6 or later.
  * The user has the [Looker mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-installation) installed on their mobile device.



## View an alert in the mobile application

To view information about an existing alert, tap the add_alert **Alerts** icon on a dashboard tile. When you tap the icon, the Looker mobile application displays the following details about the alert:

  * The value that triggered the alert
  * The visualization for the tile on which the alert is based
  * The name of the dashboard tile on which the alert is based



## Share an alert

To share an alert with others, tap share **Share** and select at least one recipient. The recipients that you specify will receive a push notification with information about the alert. If they tap the notification, they can view additional details about the alert within the Looker mobile application.

You can also share a link to the alert directly with recipients by tapping the alert's three-dot menu and selecting **Share link** or **Copy link**.

**Note:** Recipients must have a Looker role that contains permissions to access the model that underlies the dashboard tile on which the alert is based.

## Alert push notifications

For alerts that are configured for email, once an alert is triggered, any specified recipients will receive a notification on their mobile device at the specified frequency. The banner or badge notification will include these elements:

  * The name of the alert owner
  * The value that triggered the alert
  * The name of the dashboard tile on which the alert is based
  * A link to view the dashboard tile on which the alert is based



When you tap the notification, the Looker mobile application opens and displays the following details about the alert:

  * The value that triggered the alert
  * The visualization for the tile on which the alert is based
  * The name of the dashboard tile on which the alert is based



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
