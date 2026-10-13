---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRoutesListOrBuilder
title: Interface ExchangedPeeringRoutesListOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:19:59.192349+00:00
---

# Interface ExchangedPeeringRoutesListOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRoutesListOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ExchangedPeeringRoutesListOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface ExchangedPeeringRoutesListOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getId()
    
    
    public abstract String getId()

[Output Only] Unique identifier for the resource; defined by the server.

`optional string id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

[Output Only] Unique identifier for the resource; defined by the server.

`optional string id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getItems(int index)
    
    
    public abstract ExchangedPeeringRoute getItems(int index)

A list of ExchangedPeeringRoute resources.

`repeated .google.cloud.compute.v1.ExchangedPeeringRoute items = 100526016;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExchangedPeeringRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRoute)` |   
  
### getItemsCount()
    
    
    public abstract int getItemsCount()

A list of ExchangedPeeringRoute resources.

`repeated .google.cloud.compute.v1.ExchangedPeeringRoute items = 100526016;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getItemsList()
    
    
    public abstract List<ExchangedPeeringRoute> getItemsList()

A list of ExchangedPeeringRoute resources.

`repeated .google.cloud.compute.v1.ExchangedPeeringRoute items = 100526016;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ExchangedPeeringRoute](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRoute)>` |   
  
### getItemsOrBuilder(int index)
    
    
    public abstract ExchangedPeeringRouteOrBuilder getItemsOrBuilder(int index)

A list of ExchangedPeeringRoute resources.

`repeated .google.cloud.compute.v1.ExchangedPeeringRoute items = 100526016;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ExchangedPeeringRouteOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.ExchangedPeeringRouteOrBuilder)` |   
  
### getItemsOrBuilderList()
    
    
    public abstract List<? extends ExchangedPeeringRouteOrBuilder> getItemsOrBuilderList()

A list of ExchangedPeeringRoute resources.

`repeated .google.cloud.compute.v1.ExchangedPeeringRoute items = 100526016;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.ExchangedPeeringRouteOrBuilder>` |   
  
### getKind()
    
    
    public abstract String getKind()

Output only. [Output Only] Type of resource. Alwayscompute#exchangedPeeringRoutesList for exchanged peering routes lists.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The kind.  
  
### getKindBytes()
    
    
    public abstract ByteString getKindBytes()

Output only. [Output Only] Type of resource. Alwayscompute#exchangedPeeringRoutesList for exchanged peering routes lists.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for kind.  
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

[Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results.

`optional string next_page_token = 79797525;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

[Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results.

`optional string next_page_token = 79797525;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getSelfLink()
    
    
    public abstract String getSelfLink()

Output only. [Output Only] Server-defined URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The selfLink.  
  
### getSelfLinkBytes()
    
    
    public abstract ByteString getSelfLinkBytes()

Output only. [Output Only] Server-defined URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for selfLink.  
  
### getWarning()
    
    
    public abstract Warning getWarning()

[Output Only] Informational warning message.

`optional .google.cloud.compute.v1.Warning warning = 50704284;`

**Returns**  
---  
**Type** | **Description**  
`[Warning](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.Warning)` | The warning.  
  
### getWarningOrBuilder()
    
    
    public abstract WarningOrBuilder getWarningOrBuilder()

[Output Only] Informational warning message.

`optional .google.cloud.compute.v1.Warning warning = 50704284;`

**Returns**  
---  
**Type** | **Description**  
`[WarningOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.WarningOrBuilder)` |   
  
### hasId()
    
    
    public abstract boolean hasId()

[Output Only] Unique identifier for the resource; defined by the server.

`optional string id = 3355;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the id field is set.  
  
### hasKind()
    
    
    public abstract boolean hasKind()

Output only. [Output Only] Type of resource. Alwayscompute#exchangedPeeringRoutesList for exchanged peering routes lists.

`optional string kind = 3292052;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the kind field is set.  
  
### hasNextPageToken()
    
    
    public abstract boolean hasNextPageToken()

[Output Only] This token allows you to get the next page of results for list requests. If the number of results is larger thanmaxResults, use the nextPageToken as a value for the query parameter pageToken in the next list request. Subsequent list requests will have their own nextPageToken to continue paging through the results.

`optional string next_page_token = 79797525;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the nextPageToken field is set.  
  
### hasSelfLink()
    
    
    public abstract boolean hasSelfLink()

Output only. [Output Only] Server-defined URL for this resource.

`optional string self_link = 456214797;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the selfLink field is set.  
  
### hasWarning()
    
    
    public abstract boolean hasWarning()

[Output Only] Informational warning message.

`optional .google.cloud.compute.v1.Warning warning = 50704284;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the warning field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
