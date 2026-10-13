---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters
title: Google Bigtable v2 API - Class RowFilters (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:06.636420+00:00
---

# Google Bigtable v2 API - Class RowFilters (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class RowFilters (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public static class RowFilters

Reference documentation and code samples for the Google Bigtable v2 API class RowFilters.

Static class with convenience methods for creating various kinds of [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instances.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RowFilters

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Methods 

### BlockAllFilter()
    
    
    public static RowFilter BlockAllFilter()

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which does not match any cells, regardless of input. Useful for temporarily disabling just part of a filter.

**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### CellsPerColumnLimit(int)
    
    
    public static RowFilter CellsPerColumnLimit(int limit)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only the most recent N cells within each column.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The maximum number of cells allowed per column.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

For example, if N=2, this filter would match column `foo:bar` at timestamps 10 and 9, skip all earlier cells in `foo:bar`, and then begin matching again in column `foo:bar2`. 

If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately. 

### CellsPerRowLimit(int)
    
    
    public static RowFilter CellsPerRowLimit(int limit)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only the first N cells of each row.

**Parameter**  
---  
**Name** | **Description**  
`limit` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The maximum number of cells allowed per row.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately. 

### CellsPerRowOffset(int)
    
    
    public static RowFilter CellsPerRowOffset(int offset)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which skips the first N cells of each row, matching all subsequent cells.

**Parameter**  
---  
**Name** | **Description**  
`offset` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The number of cells to skip per row.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately. 

### Chain(params RowFilter[])
    
    
    public static RowFilter Chain(params RowFilter[] filters)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which sends rows through several RowFilters in sequence.

**Parameter**  
---  
**Name** | **Description**  
`filters` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The elements of "filters" are chained together to process the input row: in row -> f(0) -> intermediate row -> f(1) -> ... -> f(N) -> out row The full chain is executed atomically. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### ColumnQualifierExact(BigtableByteString)
    
    
    public static RowFilter ColumnQualifierExact(BigtableByteString value)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from columns whose qualifiers match the exact byte string specified.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exact value used to match column qualifiers.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `value` can be specified using a string as well and its UTF-8 representations will be used. 

### ColumnQualifierRegex(string)
    
    
    public static RowFilter ColumnQualifierRegex(string regex)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from columns whose qualifiers satisfy the given RE2 regex.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The RE2 regex used to match column qualifiers.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

The format of RE2 is documented at <https://github.com/google/re2/wiki/Syntax>. 

Note that, since column qualifiers can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary qualifier. 

### ColumnRange(ColumnRange)
    
    
    public static RowFilter ColumnRange(ColumnRange range)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from columns within the given range.

**Parameter**  
---  
**Name** | **Description**  
`range` | `[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)`  
The range of columns from which cells should be matched. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### Condition(RowFilter, RowFilter, RowFilter)
    
    
    public static RowFilter Condition(RowFilter predicateFilter, RowFilter trueFilter, RowFilter falseFilter)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which applies one of two possible RowFilters to the data based on the output of a predicate RowFilter.

**Parameters**  
---  
**Name** | **Description**  
`predicateFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
If `predicateFilter` outputs any cells, then `trueFilter` will be evaluated on the input row. Otherwise, `falseFilter` will be evaluated.  
`trueFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to apply to the input row if `predicateFilter` returns any results. If null, no results will be returned in the true case.  
`falseFilter` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filter to apply to the input row if `predicateFilter` does not return any results. If null, no results will be returned in the false case.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### FamilyNameExact(string)
    
    
    public static RowFilter FamilyNameExact(string value)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from column families whose names match the exact string specified.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The exact value used to match column families. Must not be null  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `value` can be specified using a string as well and its UTF-8 representations will be used. 

### FamilyNameRegex(string)
    
    
    public static RowFilter FamilyNameRegex(string regex)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from columns whose families satisfy the given RE2 regex.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The RE2 regex used to match column families. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

For technical reasons, the regex must not contain the `:` character, even if it is not being used as a literal. Note that, since column families cannot contain the new line character `\n`, it is sufficient to use `.` as a full wildcard when matching column family names. 

### Interleave(params RowFilter[])
    
    
    public static RowFilter Interleave(params RowFilter[] filters)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which applies several RowFilters to the data in parallel and combines the results.

**Parameter**  
---  
**Name** | **Description**  
`filters` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
The filters to apply in parallel. Must not be null, or contain null elements.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### PassAllFilter()
    
    
    public static RowFilter PassAllFilter()

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches all cells, regardless of input. Functionally equivalent to leaving `filter` unset, but included for completeness.

**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### RowKeyExact(BigtableByteString)
    
    
    public static RowFilter RowKeyExact(BigtableByteString value)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from rows whose keys match the exact byte string specified.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exact value used to match row keys.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `value` can be specified using a string as well and its UTF-8 representations will be used. 

### RowKeyRegex(string)
    
    
    public static RowFilter RowKeyRegex(string regex)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells from rows whose keys satisfy the given RE2 regex. In other words, passes through the entire row when the key matches, and otherwise produces an empty row.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The RE2 regex used to match row keys.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

The format of RE2 is documented at <https://github.com/google/re2/wiki/Syntax>. 

Note that, since row keys can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary key. 

### RowSample(double)
    
    
    public static RowFilter RowSample(double probability)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches all cells from a row with probability p, and matches no cells from the row with probability 1-p.

**Parameter**  
---  
**Name** | **Description**  
`probability` | `[double](https://learn.microsoft.com/dotnet/api/system.double)`  
The probability with which rows should be matched. Must be between 0 and 1, inclusive.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### StripValueTransformer()
    
    
    public static RowFilter StripValueTransformer()

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which replaces each cell's value with the empty string. This is useful for increasing performance when only getting cell counts rather than cell values.

**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### TimestampRange(DateTime?, DateTime?)
    
    
    public static RowFilter TimestampRange(DateTime? startTimestamp, DateTime? endTimestamp)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells with versions within the given range.

**Parameters**  
---  
**Name** | **Description**  
`startTimestamp` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
Of the range of versions from which cells should be matched, inclusive lower bound timestamp whose milliseconds since the Unix epoch should be used as the version value. If null, interpreted as 0. It must be specified in UTC.  
`endTimestamp` | `[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)`  
Of the range of versions from which cells should be matched, exclusive upper bound timestamp whose milliseconds since the Unix epoch should be used as the version value. If null, interpreted as infinity. It must be specified in UTC.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

Note: version values are stored on the server as if they are microseconds since the Unix epoch. However, the server only supports millisecond granularity, so the server only allows microseconds in multiples of 1,000. [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) attempts to hide this complexity by exposing its underlying [Value](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Value) in terms of milliseconds, so if desired, a custom versioning scheme of 1, 2, ... can be used rather than 1000, 2000, ... However, access to the underlying microsecond value is still provided via [Micros](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion#Google_Cloud_Bigtable_V2_BigtableVersion_Micros). 

Note: when using ReadModifyWriteRow, modified columns automatically use a server version, which is based on the current timestamp since the Unix epoch. For those columns, other reads and writes should use [BigtableVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersion) values constructed from DateTime values, as opposed to using a custom versioning scheme with 64-bit values. 

### ValueExact(BigtableByteString)
    
    
    public static RowFilter ValueExact(BigtableByteString value)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells with values that match the exact byte string specified.

**Parameter**  
---  
**Name** | **Description**  
`value` | `[BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html)`  
The exact value used to match cell values.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

Note that string is implicitly convertible to [BigtableByteString](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Common.V2/latest/Google.Cloud.Bigtable.Common.V2.BigtableByteString.html), so `value` can be specified using a string as well and its UTF-8 representations will be used. 

### ValueRange(ValueRange)
    
    
    public static RowFilter ValueRange(ValueRange range)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells with values that fall within the given range.

**Parameter**  
---  
**Name** | **Description**  
`range` | `[ValueRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ValueRange)`  
The range of values to match. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
### ValueRegex(string)
    
    
    public static RowFilter ValueRegex(string regex)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells with values that satisfy the given regular expression.

**Parameter**  
---  
**Name** | **Description**  
`regex` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The RE2 regex used to match cell values.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
**Remarks**

The format of RE2 is documented at <https://github.com/google/re2/wiki/Syntax>. 

Note that, since cell values can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary value. 

### VersionRange(BigtableVersionRange)
    
    
    public static RowFilter VersionRange(BigtableVersionRange range)

Creates a new [RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter) instance which matches only cells with versions within the given range.

**Parameter**  
---  
**Name** | **Description**  
`range` | `[BigtableVersionRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.BigtableVersionRange)`  
The range of versions from which cells should be matched. Must not be null.  
**Returns**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)` | The created row filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
