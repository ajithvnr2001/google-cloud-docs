---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.InputField.TextInputOrBuilder
title: Interface InputField.TextInputOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:18:24.945652+00:00
---

# Interface InputField.TextInputOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.InputField.TextInputOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface InputField.TextInputOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.9.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public static interface InputField.TextInputOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdditionalInfo()
    
    
    public abstract TextWithTooltip getAdditionalInfo()

Additional info regarding the field to be displayed to the business. For example, warning to not include personal identifiable information. There may be more information to be shown in a tooltip.

` optional .google.shopping.merchant.issueresolution.v1.TextWithTooltip additional_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[TextWithTooltip](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.TextWithTooltip)` | The additionalInfo.  
  
### getAdditionalInfoOrBuilder()
    
    
    public abstract TextWithTooltipOrBuilder getAdditionalInfoOrBuilder()

Additional info regarding the field to be displayed to the business. For example, warning to not include personal identifiable information. There may be more information to be shown in a tooltip.

` optional .google.shopping.merchant.issueresolution.v1.TextWithTooltip additional_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[TextWithTooltipOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.TextWithTooltipOrBuilder)` |   
  
### getAriaLabel()
    
    
    public abstract String getAriaLabel()

Text to be used as the [aria-label](https://www.w3.org/TR/WCAG20-TECHS/ARIA14.html) for the input.

`optional string aria_label = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ariaLabel.  
  
### getAriaLabelBytes()
    
    
    public abstract ByteString getAriaLabelBytes()

Text to be used as the [aria-label](https://www.w3.org/TR/WCAG20-TECHS/ARIA14.html) for the input.

`optional string aria_label = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ariaLabel.  
  
### getFormatInfo()
    
    
    public abstract String getFormatInfo()

Information about the required format. If present, it should be shown close to the input field to help the business to provide a correct value. For example: "VAT numbers should be in a format similar to SK9999999999"

`optional string format_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The formatInfo.  
  
### getFormatInfoBytes()
    
    
    public abstract ByteString getFormatInfoBytes()

Information about the required format. If present, it should be shown close to the input field to help the business to provide a correct value. For example: "VAT numbers should be in a format similar to SK9999999999"

`optional string format_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for formatInfo.  
  
### getType()
    
    
    public abstract InputField.TextInput.TextInputType getType()

Type of the text input

` .google.shopping.merchant.issueresolution.v1.InputField.TextInput.TextInputType type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[InputField.TextInput.TextInputType](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-issue-resolution/latest/com.google.shopping.merchant.issueresolution.v1.InputField.TextInput.TextInputType)` | The type.  
  
### getTypeValue()
    
    
    public abstract int getTypeValue()

Type of the text input

` .google.shopping.merchant.issueresolution.v1.InputField.TextInput.TextInputType type = 1; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for type.  
  
### hasAdditionalInfo()
    
    
    public abstract boolean hasAdditionalInfo()

Additional info regarding the field to be displayed to the business. For example, warning to not include personal identifiable information. There may be more information to be shown in a tooltip.

` optional .google.shopping.merchant.issueresolution.v1.TextWithTooltip additional_info = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the additionalInfo field is set.  
  
### hasAriaLabel()
    
    
    public abstract boolean hasAriaLabel()

Text to be used as the [aria-label](https://www.w3.org/TR/WCAG20-TECHS/ARIA14.html) for the input.

`optional string aria_label = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ariaLabel field is set.  
  
### hasFormatInfo()
    
    
    public abstract boolean hasFormatInfo()

Information about the required format. If present, it should be shown close to the input field to help the business to provide a correct value. For example: "VAT numbers should be in a format similar to SK9999999999"

`optional string format_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the formatInfo field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
