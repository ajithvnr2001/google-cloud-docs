---
url: https://docs.cloud.google.com/eventarc/docs/determining-filters-cal/
title: Determine event filters for Cloud Audit Logs \u00a0|\u00a0 Eventarc Standard \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:02:04.160794+00:00
---

# Determine event filters for Cloud Audit Logs  |  Eventarc Standard  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/docs/determining-filters-cal/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/standard/docs/overview)



Send feedback 

#  Determine event filters for Cloud Audit Logs Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

An Eventarc trigger declares your interest in a certain event or set of events, allowing you to capture and act on specific events. Eventarc triggers with `type=google.cloud.audit.log.v1.written` send requests to a destination when an audit log is created that matches the trigger's filter criteria. Matches are made on the following values from the audit log entry:

  * `serviceName`: the service that wrote the audit log
  * `methodName`: the operation that is being audited
  * `resourceName`: the resource that is being audited



For a list of Google Cloud services that provide audit logs, see [Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services). You can also retrieve the event filter values that apply to the `google.cloud.audit.log.v1.written` event type.

## Identify event filters

To identify the exact event filters needed to create a trigger, generate the event that you want to capture, and then view its corresponding Cloud Audit Logs entry. Note that data from a log entry might be split and distributed across several entries.

  1. Ensure that you have enabled the data access audit log types for your service.

[Go to Audit Logs](https://console.cloud.google.com/iam-admin/audit)

Note that any services that have auditing enabled by default are not listed.

     1. In the main table on the **Audit Logs** page, select a Google Cloud service.

     2. In the **Log Types** tab, select the **Admin Read** , **Data Read** , and **Data Write** checkboxes and then click **Save**.

  2. Perform the operation you want to create an event filter for and generate an audit log entry. For example, store a file in a Cloud Storage bucket.

  3. In the Google Cloud console, go to the **Logs Explorer**.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  4. In the **Query builder** pane, build and run a query to filter the log entries and retrieve the results. For example:
         
         resource.type="gcs_bucket" resource.labels.bucket_name="eventarc-bucket"
         

For more details on how to build queries to retrieve and refine logs, see [Build queries by using the Logging query language](https://docs.cloud.google.com/logging/docs/view/building-queries).

  5. To see the full details of one log entry, click the expander arrow (▸) at the start of the entry.

The `protoPayload` field distinguishes an audit log entry from other log entries. In the following example, some parts of the log entry are omitted, and some fields are highlighted: 
         
         {
            **pro toPayload**:{
               **@ type:"type.googleapis.com/google.cloud.audit.AuditLog"**,
               status:{},
               authenticationInfo:{},
               requestMetadata:{},
               **serviceName :"storage.googleapis.com"**,
               **me thodName:"storage.objects.create"**,
               authorizationInfo:[],
               **resourceName :"projects/_/buckets/eventarc-bucket/objects/random.txt"**,
               resourceLocation:{}
            },
            insertId:"il9evleafpdk",
            resource:{
               type:"gcs_bucket",
               labels:{
                  project_id:"cloud-run-test",
                  location:"us-central1",
                  bucket_name:"eventarc-bucket"
               }
            },
            timestamp:"2021-03-05T15:55:20.754688805Z",
            severity:"INFO",
            **logName :"projects/cloud-run-test/logs/cloudaudit.googleapis.com%2Fdata_access"**,
            receiveTimestamp:"2021-03-05T15:55:20.884984611Z"
         }

     * The following information can be used to verify the contents of this audit log entry:

       * The `protoPayload.@type` field is `type.googleapis.com/google.cloud.audit.AuditLog`.

       * The `logName` field includes the domain `cloudaudit.googleapis.com`.

     * The `protoPayload.serviceName` field is the service that wrote the audit log.

     * The `protoPayload.methodName` field is the operation that is being audited.

     * The `protoPayload.resourceName` field is the resource that is being audited.

For more details on how to find information in an audit log entry, see [Understanding audit logs](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs).




## Retrieve event filter values

You can use the [`gcloud eventarc audit-logs-provider`](https://docs.cloud.google.com/sdk/gcloud/reference/eventarc/audit-logs-provider) command to explore and list provider `serviceName` and `methodName` values for the `google.cloud.audit.log.v1.written` event type.

**Note:** The `gcloud eventarc audit-logs-provider` command no longer retrieves the latest provider `serviceName` and `methodName` values. We recommend that you identify the event filter needed to create an Eventarc trigger. Or, for the list of Google Cloud services that provide audit logs, see [Google Cloud services with audit logs](https://docs.cloud.google.com/logging/docs/audit/services). 

To list service names, run the following command:
    
    
    gcloud eventarc audit-logs-provider service-names list

This returns all `serviceName` attribute values for the `google.cloud.audit.log.v1.written` event type.

To list method names for a specific service, run the following command:
    
    
    gcloud eventarc audit-logs-provider method-names list \
         --service-name=SERVICE_NAME

Replace `SERVICE_NAME` with a `serviceName` value—for example, `bigquery.googleapis.com`.

## Eventarc trigger examples

**Note:** Eventarc is available in [specific regions](https://docs.cloud.google.com/eventarc/docs/locations) and in the global region for Cloud Audit Logs triggers. Eventarc is not available in dual-region and multi-region locations. If you specify the global location, you will receive events from all locations for which the event filters match. For example, by creating a global Eventarc trigger, you can receive events from resources such as Cloud Storage buckets in the EU and US multi-regions. For more information, see [Understand Eventarc locations](https://docs.cloud.google.com/eventarc/docs/understand-locations).

The following example creates a trigger called `cal-workflows-trigger` for a Workflows destination. The trigger filters for audit logs that are written by `bigquery.googleapis.com` and for the operation identified as `google.cloud.bigquery.v2.JobService.InsertJob`:
    
    
    gcloud eventarc triggers create cal-workflows-trigger \
       --location=us-central1 \
       --destination-workflow=my-workflow \
       --destination-workflow-location=europe-west4 \
       --event-filters="type=google.cloud.audit.log.v1.written" \
       --event-filters="serviceName=bigquery.googleapis.com" \
       --event-filters="methodName=google.cloud.bigquery.v2.JobService.InsertJob" \
       --service-account=${TRIGGER_SA}@${PROJECT_ID}.iam.gserviceaccount.com

The following example creates a trigger called `cal-run-trigger` for a Cloud Run destination. The trigger filters for audit logs that are written by `workflows.googleapis.com` and for the operation identified as `google.cloud.workflows.v1.Workflows.GetWorkflow`:
    
    
    gcloud eventarc triggers create cal-run-trigger \
       --location=us-central1 \
       --destination-run-service=helloworld-events \
       --destination-run-region=us-central1 \
       --event-filters="type=google.cloud.audit.log.v1.written" \
       --event-filters="serviceName=workflows.googleapis.com" \
       --event-filters="methodName=google.cloud.workflows.v1.Workflows.GetWorkflow" \
       --event-filters="resourceName=projects/_/locations/us-central1/workflows/test-workflow" \
       --service-account=${PROJECT_NUMBER}-compute@developer.gserviceaccount.com

## Oversized audit log entries

Cloud Logging splits audit log entries that are larger than [the usage limit](https://docs.cloud.google.com/logging/quotas#log-limits) and distributes the data contained in the original audit log entry across several _split_ entries. If a log entry contains a `split` field, then the entry is the result of splitting a larger original log entry. The `split` field is a `LogSplit` object that contains the information needed to identify related split entries.

Each split entry has a `protoPayload` that includes the same `serviceName`, `methodName`, and `resourceName` values to help filter the Cloud Audit Logs events. Eventarc triggers deliver an event for each split entry.

When you have an audit log entry that is split into multiple log entries, you can filter for any of the fields in the `LogEntry`. For example, if you need the first entry in a series of split log entries, you can run the following gcloud CLI command, using `split.index=0` to indicate the position of the first entry:
    
    
    gcloud logging read "split.index=0"

For more information, including how to recognize entries and sample queries, see [Split audit log entries](https://docs.cloud.google.com/logging/docs/audit/split-logs).

## What's next

  * [Learn how to create a trigger](https://docs.cloud.google.com/eventarc/standard/docs/event-providers-targets#triggers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
