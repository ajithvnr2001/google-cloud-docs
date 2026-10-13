---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.TableExtensions
title: Google BigQuery v2 API - Class TableExtensions (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:10.421330+00:00
---

# Google BigQuery v2 API - Class TableExtensions (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.TableExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class TableExtensions (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public static class TableExtensions

Reference documentation and code samples for the Google BigQuery v2 API class TableExtensions.

Extension methods for making it easier to work with [Table](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Table.html)

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TableExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Methods 

### GetExpirationTime(Table)
    
    
    public static DateTimeOffset? GetExpirationTime(this Table table)

Gets the time at which this table expires, at which point it will be deleted.

**Parameter**  
---  
**Name** | **Description**  
`table` | `[Table](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Table.html)`  
The table for which to set the expiration for. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset)` |   
  
### SetExpirationTime(Table, DateTimeOffset?)
    
    
    public static Table SetExpirationTime(this Table table, DateTimeOffset? expiration)

Sets the time at which this table expires, at which point it will be deleted. If this is not set and the dataset does not have a default expiration period, the table will persist until it is deleted.

**Parameters**  
---  
**Name** | **Description**  
`table` | `[Table](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Table.html)`  
The table for which to set the expiration for. Must not be null.  
`expiration` | `[DateTimeOffset](https://learn.microsoft.com/dotnet/api/system.datetimeoffset)`  
The new expiration to be set.  
**Returns**  
---  
**Type** | **Description**  
`[Table](https://googleapis.dev/dotnet/Google.Apis.Bigquery.v2/1.74.0.4090/api/Google.Apis.Bigquery.v2.Data.Table.html)` | The same table on which the change was made. To facilitate method chaining.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
