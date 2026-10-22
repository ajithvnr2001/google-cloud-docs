---
url: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with/
title: Working with environments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:54.697778+00:00
---

# Working with environments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Working with environments Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes how to create, edit, and delete environments with Apigee.

##  About environments 

An [ _environment_](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview) is an isolated area within an organization where you can [create](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) and [deploy](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy) API proxies. You [create an environment](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-environment) during provisioning, and can later add more environments to your organization.

## Environments and instances

Each environment must be attached to at least one Apigee instance. An instance is a region-specific virtual machine. Attaching an environment to an instance means the instance loads, deploys, and serves proxies for the environment.

The instance or instances an environment is attached to should match the region or regions with the most traffic for the environment. You can add the environment to an instance or move it to a different instance if more of the traffic is in the new instance's region.

To set and change the environment's instance, see [Attaching or removing an environment from an instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#add-envs).

**Note** : Pay-as-you-go environments begin incurring charges once attached to an instance. Charges may accrue prior to any API traffic beginning. For more information about Pay-as-you-go pricing, see [ Pay-as-you-go example pricing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples).

## Creating environments

You can create a new environment using the Apigee UI or the Apigee API, as described in the following sections. Before you begin, it is important to note that Apigee and Apigee hybrid have limits on the number of environments and environment groups you can create per organization and per region. For details, see [Limits: Environment and organization](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits#environment-and-organization). 

### Creating a new environment in the UI

To create a new environment in Apigee Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. In the **Environments** pane, click **\+ Create Environment**.
  3. In the **Create an environment** pane, enter the following: 
     * **Select environment type** : If you are a Pay-as-you-go customer, click **Select** to choose the type of environment you want to create: Base, Intermediate, or Comprehensive. 

The selection of environment type does not apply to Subscription customers and will not appear in the UI.

     * **Name** : The programmatic environment name. The **Name** can't be changed after it is created.

The name must contain between 2 and 32 characters which can be lower-case letters, numbers, or hyphens. The name must begin with a letter and cannot end with a hyphen. The name must be different from any other environment name in your organization.

     * **Display Name** : The name for the environment that is displayed in the UI.
     * **Description** : Optional. A description of the environment.
     * **Instance** : Optional. Select the Apigee instance that will load, deploy, and serve traffic for the environment.
     * **Environment group** : Optional. Select a checkbox to add the new environment to an existing environment group. Click **OK**.
     * **Deployment type** : Select whether you want to deploy individual API proxies or an archive of your API proxy configuration environment. For more information, see [Supported deployment types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#deployment-types). **Note** : The deployment type used with this environment cannot be changed after the environment is created.
  4. Click **Create**.

**Note:** This operation to create the environment may take up to five minutes if an instance attachment is specified.

Once complete, the new environment is displayed in the table in the **Environments** pane.

Every new environment must be attached to an Apigee _instance_ and an _environment group_.

If you did not attach your environment to an instance during creation, you can do this step in the [Instances UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#add-envs) or using the [Instances attachment create API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments/create). For an example of how to do this using the API, see [Create an environment](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-environment) in the command-line provisioning documentation.

**Note** : Pay-as-you-go environments begin incurring charges once attached to an instance. Charges may accrue prior to any API traffic beginning. 

For more information about Pay-as-you-go pricing based on updated attributes, see [ Pay-as-you-go (updated attributes) example pricing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples).

If you did not assign the new environment to a group during creation, you can follow the steps in [Adding environments to an environment group](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#adding). Environments not assigned to groups have no hostnames pointing to them, and therefore they are not accessible. For more information, see [Creating environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with#groups).

If you have an Apigee organization with Pay-as-you-go billing, you may want to enable the Apigee API Analytics add-on in your new environment. For more information, see [Manage the Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on). 

### Creating a new environment with the Apigee API

This section describes how to create a new environment using the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

Most steps in this process trigger long-running operations that can take several minutes.

**To create a new environment with the Apigee API:**

  1. Create the new environment with the [Create environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/create).
  2. Attach the environment to the runtime instance using the [Instances attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances.attachments). **Note** : Pay-as-you-go environments begin incurring charges once attached to an instance. Charges may accrue prior to any API traffic beginning. 

For more information about Pay-as-you-go pricing based on updated attributes, see [ Pay-as-you-go (updated attributes) example pricing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples).

  3. Create an environment group if you do not already have one. To do this, use the [Create environment groups API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups/create).
  4. Attach the new environment to the environment group using the [Environment group attachment API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.envgroups.attachments). 

Attaching an environment to the group makes the proxies in that environment routable via the hostnames in the group.




For detailed information and examples on using the Apigee APIs to create and attach new environments, see [Create an environment](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#create-environment) in the command-line provisioning instructions.

## Editing environments

This section describes how to edit existing environments in the Apigee UI and with the Apigee API.

### Edit environments in the Apigee UI

You can change the following properties of an existing environment in the Apigee UI:

  * **Display name** : Enter a new display name for the environment.
  * **Description** : Enter a new description for the environment.
  * **Environment group** : Clear the previously selected checkbox and select the checkbox for the new environment group.



To edit environment in the Apigee Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the project with the environments you want to update.
  3. Locate the row of the environment you want to edit, click more_vert **Actions > Edit**. The **Edit environment** dialog is displayed.
  4. **Select environment type** : If you are a Pay-as-you-go customer, choose an option under **Select environment type** to change the environment type. Options include **Base** , **Intermediate** , or **Comprehensive**. 

The selection of environment type does not apply to Subscription customers and will not appear in the UI.

  5. You can make any changes required in either the **Display name** or **Description** fields.
  6. In the **Environment group** listbox, you can clear the previously selected checkbox and select the checkbox for the new environment group.
  7. Click **Update** to save your changes.

**Note:** This operation may take up to five minutes to complete.

### Edit environments with the Apigee API

To edit an existing environment with the Apigee API, use the [Get environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/get) to get the list of current properties that you can modify, and the [Update environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/update) to set or change them.

### Configure forward proxying on an environment

To configure [forward proxying](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview#forward-proxying), set the `forwardProxyUri` value for the environment using the [environments API](https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments). 

**Important:** When configuring forward proxy for _hybrid_ installations, use the hybrid forward proxying functionality described in [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/latest/forward-proxy) rather than the instructions provided here.

#### Disable forward proxying for a proxy in the environment

If the traffic for a specific target of an API proxy should go directly to the backend target, bypassing the forward proxy, then set the following property in the TargetEndpoint to override the HTTP forward proxy:
    
    
    <Property name="use.proxy">false</Property>

For more information on setting the TargetEndpoint properties, including how to configure the connection to the target endpoint, see [Endpoint properties reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/endpoint-properties-reference).

Set `use.proxy` to "true" for any TargetEndpoint that you want to go through an HTTP forward proxy:
    
    
    <Property name="use.proxy">true</Property>

## Deleting environments

Before deleting an environment, make sure to consider the following key points: 

  * **You must delete all key value maps and key value entries before you delete an environment.** Otherwise, if you re-create the environment the key value map entry operations will encounter encryption/decryption discrepancies.
  * When you delete an environment with the [Apigee API Analytics add-on](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on) enabled, the analytics data for the environment is also deleted. If you wish to retain analytics data for any environment, we recommend that you export and save your data in another location. For more information on saving your data, see [ Exporting data from Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/export-data). To learn more about the impact of environment deletion on Apigee API Analytics data, see [Manage your Apigee API Analytics data](https://docs.cloud.google.com/apigee/docs/api-platform/reference/manage-analytics-add-on#manage-your-apigee-api-analytics-data)



### Deleting an environment with the Apigee UI

To delete an environment in the Apigee Apigee UI:

  1. In the Google Cloud console, go to the **Apigee > Management > Environments** page.

[Go to Environments](https://console.cloud.google.com/apigee/environments)

  2. Select the project with the environments you want to delete.
  3. Locate the row of the environment you want to delete, click more_vert **Actions > Delete**.

**Note:** This operation may take up to five minutes to complete.

### Deleting an environment with the Apigee API

To delete an environment, use the [Delete environments API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments/delete).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
