---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership/
title: Organizing client app ownership \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:59.373448+00:00
---

# Organizing client app ownership  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/organizing-client-app-ownership/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Organizing client app ownership Stay organized with collections  Save and categorize content based on your preferences. 

This page describes tools and strategies used to organize client app ownership.

## Using AppGroups to organize app ownership

This section provides an overview of AppGroups and how to manage them.

### What are AppGroups?

An AppGroup represents a relationship between one or more apps that are managed by the same set of people.

An AppGroup is associated with another system that is responsible for managing the roster of people who share responsibility for these apps, such as a portal. Both Apigee apps and Apigee developers are associated to the AppGroup.

**Important:** AppGroups provide an abstraction to manage grouped developers as a single entity for the purposes of app ownership and management. Since API access is managed at the credential level for each app, a group of developers that are members of an AppGroup can manage and own AppGroup apps as a single entity. Note that permissions and API key management are handled at the app level, separately from AppGroup membership.

AppGroups provide: 

  * A method of organizing and viewing app ownership and associations.
  * The ability to create a roster for a portal or API storefront of workers who are responsible for an app. For example, you might set up different AppGroups for billing purposes.
  * Flexibility for tracking app ownership by partner, business unit, product line, division, or other corporate entities.
  * A potentially multi-level structure for tracking how apps are logically related to app owners and developers.
  * Monetization integration. Manage subscriptions for groups of app developers by using AppGroups to subscribe to API products with rate plans. For information, see [ Use AppGroups to manage API product subscriptions](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#use-appgroups-to-manage-api-product-subscriptions).



### IAM roles and permissions

To control permissions required for AppGroup management, you can view and grant permissions or roles using the permissions panel on the **IAM & Admin > IAM** page in your Google Cloud project.

[Go to IAM & Admin](https://console.cloud.google.com/iam-admin/iam)

The following table lists the permissions required to create and manage AppGroups resources. You can grant the permissions individually or through an Apigee role including the permissions. See [Users and roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/users-roles-overview) for information on Apigee user and role management.

Description | Permissions  
---|---  
Manage AppGroups and associated apps and keys. | 

  * `apigee.appgroups.list`
  * `apigee.appgroups.get`
  * `apigee.appgroups.create`
  * `apigee.appgroups.update`
  * `apigee.appgroups.delete`

  
Manage AppGroup apps. | 

  * `apigee.appgroupapps.list`
  * `apigee.appgroupapps.get`
  * `apigee.appgroupapps.create`
  * `apigee.appgroupapps.manage`
  * `apigee.appgroupapps.delete`

  
Manage app keys for AppGroups: | 

  * `apigee.appkeys.get`
  * `apigee.appkeys.create`
  * `apigee.appkeys.manage`
  * `apigee.appkeys.delete`

  
Manage AppGroup subscriptions and monetization configurations. | 

  * `apigee.appgroupbalances.adjust`
  * `apigee.appgroupbalances.get`
  * `apigee.appgroupbalances.update`
  * `apigee.appgroupmonetizationconfigs.get`
  * `apigee.appgroupmonetizationconfigs.update`
  * `apigee.appgroupsubscriptions.create`
  * `apigee.appgroupsubscriptions.get`
  * `apigee.appgroupsubscriptions.list`
  * `apigee.appgroupsubscriptions.update`

  
  
### Viewing and managing AppGroups

This section shows how to view and manage AppGroups. You can manage AppGroups and AppGroup apps via the Apigee APIs and Drupal portals. 

**Note:** AppGroup management in Apigee UI in Cloud console will be considered in a future release.**Note:** To manage the Display Name and Notes of an App associated with an AppGroup, you should use the DisplayName and Notes attribute in the [organizations.appgroups.apps.update method](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/update).**Note:** We recommend that you avoid making concurrent update requests for the same resource. Near-simultaneous writes to the same entity can result in conflicts and unexpected behavior. Ensure operations are sequential when modifying a single resource.

#### AppGroup settings

AppGroups include these settings:

Setting | Description | **Name** | Required. The AppGroup name. AppGroup names must be unique across an organization.  
  
Allowed characters are alphanumeric characters and any of these special characters: ._\\-$ %.  
---|---  
**AppGroup Id** | Created automatically and not editable. Created in the form "OrgName@@@AppGroupName". For example, with an Apigee org name `XYZDev` and AppGroup name `ABCMarketing`, the AppGroup Id is `XYZDev@@@ABCMarketing`.  
**Display Name** | Optional. A friendly display name for the AppGroup.  
**channelId** | Optional. Identifies the system responsible for creating and managing the AppGroup. This could be a storefront or marketplace. Multiple AppGroups might share the same channelId.  
**channelUri** | Optional. Reference to the group of people who share responsibility for the AppGroup. Often the channelUri links to or refers to a group or team in a developer portal or other system such as Apigee's Drupal Teams module.  
  
#### Managing AppGroups using Drupal-based portals

Apigee's Team module for Drupal works with AppGroups in Apigee X and hybrid and is the primary interface for managing AppGroups. For information on Drupal-based portals, see [Building your Portal using Drupal](https://cloud.google.com/apigee/docs/api-platform/publish/drupal/open-source-drupal). 

#### Managing AppGroups using the Apigee APIs

Use these APIs to manage AppGroups in your orgs:

Activities | Link | **View and manage AppGroups** | <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups>  
---|---  
**View and manage the apps that belong to AppGroups** | <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps>  
**View and manage the app keys associated to AppGroups** | <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys>  
**View and manage AppGroup subscriptions to API products** | <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions> See also [AppGroup subscription management](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/purchase-api-products-api#appgroup-subscription-management).  
**View and manage AppGroup monetization configurations and balances (if enabled)** | <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions> <https://cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance> See also [Use AppGroups to manage API product subscriptions](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview#use-appgroups-to-manage-api-product-subscriptions) and [Manage prepaid balances](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/manage-prepaid-balances).  
  
### Migrating from Apigee Edge for Drupal users

Migrating a company-developer and its role involves creating an AppGroup representing the company, and adding the company-developer and its role(s) as custom Attributes of the AppGroup. The expected syntax to store this is:
    
    
    [{
          "developer":"<developer email>",
          "roles":[
            "<role(s)>"
          ]
        },
        ...
    ]

## Using developer-app association to organize app ownership

A less comprehensive and flexible method of tracking app ownership than AppGroups is tracking apps by developer association.

For information on managing developer-app associations, see [Registering app developers](https://docs.cloud.google.com/apigee/docs/api-platform/publish/adding-developers-your-api-product) for information on registering developers and associated apps. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
