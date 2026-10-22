---
url: https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs/
title: Write and view logs \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:57.161565+00:00
---

# Write and view logs  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Write and view logs Stay organized with collections  Save and categorize content based on your preferences. 

Go Java Node.js PHP Python Ruby

This page describes the logs that are available for App Engine apps, and how to write, correlate, and view log entries.

App Engine collects two types of logs:

  * **Request log:** Logs of requests sent to your app. By default, App Engine automatically emits a log entry for each HTTP request an app receives.

  * **App log:** Log entries that are emitted by an App Engine app based on the log entries you write to a supported framework or file.




App Engine automatically sends both the request logs and app logs to the [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) agent.

## Write app logs

App Engine automatically emits logs for requests sent to your app, so there is no need to write request logs. This section covers how to write app logs.

When you write app logs from your App Engine app, the logs are picked up automatically by Cloud Logging, as long as the logs are written using the following methods:

  * Integrate with Cloud Logging
  * Write structured logs with `stdout` and `stderr`



### Integrate with Cloud Logging

You can integrate your App Engine app with Cloud Logging. This approach lets you use all the features offered by Cloud Logging and requires only a few lines of Google-specific code.

You can write logs to Cloud Logging from Python applications by using the standard Python logging handler, or by using the Cloud Logging API client library for Python directly. When you use the standard Python logging handler, you must attach a Cloud Logging handler to the Python root handler. For more information, see [Setting up Cloud Logging for Python](https://docs.cloud.google.com/logging/docs/setup/python). 

**Important:** The Logs Explorer does not display an app log entry that exceeds 16 kilobytes.

### Write structured logs to `stdout` and `stderr`

By default, App Engine uses the Cloud Logging client library to send logs. However, this method doesn't support structured logging. You can only write structured logs using `stdout/stderr`. Additionally, you can also send text strings to `stdout` and `stderr`. By default, the log payload is a text string stored in the `textPayload` field of the log entry. The strings appear as messages in the Logs Explorer, the command line, and the Cloud Logging API, and are associated with the App Engine service and version that emitted them.

To get more value from the logs, you can filter these strings in the Logs Explorer by severity level. To filter these strings, you need to format the strings as [**structured data**](https://docs.cloud.google.com/logging/docs/structured-logging). To do this, you write logs in the form of a single line of serialized JSON. App Engine picks up and parses this serialized JSON line, and places it into the `jsonPayload` field of the log entry instead of `textPayload`.

The following snippets demonstrate writing such structured logs.

**Note:** These snippets were originally written for [Cloud Run](https://docs.cloud.google.com/run/docs/logging#writing_structured_logs). They are equally applicable to App Engine.
    
    
    # Uncomment and populate this variable in your code:
    # PROJECT = 'The project ID of your Cloud Run service';
    
    # Build structured log messages as an object.
    global_log_fields = {}
    
    # Add log correlation to nest all log messages.
    # This is only relevant in HTTP-based contexts, and is ignored elsewhere.
    # (In particular, non-HTTP-based Cloud Functions.)
    request_is_defined = "request" in globals() or "request" in locals()
    if request_is_defined and request:
        trace_header = request.headers.get("X-Cloud-Trace-Context")
    
        if trace_header and PROJECT:
            trace = trace_header.split("/")
            global_log_fields[
                "logging.googleapis.com/trace"
            ] = f"projects/{PROJECT}/traces/{trace[0]}"
    
    # Complete a structured log entry.
    entry = dict(
        severity="NOTICE",
        message="This is the default display field.",
        # Log viewer accesses 'component' as jsonPayload.component'.
        component="arbitrary-property",
        **global_log_fields,
    )
    
    print(json.dumps(entry))

In the App Engine standard environment, writing structured logs to `stdout` and `stderr` don't count against the log ingestion requests per minute quota in the Cloud Logging API. 

### Special JSON fields in messages

When you provide a structured log as a JSON dictionary, some special fields are stripped from the `jsonPayload` and are written to the corresponding field in the generated [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) as described in the documentation for [special fields](https://docs.cloud.google.com/logging/docs/agent/configuration#special-fields).

For example, if your JSON includes a `severity` property, it is removed from the `jsonPayload` and appears instead as the log entry's `severity`. The `message` property is used as the main display text of the log entry if present.

### Correlate request logs with app logs

After you've formatted the entries as a JSON object and provided specific metadata, you can enable filtering and correlation with request logs. To correlate the request log entries with the app log entries, you need the request's trace identifier. Follow the instructions to correlate log messages:

  1. Extract the trace identifier from the `X-Cloud-Trace-Context` request header.
  2. In your structured log entry, write the ID to a field named `logging.googleapis.com/trace`. For more information about the `X-Cloud-Trace-Context` header, see [Forcing a request to be traced](https://docs.cloud.google.com/trace/docs/setup#force-trace).



To view correlated logs, see View correlated log entries in the Logs Explorer. 

## View logs

You can view app logs and request logs in several ways:

  * Use Logs Explorer from Cloud Logging in the Google Cloud console.
  * Use the Google Cloud CLI to view logs using gcloud.
  * Read logs programmatically using various methods.



### Use Logs Explorer

You can view your app and request logs using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface):

  1. Go to **Logs Explorer** in the Google Cloud console:

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select an existing Google Cloud project at the top of the page.

  3. In **Resource Type** , select **GAE Application**.




You can filter the Logs Explorer by App Engine service, version and other criteria. You can also search the logs for specific entries. See [Using the Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) for details.

If you send simple text entries to standard output, you cannot use the Logs Viewer to filter app entries by severity, nor can you see which app logs correspond to specific requests. You can still use other types of filtering in the Logs Explorer, such as text and timestamp.

### View correlated log entries in the Logs Explorer

In the Logs Explorer, to view the child log entries correlated with a parent log entry, expand the log entry.

For example, to display your App Engine request log entry and application log entries, do the following:

  1. In the navigation panel of the Google Cloud console, select **Logging** , and then select **Logs Explorer** :

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. In **Resource Type** , select **GAE Application**.

  3. To view and correlate request logs, in **Log Name** , select **request_log**. Alternatively, to correlate by request logs, click **Correlate by** and select **request_log**.

![Correlating logs](https://docs.cloud.google.com/static/appengine/docs/images/logging/correlate_logs.png)

  4. In the **Query results** pane, to expand a log entry, click **Expand**. On expanding, each request log will show the associated app logs.




After creating a filter for the logs, each request log shows corresponding app logs as child logs. Logs Explorer achieves this by correlating the `trace` field in app logs and a given request log, assuming the application uses the `google-cloud-logging` library.

The following image shows app logs grouped by the `trace` field:

![App log entries are nested in the request log entry.](https://docs.cloud.google.com/static/appengine/docs/images/logging/view_correlated_logs.png)

### Use the Google Cloud CLI

To view your App Engine logs from the command line, use the following command:
    
    
    gcloud app logs tail

For more information, see [gcloud app logs tail](https://docs.cloud.google.com/sdk/gcloud/reference/app/logs/tail).

### Reading logs programmatically

If you want to read the logs programmatically, you can use one of these methods:

  * Use a [log sink to Pub/Sub and a script to pull from Pub/Sub](https://docs.cloud.google.com/logging/docs/export).
  * Call the Cloud Logging API through the [client library](https://docs.cloud.google.com/logging/docs/reference/libraries) for your programming language.
  * Call the [Cloud Logging API REST endpoints](https://docs.cloud.google.com/logging/docs/reference/v2/rest) directly.



## Pricing, quotas, and logs retention policy

For information about pricing that applies to both request and app logs, see [Pricing for Cloud Logging](https://cloud.google.com/logging/pricing#logging-costs).

For the logs retention policy and the maximum size of log entries, see [Quotas and limits](https://docs.cloud.google.com/logging/quotas). If you want to store your logs for a longer period, you can [export your logs](https://docs.cloud.google.com/logging/docs/export) to Cloud Storage. You can also export your logs to BigQuery and Pub/Sub for further processing.

### Managing log resource usage

You can control the amount of logging activity from your app logs by writing more or fewer entries from your app's code. Request logs are created automatically, so to manage the number of request log entries associated with your app, Use the [logs exclusion](https://docs.cloud.google.com/logging/docs/exclusions#overview) feature from Cloud Logging.

## Known issues

The following are some logging issues in the second-generation runtimes:

  * Sometimes app log entries are not correlated with the request log. This happens the first time your app receives a request and any other time App Engine writes status messages to your app's log. For more information, see <https://issuetracker.google.com/issues/138365527>.

  * When you route logs from log sink to Cloud Storage, the Cloud Storage destination only contains request logs. App Engine writes app logs to different folders.

  * BigQuery fails to ingest logs due to the `@type` field in request logs. This disrupts the auto-schema detection, since BigQuery doesn't allow `@type` in field names. To resolve this, you must manually define the schema, and remove the `@type` field from request logs.

  * If you use the logging REST APIs, a background thread writes logs to Cloud Logging. If the main thread isn't active, the instance doesn't get CPU time, which causes the background thread to stop. Log processing time is delayed. At some point, the instance is removed and any unsent logs are lost. To avoid losing logs, use one of the following options:

    * Configure the Cloud Logging SDK to use gRPC. With gRPC, the logs are sent to Cloud Logging immediately. However this can increase the required CPU limits.
    * Send log messages to Cloud Logging using `stdout/stderr`. This pipeline is outside the App Engine instance and doesn't get throttled.



## What's next

  * See [Monitor and alert latency](https://docs.cloud.google.com/appengine/docs/standard/monitoring-and-alerting-latency) to learn how to use Cloud Logging to view logs for debugging errors, and how to use Cloud Trace to understand app latency.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
