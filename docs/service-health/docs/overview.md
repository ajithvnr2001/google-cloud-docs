---
url: https://docs.cloud.google.com/service-health/docs/overview/
title: Personalized Service Health overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:29.157012+00:00
---

# Personalized Service Health overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-health/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Personalized Service Health ](https://docs.cloud.google.com/service-health/docs)
  * [ Guides ](https://docs.cloud.google.com/service-health/docs/overview)



Send feedback 

#  Personalized Service Health overview Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Personalized Service Health, which helps you identify Google Cloud service health events relevant to your projects so you can manage and respond to them efficiently. Details of these disruptions are available in the Google Cloud console and a variety of integration points.

## How Personalized Service Health works

The following diagram shows how Personalized Service Health makes service health events available.

![Personalized Service Health](https://docs.cloud.google.com/service-health/images/personalized-service-health.png)

You can access service health events by using the following:

  * **Service Health dashboard** : Track emerging and active Google Cloud incidents relevant to your projects or organization.
  * **Service Health API** : Pull service health event information for each project or organization.
  * **Alerts** : Get notified of events relevant to your projects. Alerts are based on logs in Cloud Logging.
  * **Logs** : Export logs related to Google Cloud events.



### How Personalized Service Health fits into Google Cloud incident communication

Personalized Service Health is your primary channel for incident information and service health events relevant to your projects.

Google Cloud uses multiple channels to communicate service health. To understand the roles of Personalized Service Health and the public Cloud Service Health (CSH) dashboard, see [Google Cloud incident communication](https://docs.cloud.google.com/service-health/docs/incident-communication).

### Dynamic product names during rebranding

To help you match event disruptions with commonly marketed terms, the API and dashboard display customer-facing monikers. When products are renamed or rebranded, events reference their mapped common monikers rather than just internal identifiers. For more information about dynamic display attributes, see the [Concepts guide](https://docs.cloud.google.com/service-health/docs/concepts#product-identity).

### View active and past Google Cloud incidents in the Service Health dashboard

The Service Health dashboard in the Google Cloud console shows incidents that are relevant to your project, their overall state, and the affected Google Cloud products and locations. For multi-product or multi-location incidents, the dashboard also displays the **granular disruption status** (**Affected** or **Resolved**) and recovery timestamp for each individual product and location, which lets you see partial recoveries while an incident remains active.

For more information about how to access the Service Health dashboard, see the [quickstart](https://docs.cloud.google.com/service-health/docs/view-events).

### View Google Cloud incidents and receive alerts on a mobile device

The Service Health dashboard is also [available on a mobile device](https://docs.cloud.google.com/service-health/docs/view-events#service-health-dashboard-mobile). 

To receive alerts on your mobile device, you can [configure an alerting policy](https://docs.cloud.google.com/service-health/docs/configure-alerts-cloud-logging).

### Request service health events using the Service Health API

The Service Health API lets you get service health events that might be affecting or have affected your project or organization, or get event details such as updates, start and end times, affected Google Cloud products and locations, and state.

For more information, see the [Service Health API reference](https://docs.cloud.google.com/service-health/docs/reference).

### Configure alerts or export logs through Cloud Logging

Personalized Service Health logs service health events in [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview), and lets you set up alerts based on these logs. You can set up alerts for conditions such as when new incidents are reported, when existing incidents are updated, or when incidents for specific Google Cloud products or locations are created or updated.

For more information about setting up an alert in the Service Health dashboard, see the [quickstart](https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard).

### View Google Cloud incidents for your applications

If you manage Google Cloud resources using [App Hub](https://docs.cloud.google.com/app-hub/docs/overview), [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview) lets you view Google Cloud incidents for your applications. This feature supports incidents that meet both of the following conditions:

  * Relate to [products that support App Hub](https://docs.cloud.google.com/app-hub/docs/supported-resources) and Gemini Cloud Assist.
  * Have [Related relevance](https://docs.cloud.google.com/service-health/docs/concepts#relevance).



If you don't have an application set up, to display incidents in Cloud Hub, do the following:

  1. [Configure a folder for application management](https://docs.cloud.google.com/resource-manager/docs/manage-applications).
  2. [Set up App Hub and create an application](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).
  3. If needed, ensure that you have the following permissions: 
     * `servicehealth.events.list`
     * `apphub.applications.get` on the specific application
     * `apphub.applications.list`
  4. If needed, [enable the App Hub API](https://console.cloud.google.com/marketplace/product/google/apphub.googleapis.com).



### Check for incidents affecting your organization

You can see active incidents affecting Google Cloud products and services using the following:

  * **Organization Views** : Provides a unified view of service health incidents affecting any project within your Google Cloud organization. Instead of checking individual projects, you can see aggregated information about affected services and projects at the organizational level. For more information, see [View organization incidents in Google Cloud console](https://docs.cloud.google.com/service-health/docs/organization-views).

  * **Service Health API** : Lets you get service health events that might be affecting or have affected your organization. For more information, see the [Service Health API reference](https://docs.cloud.google.com/service-health/docs/reference).




## Next steps

  * Learn more about [Google Cloud incident communication](https://docs.cloud.google.com/service-health/docs/incident-communication).
  * Review key [Personalized Service Health concepts](https://docs.cloud.google.com/service-health/docs/concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
