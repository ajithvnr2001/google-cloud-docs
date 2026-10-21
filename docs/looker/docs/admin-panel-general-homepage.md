---
url: https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage/
title: Admin settings - Homepage \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:14:57.367009+00:00
---

# Admin settings - Homepage  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-general-homepage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Homepage Stay organized with collections  Save and categorize content based on your preferences. 

The **Homepage** page in the **General** section of Looker's **Admin** menu lets admins configure a default homepage for their Looker instance. Looker admins can also set a homepage for a specific user or group with the `landing_page` [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Setting a default homepage for your instance

The Looker homepage appears when users log in to Looker or navigate to the homepage by clicking **Home** in the left navigation panel or by clicking the Looker logo. By default, the homepage for your instance is the [pre-built Looker homepage](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage), which displays a user's favorite content, that user's recently viewed content, and the recently viewed content at the organization. However, you can change this default to a URL within Looker.

![](https://docs.cloud.google.com/static/looker/docs/images/browse-folders-homepage-2412.png)

The homepage options for your instance are available on the **Homepage** page under **Set a default homepage for your organization** :

  * **Looker's pre-built homepage** : The [pre-built Looker homepage](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage) displays tabs for recently viewed content and favorited content. This setting is the default.

**Note:** If you are using Looker (Google Cloud core), the pre-built homepage also displays the following sections in addition to the **Recently Viewed** and **Favorites** tabs: 
    * A **Sample Dashboards** section, which displays the [sample dashboards](https://docs.cloud.google.com/looker/docs/looker-core-sample-project#view_and_edit_the_sample_dashboards) from the sample LookML project, unless the sample LookML project has been [removed](https://docs.cloud.google.com/looker/docs/looker-core-sample-project#remove_the_sample_lookml_project).
    * A **BigQuery Connection** section, which is visible to users with the [`manage_project_connections` Looker permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_project_connections). This section won't appear if the default BigQuery connection for the instance has been set up already.
  * **A URL within Looker** : You can set the default homepage to a specific page within Looker (such as the **Favorites** page), a [board](https://docs.cloud.google.com/looker/docs/presenting-content), a [folder](https://docs.cloud.google.com/looker/docs/organizing-spaces), or a Markdown file (such as a README or [document file](https://docs.cloud.google.com/looker/docs/other-project-files#document_files) in a project) by specifying a relative URL such as `/browse/boards/2`. If you set the homepage in your instance to a specific page within Looker or to a board, the **Home** button in the left navigation panel updates to the name of the page or the board.




If you have configured group or user homepage settings with the `landing_page` user attribute, those settings will override the default homepage that you have chosen for your instance. Users with group or user homepages will still be able to access a link to the instance-wide default homepage from the left navigation.

## Setting a homepage for a specific user or group

In addition to setting a homepage for your entire instance, you can configure homepage settings for specific [users](https://docs.cloud.google.com/looker/docs/admin-panel-users-users) or [groups](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups) with the `landing_page` [user attribute](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes).

You can assign a specific homepage [to a user](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_individual_users) or [to a group](https://docs.cloud.google.com/looker/docs/admin-panel-users-user-attributes#assigning_values_to_user_groups) by setting the value of the `landing_page` user attribute to a relative URL within Looker. If you want to assign a specific homepage to multiple users, we recommend that you [create a new group](https://docs.cloud.google.com/looker/docs/admin-panel-users-groups#adding_groups) specifically for that homepage option.

> Setting a homepage for a specific group overrides the default homepage for your instance for members of the group. Setting a user-specific homepage also overrides any group homepage settings as well as the default homepage.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
