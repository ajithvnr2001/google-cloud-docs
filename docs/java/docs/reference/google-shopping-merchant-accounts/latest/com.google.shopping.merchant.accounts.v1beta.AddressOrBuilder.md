---
url: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.AddressOrBuilder
title: Interface AddressOrBuilder (1.27.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:23.999396+00:00
---

# Interface AddressOrBuilder (1.27.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-shopping-merchant-accounts/latest/com.google.shopping.merchant.accounts.v1beta.AddressOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AddressOrBuilder (1.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.27.0 (latest)  1.23.0  1.22.0  1.21.0  1.19.0  1.16.0  1.15.0  1.13.0  1.11.0  1.10.0  1.8.0  1.6.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.26.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface AddressOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAdministrativeArea()
    
    
    public abstract String getAdministrativeArea()

Required. Top-level administrative subdivision of the country. For example, a state like California ("CA") or a province like Quebec ("QC").

`optional string administrative_area = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The administrativeArea.  
  
### getAdministrativeAreaBytes()
    
    
    public abstract ByteString getAdministrativeAreaBytes()

Required. Top-level administrative subdivision of the country. For example, a state like California ("CA") or a province like Quebec ("QC").

`optional string administrative_area = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for administrativeArea.  
  
### getCity()
    
    
    public abstract String getCity()

Required. City, town or commune. May also include dependent localities or sublocalities (For example neighborhoods or suburbs).

`optional string city = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The city.  
  
### getCityBytes()
    
    
    public abstract ByteString getCityBytes()

Required. City, town or commune. May also include dependent localities or sublocalities (For example neighborhoods or suburbs).

`optional string city = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for city.  
  
### getPostalCode()
    
    
    public abstract String getPostalCode()

Required. Postal code or ZIP (For example "94043").

`optional string postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The postalCode.  
  
### getPostalCodeBytes()
    
    
    public abstract ByteString getPostalCodeBytes()

Required. Postal code or ZIP (For example "94043").

`optional string postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for postalCode.  
  
### getRegionCode()
    
    
    public abstract String getRegionCode()

Required. [CLDR country code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) (For example "US").

`optional string region_code = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The regionCode.  
  
### getRegionCodeBytes()
    
    
    public abstract ByteString getRegionCodeBytes()

Required. [CLDR country code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) (For example "US").

`optional string region_code = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for regionCode.  
  
### getStreetAddress()
    
    
    public abstract String getStreetAddress()

Street-level part of the address. For example: `111w 31st Street`.

`optional string street_address = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The streetAddress.  
  
### getStreetAddressBytes()
    
    
    public abstract ByteString getStreetAddressBytes()

Street-level part of the address. For example: `111w 31st Street`.

`optional string street_address = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for streetAddress.  
  
### hasAdministrativeArea()
    
    
    public abstract boolean hasAdministrativeArea()

Required. Top-level administrative subdivision of the country. For example, a state like California ("CA") or a province like Quebec ("QC").

`optional string administrative_area = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the administrativeArea field is set.  
  
### hasCity()
    
    
    public abstract boolean hasCity()

Required. City, town or commune. May also include dependent localities or sublocalities (For example neighborhoods or suburbs).

`optional string city = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the city field is set.  
  
### hasPostalCode()
    
    
    public abstract boolean hasPostalCode()

Required. Postal code or ZIP (For example "94043").

`optional string postal_code = 4 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the postalCode field is set.  
  
### hasRegionCode()
    
    
    public abstract boolean hasRegionCode()

Required. [CLDR country code](http://www.unicode.org/repos/cldr/tags/latest/common/main/en.xml) (For example "US").

`optional string region_code = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the regionCode field is set.  
  
### hasStreetAddress()
    
    
    public abstract boolean hasStreetAddress()

Street-level part of the address. For example: `111w 31st Street`.

`optional string street_address = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the streetAddress field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
