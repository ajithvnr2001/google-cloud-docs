---
url: https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger/
title: Salesforce trigger \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:38.009300+00:00
---

# Salesforce trigger  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/configure-salesforce-trigger/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Salesforce trigger

The **Salesforce trigger** lets you listen to either [Change Data Capture (CDC)](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) or [Enterprise Messaging Platform](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_emp.htm) events. With this trigger, you can start your integration based on any of the CDC events (Create, Update, Delete, or Undelete) or the platform events in your Salesforce instance. 

For more information, see the following tutorials:

  * To use Application Integration to automate the business process flow of routing and assigning a Salesforce customer case, see the [Automate Salesforce case routing assignments](https://docs.cloud.google.com/application-integration/docs/automate-salesforce-case-routing) tutorial.
  * To use Application Integration to automate an order management flow between a customer relationship management (CRM) application and an enterprise resource planning (ERP) application, see the [Automate Salesforce opportunity to BigQuery order](https://docs.cloud.google.com/application-integration/docs/automate-salesforce-opportunity-to-bigquery-order) tutorial.
  * To use the Salesforce trigger to invoke an integration in Application Integration for a Salesforce Change Data Capture (CDC) event, see the [Invoke an integration for a Salesforce Change Data Capture (CDC) event](https://docs.cloud.google.com/application-integration/docs/invoke-integration-salesforce-cdc-event) tutorial.



## Before you begin

This section outlines the steps required to connect and configure a Salesforce instance to use [Change Data Capture (CDC)](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_intro.htm) or [ Platform](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro.htm) events to stream changes to your Application Integration in a pub/sub manner. The following steps must be completed before configuring any Salesforce-related task or trigger in Application Integration: 

  * Set up an integration user
  * Configure a permission set
  * Set up a security token
  * Create a connected app

**Note** : To complete these steps, system administration access to your Salesforce instance is required. If you do not have admin access, share these instructions with your Salesforce Administrator. 

This tutorial provides in-depth instruction, but we recommend that you have some understanding of Salesforce configuration options. Salesforce provides detailed [Developer Documentation](https://developer.salesforce.com/docs/) to help you get started. 

### Set up an integration user

**Note** : If you already have an integration user and you know the password, you can skip to the next step. If you need to reset the password, see Step 6 below.

Set up an integration user with the following steps: 

  1. Log in to your Salesforce instance with your `sysadmin` credentials. 
  2. Click the **Gear** icon and then select **Setup** , as shown in the image below: ![image showing Setup page](https://docs.cloud.google.com/static/application-integration/images/setup.png)![image showing Setup page](https://docs.cloud.google.com/static/application-integration/images/setup.png)
  3. Click **Users > Users** from the **Administration menu**. 
  4. From the **Users** pane, select the **New User** button. 
  5. In the **User Edit** dialog, fill in the following details: 
     1. **First Name** : First name of the integration user.
     2. **Last Name** : Last name of the integration user. 
     3. **Email Address** : Email for the integration user. Ideally, this should be a group email. 
     4. **Username** : User name that complies with any org-level naming conventions. 

If you are creating a new integration user, use the following format: `EMAIL.SALESFORCE_ORG_NAME.SANDBOX_NAME`

If you have an existing integration user, confirm that the username is entered here. 

     5. **Role** : Select from the dropdown of options.
     6. **User License** : Enter `Salesforce` or, if using a trial org, enter `Salesforce Platform`. 
     7. **Profile** : Select the permissions profile for integration users from the dropdown. 

We recommend assigning a profile with _no permissions_ , to protect your integration user Salesforce access from unauthorized usage.

     8. Click **Save**.
  6. To update the password for the new integration user, follow these steps: 
     1. Click the **Reset password(s)** button on the **Users** pane. A password reset email is sent to the email address associated with the user. **Note** : Confirm that you have access to the email account associated with the integration user before triggering the reset password flow. In addition, **if you have if you have SSO enabled** for this user, you will not be able to reset the password. To enable the reset option, go to **Profile > System Permissions** and uncheck the option for **SSO Login Enabled.**
     2. Follow the reset password flow from the email account. **Take note of the new password** , as you will need it for a later step.



### Configure a Permission Set

If you have already have access to a Permission Set that is appropriate for an integration user, you can skip this step and proceed to Set up a security token. Otherwise, follow these steps to configure a Permission Set for the integration user and the Salesforce object. 

To configure a Permission Set for the integration user: 

  1. From the **Setup** menu, click **Users > Permission Sets**.
  2. In the **Permission Sets** pane, click the **New** button.
  3. In the **Permission Sets** dialog, enter the following details: 
     * **Label** : Enter a name for the Permission Set. 
     * **License** : Select **Salesforce** from the **License** dropdown.
     * Click **Save**.
  4. From the list of **System** setting options, scroll down and select **System Permissions**
  5. On the **System Permissions** page, click the **Edit** button.
  6. Scroll down the list of available permissions and select the **API Enabled** checkbox. 

The **Api Only User** permission is also required, but cannot be enabled until the required security token is reset. This permission is added in a later step.

  7. _(Optional)_ Scroll and select **Modify All Data** and **View All Data** , if applicable. These permissions are not required, but can be helpful if you want to automatically give the integration user access to new objects. We recommend only enabling these permissions for testing in a sandbox.
  8. Scroll to the top of the permissions list and click **Save**. 
  9. Confirm your settings and click **Save**.



To configure the Permission Set for the Salesforce object: 

  1. Click **Permission Set Overview** to return to the main **Permissions Set** configuration page.
  2. Select **Object Settings** from the **Apps** section of the **Permissions Set** pane. 
  3. Scroll down and select the Salesforce object(s) requiring a Permission Set. This example uses the **Opportunity** object. **NOTE:** CDC only supports a subset of standard Salesforce objects. To learn more, see: [Change Event Object Support](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_object_support.htm).
  4. Click the **Edit** button on the object detail page.
  5. Select the checkboxes for record types If you know which record types are required select those. If you don't know which record types are required, select them all.
  6. Select the checkboxes for the **Object Permissions** to enable. **Read** and **View All** are recommended.
  7. Grant **Read Access** or **Edit Access** for each object field by selecting the corresponding checkbox. **Note** : Write access is not required for use with CDC.
  8. Scroll to the top of the page and click **Save**.



### Set up a Security Token  


If you have created a security token for the integration user previously, and reset the password, an email with a new security token is sent automatically. You can use the new token and skip to Create a connected app.

Otherwise, use the following steps to reset the security token for the integration user: 

  1. Log in to Salesforce as the integration user, using the username and password set in a previous step.
  2. From the main menu, click the profile picture, then click **Settings**. 
  3. From the **Settings** menu, select **Reset My Security Token** to open the **Reset Security Token** pane.
  4. Click the **Reset Security Token** button.
  5. Check the email account associated with the integration user for an email containing the new security token. **Take note of the new security token** , as you will need it for a later step. 
  6. _(Optional)_ Enable the **Api User Only** permission in **System Permissions** for your permission set, as described in Configure a permission set above.



### Create a Connected App

System administration permission is required to set up a Connected App. If you are currently logged in as the integration users, make sure to log out and then log in again as `sysadmin`. 

Follow these steps to set up a Connected App: 

  1. Click the **Gear** icon and then select **Setup**.
  2. From the **Setup** menu, search for and select **App Manager** , as shown in the image below: ![image showing Setup page](https://docs.cloud.google.com/static/application-integration/images/app-manager.png)![image showing Setup page](https://docs.cloud.google.com/static/application-integration/images/app-manager.png)
  3. Click **New Connected App**.
  4. In the configuration pane, provide the following details: 
     * **Connected App Name** : Enter a name for your connected app.
     * **API Name** : Enter the name of the API.
     * **Contact email** : Enter an email for your connected app, ideally a group email alias.
     * **API (Enable OAuth Settings)** : Select **Enable OAuth Settings**. Then, set the following: 
       1. **Callback URL** : This is only required if the you want an external service to receive the OAuth authorization response (for example, authorization codes or tokens) and perform validation. If you do choose to provide a callback, make sure to include the `http(s)://` prefix.
       2. **Selected OAuth Scopes** : Select: 
          * **Access and manage your data (api)**
          * **Perform requests on your behalf at any time (refresh_token, offline_access)**
**Note:** If you are using OAuth authentication, you must install the connected app in your Salesforce account after creating the trigger. For details, see Install the OAuth connected app.
  5. Click **Save**. **Note** : Your newly created connected app will not work for the initial 2-10 minutes after creation.
  6. Click **Continue**. You need to re-authorize with a verification code that is sent to your email address.
  7. After successfully verifying the code, a **consumer secret** and a **consumer key** are displayed on the next page. Make a note of these values, as they will be used when setting up the Auth Module for Application Integration.
  8. Click the **Manage** button.
  9. Once on the **Connected App Detail** page, click the **Edit Policies** button.
  10. In the **OAuth Policies** section, change the value in the **Permitted Users** dropdown to **Admin approved users are pre-authorized**.
  11. Click **Save**.
  12. Scroll to the **Profiles** and **Permission Sets** section of the page to select the profile or Permission Set you want to apply to the connected app. You can select either a profile or a Permission Set, or a mixture of both, which will allow users with either the correct profile or Permission Set to access the connected app.
  13. Select the desired profile or Permission Set.
  14. Click **Save**.



## Prerequisite steps to use CDC events

Before configuring your Application Integration trigger to use CDC events, make sure to add a configured object to CDC in Salesforce: 

  1. Log in to Salesforce as a `sysadmin`.
  2. Click the **Gear** icon, then click **Setup**.
  3. Using the left nav, search for and select **Change Data Capture**.
  4. On the **Change Data Capture** setup page, locate the Salesforce object you'd like to use in the **Available Entities** column and drag it to the **Selected Entities** column. **Note** : A maximum of 5 objects per Salesforce license can be selected for CDC. Contact your Salesforce representative for more information and licensing options.
  5. Click **Save**.



## Prerequisite steps to use Platform events

Before configuring your Application Integration trigger to use Platform events, complete the following steps in Salesforce: 

  * Create a Platform Event
  * Update permissions for the Platform Event



###  Create a Platform event 

To create a Platform event, perform the following steps:

  1. Log in to your Salesforce instance with your `sysadmin` credentials.
  2. Click the **Gear** icon and then select **Setup**.
  3. In the navigation pane, search for **Platform** and then click **Platform events**.
![image showing a new platform event](https://docs.cloud.google.com/static/application-integration/images/new-platform-event.png)![image showing a new platform event](https://docs.cloud.google.com/static/application-integration/images/new-platform-event.png)
  4. In the **Platform events** page, click **New Platform Event** and set the following properties:


  * **Label**
  * **Plural Label**
  * **Object Name**(This field is automatically populated)
  * **Publish Behavior** Select any one of the following values: 
    * **Publish After Commit** : Reverts streaming of events if a condition isn't met.
    * **Publish Immediately** : Instantly triggers the event, without waiting for any validation.
For more information about the publishing behavior, see [ Platform events and Transactions](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_events_intro_emp.htm). 
  * **Deployment Status** (Optional): Select **Deployed** if the event is ready for deployment.


* Click **Save**.
![image showing setting of labels and publish behavior for a platform event](https://docs.cloud.google.com/static/application-integration/images/new-platform-event-2.png)![image showing setting of labels and publish behavior for a platform event](https://docs.cloud.google.com/static/application-integration/images/new-platform-event-2.png)
* Create custom fields. To create the custom fields, click **New** in the **Custom Fields and Relationships section** and select the type of custom field. You can create as many custom fields as required.

After creating the custom fields, in the **Platform events** page, notice the value of the **API Name** field. The object name ends with **_e** , which means that the object is a Platform Event object. For a CDC object, the object name ends with **_c**. 

![image showing details of a saved platform event](https://docs.cloud.google.com/static/application-integration/images/api-name-publish-behavior.png)![image showing details of a saved platform event](https://docs.cloud.google.com/static/application-integration/images/api-name-publish-behavior.png)

### Update permissions for the Platform Event

The permissions set must be updated to let the integration user access the newly created Platform Event.

To update the permissions, perform the following steps:

  1. From the **Setup** menu, click **Users > Permission Sets**.
  2. In the **Permission Sets** page, click the previously created permission.
  3. Click **Object Settings** > Plural Label of the Platform Event.
  4. In the **Object Permissions** section, enable the **Read** and **Create** permissions.
  5. Click **Save**.
![image showing permissions of a platform event](https://docs.cloud.google.com/static/application-integration/images/platform-event-permissions.png)![image showing permissions of a platform event](https://docs.cloud.google.com/static/application-integration/images/platform-event-permissions.png)


## Add a Salesforce trigger

To add a **Salesforce trigger** to a new or existing integration, follow the steps below: 

  1. In the Google Cloud console, go to the **Application Integration** page. 

[Go to Application Integration](https://console.cloud.google.com/integrations)

  2. In the navigation menu, click **Integrations**. 

The **Integrations** page appears listing all the integrations available in the Google Cloud project. 

  3. Select an existing integration or click **Create integration** to create a new one. 

If you are creating a new integration: 

     1. Enter a name and description in the **Create Integration** pane.
     2. Select a region for the integration. **Note:** The **Regions** dropdown only lists the regions provisioned in your Google Cloud project. To provision a new region, click **Enable Region**. See [Enable new region](https://docs.cloud.google.com/application-integration/docs/enable-new-region) for more information. 
     3. Select a service account for the integration. You can change or update the service account details of an integration any time from the info **Integration summary** pane in the integration toolbar. **Note:** The option to select a service account is displayed only if you have enabled integration governance for the selected region. 
     4. Click **Create**. The newly created integration opens in the _integration editor_. 

  4. In the _integration editor_ navigation bar, click **Tasks** to view the list of available tasks and connectors. 
  5. Select an existing integration or click **Create integration**. 
  6. In the integration editor, click **\+ Add a task/trigger > Triggers** to view the available triggers
  7. Click and place the **Salesforce trigger** element to the designer.



## Configure the Salesforce trigger

To configure the Salesforce trigger, perform the following steps:

  1. Click **Salesforce trigger** in the integration editor to view the trigger configuration pane.
  2. Select a Salesforce instance from the **Salesforce instance configuration** drop-down. 

If you do not have a Salesforce instance, create a new instance. For more information, see Create a new Salesforce instance.

  3. Select a Salesforce channel from the **Salesforce channel configuration** drop-down. 

If you do not have a Salesforce channel, create a new channel. For more information, see Create a new Salesforce channel.

  4. If you have chosen the event type as **CDC** , select any one of the following operations: 
     * `Create`
     * `Update`
     * `Delete`
     * `Undelete`

The trigger runs only if the specific operation or gap operation occurs. 

The **Salesforce trigger** can be configured for only one operation. If you want to run the trigger for multiple operations, create a **Salesforce trigger** for each operation.




### Create a new Salesforce instance

To configure a new Salesforce instance, perform the following steps:

  1. In the editable properties of the trigger, click **Select a Salesforce instance configuration** > **\+ Add new Salesforce instance configuration**.
  2. In the **Add Salesforce instance configuration** dialog, set the following properties:
     * **Salesforce instance connection name** : Enter a name for the instance. 

After configuration, you will use this name to refer to the Salesforce instance.

     * **Salesforce domain** : Enter a service authority for the instance. You can find the domain in your Salesforce account. For example, `instance.my.salesforce.com`. The following image shows the Salesforce domain: 

![Get Salesforce domain in a Salesforce instance](https://docs.cloud.google.com/static/application-integration/images/salesforce-domain.png)![Get Salesforce domain in a Salesforce instance](https://docs.cloud.google.com/static/application-integration/images/salesforce-domain.png)

     * **Authentication profile** : Select an authentication profile. 

If you don't have an authentication profile, [create a new profile](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#createAuthProfile) of the _OAuth 2.0 resource owner password credentials_ authentication type. For information about the fields, see [OAuth 2.0 resource owner password credentials](https://docs.cloud.google.com/application-integration/docs/configure-authentication-profiles#oauth2-owner). For the Salesforce instance, enter the following values: 

       * **Client ID:** enter the consumer key that you noted when you set up a connected app.
       * **Secret:** enter the consumer secret that you noted when you set up a connected app.
       * **Password:** Enter the user password with the `USER_PASSWORDSECURITY_TOKEN` format. Replace the following: 
         * `USER_PASSWORD`: the Salesforce user password.
         * `SECURITY_TOKEN`: the security token that you set for your integration.
For example, if your `USER_PASSWORD` is `test-password` and `SECURITY_TOKEN` is `737K27NCa3O6`, then your password will be `test-password737K27NCa3O6`. 

The following image shows the fields required to create an authentication profile:

![OAuth 2.0 resource owner password credentials](https://docs.cloud.google.com/static/application-integration/images/authentication-profile-oauth2.png)![OAuth 2.0 resource owner password credentials](https://docs.cloud.google.com/static/application-integration/images/authentication-profile-oauth2.png)

     * **Salesforce Organization ID** : Enter the org id of the salesforce instance. You can get the ID from your Salesforce administrator.
  3. Click **Add**.



### Create a new Salesforce channel

To configure a new Salesforce channel, perform the following steps:

  1. In the editable properties of the trigger, click **Select a Salesforce channel configuration** > **\+ Add new Salesforce channel configuration**.
  2. In the **Add Salesforce channel configuration** dialog, enter the object name for the **Salesforce object name** property. 

For the list of Saleforce objects, see [Standard objects in Salesforce](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_list.htm). If unsure of the object name, contact your Salesforce administrator.

  3. Click **Add**.



## Install the OAuth 2.0 connected app

As part of a security enhancement, Salesforce now requires all connected apps using OAuth 2.0 authentication to be installed. This applies to both new and existing triggers. This change means your existing trigger might stop working unless the connected app is installed in Salesforce. Navigate to the **Connected Apps OAuth Usage** page in your Salesforce account and install the app. For more information, see [Connected App Usage Restrictions Change](https://help.salesforce.com/s/articleView?id=005132365&type=1).

## Output variables

The response from the **Salesforce trigger** is available to you in the output variables.

The output variables for a **CDC** event are described in the following table:

**Variable** | **Data type** | **Description**  
---|---|---  
SalesforceTriggerCdcPayload | JSON | Details of the change event.  
SalesforceTriggerEvent | JSON | Contains `replayId` of the event.  
SalesforceTriggerSchema | String | Trigger schema.  
SalesforceTriggerCdcSnapshot | JSON | Snapshot of the object after the change event. This field is available only for `Update` and `Create` operations.  
SalesforceTriggerCdcRecordId | String | Contains the `recordId` of the updated or added record. The `recordId` is an identifier of the changed Salesforce object.  
  
The output variables for a **Platform** event are described in the following table:

**Variable** | **Data type** | **Description**  
---|---|---  
SalesforceTriggerPEPayload | JSON | Details of the change event.  
SalesforceTriggerEvent | JSON | Contains `replayId` of the event.  
SalesforceTriggerSchema | String | Trigger schema.  
The output parameter for this trigger is the `CdcTriggerPayload` JSON variable. The JSON variable contains updated record objects. 

## Best practices

Using the **Salesforce trigger** is recommended in cases where you want to use Salesforce notifications to trigger integrations without writing custom code to publish Salesforce events. Any small field change in your Salesforce case will trigger a Salesforce CDC event, and thus trigger an integration, which can result in significant integration _noise_. Consider using [Change event filters](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_filters.htm) to filter only the required CDC events that trigger the integration. Using [Change event filters](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_filters.htm) can help reduce integration noise and ensure compliance with your license limitations.

Similarly, we recommend unpublishing any integration using this trigger when the integration is no longer needed. Until it is unpublished or deleted, the integration will continue to listen for Salesforce CDC and Platform events. 

## Considerations

Before using the **Salesforce trigger** to run your integration, consider the following: 

  * Salesforce sends a _maximum_ of 100k CDC and Platform events per day. If you buy more platform event capacity from Salesforce, you can publish over 10 million events per day. For more information, see [Platform Event Allocation](https://developer.salesforce.com/docs/atlas.en-us.platform_events.meta/platform_events/platform_event_limits.htm). Contact your Salesforce administrator to understand your license restrictions before choosing CDC events for your integration trigger. **Note** : Multiple integrations using the same Salesforce Channel will not double your Salesforce quota consumption. 
  * If you are planning bulk uploads to Salesforce, consider pausing CDC to reduce integration noise and ensure compliance with your license limitations.
  * The maximum event message size that Salesforce can publish is 1 MB. For more information, see [Change Data Capture Allocations](https://developer.salesforce.com/docs/atlas.en-us.change_data_capture.meta/change_data_capture/cdc_allocations.htm).
  * Application Integration does not support Salesforce CDC events for the following regions: 
    * `asia-northeast1`
    * `asia-south1`
    * `australia-southeast1`
    * `europe-west2`
    * `europe-west3`
    * `europe-west6`
    * `northamerica-northeast1`
    * `southamerica-east1`
    * `us-east4`
    * `us-west2`



## SLA exclusions

The Salesforce trigger is dependent on the [Salesforce](https://developer.salesforce.com/) product. As this dependency is external to the Application Integration, the [Application Integration Service Level Agreement (SLA)](https://cloud.google.com/application-integration/sla) terms and conditions are applicable only when the Salesforce trigger successfully starts the execution of an `active` integration.

## Pricing

The Cloud Pub/Sub trigger and Salesforce trigger don't require you to create a [connector](https://docs.cloud.google.com/integration-connectors/docs/all-integration-connectors). However, if you use the [Connectors task](https://docs.cloud.google.com/application-integration/docs/configure-connectors-task) to connect to Pub/Sub or Salesforce, then you are billed for the connector usage. For information about pricing, see [Application Integration pricing](https://docs.cloud.google.com/application-integration/docs/pricing).

## Quotas and limits

For information about quotas and limits, see [Quotas and limits](https://docs.cloud.google.com/application-integration/docs/quotas).

## What's next

  * Learn about [all tasks and triggers](https://docs.cloud.google.com/application-integration/docs/all-triggers-tasks).
  * Learn how to [test and publish an integration](https://docs.cloud.google.com/application-integration/docs/test-publish-integrations).
  * Learn about [error handling](https://docs.cloud.google.com/application-integration/docs/error-handling-strategy).
  * Learn about [integration execution logs](https://docs.cloud.google.com/application-integration/docs/introduction-logs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
