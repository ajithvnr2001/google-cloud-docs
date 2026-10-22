---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/migrate-support-center/
title: Migrate a voice-channel support center \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:24.949427+00:00
---

# Migrate a voice-channel support center  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/migrate-support-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Migrate a voice-channel support center Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of migrating from an existing voice-channel support center to a contact center based on Contact Center AI Platform (CCAI Platform).

The instructions on this page assume that you have a working support center with an integrated CRM.

## Before you begin

If you are unfamiliar with CCAI Platform, see [Create a sample contact center](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-contact-center).

When you test your new CCAI Platform contact center, you need new telephone numbers. Determine in advance how many numbers you want for your CCAI Platform contact center and contact your account manager to request them.

## Enter basic information

To enter the basic information for your contact center, follow these steps:

  1. To enter the support center email and name, do the following:

     1. In the CCAI Platform portal, go to **Settings > Support Center Details**.

     2. Go to the **General** section.

     3. In the **Support Center Name** field, enter a name for your contact center. This is displayed in reports.

     4. In the **Display Name** field, enter a display name for your contact center. This is displayed to end-users.

     5. In the **Support Email Address** field, enter an administrator email address for your contact center. This is used as a forwarding address for support emails.

  2. Enter time zones, hours of operation, and holiday closures.

For more information, see [Hours of operation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hours-of-operation) settings.




## Set up management operations

CCAI Platform provides a set of features for operation management.

Get your Operation Management settings in order:

  1. Specify the Operation Management settings for your support center.

  2. Create any custom Agent Statuses necessary for your operation.

  3. Establish your Target Metrics such as SLA and Target pickup time.

  4. Decide how you want your calls routed.




## Set up teams

In this task, you create teams that parallel the teams in your existing support center.

You add and configure teams, but you don't add users to the teams. You bulk-upload users in the next section, Upload users.

To set up teams, follow these steps:

  1. Review [User and agent configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user).

  2. For each team in your existing support center, create a team and, if necessary, sub-teams.




## Upload users

To migrate many users from an existing support center to your CCAI Platform contact center, use the bulk user management process.

This lets you populate a CSV file with information about all your users and upload the information to CCAI Platform in a single operation.

To bulk upload your users, follow these steps:

  1. Determine which CCAI Platform roles map best to your existing roles.

For instructions, see [User and agent configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user).

If necessary, you can create custom roles; see [Custom roles and permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions#custom_roles_permissions).

  2. Download a CSV file that you can use as template, edit, and upload the CSV file to create your users.

For instructions, see [Bulk user management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management).




## Create IVR and integrate your CRM

After adding your agents and teams, you need to set up queues for your Interactive Voice Response (IVR) and assign them to agents. After your queues are working, integrate CCAI Platform with your CRM.

  1. Set up queues for IVR calls.

See [IVR: Add and edit queue menus](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-and-edit-ivr-queue-menus).

  2. Assign agents to queues.

See [Setting up and assigning agents to channels and queues: IVR, mobile, web](https://docs.cloud.google.com/contact-center/ccai-platform/docs/setup-agents-channels).

  3. Test the IVR queue menus.

  4. Integrate your CRM.

CRM | See documentation  
---|---  
Salesforce | [Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce)  
[Salesforce Installation Guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce_Installation_Guide)  
[Salesforce Status App Setup 1.0](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce_Status_App_Setup_1_0)  
Zendesk | [Zendesk](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Zendesk)  
[Zendesk App installation guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Zendesk_App_Installation_Guide/publication--en)  
Kustomer | [Kustomer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/kustomer)  
Microsoft Dynamics | [Microsoft Dynamics](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-dynamics-crm)  
Freshdesk | [Freshdesk ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/freshdesk)  
HubSpot | [ HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot)  
ServiceNow | [ ServiceNow](https://docs.cloud.google.com/contact-center/ccai-platform/docs/servicenow)  
Custom CRM | [ Custom CRM](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm)  
  5. Test your CRM integration.




## Port your support center phone number

When you've completed setup and testing of your IVR, you're ready to begin taking live calls from your customers.

Depending on your telephony options, consider taking traffic on both your new CCAI Platform contact center and your existing support center, as agents ramp up on the new system.

Follow these steps to port your support center number:

  1. Review the information about porting.

See [Domestic phone number porting process](https://docs.cloud.google.com/contact-center/ccai-platform/docs/domestic-phone-number-porting-process).

  2. Work with your account manager and your current phone provider to port your phone number.




## What's next

  * To create a mobile app, see [Android SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide) and [iOS SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide).

  * To create a website, see [Web SDK installation guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Guide/publication--en).

  * To add SMS messaging, see [SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sms).

  * To learn about reporting, see Real-time dashboards and monitoring pages.

  * To learn more about Google's AI technology for contact centers, see [Customer Engagement Suite with Google AI](https://docs.cloud.google.com/solutions/customer-engagement-ai).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
