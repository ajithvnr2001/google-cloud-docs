---
url: https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud/
title: Configure a Salesforce Marketing Cloud instance for replication \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:52.166753+00:00
---

# Configure a Salesforce Marketing Cloud instance for replication  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-salesforce-marketing-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Salesforce Marketing Cloud instance for replication Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure a Salesforce Marketing Cloud instance to stream data to [supported destination](https://docs.cloud.google.com/datastream/docs/destinations) using Datastream.

## Before you begin

Before you start configuring Salesforce Marketing Cloud for use with Datastream, you need to:

  * Have access to an active Salesforce Marketing Cloud instance.
  * Have knowledge of how to navigate and change settings in Salesforce Marketing Cloud.



## Configure Salesforce Marketing Cloud for use with Datastream

To establish a connection between your Salesforce Marketing Cloud instance and Datastream, you need to generate API credentials. Datastream uses these credentials to facilitate secure, authenticated communication using the server-to-server OAuth 2.0 flow.

Follow these steps in your Salesforce Marketing Cloud instance to generate the necessary API credentials:

  1. In the Salesforce Marketing Cloud interface, navigate to the **Setup** menu.
  2. In the sidebar, go to **Platform Tools > Apps > Installed Packages**.
  3. Click **New** at the top right of the page to create a new package.
  4. In the **New Package Details** dialog, enter a name and a description for your package in the corresponding fields, and then click **Save**.
  5. In the details page for your newly created package, click **Add Component**.
  6. Select **API Integration** as the component type, and then click **Next**.
  7. Select the **Server-to-Server** integration type, and then click **Next**.
  8. Under **Scope** , define the required permissions. Make sure you provide **Read** permissions to all objects that you want Datastream to replicate.
  9. Click **Save**.
  10. Salesforce Marketing Cloud generates your credentials. Make sure that you store the **Client ID** and **Client Secret** in a secure location. You need these when you create a Salesforce Marketing Cloud connection profile.
  11. Click **Finish**.
  12. Take note of the **subdomain** name for your instance. You can find it in the **Authentication Base URI** section of the **API Integration** page. The subdomain is the string between the `https://` and `.auth.marketingcloudapis.com/` parts of the URI. For example, if your URI is `https://SUBDOMAIN.auth.marketingcloudapis.com/`, then your subdomain name is `SUBDOMAIN`. You need the subdomain name when you create a Salesforce Marketing Cloud connection profile.



## What's next

  * Learn more about the [Salesforce Marketing Cloud source](https://docs.cloud.google.com/datastream/docs/sources-salesforce-marketing-cloud).
  * Learn how to create a [Salesforce Marketing Cloud](https://docs.cloud.google.com/datastream/docs/create-connection-profiles#cp4salesforcemarketingcloud) connection profile.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
