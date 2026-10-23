---
url: https://docs.cloud.google.com/service-extensions/docs/manage-plugins/
title: Manage plugins \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:48.981146+00:00
---

# Manage plugins  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/manage-plugins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Manage plugins Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can view, edit, and delete plugins [created using Service Extensions](https://docs.cloud.google.com/service-extensions/docs/create-plugin).

The plugins feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Media CDN.

For a product overview, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

## View plugins

This section describes how you can view plugins and plugin versions created using Service Extensions.

### List plugins

To list the plugins in your project, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

A list of the plugins appears in a sortable table with the following information:

     * **Status** : the status of the plugin. If a service isn't attached, the value is `Not attached`. If a service is attached with a plugin, the value is `Attached`.
     * **Name** : the name of the plugin.
     * **Main version** : the active version of the plugin.
     * **Product** : the Google Cloud product to which the plugin is attached.
     * **Type** : the type of extension.
     * **Scope** : the scope of the plugin.
     * **Region** : the region when the plugin scope is `Regional`.
     * **In use by** : one or more extensions to which the plugin is associated.
     * **Last modified** : the time when the plugin was last modified.
     * **Labels** : the labels added to the plugin.
  3. Optional: To filter the list, do the following:

     1. Click next to **Filter table** to see a list of properties.

     2. From the list, select a property.

The property name, followed by a colon, appears next to the **Filter table** label.

     3. Insert a space next to the colon to see a list of values that match the property, and then select a value from the list.

     4. Optional: Enter the `OR` operator between property-value pairs to specify combined filters.

  4. Optional: To perform other operations with a selected plugin, click more_vert**More actions** , and then select an option:

     * To [edit the plugin](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#edit-plugin), click **Edit**.
     * To [delete the plugin](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#delete-plugin), click **Delete**.
     * To [open Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface), which you can use to retrieve, view, and analyze log data about the plugin, click **View in Logs Explorer**.
     * To open the [Service Extensions Monitoring](https://docs.cloud.google.com/service-extensions/docs/monitor-lb-plugins) page, click **View Monitoring**.



###  gcloud 

Run the [`gcloud service-extensions wasm-plugins list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/list):
    
    
    gcloud service-extensions wasm-plugins list \
        --location=LOCATION
    

Replace `LOCATION` with the location of the plugin as either `global` or a region.

The plugins in your project are listed in a table that has the following information:

  * **Name** : the name of the plugin
  * **Description** : the description of the plugin
  * **Main version** : the active version of the plugin
  * **Update time** : the time when the plugin was last modified



### View the details of a plugin

To view the details of a plugin, use one of the following methods:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. Click the name of the plugin for which you want to see details.

The **Details** page for the plugin opens. The page has the following sections:

     * **Basic information** : this section shows basic details about the plugin, including the Google Cloud product to which the plugin is attached, the load balancer type, the extension type, the extensions that are using the plugin, the plugin scope, the creation and modification timestamps for the plugin, the size of the plugin, labels, and, if logging is enabled, the log sample rate and the minimum logging level.

     * **Versions** : this section shows details about plugin versions, including the version of plugin, the creation timestamp, any description that was specified, the URI and digests for the image, and the plugin configuration file or image and related digests.

You can click the image URL to view its details.




###  gcloud 

To view the details of a plugin, run the [`gcloud service-extensions wasm-plugins describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/describe):
    
    
     gcloud service-extensions wasm-plugins describe WASM_PLUGIN \
         --location=LOCATION
    

Replace the following:

  * `WASM_PLUGIN`: the name of the plugin
  * `LOCATION`: the location of the plugin as either `global` or a region



The following details about the plugin are shown:

  * The plugin name
  * The creation and modification timestamps for the plugin
  * The labels
  * The log sampling rate (if logging is enabled)



To list the versions for a plugin, use the [`gcloud service-extensions wasm-plugin-versions list` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugin-versions/list):
    
    
     gcloud service-extensions wasm-plugin-versions list WASM_PLUGIN \
         --location=LOCATION
    

Replace the following:

  * `WASM_PLUGIN`: the name of the plugin
  * `LOCATION`: the location of the plugin as either `global` or a region



The versions of the specified plugin are listed in a table with the name of the plugin.

To view the details of a plugin version, use the [`gcloud service-extensions wasm-plugin-versions describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugin-versions/describe):
    
    
     gcloud service-extensions wasm-plugin-versions describe WASM_PLUGIN_VERSION \
         --location=LOCATION
    

Replace the following:

  * `WASM_PLUGIN_VERSION`: the main version of the plugin
  * `LOCATION`: the location of the plugin as either `global` or a region



The following details about the plugin version are shown:

  * The version name
  * The creation timestamp
  * A description, if it was entered
  * The URI and digests for the image
  * The plugin configuration file or image and related digests



## Edit plugins

This section describes how you can edit plugins created using Service Extensions.

### Edit a plugin

To edit a plugin, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. For the plugin that you want to edit, click more_vert**More actions** , and then select **Edit**.

Alternatively, click the plugin name, and then, on the **Details** page, click edit**Edit**.

On the **Edit plugin** page, the name of the plugin isn't editable. You can edit other details.

  4. Make changes as required.

For information about most fields, see [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin).

For information about the **Versions** section, see [Add a new version of a plugin](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#add-new-version).

  5. Click **Update plugin**.




###  gcloud 

Run the [`gcloud service-extensions wasm-plugins update` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/update):
    
    
    gcloud service-extensions wasm-plugins update WASM_PLUGIN \
       --location=LOCATION \
       --description=PLUGIN_DESCRIPTION \
       --labels=[LABELS,...]
    

Replace the following:

  * `WASM_PLUGIN`: the name of the plugin
  * `LOCATION`: the location of the plugin as either `global` or a region
  * `PLUGIN_DESCRIPTION`: the description of the plugin
  * `LABELS`: labels in the form of key-value pairs separated by commas



### Add a new version of a plugin

You can [create a new version of the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#create-new-version-of-plugin) and then add it as a new version of the plugin.

To add a new version of a plugin, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. Click edit**Edit**.

  4. In the **Versions** section, click **Add version**.

  5. On the **Add version** pane, specify the details for the plugin version.

  6. Optional: Select the **Set as main** checkbox.

You can also [set this version as the main version](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#set-version) later.

  7. Click **Add**.

  8. Click **Update plugin**.




###  gcloud 

Run the [`gcloud service-extensions wasm-plugins update` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/update):
    
    
     gcloud service-extensions wasm-plugins update WASM_PLUGIN \
         --location=LOCATION \
         --image=IMAGE \
         --main-version=MAIN_VERSION \
         --plugin-config=PLUGIN_CONFIG | --plugin-config-file=PLUGIN_CONFIG_FILE | --plugin-config-uri=PLUGIN_CONFIG_URI
    

Replace the following:

  * `WASM_PLUGIN`: the ID or the fully qualified name of the plugin
  * `LOCATION`: the location of the plugin as either `global` or a region
  * `IMAGE`: the URI of the new Wasm module [stored in the Artifact Registry repository](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#upload-code)
  * `MAIN_VERSION`: the ID of the plugin version to create and set as the main (or serving) version.
  * `PLUGIN_CONFIG`, `PLUGIN_CONFIG_FILE`, or `PLUGIN_CONFIG_URI`: the optional [configuration file](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#config-file), which can be specified inline as text, as a local file, or as an image in Artifact Registry, respectively.

**Note:** To create a new plugin version without also setting it as the main version, use the [`gcloud service-extensions wasm-plugins create` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/create).

### Change the main version of a plugin

To change the main version of a plugin, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. Click the **Edit** button.

  4. In the **Versions** section, select a version that's inactive, and then click **Set as main**.

Alternatively, while [creating a new version of the plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin), you can opt to set the version as the main version.

  5. Click **Update plugin**.




###  gcloud 

Run the [`gcloud service-extensions wasm-plugins update` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/update):
    
    
     gcloud service-extensions wasm-plugins update \
         --location=LOCATION \
         --main-version=WASM_PLUGIN_VERSION
    

Replace the following:

  * `LOCATION`: the location of the plugin as either `global` or a region
  * `WASM_PLUGIN_VERSION`: the name of the main version of the plugin



It might take a few minutes for the new plugin version to be distributed across all locations. The number of minutes might vary across locations because the plugin isn't delivered to all locations simultaneously.

**Note:** To roll back a plugin, set a previous version as the main version.

## Delete plugins

This section describes how you can delete plugins and plugin versions created using Service Extensions.

### Delete a plugin

To delete a plugin, follow these steps:

### Console

  1. Go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. For the plugin that you want to delete, click the more_vert**More actions** button, and then select **Delete**.

Alternatively, click the plugin name, and then click the **Delete** button on the **Details** page.

Plugins that are in use by an extension can't be deleted. To delete such a plugin, first [modify the extension](https://docs.cloud.google.com/service-extensions/docs/manage-extensions#modify-extension) to remove the plugin or [delete the extension](https://docs.cloud.google.com/service-extensions/docs/manage-extensions#delete-extension).

  4. In the confirmation message box, confirm the operation by clicking **Delete**.




###  gcloud 

  1. Remove the references to the plugin from the service configuration, and then reimport the configuration YAML file.

For more information, see how to configure Cloud Load Balancing [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) plugins and [Media CDN](https://docs.cloud.google.com/service-extensions/docs/attach-plugins-to-routes) plugins.

  2. Run the [`gcloud service-extensions wasm-plugins delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/delete):
         
         gcloud service-extensions wasm-plugins delete WASM_PLUGIN \
             --location=LOCATION
         

Replace the following:

     * `WASM_PLUGIN`: the name of the plugin
     * `LOCATION`: the location of the plugin as either `global` or a region



Deleting a plugin also deletes the related plugin resources.

### Delete a version of a plugin

To delete a version of a plugin, follow these steps:

### Console

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. Select the plugin that you want to edit and switch to the [edit mode](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#edit-plugin).

  4. In the **Versions** section, select checkboxes for the versions that you want to delete, and then click **Delete**.

  5. Click **Update plugin**.




###  gcloud 

Run the [`gcloud service-extensions wasm-plugin-versions delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugin-versions/delete):
    
    
     gcloud service-extensions wasm-plugin-versions delete WASM_PLUGIN_VERSION \
         --location=LOCATION
    

Replace the following:

  * `WASM_PLUGIN_VERSION`: the name of a plugin version that's not being used as the main version
  * `LOCATION`: the location of the plugin as either `global` or a region



If a version is set as the main version, which is the main (active) version, you can delete it only after you [set another version as the main version](https://docs.cloud.google.com/service-extensions/docs/manage-plugins#change-main-version).

## What's next

  * Learn how to [create plugins](https://docs.cloud.google.com/service-extensions/docs/create-plugin).
  * See the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
