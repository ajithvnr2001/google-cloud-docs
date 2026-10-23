---
url: https://docs.cloud.google.com/support/docs/checklists/onboard-customer-care/
title: Onboard to Cloud Customer Care \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:10.037430+00:00
---

# Onboard to Cloud Customer Care  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/support/docs/checklists/onboard-customer-care/

When creating a case, **Live chat** is your quickest connection to a support representative. For more information, see [Create a support case](https://docs.cloud.google.com/support/docs/customer-care-procedures#create_a_support_case). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Customer Care ](https://docs.cloud.google.com/support/docs)
  * [ Guides ](https://docs.cloud.google.com/support/docs/overview)



Send feedback 

#  Onboard to Cloud Customer Care Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to onboard to Customer Care so that you can effectively engage with Customer Care teams and have a beneficial support experience.

## Checklist

Learn how to onboard to Customer Care by completing the following tasks:

    

1\.  Understand and benefit from your support package.   
2\.  Set up your Google Cloud project environment.   
3\.  Configure access control.   
4\.  Create a test support case.   
5\.  Set up Essential Contacts.   
6\.  Use additional services.

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/freetrial?redirectPath=/?walkthrough_id=support--onboard-customer-care)

* * *

## Before you begin

Customer Care offers several support packages. This guide assumes that you have already purchased a Customer Care support package:

  * [Purchase and set up Standard Support](https://docs.cloud.google.com/support/docs/purchasing-setting-up-standard)
  * [Purchase and set up Enhanced Support](https://docs.cloud.google.com/support/docs/purchasing-setting-up-enhanced)
  * To purchase Premium Support, [contact sales](https://cloud.google.com/contact)

**Note:** Basic Support is included for all Google Cloud customers, and provides access to [documentation](https://docs.cloud.google.com/support/docs/overview), [community support](https://docs.cloud.google.com/support/docs/community-support), [Cloud Billing support](https://docs.cloud.google.com/support/billing), and [Active Assist recommendations](https://docs.cloud.google.com/recommender/docs/whatis-activeassist).

## Understand and benefit from your support package

Make sure that you understand your Customer Care package so that you can fully benefit from the services and features included in it.

  1. Learn about your Customer Care package and [compare package features and services](https://docs.cloud.google.com/support#compare-features):

     * [Standard Support](https://docs.cloud.google.com/support/docs/standard) is recommended for small to medium organizations with workloads under development looking to begin their support journey.
     * [Enhanced Support](https://docs.cloud.google.com/support/docs/enhanced) offers faster response times and additional services designed for medium to large companies running their cloud workloads in production.
     * [Premium Support](https://docs.cloud.google.com/support/docs/premium) is designed for enterprises that run priority workloads and require fast response times, platform stability, and increased operational efficiencies.
  2. Optionally, increase your capabilities with Value-Add Services. Value-Add Services are available as an additional purchase for Enhanced and Premium Support customers:

     * Enhanced Support:

       * [Technical Account Advisor Service](https://docs.cloud.google.com/support/docs/enhanced#taas) provides increased oversight and assistance from experts who are invested in your organization's success.
       * [Planned Event Support](https://docs.cloud.google.com/support/docs/enhanced#pes) provides coverage for critical phases of high-traffic short-term digital events like grand openings, new product launches, or data migrations.
       * [Assured Support](https://docs.cloud.google.com/support/docs/enhanced#assured_support) delivers an essential layer of compliance to secure your workloads.
       * [Media CDN](https://docs.cloud.google.com/support/docs/enhanced#enhanced-support-mediacdn) provides an elevated level of technical support during specific content delivery events, such as live VOD streaming events.
     * Premium Support:

       * [Mission Critical Services](https://docs.cloud.google.com/support/docs/premium#mission_critical) lets you assess and mitigate potential service disruptions for environments that are essential to an organization and can cause significant impact when disrupted.
       * [Assured Support](https://docs.cloud.google.com/support/docs/premium#assured_support) delivers an essential layer of compliance to secure your workloads.
       * [Media CDN](https://docs.cloud.google.com/support/docs/premium#premium-support-mediacdn) provides an elevated level of technical support during specific content delivery events, such as live VOD streaming events.



## Set up your Google Cloud project environment

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.  


[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  3. Enable the Cloud Support, Essential Contacts, and Service Health APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudsupport.googleapis.com,essentialcontacts.googleapis.com,servicehealth.googleapis.com)

     * Use the Cloud Support API to programmatically create and manage support cases. The API is available to Customer Care customers with Standard, Enhanced, or Premium Support. Alternatively, if you prefer to use a graphical interface, you can use the Google Cloud console to [create and manage support cases](https://docs.cloud.google.com/support/docs/customer-care-procedures). For more information, see the [API overview](https://docs.cloud.google.com/support/docs/reference/support-api).
     * Use the Essential Contacts API to customize who receives Google Cloud notifications by providing your own list of contacts. Note that if you want to manage contacts through the Google Cloud console only, you don't need to enable the API. In this guide, see Set up Essential Contacts.
     * Use the Service Health API to access Personalized Service Health and receive communications about active and past Google Cloud incidents that might impact your projects and resources. In this guide, see Use additional services.



## Configure access control

To manage how users in your organization access and use a Customer Care package, you must have a Google Cloud organization, and the [Organization Administrator](https://docs.cloud.google.com/resource-manager/docs/access-control-org#using_predefined_roles) Identity and Access Management (IAM) role for the organization.

  1. To create an organization and add an Organization Administrator, see [Creating and managing organization resources](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).

  2. As the Organization Administrator, you can grant the Support Account Administrator role by following the steps in the next section. If you are the Organization Administrator, you can also grant yourself the role.

  3. If you are not the Organization Administrator for an existing organization, contact your Organization Administrator to grant you the Support Account Administrator role.




For more information, see [Access control with IAM](https://docs.cloud.google.com/support/docs/access-control).

### Grant the Support Account Administrator role

The [Support Account Administrator](https://docs.cloud.google.com/support/docs/access-control#support_account_admin) role allows management of a support account without giving access to support cases, and it can be granted only at the organization level.

  1. In the Google Cloud console, go to the **IAM & Admin** > **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Using the resource selector on the console toolbar, select your organization.

  3. Select a principal to grant a role to. A principal can be a user, service account, or Google group.

     * To grant a role to a principal who already has other roles on the resource, find a row containing the principal, click edit **Edit principal** in that row, and click add **Add another role**.

     * To grant a role to a principal who doesn't have any existing roles on the resource, click person_add **Grant Access** , then enter an identifier for the principal—for example, `my-user@example.com`.

  4. In the **Select a role** list, select **Support Account Administrator**.

  5. Click **Save**.

As the Support Account Administrator, you can grant the Tech Support Editor role by following the steps in the next section. If you are the Support Account Administrator, you can also grant yourself the role.




### Grant the other required roles

  * To create and manage support cases: 
    * [Tech Support Editor](https://docs.cloud.google.com/support/docs/access-control#tech_support_editor): to enable read-write access to the support cases. You can grant this role at the organization, folder, or project levels.
  * To create and manage advisory support cases, including event requests (for Premium Support customers). These roles can only be granted at the organization level. 
    * [Advisory Support Editor](https://docs.cloud.google.com/support/docs/access-control#cloudsupport.advisorySupportEditor): to enable read-write access to advisory support cases, including event requests.
    * [Advisory Support Viewer](https://docs.cloud.google.com/support/docs/access-control#cloudsupport.advisorySupportViewer): to enable read-only access to advisory support cases.
  * To manage support event subscriptions (optional): 
    * [Support Subscription Editor](https://docs.cloud.google.com/support/docs/access-control#support_subscription_editor): to enable read-write access to support event subscriptions. This role can only be granted at the organization level.
    * [Support Subscription Viewer](https://docs.cloud.google.com/support/docs/access-control#support_subscription_viewer): to enable read-only access to support event subscriptions. This role can only be granted at the organization level.



To grant roles, do the following:

  1. In the Google Cloud console, go to the **IAM & Admin** > **IAM** page.

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  2. Using the resource selector on the console toolbar, select your organization, folder, or project.

  3. Select a principal to grant a role to:

     * To grant a role to a principal who already has other roles on the resource, find a row containing the principal, click edit **Edit principal** in that row, and click add **Add another role**.

     * To grant a role to a principal who doesn't have any existing roles on the resource, click person_add **Grant Access** , then enter an identifier for the principal—for example, `my-user@example.com`.

  4. In the **Select a role** list, select the role you want to grant.

  5. Click **Save**.




## Create a test support case

Writing a detailed support case makes it easier for the Customer Care team to respond to you quickly and efficiently. The best support cases are both detailed and specific. For more information, see [Create and manage support cases](https://docs.cloud.google.com/support/docs/customer-care-procedures) and [Best practices for working with Customer Care](https://docs.cloud.google.com/support/docs/best-practices).

To understand how to file a support case, create a test support case:

  1. In the Google Cloud console, go to the **Support** > **Cases** page.

[Go to Cases](https://console.cloud.google.com/support/cases)

  2. Using the resource selector on the console toolbar, select the resource for which you'd like to create a support case. Support cases can be created for either organizations or projects.

  3. Click _add_box_ **Get help**.

  4. In the **Select a product** list, search for **Compute Engine** and select it.

  5. In the **Describe your issue** field, enter `Test issue`.

Learn more about [the essential details you should provide](https://docs.cloud.google.com/support/docs/best-practices#describing_your_issue) such as timestamps, locations, and logs.

  6. In the **Observed error message** field, enter `Test message`.

  7. Accept the default priority of **P4 - Low impact** and click **Next**.

Learn more about [how to set the priority](https://docs.cloud.google.com/support/docs/best-practices#setting_the_priority_and_escalating).

  8. Explore the listed resources that might help resolve your issue. To proceed, click **Next**.

  9. In the **Select a category** list, select a sub-category that best describes your issue.

This ensures that your case is forwarded to the correct team.

  10. Choose a support channel: **Live chat** or **Email**.

Live chat is available only in English. A transcript will be emailed to you and can be viewed in the console by those who have the appropriate permission.

If you select email, you can also specify a supported language.

  11. In the **Business impact** list, select **Other**.

  12. In the **Compute Engine VM Instances** field, enter `none` and then select **none (Create new)**.

  13. In the **Third Party Support Consent** list, select **Yes**.

  14. For this test support case, you can accept the other defaults but for an actual support case, you should provide as many details as possible.

  15. Click **Submit**. The Customer Care team responds to the case based on its priority and the support package that applies.

After you submit the form, you're returned to the **Cases** page.

  16. To close the case, do the following:

     1. Click **View case**.
     2. In the **General Information** section, click **Close case**.
     3. To confirm the action, click **Yes**.

You can also add comments, escalate, upload file attachments, or modify other case attributes.

After you close a case, you will receive a Customer Feedback Survey about your support case.




## Set up Essential Contacts

Many Google Cloud offerings, such as Cloud Billing, send out notifications to share important information with Google Cloud users. By default, these notifications are sent to members with certain IAM roles. With Essential Contacts, you can customize who receives notifications by providing your own list of contacts. For more information, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

### Grant required roles

To get the permissions that you need to manage contacts, ask your administrator to grant you the following IAM roles on the project, folder, or organization where the contact is assigned : 

  * To view contacts: [Essential Contacts Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/essentialcontacts#essentialcontacts.viewer) (`roles/essentialcontacts.viewer`) 
  * To view, edit, delete, and create contacts: [Essential Contacts Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/essentialcontacts#essentialcontacts.admin) (`roles/essentialcontacts.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Add a contact

You can add contacts, remove them, or assign notification categories for them.

  1. In the Google Cloud console, go to the **IAM & Admin** > **Essential Contacts** page.

[Go to Essential Contacts](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector on the console toolbar. The resource selector tells you what project, folder, or organization you are managing contacts for.

  3. Click person_add **Add contact**.

  4. In the **Email** and **Confirm email** fields, enter the email address of the contact.

  5. In the **Notification categories** list, select the notification categories that you want the contact to receive communications for. For more information, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

  6. Click **Save**.




## Use additional services

To automate and optimize your performance across Google Cloud, you can access the following additional services:

  * **Personalized Service Health** lets you identify Google Cloud service disruptions relevant to your projects so that you can manage and respond to them efficiently. For more information, see [Monitor Google Cloud Service Health incidents](https://docs.cloud.google.com/support/docs/dashboard).

While Personalized Service Health offers extensive coverage of incidents relevant to you, you can also view the public status dashboard: [Google Cloud Service Health](https://status.cloud.google.com/).

To view your personalized incidents, in the Google Cloud console, go to the **Service Health** > **Google Cloud Incidents** page:

[Go to Google Cloud Incidents](https://console.cloud.google.com/servicehealth/incidents)

  * **Recommender** lets you receive recommendations and insights through a portfolio of tools called Active Assist that can optimize your Google Cloud resources for cost, security, performance, and manageability. For more information, see the [Recommender documentation](https://docs.cloud.google.com/recommender/docs).

To view your recommendations, in the Google Cloud console, go to the **Active Assist** :

[Go to Active Assist](https://console.cloud.google.com/active-assist/dashboard)

  * **Google Cloud Skills Boost** provides a portal where you can pursue the credentials and training you or your team need to achieve your goals. For more information, [contact your sales team](https://cloud.google.com/contact) about how to access Google Cloud Skills Boost.

To explore the offerings, go to the **Google Cloud Skills Boost** portal:

[Go to Google Cloud Skills Boost](https://www.cloudskillsboost.google/)




## What's next

  * [Create and manage support cases](https://docs.cloud.google.com/support/docs/customer-care-procedures)
  * [Best practices for working with Customer Care](https://docs.cloud.google.com/support/docs/best-practices)
  * [Best practices for working with Premium Support](https://docs.cloud.google.com/support/docs/premium-best-practices)
  * [Language support and working hours](https://docs.cloud.google.com/support/docs/language-working-hours)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
