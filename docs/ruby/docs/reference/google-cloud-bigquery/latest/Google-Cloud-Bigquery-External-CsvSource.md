---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-CsvSource/
title: BigQuery API - Class Google::Cloud::Bigquery::External::CsvSource (v1.64.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:22:00.777976+00:00
---

# BigQuery API - Class Google::Cloud::Bigquery::External::CsvSource (v1.64.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-CsvSource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery API - Class Google::Cloud::Bigquery::External::CsvSource (v1.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.64.0 (latest)  1.63.1  1.62.0  1.61.1  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.1  1.51.1  1.50.0  1.49.1  1.48.1  1.47.0  1.46.1  1.45.0  1.44.2  1.43.1  1.42.0  1.41.0  1.40.0  1.39.0  1.38.1 

Reference documentation and code samples for the BigQuery API class Google::Cloud::Bigquery::External::CsvSource.

## CsvSource

[CsvSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-CsvSource "Google::Cloud::Bigquery::External::CsvSource \(class\)") is a subclass of [DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-DataSource "Google::Cloud::Bigquery::External::DataSource \(class\)") and represents a CSV external data source that can be queried from directly, such as Google Cloud Storage or Google Drive, even though the data is not stored in BigQuery. Instead of loading or streaming the data, this object references the external data source.

## Inherits

  * [Google::Cloud::Bigquery::External::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-DataSource)



## Example
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.autodetect = true
      csv.skip_leading_rows = 1
    end
    
    data = bigquery.query "SELECT * FROM my_ext_table",
                          external: { my_ext_table: csv_table }
    
    # Iterate over the first page of results
    data.each do |row|
      puts row[:name]
    end
    # Retrieve the next page of results
    data = data.next if data.next?

## Methods 

### #delimiter
    
    
    def delimiter() -> String

The separator for fields in a CSV file.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.delimiter = "|"
    end
    
    csv_table.delimiter #=> "|"

### #delimiter=
    
    
    def delimiter=(new_delimiter)

Set the separator for fields in a CSV file.

**Parameter**

  * **new_delimiter** (String) — New delimiter value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.delimiter = "|"
    end
    
    csv_table.delimiter #=> "|"

### #encoding
    
    
    def encoding() -> String

The character encoding of the data.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.encoding = "UTF-8"
    end
    
    csv_table.encoding #=> "UTF-8"

### #encoding=
    
    
    def encoding=(new_encoding)

Set the character encoding of the data.

**Parameter**

  * **new_encoding** (String) — New encoding value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.encoding = "UTF-8"
    end
    
    csv_table.encoding #=> "UTF-8"

### #fields
    
    
    def fields() -> Array<Schema::Field>

The fields of the schema.

**Returns**

  * (Array<[Schema::Field](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Schema-Field)>) — An array of field objects. 



### #headers
    
    
    def headers() -> Array<Symbol>

The names of the columns in the schema.

**Returns**

  * (Array<Symbol>) — An array of column names. 



### #iso8859_1?
    
    
    def iso8859_1?() -> Boolean

Checks if the character encoding of the data is "ISO-8859-1".

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.encoding = "ISO-8859-1"
    end
    
    csv_table.encoding #=> "ISO-8859-1"
    csv_table.iso8859_1? #=> true

### #jagged_rows
    
    
    def jagged_rows() -> Boolean

Indicates if BigQuery should accept rows that are missing trailing optional columns.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.jagged_rows = true
    end
    
    csv_table.jagged_rows #=> true

### #jagged_rows=
    
    
    def jagged_rows=(new_jagged_rows)

Set whether BigQuery should accept rows that are missing trailing optional columns.

**Parameter**

  * **new_jagged_rows** (Boolean) — New jagged_rows value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.jagged_rows = true
    end
    
    csv_table.jagged_rows #=> true

### #null_marker
    
    
    def null_marker() -> String, nil

Specifies a string that represents a null value in a CSV file. For example, if you specify `\N`, BigQuery interprets `\N` as a null value when querying a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as an empty value.

**Returns**

  * (String, nil) — The null marker string. `nil` if not set. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.null_marker = "\N"
    end
    
    csv_table.null_marker #=> "\N"

### #null_marker=
    
    
    def null_marker=(null_marker)

Sets a string that represents a null value in a CSV file. For example, if you specify `\N`, BigQuery interprets `\N` as a null value when querying a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as an empty value.

**Parameter**

  * **null_marker** (String, nil) — The null marker string. `nil` to unset. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.null_marker = "\N"
    end
    
    csv_table.null_marker #=> "\N"

### #null_markers
    
    
    def null_markers() -> Array<String>

The list of strings represented as SQL NULL value in a CSV file. null_marker and null_markers can't be set at the same time. If null_marker is set, null_markers has to be not set. If null_markers is set, null_marker has to be not set. If both null_marker and null_markers are set at the same time, a user error would be thrown. Any strings listed in null_markers, including empty string would be interpreted as SQL NULL. This applies to all column types.

**Returns**

  * (Array<String>) — The array of null marker strings. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.null_markers = ["\N", "NULL"]
    end
    
    csv_table.null_markers #=> ["\N", "NULL"]

### #null_markers=
    
    
    def null_markers=(null_markers)

Sets the list of strings represented as SQL NULL value in a CSV file. null_marker and null_markers can't be set at the same time. If null_marker is set, null_markers has to be not set. If null_markers is set, null_marker has to be not set. If both null_marker and null_markers are set at the same time, a user error would be thrown. Any strings listed in null_markers, including empty string would be interpreted as SQL NULL. This applies to all column types.

**Parameter**

  * **null_markers** (Array<String>) — The array of null marker strings. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.null_markers = ["\N", "NULL"]
    end
    
    csv_table.null_markers #=> ["\N", "NULL"]

### #param_types
    
    
    def param_types() -> Hash

The types of the fields in the data in the schema, using the same format as the optional query parameter types.

**Returns**

  * (Hash) — A hash with field names as keys, and types as values. 



### #preserve_ascii_control_characters
    
    
    def preserve_ascii_control_characters() -> Boolean, nil

Indicates if the embedded ASCII control characters (the first 32 characters in the ASCII-table, from `\x00` to `\x1F`) are preserved. By default, ASCII control characters are not preserved.

**Returns**

  * (Boolean, nil) — whether or not ASCII control characters are preserved. `nil` if not set. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.preserve_ascii_control_characters = true
    end
    
    csv_table.preserve_ascii_control_characters #=> true

### #preserve_ascii_control_characters=
    
    
    def preserve_ascii_control_characters=(val)

Sets whether the embedded ASCII control characters (the first 32 characters in the ASCII-table, from `\x00` to `\x1F`) are preserved. By default, ASCII control characters are not preserved.

**Parameter**

  * **val** (Boolean, nil) — whether or not ASCII control characters are preserved. `nil` to unset. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.preserve_ascii_control_characters = true
    end
    
    csv_table.preserve_ascii_control_characters #=> true

### #quote
    
    
    def quote() -> String

The value that is used to quote data sections in a CSV file.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.quote = "'"
    end
    
    csv_table.quote #=> "'"

### #quote=
    
    
    def quote=(new_quote)

Set the value that is used to quote data sections in a CSV file.

**Parameter**

  * **new_quote** (String) — New quote value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.quote = "'"
    end
    
    csv_table.quote #=> "'"

### #quoted_newlines
    
    
    def quoted_newlines() -> Boolean

Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.quoted_newlines = true
    end
    
    csv_table.quoted_newlines #=> true

### #quoted_newlines=
    
    
    def quoted_newlines=(new_quoted_newlines)

Set whether BigQuery should allow quoted data sections that contain newline characters in a CSV file.

**Parameter**

  * **new_quoted_newlines** (Boolean) — New quoted_newlines value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.quoted_newlines = true
    end
    
    csv_table.quoted_newlines #=> true

### #schema
    
    
    def schema(replace: false) { |schema| ... } -> Google::Cloud::Bigquery::Schema

The schema for the data.

**Parameter**

  * **replace** (Boolean) _(defaults to: false)_ — Whether to replace the existing schema with the new schema. If `true`, the fields will replace the existing schema. If `false`, the fields will be added to the existing schema. The default value is `false`. 



**Yields**

  * (schema) — a block for setting the schema 



**Yield Parameter**

  * **schema** ([Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Schema)) — the object accepting the schema 



**Returns**

  * ([Google::Cloud::Bigquery::Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Schema)) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.schema do |schema|
        schema.string "name", mode: :required
        schema.string "email", mode: :required
        schema.integer "age", mode: :required
        schema.boolean "active", mode: :required
      end
    end

### #schema=
    
    
    def schema=(new_schema)

Set the schema for the data.

**Parameter**

  * **new_schema** ([Schema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-Schema)) — The schema object. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_shema = bigquery.schema do |schema|
      schema.string "name", mode: :required
      schema.string "email", mode: :required
      schema.integer "age", mode: :required
      schema.boolean "active", mode: :required
    end
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url
    csv_table.schema = csv_shema

### #skip_leading_rows
    
    
    def skip_leading_rows() -> Integer

The number of rows at the top of a CSV file that BigQuery will skip when reading the data.

**Returns**

  * (Integer) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.skip_leading_rows = 1
    end
    
    csv_table.skip_leading_rows #=> 1

### #skip_leading_rows=
    
    
    def skip_leading_rows=(row_count)

Set the number of rows at the top of a CSV file that BigQuery will skip when reading the data.

**Parameter**

  * **row_count** (Integer) — New skip_leading_rows value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.skip_leading_rows = 1
    end
    
    csv_table.skip_leading_rows #=> 1

### #source_column_match
    
    
    def source_column_match() -> String, nil

Controls the strategy used to match loaded columns to the schema. If not set, a sensible default is chosen based on how the schema is provided. If autodetect is used, then columns are matched by name. Otherwise, columns are matched by position. This is done to keep the behavior backward-compatible.

Acceptable values are:

  * `POSITION`: matches by position. Assumes columns are ordered the same way as the schema.
  * `NAME`: matches by name. Reads the header row as column names and reorders columns to match the schema.



**Returns**

  * (String, nil) — The source column match value. `nil` if not set. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.source_column_match = "NAME"
    end
    
    csv_table.source_column_match #=> "NAME"

### #source_column_match=
    
    
    def source_column_match=(source_column_match)

Sets the strategy used to match loaded columns to the schema. If not set, a sensible default is chosen based on how the schema is provided. If autodetect is used, then columns are matched by name. Otherwise, columns are matched by position. This is done to keep the behavior backward-compatible. Optional.

Acceptable values are:

  * `POSITION`: matches by position. Assumes columns are ordered the same way as the schema.
  * `NAME`: matches by name. Reads the header row as column names and reorders columns to match the schema.



**Parameter**

  * **source_column_match** (String, nil) — The new source column match value. `nil` to unset. 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.source_column_match = "NAME"
    end
    
    csv_table.source_column_match #=> "NAME"

### #utf8?
    
    
    def utf8?() -> Boolean

Checks if the character encoding of the data is "UTF-8". This is the default.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    csv_url = "gs://bucket/path/to/data.csv"
    csv_table = bigquery.external csv_url do |csv|
      csv.encoding = "UTF-8"
    end
    
    csv_table.encoding #=> "UTF-8"
    csv_table.utf8? #=> true

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
