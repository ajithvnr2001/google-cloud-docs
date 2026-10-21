---
url: https://docs.cloud.google.com/chronicle/docs/review-alert/
title: Review alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:39:54.089028+00:00
---

# Review alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/review-alert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review alerts

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide shows how to investigate an alert using Google Security Operations. 

### What is an alert?

An [alert](https://docs.cloud.google.com/chronicle/docs/investigation/alerts-iocs) is an Indicator of Compromise (IOC), flagged by [Google Security Operations](https://docs.cloud.google.com/chronicle/docs/overview), indicating an anomaly in the normal workflow of traffic within the enterprise. You should investigate alerts as a possible breach of security.

### How do alerts get to Google Security Operations?

Google Security Operations taps into various external sources within the security community using industry-wide databases updated continuously. Google Security Operations also has a feature-rich programming language, YARA-L, so you can craft your own custom rules.

For more information on YARA-L, see the [Overview of the YARA-L 2.0 language](https://docs.cloud.google.com/chronicle/docs/detection/yara-l-2-0-overview). For more information on rules, see [Manage Rules Using Rules Editor](https://docs.cloud.google.com/chronicle/docs/detection/manage-all-rules).

## Before you begin

You can perform these steps from your company's Google Security Operations instance or from the Google Security Operations demo environment.

Google Security Operations supports the Google Chrome and Mozilla Firefox browsers. Upgrade your browser to the most current version for optimal performance and security. The latest Chrome version is available for download at <https://www.google.com/chrome/>. Mobile operating systems (iOS/Android) and mobile browsers are not supported.

**Note:** You can access multiple Google SecOps instances within the same browser profile as long as you log in using the same user identity (the same Cloud Identity account or the same workforce identity pool). However, your active session is invalidated if you switch user accounts or access an instance configured with different workforce pool or different Google Cloud organization. To maintain concurrent sessions across different identities or authentication setups, use a separate browser profile or an incognito/private window for each session.

## Authentication and access

Google SecOps integrates with SSO solutions. Access to the Google SecOps platform requires valid enterprise credentials.

  1. Launch Chrome or Firefox.

  2. Verify you have active access to the corporate account.

  3. Go to the following URL and replace customer_subdomain with the customer-specific identifier to access the Google SecOps application:

`https://customer_subdomain.backstory.chronicle.security`




## View Alerts and IOC Matches

In the navigation bar, select **Detection > Alerts and IOCs**.

The Alerts and IOC Matches tabs are displayed. You may have to adjust the time range using the calendar control in the top right for matches and alerts to appear.

## Pivot to Asset view

Next, drill down to a particular asset that may have been compromised.

  1. From the IOC Matches tab, click on a domain to open Domain view.

  2. Select the Timeline tab.

  3. To pivot to Asset view, select an event by clicking on its time. Asset view shows details of the selected asset around the timeline of the alert trigger, as shown in the following figure.

![Asset View](https://docs.cloud.google.com/chronicle/images/qs/qs-alert-asset-view.png)**Asset view**

The bubbles in the main window represent the prevalence of the asset. The graph is arranged so events occurring less often are at the top. These low-prevalence events are considered suspicious. Use the Time slider in the upper right to zoom in to events requiring investigation.

  4. If the Procedural Filtering menu is not visible, open it by clicking the _Filter_ icon ![Filter icon](https://docs.cloud.google.com/chronicle/images/filtering-icon-c.png) (near the upper right corner).

  5. At the top of the menu, adjust the **Prevalence** slider to filter out common events. Using the Time and Prevalence sliders, to identify suspicious events.

  6. Open the alert from the Timeline sidebar list. In the left panel, select the Timeline tab which display events occurring around the alert. The triggering event is highlighted in green.




## Investigate what triggered the alert

There are several ways to gain more insight into the triggering event.

  * In the middle panel, an orange dialog box may appear above a small orange triangle indicating the location, in time, of the alert. If the dialog box is not displayed, hovering over the triangle causes it to appear. The dialog contains the date, time, and description of the alert.

  * The left panel in Asset view shows the Timeline tab. If the event is labeled _Rule Alert_ , it will also mention a description of the alert.

  * Hovering over the _Rule Alert_ event causes an _Expand_ icon ![Expand Event Icon](https://docs.cloud.google.com/chronicle/images/expand-event-icon-c.png) to appear on the right side of the event. Clicking on this icon will open a new window with more details about the event in UDM format, as shown in the following figure.

![Event Details](https://docs.cloud.google.com/chronicle/images/qs/qs-alert-event-details.png)**Event Details**




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
