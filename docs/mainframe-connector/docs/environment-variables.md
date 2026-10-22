---
url: https://docs.cloud.google.com/mainframe-connector/docs/environment-variables/
title: Mainframe Connector environment variables \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:12.199064+00:00
---

# Mainframe Connector environment variables  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Mainframe Connector environment variables Stay organized with collections  Save and categorize content based on your preferences. 

This page lists all the environment variables that Mainframe Connector supports. Depending on the version of the Mainframe Connector, some variables might not be supported. For more details, see the **Available from version** column in the following table.

Name | Default value | Available from version | Description  
---|---|---|---  
  
###### `BQSH_FEATURE_TRIM_STRING_SUFFIX`

| `True` | 5.8.0 | Trims the whitespace at the end of strings. Note that strings that consist only of whitespaces are treated as empty strings.  
  
###### `ENCODING`

| `cp037` | 5.8.0 | Specifies the character encoding used for encoding and decoding.  
  
###### `BQ_QUERY_REMOTE_EXECUTION`

| `False` | 5.10.0 | Configures `bq query` to run in remote mode.  
  
###### `BQSH_FEATURE_VARIABLE_LENGTH_ENABLED`

| `False` | 5.11.0 | Enables support for [variable-length character strings](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#variable-length-strings) when set to True.  
  
###### `BQSH_FEATURE_VARIABLE_LENGTH_LEN_SUFFIX`

| `-LEN` | 5.11.0 | Relevant if `BQSH_FEATURE_VARIABLE_LENGTH_ENABLED` is set. Represents the suffix of the first parameter in the variable-length character struct. By default, the suffix is `-LEN`. If you want to use a different suffix, set this environment variable to the suffix of your choice.   
  
###### `BQSH_FEATURE_VARIABLE_LENGTH_DATA_SUFFIX`

| `-TEXT` | 5.11.0 | Relevant if `BQSH_FEATURE_VARIABLE_LENGTH_ENABLED` is set. Represents the suffix of the second parameter in the variable-length character struct. By default, the suffix is `-TEXT`. If you want to use a different suffix, set this environment variable to the suffix of your choice.   
  
###### `SUFFIX_SUFFIX_STRING`

|  \-  | 5.11.0/5.13.0 |  (5.13.0 and onwards) Sets the values for the date, timestamp, and null indicator data types.   
  
Use the following format to set the null indicator: `SUFFIX_NULL_INDICATOR_NAME="command --null-value NULL_VALUE --not-null-value NOT_NULL_VALUE"`   
  
Use the following format to set the date and timestamp: `SUFFIX_SUFFIX_NAME="command --format FORMAT --timezone TIMEZONE"`   
  
For more information, see [Support for date and timestamp fields](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#date-timestamp) and [Support for null indicator fields](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator).   
  
(5.11.0 and onwards) Sets the values for the date and timestamp data types. You can set this environment variable to any value in the following format: `SUFFIX_SUFFIX_STRING="--bqtype TYPE --format FORMAT --timezone TIMEZONE"`  
  
###### `BQSH_FEATURE_CONVERT_UNDERSCORE_IN_FIELDS_NAME`

| True | 5.12.0 | Replaces hyphens in the field names in the [COPYBOOK](https://docs.cloud.google.com/mainframe-connector/docs/reference#dataset-names) to underscores in the corresponding field names in BigQuery.  
  
###### `BQSH_FEATURE_EMPTY_STRING_AS_NULL`

| True | 5.12.0 | Exports strings with a length of 0 as null to BigQuery. If you set `BQSH_FEATURE_EMPTY_STRING_AS_NULL` to false, then an empty string remains as an empty string when it is exported to BigQuery (an empty string won't be set to null).  
  
###### `BQSH_FEATURE_FAIL_ON_INVALID_DATA`

| False | 5.12.1/5.13.0 | (5.13.0 and onwards) Lets you enforce stricter error handling, as follows: 

  * Raise an error when parsing date and timestamp types that contain spaces (or are invalid dates or timestamps). 
  * Raise an error when decoding an invalid byte in a packed decimal type or a zoned decimal type. This includes values that contain only nulls, spaces, or high bytes.

  
(5.12.1 and onwards) Lets you enforce stricter error handling, as follows: 

  * Raise an error when parsing date and timestamp types that contain spaces (or are invalid dates or timestamps).
  * Raise an error when decoding an invalid byte in a packed decimal type. If a value only contains nulls (0x00) or spaces (0x40), it is decoded to null and does not throw an error for packed decimal, even if this flag is set to true.

  
  
###### `BQSH_FEATURE_EMPTY_VALUES_ARE_NULL`

| True | 5.13.0 | Specifies that values containing only nulls (0x00), spaces (0x40), or high bytes (0xFF) should be decoded as null, and not throw an error for packed decimal and zoned decimal types. This flag only has an effect if `BQSH_FEATURE_FAIL_ON_INVALID_DATA` is set to true. Otherwise, it does not impact the behavior of the decoders or encoders.  
  
###### `OVERRIDE_GRPC_WINDOW_MB`

| False | 5.13.0 | Increases or decreases the window size of the HTTP/2 flow control.  
  
###### `BQSH_FEATURE_TERMINATE_STRINGS_ON_NULL`

| True | 5.14.0 | If not set, or if true, the `DISPLAY`, `NATIONAL`, `DBCS`, and `UTF8` fields interpret null bytes as an end-of-string indicator and ignore the remaining bytes. If set to false, null bytes are decoded according to the used character set.  
  
###### `BQSH_FEATURE_CUSTOM_CHARSET`

| Empty string | 5.14.0 | Set path to a [customized character set](https://docs.cloud.google.com/mainframe-connector/docs/api-reference#customized-charsets). If you want to use multiple character sets, you can provide the paths to multiple characters sets separated by the semi-colon delimiter. For example, `export BQSH_FEATURE_CUSTOM_CHARSET=path1;path2`.  
  
###### `DISABLE_ANALYTICS`

| False | 5.15.0 | Disable Google Analytics.  
  
###### `BQSH_FEATURE_RESPECT_FILLER_ON_EXPORT`

| False | 5.15.1 | Populate `FILLER` fields in a BigQuery export operation. If you set `BQSH_FEATURE_RESPECT_FILLER_ON_EXPORT` to true, Mainframe Connector assigns `FILLER` values based on the results of the BigQuery query. For example, `SELECT f1, '|', f2 … from TABLE`. The `FILLER` value in this case will be set as `|`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
