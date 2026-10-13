---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Quota
title: Google API Common Protos Client - Class Quota (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:13:16.126828+00:00
---

# Google API Common Protos Client - Class Quota (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.Quota

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class Quota (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class Quota.

Quota configuration helps to achieve fairness and budgeting in service usage.

The metric based quota configuration works this way:

  * The service configuration defines a set of metrics.
  * For API calls, the quota.metric_rules maps methods to metrics with corresponding costs.
  * The quota.limits defines limits on the metrics, which will be used for quota checks at runtime. An example quota configuration in yaml format: quota: limits:
    * name: apiWriteQpsPerProject metric: library.googleapis.com/write_calls unit: "1/min/{project}" # rate limit for consumer projects values: STANDARD: 10000 (The metric rules bind all methods to the read_calls metric, except for the UpdateBook and DeleteBook methods. These two methods are mapped to the write_calls metric, with the UpdateBook method consuming at twice rate as the DeleteBook method.) metric_rules:
    * selector: "*" metric_costs: library.googleapis.com/read_calls: 1
    * selector: google.example.library.v1.LibraryService.UpdateBook metric_costs: library.googleapis.com/write_calls: 2
    * selector: google.example.library.v1.LibraryService.DeleteBook metric_costs: library.googleapis.com/write_calls: 1 Corresponding Metric definition: metrics:
    * name: library.googleapis.com/read_calls display_name: Read requests metric_kind: DELTA value_type: INT64
    * name: library.googleapis.com/write_calls display_name: Write requests metric_kind: DELTA value_type: INT64



Generated from protobuf message `google.api.Quota`

## Namespace

Google \ Api

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ limits` |  `array<[QuotaLimit](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.QuotaLimit)>`   
List of QuotaLimit definitions for the service.  
`↳ metric_rules` |  `array<[MetricRule](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricRule)>`   
List of MetricRule definitions, each one mapping a selected method to one or more metrics.  
  
### getLimits

List of QuotaLimit definitions for the service.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<[QuotaLimit](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.QuotaLimit)>` |   
  
### setLimits

List of QuotaLimit definitions for the service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[QuotaLimit](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.QuotaLimit)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetricRules

List of MetricRule definitions, each one mapping a selected method to one or more metrics.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<[MetricRule](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricRule)>` |   
  
### setMetricRules

List of MetricRule definitions, each one mapping a selected method to one or more metrics.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[MetricRule](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MetricRule)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
