---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInputOrBuilder
title: Interface InputField.ChoiceInputOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:54.282503+00:00
---

# Interface InputField.ChoiceInputOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInputOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InputField.ChoiceInputOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface InputField.ChoiceInputOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getOptions(int index)
    
    
    public abstract InputField.ChoiceInput.ChoiceInputOption getOptions(int index)

A list of choices. Only one option can be selected.

` repeated .google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption options = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputField.ChoiceInput.ChoiceInputOption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption)` |   
  
### getOptionsCount()
    
    
    public abstract int getOptionsCount()

A list of choices. Only one option can be selected.

` repeated .google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption options = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOptionsList()
    
    
    public abstract List<InputField.ChoiceInput.ChoiceInputOption> getOptionsList()

A list of choices. Only one option can be selected.

` repeated .google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption options = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ChoiceInputOption](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption)>` |   
  
### getOptionsOrBuilder(int index)
    
    
    public abstract InputField.ChoiceInput.ChoiceInputOptionOrBuilder getOptionsOrBuilder(int index)

A list of choices. Only one option can be selected.

` repeated .google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption options = 1; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[InputField.ChoiceInput.ChoiceInputOptionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOptionOrBuilder)` |   
  
### getOptionsOrBuilderList()
    
    
    public abstract List<? extends InputField.ChoiceInput.ChoiceInputOptionOrBuilder> getOptionsOrBuilderList()

A list of choices. Only one option can be selected.

` repeated .google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOption options = 1; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.issueresolution.v1beta.InputField.ChoiceInput.ChoiceInputOptionOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
