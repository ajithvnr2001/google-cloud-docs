---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-BigtableSource-Column/
title: BigQuery API - Class Google::Cloud::Bigquery::External::BigtableSource::Column (v1.64.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:12.897740+00:00
---

# BigQuery API - Class Google::Cloud::Bigquery::External::BigtableSource::Column (v1.64.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery/latest/Google-Cloud-Bigquery-External-BigtableSource-Column/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery API - Class Google::Cloud::Bigquery::External::BigtableSource::Column (v1.64.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.64.0 (latest)  1.63.1  1.62.0  1.61.1  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.1  1.51.1  1.50.0  1.49.1  1.48.1  1.47.0  1.46.1  1.45.0  1.44.2  1.43.1  1.42.0  1.41.0  1.40.0  1.39.0  1.38.1 

Reference documentation and code samples for the BigQuery API class Google::Cloud::Bigquery::External::BigtableSource::Column.

## BigtableSource::Column

A Bigtable column to expose in the table schema along with its types.

## Inherits

  * Object 



## Example
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.rowkey_as_string = true
      bt.add_family "user" do |u|
        u.add_string "name"
        u.add_string "email"
        u.add_integer "age"
        u.add_boolean "active"
      end
    end
    
    data = bigquery.query "SELECT * FROM my_ext_table",
                          external: { my_ext_table: bigtable_table }
    
    # Iterate over the first page of results
    data.each do |row|
      puts row[:name]
    end
    # Retrieve the next page of results
    data = data.next if data.next?

## Methods 

### #encoding
    
    
    def encoding() -> String

The encoding of the values when the type is not `STRING`.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_bytes "name" do |col|
          col.encoding = "TEXT"
          col.encoding # "TEXT"
        end
      end
    end

### #encoding=
    
    
    def encoding=(new_encoding)

Set the encoding of the values when the type is not `STRING`. Acceptable encoding values are:

  * `TEXT` \- indicates values are alphanumeric text strings.
  * `BINARY` \- indicates values are encoded using HBase `Bytes.toBytes` family of functions. This can be overridden on a column.



**Parameter**

  * **new_encoding** (String) — New encoding value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_bytes "name" do |col|
          col.encoding = "TEXT"
          col.encoding # "TEXT"
        end
      end
    end

### #field_name
    
    
    def field_name() -> String

If the qualifier is not a valid BigQuery field identifier (does not match `[a-zA-Z][a-zA-Z0-9_]*`) a valid identifier must be provided as the column field name and is used as field name in queries.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "001_name", as: "user" do |col|
          col.field_name # "user"
          col.field_name = "User"
          col.field_name # "User"
        end
      end
    end

### #field_name=
    
    
    def field_name=(new_field_name)

Sets the identifier to be used as the column field name in queries when the qualifier is not a valid BigQuery field identifier (does not match `[a-zA-Z][a-zA-Z0-9_]*`).

**Parameter**

  * **new_field_name** (String) — New field_name value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "001_name", as: "user" do |col|
          col.field_name # "user"
          col.field_name = "User"
          col.field_name # "User"
        end
      end
    end

### #latest
    
    
    def latest() -> Boolean

Whether only the latest version of value in this column are exposed. Can also be set at the column family level. However, this value takes precedence when set at both levels.

**Returns**

  * (Boolean) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.latest = true
          col.latest # true
        end
      end
    end

### #latest=
    
    
    def latest=(new_latest)

Set whether only the latest version of value in this column are exposed. Can also be set at the column family level. However, this value takes precedence when set at both levels.

**Parameter**

  * **new_latest** (Boolean) — New latest value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.latest = true
          col.latest # true
        end
      end
    end

### #qualifier
    
    
    def qualifier() -> String

Qualifier of the column. Columns in the parent column family that has this exact qualifier are exposed as `.` field. If the qualifier is valid UTF-8 string, it will be represented as a UTF-8 string. Otherwise, it will represented as a ASCII-8BIT string.

If the qualifier is not a valid BigQuery field identifier (does not match `[a-zA-Z][a-zA-Z0-9_]*`) a valid identifier must be provided as `field_name`.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.qualifier # "user"
          col.qualifier = "User"
          col.qualifier # "User"
        end
      end
    end

### #qualifier=
    
    
    def qualifier=(new_qualifier)

Set the qualifier of the column. Columns in the parent column family that has this exact qualifier are exposed as `.` field. Values that are valid UTF-8 strings will be treated as such. All other values will be treated as `BINARY`.

**Parameter**

  * **new_qualifier** (String) — New qualifier value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.qualifier # "user"
          col.qualifier = "User"
          col.qualifier # "User"
        end
      end
    end

### #type
    
    
    def type() -> String

The type to convert the value in cells of this column. The values are expected to be encoded using HBase `Bytes.toBytes` function when using the `BINARY` encoding value. The following BigQuery types are allowed:

  * `BYTES`
  * `STRING`
  * `INTEGER`
  * `FLOAT`
  * `BOOLEAN`



Default type is `BYTES`. Can also be set at the column family level. However, this value takes precedence when set at both levels.

**Returns**

  * (String) 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.type # "STRING"
        end
      end
    end

### #type=
    
    
    def type=(new_type)

Set the type to convert the value in cells of this column. The values are expected to be encoded using HBase `Bytes.toBytes` function when using the `BINARY` encoding value. The following BigQuery types are allowed:

  * `BYTES`
  * `STRING`
  * `INTEGER`
  * `FLOAT`
  * `BOOLEAN`



Default type is `BYTES`. Can also be set at the column family level. However, this value takes precedence when set at both levels.

**Parameter**

  * **new_type** (String) — New type value 



**Example**
    
    
    require "google/cloud/bigquery"
    
    bigquery = Google::Cloud::Bigquery.new
    
    bigtable_url = "https://googleapis.com/bigtable/projects/..."
    bigtable_table = bigquery.external bigtable_url do |bt|
      bt.add_family "user" do |u|
        u.add_string "name" do |col|
          col.type # "STRING"
          col.type = "BYTES"
          col.type # "BYTES"
        end
      end
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-11 UTC."],[],[]] 
