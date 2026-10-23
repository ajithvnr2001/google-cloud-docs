---
url: https://docs.cloud.google.com/talent-solution/docs/management-tools/
title: Cloud Talent Solution management tools \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:37:09.781012+00:00
---

# Cloud Talent Solution management tools  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/talent-solution/docs/management-tools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Talent Solution ](https://docs.cloud.google.com/talent-solution/docs)
  * [ Resources ](https://docs.cloud.google.com/talent-solution/docs/resources)



Send feedback 

#  Cloud Talent Solution management tools Stay organized with collections  Save and categorize content based on your preferences. 

## Cloud Talent Solution dashboard

The Cloud Talent Solution [dashboard](http://console.cloud.google.com/talent-solution) provides visual data to give you more insight into:

  1. How your job seekers are engaging with Job Search, by showing top queries and locations by domain.
  2. Whether your Job Search is properly configured, by showing inconsistencies in your integration.
  3. Whether your client events are properly configured. The dashboard can show client events that you need to correct or improve.



For more information, see the [dashboard documentation](https://docs.cloud.google.com/talent-solution/job-search/docs/dashboard).

## Client event livestream

Check if Google received the event messages you sent, and confirm that the format of the messages are correct. In the [GCP Console](http://console.cloud.google.com), you can access the [Client event livestream tool](https://console.cloud.google.com/talent-solution/behavioral-livestream). The most recent event messages (up to 50) are listed. View event details by selecting any of the listed events. Check all events with the same `requestId` by clicking the "ALL EVENTS BY REQUESTID" button in the header. You'll see warnings in the detailed view in cases where the `clientEvent` message was sent with incorrect formats. Use filtering options to filter the messages by either the `requestId`, `userId`, or `sessionId`.

If the message doesn't appear in the Client event livestream, check that the `requestId` in the event message is valid. Event messages without a valid `requestId` are discarded by Cloud Talent Solution.

See Troubleshooting `ClientEvent` validation errors for more information about single-event error messages.

## Client event search

Search for all event messages having a specific `requestId`. Similar to Client event livestream, you can verify if Google received your event messages and that these are well-formatted messages for a particular `requestId`. You can also use the filter panel on the right side to filter out, for example, well-formed messages.

See [Troubleshooting`ClientEvent` validation errors](https://docs.cloud.google.com/talent-solution/docs/management-tools#Troubleshooting) for more information on aggregated-event error messages.

## Jobs and companies data

Use the [**Jobs and companies**](https://console.cloud.google.com/job-discovery/) page to:

  * View a summary of jobs and companies counts, broken down by type and category.

  * Search for specific jobs details by name or requisition ID.

  * Export data of jobs, companies, or tenants into a BigQuery dataset.




If you have not yet set up the console, use the instructions in [Before you begin](https://docs.cloud.google.com/talent-solution/job-search/docs/before-you-begin) to get access.

#### View and search for job data

The **Summary** tab on the **Jobs and Companies** page shows aggregated information about job and company counts. 

  * The **Latest Snapshot of Counts** table summarizes counts for open and deleted jobs, and counts for active companies of the previous day. This snapshot updates once a day. 
  * The **Counts Over Time** graph visualizes the job and company counts over an amount of time you select. Use the dropdown filters to select types, tenants, and duration to display. 



The **Job Metadata** tab provides a search tool for specific job details. You can search for up to 10 job names or job requisition IDs to get a table with available metadata for those jobs. If no results are found for a particular job (for example, an incorrect name or ID was entered) the table displays a `NOT_FOUND` result in the table row for that job name or ID. 

#### Export data to BigQuery

You can export data to BigQuery by job, company, or tenant for further troubleshooting.

To grant BigQuery permissions to the CTS service account:

  1. On the [Google Cloud console **IAM** page](https://console.cloud.google.com/iam-admin/iam), add a new principal assigning the role **BigQuery Job User** to `gjobs-bq-prod@system.gserviceaccount.com`.

See [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) for more about granting roles on BigQuery.

  2. In [**BigQuery**](https://console.cloud.google.com/bigquery), [create a new BigQuery dataset](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset) with a unique name.

You will use this dataset for exported CTS data.

  3. In the **Explorer** pane, find the dataset you will export CTS data to. Click **Share** and give access to the `gjobs-bq-prod@system.gserviceaccount.com` **BigQuery Data Editor**.

See [Granting access to a dataset](https://docs.cloud.google.com/bigquery/docs/dataset-access-controls#granting_access_to_a_dataset) in the BigQuery documentation for more information.




To export your data from CTS:

  1. In the in the CTS console, go to the **Exports** tab of the **Jobs and companies** page.

  2. Under **Generate BigQuery Export** , select whether to export job, company, or tenant data.

  3. Select an existing BigQuery table to export data to.

  4. Click **Generate** to export the data.

The **Data export** tab displays the export job in progress, and displays a link to the exported dataset in BigQuery when the data is generated.




## Service account management

You must connect a service account to Cloud Talent Solution in order to use the credentials associated with that account and to make an API request. Use the [Service accounts connections tool](https://console.cloud.google.com/talent-solution/service-account-connections) to manage your service accounts. All service accounts associated with your Google Cloud project are listed. Click "Connect" to associate a service account with Cloud Talent Solution. Learn more about service accounts at [Creating and Managing Service Accounts](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts).

## Troubleshooting `ClientEvent` validation errors

### Validations based on a single event

**Constant** | **UI string**  
---|---  
RELATED_JOB_ID_INVALID | The `ClientEvent` message has one or more invalid or incorrect [`relatedJobNames`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#FIELDS.related_job_names)  
EVENT_ID_REUSED | An `eventId` must be unique to a Google Cloud Project. In this case, the message has an `eventId` previously generated by your Google Cloud Project. Best practice is to include some form of timestamp into each `eventId`, to ensure uniqueness.  
MISSING_REQUIRED_FIELDS | Missing required field(s). Check the [`ClientEvent`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event) schema to identify the missing required field(s).  
INVALID_FIELDS | One or more fields of the message were either incomplete or were not expected by Cloud Talent Solution. See the [`ClientEvent`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.ClientEvent) schema for more information on required fields, and the values expected in those fields.  
UNKNOWN_FIELDS | Received unknown field(s)  
INVALID_FORMAT | Received an invalid JSON string in the Cloud Talent Solution `ClientEvent` message. For example, a missing brace.  
  
### Aggregated validations by requestId

**Constant** | **Description**  
---|---  
NO_SEARCH_IMPRESSION | No [`IMPRESSION`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.IMPRESSION) events  
VIEWS_FEWER_THAN_APPLY_STARTS | The number of `VIEW` events is fewer than the number of [`APPLICATION_START`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_START) events. This could either be because the [`VIEW`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.VIEW) events are not being correctly sent to Cloud Talent Solution, or the Apply button on the UI is being triggered without actually triggering a view. If this is the intended behavior (for example, if the search results page has an apply button that job seekers can click without viewing the job details) then consider using a [`APPLICATION_START_FROM_SERP`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_START_FROM_SERP) event for this use case instead.  
VIEWS_FEWER_THAN_APPLY_REDIRECTS | The number of `VIEW` events is fewer than the number of `APPLICATION_REDIRECT` events. This could be either because the `VIEW` events are not being correctly sent to Cloud Talent Solution, or the Apply button on the UI is being triggered without actually triggering a view. If this is the intended behavior (for example, if the search results page has an apply button that job seekers can click, without viewing the job details) then consider using a [`APPLICATION_REDIRECT_FROM_SERP`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_REDIRECT_FROM_SERP) event for this use case instead.   
APPLY_STARTS_FEWER_THAN_APPLY_FINISHES | This is likely due to a misconfiguration where either the [`APPLICATION_START`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_START) message is not being sent in all instances, or the [`APPLICATION_FINISH`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_FINISH) message is being sent in instances when it shouldn't be sent. Ideally the number of [`APPLICATION_START`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_START) messages should be greater than or equal to the number of [`APPLICATION_FINISH`](https://docs.cloud.google.com/talent-solution/job-search/docs/client-event#client-event.EventType.ENUM_VALUES.client-event.EventType.APPLICATION_FINISH) messages.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
