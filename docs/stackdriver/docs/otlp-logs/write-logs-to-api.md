---
url: https://docs.cloud.google.com/stackdriver/docs/otlp-logs/write-logs-to-api/
title: Use curl to write OTLP logs to the Telemetry API \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:16:34.422678+00:00
---

# Use curl to write OTLP logs to the Telemetry API  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/otlp-logs/write-logs-to-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Use curl to write OTLP logs to the Telemetry API Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to send OTLP logs directly to the logging endpoint of the [Telemetry (OTLP) API](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview), `telemetry.googleapis.com`, and how to view the ingested log entries in Cloud Logging.

## Before you begin

This section describes how to set up your environment for using the Telemetry API.

### Select or create a Google Cloud project

Choose a Google Cloud project for this example. If you don't already have a Google Cloud project, then create one:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Set up `gcloud`

The `gcloud` tool is part of the Google Cloud CLI. For information about installing it, see [Managing Google Cloud CLI components](https://docs.cloud.google.com/sdk/docs/components). To see the gcloud CLI components you have installed, run the following command:
    
    
    gcloud components list
    

To configure the gcloud CLI for use, run the following commands after replacing the PROJECT_ID variable with the identifier of your Google Cloud project.
    
    
    export GOOGLE_CLOUD_PROJECT=PROJECT_ID
    
    gcloud auth login
    gcloud config set project PROJECT_ID
    

### Enable APIs

Enable the Cloud Logging API and the Telemetry API in your Google Cloud project. **Pay particular attention to the Telemetry API,`telemetry.googleapis.com`**; this document might be the first time you've encountered this API.

If the APIs appear in the output of the following command, then they are already enabled:
    
    
    gcloud services list
    

If either of the APIs is not enabled, run the corresponding command:
    
    
    gcloud services enable logging.googleapis.com
    gcloud services enable telemetry.googleapis.com
    

### Get permission to write logs

To get the permissions that you need to write logs to the Telemetry API and view the created log entries, ask your administrator to grant you the following IAM roles: 

  * [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) on your project
  * [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) on your project
  * [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) on your quota project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To learn how to configure a quota project, see [Set the quota project](https://docs.cloud.google.com/docs/quotas/set-quota-project).

## Write OTLP logs by using the Telemetry API

This section describes how to create an OTLP-formatted log record and send the record to the Telemetry API by using the `curl` utility.

### Create an OTLP log

Create a JSON file containing an OTLP-formatted log record. The following tabs contain a very simple log record and a more complex, multi-log record. You can choose one or the other, or send each in succession.

###  Simple OTLP log 
    
    
    {
      "resourceLogs": [
        {
          "resource": {
            "attributes": [
              {"key": "gcp.project_id", "value": {"stringValue": "PROJECT_ID"}},
              {"key": "cloud.platform", "value": {"stringValue": "gcp_compute_engine"}},
              {"key": "zone", "value": {"stringValue": "us-central1"}},
              {"key": "instance_id", "value": {"stringValue": "12345"}},
            ]
          },
          "scopeLogs": [
          {
            "logRecords": [
              { "eventName": "otlp-test-log",
                "body": { "stringValue": "This is a trivial log message." },
              }
            ]
          }
          ]
        }
      ]
    }
    

###  More complex OTLP log 
    
    
    {
      "resourceLogs": [
        {
          "resource": {
            "attributes": [
              {"key": "gcp.project_id", "value": {"stringValue": "PROJECT_ID"}},
              {"key": "cloud.platform", "value": {"stringValue": "gcp_compute_engine"}},
              {"key": "zone", "value": {"stringValue": "us-central1"}},
              {"key": "instance_id", "value": {"stringValue": "12345"}},
            ]
          },
          "scopeLogs": [
          {
            "logRecords": [
              { "eventName": "otlp-test-log",
                "severityText": "INFO",
                "body": { "stringValue": "This is an informational message." },
                "attributes": [
                  {"key": "string.attribute",
                   "value": { "stringValue": "Here's some general info."}},
                  {"key": "int.attribute",
                   "value": { "intValue": "666"}},
                  {"key": "double.attribute",
                   "value": { "doubleValue": "3.14159"}},
                  {"key": "boolean.attribute",
                   "value": { "boolValue": true}},
                ]
              },
              { "eventName": "otlp-test-log",
                "severityText": "DEBUG",
                "body": { "stringValue": "This is a debug message." },
                "attributes": [
                  {"key": "string.attribute",
                   "value": { "stringValue": "Here's some debug info."}},
                  {"key": "int.attribute",
                   "value": { "intValue": "42"}},
                  {"key": "double.attribute",
                   "value": { "doubleValue": "6373.392"}},
                  {"key": "boolean.attribute",
                   "value": { "boolValue": false}},
                 ]
              }
            ]
          }
          ]
        }
      ]
    }
    

Copy the JSON content from either tab into a file and save the file.

Both of these JSON examples result in Cloud Logging log entries that are written against the [`gce_instance`](https://docs.cloud.google.com/logging/docs/api/v2/resource-list#tag_gce_instance) monitored-resource type. Each `logRecord` item in the `scopeLogs` array becomes a separate Cloud Logging log entry in a log named for the value of the `eventName` field in the OTLP log record. For more information about how OTLP logs are mapped to Logging log entries, see the following:

  * [OTLP log record to log entry mapping](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/otlp-log-record-to-log-entry)
  * [OTLP attributes to resource-type mapping](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/otlp-attribute-to-logging-resource)



### Send the log to the Telemetry API

After replacing the OTLP_LOG_JSON_FILE variable with the name of the file you created, use the following `curl` command to post the contents of the file to the logging endpoint of the Telemetry API, `https://telemetry.googleapis.com/v1/logs`:
    
    
    curl -i -X POST -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Content-Type: application/json" -H "X-Goog-User-Project: ${PROJECT_ID}" \
    -d @OTLP_LOG_JSON_FILE \
    "https://telemetry.googleapis.com/v1/logs"
    

If you create multiple files of JSON log records, then be sure to change the OTLP_LOG_JSON_FILE variable in the `curl` command.

The `curl` command produces a sequence of messages, and if successful, an empty response (`{}`). The output looks similar to the following:
    
    
    HTTP/2 200
    x-google-esf-cloud-client-params: backend_service_name: "telemetry.googleapis.com" backend_fully_qualified_method: "opentelemetry.proto.collector.logs.v1.LogsService.Export"
    [...]
    x-google-gfe-response-code-details-trace: response_code_set_by_backend
    x-google-gfe-response-body-transformations: gunzipped,chunked
    x-google-shellfish-status: CA0gBEBG
    x-google-gfe-version: 2.970.1
    alt-svc: h3=":443"; ma=2592000,h3-29=":443"; ma=2592000
    accept-ranges: none
    
    {}
    

## View ingested OTLP logs

You can view the log entries that result from your OTLP logs by using any of the Cloud Logging tools, including Logs Explorer and Observability Analytics. The following sections describe how to view log entries by using the following:

  * The gcloud CLI
  * Logs Explorer



### Use `gcloud` to view logs

You can retrieve log entries you just created by using the [`gcloud logging read`](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read) command. The following command restricts the output to the log entries in the `otlp-test-log` log that were written in the last five minutes:
    
    
    gcloud logging read "LOG_ID(otlp-test-log)" --freshness=5m --format=json
    

The log entries that correspond to the sample OTLP logs look like the following:

###  Simple log entry 
    
    
    [
      {
        "insertId": "1yt9bu7a0",
        "logName": "projects/PROJECT_ID/logs/otlp-test-log",
        "otel": {
          "resource": {
            "attributes": {
              "cloud.platform": "gcp_compute_engine",
              "gcp.project_id": "PROJECT_ID",
              "instance_id": "12345",
              "zone": "us-central1"
            }
          }
        },
        "receiveTimestamp": "2026-03-18T20:17:00.128801819Z",
        "resource": {
          "labels": {
            "instance_id": "12345",
            "project_id": "PROJECT_ID",
            "zone": "us-central1"
          },
          "type": "gce_instance"
        },
        "textPayload": "This is a trivial log message.",
        "timestamp": "2026-03-18T20:17:00.128801819Z"
      }
    ]
    

###  More complex log entries 
    
    
    [
      {
        "insertId": "1aw7fsja1",
        "labels": {
          "boolean.attribute": "false",
          "double.attribute": "6373.39",
          "int.attribute": "42",
          "string.attribute": "Here's some debug info."
        },
        "logName": "projects/PROJECT_ID/logs/otlp-test-log",
        "otel": {
          "resource": {
            "attributes": {
              "cloud.platform": "gcp_compute_engine",
              "gcp.project_id": "PROJECT_ID",
              "instance_id": "12345",
              "zone": "us-central1"
            }
          }
        },
        "receiveTimestamp": "2026-03-16T17:11:19.461096569Z",
        "resource": {
          "labels": {
            "instance_id": "12345",
            "project_id": "PROJECT_ID",
            "zone": "us-central1"
          },
          "type": "gce_instance"
        },
        "severity": "DEBUG",
        "textPayload": "This is a debug message.",
        "timestamp": "2026-03-16T17:11:19.461096569Z"
      },
      {
        "insertId": "1aw7fsja0",
        "labels": {
          "boolean.attribute": "true",
          "double.attribute": "3.14159",
          "int.attribute": "666",
          "string.attribute": "Here's some general info."
        },
        "logName": "projects/PROJECT_ID/logs/otlp-test-log",
        "otel": {
          "resource": {
            "attributes": {
              "cloud.platform": "gcp_compute_engine",
              "gcp.project_id": "PROJECT_ID",
              "instance_id": "12345",
              "zone": "us-central1"
            }
          }
        },
        "receiveTimestamp": "2026-03-16T17:11:19.461096569Z",
        "resource": {
          "labels": {
            "instance_id": "12345",
            "project_id": "PROJECT_ID",
            "zone": "us-central1"
          },
          "type": "gce_instance"
        },
        "severity": "INFO",
        "textPayload": "This is an informational message.",
        "timestamp": "2026-03-16T17:11:19.461096569Z"
      }
    ]
    

### Use Logs Explorer to view logs

To view the log entries created from your OTLP logs in the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. Select the Google Cloud project to which you sent your OTLP logs.
  3. Use the **Query** pane to enter a query. The samples in this document are written to a log named `otlp-test-log`. To search for entries in this log, enter the following query:
         
         LOG_ID(otlp-test-log)
         

  4. Click **Run query**.




## Clean up

If you created a new project and no longer need it, then you can [delete the project](https://console.cloud.google.com/cloud-resource-manager) to avoid incurring charges to your Google Cloud account.

## What's next

To learn more about the Telemetry API, see the following documents:

  * [API overview](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/overview) describes the Telemetry API for logs, metrics, and traces.
  * [v1.logs](https://docs.cloud.google.com/stackdriver/docs/reference/telemetry/v1.logs) describes the Telemetry API endpoint for logging, and provides detailed information about how OTLP log records are ingested as Cloud Logging log entries.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
