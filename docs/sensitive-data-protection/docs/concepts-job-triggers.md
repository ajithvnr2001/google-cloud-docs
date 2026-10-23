---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers/
title: Jobs and job triggers \u00a0|\u00a0 Sensitive Data Protection \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:43.675220+00:00
---

# Jobs and job triggers  |  Sensitive Data Protection  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-job-triggers/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Jobs and job triggers Stay organized with collections  Save and categorize content based on your preferences. 

A _job_ is an action that Sensitive Data Protection runs to either scan content for sensitive data or calculate the risk of re-identification. Sensitive Data Protection creates and runs a job resource whenever you tell it to inspect your data.

There are currently two types of Sensitive Data Protection jobs:

  * _Inspection jobs_ inspect your content for sensitive data according to your criteria and generate summary reports of where and what type of sensitive data exists.
  * _Risk analysis jobs_ analyze de-identified data and return metrics about the likelihood that the data can be re-identified.



You can schedule when Sensitive Data Protection runs jobs by creating _job triggers_. A job trigger is an event that automates the creation of Sensitive Data Protection jobs to scan Google Cloud storage repositories, including Cloud Storage buckets, BigQuery tables, and Datastore kinds.

Job triggers enable you to schedule scan jobs by setting intervals at which each trigger goes off. They can be configured to look for new findings since the last scan run to help monitor changes or additions to content, or to generate up-to-date findings reports. Scheduled triggers run on an interval that you set, from 1 day to 60 days.

**Note:** Prematurely canceling an operation midway through a job still incurs costs for the portion of the job that was completed. For more information about billing, see [Sensitive Data Protection pricing](https://cloud.google.com/sensitive-data-protection/pricing).

## When to use job triggers

The following are some common use cases:

  * **Automate recurring compliance scans** : Schedule regular inspection scans across Cloud Storage buckets and BigQuery tables to maintain continuous visibility into newly stored sensitive data.
  * **Optimize inspection costs on dynamic storage** : Configure timespan rules on job triggers to scan only content that was added or modified since the previous scan cycle.
  * **Monitor ongoing data drift in production databases** : Track shifts in sensitive data exposure over time by generating periodic finding summaries for risk posture reviews.
  * **Coordinate with event-driven data pipelines** : Trigger inspection jobs in response to Cloud Storage upload events or automated ETL pipeline milestones.



## Next steps

Find more information about how to create, edit, and run jobs and job triggers in the following topics:

  * [Creating Sensitive Data Protection inspection jobs and job triggers](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)
  * [Measuring re-identification and disclosure risk](https://docs.cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis) (Covers risk analysis jobs.)



In addition, the following quickstart is available:

  * [Quickstart creating a Sensitive Data Protection job trigger](https://docs.cloud.google.com/sensitive-data-protection/docs/quickstart-create-job-trigger)



## The `JobTrigger` object

A job trigger is represented in the DLP API by the [`JobTrigger`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers) object.

### Job trigger configuration fields

Each `JobTrigger` contains several configuration fields, including:

  * The trigger's name and display name, and a description.
  * A collection of [`Trigger`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#trigger) objects, each of which contains a [`Schedule`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#schedule) object, which defines the scan recurrence in seconds.
  * An [`InspectJobConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig) object, which contains the configuration information for the triggered job.
  * A [`Status`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers#status) enumeration, which indicates whether the trigger is currently active.
  * Timestamp fields representing creation, update, and last run times.
  * A collection of [`Error`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/Error) objects, if any were encountered when the trigger was activated.



### Job trigger methods

Each `JobTrigger` object also includes several built-in methods. Using these methods, you can do the following:

  * Create a new job trigger: [`projects.jobTriggers.create`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/create)
  * Update an existing job trigger: [`projects.jobTriggers.patch`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/patch)
  * Delete an existing job trigger: [`projects.jobTriggers.delete`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/delete)
  * Retrieve an existing job trigger, including its configuration and status: [`projects.jobTriggers.get`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/get)
  * List all existing job triggers: [`projects.jobTriggers.list`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.jobTriggers/list)



## Job latency

There are no service level objectives (SLO) guaranteed for jobs and job triggers. Latency is affected by several factors, including the amount of data to scan, the storage repository being scanned, the type and number of infoTypes you are scanning for, the region where the job is processed, and the computing resources available in that region. Therefore, the latency of inspection jobs can't be determined in advance.

To help reduce job latency, you can try the following:

  * If [sampling](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage#sampling) is available for your job or job trigger, enable it.
  * Avoid enabling infoTypes that you don't need. Although the following are useful in certain scenarios, these infoTypes can make requests run much more slowly than requests that don't include them:

    * `PERSON_NAME`
    * `FEMALE_NAME`
    * `MALE_NAME`
    * `FIRST_NAME`
    * `LAST_NAME`
    * `DATE_OF_BIRTH`
    * `LOCATION`
    * `STREET_ADDRESS`
    * `ORGANIZATION_NAME`
  * Always specify infoTypes explicitly. Do not use an empty infoTypes list.

  * If possible, use a different processing region.




If you're still having latency issues with jobs after trying these techniques, consider using [`content.inspect`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/inspect) or [`content.deidentify`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/projects.content/deidentify) requests instead of jobs. These methods are covered under the Service Level Agreement. For more information, see [Sensitive Data Protection Service Level Agreement](https://cloud.google.com/sensitive-data-protection/sla).

## Limit scans to only new content

You can configure your job trigger to automatically set the timespan date for files stored in [Cloud Storage](https://docs.cloud.google.com/storage) or [BigQuery](https://docs.cloud.google.com/bigquery). When you set the [`TimespanConfig`](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest/v2/InspectJobConfig#timespanconfig) object to auto-populate, Sensitive Data Protection only scans data that was added or modified since the trigger last ran:
    
    
    ...
      timespan_config {
            enable_auto_population_of_timespan_config: true
          }
    ...
    

For BigQuery inspection, only rows that are at least three hours old are included in the scan. See the [known issue](https://docs.cloud.google.com/sensitive-data-protection/docs/known-issues#bq-timespan) related to this operation.

## Trigger jobs at file upload

In addition to the support for job triggers—which is built into Sensitive Data Protection—Google Cloud also has a variety of other components that you can use to integrate or trigger Sensitive Data Protection jobs. For example, you can use [Cloud Run functions](https://docs.cloud.google.com/functions) to trigger a Sensitive Data Protection scan every time a file is uploaded to Cloud Storage.

For information about how to set up this operation, see [Automating the classification of data uploaded to Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/automating-classification-of-data-uploaded-to-cloud-storage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
