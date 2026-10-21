---
url: https://docs.cloud.google.com/iap/docs/managed-oauth-client/
title: Enable IAP using a Google-managed OAuth client \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:53.676355+00:00
---

# Enable IAP using a Google-managed OAuth client  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/managed-oauth-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  Enable IAP using a Google-managed OAuth client Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to enable Identity-Aware Proxy (IAP) for a Google Cloud resource, using a Google-managed OAuth client.

When enabling IAP on a resource using a Google-managed OAuth client, only users within the organization in which the resource is contained can access that resource. If you want to allow users outside of the organization access to an IAP-enabled resource, enable custom OAuth credentials.

## Enable IAP for a new resource

New Google Cloud resources don't have IAP enabled. Complete the following steps to enable IAP on a new resource.

  1. In the Google Cloud console, go to the IAP page.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Click the **Applications** tab.

  3. From the list of resources, select the resource for which you want to enable IAP.

  4. In the **IAP** column, click the toggle to the on position.

  5. For the **Turn on IAP** option, click **Turn on**.




## Set up custom OAuth credentials for a resource

To allow users outside of the organization access to an IAP-enabled resource, complete the following steps.

  1. In the Google Cloud console, go to the IAP page.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Click the **Applications** tab.

  3. In the list of resources, go to the settings of the resource for which you want to configure custom OAuth credentials.

  4. Select the **Enable custom OAuth credentials to allow users outside of this organization to access this application** checkbox.

  5. In the **OAuth configuration** dialog, enter a client ID and secret.

  6. Optional: To have a client ID and secret generated for you, click **Auto generate credentials**.

You can download the client credentials to a CSV file, or delete the credentials. After you save your changes, custom client credentials cannot be retrieved, so we recommend that you save your credentials.

If you delete the credentials, the auto-generated OAuth client is also deleted.

  7. To save your changes, Click **Save**. Saving your changes does not change the IAP enabled state.




## Change to a Google-managed OAuth client

You can change resources using a custom OAuth client to use a Google-managed OAuth client by completing the following steps.

  1. In the Google Cloud console, go to the IAP page.

[ Go to the IAP page](https://console.cloud.google.com/security/iap)

  2. Click the **Applications** tab.

  3. In the list of resources, go to the settings of the resource for which you want to change to use a Google-managed OAuth client.

  4. Deselect the **Enable custom OAuth credentials to allow users outside of this organization to access this application** checkbox.

  5. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
