---
url: https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions/
title: Setting permissions for Looker extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:37.721388+00:00
---

# Setting permissions for Looker extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Setting permissions for Looker extensions Stay organized with collections  Save and categorize content based on your preferences. 

Extensions are web applications built with Looker components that are developed through the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework). These extensions will inherit the permissions structure of your Looker instance, handling permissions at the model set level. If a user does not have permissions to access certain models in the standard Looker application, they won't be able to access those models in Looker extensions. This page explains how Looker admins can grant users the appropriate permissions to access Looker extensions.

The [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace) deploys an extension by importing a new [project](https://docs.cloud.google.com/looker/docs/how-project-works) into your Looker application. This project contains everything required to run the extension and has at least one [model](https://docs.cloud.google.com/looker/docs/model-and-view-files) file. Looker admins can control how a user views or interacts with content based on that model by assigning them a [role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) that has permissions to access the extension's model.

For example, if your Looker instance has data based on models called `finance`, `marketing`, and `sales`, but you only want certain users to access the finance data, you would grant users access to only the `finance` model. Permissions for extensions work similarly.

> Looker admins can control permissions to access an extension's model (and therefore access the extension itself) as well as the model or models upon which any content _within_ the extension is based.

Looker admins can configure the available model sets for a Looker instance by [navigating to the **Roles** page](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles) in the **Admin** panel. To access and use the extension, users must be assigned a role that has either `manage models` permissions or [`explore` or `develop` permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) for all models or the model set that contains the extensions's model.

## Granting users permissions to extensions

Looker extensions are developed through the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) and are available for installation through the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace). Extensions require that the [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework) and [**Marketplace**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace) features be enabled.

In addition to these features, there are three types of permissions associated with extensions:

  * Permissions to develop extensions
  * Permissions to install extensions from the Looker Marketplace
  * Permissions to use extensions



### Permissions to develop extensions

To develop an extension using the Looker extension framework, users need LookML developer permissions to the instance, as well as the skills recommended on the [Introduction to the Looker extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#extension_framework_requirements) documentation page.

### Permissions to install extensions from the Looker Marketplace

Each extension will have a project with at least one dedicated LookML [model](https://docs.cloud.google.com/looker/docs/model-and-view-files). For example, the [Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary) extension uses the `data-dictionary` model.

To install an extension from the Looker Marketplace, a user must have `develop`, `manage_models`, and `deploy` permissions for the extension's model.

When installing an extension that requires an access key from the Looker Marketplace, a configuration screen prompts the user for access key values, which will be stored as [user attributes](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes) for the Looker instance.

### Permissions to use extensions

If the extension is [installed through the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace#installing_a_tool_from_the_marketplace) or [made available from within a Looker instance](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#adding_extension_to_looker), the Looker admin will need to configure user permissions.

For most extension use cases, the extension always runs with the permissions granted to the user when they log in. By default, once the extension is installed, any user with a role that has `explore` or `develop` permissions and [**Model Set** access](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model_sets) set to **All** will automatically have the ability to view and use the extension _and_ its content with no additional permission configuration required. Users [must have access to all the models](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions#granting_users_permissions_to_extensions) that the extension uses for the extension to function fully.

Looker displays the extension in the **Applications** section of the Looker main menu.

> Looker only displays the extension for Looker users who have access to at least one of the extension's underlying models.

For [embedded extensions](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#embedded_extensions), the extension takes on the [permissions](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#permissions) given to the created [embed user ID](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding#external_user_id), just like an embedded Look, dashboard, or Explore.

For [full screen extensions](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework#full_screen_extensions) that use the `/spartan` option in the extension URL, you can add users to an **Extensions Only** user group. Users in this group are prevented from viewing Looker pages outside of the extension. Looker admins can customize the **Extensions Only** group like any other group and assign it a role that has certain permissions and [model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#model-sets) access. Users are not required to belong to the **Extensions Only** group to view a full screen extension; if a user is not in that user group, the extension will run with the permissions of that logged-in user.

#### Adding user permissions

A Looker admin will need to grant users and embed users a [permission set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permission_sets) that includes [`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) and any more restrictive permissions associated with that extension. These permissions must be applied to a model set that includes the extension's model or models.

To grant users access to the extension, Looker admins must:

  1. [Create a model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#creating_a_model_set) that includes the extension's model — or [edit an existing model set](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#editing_a_model_set) to add the extension's model.
  2. Confirm that users are [assigned to a role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#assigning_roles) with at least the `access_data` permission (and any more restrictive permissions associated with that extension) for this model set.



## Example: Data Dictionary extension

The [Data Dictionary](https://docs.cloud.google.com/looker/docs/using-looker-data-dictionary) extension project uses the `data-dictionary` model.

Users whose roles don't include `explore` or `develop` permissions or that have **Model Set** access _not_ set to **All** will need a Looker admin to grant them `explore` or `develop` permissions for a model set that includes the `data-dictionary` model.

For example, say that you want to give your finance team access to the Data Dictionary extension. The finance team is assigned the `Finance Team` model set, but it does not currently grant access to the `data-dictionary` model:

![A view of the Finance Team model set, which contains flying_research and thelook models but not the data-dictionary model.](https://docs.cloud.google.com/static/looker/docs/images/admin-extension-permissions-1-2214.png)

To add the `data-dictionary` model to their model set, select the **Edit** button next to the `Finance Team` model set and check the `data-dictionary` model checkbox.

Select **Update Settings** to save your selection.

After adding the `data-dictionary` model to the `Finance Team` model set, confirm that the finance team's role uses a permission set that contains `explore` or `develop` permissions. In this example, the finance team's role (**Finance Department**) contains the `Developer` permission set, along with the `Finance Team` model set.

![](https://docs.cloud.google.com/static/looker/docs/images/admin-extension-permissions-3-2220.png)

The `Developer` permission set contains both the `explore` and the `develop` permissions.

Now, any users assigned to the **Finance Department** role will have access to the Data Dictionary extension because that role contains the appropriate permissions and the appropriate model access.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
