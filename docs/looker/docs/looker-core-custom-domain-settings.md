---
url: https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings/
title: View information about a Looker (Google Cloud core) custom domain \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:33.744388+00:00
---

# View information about a Looker (Google Cloud core) custom domain  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  View information about a Looker (Google Cloud core) custom domain Stay organized with collections  Save and categorize content based on your preferences. 

You can view the status and configuration details for the custom domains that are mapped to your Looker (Google Cloud core) instance on the **CUSTOM DOMAIN** tab of the instance details page in the Google Cloud console. You navigate to the instance details page by clicking on the instance name from the [**Instances** page](https://docs.cloud.google.com/looker/docs/looker-core-view-console). This information helps you verify that your domain is correctly set up and operating, allowing users to access your instance through a custom URL. This page explains how to find and interpret the custom domain information that's displayed in the console.

The settings are as follows:

  * **Status** : An icon that summarizes the status of the domain, as described in more detail in the second **Status** column.
  * **Domain** : The domain that is associated with the instance.
  * **Record Type** : The type of DNS record that is associated with the domain.
  * **Data** : The IP address that is associated with the domain's DNS record.
  * **Status** : A description of where the domain is in the provisioning and verification process.

    * **Unverified** : A DNS record has not been created, or the record's IP address doesn't match the appropriate IP address for the type of network connection that the instance is using. For instances that use only private networking, the status may remain **Unverified** because Google cannot verify private DNS records or reach internal IP addresses for your instance. Even if the status is **Unverified** , you can still use the custom domain.

    * **Verifying** : The domain verification is in progress.

    * **Modifying** : The domain modification is in progress.

    * **Available** : The custom domain is ready to use.

    * **Unavailable** : The custom domain is provisioned to the Looker (Google Cloud core) instance but the SSL certificate is not ready.

  * **VERIFY DOMAIN** : For domains that are unverified, a **VERIFY DOMAIN** button appears. Click the button to verify the domain. An error appears in a window on the page if the domain cannot be verified.

  * **Delete** : The **Delete** trash icon lets you [delete a custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-delete).


**Note:** You cannot modify a custom domain once it is created. If you want to make changes to the custom domain, you must delete the existing custom domain and create a new one.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
