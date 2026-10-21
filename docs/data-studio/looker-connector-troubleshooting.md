---
url: https://docs.cloud.google.com/data-studio/looker-connector-troubleshooting/
title: Troubleshoot errors from the Looker connector \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:19.583200+00:00
---

# Troubleshoot errors from the Looker connector  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/looker-connector-troubleshooting/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Troubleshoot errors from the Looker connector Stay organized with collections  Save and categorize content based on your preferences. 

This page covers the following topics about the Looker connector in Data Studio:

  * Troubleshooting guidance
  * How to report a problem to the Support team



## Looker connector error messages and suggested resolutions

You may encounter the following errors when using the Looker connector in Data Studio:

Authentication and Authorization  
---  
**Issue description or error message** | **Explanation** | **Suggested resolution**  
Data Studio displays this error message:`No dataset accessCouldn't access the underlying data set due to insufficient permissionsSession has expired or lacks credentials. This includes expired OAuth grants. Try logging in again.` | Your authorization to the Looker instance has expired or was revoked. | Edit your Data Studio data source, and then click **Reconnect**.  
Data Studio displays this error message:`No dataset accessCouldn't access the underlying data set due to insufficient permissionsCouldn't query a specific database table due to lack of permissions` | You don't have sufficient Looker permissions to query the Looker Explore. | Talk to you Looker admin about granting you the appropriate permissions to query the model that underlies the Explore.  
Data Studio displays this error message:`Authorization Required` | You must link your Looker and Data Studio accounts to view Looker data in Data Studio. | Authorize the Looker connector to link any necessary accounts, as described in the [View and interact with Looker data on a Data Studio](https://docs.cloud.google.com/data-studio/view-and-interact-with-looker-data-on-a-report) documentation.  
Charts don't render on a downloaded report | To download a report that's based on one or more Looker Explores, you must have the `download_with_limit` or the `download_without_limit` permission on the underlying LookML model or models that underlie the Explores. | Ask your Looker admin to grant you a role that contains the `download_with_limit` or the `download_without_limit` permission on the LookML models that underlie the report's Explores. These permissions are available only for Data Studio Pro users.  
Charts don't render in the exported file | To view charts on an exported report, you must have the `download_with_limit` or the `download_without_limit` permission on the underlying LookML model or models that underlie the Explores. | Ask your Looker admin to grant you a role that contains the `download_with_limit` or the `download_without_limit` permission on the LookML models that underlie the report's Explores. These permissions are available only for Data Studio Pro users.  
Charts don't render in the scheduled report delivery | To view charts on a scheduled report, you must have the `download_with_limit` or the `download_without_limit` permission on the underlying LookML model or models that underlie the Explores. | If you own the report delivery, you have insufficient Looker permissions to view at least one of the models that are referenced in the delivered report. Ask your Looker admin to grant you a role that contains the `schedule_look_emails` permission on the LookML models that underlie the report's Explores. This permission is available only for Data Studio Pro users.If you are a report recipient and receive this message, notify the sender of the report.  
When you're downloading a report, Data Studio displays this error message:`Due to lack of permissions, some charts using Looker models will not download. Ask your Looker admin to grant permissions.` | To view charts on a downloaded report, you must have a role that contains the `download_with_limit` or the `download_without_limit` permission on the underlying LookML model or models that underlie the Explores. | Ask your Looker admin to grant you a roler that contains the `download_with_limit` or the `download_without_limit` permission on the report's underlying LookML models. These permissions are available only for Data Studio Pro users.  
When you're scheduling a report delivery, Data Studio displays this error message:`Due to lack of permissions, some charts using Looker data will be missing from your scheduled report. Ask your Looker admin to grant permissions.` | To schedule a report deliveries, you must have a role that contains the `schedule_look_emails` permission on the underlying LookML model or models that underlie the Explores. | Ask your Looker admin to grant you a role that contains the `schedule_look_emails` permission on the report's underlying LookML model or models. This permission is available only for Data Studio Pro users.  
On the list of report schedules, Data Studio displays this error message:`Some Looker data may be missing from your report deliveries. Ask your Looker admin to grant permissions to deliver all data in this report.` | To view charts on a scheduled report, you must have a role that contains the `schedule_look_emails` permission on the underlying LookML model or models that underlie the Explores. | Ask your Looker admin to grant you a role that contains the `schedule_look_emails` permission on the report's underlying LookML model or models. This permission is available only for Data Studio Pro users.  
Connectivity  
**Issue description or error message** | **Explanation** | **Suggested resolution**  
Data Studio displays this error message:`Looker connection failed` | Data Studio couldn't connect to the Looker instance that you specified | 

  * Confirm that the Looker instance URL is correct and that there are no trailing spaces.
  * The Looker connector is valid only for [specific configurations and versions](https://docs.cloud.google.com/data-studio/limits-of-the-looker-connector#looker-instance-requirements) of Looker instances.
  * Looker (original) instances that have the **Enable Allowlist** feature enabled may require special setup — [Contact Support](https://cloud.google.com/contact).
  * Confirm that the API Host URL in the Looker instance is configured properly.

  
Data Studio displays an HTTP 400 error | The Looker server couldn't process Data Studio's connection request because it interpreted the request as malformed or invalid. | 

  * Confirm that the [**Data Studio** BI connector](https://docs.cloud.google.com/looker/docs/bi-connectors#looker_studio) is enabled in the Looker instance.
  * Confirm that account linking was successful.

  
A chart from a report that you've already created is broken | Something about the connection to the Looker instance has changed. | 

  * Edit your Data Studio data source, and then click **Reconnect**.
  * Confirm that the Data Studio connector is enabled in the Looker instance.
  * Looker instances that have the **Enable Allowlist** feature enabled may require special setup — [Contact Support](https://cloud.google.com/contact).
  * Confirm that the [API endpoint for the Looker instance](https://docs.cloud.google.com/looker/docs/admin-panel-platform-api#api_host_url) is configured properly.

  
Data configuration  
**Issue description or error message** | **Explanation** | **Suggested resolution**  
Data Studio displays this error message:`Couldn't complete the report queryData Studio couldn't get data from the Explore. Reach out to your admin for more information.` | There may be a mismatch between the data structure that Data Studio expects to receive from your Looker Explore and the data it actually receives. Data Studio can't parse or display the data because it's malformed, incomplete, or structured in an unexpected way. | 

  * In your Data Studio data source, click **Edit connection** , then click **Refresh fields**.
  * Run the same query in the Looker Explore. If the query fails, the issue is within Looker itself and needs to be addressed by a Looker developer.

  
Data Studio displays this error message:`LookML model configuration error` | Data Studio couldn't run the query because a specified LookML model or view either doesn't exist or isn't correctly configured. | Verify that the Looker Explore's underlying LookML is correct, and then retry the query.  
Data Studio displays this error message:`Invalid filter expression` | The syntax, logic, or field references within a filter expression are incorrect. | Check the filter expression, and then retry the query.  
Data Studio displays this error message:`Couldn't complete the report queryA filter is not allowed by the LookML model configuration.` | The filter expression in your query is explicitly restricted by the Looker Explore's underlying LookML. The LookML may include an `always_filter` parameter that requires a field to be filtered, filter suggestions or allowed values that restrict what values you can use for that filter, or forbid filtering on the field altogether. | The LookML is working as intended. If the restriction is preventing you from doing a necessary analysis, reach out to your Looker admin or developer. They may be able to adjust the LookML to accommodate your use case.  
Data Studio displays this error message:`No Explores found` | The model that you selected may not have any Explores associated with it, or you may not have access to its Explores. | Select a different Looker model, or ask your Looker admin to grant you permission to access the LookML model.  
Query configuration  
**Issue description or error message** | **Explanation** | **Suggested resolution**  
Data Studio displays this error message:`Query timed out` | Data Studio successfully sent the query to Looker, but Looker's connection to the data's underlying database (like BigQuery, Redshift, or Snowflake) timed out before the database could finish running the query and send the data back. | If the timeout was caused by an overly complex query, try simplifying the query by applying stricter filters, reducing the number of dimensions and measures in your charts, or, if possible, using more aggregated metrics and fewer raw, granular dimensions.  
Data Studio displays this error message:`Query limit exceeded` | The query result set is too large for Looker to stream incrementally. | Reduce the number of rows and try again, or contact your admin to adjust streaming settings.  
Data Studio displays this error message:`Couldn't complete the report queryData Studio couldn't get data from the Explore. Reach out to your admin for more information.` | The report query may contain grammatical errors (such as unexpected characters), misplaced keywords, or incorrect structure. The query couldn't be parsed by the database or failed to run because of limits or conditions that were set by the admin. | Check the syntax of any fields that you manually entered, and then retry the query.  
Data Studio displays this error message:`Database connection timed outThe connection to the underlying database within Looker timed out before completing the query` | Looker's connection to the data's underlying database (like BigQuery, Redshift, or Snowflake) has timed out. | Try the same query again later in case the query timeout was caused by load on the database.If this error persists, talk to your Looker admin about increasing the database connection timeout limit.  
  
## Report a problem

Report problems with the Looker connector to the [Support team](https://cloud.google.com/contact).

If you're a Data Studio Pro customer and experience problems that are related to Data Studio features other than the Looker connector, contact [Cloud Customer Care](https://docs.cloud.google.com/support).

If you're using the free version of Data Studio, post your question or issue in the [Data Studio Community](https://discuss.google.dev/c/looker/looker-q-a/looker-studio/214).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
