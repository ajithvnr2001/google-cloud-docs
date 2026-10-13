---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.RegionOrBuilder
title: Interface RegionOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:36.092043+00:00
---

# Interface RegionOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.RegionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RegionOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface RegionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDisplayName()
    
    
    public abstract String getDisplayName()

Optional. The display name of the region.

`optional string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Optional. The display name of the region.

`optional string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getGeotargetArea()
    
    
    public abstract Region.GeoTargetArea getGeotargetArea()

Optional. A list of geotargets that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.GeoTargetArea geotarget_area = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Region.GeoTargetArea](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Region.GeoTargetArea)` | The geotargetArea.  
  
### getGeotargetAreaOrBuilder()
    
    
    public abstract Region.GeoTargetAreaOrBuilder getGeotargetAreaOrBuilder()

Optional. A list of geotargets that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.GeoTargetArea geotarget_area = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Region.GeoTargetAreaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Region.GeoTargetAreaOrBuilder)` |   
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name of the region. Format: `accounts/{account}/regions/{region}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name of the region. Format: `accounts/{account}/regions/{region}`

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPostalCodeArea()
    
    
    public abstract Region.PostalCodeArea getPostalCodeArea()

Optional. A list of postal codes that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.PostalCodeArea postal_code_area = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Region.PostalCodeArea](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Region.PostalCodeArea)` | The postalCodeArea.  
  
### getPostalCodeAreaOrBuilder()
    
    
    public abstract Region.PostalCodeAreaOrBuilder getPostalCodeAreaOrBuilder()

Optional. A list of postal codes that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.PostalCodeArea postal_code_area = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Region.PostalCodeAreaOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.Region.PostalCodeAreaOrBuilder)` |   
  
### getRegionalInventoryEligible()
    
    
    public abstract BoolValue getRegionalInventoryEligible()

Output only. Indicates if the region is eligible for use in the Regional Inventory configuration.

` .google.protobuf.BoolValue regional_inventory_eligible = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The regionalInventoryEligible.  
  
### getRegionalInventoryEligibleOrBuilder()
    
    
    public abstract BoolValueOrBuilder getRegionalInventoryEligibleOrBuilder()

Output only. Indicates if the region is eligible for use in the Regional Inventory configuration.

` .google.protobuf.BoolValue regional_inventory_eligible = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### getShippingEligible()
    
    
    public abstract BoolValue getShippingEligible()

Output only. Indicates if the region is eligible for use in the Shipping Services configuration.

` .google.protobuf.BoolValue shipping_eligible = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValue](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValue.html)` | The shippingEligible.  
  
### getShippingEligibleOrBuilder()
    
    
    public abstract BoolValueOrBuilder getShippingEligibleOrBuilder()

Output only. Indicates if the region is eligible for use in the Shipping Services configuration.

` .google.protobuf.BoolValue shipping_eligible = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[BoolValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.BoolValueOrBuilder.html)` |   
  
### hasDisplayName()
    
    
    public abstract boolean hasDisplayName()

Optional. The display name of the region.

`optional string display_name = 2 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the displayName field is set.  
  
### hasGeotargetArea()
    
    
    public abstract boolean hasGeotargetArea()

Optional. A list of geotargets that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.GeoTargetArea geotarget_area = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the geotargetArea field is set.  
  
### hasPostalCodeArea()
    
    
    public abstract boolean hasPostalCodeArea()

Optional. A list of postal codes that defines the region area.

` .google.shopping.merchant.accounts.v1beta.Region.PostalCodeArea postal_code_area = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postalCodeArea field is set.  
  
### hasRegionalInventoryEligible()
    
    
    public abstract boolean hasRegionalInventoryEligible()

Output only. Indicates if the region is eligible for use in the Regional Inventory configuration.

` .google.protobuf.BoolValue regional_inventory_eligible = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the regionalInventoryEligible field is set.  
  
### hasShippingEligible()
    
    
    public abstract boolean hasShippingEligible()

Output only. Indicates if the region is eligible for use in the Shipping Services configuration.

` .google.protobuf.BoolValue shipping_eligible = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the shippingEligible field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
