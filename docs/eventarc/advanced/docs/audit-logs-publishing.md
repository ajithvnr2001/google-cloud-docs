---
url: https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs-publishing/
title: Eventarc Publishing audit logging \u00a0|\u00a0 Eventarc Advanced \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:15.117105+00:00
---

# Eventarc Publishing audit logging  |  Eventarc Advanced  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/eventarc/advanced/docs/audit-logs-publishing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Eventarc ](https://docs.cloud.google.com/eventarc/docs)
  * [ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs)
  * [ Guides ](https://docs.cloud.google.com/eventarc/advanced/docs/overview)



Send feedback 

#  Eventarc Publishing audit logging Stay organized with collections  Save and categorize content based on your preferences. 

[ Advanced ](https://docs.cloud.google.com/eventarc/advanced/docs/overview) [ Standard ](https://docs.cloud.google.com/eventarc/standard/docs/overview)

This document describes audit logging for Eventarc Publishing. Google Cloud services generate audit logs that record administrative and access activities within your Google Cloud resources. For more information about Cloud Audit Logs, see the following: 

  * [Types of audit logs](https://docs.cloud.google.com/logging/docs/audit#types)
  * [Audit log entry structure](https://docs.cloud.google.com/logging/docs/audit#audit_log_entry_structure)
  * [Storing and routing audit logs](https://docs.cloud.google.com/logging/docs/audit#storing_and_routing_audit_logs)
  * [Cloud Logging pricing summary](https://docs.cloud.google.com/stackdriver/pricing#logs-pricing-summary)
  * [Enable Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access)



## Service name

Eventarc Publishing audit logs use the service name `eventarcpublishing.googleapis.com`. Filter for this service: 
    
    
        protoPayload.serviceName="eventarcpublishing.googleapis.com"
      

## Methods by permission type

Each IAM permission has a `type` property, whose value is an enum that can be one of four values: `ADMIN_READ`, `ADMIN_WRITE`, `DATA_READ`, or `DATA_WRITE`. When you call a method, Eventarc Publishing generates an audit log whose category is dependent on the `type` property of the permission required to perform the method. Methods that require an IAM permission with the `type` property value of `DATA_READ`, `DATA_WRITE`, or `ADMIN_READ` generate [Data Access](https://docs.cloud.google.com/logging/docs/audit#data-access) audit logs. Methods that require an IAM permission with the `type` property value of `ADMIN_WRITE` generate [Admin Activity](https://docs.cloud.google.com/logging/docs/audit#admin-activity) audit logs.

Permission type | Methods  
---|---  
`DATA_WRITE` | `google.cloud.eventarc.publishing.v1.Publisher.Publish`  
  
## API interface audit logs

For information about how and which permissions are evaluated for each method, see the Identity and Access Management documentation for Eventarc Publishing.

### `google.cloud.eventarc.publishing.v1.Publisher`

The following audit logs are associated with methods belonging to `google.cloud.eventarc.publishing.v1.Publisher`.

#### `Publish`

  * **Method** : `google.cloud.eventarc.publishing.v1.Publisher.Publish`  

  * **Audit log type** : [Data access](https://docs.cloud.google.com/logging/docs/audit#data-access)  

  * **Permissions** : 
    * `eventarc.messageBuses.publish - DATA_WRITE`
  * **Method is a long-running or streaming operation** : No.  

  * **Filter for this method** : ` protoPayload.methodName="google.cloud.eventarc.publishing.v1.Publisher.Publish" `  




## Methods that don't produce audit logs

A method might not produce audit logs for one or more of the following reasons: 

  * It is a high volume method involving significant log generation and storage costs.
  * It has low auditing value.
  * Another audit or platform log already provides method coverage.



The following methods don't produce audit logs:

  * `google.cloud.eventarc.publishing.v1.Publisher.PublishChannelConnectionEvents`
  * `google.cloud.eventarc.publishing.v1.Publisher.PublishEvents`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
