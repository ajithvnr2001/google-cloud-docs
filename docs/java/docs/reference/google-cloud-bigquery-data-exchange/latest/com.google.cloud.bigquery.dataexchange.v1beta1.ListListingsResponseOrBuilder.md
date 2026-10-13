---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-data-exchange/latest/com.google.cloud.bigquery.dataexchange.v1beta1.ListListingsResponseOrBuilder
title: Interface ListListingsResponseOrBuilder (2.94.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:02.161420+00:00
---

# Interface ListListingsResponseOrBuilder (2.94.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-data-exchange/latest/com.google.cloud.bigquery.dataexchange.v1beta1.ListListingsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListListingsResponseOrBuilder (2.94.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.94.0 (latest)  2.90.0  2.89.0  2.88.0  2.86.0  2.83.0  2.82.0  2.80.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.69.0  2.68.0  2.67.0  2.65.0  2.63.0  2.62.0  2.59.0  2.58.0  2.57.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0  0.3.2  0.2.1  0.1.0 
    
    
    public interface ListListingsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getListings(int index)
    
    
    public abstract Listing getListings(int index)

The list of Listing.

`repeated .google.cloud.bigquery.dataexchange.v1beta1.Listing listings = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-data-exchange/latest/com.google.cloud.bigquery.dataexchange.v1beta1.Listing)` |   
  
### getListingsCount()
    
    
    public abstract int getListingsCount()

The list of Listing.

`repeated .google.cloud.bigquery.dataexchange.v1beta1.Listing listings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getListingsList()
    
    
    public abstract List<Listing> getListingsList()

The list of Listing.

`repeated .google.cloud.bigquery.dataexchange.v1beta1.Listing listings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Listing](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-data-exchange/latest/com.google.cloud.bigquery.dataexchange.v1beta1.Listing)>` |   
  
### getListingsOrBuilder(int index)
    
    
    public abstract ListingOrBuilder getListingsOrBuilder(int index)

The list of Listing.

`repeated .google.cloud.bigquery.dataexchange.v1beta1.Listing listings = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ListingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery-data-exchange/latest/com.google.cloud.bigquery.dataexchange.v1beta1.ListingOrBuilder)` |   
  
### getListingsOrBuilderList()
    
    
    public abstract List<? extends ListingOrBuilder> getListingsOrBuilderList()

The list of Listing.

`repeated .google.cloud.bigquery.dataexchange.v1beta1.Listing listings = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.dataexchange.v1beta1.ListingOrBuilder>` |   
  
### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token to request the next page of results.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token to request the next page of results.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
