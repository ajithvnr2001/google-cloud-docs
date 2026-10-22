---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product/
title: Registering app developers \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:46:04.287626+00:00
---

# Registering app developers  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Registering app developers Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Register and manage your app developers, as described in the following sections. (App registration is a separate process, as described in [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api)).

## Introduction

Apigee provides many benefits that are completely dependent on knowing who's calling your APIs. For example, API security, traffic management, and a fair amount of analytics data depend on knowing who's calling. And how does Apigee know who's calling your APIs? By reading unique information in each API call, such as a user ID, an API key, or an OAuth token. That unique information locks or unlocks the functionality you build into your API proxies, giving you full control over API access and behavior.

That's why app developers need to register to use your APIs. Once added, developers register their apps, choose the APIs they want to use, and receive the unique API credentials (consumer keys and secrets) needed to access your APIs.

**Warning:** API security, traffic management, and developer/app analytics are dependent on proper API proxy configuration. For example, you need to add the right policies to your proxies, such as API key validation or OAuth access token verification, quota enforcement, and rate limiting. Those policies identify which specific developer and app is making the call, which in turn enables API security enforcement, developer- or app-specific traffic management, API analytics capture, and other functionality. Technically, you could develop open APIs that don't check for API keys or access tokens, which means you wouldn't really need to register developers. But we strongly discourage this, because you lose API security, lose control over performance (through good traffic management), lose out on analytics data, and miss out on other major benefits that Apigee provides.

### How to register app developers

Register app developers using one of the following methods:

  * If you have a paid Apigee account, developers can self-register through a developer portal. For more information, see one of the following sections based on the type of developer portal: 
    * **Integrated portal** : [Creating a user account on the integrated portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register)
    * **Drupal 10** : [Register an app developer](https://www.drupal.org/docs/8/modules/apigee-edge/understand-how-app-developers-interact-with-the-apigee-edge-module#register)
  * Administrators can register app developers using the API.
  * As a developer portal administrator, manage developers directly on your portal, as described in the following sections: 
    * **Integrated portal** : [Managing users](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users) to manage user accounts. **Note:** After a user creates an app on the integrated portal, as described in this section, the user account information is synced to and available on Apigee on the Developers page. The app developer record is associated with the account using the user's email address. For more information about where account and associated app information is stored, see [Where app developer account information is stored](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#apidev-info-stored).
    * **Drupal 10** : [Understand how app developers interact with the Apigee module](https://www.drupal.org/docs/8/modules/apigee-edge/how-app-developers-interact-with-the-apigee-edge-module)
  * As an organization administrator, manage developers using the Apigee UI or API, as described in the following sections.

**Note:** When portal users create a team in the integrated portal, the developer team information is stored on Apigee and a unique, auto-generated email address is generated to serve as the primary key used by Apigee to identify the developer team. For more information, see [Where developer team information is stored (beta)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#team-info-stored).

### Recommendations for managing user accounts on developer portals

Apigee recommends that you manage user accounts directly on your developer portal. 

If you are using the integrated portal, this is the only way to ensure that the user accounts on the integrated portal and Apigee stay in sync. 

If you use the Drupal-based developer portal, managing user accounts directly on the developer portal provides the following advantages:

  * When you add a developer through the administrator interface on the portal, you can set the developer's password for the portal and trigger an automated email message sent to the developer.

When adding or modifying a developer using Apigee, no email is sent to the developer and you cannot set the password for the developer on the portal. Therefore, the developer must reset their password on the portal before they can sign in to the portal.

  * Any changes made to the developer's account on the portal are automatically sent to Apigee. 



If you decide to manage Drupal-based user accounts using Apigee, you must synchronize app developers between the portal and Apigee.

## Exploring the Developers page

Access and explore the Developers page using the Apigee UI. **Note:** For integrated portals, user accounts are managed as described in [Managing users](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users). After a developer creates an app on the integrated portal, as described in [Registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-interact#register-apps), a separate developer record is created to track apps associated with the user account and can be accessed on the Developers page. The developer record is associated using the user's email address.

To access the **Distribution > Developers** page:

[Go to Developers](https://console.cloud.google.com/apigee/developers)

The **Developers** page enables you to: 

  * Add a developer
  * View and edit developer details, including the following:
    * Manage custom attributes
    * Activate or deactivate a developer
  * Export publishing data
  * Delete a developer
  * Search the list of developers



## Adding a developer

To add a developer:

  1. Access the Developers page.
  2. Click **\+ Create**.
  3. Enter the developer details, including first name, last name, email, and username. 
  4. Click **Add**.



See also [Managing users](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-users).

## Viewing and editing developer details

**Note:** We recommend that you avoid making concurrent update requests for the same resource. Near-simultaneous writes to the same entity can result in conflicts and unexpected behavior. Ensure operations are sequential when modifying a single resource.

View and edit developer details.

To view and edit developer details:

  1. Access the Developers page.
  2. Click the row of the developer that you want to view and edit to open the developer details. 
  3. In the **Details** section, the following information is displayed. Click edit **Edit** to edit the developer details, as required. Detail | Description | Details |  Developer first and last name, username, and email; registration status and duration; and developer ID.   
---|---  
Custom attributes | Custom attributes defined for the developer. Configure custom attributes, as required. For more information, see: Managing custom attributes for a developer  
Apps | Apps that have been registered by the developer. See [Controlling access to your APIs by registering apps](https://docs.cloud.google.com/apigee/docs/api-platform/publish/creating-apps-surface-your-api).  
  4. Activate or deactivate the developer in the **Status** field.  
For more information, see Activating and deactivating a developer.



Apigee keeps the following entities in cache for a minimum of 180 seconds after the entities are _accessed_.

  * OAuth access tokens. This means the [ `ExpiresIn`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy#expiresinelement) element on the OAuth v2 policy won't be able to expire an access token in less than 180 seconds.
  * Key Management Service (KMS) entities (Apps, Developers, API Products).
  * Custom attributes on OAuth tokens and KMS entities.



## Managing custom attributes for a developer

Add up to 18 custom attributes for each developer.

To manage custom attributes:

  1. Access the Developers page.
  2. Click the row of the developer for which you want to manage custom attributes to to open the developer details. 
  3. Click edit **Edit**.
  4. Click **\+ Add attribute** in the **Custom Attributes** section.
  5. Enter the attribute name and value.
  6. Click **Save**.
  7. To delete a custom attribute, click edit **Edit** , then delete **Delete** , then click **Save**. 



## Activating and deactivating a developer

When an app developer self-registers in your portal, you can configure whether or not they are active by default. 

When a developer is inactive, the developer can still sign in to the developer portal and create apps, but none of the corresponding API keys will work. The developer's apps still retain their approved (or other) status, as do the API keys, even though they're not valid while the developer is inactive. 

**Note:** When you deactivate a developer, it may take a few minutes for the change to be updated on all message processors. Until then, some calls by the developer's app may succeed. 

To activate or deactivate a developer:

  1. Access the Developers page.
  2. Click the row of the developer that you want to activate or deactivate to to open the developer details. 
  3. Click edit **Edit**.
  4. In the Details section, set the **Status** field to **Active** or **Inactive** , as required. 
  5. Click **Save**.
  6. Repeat the steps if the developer is in multiple organizations.



## Exporting publishing data

This section describes how to export publishing data for developers, apps, or API products as a comma-separated values (CSV) file or JSON file. 

Prerequisites:

  * Cloud Storage bucket
  * Read access to the data you are exporting
  * Read + write access to the Cloud Storage bucket



For more information on buckets, see the following:

  * [About Cloud Storage buckets](https://docs.cloud.google.com/storage/docs/buckets)
  * [Create a bucket](https://docs.cloud.google.com/storage/docs/creating-buckets)
  * [Listing buckets](https://docs.cloud.google.com/storage/docs/listing-buckets)



To export publishing data:

  1. Create the Cloud Storage bucket or get the name of an existing bucket.
  2. Access one of the following pages: 
     * In the Google Cloud console, go to the **Apigee > Distribution > Developers** page.

[Go to Developers](https://console.cloud.google.com/apigee/developers)

     * In the Google Cloud console, go to the **Apigee > Distribution > Apps** page.

[Go to Apps](https://console.cloud.google.com/apigee/apps)

     * In the Google Cloud console, go to the **Distribution > API Products** page.

[Go to Products](https://console.cloud.google.com/apigee/apiproducts)

  3. Click **Export**.
  4. The **Save table as** dialog displays. Type the name of the Cloud Storage bucket and specify the export format; JSON or CSV.
  5. Click **Save**. A long-running operation (LRO) starts. The LRO status is shown in the notifications_none **Notification** icon.
  6. Once the export is complete, click **Download** in the notification. The Cloud Storage bucket page for the file opens.
  7. Click **Download**. The file is downloaded to your local machine.

Notes on the exported data: 
  * The structure of the exported data follows the proto definitions exactly so the proto documentation can be used as a reference for the exported data structures. See: 
    * [Developers](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers)
    * [Apps](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps)
    * [API Products](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts)
  * Unlike the Apigee Classic UI, each resource has an independent, dedicated export button. 
  * CSV exports don't list any repeated or nested fields from the proto as it cannot properly be represented in a table data structure. In order to get this information JSON export must be used. 
  * Exported files are named `ExportFinal_{hash}`.



## Deleting a developer

**Warning:** Deleting developers completely removes them and their related artifacts (such as apps and API keys) from your organization. To avoid permanently deleting developers and their artifacts, consider deactivating developers instead.

To delete a developer:

  1. Access the Developers page.
  2. Position your cursor over the row of the developer that you want to delete. 
  3. Click more_vert **More** , then click delete **Delete**. 
  4. Click **Delete** to confirm the deletion.



## Synchronizing app developers between the portal and Apigee

If you are using a Drupal-based developer portal to publish your APIs, changes made to app developers using Apigee are not propagated to the portal. You must sign in to the portal as a portal administrator and synchronize the portal with Apigee for those changes to appear on the portal.

**Note:** If you use the Drupal-based developer portal, Apigee recommends that you manage app developers directly on your portal, not using Apigee. See Recommendations for managing user accounts on developer portals.

To synchronize your developer portal with the app developers defined on Apigee, refer to the following section:

Drupal 10: [Synchronize developers with Apigee](https://www.drupal.org/docs/8/modules/apigee-edge/synchronize-developers-with-apigee-edge)

## Managing developers using the API

Manage developers using the [Developer APIs](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
