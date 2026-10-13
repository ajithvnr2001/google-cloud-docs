---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter/
title: Cloud Bigtable API - Module Google::Cloud::Bigtable::RowFilter (v2.13.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:01.197862+00:00
---

# Cloud Bigtable API - Module Google::Cloud::Bigtable::RowFilter (v2.13.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Bigtable API - Module Google::Cloud::Bigtable::RowFilter (v2.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.13.0 (latest)  2.12.3  2.11.1  2.10.2  2.9.1  2.8.0  2.7.1  2.6.5 

Reference documentation and code samples for the Cloud Bigtable API module Google::Cloud::Bigtable::RowFilter.

## RowFilter

Takes a row as input and produces an alternate view of the row based on specified rules. For example, a RowFilter might trim down a row to include just the cells from columns matching a given regular expression, or it might return all the cells of a row but not their values. More complicated filters can be composed out of these components to express requests such as, "within every column of a particular family, give just the two most recent cells that are older than timestamp X."

Two broad categories of RowFilters are `true filters` and `transformers`. Two ways to compose simple filters into more complex ones are `chains` and `interleaves`. They work as follows:

  * True filters alter the input row by excluding some of its cells wholesale from the output row. An example of a true filter is the `value_regex_filter`, which excludes cells whose values don't match the specified pattern. All regex true filters use RE2 syntax (https:#github.com/google/re2/wiki/Syntax) in raw byte mode (RE2::Latin1) and are evaluated as full matches. An important point to keep in mind is that `RE2(.)` is equivalent by default to `RE2([^\n])`, meaning that it does not match newlines. When attempting to match an arbitrary byte, you should therefore use the escape sequence `\C`, which should be further escaped as `\C` in Ruby.

  * Transformers alter the input row by changing the values of some of its cells in the output, without excluding them completely. Currently, the only supported transformer is the `strip_value_transformer`, which replaces every cell's value with an empty string.

  * Chains and interleaves are described in more detail in the RowFilter.Chain and RowFilter.Interleave documentation.




The total serialized size of a RowFilter message must not exceed 4096 bytes, and RowFilters may not be nested within each other (in chains or interleaves) to a depth of more than 20.

ADVANCED USE:. Hook for introspection into the RowFilter. Outputs all cells directly to the output of the read rather than to any parent filter. Consider the following example:
    
    
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
                        A,B,2,x,labels:[foo]  # could be switched
                        A,B,2,x               # could be switched
    

Despite being excluded by the qualifier filter, a copy of every cell that reaches the sink is present in the final result.

As with an interleave filter, duplicate cells are possible and appear in an unspecified mutual order. In this case we have a duplicate with column "A:B" and timestamp 2 because one copy passed through the All filter while the other was passed through the Label and Sink filters. Note that one copy has the label "foo", while the other does not.

## Example
    
    
    require "google/cloud/bigtable"
    
    # Pass filter
    Google::Cloud::Bigtable::RowFilter.pass
    
    # Key regex filter
    Google::Cloud::Bigtable::RowFilter.key "user-*"
    
    # Cell limit filter
    Google::Cloud::Bigtable::RowFilter.cells_per_row 10

## Methods 

### .block
    
    
    def self.block() -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a block-all filter instance.

Does not match any cells, regardless of input. Useful for temporarily disabling just part of a filter.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.block

### .cells_per_column
    
    
    def self.cells_per_column(limit) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates cells-per-column filter instance.

Matches only the most recent N cells within each column. If duplicate cells are present, as is possible when using an interleave, each copy of the cell is counted separately.

**Parameter**

  * **limit** (String) — Max cell match per column limit 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_column 5

### .cells_per_row
    
    
    def self.cells_per_row(limit) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Create a cells-per-row limit filter instance.

Matches only the first N cells of each row. If duplicate cells are present, as is possible when using an interleave, each copy of the cell is counted separately.

**Parameter**

  * **limit** (String) — Max cell match per row limit 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_row 5

### .cells_per_row_offset
    
    
    def self.cells_per_row_offset(offset) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a cell-per-row-offset filter instance to skip first N cells.

Skips the first N cells of each row, matching all subsequent cells. If duplicate cells are present, as is possible when using an interleave, each copy of the cell is counted separately.

**Parameter**

  * **offset** (Integer) — Offset value. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.cells_per_row_offset 3

### .chain
    
    
    def self.chain() -> Google::Cloud::Bigtable::RowFilter::ChainFilter

Creates a chain filter instance.

A chain RowFilter that sends rows through several RowFilters in sequence.

See [ChainFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-ChainFilter "Google::Cloud::Bigtable::RowFilter::ChainFilter \(class\)").

The elements of "filters" are chained together to process the input row: in row -> f(0) -> intermediate row -> f(1) -> ... -> f(N) -> out row The full chain is executed atomically.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::ChainFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-ChainFilter)) 



**Examples**

Create chain filter with simple filter.
    
    
    require "google/cloud/bigtable"
    
    chain = Google::Cloud::Bigtable::RowFilter.chain
    
    # Add filters to chain filter
    chain.key "user-*"
    chain.strip_value
    
    # OR
    chain.key("user-*").strip_value

Create complex chain filter.
    
    
    require "google/cloud/bigtable"
    
    chain = Google::Cloud::Bigtable::RowFilter.chain
    
    chain_1 = Google::Cloud::Bigtable::RowFilter.chain
    chain_1.label("users").qualifier("name").cells_per_row(5)
    
    # Add to main chain filter
    chain.chain(chain_1).value("xyz*").key("user-*")

### .column_range
    
    
    def self.column_range(range) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a column-range filter instance.

Matches only cells from columns within the given range.

**Parameter**

  * **range** ([Google::Cloud::Bigtable::ColumnRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ColumnRange)) 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    range = Google::Cloud::Bigtable::ColumnRange.new("cf").from("field0").to("field5")
    
    filter = Google::Cloud::Bigtable::RowFilter.column_range range

### .condition
    
    
    def self.condition(predicate) -> Google::Cloud::Bigtable::RowFilter::ConditionFilter

Creates a condition filter instance.

A RowFilter that evaluates one of two possible RowFilters, depending on whether or not a predicate RowFilter outputs any cells from the input row.

IMPORTANT NOTE: The predicate filter does not execute atomically with the true and false filters, which may lead to inconsistent or unexpected results. Additionally, condition filters have poor performance, especially when filters are set for the false condition.

Cannot be used within the `predicate_filter`, `true_filter`, or `false_filter`.

**Parameter**

  * **predicate** ([SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter), [ChainFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-ChainFilter), [InterleaveFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-InterleaveFilter), [ConditionFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-ConditionFilter)) 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::ConditionFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-ConditionFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    predicate = Google::Cloud::Bigtable::RowFilter.key "user-*"
    condition = Google::Cloud::Bigtable::RowFilter.condition predicate
    
    label = Google::Cloud::Bigtable::RowFilter.label "user"
    strip_value = Google::Cloud::Bigtable::RowFilter.strip_value
    
    # On match apply label, else strip cell values
    condition.on_match(label).otherwise(strip_value)

### .family
    
    
    def self.family(regex) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a family name match filter using a regular expression.

Matches only cells from columns whose families satisfy the given RE2 regex. For technical reasons, the regex must not contain the `:` character, even if it is not being used as a literal. Note that, since column families cannot contain the new line character `\n`, it is sufficient to use `.` as a full wildcard when matching column family names.

**Parameter**

  * **regex** (String) — Regex to match family name. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.family "cf-.*"

### .interleave
    
    
    def self.interleave() -> Google::Cloud::Bigtable::RowFilter::InterleaveFilter

Creates an interleave filter.

A RowFilter that sends each row to each of several component RowFilters and interleaves the results.

The elements of "filters" all process a copy of the input row, and the results are pooled, sorted, and combined into a single output row. If multiple cells are produced with the same column and timestamp, they will all appear in the output row in an unspecified mutual order. Consider the following example, with three filters:
    
    
                                 input row
                                     |
           -----------------------------------------------------
           |                         |                         |
          f(0)                      f(1)                      f(2)
           |                         |                         |
    1: foo,bar,10,x             foo,bar,10,z              far,bar,7,a
    2: foo,blah,11,z            far,blah,5,x              far,blah,5,x
           |                         |                         |
           -----------------------------------------------------
                                     |
    1:                      foo,bar,10,z   # could have switched with #2
    2:                      foo,bar,10,x   # could have switched with #1
    3:                      foo,blah,11,z
    4:                      far,bar,7,a
    5:                      far,blah,5,x   # identical to #6
    6:                      far,blah,5,x   # identical to #5
    

All interleaved filters are executed atomically.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::InterleaveFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-InterleaveFilter)) 



**Examples**

Create an interleave filter with simple filter.
    
    
    require "google/cloud/bigtable"
    
    interleave = Google::Cloud::Bigtable::RowFilter.interleave
    
    # Add filters to interleave filter
    interleave.key "user-*"
    interleave.sink
    
    # OR
    interleave.key("user-*").sink

Create complex interleave filter.
    
    
    require "google/cloud/bigtable"
    
    interleave = Google::Cloud::Bigtable::RowFilter.interleave
    
    chain_1 = Google::Cloud::Bigtable::RowFilter.chain
    chain_1.label("users").qualifier("name").cells_per_row(5)
    
    # Add to main chain filter
    interleave.chain(chain_1).value("xyz*").key("user-*")

### .key
    
    
    def self.key(regex) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a key filter instance to match a row key using a regular expression.

Matches only cells from rows whose row keys satisfy the given RE2 regex. In other words, passes through the entire row when the key matches, and otherwise produces an empty row. Note that, since row keys can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary key.

**Parameter**

  * **regex** (String) — Regex to match row keys. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.key "user-.*"

### .label
    
    
    def self.label(value) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a label filter instance to apply a label based on the result of read rows.

Applies the given label to all cells in the output row. This allows the client to determine which results were produced from which part of the filter.

Values must be at most 15 characters and match the RE2 pattern `[a-z0-9\-]+`

Due to a technical limitation, it is not possible to apply multiple labels to a cell. As a result, a chain may have no more than one sub-filter that contains an `apply_label_transformer`. It is okay for an interleave to contain multiple `apply_label_transformers`, as they will be applied to separate copies of the input.

**Parameter**

  * **value** (String) — Label name 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.label "user-detail"

### .pass
    
    
    def self.pass() -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a pass filter instance.

Matches all cells, regardless of input. Functionally equivalent to leaving `filter` unset, but included for completeness.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.pass

### .qualifier
    
    
    def self.qualifier(regex) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a column qualifier match filter using a regular expression.

Matches only cells from columns whose qualifiers satisfy the given RE2 regex. Note that, since column qualifiers can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary qualifier.

**Parameter**

  * **regex** (String) — Regex to match column qualifier name. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.qualifier "user-name.*"

### .sample
    
    
    def self.sample(probability) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a sample probability filter instance.

Matches all cells from a row with probability p, and matches no cells from the row with probability 1-p.

**Parameter**

  * **probability** (Float) — Probability value. Probability must be greater than 0 and less than 1.0. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.sample 0.5

### .sink
    
    
    def self.sink() -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a sink filter instance.

Outputs all cells directly to the output of the read rather than to any parent filter.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.sink

### .strip_value
    
    
    def self.strip_value() -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a strip value filter instance.

Replaces each cell's value with an empty string.

**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.strip_value

### .timestamp_range
    
    
    def self.timestamp_range(from: nil, to: nil) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a timestamp-range filter instance.

Matches only cells with timestamps within the given range. Specifies a contiguous range of timestamps.

**Parameters**

  * **from** (Integer) _(defaults to: nil)_ — Inclusive lower bound. If left empty, interpreted as 0. 
  * **to** (Integer) _(defaults to: nil)_ — Exclusive upper bound. If left empty, interpreted as infinity. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    timestamp_micros = (Time.now.to_f * 1_000_000).round(-3)
    from = timestamp_micros - 300_000_000
    to = timestamp_micros
    
    filter = Google::Cloud::Bigtable::RowFilter.timestamp_range from: from, to: to
    
    # From to infinity
    filter = Google::Cloud::Bigtable::RowFilter.timestamp_range from: from
    
    # From 0 value to `to`
    filter = Google::Cloud::Bigtable::RowFilter.timestamp_range to: to

### .value
    
    
    def self.value(regex) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a value match filter using a regular expression.

Matches only cells with values that satisfy the given regular expression. Note that, since cell values can contain arbitrary bytes, the `\C` escape sequence must be used if a true wildcard is desired. The `.` character will not match the new line character `\n`, which may be present in a binary value.

**Parameter**

  * **regex** (String) — Regex to match cell value. 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Example**
    
    
    require "google/cloud/bigtable"
    
    filter = Google::Cloud::Bigtable::RowFilter.value "abc.*"

### .value_range
    
    
    def self.value_range(range) -> Google::Cloud::Bigtable::RowFilter::SimpleFilter

Creates a value-range filter instance.

Matches only cells with values that fall within the given range.

See [ValueRange#from](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ValueRange#Google__Cloud__Bigtable__ValueRange_from_instance_ "Google::Cloud::Bigtable::ValueRange#from \(method\)") and { Google::Cloud::Bigtable::ValueRange#to} for range option inclusive/exclusive options

  * The value at which to start the range. If neither field is set, interpreted as an empty string, inclusive.
  * The value at which to end the range. If neither field is set, interpreted as an infinite string, exclusive.



**Parameter**

  * **range** ([Google::Cloud::Bigtable::ValueRange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-ValueRange)) 



**Returns**

  * ([Google::Cloud::Bigtable::RowFilter::SimpleFilter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigtable/latest/Google-Cloud-Bigtable-RowFilter-SimpleFilter)) 



**Examples**

Start to end range.
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table "my-instance", "my-table"
    
    range = table.new_value_range.from "value-001", inclusive: false
    filter = Google::Cloud::Bigtable::RowFilter.value_range range

Start exclusive to infinite end range.
    
    
    require "google/cloud/bigtable"
    
    bigtable = Google::Cloud::Bigtable.new
    table = bigtable.table "my-instance", "my-table"
    
    range = table.new_value_range.from "value-001", inclusive: false
    filter = Google::Cloud::Bigtable::RowFilter.value_range range

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
