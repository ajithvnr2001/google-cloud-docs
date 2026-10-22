---
url: https://docs.cloud.google.com/looker/docs/content-certification/
title: Content certification \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:38.025887+00:00
---

# Content certification  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/content-certification/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Content certification Stay organized with collections  Save and categorize content based on your preferences. 

Content certification lets trusted users certify Looker [dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards), [Looks](https://docs.cloud.google.com/looker/docs/viewing-looks), [Explores](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores), [LookML dashboards](https://docs.cloud.google.com/looker/docs/building-lookml-dashboards), and [self-service Explores](https://docs.cloud.google.com/looker/docs/exploring-self-service) to indicate that the content has gone through a manual review and is certified as reliable and trustworthy. This lets other users identify reliable content and confidently use that data for decision-making.

## Enabling content certification

A Looker admin can enable or disable content certification by using the **Content Certification** field on the **Settings** page in the **General** section of Looker's admin panel. Content certification is enabled by default.

## Identifying certified content

When content certification is enabled, Looker maintains three trust levels for dashboards, LookML dashboards, Looks, and self-service Explores. These trust levels are indicated by badges, and are as follows:

  * Ungoverned (untrusted): Indicated with an "ungoverned" warning badge ![](https://docs.cloud.google.com/static/looker/docs/images/uncertified-content-badge-2604.png). This trust level is the default for self-service Explores, Looks that are based on self-service Explores, and dashboards or LookML dashboards that include tiles that are built on or more self-service Explores. You can hover over the yellow badge to view the name of the source file of the self-serve Explore. Once the content is certified, the "ungoverned" warning badge is removed, signifying the content's trusted status.

  * Empty state (standard): This content doesn't display a badge. This is the default for uncertified dashboards, LookML dashboards, Looks, and Explores that are built on standard LookML Explores.

  * Certified (highly trusted): Indicated with a "Certified" badge ![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-badge-2604.png). This badge indicates that the content has undergone manual review and certification. You can hover over the green badge to see certification metadata, including the certifier's name, the certification date and time, and any notes that were saved by the certifier. For example:

![](https://docs.cloud.google.com/static/looker/docs/images/certified-dashboard-details-2604.png)




The following table summarizes the trust signals:

| Indicator | After certification (highly trusted)  
---|---|---  
**Governed data** (dashboards, LookML dashboards, Explores, and Looks that are based on LookML models) | No badge | ![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-badge-2604.png)  
**Ungoverned data** (self-service Explores, Looks that are based on self-service Explores, and dashboards and LookML dashboards that have tiles based on self-service Explores) | ![](https://docs.cloud.google.com/static/looker/docs/images/uncertified-content-badge-2604.png) | ![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-badge-2604.png)  
  
Badges are displayed in the following places:

  * Next to content titles on tiles on the Looker home page:

![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-tiles-2604.png)

  * Next to content titles on content lists in folder views:

![](https://docs.cloud.google.com/static/looker/docs/images/certified-content-lists-2604.png)

  * Next to content titles on search results.

  * For Explores and self-service Explores, next to the Explore title in the Explore list:

![](https://docs.cloud.google.com/static/looker/docs/images/certified-explores-2604.png)

  * When a dashboard, a LookML dashboard, a Look, an Explore, or a self-service Explore is being viewed, next to the content title.

  * For dashboards or LookML dashboards that have tiles based on self-service Explores, if the underlying self-service Explores have not been certified, you will see the Ungoverned data badge next to both the dashboard title and the titles of any tiles that are based on the uncertified self-service Explores. Once the underlying self-service Explores are certified, the Ungoverned data badge will be removed.

  * For Looks based on a self-service Explore, if the underlying self-service Explore has not been certified, you will see the Ungoverned data badge next to the Look title. Once the underlying self-service Explore is certified, the Ungoverned data badge will be removed.

  * In the details panel for dashboards, LookML dashboards, and Looks, you can view certification metadata, including the certifier's name, the certification date and time, and any notes that were saved by the certifier.


**Note:** Starting in Looker 26.4, certification badges are not displayed on [signed embedded](https://docs.cloud.google.com/looker/docs/signed-embedding) content.

## Certifying content

Before certifying content, consider reviewing it for accuracy, consistency, and adherence to your organization's data governance standards. Certified content should be reliable and well-documented, so that other users can understand and trust the certified content.

This section contains the following information:

  * Requirements for content certification
  * How to request content certification
  * How to certify content
  * How certification can be revoked



### Requirements for content certification

To be able to certify content, you must be a Looker admin or have the [`certify_content` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#certify_content).

### Requesting content certification

If you don't have the permission to certify content, contact a user in your organization who has the permission to certify content and request that they certify your content for you.

If your Looker admin has entered a custom URL in the [**Certification Process URL** field](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#certification_process_url), next to the **Want to get this content certified?** menu option, click **Learn how**. This will open up the page at the custom URL.

You can find the **Learn how** link on a dashboard's or LookML dashboard's [three-dot dashboard menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu), or a Look, Explore, or self-service Explore's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu).

### Certifying a dashboard, Look, or self-service Explore

If you have the permission to certify content, you can certify content in the following ways, depending on the type of content:

  * To certify a dashboard or LookML dashboard, from the dashboard's [three-dot dashboard menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu), select **Certify**.
  * To certify a Look, from the Look's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu), select **Certify**.
  * To certify an Explore or a self-service Explore, from the [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-and-interacting-with-explores#the_explore_actions_gear_menu), select **Certify**.



After you select **Certify** , Looker displays the **Certify this content?** dialog:

![](https://docs.cloud.google.com/static/looker/docs/images/certify-content-dialog-2520.png)

Enter any notes about the content in the **Notes** field, and click **Certify**. Notes will be visible when a user hovers over the green certified badge, and from the dashboard, LookML dashboard, and Look details panels.

### Revoking certification

If the [**Revoke Certification on Edit** option](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#revoke_certification_on_edit) is enabled, the "Certified" status will be automatically revoked if a user makes significant edits to the content. A warning will be displayed to the user before they save their changes.

Minor edits that won't revoke certification status include the following:

  * Moving or resizing a dashboard tile
  * Dashboard [quick layout](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards#quick_layout) changes
  * Marking a dashboard or Look as a [favorite](https://docs.cloud.google.com/looker/docs/finding-content#marking_content_as_a_favorite)
  * Adding the dashboard or Look to a [board](https://docs.cloud.google.com/looker/docs/presenting-content#adding_content_to_a_board)
  * Updating the name, description, or notes of a dashboard or dashboard tile
  * Updating the name or description of a Look
  * Updating the title of a self-service Explore
  * Changing the [**Public Access** setting](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls#enabling_public_access_for_a_specific_look) of a Look



Major edits that will revoke certification status include the following:

  * Changing the query or dashboard tile content
  * Adding, duplicating, or removing a dashboard tile or visualization element
  * Changing filter values
  * Adding a dimension or measure to an Explore
  * Changing the [**Run on Load** setting](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks#turning_off_automatic_run_on_load) of a Look



A certifier can also revoke certification from content by selecting **Remove Certification** from a dashboard's or LookML dashboard's [three-dot dashboard menu](https://docs.cloud.google.com/looker/docs/viewing-dashboards#three-dot_dashboard_menu), a Look's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu), or a self-service Explore's [Explore actions gear menu](https://docs.cloud.google.com/looker/docs/viewing-looks#the_look_explore_actions_gear_menu).

### Viewing certification activity

Looker admins can use the [System Activity Event Attributes Explore](https://docs.cloud.google.com/looker/docs/usage-reports-with-system-activity-explores#event_attribute) to view content certification activity. If the certification status of any content changes, an event is generated.

The following events indicate the certification status of a piece of content has changed. Each event also shows the new content certification status, the content ID, and any notes included with the certification status change:

  * `update_dashboard_certification`: Indicates the certification status of a UDD dashboard has changed.
  * `update_look_certification`: Indicates the certification status of a Look has changed.
  * `update_lookml_certification`: Indicates the certification status of a LookML dashboard has changed.
  * `update_lookml_explore_certification`: Indicates the certification status of a LookML Explore has changed.
  * `auto_remove_certification`: Indicates the certification status of a piece of content has been automatically revoked.



For self-service Explores, when certification status is changed, the `activity_non_query` event is generated, and the `category` attribute indicates whether the self-service Explore was certified or uncertified.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
