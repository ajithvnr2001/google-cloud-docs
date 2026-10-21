---
url: https://docs.cloud.google.com/service-extensions/docs/create-plugin/
title: Create a plugin \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:13.270363+00:00
---

# Create a plugin  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/create-plugin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Create a plugin Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create Service Extensions plugins that you can use to implement extensibility with Google Cloud services.

This feature is in [Preview](https://cloud.google.com/products#product-launch-stages) for Media CDN.

For a product overview, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

## Before you begin

  1. [Prepare and upload the files](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code) required to create a plugin.

  2. Get the [required Identity and Access Management (IAM) roles and permissions](https://docs.cloud.google.com/service-extensions/docs/access-control).

  3. Enable the Network Services API, if it's not already enabled.
         
         gcloud services enable networkservices.googleapis.com
         

  4. For Media CDN plugins, if you intend to enable logging, enable the Network Actions API.
         
         gcloud services enable networkactions.googleapis.com
         




## Create a plugin resource

Creating a plugin resource entails specifying an image that contains the plugin code and specifying labels and logging options for the plugin.

**Note:** For Media CDN, the Google Cloud console isn't supported.

###  Console

To create a plugin, follow these steps:

  1. In the Google Cloud console, go to the **Service Extensions** page.

[Go to Service Extensions](https://console.cloud.google.com/net-services/service-extensions)

  2. Click the **Plugins** tab.

  3. Click **Create plugin**.

  4. In the **Basics** section, do the following:

     1. For **Scope** , select either **Global** or **Regional**.

If you set the scope as **Regional** , select the region as well.

     2. Enter a unique plugin name.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

     3. Optional: Enter a brief description about the plugin by using up to 1024 characters.

  5. In the **Wasm image** section, do the following:

     1. For **Plugin version name** , specify a name for the plugin version.

The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens and must not end with a hyphen.

     2. Optional: For **Plugin version description** , enter a brief description about the plugin version by using up to 1024 characters.

     3. For **Image URL** , enter the URL for the [generic artifact or container image that has the Wasm module](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#generic-repository) from the Artifact Registry pane. The option to use a generic repository is in [Preview](https://cloud.google.com/products#product-launch-stages).

If you want to specify a container image in a Docker repository, you can, alternatively, click **Select** to browse and select it. The Artifact Registry pane displays the folders in the repository that's connected to the current project.

To select an image from another project, [ensure that Service Extensions has access to it](https://docs.cloud.google.com/service-extensions/docs/create-plugin#another-project), and then click **Change** , next to the project name.

  6. Optional: In the **Plugin configuration** section, to associate the [configuration data](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#config-file) with the plugin, select the **Add plugin configuration** checkbox, and then select either of the following options:

     * **Upload plugin configuration file**. If your file size is less than 900 KiB and in a local drive, click **Browse** to locate and select it.

     * **Select plugin configuration image or artifact from Artifact Registry**. Enter the URL for the [generic artifact or container image that has the Wasm module](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#generic-repository) from the Artifact Registry pane. The option to use a generic repository is in [Preview](https://cloud.google.com/products#product-launch-stages).

To specify a container image in a Docker repository, you can, alternatively, click **Select** to browse and select it. The Artifact Registry pane displays the folders in the repository that's connected to the current project.

  7. Optional: In the **Labels** section, click **Add label**. Then, in the row that appears, do the following:

     1. For **Key** , enter a key name.
     2. For **Value** , enter a value for the key.

You can add a maximum of 64 key-value pairs. To add more key-value pairs, click **Add label**.

For more information about labels, see [Create and update labels for projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

  8. In the **Encryption** section, choose the encryption mechanism for the plugin. This option is available only for regional plugins.

     * **Google-managed encryption key**. Encrypt plugin content with the [Google default encryption mechanism](https://cloud.google.com/docs/security/encryption/default-encryption).
     * **Cloud KMS key**. Encrypt plugin content with a [customer-managed encryption key](https://docs.cloud.google.com/service-extensions/docs/cmek#create-cmek) created by using Cloud Key Management Service. In this case, for **Key management type** , select **Cloud KMS**. Then, select a Cloud KMS key.
  9. Optional: In the **Logging** section, select **Enable logging** and do the following:

     * For **Sample rate** , specify a value between `0` and `1`. The value `0` indicates that log messages aren't stored. The default value `1` indicates that all log messages are stored. A floating point value between `0.0` and `1.0` indicates that a percentage of log messages is stored.

     * For **Minimum log level** , select the minimum [severity level](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) of plugin log messages to be exported to Cloud Logging. The default value is `Info and higher`.

  10. Click **Create**.




###  gcloud 

  1. Create a plugin by running the [`gcloud service-extensions wasm-plugins create` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/create):
         
         gcloud service-extensions wasm-plugins create WASM_PLUGIN \
             --description=PLUGIN_DESCRIPTION \
             --location=LOCATION \
             --labels=[LABELS,...] \
             --log-config=[LOG_CONFIG,...] \
             --image=IMAGE \
             --main-version=MAIN_VERSION \
             --plugin-config=PLUGIN_CONFIG |
                 --plugin-config-file=PLUGIN_CONFIG_FILE |
                 --plugin-config-uri=PLUGIN_CONFIG_URI \
             --kms-key-name=KEY_NAME
         

Replace the following:

     * `WASM_PLUGIN`: the ID or the fully qualified name of the plugin
     * `PLUGIN_DESCRIPTION`: a description of the plugin
     * `LOCATION`: the location of the plugin as either `global` or a region
     * `LABELS`: labels in the form of key-value pairs separated by commas
     * `LOG_CONFIG`: logging options for the plugin. When the `enable` option is set to `false`, logs aren't captured for the plugin. To enable logging, set the `enable` option to `true`. Then, specify the following details:

       * `sample-rate`: the sampling rate of activity logs as a value between `0` and `1`. The value `0` indicates that log messages aren't stored. The default value `1` indicates that all log messages are stored. A floating point value between `0.0` and `1.0` indicates that a percentage of log messages is stored.

       * `min-log-level`: the minimum [severity level](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity) of plugin log messages to be exported to Cloud Logging. The default value is `INFO`.

     * `IMAGE`: the URI of the [artifact that contains the Wasm module](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#upload-image) stored in the Artifact Registry repository. Before you specify a container image from another project, [ensure that Service Extensions has access to it](https://docs.cloud.google.com/service-extensions/docs/create-plugin#another-project).

     * `MAIN_VERSION`: the ID of the plugin version to create and set as the main (active) version.

     * `PLUGIN_CONFIG`, `PLUGIN_CONFIG_FILE`, or `PLUGIN_CONFIG_URI`: the optional [configuration data](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#config-file), which can be specified as text, a local file, or a container image in Artifact Registry, respectively.

     * `KEY_NAME`: for regional plugins, the fully qualified name of the [customer-managed encryption key](https://docs.cloud.google.com/service-extensions/docs/cmek#create-cmek) in the following format: `projects/PROJECT/locations/LOCATION/keyRings/KEYRING_NAME/cryptoKeys/KEY_NAME`.

Replace the following:

       * `PROJECT`: the ID of the project that contains the key
       * `LOCATION`: the location of the key
       * `KEYRING_NAME`: the key ring name
       * `KEY_NAME`: the key name

If this option isn't specified, the [Google default encryption mechanism](https://cloud.google.com/docs/security/encryption/default-encryption) is used.

For example:
    
    gcloud service-extensions wasm-plugins create my-plugin \
        --description="This is my plugin." \
        --log-config=enable=true,sample-rate=0.5,min-log-level=INFO \
        --labels=key1=value1,key2=value2 \
        --image=...-docker.pkg.dev/my-project/repository/container:tag \
        --main-version=v1 \
        --plugin-config-file=config.txt
    

To deploy a new version, use the [`gcloud service-extensions wasm-plugins update` command](https://docs.cloud.google.com/sdk/gcloud/reference/service-extensions/wasm-plugins/update). Specify a new image and version name:
    
    gcloud service-extensions wasm-plugins update my-plugin \
        --image=...-docker.pkg.dev/my-project/repository/container:tag \
        --main-version=v2
    




To run these plugins, you can configure [Cloud Load Balancing extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview) and [Media CDN extensions](https://docs.cloud.google.com/service-extensions/docs/media-cdn-extensions-overview).

**Important:** To request access to Media CDN, contact your Google Cloud sales representative or your account team.

### Access images in another project

Before you can select images from another project, the Service Extensions service agent must have [access to the project repository](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant-repo) and, depending on how your Wasm module is packaged, one of the following permissions on the project:

  * For generic artifacts: `artifactregistry.files.download`
  * For container images: `artifactregistry.repositories.downloadArtifacts`



The Service Extensions service agent is named as follows:
    
    
    service-PROJECT_NUMBER@gcp-sa-networkactions.iam.gserviceaccount.com
    

Replace `PROJECT_NUMBER` with your [project number](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects).

## What's next

  * See [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) for Cloud Load Balancing plugins.
  * Learn how to configure Cloud Load Balancing [edge extensions](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions#configure-edge-plugins), [route extensions](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins), and [traffic extensions](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) by using plugins.
  * Learn how to [attach Media CDN plugins to routes](https://docs.cloud.google.com/service-extensions/docs/attach-plugins-to-routes).
  * Learn how to [manage plugins](https://docs.cloud.google.com/service-extensions/docs/manage-plugins).
  * See the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
