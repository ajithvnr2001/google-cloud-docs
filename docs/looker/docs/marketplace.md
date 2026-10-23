---
url: https://docs.cloud.google.com/looker/docs/marketplace/
title: Using the Looker Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:16.706695+00:00
---

# Using the Looker Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Using the Looker Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

The Looker Marketplace is a central location for finding, deploying, and managing [Looker Blocks](https://docs.cloud.google.com/looker/docs/glossary#block), [applications](https://docs.cloud.google.com/looker/docs/glossary#extension), [custom visualizations](https://docs.cloud.google.com/looker/docs/glossary#visualization), and [actions](https://docs.cloud.google.com/looker/docs/glossary#action-hub). This page describes how to access the Looker Marketplace and how to install its content for use within a Looker instance.

## Looker Marketplace permissions

No permissions are needed to browse content on the standalone Marketplace instance; however, you won't be able to install Marketplace content for use with your Looker instance.

See the following table for an overview of the permissions that are required to perform the actions that are described on this page.

Task | Required role or permission  
---|---  
Enable Marketplace setting | [Admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles)  
View the Marketplace icon | [access_data](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data)  
Browse content from the Looker Marketplace that is associated with your Looker instance | [access_data](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data)  
Install content from the Marketplace | [develop](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [manage_models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [deploy](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy)  
Install content from git URL | [develop](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [manage_models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [deploy](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy)  
Manage installed tools | [develop](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [manage_models](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [deploy](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy)  
Use applications | Depends on the extension  
Use visualizations or plug-ins | [explore](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore)  
Use models or Blocks | Depends on the model or Block  
  
## Enabling access to the Looker Marketplace and its content

To enable users to access and install content from the Looker Marketplace, a Looker admin must follow these steps:

  1. Navigate to the **Marketplace** page in the **Platform** section of the **Admin** panel.
  2. Turn on the **Marketplace** setting. This setting is enabled by default.
  3. Optionally, enable the **Auto Install** setting. When enabled, this setting causes some Looker-built applications to install and update automatically on your Looker instance.
  4. Optionally, enable the **Auto Update Looker applications** setting. When enabled, this setting causes some Looker-built applications to update automatically on your Looker instance.



See the [Admin settings – Marketplace](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) documentation page for more information on these settings.

**Note:** Looker (Google Cloud core) instances that use [private services access](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psa) connections don't support Marketplace. Looker (Google Cloud core) instances that use [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#psc) connections can [connect to the Marketplace](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#connect-to-marketplace) through the Google Cloud console.

Some Marketplace content requires additional features to be enabled. To install [extensions](https://docs.cloud.google.com/looker/docs/glossary#extension), a Looker admin must follow these steps:

  1. Navigate to the **Extension Framework** page in the **Platform** section of the **Admin** panel.
  2. Turn on the **Extension Framework** setting. When enabled, this setting allows developers to build and run Looker-hosted applications as well as install and run extensions from the Looker Marketplace, such as the Data Dictionary.



See the [**Admin settings – Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) documentation page for more information on this setting.

## Discovering Looker Marketplace content

You can browse content on the Looker Marketplace by selecting the **Marketplace** storefront on the Looker menu bar. (If you have the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) permissions, selecting **Marketplace** will open a menu of options; select **Discover**.)

To find content, use the search bar. You can use the **Applications** , **Models** , **Visualizations** , and **All** filters that appear near the search bar to filter for different types of content. Narrow your results by tag, category, industry, and author using the filter checkboxes on the left side.

Next, you can install the selected tool.

## Installing a tool from the Marketplace that is associated with your instance

**Important:** All Marketplace content is labeled with its author, whether it was developed by Google or a third-party developer. Before you download or purchase content from the Marketplace, be sure that you have evaluated the third-party developer and tool. Google shares with the developer aggregated, non-identifying and non-profiling, statistical information regarding the performance of their tool in the marketplace, such as upload and deletion counts. These third-party developers are not subprocessors to Looker.

The installation process varies depending on the tool you are installing. Applications and some models, for example, have the option to connect the tool to your source database. The following procedure shows all the possible installation options; however, depending on the tool you are installing, you may only see a subset of the following steps.

**Tip:** For best performance, always install the latest version of any Marketplace tool. Some visualizations serve JavaScript in the [`file:` subparameter](https://docs.cloud.google.com/looker/docs/reference/param-manifest-visualization). If you have the most recent update of the visualization installed and the visualization is not rendering, you must enable Looker cookies in your browser.

To install a tool from the Looker Marketplace, follow these steps:

  1. Make sure you have at least the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) permissions.

  2. From the Marketplace main menu, select the tool that you want to install, and then select its tile.

Looker displays the tool's installation page, which shows a short description of the tool and any needed information about installing and using the tool.

  3. Select **Install** or **Install Free Trial**.

  4. Looker displays pages asking you to accept the tool's license agreements and the Looker permissions that are required by the tool. If you want to accept the license agreements and permission requests, select **Accept** on these pages.

  5. Each tool requires some configuration information that is specific for that tool, such as a connection name or visualization label. Select or enter the configuration information, and then select **Install**. (After the installation is complete, you can change this configuration information at any time by using the **Manage** page.)

  6. Looker will complete the installation. You can now use the installed content.




See the [Customizing Looker Marketplace Blocks](https://docs.cloud.google.com/looker/docs/marketplace-customize-blocks) documentation for information on customizing **Models** or Blocks that you have installed from the Marketplace.

### Automatically installing Looker-built applications

If your Looker admin has enabled the [**Auto Install**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace#auto_install) option in the [**Marketplace**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) page in the **Platform** section of Looker's **Admin** menu, some Looker-built applications will automatically install and update on your Looker instance. The [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) is the only extension that will automatically install, but more Looker-built applications may be added in the future.

For more information, see the [Admin settings - Marketplace](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) documentation page.

## Installing a tool from a Git URL

To install models and plug-ins directly from the Git repository, follow these steps:

  1. Select the **Marketplace** button on the Looker menu bar storefront.

  2. From the Marketplace menu, select the **Manage** option.

  3. On the **Manage** page, select the three-dot **Options** button more_vert.

  4. Click the **Install via Git URL** button.

  5. Looker shows the **Install via Git** page. Enter the URL and commit SHA of the repository and the version of the tool or visualization that you want to install.

  6. Select **Install**.




## Installing a tool from the Marketplace instance

To install a tool from the Marketplace instance, perform the following steps:

  1. Navigate to the [Looker Marketplace Directory](https://marketplace.looker.com/marketplace/directory).
  2. Select an action, application, Block, or plug-in.
  3. Select **See Code** and navigate to the tool's `READ.ME` file.
  4. Follow the `READ.ME` file's installation instructions.



## Using Looker Marketplace content

Installed Marketplace content appears in the following places of a Looker instance:

  * Applications or extensions are listed in the **Applications** menu
  * Models or Blocks are listed in the **Blocks** menu — users will be able to access only the installed packages that are based on the models to which they have been [granted access permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets)
    * Any Explores built for the tool appear in Looker's **Explore** menu prepended with **Marketplace**
    * The tool's LookML appears in the **Develop** menu prepended with `marketplace_`
  * Visualizations or plug-ins appear in the **Visualization** menu in an Explore



See the [Customizing Looker Marketplace Blocks](https://docs.cloud.google.com/looker/docs/marketplace-customize-blocks) documentation for information on customizing the blocks that you have installed from the Marketplace.

## Managing installed tools

If you have at least the [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_models), and [`deploy`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) permissions, you can use the **Manage** page to manage the tools that are installed on your Looker instance.

To navigate to the **Manage** page, follow these steps:

  1. Select the **Marketplace** button on the Looker menu bar storefront.

  2. From the Marketplace menu, select the **Manage** option.




The **Manage** page displays a list of all tools installed on your Looker instance. From the **Manage** page, you can also update tools, open tools, change a tool's configuration, or uninstall tools.

## Related resources

  * [Customizing Looker Marketplace Blocks](https://docs.cloud.google.com/looker/docs/marketplace-customize-blocks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
