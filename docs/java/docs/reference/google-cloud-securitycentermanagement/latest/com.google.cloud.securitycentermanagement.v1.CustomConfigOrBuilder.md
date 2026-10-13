---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfigOrBuilder
title: Interface CustomConfigOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:39.937212+00:00
---

# Interface CustomConfigOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface CustomConfigOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface CustomConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCustomOutput()
    
    
    public abstract CustomConfig.CustomOutputSpec getCustomOutput()

Optional. Custom output properties.

` .google.cloud.securitycentermanagement.v1.CustomConfig.CustomOutputSpec custom_output = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConfig.CustomOutputSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.CustomOutputSpec)` | The customOutput.  
  
### getCustomOutputOrBuilder()
    
    
    public abstract CustomConfig.CustomOutputSpecOrBuilder getCustomOutputOrBuilder()

Optional. Custom output properties.

` .google.cloud.securitycentermanagement.v1.CustomConfig.CustomOutputSpec custom_output = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConfig.CustomOutputSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.CustomOutputSpecOrBuilder)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

Optional. Text that describes the vulnerability or misconfiguration that the custom module detects. This explanation is returned with each finding instance to help investigators understand the detected issue. The text must be enclosed in quotation marks.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

Optional. Text that describes the vulnerability or misconfiguration that the custom module detects. This explanation is returned with each finding instance to help investigators understand the detected issue. The text must be enclosed in quotation marks.

`string description = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getPredicate()
    
    
    public abstract Expr getPredicate()

Optional. The Common Expression Language (CEL) expression to evaluate to produce findings. When the expression evaluates to `true` against a resource, a finding is generated.

`.google.type.Expr predicate = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.Expr` | The predicate.  
  
### getPredicateOrBuilder()
    
    
    public abstract ExprOrBuilder getPredicateOrBuilder()

Optional. The Common Expression Language (CEL) expression to evaluate to produce findings. When the expression evaluates to `true` against a resource, a finding is generated.

`.google.type.Expr predicate = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`com.google.type.ExprOrBuilder` |   
  
### getRecommendation()
    
    
    public abstract String getRecommendation()

Optional. An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is returned with each finding generated by this module.

`string recommendation = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The recommendation.  
  
### getRecommendationBytes()
    
    
    public abstract ByteString getRecommendationBytes()

Optional. An explanation of the recommended steps that security teams can take to resolve the detected issue. This explanation is returned with each finding generated by this module.

`string recommendation = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for recommendation.  
  
### getResourceSelector()
    
    
    public abstract CustomConfig.ResourceSelector getResourceSelector()

Optional. The Cloud Asset Inventory resource types that the custom module operates on. For information about resource types, see [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Each custom module can specify up to 5 resource types.

` .google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector resource_selector = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConfig.ResourceSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector)` | The resourceSelector.  
  
### getResourceSelectorOrBuilder()
    
    
    public abstract CustomConfig.ResourceSelectorOrBuilder getResourceSelectorOrBuilder()

Optional. The Cloud Asset Inventory resource types that the custom module operates on. For information about resource types, see [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Each custom module can specify up to 5 resource types.

` .google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector resource_selector = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConfig.ResourceSelectorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelectorOrBuilder)` |   
  
### getSeverity()
    
    
    public abstract CustomConfig.Severity getSeverity()

Optional. The severity to assign to findings generated by the module.

` .google.cloud.securitycentermanagement.v1.CustomConfig.Severity severity = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomConfig.Severity](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycentermanagement/latest/com.google.cloud.securitycentermanagement.v1.CustomConfig.Severity)` | The severity.  
  
### getSeverityValue()
    
    
    public abstract int getSeverityValue()

Optional. The severity to assign to findings generated by the module.

` .google.cloud.securitycentermanagement.v1.CustomConfig.Severity severity = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for severity.  
  
### hasCustomOutput()
    
    
    public abstract boolean hasCustomOutput()

Optional. Custom output properties.

` .google.cloud.securitycentermanagement.v1.CustomConfig.CustomOutputSpec custom_output = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the customOutput field is set.  
  
### hasPredicate()
    
    
    public abstract boolean hasPredicate()

Optional. The Common Expression Language (CEL) expression to evaluate to produce findings. When the expression evaluates to `true` against a resource, a finding is generated.

`.google.type.Expr predicate = 1 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the predicate field is set.  
  
### hasResourceSelector()
    
    
    public abstract boolean hasResourceSelector()

Optional. The Cloud Asset Inventory resource types that the custom module operates on. For information about resource types, see [Supported asset types](https://cloud.google.com/asset-inventory/docs/supported-asset-types). Each custom module can specify up to 5 resource types.

` .google.cloud.securitycentermanagement.v1.CustomConfig.ResourceSelector resource_selector = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resourceSelector field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
