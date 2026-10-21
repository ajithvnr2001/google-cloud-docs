---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-cli-directives/
title: Wrangler command-line directives \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:30.822485+00:00
---

# Wrangler command-line directives  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-cli-directives/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Wrangler command-line directives Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the directives you can use in Wrangler.

In Wrangler _Power mode_ (the Wrangler CLI), you can add directives and functions to a recipe. For more information, see [Wrangler CLI Directives](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/380600349/Directives) and [Wrangler Functions](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/380600356/Functions).

Wrangler supports the following directives:

## Column operations

Directive | Description  
---|---  
[Change Column Case](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042120/Change+Column+Case) | Changes column names to either lowercase or uppercase.  
[Changing Case](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382074887/Changing+Case) | Changes the case of column values.  
[Cleanse Column Names](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107671/Cleanse+Column+Names) | Sanitizes column names, following specific rules.  
[Columns Replace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140422/Columns+Replace) | Alters column names in bulk.  
[Copy](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/381976593/Copy) | Copies values from a source column into a destination column.  
[Drop Column](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042167/Drop+Column) | Drops a column in a record.  
[Fill Null or Empty](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140489/Fill+NULL+or+Empty) | If the value is null or empty, enters a fixed column value.  
[Keep](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382074988/Keep) | Keeps specified columns from the record.  
[Merge](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140577/Merge) | Merges two columns by inserting a third column.  
[Rename](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107917/Rename) | Renames an existing column in the record.  
[Set Headers](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140629/Set+Headers) | Sets the names of columns, in the order they're specified.  
[Split to Columns](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042365/Split+to+Columns) | Splits a column based on a separator into multiple columns.  
[Swap](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140743/Swap) | Swaps column names of two columns.  
[Set Type](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042346/Set+Type) | Converts the data type of a column.  
  
## Date transformations

Directive | Description  
---|---  
[Diff Date](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/381976612/Diff+Date) | Calculates the difference between two dates.  
[Format Date](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140525/Format+Date) | Custom patterns for date-time formatting.  
[Format UNIX Timestamp](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107751/Format+UNIX+Timestamp) | Formats a UNIX timestamp as a date.  
  
## Datetime transformations

Directive | Description  
---|---  
[Current Datetime](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1124434140) | Generates current datetime with a given time zone.  
[Datetime to Timestamp](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1126858858) | Creates a timestamp from datetime and given time zone.  
[Format Datetime](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1124401299) | Formats datetime to a string of a given format.  
[Timestamp to Datetime](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1126858849) | Converts a timestamp to datetime.  
  
## Encoders and decoders

Directive | Description  
---|---  
[Decode](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107710/Decode) | Decodes a column value as one of `base32`, `base64`, or `hex.`  
[Encode](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042182/Encode) | Encodes a column value as one of `base32`, `base64`, or `hex.`  
  
## Hashing and masking

Directive | Description  
---|---  
[Hash](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140542/Hash) | Generates a message digest.  
[Mask Number](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382074995/Mask+Number) | Applies substitution masking on the column values.  
[Mask Shuffle](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075012/Mask+Shuffle) | Applies shuffle masking on the column values.  
  
## Lookups

Directive | Description  
---|---  
[Catalog Lookup](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042113/Catalog+Lookup) | Static catalog lookup of ICD-9, ICD-10-2016, and ICD-10-2017 codes.  
[Table Lookup](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075144/Table+Lookup) | Performs lookups into Table datasets.  
  
## Natural language processing

Directive | Description  
---|---  
[Stemming Tokenized Words](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140736/Stemming) | Applies the Porter stemming algorithm for English words.  
  
## Output Formatters

Directive | Description  
---|---  
[Write as CSV](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075172/Write+as+CSV) | Converts a record into CSV format.  
[Write as JSON Map](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140802/Write+as+JSON+Map) | Converts the record into a JSON map.  
[Write JSON Object](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042460/Write+as+JSON+object) | Composes a JSON object based on the fields specified.  
[Format as Currency](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042228/Format+As+Currency) | Formats a number as currency as specified by locale.  
  
## Parsers

Directive | Description  
---|---  
[JSON Path](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107800/JSON+Path) | Uses a DSL (a JSON path expression) for parsing JSON records.  
[Parse as AVRO File](https://github.com/data-integrations/wrangler/blob/feature/datastage/wrangler-docs/directives/parse-as-avro-file.md) | Parses an AVRO data file.  
[Parse as CSV](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075022/Parse+as+CSV) | Parses an input record as comma-separated values  
[Parse as Currency](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075039/Parse+as+Currency) | Parses a currency value that is a string representation of local currency into a number.  
[Parse as Datetime](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1128988735) | Parses string as datetime data type with a given format.  
[Parse as Excel](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107832/Parse+as+Excel) | Parses into a Microsoft Excel file.  
[Parse as Fixed Length](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042272/Parse+as+Fixed+Length) | Parses as a fixed length record with specified widths.  
[Parse as HL7](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042279/Parse+as+HL7) | Parses Health Level 7 Version 2 (HL7 V2) messages.  
[Parse as JSON](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107862/Parse+as+JSON) | Parses a JSON object.  
[Parse as Log](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/381976753/Parse+as+Log) | Parses access log files, such as Apache httpd and NGINX servers.  
[Parse as Simple Date](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107884/Parse+as+Simple+Date) | Parses date strings.  
[Parse as Timestamp](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107891/Parse+Timestamp) | Parses column values representing unix timestamp as date.  
[Parse XML To JSON](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140609/Parse+XML+to+JSON) | Parses an XML document into a JSON structure.  
  
## Row operations

Directive | Description  
---|---  
[Filter Rows](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/391610418) | Filters records based on a condition.  
[Filter Row if Matched](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042202/Filter+Row+If+Matched) | Filters rows that match a pattern for a column.  
[Flatten](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042221/Flatten) | Separates the elements in a repeated field.  
[Fail on condition](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042192/Fail+on+condition) | Fails processing when the condition is evaluated to true.  
[Send to Error](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042332/Send+to+Error) | Filters records to an error collector.  
[Send to Error and Continue Processing](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140616/Send+to+Error+and+continue+processing) | Filters records to an error collector and continues processing.  
[Split to Rows](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042372/Split+to+Rows) | Splits based on a separator into multiple records.  
  
## Transformations

Directive | Description  
---|---  
[Changing Case](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042120/Change+Column+Case) | Changes the case of column values to uppercase or lowercase characters.  
[Create Record](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1798438913) | Creates a record column with nested values by copying values from source columns into a destination column.  
[Cut Character](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382074928/Cut+Character) | Selects parts of a string value.  
[Set Column](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107931/Set+Column) | Sets the column value to the result of an expression execution.  
[Find and Replace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107735/Find+and+Replace) | Transforms string column values using a "sed"-like expression.  
[Quantization](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042315/Quantize) | Applies quantization to column values.  
[Extract Regex Groups](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382074940/Extract+Regex+Groups) | Extracts the data from a group of regular expressions into its own column.  
[Set Charset](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107924/Set+Charset) | Sets the encoding and then converts the data to a UTF-8 String.  
[Set Record Delim](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042339/Set+Record+Delim) | Sets the record delimiter.  
[Split Email](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/381976826/Split+Email) | Splits an email ID into an account and its domain.  
[Split URL](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042403/Split+URL) | Splits a URL into its constituents.  
[Text Distance (Fuzzy String Match)](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042419/Text+Distance) | Measures the difference between two sequences of characters.  
[Text Metric (Fuzzy String Match)](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107992/Text+Metric) | Measures the difference between two sequences of characters.  
[URL Decode](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382075162/URL+Decode) | Decodes from the `application/x-www-form-urlencoded` MIME format.  
[URL Encode](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042451/URL+Encode) | Encodes to the `application/x-www-form-urlencoded` MIME format.  
[Trimming Spaces](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382042441/Trimming+Spaces) | Functions for trimming white spaces around string data.  
  
## Transient aggregators and setters

Directive | Description  
---|---  
[Increment Variable](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382107767/Increment+variable) | Increments a transient variable with a record of processing.  
[Set Variable](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140645/Set+variable) | Sets a transient variable with a record of processing.  
  
## Unique ID

Directive | Description  
---|---  
[Generate UUID](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/382140532/Generate+UUID) | Generates a universally unique identifier (UUID).  
  
## What's next

  * Learn more about [Wrangler functions](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/380600356/Functions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
