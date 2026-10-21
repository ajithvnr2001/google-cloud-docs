---
url: https://docs.cloud.google.com/integration-connectors/docs/setup-integration-connectors/
title: Set up Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:41:12.172429+00:00
---

# Set up Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/setup-integration-connectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Integration Connectors

This page describes how to setup (provision) Integration Connectors in the Google Cloud console. 

## Setting up Integration Connectors

To successfully set up Integration Connectors for your Google Cloud project, perform the following steps: 

  1. In the [Cloud console](https://console.cloud.google.com/), select your Google Cloud project. 
  2. Search for **Integration Connectors** in the search bar and select **Integration Connectors**. This shows the **Overview** page. 
  3. In the **Overview** page, click **Set up integration connectors**. This shows the **Set up integration connectors** panel.
  4. Click **Enable APIs**. The following APIs are enabled:  API Name  | Location  | Description   
---|---|---  
[Secret Manager API](https://console.cloud.google.com/apis/library/secretmanager.googleapis.com) | secretmanager.googleapis.com  | Stores sensitive data such as API keys, passwords, and certificates. Provides convenience while improving security.   
[Connectors API](https://console.cloud.google.com/apis/library/connectors.googleapis.com) | connectors.googleapis.com  | Enables users to create and manage connections to Google Cloud services and third-party business applications using the Connectors interface.   

**Note:** You will be billed for usage of a generally available connector version as per the prices mentioned in the [pricing page](https://docs.cloud.google.com/integration-connectors/docs/pricing). You aren't charged for using connectors in preview. To know when a connector version has moved from preview to general availability, you can use of the following approaches: 

  * Subscribe to the [Integration Connector release notifications](https://docs.cloud.google.com/integration-connectors/docs/release-notes).
  * Regularly check for the presence of the `Preview` label next to the connector name in the [List connections page](https://console.cloud.google.com/connectors/connections). If a connector doesn't have the `Preview` label, it means that the connector is generally available.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
