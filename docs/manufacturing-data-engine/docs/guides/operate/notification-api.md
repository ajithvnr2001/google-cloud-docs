---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/notification-api/
title: Notification service \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:50.789598+00:00
---

# Notification service  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/notification-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Notification service

The notification service enables Manufacturing Data Engine (MDE) to send notifications to the user regarding updates in the processing status. This feature was introduced in release v1.4.0 to enable a more convenient way for the user to take action based on certain events without the need to manually check the logs.

In v1.4.0, this notification service has two different types of notifications:

  * A warning, when a metadata natural-key instance count is approaching the maximum limit (which is 200). This warning will be triggered when reaching 50% of the maximum hard limit. The user can check the metadata warning [page](https://docs.cloud.google.com/manufacturing-data-engine/docs/guides/operate/metadata-keys-warning) to filter through the natural keys that are approaching the deletion limit.
  * A notification, when the metadata natural-key instances are actually deleted from the MDE operational datastore in order to ensure the system performance.



In the web interface, the notifications will show up in the top-right corner of the screen. If you're using the Notification API, it supports the following operations:

  * Listing the reported notifications with the ability to filter by their status (for example, `read` and `unread`).
  * Mark a notification as `read`.
  * Delete read notifications.
  * Delete all notifications.



Future releases of MDE might include more notification types for a better user experience.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
