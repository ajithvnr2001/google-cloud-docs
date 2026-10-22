---
url: https://docs.cloud.google.com/error-reporting/docs/setup/
title: Collect error data by using Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:08.507164+00:00
---

# Collect error data by using Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Collect error data by using Error Reporting Stay organized with collections  Save and categorize content based on your preferences. 

You can send application exceptions and error events to Error Reporting so that Error Reporting can analyze error data in your Google Cloud project. Depending on your compute environment, programming language, and authentication requirements, you can collect error data in the following ways:

  * **Automatic log collection** : Supported compute environments automatically send error data to Cloud Logging for Error Reporting to analyze. For example, Cloud Run automatically sends exceptions written to `stderr` to Logging.
  * **Client libraries** : You can instrument your application code with language-specific client libraries to send error reports directly from your app.
  * **REST APIs** : You can call the Error Reporting API or the Cloud Logging API to write formatted error events and stack traces, including when you require API key authentication.



## When Error Reporting analyzes log entries

Error Reporting is a global service built on Cloud Logging and can analyze log entries when all of the following are true: 

  * Assured workloads are disabled. For more information, see [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage) are disabled on all log buckets that store the log entry. Error Reporting can't store log entries in log buckets that have CMEK enabled. For information about how to determine the CMEK configuration for a log bucket, see [Verify key enablement](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#verify-key).
  * The log bucket satisfies one of the following: 
    * The log bucket is stored in the same project where the log entries originated.
    * The log entries were routed to a project, and then that project stored those log entries in a log bucket that it owns.



## VPC Service Controls support

VPC Service Controls support Error Reporting.

To reduce the risk of data exfiltration, use VPC Service Controls to create a service perimeter around your Google-managed services. For information about VPC Service Controls and how to create a service perimeter, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

## Configure environments to automatically report error data

For information about environment-specific configuration requirements, see the following guides:

  * [App Engine flexible environment](https://docs.cloud.google.com/error-reporting/docs/setup/app-engine-flexible-environment)
  * [App Engine standard environment](https://docs.cloud.google.com/error-reporting/docs/setup/app-engine-standard-environment)
  * [Apps Script](https://docs.cloud.google.com/error-reporting/docs/setup/apps-script)
  * [Cloud Run functions](https://docs.cloud.google.com/error-reporting/docs/setup/cloud-functions)
  * [Cloud Run](https://docs.cloud.google.com/error-reporting/docs/setup/cloud-run)
  * [Compute Engine](https://docs.cloud.google.com/error-reporting/docs/setup/compute-engine)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/error-reporting/docs/setup/kubernetes-engine)
  * [Amazon EC2](https://docs.cloud.google.com/error-reporting/docs/setup/ec2)



## Instrument apps by using client libraries

For information about how to configure your application to send error reports, see the language-specific configuration guides:

  * [Go apps](https://docs.cloud.google.com/error-reporting/docs/setup/go)
  * [Java apps](https://docs.cloud.google.com/error-reporting/docs/setup/java)
  * [.NET apps](https://docs.cloud.google.com/error-reporting/docs/setup/dotnet)
  * [Node.js apps](https://docs.cloud.google.com/error-reporting/docs/setup/nodejs)
  * [Python apps](https://docs.cloud.google.com/error-reporting/docs/setup/python)
  * [PHP apps](https://docs.cloud.google.com/error-reporting/docs/setup/php)
  * [Ruby apps](https://docs.cloud.google.com/error-reporting/docs/setup/ruby)



## Write error data by using an API

You can report error events to your Google Cloud project by executing the Error Reporting API method [`report`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report) or the Logging API method [`write`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/write).

  * If you require API key-based authentication, then you must use the Error Reporting API. To report an error event by using the Error Reporting API, execute the method [`report`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report) and format the request body of the method as a [`ReportedErrorEvent`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent) object.

When you use the Error Reporting API, log entries with properly formatted error messages are automatically generated and written to [Logging](https://docs.cloud.google.com/logging/docs). These log entries are written to a log whose `logName` is formatted as follows:
        
        projects/PROJECT_ID/clouderrorreporting.googleapis.com%2Freported_errors
        

Because log entries are generated by calls to `report`, you might incur Logging ingestion costs. To control which log entries are ingested, see [Exclusion filters](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions).

  * If you want to use the Logging API, then you must format the [`LogEntry`](https://docs.cloud.google.com/logging/docs/api/reference/rest/v2/LogEntry) object so that it includes a stack trace or a [`ReportedErrorEvent`](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent) object. For more information about the formatting requirements, see [Format errors in logs](https://docs.cloud.google.com/error-reporting/docs/formatting-error-messages).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
