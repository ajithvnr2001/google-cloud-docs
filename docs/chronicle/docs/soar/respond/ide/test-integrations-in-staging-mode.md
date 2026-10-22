---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/test-integrations-in-staging-mode/
title: Test response integrations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:52.763951+00:00
---

# Test response integrations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/test-integrations-in-staging-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test response integrations 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document outlines the best practices for managing response integrations in Content Hub. When updates are available and to prevent disruptions, we recommend that you first download and test updates in your Integrated Development Environment (IDE) staging mode before you deploy to production.

**Staging** mode offers all the basic features of the production default mode of the IDE. For details on all available features, refer to [ Use the IDE](https://docs.cloud.google.com/chronicle/docs/soar/respond/ide/using-the-ide).

## Before you begin

Make sure you have **All Environments** selected in your permission group.

For more information, see [ Work with permission groups](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/permissions/working-with-permission-groups).

## Use the IDE in staging mode

The IDE contains two modes:

  * Production (default mode)
  * Staging



## Add an integration

These are the ways you can add an integration to the staging mode: 

  * **Install** an integration from the **Content Hub**.
  * **Push** an integration from production to staging mode.
  * **Import** an integration.



### Install the integration from the Content Hub

To install the integration from the Content Hub, follow these steps:

  1. In the main menu, click **Response > IDE**.
  2. Click the toggle from **Production** mode to **Staging** mode to turn on staging mode.
  3. Click **Confirm** on the warning message.
  4. Click  list **Menu** and select **Install from Marketplace (Content Hub)**.
  5. Choose an integration and click **Install**.



### Push the integration from Production to Staging

Pushing the integration to **Staging** mode creates a copy of the production integration, including its version number and all its certified and custom items, in the staging environment.

To push the integration into **Staging** mode, follow these steps:

  1. In the IDE, locate the required integration.
  2. Click  more_vert  **More > Push to staging**.
  3. Click the toggle from **Production** mode to **Staging** mode; you can now work with this integration in **Staging** mode.



### Import an integration or integration items

You can import an entire package or specific integration items directly into the **Staging** mode. To do this, follow these steps:

  1. Click  list **Menu** and select one of these options:
     * **Import Package**
     * **Import Items**. To import individual items, you first must select the integration to import them into.
       1. Locate the package or items you want to import.
       2. Click **Import**.



## Configure the integration instance

Before you can perform any tests on the integration, you first must create an instance for each integration in **Staging** mode. The integration instance is a specific staging instance and won't appear in the **Integration Configuration** page.

**Note:** You can create only one staging instance for each integration. For information on how to configure multiple instances, see [ Support multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

To configure an instance, follow these steps:

  1. In the IDE staging mode, locate the required integration. A yellow triangle by this integration indicates that you need to configure a staging instance. 
  2. Click  more_vert  **More > settings  Configure instance**.
  3. In the **Configure Instance** dialog, enter the following information:
     * **API Root** : The base URL for the service you're connecting to.
     * **API Secret** : A confidential key used to authenticate your application with the service.
  4. Click **Save**.



## Update the integration in IDE staging mode

When an update is available for an integration, an **Update** icon appears. You can see the version numbers for both the staging and production integrations by hovering over their icons.

  1. On the integration, click  more_vert  **More > Upgrade Integration**. This upgrades the integration to the latest version.
  2. Click **Save**. 
  3. Review the update and click **Confirm** on the override message that describes the items affected by the upgrade.



## Delete an integration

Deleting an integration in the **Staging** mode also deletes the integration and the instance. To delete an integration, follow these steps:

  1. On the selected integration, click  more_vert  **More > Delete**. 
  2. Click **Confirm**.



## Push an integration from Staging to Production

Once you've finished testing or upgrading the integration in **Staging** mode, you can push it to **Production** mode to replace the live version. We recommend that you test an integration in **Testing** first.

To push an integration from **Staging** into **Production** , follow these steps:

  1. On the selected integration, click  more_vert  **More > Push to production**. 
  2. Review the warning prompt and click **Confirm**.
  3. Click the toggle from **Staging** mode to **Production** mode. The integration now exists in both modes. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
