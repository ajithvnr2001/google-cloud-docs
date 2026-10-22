---
url: https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-report/
title: View and interact with Looker data on a Data Studio report \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:51.753385+00:00
---

# View and interact with Looker data on a Data Studio report  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-report/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  View and interact with Looker data on a Data Studio report Stay organized with collections  Save and categorize content based on your preferences. 

Some Looker data sources may require additional authorization before you can view and interact with them. These data sources include those that are created by another Data Studio user or those that are based on BigQuery (if you are not signed in to your BigQuery account on the Looker instance).

An "Authorization Required" message on a Data Studio report chart prompts you to authorize the Looker connector to link any necessary credentials.

## Authorize a Looker data source that was created by another user

Before you can view data from any [Looker data source](https://docs.cloud.google.com/data-studio/connect-to-looker), you must link your Google Account credentials to your account credentials for the Looker instance from which the data source originates. Data source owners typically authorize this linking when they create the data source. If you are trying to view a Looker data source that was created by another user, you must also perform this authorization.

**Warning:** If you don't have a Looker account, a Looker [admin](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#admin) on the connected Looker instance must create one for you. To view data from Looker data sources, you must have at least `access_data` and `clear_cache_refresh` permissions for the model on which the Explore is based. [Learn more about Looker connector permissions](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions).

To authorize the Looker connector to link your accounts, follow these steps:

  1. In the selected chart, click **Authorize now**.
  2. In the Data Studio authorization request dialog, verify the name of the connected Looker instance, and click **AUTHORIZE**.
  3. In the Google authorization dialog, click **Allow and continue**.



You can both link and unlink your Google and Looker accounts on the [Account Linking](https://myaccount.google.com/accountlinking) page in your Google Account profile.

Once your accounts are linked, you can view and interact with data from Looker Explores that you have permission to access.

## Authorize a Looker data source that is based on BigQuery data

Your BigQuery OAuth credentials for a Looker instance are managed in the **OAuth Connection Credentials** section of your [user account settings](https://docs.cloud.google.com/looker/docs/user-account#configuring_oauth_connection_credentials). When you create a data source in Data Studio that is based on a Looker Explore that uses BigQuery data, you must use the same BigQuery credentials in Looker and Data Studio. If you are not logged in with your BigQuery OAuth credentials in the Looker instance, you must authorize Data Studio to use your BigQuery credentials.

You can authorize the Looker connector to use the BigQuery OAuth credentials that you use with Looker, follow these steps:

  1. In the selected chart, click **Authorize now**.
  2. In the Data Studio authorization request dialog, select your Google BigQuery OAuth account.
  3. To consent to your BigQuery data being accessed, click **Allow**.



Once your accounts are linked, you can view and interact with data from Looker Explores that you have permission to access.

## Revoke credentials

If you revoke your credentials, the data source won't be able to connect to Looker data. To view the Looker Explore, you must reconnect the Looker data source or re-authorize any accounts or credentials that you have revoked.

Learn more about how to [set and revoke your data credentials](https://docs.cloud.google.com/data-studio/data-credentials-article).

## Refresh data

When you [refresh your data](https://docs.cloud.google.com/data-studio/manage-data-freshness) in Data Studio, data is also refreshed in Looker as if you had clicked **Clear Cache and Refresh** from the Looker Explore. If you have signed out of any authorized accounts or revoked any credentials, any data sources that require authorization will display an **Authorization Required** message.

## Export data

You can [export data from a chart](https://docs.cloud.google.com/data-studio/export-data-from-a-chart) that is based on Looker data source. Data download limits depend on your Looker permissions on the model on which the chart is based:

  * If you have the [`download_with_limit` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_with_limit), you can download up to 5,000 rows.
  * If you have the [`download_without_limit` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#download_without_limit), you can download up to 75,000 rows.

See the [Overview of Looker connector permissions](https://docs.cloud.google.com/data-studio/overview-of-looker-connector-permissions) for more information about how Looker permissions affect what you can do with Looker data sources in Data Studio.




When you're exporting data, specify the number of rows for your data download in the **Rows to export** field.

If your chart uses a [blended data source](https://docs.cloud.google.com/data-studio/blending-data), and one of the data sources is a [Looker Explore](https://docs.cloud.google.com/data-studio/connect-to-looker), the number of rows in the exported data may differ from the number of rows that are displayed in the chart.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
