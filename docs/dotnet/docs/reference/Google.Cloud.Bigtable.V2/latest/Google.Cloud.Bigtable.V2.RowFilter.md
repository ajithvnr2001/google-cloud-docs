---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter
title: Google Bigtable v2 API - Class RowFilter (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:05.736905+00:00
---

# Google Bigtable v2 API - Class RowFilter (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class RowFilter (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class RowFilter : IMessage<RowFilter>, IEquatable<RowFilter>, IDeepCloneable<RowFilter>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class RowFilter.

Takes a row as input and produces an alternate view of the row based on specified rules. For example, a RowFilter might trim down a row to include just the cells from columns matching a given regular expression, or might return all the cells of a row but not their values. More complicated filters can be composed out of these components to express requests such as, "within every column of a particular family, give just the two most recent cells which are older than timestamp X."

There are two broad categories of RowFilters (true filters and transformers), as well as two ways to compose simple filters into more complex ones (chains and interleaves). They work as follows:

  * True filters alter the input row by excluding some of its cells wholesale from the output row. An example of a true filter is the `value_regex_filter`, which excludes cells whose values don't match the specified pattern. All regex true filters use RE2 syntax (<https://github.com/google/re2/wiki/Syntax>) in raw byte mode (RE2::Latin1), and are evaluated as full matches. An important point to keep in mind is that `RE2(.)` is equivalent by default to `RE2([^\n])`, meaning that it does not match newlines. When attempting to match an arbitrary byte, you should therefore use the escape sequence `\C`, which may need to be further escaped as `\\C` in your client language.

  * Transformers alter the input row by changing the values of some of its cells in the output, without excluding them completely. Currently, the only supported transformer is the `strip_value_transformer`, which replaces every cell's value with the empty string.

  * Chains and interleaves are described in more detail in the RowFilter.Chain and RowFilter.Interleave documentation.




The total serialized size of a RowFilter message must not exceed 20480 bytes, and RowFilters may not be nested within each other (in Chains or Interleaves) to a depth of more than 20.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RowFilter

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### RowFilter()
    
    
    public RowFilter()

### RowFilter(RowFilter)
    
    
    public RowFilter(RowFilter other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)`  
  
  
## Properties 

### ApplyLabelTransformer
    
    
    public string ApplyLabelTransformer { get; set; }

Applies the given label to all cells in the output row. This allows the client to determine which results were produced from which part of the filter.

Values must be at most 15 characters in length, and match the RE2 pattern `[a-z0-9\\-]+`

Due to a technical limitation, it is not currently possible to apply multiple labels to a cell. As a result, a Chain may have no more than one sub-filter which contains a `apply_label_transformer`. It is okay for an Interleave to contain multiple `apply_label_transformers`, as they will be applied to separate copies of the input. This may be relaxed in the future.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### BlockAllFilter
    
    
    public bool BlockAllFilter { get; set; }

Does not match any cells, regardless of input. Useful for temporarily disabling just part of a filter.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### CellsPerColumnLimitFilter
    
    
    public int CellsPerColumnLimitFilter { get; set; }

Matches only the most recent N cells within each column. For example, if N=2, this filter would match column `foo:bar` at timestamps 10 and 9, skip all earlier cells in `foo:bar`, and then begin matching again in column `foo:bar2`. If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### CellsPerRowLimitFilter
    
    
    public int CellsPerRowLimitFilter { get; set; }

Matches only the first N cells of each row. If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### CellsPerRowOffsetFilter
    
    
    public int CellsPerRowOffsetFilter { get; set; }

Skips the first N cells of each row, matching all subsequent cells. If duplicate cells are present, as is possible when using an Interleave, each copy of the cell is counted separately.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Chain
    
    
    public RowFilter.Types.Chain Chain { get; set; }

Applies several RowFilters to the data in sequence, progressively narrowing the results.

**Property Value**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types)[Chain](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types.Chain)` |   
  
### ColumnQualifierRegexFilter
    
    
    public ByteString ColumnQualifierRegexFilter { get; set; }

Matches only cells from columns whose qualifiers satisfy the given RE2 regex. Note that, since column qualifiers can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary qualifier.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ColumnRangeFilter
    
    
    public ColumnRange ColumnRangeFilter { get; set; }

Matches only cells from columns within the given range.

**Property Value**  
---  
**Type** | **Description**  
`[ColumnRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ColumnRange)` |   
  
### Condition
    
    
    public RowFilter.Types.Condition Condition { get; set; }

Applies one of two possible RowFilters to the data based on the output of a predicate RowFilter.

**Property Value**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types)[Condition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types.Condition)` |   
  
### FamilyNameRegexFilter
    
    
    public string FamilyNameRegexFilter { get; set; }

Matches only cells from columns whose families satisfy the given RE2 regex. For technical reasons, the regex must not contain the `:` character, even if it is not being used as a literal. Note that, since column families cannot contain the new line character `\n`, it is sufficient to use `.` as a full wildcard when matching column family names.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FilterCase
    
    
    public RowFilter.FilterOneofCase FilterCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)[FilterOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.FilterOneofCase)` |   
  
### HasApplyLabelTransformer
    
    
    public bool HasApplyLabelTransformer { get; }

Gets whether the "apply_label_transformer" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasBlockAllFilter
    
    
    public bool HasBlockAllFilter { get; }

Gets whether the "block_all_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCellsPerColumnLimitFilter
    
    
    public bool HasCellsPerColumnLimitFilter { get; }

Gets whether the "cells_per_column_limit_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCellsPerRowLimitFilter
    
    
    public bool HasCellsPerRowLimitFilter { get; }

Gets whether the "cells_per_row_limit_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasCellsPerRowOffsetFilter
    
    
    public bool HasCellsPerRowOffsetFilter { get; }

Gets whether the "cells_per_row_offset_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasColumnQualifierRegexFilter
    
    
    public bool HasColumnQualifierRegexFilter { get; }

Gets whether the "column_qualifier_regex_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasFamilyNameRegexFilter
    
    
    public bool HasFamilyNameRegexFilter { get; }

Gets whether the "family_name_regex_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPassAllFilter
    
    
    public bool HasPassAllFilter { get; }

Gets whether the "pass_all_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRowKeyRegexFilter
    
    
    public bool HasRowKeyRegexFilter { get; }

Gets whether the "row_key_regex_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasRowSampleFilter
    
    
    public bool HasRowSampleFilter { get; }

Gets whether the "row_sample_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasSink
    
    
    public bool HasSink { get; }

Gets whether the "sink" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasStripValueTransformer
    
    
    public bool HasStripValueTransformer { get; }

Gets whether the "strip_value_transformer" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasValueRegexFilter
    
    
    public bool HasValueRegexFilter { get; }

Gets whether the "value_regex_filter" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Interleave
    
    
    public RowFilter.Types.Interleave Interleave { get; set; }

Applies several RowFilters to the data in parallel and combines the results.

**Property Value**  
---  
**Type** | **Description**  
`[RowFilter](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types)[Interleave](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.RowFilter.Types.Interleave)` |   
  
### PassAllFilter
    
    
    public bool PassAllFilter { get; set; }

Matches all cells, regardless of input. Functionally equivalent to leaving `filter` unset, but included for completeness.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RowKeyRegexFilter
    
    
    public ByteString RowKeyRegexFilter { get; set; }

Matches only cells from rows whose keys satisfy the given RE2 regex. In other words, passes through the entire row when the key matches, and otherwise produces an empty row. Note that, since row keys can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary key.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### RowSampleFilter
    
    
    public double RowSampleFilter { get; set; }

Matches all cells from a row with probability p, and matches no cells from the row with probability 1-p.

**Property Value**  
---  
**Type** | **Description**  
`[double](https://learn.microsoft.com/dotnet/api/system.double)` |   
  
### Sink
    
    
    public bool Sink { get; set; }

ADVANCED USE ONLY. Hook for introspection into the RowFilter. Outputs all cells directly to the output of the read rather than to any parent filter. Consider the following example:
    
    
    Chain(
      FamilyRegex("A"),
      Interleave(
        All(),
        Chain(Label("foo"), Sink())
      ),
      QualifierRegex("B")
    )
    
                        A,A,1,w
                        A,B,2,x
                        B,B,4,z
                           |
                    FamilyRegex("A")
                           |
                        A,A,1,w
                        A,B,2,x
                           |
              +------------+-------------+
              |                          |
            All()                    Label(foo)
              |                          |
           A,A,1,w              A,A,1,w,labels:[foo]
           A,B,2,x              A,B,2,x,labels:[foo]
              |                          |
              |                        Sink() --------------+
              |                          |                  |
              +------------+      x------+          A,A,1,w,labels:[foo]
                           |                        A,B,2,x,labels:[foo]
                        A,A,1,w                             |
                        A,B,2,x                             |
                           |                                |
                   QualifierRegex("B")                      |
                           |                                |
                        A,B,2,x                             |
                           |                                |
                           +--------------------------------+
                           |
                        A,A,1,w,labels:[foo]
                        A,B,2,x,labels:[foo]  // could be switched
                        A,B,2,x               // could be switched
    

Despite being excluded by the qualifier filter, a copy of every cell that reaches the sink is present in the final result.

As with an [Interleave][google.bigtable.v2.RowFilter.Interleave], duplicate cells are possible, and appear in an unspecified mutual order. In this case we have a duplicate with column "A:B" and timestamp 2, because one copy passed through the all filter while the other was passed through the label and sink. Note that one copy has label "foo", while the other does not.

Cannot be used within the `predicate_filter`, `true_filter`, or `false_filter` of a [Condition][google.bigtable.v2.RowFilter.Condition].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### StripValueTransformer
    
    
    public bool StripValueTransformer { get; set; }

Replaces each cell's value with the empty string.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TimestampRangeFilter
    
    
    public TimestampRange TimestampRangeFilter { get; set; }

Matches only cells with timestamps within the given range.

**Property Value**  
---  
**Type** | **Description**  
`[TimestampRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.TimestampRange)` |   
  
### ValueBitmaskFilter
    
    
    public ValueBitmask ValueBitmaskFilter { get; set; }

Matches only cells with values that satisfy the condition `(value & mask) == mask`. The mask length must exactly match the value length, otherwise the cell is not considered a match.

**Property Value**  
---  
**Type** | **Description**  
`[ValueBitmask](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ValueBitmask)` |   
  
### ValueRangeFilter
    
    
    public ValueRange ValueRangeFilter { get; set; }

Matches only cells with values that fall within the given range.

**Property Value**  
---  
**Type** | **Description**  
`[ValueRange](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ValueRange)` |   
  
### ValueRegexFilter
    
    
    public ByteString ValueRegexFilter { get; set; }

Matches only cells with values that satisfy the given regular expression. Note that, since cell values can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary value.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
