---
url: https://docs.cloud.google.com/migration-center/docs/installation-process/
title: Install and configure the Discovery client \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:47.491320+00:00
---

# Install and configure the Discovery client  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/installation-process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Install and configure the Discovery client Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to install and set up the discovery client for data collection.

## Before you begin

If you plan to upload the collected data to Migration Center, you need to meet the following requirements:

  * You need to set up a Google Cloud project and activate Migration Center. For more information, see [Get started with Migration Center](https://docs.cloud.google.com/migration-center/docs/get-started-with-migration-center).
  * Enable the [Cloud Resource Manager API](https://console.cloud.google.com/apis/library/cloudresourcemanager.googleapis.com).
  * As part of the installation process, the discovery client needs to create a new service account on your behalf. If you don't have the required permissions to create a service account, ask your organization administrator to provide you with the access key to a valid service account. For more information, see [Troubleshoot permissions and service accounts](https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client).



## Download and install the discovery client

To install the discovery client, follow these steps:

  1. Download the discovery client on a Windows machine that can access the other machines in your infrastructure.

[Download the discovery client](https://storage.googleapis.com/mc-release/mcdc/current/windows/mcdc.msi)

  2. Run the discovery client installer as a local administrator.

  3. Review and accept the license agreement.

  4. Follow the instructions on the screen to complete the installation.

  5. At the end of the installation, restart your machine.

  6. After the installation is complete, you can see a new application shortcut on your desktop.


**Warning:** The local database is encrypted by using the [Windows Data Protection API](https://learn.microsoft.com/en-us/previous-versions/ms995355\(v%3Dmsdn.10\)). Resetting the Windows user password can cause the loss of all locally collected data.

## Decide if you want to upload data to Migration Center

The first time you open the discovery client application, you need to choose if you want to automatically upload the collected data to Migration Center. You can use the discovery client in two ways:

  * If you enable data upload (connected mode), the discovery client automatically sends the collected data to Migration Center, where you can perform the assessment. Connected mode requires a connection to the Internet. This is the recommended mode for most situations.
  * If you don't enable data upload (disconnected mode), the discovery client stores the collected data locally and can work without Internet connection. You can send the collected data to Migration Center later to complete the assessment.



### Work in connected mode

To work in connected mode and let the discovery client send data to Migration Center, click **Log in to Migration Center**.

After you click the **Log in to Migration Center** button, the discovery client performs a connection check. Then, you need to configure the connection with Migration Center with the following steps:

  1. Sign in with the Google Account that you use to sign in to Migration Center.
  2. Choose the Google Cloud project where you want to collect the data by entering the project name or ID. Then, click **Continue**.
  3. If your organization has policy restrictions that prevent you from creating a service account, ask your organization administrator to create a service account with assigned the `Migration Center discovery client` role. In the **Add an access key** step, upload the service account key that your administrator gave you. If you have issues with the authorization, see [Troubleshoot permissions and service accounts](https://docs.cloud.google.com/migration-center/docs/troubleshooting/troubleshoot-discovery-client).
  4. Enter a name for the discovery client.
  5. Click **Authorize**.



### Work in disconnected mode

If you want to work in disconnected mode, the first time you open the discovery client application, click **Continue without logging in**.

### Switch from disconnected mode to connected mode

If you work with the discovery client in disconnected mode, you can decide to activate the connected mode at any time. This lets you send all the data that you already collected to Migration Center, where you can perform the remaining parts of your assessment.

To activate the connected mode on the discovery client, follow these steps:

  1. In the discovery client application, go to the **Overview** tab.
  2. In the banner, click **Activate to add data**.
  3. Follow the steps to configure the connection with Migration Center.



## Grant access to other users

During the installation, the discovery client creates a Windows user group called `MCDCUsers`, which controls who can access the application. By default, only the user who installs the applications and the VM administrators are automatically added to the group, and can access the application.

To grant access to the discovery client to other users, add the user names to the `MCDCUsers` group from the **Computer Management** console of your VM. After you add the users, restart your VM to apply the changes.

## What's next

  * Learn more about the [collection methods in the discovery client](https://docs.cloud.google.com/migration-center/docs/collection-methods).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
