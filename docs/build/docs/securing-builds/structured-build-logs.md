---
url: https://docs.cloud.google.com/build/docs/securing-builds/structured-build-logs/
title: Use structured logging with build logs \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:10.086594+00:00
---

# Use structured logging with build logs  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/securing-builds/structured-build-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Use structured logging with build logs Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how you can configure your Cloud Build logs for use with [structured logging](https://docs.cloud.google.com/logging/docs/structured-logging) in Cloud Logging.

Structured logging lets you store a JSON-formatted build log field as part of the `jsonPayload` field, or as certain other fields, in a [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). You can set up your build config file so that specific build log fields are mapped this way when you send a build log to Logging.

For example, if your build log contains a `message`, then the message appears in either `textPayload` or `jsonPayload.message` in the resulting log entry. If a build log field can't be mapped to a specific log entry field, then the build log field is stored as part of the log entry `jsonPayload`.

## Map build log fields to log entry fields

To enable field mapping on your build logs, set the [`BuildOptions`](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#buildoptions) field `enableStructuredLogging` to `TRUE`.

The following table shows build log fields that map to a log entry field:

BuildLog Field (JSON) | LogEntry Field | Description | Notes  
---|---|---|---  
`message` | `textPayload` or `jsonPayload.message` | Lets you set the log message | Must be a string. If the build log contains only mappable fields, then the message appears in `textPayload`. Otherwise, the message appears in `jsonPayload.message`. If the build log contains multiple steps, then the step identifier appears at the beginning of the message.  
`severity` | `severity` | Lets you set the log severity. | Must be an enum of `[LogSeverity](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#logseverity)`.  
  
The following build log fields can't be mapped and will be dropped from the log entry if they appear in a build log:

  * `httpRequest`
  * `logging.googleapis.com/insertId`
  * `logging.googleapis.com/labels`
  * `logging.googleapis.com/operation`
  * `logging.googleapis.com/sourceLocation`
  * `logging.googleapis.com/spanId`
  * `logging.googleapis.com/trace`
  * `logging.googleapis.com/trace_sampled`
  * `time`
  * `timestamp`
  * `timestampSeconds`
  * `timestampNanos`



All other build log fields will appear as part of the log entry's `jsonPayload`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
