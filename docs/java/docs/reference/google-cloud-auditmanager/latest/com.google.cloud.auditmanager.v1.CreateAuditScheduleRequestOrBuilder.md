---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.CreateAuditScheduleRequestOrBuilder
title: Interface CreateAuditScheduleRequestOrBuilder (0.17.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:46:44.053290+00:00
---

# Interface CreateAuditScheduleRequestOrBuilder (0.17.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.CreateAuditScheduleRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CreateAuditScheduleRequestOrBuilder (0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.13.0  0.12.0  0.11.0  0.9.0  0.6.0  0.5.0  0.3.0  0.1.0 
    
    
    public interface CreateAuditScheduleRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuditSchedule()
    
    
    public abstract AuditSchedule getAuditSchedule()

Required. Audit schedule to create.

` .google.cloud.auditmanager.v1.AuditSchedule audit_schedule = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AuditSchedule](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.AuditSchedule)` | The auditSchedule.  
  
### getAuditScheduleId()
    
    
    public abstract String getAuditScheduleId()

Required. ID to use for the audit schedule, which becomes the final component of the audit schedule's resource name.

`string audit_schedule_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The auditScheduleId.  
  
### getAuditScheduleIdBytes()
    
    
    public abstract ByteString getAuditScheduleIdBytes()

Required. ID to use for the audit schedule, which becomes the final component of the audit schedule's resource name.

`string audit_schedule_id = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for auditScheduleId.  
  
### getAuditScheduleOrBuilder()
    
    
    public abstract AuditScheduleOrBuilder getAuditScheduleOrBuilder()

Required. Audit schedule to create.

` .google.cloud.auditmanager.v1.AuditSchedule audit_schedule = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AuditScheduleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-auditmanager/latest/com.google.cloud.auditmanager.v1.AuditScheduleOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. Project or folder that this audit schedule is for, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. Project or folder that this audit schedule is for, in one of the following formats:

  * `projects/{project}/locations/{location}`
  * `folders/{folder}/locations/{location}`



` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If `true`, only validates the request and does not create the audit schedule. This executes standard request validation (such as schema, framework existence, scope, and IAM checks) and skips the apply phase.

Use this field for the following purposes:

  * **Infrastructure as Code (IaC)** : Allow tools like Terraform to run dry-run mutations (e.g., `terraform plan`) without creating real resources or incurring costs.
  * **User Interface Validation** : Enable real-time form and permission validation in custom UIs before submitting requests.
  * **CI/CD & Automation**: Test your scripts, permissions, and parameters safely without consuming resource quotas.



`bool validate_only = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasAuditSchedule()
    
    
    public abstract boolean hasAuditSchedule()

Required. Audit schedule to create.

` .google.cloud.auditmanager.v1.AuditSchedule audit_schedule = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the auditSchedule field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
