---
url: https://docs.cloud.google.com/migration-center/docs/manage-discovery-client/
title: Manage the discovery client \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:16.056106+00:00
---

# Manage the discovery client  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/manage-discovery-client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Manage the discovery client Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to manage the discovery client after you install it and how to perform basic maintenance activities.

## Upgrade the discovery client

To upgrade the discovery client, [download the latest version of the discovery client](https://storage.googleapis.com/mc-release/mcdc/current/windows/mcdc.msi) and run the MSI file as a local administrator on the machine. When you upgrade to the latest version, all your data is preserved, including the users you add to the `MCDCUsers` group.

If you encounter errors during the upgrade, see [Troubleshoot installation errors](https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client#troubleshoot_installation_issues).

## Review the discovery client details

In Migration Center, you can see the discovery clients that you're using in connected mode. To review the list of clients, follow these steps:

  1. In the Google Cloud console, go to the **Data import** page.

[Go to Data import](https://console.cloud.google.com/migration/discovery/dataImport)

If errors prevent the discovery client from connecting to Google Cloud Migration Center, you see a list of errors and warnings.

  2. Click **Clients**.

  3. Review the list of connected discovery client applications.

The table provides the following information for each client: 

Column | Description  
---|---  
**Name** | The discovery client name.  
**Status** | The status of the discovery client. For example, `Offline`.  
**Created** | The timestamp when the discovery client was first registered with Migration Center.  
**Last sync time** | The last recorded time that the discovery client successfully synchronized data with Migration Center.  
**Version** | The version of the discovery client.  
**Errors** | A short description of errors preventing the discovery client from connecting to Google Cloud Migration Center. For more information about the error, click **View details**.  
  4. To view the details about a specific discovery client, click the name of the discovery client.




## View the collected servers

If you use the discovery client in connected mode, after you collect data from your servers, you can view the collected data in the Google Cloud console. For more information, see [View the collected assets](https://docs.cloud.google.com/migration-center/docs/view-assets).

## Analytics data collection

The discovery client can collect usage data and other anonymized data that helps Google improve the product. If you agree to send analytics data to Google, the events and statistics that the discovery client collects might include the following:

  * Requests made to the discovery client service, for example when configuring a discovery method, changing configuration, and listing assets. The data includes the request duration and its success rate.
  * Periodic jobs running in the background, such as vCenter discovery, and IP range scan. The data includes high level statistics about the discovery method, such as the number of VMs in scope and the collection success rate.
  * Rates of specific predefined errors occurring in the discovery client.



For all events, the discovery client provides information on the current version of the application.

### Manage analytics collection

To manage the discovery client analytics collection, follow these steps:

  1. In the discovery client application, go to **Settings**.
  2. In the **Configure Analytics sent to Google** section, toggle if you want to enable or disable analytics data collection.



## Set up a proxy connection

The discovery client and the corresponding Windows services use the default proxy settings returned by Windows. In some cases, the `Local System` user doesn't have the proxy that is normally available for users logged into the system. In such cases, you can set the proxy settings in the discovery client with the following steps:

  1. In the discovery client application, go to the **Settings** tab.
  2. Click the **Proxy credentials** toggle to the **Enabled** position.
  3. Enter the proxy host and port.
  4. Enter the proxy credentials, if needed.
  5. To finish, click **Save proxy credentials**.



## What's next

  * Learn how to [add servers to discovery client](https://docs.cloud.google.com/migration-center/docs/add-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
