---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/manage-portals/
title: Managing your portals \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:18.332751+00:00
---

# Managing your portals  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/manage-portals/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing your portals Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Create and manage your portals, as described in the following sections.

## About the portal roles

You need one of the following roles to manage your portals. To assign roles to a user, see [Change user roles in the UI](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/manage-users#change-user-roles-in-the-ui).

Role | Description  
---|---  
Portal Administrator | Full CRUD permissions for integrated portals.   
  
**Note** : The Portal Administrator role is not currently visible in the UI. In order to assign the role to a user, use the following `gcloud` command:   
  
`gcloud projects add-iam-policy-binding <project-id> --member=user:<user-email> --role=roles/apigee.portalAdmin`  
Organization Administrator | Super user. Has full CRUD access to resources in the organization. This is a [Apigee-specified role](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles#apigee-specific-roles).  
Read-only Organization Administrator | Has read-only access to resources in the organization. This is a [Apigee-specific role](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles#apigee-specific-roles).  
  
## Exploring the Portals page

To access the Portals page:

In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

The portals page opens and lists the current portals.

The Portals page enables you to:

  * Create a portal
  * Build your portal and its contents
  * [View the live portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/view-live-portal)
  * Edit portal details
  * Delete a portal



## Creating a portal

Create multiple portals for your organization, as required.

When you create a new portal, a set of starter pages is provided for you to use as a jump-off point. See [About the sample portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#sample-portal) and [Quick tips for customizing the sample portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-quick-tips).

**Note** : You can create a **maximum of 10 portals** in your organization.

To create a new portal:

  1. Access the Portals page.
  2. Click **\+ Create**.
  3. Enter the following information in **Create a portal** :

Field | Description  
---|---  
Name | Name of portal. The name can contain only letters, numbers, spaces, and the following special characters: period (.), comma (,), dash (-), or underscore (_). Must be unique across all organizations.   
  
**Note** : If you delete a portal, you cannot immediately create a portal with the same name as the deleted portal will be stored temporarily in the Trash folder.  
Domain | (Read only) As you enter the portal name, the default domain for the portal is displayed. For example: '_orgname-portalname_.apigee.io', where _'orgname'_ is the organization name and _'portalname'_ is defined using the portal name converted to all lowercase and with spaces removed.  
  
**Note** : You can customize the domain name, as described in [Customizing your domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain).  
Description | Description of your portal. This information is for internal use only. It will not be displayed on your live portal.  
  4. Click **Create**.




## Building your portal

To build your portal and its contents:

  1. Access the Portals page.
  2. Click the name of the portal you want to build. The portal landing page is displayed.
  3. Build the portal and its contents, as described in [steps to build your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-steps).



## Editing the portal name and description

To edit portal details, including name and description:

**Note:** You cannot modify the default URL once the portal is created. However, you can create a [custom domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain).

  1. Access the Portals page.
  2. On the portal row you want to edit, click more_vert **More** > edit **Edit**
  3. Edit the portal name and description.
  4. Click **Save**.



## Viewing the live portal

To view the live portal:

  1. Access the Portals page.
  2. On the portal row you want to view, click more_vert **More** > **View live portal**.



The live portal opens in a new browser tab.

## Deleting a portal

There are times when you may need to delete a portal. For example, if you have created a test portal to try out features in your local environment, you may delete it after the testing phase is complete.

**Note:** Existing app registrations and API keys of individual developers won't be impacted when you delete a portal, but all Team related app registrations and API Keys will be deleted. See [ Where app registration and API keys are stored](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#app-keys).

To delete a portal:

  1. Access the Portals page.
  2. On the portal row you want to delete, click more_vert **More** > delete **Delete**
  3. To confirm the delete operation: 
     1. Type **DELETE** in the text field.
     2. Click **Confirm**.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
