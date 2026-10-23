---
url: https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials/
title: Create and manage credentials \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:54.568545+00:00
---

# Create and manage credentials  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/create-and-manage-credentials/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback 

#  Create and manage credentials Stay organized with collections  Save and categorize content based on your preferences. 

As part of your data collection process, you need to define one or more credentials that discovery client can use to access your assets.

A credential provides a way to access parts of your infrastructure that share the same credentials. discovery client uses this credential to access all the assets attached to it, unless you specify different credentials for an individual asset.

When you add a set of credentials, they are saved locally in your system and encrypted. **Credentials are never sent to Migration Center** , even if you're using the discovery client in connected mode.

This document describes how to create a credential and add assets to it.

### Before you begin

  * To add credentials for Windows servers, you need an account with administrator rights to the servers.
  * To add credentials for Linux servers, you need an account with user-level access (no sudo or root privileges required).



### Limitations

  * The discovery client supports adding up to 1000 credentials.



### Add credentials for servers

To scan Linux and Windows servers, add new operating system credentials in the discovery client with the following steps:

  1. Click **Credentials** , then click **Add credentials**.
  2. To enter the details, click **Add OS credentials**.
  3. Enter a name to identify your credentials, then select one of the credential types available. 
     * **Username & Password**: applicable to both Windows and Linux collections. 
       * Enter domain accounts as `DOMAIN\USERNAME`.
       * Enter local accounts as `.\USERNAME`.
     * **SSH Key / Certificate** (Linux only): you can connect to a Linux machine using SSH with a certificate-based authentication instead of using a username and password combination. Enter the username and password for the certificate, then upload a new private key in the PEM format.
  4. To confirm, click **Save**.



### Add vCenter Credentials

To scan a vCenter source, add the new vCenter credentials in the discovery client with the following steps:

  1. Click **Credentials** , then click **Add credentials**.
  2. To enter the details, click Select **Add vCenter credentials**.
  3. Enter a name to identify the credentials.
  4. Enter the username.
  5. Enter the password.
  6. To confirm, click **Save**.



## What's next

  * Learn how to [add servers to a credential](https://docs.cloud.google.com/migration-center/docs/add-servers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
