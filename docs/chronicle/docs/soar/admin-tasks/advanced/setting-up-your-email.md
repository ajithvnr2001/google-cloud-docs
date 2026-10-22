---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/setting-up-your-email/
title: Configure email settings \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:24:07.502051+00:00
---

# Configure email settings  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/setting-up-your-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure email settings

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can set up an email box in Google Security Operations to send emails to users. When you select the default Google SecOps Simple Mail Transfer Protocol (SMTP) configuration, the platform's email service sends your emails. You can also select the **Customer Configuration** option to use your own email service to send your emails. 

This document explains how to set up your email box using Microsoft Azure.

## Before you begin

  1. Sign in to the Microsoft Azure portal.
  2. Go to **Users > Active Users**.
  3. Select the Google SecOps user and click **Mail**.
  4. In the **Email apps** section, click **Manage email apps**.
  5. Verify that the **Authenticated SMTP** setting is enabled.
  6. Click **Save changes**.



## Set up Microsoft email settings

  1. Go to **Settings** > **Advanced** > **Email Settings**.
  2. Select **Customer Configuration**.
  3. Enter the required information for your organization.
  4. In the **Display name** field, enter the sender's email address.
  5. Select the **Use Exchange OAuth** checkbox. The **Azure Client ID** and **Azure Tenant ID** fields display.



## Get Azure IDs and enable permissions

To get the required IDs and enable this feature in Microsoft Azure, follow these steps:

  1. Sign in to the Microsoft Azure portal.
  2. Click **App Registrations**.
  3. Locate the OAuth mail application app you previously created.
  4. Store the **Application Client ID** and **Tenant ID**. You can use the IDs later in the Google SecOps platform.
  5. Go to **Manage** > **Advanced Settings** and set **Allow public client flows** to **Yes**.
  6. In the **API Permission** tab, grant the following permissions: 
     * `IMAP.AccessAsUser.All`
     * `SMTP.Send`
  7. Click **Save**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
