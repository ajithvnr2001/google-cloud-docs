---
url: https://docs.cloud.google.com/mainframe-dual-run/docs/online-comparison-overview/
title: Online comparison overview \u00a0|\u00a0 Dual Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:31.150889+00:00
---

# Online comparison overview  |  Dual Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-dual-run/docs/online-comparison-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Dual Run ](https://docs.cloud.google.com/mainframe-dual-run/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-overview)



Send feedback 

#  Online comparison overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes Dual Run Online Comparison, which helps you compare the outputs of online transactions. With this feature, you can verify that the modernized application running on Google Cloud behaves identically to the legacy mainframe application for the same given inputs.

## How online comparisons work

Dual Run's online comparison feature lets you analyze transactions by capturing live traffic, replaying it on the modernized system, and comparing the results.

The first step in online comparison is capturing the network traffic between the mainframe and the modernized application. Dual Run uses **interceptors** for this purpose.

The **dualizer** component then replays captured online transactions to the modernized secondary system. It consumes recorded transactions from a queue (e.g., Pub/Sub), sends requests to the secondary system, and retrieves responses.

Finally, Dual Run compares the primary and secondary responses using the same underlying comparison engine that the File Comparison for batch uses. It stores requests, responses, and comparison results in Cloud Storage, and streams comparison results to BigQuery.

## Supported protocols

Dual Run supports the following protocols for online comparison:

  * HTTP(S) SOAP
  * HTTP(S) REST
  * MQ
  * TN3270



## Key features

Dual Run online comparison provides several features to enable precise and flexible transaction analysis.

### Endpoint groups

Endpoint groups are the core mechanism in Dual Run that lets you connect your mainframe endpoint to your modernized application endpoint. You define endpoint groups to specify how traffic should be handled and compared.

### Flexible comparison configuration

Online Comparison relies on two configuration files to perform the comparison:

  * **Format file:** Specifies the formats of the fields that are present in the message.
  * **Comparison file:** Specifies the fields that Dual Run should compare.



These configuration files use the same logic as the batch comparison files.

Dual Run provides flexibility by letting you specify default format and comparison files for endpoint groups, and override them for specific endpoints if needed.

Dual Run also provides a command-line interface (CLI) tool that helps you generate the configuration files based on traffic message recordings. After generation, you can manually edit the files to fine-tune the configuration.

### Operational modes

You can configure endpoint groups to operate in different modes:

  * **Passthrough:** Forwards traffic through the interceptor without modification or dualization. This mode is useful for validating network connectivity without impacting primary endpoint performance.
  * **Record:** Captures and stores live traffic from the primary endpoint for later analysis or configuration generation.
  * **Dualize:** Records the operation on the primary endpoint, replays it in the secondary endpoint, and compares the transactions.
  * **Single Output Hub (SOH):** Used for MQ endpoints where the mainframe acts as a client. It records the operation on the primary endpoint, blocks it in the secondary endpoint to prevent duplicate messages to external systems, and compares the requests rather than the responses.



### Routing and comparison rules

Dual Run lets you apply mapping rules to your application's traffic to configure distinct comparison and format files for different scenarios. When a record matches a rule (based on fields, body content, source, or format), Dual Run performs the comparison using the specific configuration files you specified.

### Support for different message formats

Dual Run supports scenarios where the modernized (secondary) system returns a different message format than the legacy (primary) system (e.g., migrating from plain-text to JSON). You can configure independent formats and define how Dual Run should pair them up for comparison.

### Support for stateful sessions

For stateful communication protocols like TN3270, Dual Run uses a **session handler**. This component maintains active sessions with the secondary system and makes the continuous connection with the mainframe possible.

## What's next

Learn more about [Dual Run architecture](https://docs.cloud.google.com/mainframe-dual-run/docs/dual-run-architecture).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
