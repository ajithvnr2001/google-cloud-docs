---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-upgrade-dashboard-experience-for-looker-users/
title: Upgrading the default dashboard experience for all Looker users \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:33.139403+00:00
---

# Upgrading the default dashboard experience for all Looker users  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-upgrade-dashboard-experience-for-looker-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Upgrading the default dashboard experience for all Looker users Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Visit the [Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023)](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page to learn about legacy dashboard deprecation in November 2022 (Looker 22.20) and removal in April 2023 (Looker 23.6). **The following page is intended for customers on Looker 22.18 or earlier.**

In Looker 21.20, Looker upgraded the default dashboard experience for all users to the [new dashboard experience](https://docs.cloud.google.com/looker/docs/viewing-dashboards). As part of that effort, we introduced a change to dashboard and legacy dashboard URL routing: 

**Dashboard type** |  **URLs in Looker 21.18 and earlier** |  **URLs in Looker 21.20 and later**  
---|---|---  
[Dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards) (i.e., the new dashboard experience)  |  https://instance.looker.com/**dashboards-next** /1  |  https://instance.looker.com/**dashboards** /1   
[Legacy dashboards](https://docs.cloud.google.com/looker/docs/viewing-legacy-dashboards) |  https://instance.looker.com/**dashboards** /1  |  https://instance.looker.com/**dashboards-legacy** /1   
  
This change does not break any links or bookmarks to dashboards. 

Any links or bookmarks that use `/dashboards-next/` now automatically redirect to `dashboards/`. Any links or bookmarks to `/dashboards/` now redirect to the new dashboard experience, as opposed to legacy dashboards. 

When you are navigating within Looker, any dashboards that have not been reverted to legacy dashboards will now default to the new dashboard experience. 

##  For customers who adopted Looker _on or after_ Looker 7.18 (October 2020) 

For user-defined dashboards, your instance already defaults to the new dashboard experience, and dashboards will continue to appear as your users have created them. Any dashboards that were legacy dashboards before Looker 21.20 will remain legacy dashboards after Looker 21.20. 

For LookML dashboards and dashboards that were created with the API, if the dashboards have no `preferred_viewer` parameter set, they will be upgraded to the new dashboard experience. To keep them as legacy dashboards, set the `preferred_viewer` parameter to `dashboards`. 

Embedded dashboards will also be upgraded to the new dashboard experience. To keep them as legacy dashboards, update their URLs to contain `/embed/dashboards-legacy/`. 

##  For customers who adopted Looker _before_ Looker 7.18 (October 2020) 

> _Note: The[Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023) ](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page contains updated information about Looker dashboard behavior upon update to Looker 22.20 and 23.6. _

As of Looker 21.20, dashboards on your instance will default to the new dashboard experience, unless they have been reverted to legacy dashboards. 

Any dashboards that use the following configurations will continue to appear as legacy dashboards: 

  * User-defined dashboards that have been [reverted](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reverting_a_dashboard_permanently_with_the_dashboard_menu) to legacy dashboards 
  * LookML dashboards that have a `[preferred_viewer](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard#preferred_viewer)` parameter set to `dashboards`
  * Dashboards created with the API that have a `[preferred_viewer](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/create_dashboard)` parameter set to `dashboards`



Any dashboards that use the following configurations will be upgraded from legacy dashboards to dashboards: 

  * User-defined dashboards that have not been reverted to legacy dashboards 
  * LookML dashboards with newspaper layout that have no `preferred_viewer` parameter set 
  * Dashboards that were created through the API and that have no `preferred_viewer` parameter set 
  * Embedded dashboards that use `/embed/dashboards/` [in their URLs](https://docs.cloud.google.com/looker/docs/private-embedding#embedding_a_dashboard)



If you want to keep particular dashboards as legacy dashboards after Looker 21.20, see the **If you want to continue using legacy dashboards** section on this page. 

If you want to postpone the change to URL routing entirely, see the **Postponing the change to dashboard URL routing** section on this page. 

## If you want to continue using legacy dashboards

> _Note: As of Looker 22.20, the**Use old dashboard routes** and **Revert to legacy dashboards** legacy features have been removed. Use the **Can use Legacy Dashboards** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) to continue to use legacy dashboards until you upgrade to Looker 23.6. See the [Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023) ](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page for more information. _

Looker plans to fully deprecate legacy dashboards in November 2022 and to remove them entirely in April 2023. Currently, we are incorporating customer feedback and adding new features to the new dashboard experience. During the transition, you can choose to continue viewing legacy dashboards. 

To continue viewing legacy dashboards, there are several methods, depending on the type of dashboard. 

### Reverting user-defined dashboards to legacy dashboards

If you have individual user-defined dashboards that you want to keep as legacy dashboards after 21.20, you can revert them. 

To revert dashboards to legacy dashboards:

  1. Make sure the **Revert to Legacy Dashboards**[legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) is enabled. 
  2. Follow the steps outlined on the [Viewing dashboards](https://docs.cloud.google.com/looker/docs/viewing-dashboards#reverting_a_dashboard_permanently_with_the_dashboard_menu) documentation page. 



The dashboard then defaults to a legacy dashboard within Looker and through external links using `dashboards-legacy/`. 

To temporarily revert a dashboard to a legacy dashboard while you're viewing it, replace `dashboards/` in the URL with `dashboards-legacy/`. **Revert to Legacy Dashboards** does not need to be enabled. This change will not be saved to the dashboard; if you navigate to the dashboard within Looker, it will default to the new dashboard experience. 

###  Reverting LookML and API-created dashboards to legacy dashboards 

If the `preferred_viewer` parameter is undefined, as of Looker 21.20, the dashboard will appear in the new dashboard experience. 

For LookML dashboards and dashboards that were created with the API, setting a dashboard's `preferred_viewer` parameter to `dashboards` reverts the dashboard to a legacy dashboard. 

For more information about the `preferred_viewer` parameter, visit the [Dashboard parameters](https://docs.cloud.google.com/looker/docs/reference/param-lookml-dashboard) documentation page or the [Create Dashboard](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/create_dashboard) and [Update Dashboard](https://docs.cloud.google.com/looker/docs/reference/looker-api/latest/methods/Dashboard/update_dashboard) API documentation. 

###  Reverting links, bookmarks, and embedded dashboards to legacy dashboards 

To revert links, bookmarks, and embedded dashboards to legacy dashboards, update your links to use `dashboards-legacy/` instead of `dashboards/`. 

For more information about embedded dashboard links, visit the [Private embedding](https://docs.cloud.google.com/looker/docs/private-embedding#embedding_a_dashboard) and [Signed embedding](https://docs.cloud.google.com/looker/docs/single-sign-on-embedding) documentation pages. 

### Postponing the change to dashboard URL routing

> _Note: As of Looker 22.20, the**Use old dashboard routes** Labs feature has been removed. Use the **Can use Legacy Dashboards** [legacy feature](https://docs.cloud.google.com/looker/docs/legacy-feature-schedule) to continue to use legacy dashboards until you upgrade to Looker 23.6. See the [Removing the legacy dashboard experience - a timeline from Looker 21.20 (November 2021) through Looker 23.6 (April 2023) ](https://docs.cloud.google.com/looker/docs/best-practices/legacy-dashboard-deprecations) Best Practices page for more information. _

To postpone the upgrade from legacy dashboards to dashboards for all dashboards on your instance, enable the **Use old dashboard routes** legacy feature. This legacy feature defaults to enabled in Looker 21.18 defaults to disabled in Looker 21.20 and is removed in Looker 22.20. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
