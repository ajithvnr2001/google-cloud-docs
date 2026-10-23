---
url: https://docs.cloud.google.com/error-reporting/docs/grouping-errors/
title: Error Reporting overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:18.683825+00:00
---

# Error Reporting overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/error-reporting/docs/grouping-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Error Reporting ](https://docs.cloud.google.com/error-reporting/docs)
  * [ Guides ](https://docs.cloud.google.com/error-reporting/docs/grouping-errors)



Send feedback 

#  Error Reporting overview Stay organized with collections  Save and categorize content based on your preferences. 

Error Reporting lets you identify, prioritize, and triage issues across your cloud services by aggregating application error events into error groups based on their root cause. An _error event_ represents a single application error and captures its timestamp, execution context, and message. Error Reporting collects events directly from the [Error Reporting API](https://docs.cloud.google.com/error-reporting/reference/rest) or infers them by scanning log entries for stack traces and common error patterns

## When Error Reporting analyzes log entries

Error Reporting is a global service built on Cloud Logging and can analyze log entries when all of the following are true: 

  * Assured workloads are disabled. For more information, see [Overview of Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage) are disabled on all log buckets that store the log entry. Error Reporting can't store log entries in log buckets that have CMEK enabled. For information about how to determine the CMEK configuration for a log bucket, see [Verify key enablement](https://docs.cloud.google.com/logging/docs/routing/managed-encryption-storage#verify-key).
  * The log bucket satisfies one of the following: 
    * The log bucket is stored in the same project where the log entries originated.
    * The log entries were routed to a project, and then that project stored those log entries in a log bucket that it owns.



## How error events are grouped

To optimize performance, Error Reporting samples up to 1,000 errors per hour, estimating counts when reaching this threshold. If event volume exceeds capacity, Error Reporting samples up to 100 errors per hour and continues to extrapolate the displayed counts.

When Error Reporting evaluates log entries to identify error events, it ignores the following data:

  * Log entries written by the App Engine standard environment that have a severity level lower than `ERROR`.
  * Stack frames that aren't owned by the user, such as those that belong to public libraries.



When a log entry is scanned, Error Reporting makes the following modifications before inferring error events:

  * Replaces any repeating sequence of one or more stack frames with a single occurrence of that sequence.
  * Removes compiler-introduced methods and symbols.



Error Reporting applies these rules, in the specified order, to group error events:

Error event | Grouped by  
---|---  
**Error events caused by a general problem in the environment**. For example, problems specific to App Engine:
    
    
    com.google.apphosting.runtime.HardDeadlineExceededError
    
    
    com.google.appengine.api.datastore.DatastoreTimeoutException

Java problems:
    
    
    java.util.concurrent.CancellationException

| Grouped by exception type.  
**Error events with a stack trace**. In the case of nested exceptions, the innermost exception is considered. For example:
    
    
    runtime error: index out of range
    package1.func1()
          file1:20
    package2.func2()
          file2:33

| Grouped by exception type and the five topmost frames.  
**Error events without a stack trace but with a message**. For example:
    
    
    runtime error: index out of range
        func1()

In this example, the following tokens are considered: `runtime`, `error`, and `index`. | Grouped by message and (if present) function name. Only the first three literal tokens of the message are considered.  
  
## Data regionality

If you set up [Assured Workloads](https://cloud.google.com/security/products/assured-workloads) for data residency or [Impact Level 4 (IL4)](https://cloud.google.com/security/compliance/disa) requirements, then Google Cloud automatically disables Error Reporting.

In Cloud Logging, you can [regionalize your logs](https://docs.cloud.google.com/logging/docs/regionalized-logs) by routing them to a specific location. On the **Error Groups** page, Error Reporting organizes and shows error groups based on the region of the log bucket that contains the log entries. For example, an error group listed under `us-central1` contains only error logs that are part of a log bucket in `us-central1`. Global error groups contain only error logs that are part of a log bucket in the `global` region.

To filter the region of the error groups displayed on the **Error Groups** page, select a value from the **Region** menu. This menu has a default value of `global`.

![The Region menu on the Error Groups page.](https://docs.cloud.google.com/static/error-reporting/images/error-region.png)

**Note:** Because Error Reporting is a global service, error groups can be accessed from any region. This behavior isn't configurable.

## What's next

  * [Collect error events by using Error Reporting](https://docs.cloud.google.com/error-reporting/docs/setup)
  * [View error groups](https://docs.cloud.google.com/error-reporting/docs/viewing-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
