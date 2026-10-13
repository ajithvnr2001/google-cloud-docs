---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentOrBuilder
title: Interface CmEnrollmentOrBuilder (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:10.810118+00:00
---

# Interface CmEnrollmentOrBuilder (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.CmEnrollmentOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CmEnrollmentOrBuilder (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CmEnrollmentOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuditConfig()
    
    
    public abstract AuditConfig getAuditConfig()

Optional. The audit configuration for Compliance Manager. If set at a scope, this configuration overrides any inherited audit configuration.

` .google.cloud.cloudsecuritycompliance.v1.AuditConfig audit_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AuditConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditConfig)` | The auditConfig.  
  
### getAuditConfigOrBuilder()
    
    
    public abstract AuditConfigOrBuilder getAuditConfigOrBuilder()

Optional. The audit configuration for Compliance Manager. If set at a scope, this configuration overrides any inherited audit configuration.

` .google.cloud.cloudsecuritycompliance.v1.AuditConfig audit_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AuditConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AuditConfigOrBuilder)` |   
  
### getEnrolled()
    
    
    public abstract boolean getEnrolled()

Optional. Whether the resource is enrolled in Compliance Manager. This setting is inherited by all descendants.

`bool enrolled = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enrolled.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The name of the Compliance Manager enrollment.

Supported formats are the following:

  * `organizations/{organization_id}/locations/{location}/cmEnrollment`
  * `folders/{folder_id}/locations/{location}/cmEnrollment`
  * `projects/{project_id}/locations/{location}/cmEnrollment`



`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The name of the Compliance Manager enrollment.

Supported formats are the following:

  * `organizations/{organization_id}/locations/{location}/cmEnrollment`
  * `folders/{folder_id}/locations/{location}/cmEnrollment`
  * `projects/{project_id}/locations/{location}/cmEnrollment`



`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### hasAuditConfig()
    
    
    public abstract boolean hasAuditConfig()

Optional. The audit configuration for Compliance Manager. If set at a scope, this configuration overrides any inherited audit configuration.

` .google.cloud.cloudsecuritycompliance.v1.AuditConfig audit_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the auditConfig field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
