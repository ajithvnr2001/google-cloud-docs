---
url: https://docs.cloud.google.com/apis/docs/troubleshooting/
title: Troubleshooting API usage \u00a0|\u00a0 Cloud APIs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:17.377104+00:00
---

# Troubleshooting API usage  |  Cloud APIs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apis/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud APIs ](https://docs.cloud.google.com/apis/docs/overview)



Send feedback 

#  Troubleshooting API usage Stay organized with collections  Save and categorize content based on your preferences. 

Diagnostic telemetry and error analysis let you identify and resolve request failures across Google APIs and Google Cloud APIs. You can inspect API usage metrics, client-side logs, Cloud Audit Logs, and structured error responses to diagnose root causes in your applications.

## Background

Google APIs are networked APIs provided by Google services. Applications can access Google APIs via JSON HTTP and gRPC from different environments. We recommend developers to use Google-provided client libraries in their applications. These libraries implement common boilerplate logic, such as authentication and list pagination, which greatly reduce development overhead and common mistakes.

For more information, see [Client Libraries Explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained)

## Getting started

If you are new to Google APIs, you should follow the [Getting Started](https://docs.cloud.google.com/apis/docs/getting-started) page to complete the preparation steps for your application. You should first use the `curl -v` command to send test requests to Google APIs that you want to use. It lets you experiment with Google APIs without writing any code. You can often resolve many issues before you start real application development.

For more information, see [Getting Started](https://docs.cloud.google.com/apis/docs/getting-started).

## Troubleshooting using metrics

Google APIs provide free API metrics that cover common aspects of API usage, including request counts, errors, latencies, request and response sizes. They provide fine-grained dimensions in terms of applications and locations. Developers can discover abnormal API usage, and identify potential root causes. For example, higher 400 errors can mean a recently updated application has some logical bugs, or higher request and response sizes can cause slower application performance.

For more information, see [Monitoring API usage](https://docs.cloud.google.com/apis/docs/monitoring).

## Troubleshooting using logs

For security and privacy reasons, Google APIs generally don't provide API logs to application developers. We highly recommend application developers log API errors on the client side. You can either log the errors to a local storage or to a remote logging API, such as [Cloud Logging API](https://docs.cloud.google.com/logging).

Logs typically contain more information about errors than metrics, such as error messages and error details. They are extremely useful and often necessary to troubleshoot API errors. When developers notice any issue with their API usage, they can query the logs to find error messages and error details, and use the information to resolve the errors or contact the support.

### Cloud Audit Logs

For security sensitive activities, Google Cloud products may generate audit logs that contain detailed information of the activities. They are a great source of information for troubleshooting your usage of Google Cloud APIs. For example, [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) dry run feature generates audit logs for administrators to evaluate the upcoming policy changes.

For more information, see [Cloud Audit Logs](https://docs.cloud.google.com/logging/docs/audit).

## Resolving errors

If you have issues with your Google API usage and you have found the corresponding metrics and logs, you can follow API Design Guide [Errors](https://docs.cloud.google.com/apis/design/errors) page to resolve the errors.

In general, each API error has 3 pieces of information: error code, error message, and error details:

  * The error code lets applications handle the error at the higher level, such as retry after `503` errors or re-authenticate users after `401` errors.
  * The error message lets application developers understand the error and fix their application logic.

**Warning:** Do not code against the error messages; they are subject to change without notice.
  * The error details contain additional information the applications can use to handle the error programmatically.




For more information, see the [Errors](https://docs.cloud.google.com/apis/design/errors) page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
