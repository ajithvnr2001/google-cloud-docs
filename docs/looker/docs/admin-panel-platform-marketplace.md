---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace/
title: Admin settings - Marketplace \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:40.896766+00:00
---

# Admin settings - Marketplace  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

The [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) is a central location for finding, deploying, and managing any type of Looker content, such as Looker Blocks, applications, visualizations, and plug-ins.

The **Marketplace** page in the **Platform** section of the **Admin** menu lets you configure settings for the Looker Marketplace.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.**Note:** Looker (Google Cloud core) instances that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa) connections don't include this page.

## Marketplace

The **Marketplace** option enables the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace). This option is enabled by default. When this option is disabled, the Marketplace icon is hidden, and users won't be able to access the Marketplace to install or manage applications.

## Auto Install

The **Auto Install** option, when enabled, causes some Looker-built applications to automatically install and update on your Looker instance. The [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) is the only extension that will automatically install, but more Looker-built applications may be added in the future.

When you enable **Auto Install** , Looker displays the **Enabling Marketplace Auto Install** dialog. The dialog contains license information and a list of necessary entitlements and permissions that are required to install and run Looker-built extensions.

Click **Accept**. Looker will install any Looker-built extensions that are not yet installed. Then, every eight hours, Looker checks to see if there are any Looker-built extensions that need to be installed or updated. If there are, Looker will install the new extension or extensions and make any available updates to existing extensions at that time.

After you accept the license and entitlements, Looker returns you to the **Marketplace** page with **Auto Install** enabled.

If you enable **Auto Install** but do not enable the **Marketplace** option, Looker displays an error and won't run auto install until the **Marketplace** option is enabled.

If the [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) option is not enabled, auto install will still occur but any extensions installed will not be available to users until the **Extension Framework** option is enabled.

Any installed Marketplace content, such as the [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer), can be accessed only by users who have the proper permissions and access to the associated models. For more information, see the [Setting permissions for Looker extensions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions#permissions_to_install_extensions_from_the_looker_marketplace) documentation page.

If you uninstall an auto installable application when **Auto Install** is enabled, the application will no longer be automatically installed and updated. To reverse this, either manually install the application again while **Auto Install** is enabled, or turn **Auto Install** off and back on again.

## Auto Update Looker applications

The **Auto Update Looker applications** option, when enabled, causes some Looker-built applications to automatically update on your Looker instance.

Every eight hours, Looker checks for available updates for the Looker-built applications on your instance. If Looker finds updates, Looker then updates the existing applications.

The **Auto Update Looker applications** option doesn't check any applications for updates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
