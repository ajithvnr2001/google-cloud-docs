---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PolicyOrBuilder
title: Interface PolicyOrBuilder (0.64.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:15:24.411279+00:00
---

# Interface PolicyOrBuilder (0.64.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.PolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PolicyOrBuilder (0.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.64.0 (latest)  0.60.0  0.59.0  0.58.0  0.56.0  0.53.0  0.52.0  0.50.0  0.48.0  0.47.0  0.45.0  0.43.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.33.0  0.32.0  0.29.0  0.28.0  0.27.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface PolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getComplianceStandards(int index)
    
    
    public abstract Policy.ComplianceStandard getComplianceStandards(int index)

Optional. Contains list of mapping for a Policy to a standard and control.

` repeated .google.cloud.securityposture.v1.Policy.ComplianceStandard compliance_standards = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Policy.ComplianceStandard](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Policy.ComplianceStandard)` |   
  
### getComplianceStandardsCount()
    
    
    public abstract int getComplianceStandardsCount()

Optional. Contains list of mapping for a Policy to a standard and control.

` repeated .google.cloud.securityposture.v1.Policy.ComplianceStandard compliance_standards = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getComplianceStandardsList()
    
    
    public abstract List<Policy.ComplianceStandard> getComplianceStandardsList()

Optional. Contains list of mapping for a Policy to a standard and control.

` repeated .google.cloud.securityposture.v1.Policy.ComplianceStandard compliance_standards = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ComplianceStandard](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Policy.ComplianceStandard)>` |   
  
### getComplianceStandardsOrBuilder(int index)
    
    
    public abstract Policy.ComplianceStandardOrBuilder getComplianceStandardsOrBuilder(int index)

Optional. Contains list of mapping for a Policy to a standard and control.

` repeated .google.cloud.securityposture.v1.Policy.ComplianceStandard compliance_standards = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Policy.ComplianceStandardOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Policy.ComplianceStandardOrBuilder)` |   
  
### getComplianceStandardsOrBuilderList()
    
    
    public abstract List<? extends Policy.ComplianceStandardOrBuilder> getComplianceStandardsOrBuilderList()

Optional. Contains list of mapping for a Policy to a standard and control.

` repeated .google.cloud.securityposture.v1.Policy.ComplianceStandard compliance_standards = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.securityposture.v1.Policy.ComplianceStandardOrBuilder>` |   
  
### getConstraint()
    
    
    public abstract Constraint getConstraint()

Required. Constraint details.

` .google.cloud.securityposture.v1.Constraint constraint = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Constraint](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.Constraint)` | The constraint.  
  
### getConstraintOrBuilder()
    
    
    public abstract ConstraintOrBuilder getConstraintOrBuilder()

Required. Constraint details.

` .google.cloud.securityposture.v1.Constraint constraint = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ConstraintOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securityposture/latest/com.google.cloud.securityposture.v1.ConstraintOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Description of the Policy.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Description of the Policy.

`string description = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getPolicyId()
    
    
    public abstract String getPolicyId()

Required. ID of the Policy that is user generated, immutable and unique within the scope of a policy set.

`string policy_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The policyId.  
  
### getPolicyIdBytes()
    
    
    public abstract ByteString getPolicyIdBytes()

Required. ID of the Policy that is user generated, immutable and unique within the scope of a policy set.

`string policy_id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for policyId.  
  
### hasConstraint()
    
    
    public abstract boolean hasConstraint()

Required. Constraint details.

` .google.cloud.securityposture.v1.Constraint constraint = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the constraint field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
