---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ParameterSubstitutionRuleOrBuilder
title: Interface ParameterSubstitutionRuleOrBuilder (0.26.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:21:49.635408+00:00
---

# Interface ParameterSubstitutionRuleOrBuilder (0.26.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ParameterSubstitutionRuleOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ParameterSubstitutionRuleOrBuilder (0.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.26.0 (latest)  0.22.0  0.21.0  0.20.0  0.18.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ParameterSubstitutionRuleOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAttributeSubstitutionRule()
    
    
    public abstract AttributeSubstitutionRule getAttributeSubstitutionRule()

The attribute substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.AttributeSubstitutionRule attribute_substitution_rule = 2; `

**Returns**  
---  
**Type** | **Description**  
`[AttributeSubstitutionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AttributeSubstitutionRule)` | The attributeSubstitutionRule.  
  
### getAttributeSubstitutionRuleOrBuilder()
    
    
    public abstract AttributeSubstitutionRuleOrBuilder getAttributeSubstitutionRuleOrBuilder()

The attribute substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.AttributeSubstitutionRule attribute_substitution_rule = 2; `

**Returns**  
---  
**Type** | **Description**  
`[AttributeSubstitutionRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.AttributeSubstitutionRuleOrBuilder)` |   
  
### getPlaceholderSubstitutionRule()
    
    
    public abstract PlaceholderSubstitutionRule getPlaceholderSubstitutionRule()

The placeholder substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.PlaceholderSubstitutionRule placeholder_substitution_rule = 1; `

**Returns**  
---  
**Type** | **Description**  
`[PlaceholderSubstitutionRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.PlaceholderSubstitutionRule)` | The placeholderSubstitutionRule.  
  
### getPlaceholderSubstitutionRuleOrBuilder()
    
    
    public abstract PlaceholderSubstitutionRuleOrBuilder getPlaceholderSubstitutionRuleOrBuilder()

The placeholder substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.PlaceholderSubstitutionRule placeholder_substitution_rule = 1; `

**Returns**  
---  
**Type** | **Description**  
`[PlaceholderSubstitutionRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.PlaceholderSubstitutionRuleOrBuilder)` |   
  
### getSubstitutionTypeCase()
    
    
    public abstract ParameterSubstitutionRule.SubstitutionTypeCase getSubstitutionTypeCase()

**Returns**  
---  
**Type** | **Description**  
`[ParameterSubstitutionRule.SubstitutionTypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudsecuritycompliance/latest/com.google.cloud.cloudsecuritycompliance.v1.ParameterSubstitutionRule.SubstitutionTypeCase)` |   
  
### hasAttributeSubstitutionRule()
    
    
    public abstract boolean hasAttributeSubstitutionRule()

The attribute substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.AttributeSubstitutionRule attribute_substitution_rule = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the attributeSubstitutionRule field is set.  
  
### hasPlaceholderSubstitutionRule()
    
    
    public abstract boolean hasPlaceholderSubstitutionRule()

The placeholder substitution rule.

` .google.cloud.cloudsecuritycompliance.v1.PlaceholderSubstitutionRule placeholder_substitution_rule = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the placeholderSubstitutionRule field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
