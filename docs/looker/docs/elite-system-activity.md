---
url: https://docs.cloud.google.com/looker/docs/elite-system-activity/
title: Elite System Activity \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:48.733106+00:00
---

# Elite System Activity  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/elite-system-activity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Elite System Activity Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Elite System Activity is a paid feature on Looker (original). [Contact a Google Cloud sales specialist](https://cloud.google.com/contact) to discuss purchasing the Elite System Activity feature.

Elite System Activity is a standard feature on the [**Enterprise** and **Embed** editions](https://docs.cloud.google.com/looker/docs/looker-core-feature-differences) of Looker (Google Cloud core).

## Benefits

Elite System Activity includes an analytical store for System Activity data that provides the following benefits:

  * System Activity Explores and dashboards remain the same, so the process of viewing System Activity data is no different.
  * More System Activity data can be stored. System Activity data can be retained for up to 1 year.
  * System Activity queries are offloaded from the Looker instance, which improves System Activity query performance and may improve Looker's performance. Elite System Activity also removes the concurrent query limit on System Activity Explores and dashboards along with the forced 12-hour caching policy for System Activity Explores and dashboards.

**Note:** This data can be useful for supplementing monitoring and auditing activities, but is not intended to replace your current compliance strategy.**Note:** When Elite System Activity is enabled, System Activity dashboards and Explores will query the analytical store, but legacy `i__looker` Explores won't. If Elite System Activity is enabled, Google Cloud recommends that you update any saved Looks or dashboards that query `i__looker` and cause them to query System Activity instead.

## Refresh intervals

The following tables refresh every 10 minutes:

  * `event`
  * `event_attribute`
  * `history`
  * `merge_query`
  * `pdt_event_log`
  * `query`
  * `query_api_client_context`
  * `query_metrics`
  * `sql_text`



The `user` table refreshes once an hour.

The following tables refresh every 24 hours:

  * `access_token`
  * `api_usage`
  * `compliance_user_permissions`
  * `content_metadata`
  * `content_usage`
  * `dashboard`
  * `dashboard_element`
  * `dashboard_layout`
  * `dashboard_layout_component`
  * `db_connection`
  * `field_usage`
  * `group`
  * `group_group`
  * `group_user`
  * `look`
  * `merge_query_source_query`
  * `model_set`
  * `node`
  * `permission_set`
  * `result_maker`
  * `role`
  * `role_group`
  * `role_user`
  * `scheduled_job`
  * `scheduled_job_stage`
  * `scheduled_plan`
  * `scheduled_plan_destination`
  * `session`
  * `slug`
  * `space`
  * `space_user`
  * `sql_query`
  * `user_attribute`
  * `user_facts`
  * `user_facts_role`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
