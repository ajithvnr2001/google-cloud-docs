---
url: https://docs.cloud.google.com/looker/docs/receiving-alerts/
title: Receiving alert notifications \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:14.427025+00:00
---

# Receiving alert notifications  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/receiving-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Receiving alert notifications Stay organized with collections  Save and categorize content based on your preferences. 

Alerts are configured to send their specified recipients or followers notification to email or Slack when the alert's conditions are met or exceeded. If the [Looker mobile application](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app) is enabled for your instance, alerts that send notifications to email also send push notifications to recipients who have the mobile application installed on their device.

## Alerts notifications to email

For alerts that are [configured for email notifications](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_email), once an alert is triggered, any specified recipients will receive an email notification at the specified frequency. The email will include these elements:

  * A link to the dashboard for the tile on which the alert is based. Dashboard links don't include any [`hide_filter` parameters](https://docs.cloud.google.com/looker/docs/filters-user-defined-dashboards#hiding_dashboard_filters).
  * The value that triggered the alert
  * The visualization for the tile on which the alert is based
  * Options to unfollow or, depending on your permissions and who owns the alert, to edit the alert
  * If [enabled](https://docs.cloud.google.com/looker/docs/creating-alerts#key_driver_analysis), the insights provided by **Gemini powered key driver analysis**.



If you choose to unfollow the alert, you will be removed from the alert's recipient list and will no longer receive notifications when the alert is triggered. If you unfollow on behalf of a group email address, group members will no longer receive notifications when that alert is triggered. If all recipients unfollow the alert, the alert is disabled. The alert owner may see that the alert status shows as **Active** on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) until the next time the alert query is run.

You will also receive a [push notification](https://docs.cloud.google.com/looker/docs/mobile-app-alerts#push-notifications) to your mobile device if the following is true:

  * The Looker instance has the [Looker mobile application enabled](https://docs.cloud.google.com/looker/docs/mobile-app-enablement).
  * The Looker instance is on Looker 26.6 or later.
  * You have the [Looker mobile application](https://docs.cloud.google.com/looker/docs/mobile-app-installation) installed on your mobile device.



### Email notifications of changes that may affect alerts

A user also receives emails when they or another Looker user has made a [change](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) to a dashboard or dashboard tile that is associated with an alert that they own. Users may receive different types of notifications depending on whether these changes maintain or break the synchronization between the alert and its dashboard or dashboard tile.

When changes _maintain_ the synchronization between the alert and the dashboard or dashboard tile:

  * Alert recipients receive an email notification once the alert is triggered, as usual.
  * Alert owners receive a separate email notifying them that a user has made a change to a dashboard or dashboard tile associated with their alert. No action is needed, but depending on the [change](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts), the dashboard tile data values may have changed in a way that invalidates the original alert. The alert owner can navigate to the [**Alert Details** page](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page) on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) for more information.



When changes _break_ the synchronization between the alert and the dashboard or dashboard tile:

  * For alerts [configured for email notifications](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_email), alert recipients receive an email notification once the alert is triggered, as usual; however, because the alert is unsynced from its dashboard, the visualization included in the email may not match the visualization on the dashboard tile.
  * Alert owners receive a separate email notifying them that a user has made a change to a dashboard or dashboard tile associated with their alert and that Looker was not able to apply these changes to the alert. Depending on the breaking [change](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts#editing_a_user-defined_or_lookml_dashboard), the alert owner may need to provide some [resolution](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts#resolving_an_unsynced_alert). From their email, the alert owner can navigate to the alert's [**Alert Details** page](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page) on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) for more information.



## Alerts notifications to Slack

Once the alert is triggered, anyone who is in the specified Slack channel or included in a direct message will receive a Slack notification at the specified frequency. The Slack notification will include these elements:

  * A PNG image of the dashboard tile visualization
  * A message with the name of the dashboard or the custom alert title and the conditions that triggered the alert
  * A link to navigate to the tile's dashboard
  * A link to [unsubscribe](https://docs.cloud.google.com/looker/docs/glossary#unsubscribe) from the alert notification
  * If [enabled](https://docs.cloud.google.com/looker/docs/creating-alerts#key_driver_analysis), the insights provided by **Gemini powered key driver analysis**.

**Note:** For [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options), the Slack notification will include the single value as text, rather than a PNG of the visualization.

### Slack notifications of changes that may affect alerts

[Changes](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts) to a dashboard or dashboard tile may carry over into the alert. Users may receive different types of notifications depending on whether these changes maintain or break the synchronization between the alert and its dashboard or dashboard tile.

When changes _maintain_ the synchronization between the alert and the dashboard or dashboard tile:

  * Alert recipients receive a Slack notification once the alert is triggered, as usual.
  * Alert owners receive a separate email notifying them that a user has made a change to a dashboard or dashboard tile associated with their alert. No action is needed, but depending on the [change](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts), the dashboard tile data values may have changed in a way that invalidates the original alert. The alert owner can navigate to the [**Alert Details** page](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page) on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) for more information.



When changes _break_ the synchronization between the alert and the dashboard or dashboard tile:

  * Alert recipients receive a Slack notification once the alert is triggered, as usual; however, because the alert is unsynced from its dashboard, the visualization included in the Slack message may not match the visualization on the dashboard tile.
  * Alert owners receive a separate email notifying them that a user has made a change to a dashboard or dashboard tile associated with their alert and that Looker was not able to apply these changes to the alert. Depending on the breaking [change](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts#editing_a_user-defined_or_lookml_dashboard), the alert owner may need to provide some [resolution](https://docs.cloud.google.com/looker/docs/effect-of-dashboard-edits-on-alerts#resolving_an_unsynced_alert). From their email, the alert owner can navigate to the alert's [**Alert Details** page](https://docs.cloud.google.com/looker/docs/user-alerts#alert_details_page) on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) for more information.



For the [Slack integration](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_the_slack_integration), the notification is sent from the Slack user who is associated with the alert owner; for the [Slack Attachment (API Token) integration](https://docs.cloud.google.com/looker/docs/creating-alerts#sending_alerts_to_the_slack_attachment_\(api_token\)_integration), the notification is sent from the bot user.

Slack recipients can [unsubscribe](https://docs.cloud.google.com/looker/docs/glossary#unsubscribe) from the alert by clicking the **Unsubscribe** button from the Slack message. If any Slack recipient unsubscribes from the alert notification, the alert is disabled. The alert owner may see that the alert status shows as **Active** on the [**Manage Alerts** user page](https://docs.cloud.google.com/looker/docs/user-alerts) until the next time the alert query is run.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
