---
url: https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances/
title: Create plugin instances \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:35:59.533844+00:00
---

# Create plugin instances  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/create-plugin-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Create plugin instances Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes how to create plugin instances in API hub. A plugin instance represents a configured and active connection between API hub and a specific API data source via the associated plugin. For more information about plugin instances, see [Plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-instance). 

## How plugin instances are created

Plugin instances are created automatically or manually depending on the [plugin type](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-types) and the action that you perform. 

  * For all Built-in Google Cloud plugins, API hub automatically creates a plugin instance during the process of attaching a runtime project to API hub. For more information, see [Attach a runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#attach-a-runtime-project).
  * For all third-party and custom plugins, you can create a plugin instance manually from the **Settings** page in API hub. For more information, see Create a plugin instance. **Note:** To create a custom plugin instance, you must first create the plugin. For more information, see [Manage custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-custom-plugins). 



## Before you begin

  * Ensure that you have the following [IAM permissions](https://docs.cloud.google.com/iam/docs/understanding-roles): 
    * `apihub.plugininstances.create`
    * `apihub.plugininstances.delete`
    * `apihub.plugininstances.get`
    * `apihub.plugininstances.list`

For information on granting roles to principals, see [Granting, changing, and revoking access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

  * For Apigee Edge Public Cloud plugins, read about [Apigee Edge API hub connector integration](https://docs.apigee.com/api-platform/get-started/apigee-edge-uapim).
  * For Apigee Edge Private Cloud (OPDK) plugins, read about [API hub connector integration](https://docs.apigee.com/private-cloud/v4.53.00/privatecloud-uapim-overview).
  * For the AWS API Gateway plugin (Preview): 
    * Create a dedicated AWS IAM user with **read-only** access to API Gateway and generate an access key for that user.
    * Store the AWS Secret Access Key in Google Cloud Secret Manager, and grant the API hub service agent (P4SA) the `roles/secretmanager.secretAccessor` role on the secret.
  * For the Azure API Management plugin (Preview): 
    * Create a dedicated Microsoft Entra service principal and assign it only the built-in **API Management Service Reader** role, scoped to the specific APIM service.
    * Store the Azure client secret in Google Cloud Secret Manager, and grant the API hub service agent (P4SA) the `roles/secretmanager.secretAccessor` role on the secret.



## Create a plugin instance

**Note:** The following steps apply only to [third-party](https://docs.cloud.google.com/apigee/docs/apihub/manage-third-party-plugins#supported-third-party-plugins) and [custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-custom-plugins). For Google Cloud plugins, a plugin instance is created automatically during the process of attaching a runtime project to API hub. For more information, see [Manage Google Cloud plugins](https://docs.cloud.google.com/apigee/docs/apihub/manage-gcp-plugins). 

To create a plugin instance, perform the following steps: 

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click settings **Settings** from the left navigation menu to open the **Settings** page.
  3. Click the **Plugins** tab to view the available plugins in your project.
  4. Hold the pointer over the desired plugin, and then click **Create instance**.
  5. Configure the following fields in the **Create a plugin instance** pane. The configuration options depend on the plugin type. 

**Common fields (all plugin types):**

     * **Display name** : Enter a name for the plugin instance.
     * **Curation** : Select the curation settings for the plugin instance. By default, the curation level is set to **Default**.

**Apigee Edge Public Cloud plugin:**

     * **Organization** : Choose the Apigee Edge organization that hosts the plugin data.

**Apigee Edge Private Cloud (OPDK) plugin:**

     * **Organization** : Choose the Apigee Edge organization that hosts the plugin data.
     * **Service account** : Enter the associated service account of the source project. **Important:** For Apigee Edge private cloud (OPDK) plugin instances. 

If your OPDK organization is within a project protected by a VPC Service Controls perimeter, then ensure that the service account is added to the VPC SC ingress policy. If the service account is not allowlisted, the plugin will fail to sync proxy data to API hub. For information about configuring VPC Service Controls, see [Configuring ingress and egress policies](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies). 

**AWS API Gateway plugin:**

     * **AWS account ID** : Enter the 12-digit AWS account ID that owns the API Gateway resources to sync.
     * **AWS region** : Enter the AWS region to sync from (for example, `us-east-1`).
     * **Auth type** : Select **OAuth 2.0 Client Credentials**. This is the only supported authentication type.
     * **Client ID** : Enter your AWS Access Key ID.
     * **Client secret** : Enter the Secret Manager resource name of the secret version that stores your AWS Secret Access Key (for example, `projects/PROJECT_ID/secrets/SECRET_ID/versions/1`).
     * **Schedule** (sync frequency): Specify how often API hub runs the scheduled sync of API metadata from the source. Defaults to every **6 hours**. Adjust the frequency for more or less frequent syncs.

**Azure API Management plugin:**

     * **Azure tenant ID** : Enter the Microsoft Entra tenant ID (GUID).
     * **Azure subscription ID** : Enter the Azure subscription ID (GUID) that contains the APIM service.
     * **Azure resource group name** : Enter the name of the Azure resource group that contains the APIM service.
     * **APIM service name** : Enter the name of the Azure API Management (APIM) service to sync from.
     * **Auth type** : Select **OAuth 2.0 Client Credentials**. This is the only supported authentication type.
     * **Client ID** : Enter your Microsoft Entra service principal application ID.
     * **Client secret** : Enter the Secret Manager resource name of the secret version that stores your Azure client secret (for example, `projects/PROJECT_ID/secrets/SECRET_ID/versions/1`).
     * **Schedule** (sync frequency): Specify how often API hub runs the scheduled sync of API metadata from the source. Defaults to every **6 hours**. Adjust the frequency for more or less frequent syncs.

**Custom plugin:**

     * **Source project ID** : Enter the unique identifier of the source project from which the plugin will import the data.
  6. Click **Create** to initiate the creation of the plugin instance. 

You can view the status of the plugin instance in the **Plugins** tab under **Manage instances**. On successful creation, the status of the plugin instance is displayed as **Active** as shown in the following image:

![Plugin instance status shown as Active in the Plugins tab.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/plugin-active.png)![Plugin instance status shown as Active in the Plugins tab.](https://docs.cloud.google.com/static/apigee/docs/apihub/images/plugin-active.png)




## What's next

  * Learn more about [managing plugin instances](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances).
  * Learn more about [plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins).
  * Learn more about [curations](https://docs.cloud.google.com/apigee/docs/apihub/curations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
