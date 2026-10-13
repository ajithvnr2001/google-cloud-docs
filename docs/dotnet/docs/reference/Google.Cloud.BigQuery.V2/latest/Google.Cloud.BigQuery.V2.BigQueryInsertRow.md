---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow
title: Google BigQuery v2 API - Class BigQueryInsertRow (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:02.658110+00:00
---

# Google BigQuery v2 API - Class BigQueryInsertRow (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google BigQuery v2 API - Class BigQueryInsertRow (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BigQueryInsertRow : IEnumerable

Reference documentation and code samples for the Google BigQuery v2 API class BigQueryInsertRow.

A row used for streaming data insertion.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BigQueryInsertRow

## Implements

[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.ienumerable)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2)

## Assembly

Google.Cloud.BigQuery.V2.dll

## Remarks

This is effectively a dictionary where each key is the field name (a string) and the value is the corresponding value for that field. Supported value types: 

  * `System.Boolean`
  * `System.Int16`
  * `System.UInt16`
  * `System.Int32`
  * `System.UInt32`
  * `System.Int64`
  * `System.Float`
  * `System.Double`
  * `System.String`
  * `System.DateTime`
  * `System.DateTimeOffset`
  * `System.TimeSpan`
  * `Google.Cloud.BigQuery.V2.BigQueryNumeric`
  * `Google.Cloud.BigQuery.V2.BigQueryGeography`
  * A `Google.Cloud.BigQuery.V2.InsertRow` (for record/struct fields)
  * Any `IReadOnlyList<T>` of one of the above types (for repeated fields). This includes arrays and `List<T>` values.



Note that all integer types are stored as `System.Int64`, and all floating point types are stored as `System.Double.`

`DateTimeOffset` values are converted to UTC and treated as timestamp. The handling of `DateTime` values depends on the `Kind`: values with a `Kind` of `Local` are rejected; values with a `Kind` of `UTC` are treated as timestamps; values with a `Kind` of `Unspecified` are treated as civil datetime values. All values are stored with a precision of a microsecond. 

`TimeSpan` values must be non-negative and less than 24 hours, used to represent a time-of-day. 

Although date values are retrieved as `System.DateTime`, they must be inserted as string values, in the format "yyyy-MM-dd". 

[BigQueryInsertRow](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow) is used for record/struct fields for convenience, but only the [InsertId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow#Google_Cloud_BigQuery_V2_BigQueryInsertRow_InsertId) of the top-level row is relevant. 

Null elements within repeated fields are prohibited. This is validated client-side when the row is inserted; validating when a value is added to the row would be ineffective as the values could change before insertion. 

## Constructors 

### BigQueryInsertRow()
    
    
    public BigQueryInsertRow()

Constructs an empty row with no insert ID.

### BigQueryInsertRow(string)
    
    
    public BigQueryInsertRow(string insertId)

Constructs an empty row with the specified insert ID.

**Parameter**  
---  
**Name** | **Description**  
`insertId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Insert ID used for deduplication. May be null.  
  
## Properties 

### InsertId
    
    
    public string InsertId { get; set; }

To help ensure data consistency, you can supply an [InsertId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow#Google_Cloud_BigQuery_V2_BigQueryInsertRow_InsertId) for each inserted row. BigQuery remembers this ID for at least one minute. If you try to stream the same set of rows within that time period and the insertId property is set, BigQuery uses the property to de-duplicate your data on a best effort basis. By default if no ID is specified, one will be generated to allow de-duplicating efforts if insert operations need to be retried. You can allow empty [InsertId](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.BigQueryInsertRow#Google_Cloud_BigQuery_V2_BigQueryInsertRow_InsertId) by setting [AllowEmptyInsertIds](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.V2/latest/Google.Cloud.BigQuery.V2.InsertOptions#Google_Cloud_BigQuery_V2_InsertOptions_AllowEmptyInsertIds) to true. This will allow for faster row inserts at the expense of possible record duplication if the operation needs to be retried. See <https://cloud.google.com/bigquery/quotas#streaming_inserts> for more information.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### this[string]
    
    
    public object this[string name] { get; set; }

Accesses a field in the row by name.

**Parameter**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the field to access. Must be a valid BigQuery field name.  
**Property Value**  
---  
**Type** | **Description**  
`[object](https://learn.microsoft.com/dotnet/api/system.object)` | The value associated with `name`.  
**Exceptions**  
---  
**Type** | **Description**  
`[KeyNotFoundException](https://learn.microsoft.com/dotnet/api/system.collections.generic.keynotfoundexception)` | The row does not have a key with the given name.  
  
## Methods 

### Add(IDictionary<string, object>)
    
    
    public void Add(IDictionary<string, object> fields)

Adds all the values in the specified dictionary to the row.

**Parameter**  
---  
**Name** | **Description**  
`fields` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[object](https://learn.microsoft.com/dotnet/api/system.object)`  
The fields to add to the row. Must not be null.  
**Remarks**

This being named `Add` rather than `AddRange` allows it to be specified in a collection initializer, which can be useful to provide a set of common fields and then some extra values.

### Add(string, object)
    
    
    public void Add(string key, object value)

Adds a single field value to the row.

**Parameters**  
---  
**Name** | **Description**  
`key` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The name of the field. Must be a valid BigQuery field name.  
`value` | `[object](https://learn.microsoft.com/dotnet/api/system.object)`  
The value for the field, which must be `null` or one of the supported types.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
