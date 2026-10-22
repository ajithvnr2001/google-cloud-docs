---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/about-global-users/
title: About global users \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:06.927870+00:00
---

# About global users  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/about-global-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  About global users Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

All Apigee users are called global users because they are created outside of any Apigee organization. Once created, a global user can then be assigned to one or more organizations:

![Global user roles.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/globalUserRoles.png)

**Note:** Your ability to add new users may depend on your account type. For more information, see [Apigee Pricing](https://cloud.google.com/apigee/pricing). 

When you assign a user to an organization, you must specify the user's role in that organization. The user's role determines the actions that the user is allowed to perform in that organization. For example, some users are allowed to create APIs, while others can view APIs but cannot modify them. 

A global user can also be assigned to the role of Apigee organization administrator or Apigee read-only administrator. An organization administrator performs all administrative tasks required to maintain Apigee, including creating new global users.

## What information defines a user?

An Apigee user is defined by the following:

  * First name
  * Last name
  * Email address
  * Password



The email address and password function as the user's credentials when logging in to the Apigee UI and when making requests through the Apigee API. 

## What are roles?

On its own, a global user cannot do anything in Apigee. For a global user to be able to function, the user must be assigned to an organization role.

Roles are essentially CRUD-based permission sets. CRUD means "create, read, update, delete". For example, a user may be given a role in an organization that permits read, or "get", access to details about a protected entity, but not write permission to update or delete it. The organization administrator is the highest-level role in the organization, and can perform any CRUD operation on any entity in the organization.

### About predefined organization roles

All Apigee organizations are created with the following roles with a [predefined set of permissions](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles):

  * Organization Administrator
  * Read-only Organization Administrator
  * Operations Administrator
  * Business User
  * User



You can also create custom roles, with custom permissions, in your organization.

### About the administrator roles

Apigee supports the following administrator roles:

  * Read-only administrator role
  * Organization administrator role



Apigee organization administrators can:

  * Create organizations and environments
  * Add additional components to an Apigee installation
  * Configure TLS/SSL
  * Create additional administrators
  * Perform all other Apigee administrative tasks

**Note:** While it is not required, you can assign a read-only administrator to an organization, typically as an organization administrator. Unless assigned to an organization, the read-only administrator cannot even log in to the [Apigee UI](https://apigee.google.com).

For details about administrator permissions, see [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles).

## Assigning global users to an organization

The following image shows the structure of an Apigee organization:

![Organization contains users and developers.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/orgUserDev.png)

An organization contains two distinct types of users:

  * **Organization users** : Create, modify, and deploy APIs, create and manage entities such as API products, developers, and developer apps, generate analytics reports, and perform other administrative tasks. **Organization users are Apigee global users** assigned to an organization with a specific role.
  * **Developers** : Build the apps that make requests to your APIs. **A developer is not an Apigee global user.** Think of developers as your API customers. To access the APIs in your organization, a developer must register with the organization and then request an _API key_. A developer can be registered with multiple organizations to consume APIs from different organizations. 



The big difference between users and developers in an organization is that **users are Apigee global users that build and maintain APIs** , while **developers are customers that build apps that consume those APIs**. Developers typically do not have global user accounts on Apigee, and cannot log in to the Apigee UI. The exception to this is an organization user who creates their own developer and developer apps for testing purposes.

**Note:** There is actually one more type of user that you have to be concerned with - the **app user**. This is the person who uses the apps created by **developers**. However, app users are not defined or controlled by Apigee. It is up to you to decide how to implement authentication and authorization for app users. For example, an app might require the app user to log in. How you process that log in is up to you, possibly by accessing a backend LDAP service or other type of authentication mechanism. 

For more on developers, see [Publishing overview](https://docs.cloud.google.com/apigee/docs/api-platform/publish/publishing-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
