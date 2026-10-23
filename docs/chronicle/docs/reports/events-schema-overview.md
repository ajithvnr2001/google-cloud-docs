---
url: https://docs.cloud.google.com/chronicle/docs/reports/events-schema-overview/
title: Google SecOps events schema \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:55:29.421530+00:00
---

# Google SecOps events schema  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/events-schema-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps events schema

In BigQuery, the table called _events_ stores UDM event records.

The `hour_time_bucket` field identifies the partition as the hour of day in the `metadata.event_timestamp` UDM field. Values in the _hour_time_bucket_ field are hourly time stamps that take the form: _< YYYY-MM-DD HH:MM:SS UTC>_. Here are examples:

  * 2022-05-20 00:00:00 UTC
  * 2022-05-20 01:00:00 UTC
  * 2022-05-20 02:00:00 UTC
  * 2022-05-20 03:00:00 UTC



For example, the value _2022-05-20 00:00:00 UTC_ labels data with an event_timestamp between 2022-05-20 **00:00:00** UTC and 2022-05-20 **00:59:59** UTC. For more information, see [Query partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).

The amount of time it takes for data to appear in the `events` table depends on the difference between when the device records the event, the `metadata.event_timestamp`, and when that event is ingested to Google Security Operations SIEM, the `metadata.ingested_timestamp`.

The following summarizes the time it takes for data to appear in the `events` table after it is received by Google Security Operations:

  * If the difference is less than two hours, then data appears approximately 2 hours after it is ingested.
  * If the difference is between 2 hours and 24 hours, it may take up to 4 hours for data to appear after it is ingested.
  * If the difference is more than 24 hours, it may take up to 5 days for data to appear after it is ingested.

**Note:** An event is considered a "future event" if its `metadata.event_timestamp` shows a later time than its `metadata.ingested_timestamp`. These events are not processed by the real-time pipeline and they should appear in the `events` table in approximately 3-4 days.



The `events` table schema changes regularly. To view information about the table, including the current schema, see the BigQuery instructions for [getting table information](https://docs.cloud.google.com/bigquery/docs/tables#get_table_information).

To access the `events` schema, do the following:

  1. Open the Google Cloud console, and then select the Google SecOps project ID that your Google SecOps representative provided shared with you.
  2. Select **BigQuery** > **BigQuery Studio** > **datalake** > **events**.

![List of fields in events table in  BigQuery](https://docs.cloud.google.com/static/chronicle/images/reports/bq-events-table.png)

**Figure:`events` table in BigQuery**




## `Events` data model for dashboards

In Google SecOps embedded dashboards, you'll notice the data structure called _UDM Events_. This is a Looker data model created for the `events` table in BigQuery.

The table includes the most commonly used UDM fields. It does not include all UDM fields. If there are missing UDM fields you need to have incorporated into a personalized dashboard, contact your Google SecOps representative.

To view fields in this Explore, perform the following steps:

  1. In the navigation bar, click **Dashboards**.
  2. Create a new dashboard (click **Add > Create New**) or edit an existing dashboard.
  3. Add a Tile.
  4. Select **Visualization** as the type if prompted.
  5. In the list of tables, select **UDM Events**.
  6. Browse the list of fields.

![Field list in Google SecOps dashboards](https://docs.cloud.google.com/static/chronicle/images/reports/events-explore-dashboards.png)

**Figure: Field list in Google SecOps Events data model**




## What's next

  * View a description of each UDM field in the [Unified Data Model field list](https://docs.cloud.google.com/chronicle/docs/reference/udm-field-list).
  * For information about accessing and running queries in BigQuery, see [Run interactive and batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * For information about how to query partitioned tables, see [Query partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).
  * For information about how to connect Looker to BigQuery, see Looker documentation about [connecting to BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery).
  * Information about how to [query partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
