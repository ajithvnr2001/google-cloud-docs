---
url: https://docs.cloud.google.com/security-command-center/docs/modify-scc-to-azure-connector/
title: Modify the connector for Azure \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.217496+00:00
---

# Modify the connector for Azure  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/modify-scc-to-azure-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Modify the connector for Azure Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The following document describe how to modify the Azure connector configuration after it has been configured for the first time. If you encounter errors, see the [Troubleshooting](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure#troubleshooting-connection) section.

## Before you begin

Make sure you have the permissions described in [Connect to Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure#before-begin).

### Edit the Azure connector

You can change the location and subscriptions collected by the connector and the user-assigned managed identity. The following fields cannot be modified:

  * **Azure tenant ID**
  * **Service agent ID**



To change the values of these fields, you must delete the Azure connector and set up a new connection.

  1. Open the **Connectors** tab on the **Settings** page.

[Go to Connectors](https://console.cloud.google.com/security/command-center/config/connectors)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. In the **Connectors** table > **Azure** row, click more_vert **More options > Edit**.

  4. On the **Configure connector** page, you can change the following configuration:

     * **Azure subscriptions**
     * **Azure locations**
     * **Grant permissions for Sensitive Data Protection discovery**
  5. Click **Continue**

  6. On the **Connect to Azure** page, you can change the following configuration:

     * **Managed identity client ID**
     * **Managed identity object ID**
  7. Click **Continue** , .

  8. In the **Test connector** page, click **Test Connector** to verify that Security Command Center can connect to the Microsoft Azure environment.

If the connection is successful, the Google Cloud service agent assumes the Microsoft Azure user-assigned managed identity and has the required Microsoft Azure and Microsoft Entra permissions. If the connection isn't successful, see [Troubleshooting errors when testing the connection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure#troubleshooting-connection).

  9. Click **Save**. The **Connectors** page appears.




### Delete the Azure connector

  1. Open the **Connectors** tab on the **Settings** page.

[Go to Connectors](https://console.cloud.google.com/security/command-center/config/connectors)

  2. Select the organization where you activated Security Command Center Enterprise.

  3. In the **Connectors** table > **Azure** row, click more_vert **More options > Delete**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
