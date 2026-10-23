---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress/
title: Configure static IP egress for third-party connectors \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:09.150607+00:00
---

# Configure static IP egress for third-party connectors  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/configure-static-ip-egress/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure static IP egress for third-party connectors Stay organized with collections  Save and categorize content based on your preferences. 

Gemini Enterprise data stores send outbound requests to third-party systems from a dynamic range of Google IP addresses. If the third-party system you're connecting to requires IP allowlisting, you'll need the outbound traffic from the connector to originate from a fixed set of IP addresses. Many third-party connectors support this through a static IP egress option, that is available when creating the data store.

When enabled, the data store routes all outbound requests to your third-party instance through a fixed, Google-managed set of IP addresses. You can then add those addresses to the allowlist on the source system. If static IP egress is not enabled, the data store continues to work using Google's dynamic egress ranges.

This page describes how static IP egress works, how to enable it, and how to add the assigned IP addresses to the allowlist on your third-party system.

## How static IP egress works

When you enable static IP egress on a data store:

  1. Gemini Enterprise assigns a fixed set of egress IP addresses to the data store at creation time.
  2. Post-authentication, all outbound calls from the data store to your third-party instance originate from that fixed set of IP addresses.
  3. The assigned IP addresses are visible on the data store's details page in the Google Cloud console.
  4. You add the assigned IP addresses to the allowlist on the third-party system.



If static IP egress is _disabled_ , the connector uses Google's general dynamic egress IP ranges.

## Supported data stores

Static IP egress is supported for most third-party data stores.

The **Enable Static IP Addresses** checkbox appears in the data store creation flow whenever the selected data store supports the feature. If the checkbox is not displayed for a data store, that data store does not support static IP egress.

## Enable static IP egress

You can only enable static IP egress when you create the data store. You cannot enable or disable static IP egress on an existing data store; to change the setting you must delete and recreate the data store.

  1. In the Google Cloud console, go to the **Gemini Enterprise** page and start the **Create data store** flow. For the list of thir-party data stores, see [Connect a third-party data source](https://docs.cloud.google.com/gemini/enterprise/docs/connect-third-party-data-source).
  2. Select your third-party source and complete the **Authentication** step.
  3. In the **Advanced options** step of the data source configuration, select the **Enable Static IP Addresses** checkbox.
  4. Complete the remaining steps of the data store creation flow.



After the data store is created, the assigned static IP addresses are surfaced on the data store's details page. See Retrieve the assigned static IP addresses for the exact location.

## Retrieve the assigned static IP addresses

  1. In the Google Cloud console, go to the **Gemini Enterprise** page and click **Data stores**.
  2. Click the name of the data store that you created.
  3. On the data store details page, locate the **Static IPs** section. The list of assigned egress IP addresses is displayed there.
  4. Copy the complete list of IP addresses. You need to allowlist all of them on the third-party system.



## Limitations

  * Static IP egress is configured per data store and cannot be modified after data store creation.

  * The assigned IP addresses are Google-managed and cannot be customer-selected.

  * Availability of the feature for a specific data store is determined by whether the **Enable Static IP Addresses** checkbox appears in the create data store flow.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
