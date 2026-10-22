---
url: https://docs.cloud.google.com/logging/docs/view/troubleshoot-lql/
title: Troubleshoot Logging query language \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:03.661030+00:00
---

# Troubleshoot Logging query language  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/view/troubleshoot-lql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Troubleshoot Logging query language Stay organized with collections  Save and categorize content based on your preferences. 

This document explains common issues that you might encounter when using the Logging query language.

### Syntax issues

If you have problems with your queries' expressions, check the following:

  * Your query obeys the syntax rules, with matched parentheses and quotation marks.

  * Your log entry field names are correctly spelled.

  * Boolean operations are in uppercase letters (`AND`, `OR`, `NOT`).

  * Ensure that you're using [`NULL_VALUE`](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#nullvalue) to represent JSON null values.

  * Boolean expressions as global restrictions or as the right-hand side of comparisons should be parenthesized for clarity. For example, the following two queries look the same, but are not:
        
        insertId = "ABC-1" OR "ABC-2"  -- ERROR!?
        insertId = ("ABC-1" OR "ABC-2")
        

  * Unquoted text must not contain any special characters. When in doubt, add double quotation marks. For example, in the following, the first comparison is illegal because of the embedded substring operator (`:`). The comparison must be written with quotation marks:
        
        insertId = abc:def  -- ILLEGAL!
        insertId = "abc:def"
        

**Note:** If you use the search bar and if you don't wrap the search terms in double quotes, then the [`SEARCH` function](https://docs.cloud.google.com/logging/docs/view/logging-query-language#search-functions) is used. The `SEARCH` function performs a search along token boundaries. For example, if you enter `world` in the search bar, then Logging runs the query `SEARCH("world")`. The previous query matches `world` but it doesn't match `worlds`.
  * The [Google Cloud CLI](https://docs.cloud.google.com/logging/docs/reference/tools/gcloud-logging) requires the query to be in double quotes. To use double quotes for escaping special characters using the `gcloud logging` command, wrap the entire query with single quotes instead:
        
        gcloud logging read 'resource.type=gce_instance AND jsonPayload.message="Stopped Unattended Upgrades Shutdown."'
        gcloud logging read 'timestamp>="2020-06-17T21:00:00Z"'
        

  * When you are filtering on a field that is associated with the [`Any`](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/any.proto) message type, the `value` field is automatically traversed. Therefore, don't include `value` in the query.

For example, the [`Status`](https://github.com/grpc/grpc/blob/master/src/proto/grpc/status/status.proto) field in an [`AuditLog`](https://docs.cloud.google.com/logging/docs/reference/audit/auditlog/rest/Shared.Types/AuditLog) message has a `details` field that is of type `google.protobuf.Any`. To query the `details` field, omit the `value` field when specifying the filter:

    * Do
          
          protoPayload.status.**details.** conditionNotMet.userVisibleMessage =~ "Specified reservation.*"
          

    * Don't
          
          protoPayload.status.**details.value.** conditionNotMet.userVisibleMessage =~ "Specified reservation.*"
          




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
