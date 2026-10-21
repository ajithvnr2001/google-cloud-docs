---
url: https://docs.cloud.google.com/service-health/docs/configure-alerts-pagerduty/
title: Configure alerts for PagerDuty \u00a0|\u00a0 Personalized Service Health \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:15.558013+00:00
---

# Configure alerts for PagerDuty  |  Personalized Service Health  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/configure-alerts-pagerduty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Configure alerts for PagerDuty Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to integrate Personalized Service Health with PagerDuty by:

  * Setting up PagerDuty alert notifications.
  * Synchronizing PagerDuty incidents with incidents in Personalized Service Health.



## Before you begin

[Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  1. [Enable the Service Health API](https://docs.cloud.google.com/service-health/docs/manage-access#enable-service-health-api-single-project) for the project that you want to create alerts for.
  2. Set [permissions to configure log alerts](https://docs.cloud.google.com/service-health/docs/manage-access#access_logs_and_configure_log_alerts).



## Set up an alert

Do the following:

  1. [Create a PagerDuty notification channel](https://cloud.google.com/monitoring/support/notification-options#pagerduty). Cloud Monitoring controls the state shown by PagerDuty.

  2. [Set up an alerting policy](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging#set_up_an_alerting_policy), which describes the circumstances under which you want to be alerted and how you want to be notified. You'll define the alert condition, where you can set fields such as the Google products, locations, and state.

  3. [Customize the content](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging#customize_the_content_of_the_alert) of the header and the alert notification.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
