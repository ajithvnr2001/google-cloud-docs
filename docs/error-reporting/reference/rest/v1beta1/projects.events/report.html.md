---
url: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html
title: Method: projects.events.report \u00a0|\u00a0 Error Reporting \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:27:40.280252+00:00
---

# Method: projects.events.report  |  Error Reporting  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report.html

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Reference ](https://docs.cloud.google.com/error-reporting/reference)



Send feedback 

#  Method: projects.events.report Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * ReportedErrorEvent
    * JSON representation
  * Try it!



Report an individual error event and record the event to a log.

This endpoint accepts **either** an OAuth token, **or** an [API key](https://support.google.com/cloud/answer/6158862) for authentication. To use an API key, append it to the URL as the value of a `key` parameter. For example:

`POST https://clouderrorreporting.googleapis.com/v1beta1/{projectName}/events:report?key=123ABC456`

**Note:** [Error Reporting](https://cloud.google.com/error-reporting) is a service built on Cloud Logging and can analyze log entries when all of the following are true:

  * Customer-managed encryption keys (CMEK) are disabled on the log bucket.
  * The log bucket satisfies one of the following: 
    * The log bucket is stored in the same project where the logs originated.
    * The logs were routed to a project, and then that project stored those logs in a log bucket that it owns.



### HTTP request

Choose an endpoint:

globalusafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://clouderrorreporting.googleapis.com/v1beta1/{projectName=projects/*}/events:report`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectName` |  `string` Required. The resource name of the Google Cloud Platform project. Written as `projects/{projectId}`, where `{projectId}` is the [Google Cloud Platform project ID](https://support.google.com/cloud/answer/6158840).Example: // `projects/my-project-123`.  
  
### Request body

The request body contains an instance of `[ReportedErrorEvent](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/projects.events/report#ReportedErrorEvent)`.

### Response body

If successful, the response body is empty.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/stackdriver-integration`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ReportedErrorEvent

An error event which is reported to the Error Reporting system.

JSON representation  
---  
      
    
    {
      "eventTime": string,
      "serviceContext": {
        object ([ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext))
      },
      "message": string,
      "context": {
        object ([ErrorContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext))
      }
    }  
  
Fields  
---  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Time when the event occurred. If not provided, the time when the event was received by the Error Reporting system is used. If provided, the time must not exceed the [logs retention period](https://cloud.google.com/logging/quotas#logs_retention_periods) in the past, or be more than 24 hours in the future. If an invalid time is provided, then an error is returned.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`serviceContext` |  `object (`[ServiceContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ServiceContext)`)` Required. The service context in which this error has occurred.  
`message` |  `string` Required. The error message. If no `context.reportLocation` is provided, the message must contain a header (typically consisting of the exception type name and an error message) and an exception stack trace in one of the supported programming languages and formats. Supported languages are Java, Python, JavaScript, Ruby, C#, PHP, Go, and Rust. Supported stack trace formats are:

  * **Java** : Must be the return value of [`Throwable.printStackTrace()`](https://docs.oracle.com/javase/7/docs/api/java/lang/Throwable.html#printStackTrace%28%29).
  * **Python** : Must be the return value of [`traceback.format_exc()`](https://docs.python.org/2/library/traceback.html#traceback.format_exc).
  * **JavaScript** : Must be the value of [`error.stack`](https://github.com/v8/v8/wiki/Stack-Trace-API) as returned by V8.
  * **Ruby** : Must contain frames returned by [`Exception.backtrace`](https://ruby-doc.org/core-2.2.0/Exception.html#method-i-backtrace).
  * **C#** : Must be the return value of [`Exception.ToString()`](https://msdn.microsoft.com/en-us/library/system.exception.tostring.aspx).
  * **PHP** : Must be prefixed with `"PHP (Notice|Parse error|Fatal error|Warning): "` and contain the result of [`(string)$exception`](https://php.net/manual/en/exception.tostring.php).
  * **Go** : Must be the return value of [`debug.Stack()`](https://pkg.go.dev/runtime/debug#Stack).
  * **Rust** : Must contain standard [`std::backtrace`](https://doc.rust-lang.org/std/backtrace/index.html) frames. Requires `RUST_BACKTRACE=1` and debug symbols enabled.

  
`context` |  `object (`[ErrorContext](https://docs.cloud.google.com/error-reporting/reference/rest/v1beta1/ErrorContext)`)` Optional. A description of the context in which the error occurred.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-18 UTC."],[],[]] 
