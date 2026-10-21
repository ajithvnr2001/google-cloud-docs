---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-salesforce-campaigns-integration/
title: Sending data to Salesforce Campaigns \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:19:46.248602+00:00
---

# Sending data to Salesforce Campaigns  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-salesforce-campaigns-integration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Sending data to Salesforce Campaigns Stay organized with collections  Save and categorize content based on your preferences. 

You can use Looker's Salesforce Campaigns integration to create campaigns in Salesforce and populate the campaign members with leads and contacts from a Looker Explore or Look. You can choose to create a new campaign or append users to an existing campaign in Looker.

## Setup requirements

  * Salesforce API v42.0 and later (released Spring 2018)
  * Users will need "Create" and "Edit" [permissions](https://help.salesforce.com/s/articleView?id=sf.admin_userperms.htm&type=5) on the Campaigns object (this is associated with the "Marketing User" profile by default) as well as the "Marketing User" checkbox selected on their user profile 
    * If you do not have sufficient permissions, you may see the following error message: `entity type cannot be inserted...`



## Setup instructions

  1. Create a [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#creating_user_attributes) to control access to the action and specify the Salesforce domain. On the **User Attributes** page in the **Users** section of the **Admin** menu, click **Create user attribute**. Define your new user attribute:

     * Name: **salesforce_campaigns_action_domain**
     * Label: **Salesforce Campaigns Action Domain**
     * Data Type: **String**
     * User Access: **View**
     * Hide Values: **No**
     * No default value

Select **Save**.

  2. Once you define a user attribute, you can assign Salesforce domain (for example, "https://MyDomainName.my.salesforce.com") as a _value_ to the individual users and user groups that will use the action. Select the **User Values** and **Group Values** tabs at the top of the **User Attributes** page to assign values to [individual users](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users) and [user groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups), respectively.

     * Different users can target different domains (for example, a Staging or Development Salesforce instance), and you can update the domain value at any time.
     * Users who do not have an assigned value will not see the action as a destination option.
  3. Next, enable the action. Go to the **Actions** page in the **Platform** section of the **Admin** menu, and select **Enable** next to the **Salesforce Campaigns Action Domain** action. On the **Salesforce Campaigns Action Domain** page, enable the **Enabled** toggle, and select the **Salesforce Campaigns Action Domain** user attribute for the **Salesforce domain** field. Click **Save**.

  4. Optionally, set up LookML tags `sfdc_contact_id` and `sfdc_lead_id` for contacts and lead fields, respectively. Alternatively, the action will attempt to regex match the field label with the following expressions: `/contact id/i` and `/lead id/i` (case insensitive).




## Using the Salesforce Campaigns action

Once the Salesforce Campaigns action has been configured, you can use it in the Looker Scheduler:

  1. From a Look or an Explore, [create a schedule or select the option to **Send** a one-time delivery](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#creating_a_delivery).
  2. Under **Where should this data go?** , select the **Salesforce Campaigns** action.
  3. The first time you use the action, you will be prompted to log in to Salesforce. Click **Log in**.
  4. On the OAuth consent screen, click **Allow** and return to the Looker Scheduler window.
  5. Select **Verify credentials**. Once you've logged in to Salesforce within the Looker Scheduler, fill out the **Salesforce Campaigns** action form to configure the details of your Look or Explore delivery:

     1. **Create or Append** : Select **Create** create a new campaign or **Append** to modify an existing campaign.
     2. **Campaign Name** : Enter the name for the new campaign or select an existing campaign.
     3. **Member Status** : Select the status of the campaign members. This list will be populated from available statuses from your Salesforce instance.
     4. **Surface Salesforce Errors In Looker** : Set this to **Yes** to surface any Salesforce errors with setting campaign members in Looker's scheduled job status detail. This will record an **Error** in Looker's scheduled job status on the **Schedule History** page in the **Admin** menu, which is useful for troubleshooting errors on a member level. Set this to **No** to ignore all errors related to campaign members (default). This will record a **Complete** status, regardless of any errors that might have occurred when you set up the campaign members.
  6. Specify any other options for your delivery.

  7. Select **Send**.




## Removing the Salesforce Campaigns action

If you want to switch the connected Salesforce instance or disconnect the Looker action from your Salesforce instance, you can [revoke the connection](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_request_manage.htm&) to the Looker application from within your Salesforce account.

## Limitations

  * This action is limited to a maximum of 5,000 rows. The functionality to send all results is currently being developed.
  * Each Salesforce Edition has a limit to the number of API calls that are allowed in a 24-hour period. Refer to the [Salesforce API Request Limits and Alloctions](https://developer.salesforce.com/docs/atlas.en-us.salesforce_app_limits_cheatsheet.meta/salesforce_app_limits_cheatsheet/salesforce_app_limits_platform_api.htm) documentation to learn your instance's API limits. This action leverages POST requests with [sObject Collections](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/resources_composite_sobjects_collections_create.htm) to execute multiple records (200 records per API call) in a single request.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
