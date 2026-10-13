---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesResponseOrBuilder
title: Interface ListExternalAddressesResponseOrBuilder (0.93.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:32.723893+00:00
---

# Interface ListExternalAddressesResponseOrBuilder (0.93.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ListExternalAddressesResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListExternalAddressesResponseOrBuilder (0.93.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.93.0 (latest)  0.89.0  0.88.0  0.87.0  0.85.0  0.82.0  0.81.0  0.79.0  0.77.0  0.76.0  0.74.0  0.72.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.64.0  0.62.0  0.61.0  0.58.0  0.57.0  0.56.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ListExternalAddressesResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExternalAddresses(int index)
    
    
    public abstract ExternalAddress getExternalAddresses(int index)

A list of external IP addresses.

`repeated .google.cloud.vmwareengine.v1.ExternalAddress external_addresses = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)` |   
  
### getExternalAddressesCount()
    
    
    public abstract int getExternalAddressesCount()

A list of external IP addresses.

`repeated .google.cloud.vmwareengine.v1.ExternalAddress external_addresses = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getExternalAddressesList()
    
    
    public abstract List<ExternalAddress> getExternalAddressesList()

A list of external IP addresses.

`repeated .google.cloud.vmwareengine.v1.ExternalAddress external_addresses = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExternalAddress](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddress)>` |   
  
### getExternalAddressesOrBuilder(int index)
    
    
    public abstract ExternalAddressOrBuilder getExternalAddressesOrBuilder(int index)

A list of external IP addresses.

`repeated .google.cloud.vmwareengine.v1.ExternalAddress external_addresses = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExternalAddressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-vmwareengine/latest/com.google.cloud.vmwareengine.v1.ExternalAddressOrBuilder)` |   
  
### getExternalAddressesOrBuilderList()
    
    
    public abstract List<? extends ExternalAddressOrBuilder> getExternalAddressesOrBuilderList()

A list of external IP addresses.

`repeated .google.cloud.vmwareengine.v1.ExternalAddress external_addresses = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.vmwareengine.v1.ExternalAddressOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getUnreachable(int index)
    
    
    public abstract String getUnreachable(int index)

Locations that could not be reached when making an aggregated query using wildcards.

`repeated string unreachable = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unreachable at the given index.  
  
### getUnreachableBytes(int index)
    
    
    public abstract ByteString getUnreachableBytes(int index)

Locations that could not be reached when making an aggregated query using wildcards.

`repeated string unreachable = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the unreachable at the given index.  
  
### getUnreachableCount()
    
    
    public abstract int getUnreachableCount()

Locations that could not be reached when making an aggregated query using wildcards.

`repeated string unreachable = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of unreachable.  
  
### getUnreachableList()
    
    
    public abstract List<String> getUnreachableList()

Locations that could not be reached when making an aggregated query using wildcards.

`repeated string unreachable = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the unreachable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
