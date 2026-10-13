---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.TransitTableOrBuilder
title: Interface TransitTableOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:55.281455+00:00
---

# Interface TransitTableOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.TransitTableOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransitTableOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface TransitTableOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getPostalCodeGroupNames(int index)
    
    
    public abstract String getPostalCodeGroupNames(int index)

Required. A list of region names Region.name . The last value can be `"all other locations"`. Example: `["zone 1", "zone 2", "all other locations"]`. The referred postal code groups must match the delivery country of the service.

`repeated string postal_code_group_names = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The postalCodeGroupNames at the given index.  
  
### getPostalCodeGroupNamesBytes(int index)
    
    
    public abstract ByteString getPostalCodeGroupNamesBytes(int index)

Required. A list of region names Region.name . The last value can be `"all other locations"`. Example: `["zone 1", "zone 2", "all other locations"]`. The referred postal code groups must match the delivery country of the service.

`repeated string postal_code_group_names = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the postalCodeGroupNames at the given index.  
  
### getPostalCodeGroupNamesCount()
    
    
    public abstract int getPostalCodeGroupNamesCount()

Required. A list of region names Region.name . The last value can be `"all other locations"`. Example: `["zone 1", "zone 2", "all other locations"]`. The referred postal code groups must match the delivery country of the service.

`repeated string postal_code_group_names = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of postalCodeGroupNames.  
  
### getPostalCodeGroupNamesList()
    
    
    public abstract List<String> getPostalCodeGroupNamesList()

Required. A list of region names Region.name . The last value can be `"all other locations"`. Example: `["zone 1", "zone 2", "all other locations"]`. The referred postal code groups must match the delivery country of the service.

`repeated string postal_code_group_names = 1 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the postalCodeGroupNames.  
  
### getRows(int index)
    
    
    public abstract TransitTable.TransitTimeRow getRows(int index)

Required. If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

` repeated .google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow rows = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransitTable.TransitTimeRow](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow)` |   
  
### getRowsCount()
    
    
    public abstract int getRowsCount()

Required. If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

` repeated .google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow rows = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRowsList()
    
    
    public abstract List<TransitTable.TransitTimeRow> getRowsList()

Required. If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

` repeated .google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow rows = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TransitTimeRow](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow)>` |   
  
### getRowsOrBuilder(int index)
    
    
    public abstract TransitTable.TransitTimeRowOrBuilder getRowsOrBuilder(int index)

Required. If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

` repeated .google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow rows = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TransitTable.TransitTimeRowOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRowOrBuilder)` |   
  
### getRowsOrBuilderList()
    
    
    public abstract List<? extends TransitTable.TransitTimeRowOrBuilder> getRowsOrBuilderList()

Required. If there's only one dimension set of `postal_code_group_names` or `transit_time_labels`, there are multiple rows each with one value for that dimension. If there are two dimensions, each row corresponds to a `postal_code_group_names`, and columns (values) to a `transit_time_labels`.

` repeated .google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRow rows = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.shopping.merchant.accounts.v1beta.TransitTable.TransitTimeRowOrBuilder>` |   
  
### getTransitTimeLabels(int index)
    
    
    public abstract String getTransitTimeLabels(int index)

Required. A list of transit time labels. The last value can be `"all other labels"`. Example: `["food", "electronics", "all other labels"]`.

`repeated string transit_time_labels = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The transitTimeLabels at the given index.  
  
### getTransitTimeLabelsBytes(int index)
    
    
    public abstract ByteString getTransitTimeLabelsBytes(int index)

Required. A list of transit time labels. The last value can be `"all other labels"`. Example: `["food", "electronics", "all other labels"]`.

`repeated string transit_time_labels = 2 [(.google.api.field_behavior) = REQUIRED];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the transitTimeLabels at the given index.  
  
### getTransitTimeLabelsCount()
    
    
    public abstract int getTransitTimeLabelsCount()

Required. A list of transit time labels. The last value can be `"all other labels"`. Example: `["food", "electronics", "all other labels"]`.

`repeated string transit_time_labels = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of transitTimeLabels.  
  
### getTransitTimeLabelsList()
    
    
    public abstract List<String> getTransitTimeLabelsList()

Required. A list of transit time labels. The last value can be `"all other labels"`. Example: `["food", "electronics", "all other labels"]`.

`repeated string transit_time_labels = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the transitTimeLabels.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
