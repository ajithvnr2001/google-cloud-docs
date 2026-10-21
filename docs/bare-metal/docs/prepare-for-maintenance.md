---
url: https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance/
title: Prepare for a maintenance event \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:38.934668+00:00
---

# Prepare for a maintenance event  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/prepare-for-maintenance/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/bare-metal/docs/bms-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare for a maintenance event

This page explains the required steps to prepare for a maintenance event that requires server downtime.

You must complete the following steps before the start of a scheduled maintenance event. Following these steps helps you minimize maintenance-related disruptions. 

**Warning:** Failure to complete these preparatory steps before the maintenance event starts can result in the cancellation of the maintenance event.

  * Disable the services and scripts that automatically start at power up.
  * Safely migrate or stop applications and databases that are running on the server.
  * Silence any monitoring and alerting associated with the server to avoid alerting on planned maintenance.
  * Disable autostart and autojoin functionality of applications and clusters to avoid returning the server to operation until the maintenance event ends.
  * Reboot the server 24-48 hours prior to the maintenance event start time. Reboot is required to confirm that the server is functioning well before the maintenance.
  * Power off the server 1 hour before the maintenance event start time.



After you complete these steps, we don't require additional confirmation.

## What's next

  * [View your maintenance events](https://docs.cloud.google.com/bare-metal/docs/manage-maintenance-events#view-maintenance-event).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
