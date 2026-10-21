---
url: https://docs.cloud.google.com/looker/docs/lookml-diagram-configuring/
title: Configuring the LookML Diagram \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:26:56.394699+00:00
---

# Configuring the LookML Diagram  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/lookml-diagram-configuring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Configuring the LookML Diagram Stay organized with collections  Save and categorize content based on your preferences. 

The LookML Diagram is an extension — a web application built using Looker components — developed using the Looker [extension framework](https://docs.cloud.google.com/looker/docs/intro-to-extension-framework) and deployed through the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace). This documentation page describes the tasks that Looker admins must complete before [Looker users can access and use the extension](https://docs.cloud.google.com/looker/docs/lookml-diagram-using), including:

  1. Enable the appropriate features.
  2. Install the LookML Diagram extension.
  3. Grant permissions to access the LookML Diagram.



## Enabling required features

Before installing the LookML Diagram from the [Marketplace](https://docs.cloud.google.com/looker/docs/marketplace), Looker admins must enable these features:

  * [**Marketplace**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-marketplace): To access the Looker Marketplace (enabled by default)
  * [**Extension Framework**](https://docs.cloud.google.com/looker/docs/admin-panel-platform-extension-framework): To deploy extensions developed using the Looker extension framework (enabled by default)



## Installing the LookML Diagram

Installing applications and tools — such as extensions — from the Marketplace requires [`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop), [`manage_models`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage-models), and [`deploy`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list).

The LookML Diagram extension is listed in the **Applications** section of the Looker Marketplace. See the [Using the Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace#installing_a_tool_from_the_marketplace) documentation page for more detailed instructions on installing a tool from the Looker Marketplace.

After you've installed the extension, you can ensure that you always have the most updated version by going to the Looker Marketplace, clicking **Manage** , and clicking the **Update** button next to the extension.

## Granting permissions to use the LookML Diagram

After the LookML Diagram is installed, a model called `lookml-diagram` is automatically added to the list of available models on the [**New Model Set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#creating_a_model_set) and [**Edit Model Set**](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#editing_a_model_set) pages, accessible from the **Roles** page in the **Admin** panel.

Looker admins must enable users to perform certain tasks with the LookML Diagram extension by granting [permissions](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#permissions_list) to the `lookml-diagram` model and any models the user needs to work with in the LookML Diagram. To enjoy full functionality of the LookML Diagram, users must have `explore` and `deploy` permissions. Refer to the following table for details.

Permission | Depends on | Extension capabilities  
---|---|---  
[`access_data`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#access_data) | None | Users can navigate to the extension but won't be able to interact with it.  
[`explore`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#explore) | `see_looks`, `access_data` | Users can view and interact with the diagram and can access Explores. **Go to LookML** links are visible but not functional. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
[`develop`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#develop) | `see_lookml`, `see_looks`, `access_data` | Users can interact with the diagram and can access LookML project files. **Explore from Field** links are visible but the user is directed to a page that they are not authorized to access. Users cannot switch or select Git branches in the **Diagram Settings** panel.  
[`deploy`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#deploy) | `develop`, `see_lookml`, `see_looks`, `access_data` | The same as with `develop` except that users _can_ switch or select Git branches in the **Diagram Settings** panel. Users can use the extension while in Development Mode.  
  
See the [Setting permissions for Looker extensions](https://docs.cloud.google.com/looker/docs/setting-permissions-for-extensions) documentation page for more information on granting users permissions to access and use extensions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
