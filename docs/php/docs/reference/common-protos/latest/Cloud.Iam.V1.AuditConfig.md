---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.AuditConfig
title: Google API Common Protos V1 Client - Class AuditConfig (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:10:37.354005+00:00
---

# Google API Common Protos V1 Client - Class AuditConfig (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.AuditConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos V1 Client - Class AuditConfig (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos V1 Client class AuditConfig.

Specifies the audit configuration for a service.

The configuration determines which permission types are logged, and what identities, if any, are exempted from logging. An AuditConfig must have one or more AuditLogConfigs. If there are AuditConfigs for both `allServices` and a specific service, the union of the two AuditConfigs is used for that service: the log_types specified in each AuditConfig are enabled, and the exempted_members in each AuditLogConfig are exempted. Example Policy with multiple AuditConfigs: { "audit_configs": [ { "service": "allServices", "audit_log_configs": [ { "log_type": "DATA_READ", "exempted_members": [ "user:jose@example.com" ] }, { "log_type": "DATA_WRITE" }, { "log_type": "ADMIN_READ" } ] }, { "service": "sampleservice.googleapis.com", "audit_log_configs": [ { "log_type": "DATA_READ" }, { "log_type": "DATA_WRITE", "exempted_members": [ "user:aliya@example.com" ] } ] } ] } For sampleservice, this policy enables DATA_READ, DATA_WRITE and ADMIN_READ logging. It also exempts `jose\@example.com` from DATA_READ logging, and `aliya\@example.com` from DATA_WRITE logging.

Generated from protobuf message `google.iam.v1.AuditConfig`

## Namespace

Google \ Cloud \ Iam \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ service` |  `string`   
Specifies a service that will be enabled for audit logging. For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.  
`↳ audit_log_configs` |  `array<[AuditLogConfig](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.AuditLogConfig)>`   
The configuration for logging of each type of permission.  
  
### getService

Specifies a service that will be enabled for audit logging.

For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setService

Specifies a service that will be enabled for audit logging.

For example, `storage.googleapis.com`, `cloudsql.googleapis.com`. `allServices` is a special value that covers all services.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAuditLogConfigs

The configuration for logging of each type of permission.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<[AuditLogConfig](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.AuditLogConfig)>` |   
  
### setAuditLogConfigs

The configuration for logging of each type of permission.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[AuditLogConfig](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Cloud.Iam.V1.AuditLogConfig)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
