---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductOrBuilder
title: Interface LogicalProductOrBuilder (0.5.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:43.579561+00:00
---

# Interface LogicalProductOrBuilder (0.5.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LogicalProductOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface LogicalProductOrBuilder (0.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.5.0 (latest)  0.1.0 
    
    
    public interface LogicalProductOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getLifecycleState()
    
    
    public abstract LifecycleState getLifecycleState()

Output only. Current Lifecycle state of the logical product.

` .google.cloud.productregistry.v1.LifecycleState lifecycle_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[LifecycleState](https://docs.cloud.google.com/java/docs/reference/google-cloud-productregistry/latest/com.google.cloud.productregistry.v1.LifecycleState)` | The lifecycleState.  
  
### getLifecycleStateValue()
    
    
    public abstract int getLifecycleStateValue()

Output only. Current Lifecycle state of the logical product.

` .google.cloud.productregistry.v1.LifecycleState lifecycle_state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for lifecycleState.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the LogicalProduct. Format: logicalProducts/{logical_product}.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the LogicalProduct. Format: logicalProducts/{logical_product}.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getProductSuite()
    
    
    public abstract String getProductSuite()

Product suite associated with the logical product. Format: productSuites/{product_suite}.

`string product_suite = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The productSuite.  
  
### getProductSuiteBytes()
    
    
    public abstract ByteString getProductSuiteBytes()

Product suite associated with the logical product. Format: productSuites/{product_suite}.

`string product_suite = 3 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for productSuite.  
  
### getReplaced()
    
    
    public abstract boolean getReplaced()

Output only. Indicates whether the logical product has been replaced. If `false`, the product is active. If `true`, the product has been replaced by another type, and the `replacement` field contains the resource name of that replacement.

`bool replaced = 6 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The replaced.  
  
### getReplacement()
    
    
    public abstract String getReplacement()

Output only. The resource name of the Logical Entity that the logical product is replaced by. This field is only populated when this logical product is replaced by some other type. Eg: logicalProducts/{logical_product}/variants/{variant}, productSuites/{product_suite}, etc.

` string replacement = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The replacement.  
  
### getReplacementBytes()
    
    
    public abstract ByteString getReplacementBytes()

Output only. The resource name of the Logical Entity that the logical product is replaced by. This field is only populated when this logical product is replaced by some other type. Eg: logicalProducts/{logical_product}/variants/{variant}, productSuites/{product_suite}, etc.

` string replacement = 7 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for replacement.  
  
### getTitle()
    
    
    public abstract String getTitle()

Display name of the LogicalProduct.

`string title = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The title.  
  
### getTitleBytes()
    
    
    public abstract ByteString getTitleBytes()

Display name of the LogicalProduct.

`string title = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for title.  
  
### getVariants(int index)
    
    
    public abstract String getVariants(int index)

Output only. Child variant resource references. Format: logicalProducts/{logical_product}/variants/{variant}

` repeated string variants = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The variants at the given index.  
  
### getVariantsBytes(int index)
    
    
    public abstract ByteString getVariantsBytes(int index)

Output only. Child variant resource references. Format: logicalProducts/{logical_product}/variants/{variant}

` repeated string variants = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the variants at the given index.  
  
### getVariantsCount()
    
    
    public abstract int getVariantsCount()

Output only. Child variant resource references. Format: logicalProducts/{logical_product}/variants/{variant}

` repeated string variants = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of variants.  
  
### getVariantsList()
    
    
    public abstract List<String> getVariantsList()

Output only. Child variant resource references. Format: logicalProducts/{logical_product}/variants/{variant}

` repeated string variants = 4 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the variants.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
