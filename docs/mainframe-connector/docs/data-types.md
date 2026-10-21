---
url: https://docs.cloud.google.com/mainframe-connector/docs/data-types/
title: Mainframe Connector data types \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:47:43.304699+00:00
---

# Mainframe Connector data types  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-connector/docs/data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Connector ](https://docs.cloud.google.com/mainframe-connector/docs)
  * [ Reference ](https://docs.cloud.google.com/mainframe-connector/docs/reference)



Send feedback 

#  Mainframe Connector data types Stay organized with collections  Save and categorize content based on your preferences. 

The following tables lists all the data types that Mainframe Connector supports.

COBOL usage type | Supported flags | Condition | Optimized Row Columnar (ORC)​​ type | Type | Decoding behavior (`gsutil cp`) | Encoding behavior (`bq export`)  
---|---|---|---|---|---|---  
  
###### `COMP1`, `COMP2`

|  |  | Double | `FLOAT64` |  | Encodes the `String`, `Double`, and `Float` data types.  
  
###### `BINARY`, `SIGNED`

|  | If signed | Long | `INT64` |  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `Integer`, and `Long` data types.  
  
###### `BINARY`, `UNSIGNED`

|  | If unsigned | Long | `INT64` |  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `Integer`, and `Long` data types.  
  
###### `DISPLAY`

| [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) | If all the following condition are satisfied: 

  * Name ends with `_BT` or `-BT.`
  * Picture not numeric.
  * There is either no field modifier or `NULL_INDICATOR`.

| Bytes | `BYTES` | Is never stored as `NULL`. | If the value is `NULL`, returns an empty byte array.  
  
###### `DISPLAY`

| [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) | [DATE](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#date-timestamp) field which uses the [DATE_CONVERTER](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#date-timestamp) command | Date | `DATE` | If an invalid date and `FAIL_ON_INVALID_DATA` is set, an error is displayed and the record is ignored. | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `LocalDate`, and `Date` data types.  
  
###### `DISPLAY`

| [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) | [TIMESTAMP](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#date-timestamp) field which uses the [TIMESTAMP_CONVERTER](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#date-timestamp) command | Timestamp | `TIMESTAMP` | If an invalid date and `FAIL_ON_INVALID_DATA` is set, an error is displayed and the record is ignored. | If the value is `NULL`, returns an empty byte array. Encodes the `String` and `Timestamp` data types.  
  
###### `DISPLAY (*)`

| [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) [EMPTY_STRING_AS_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_string_as_null) [TRIM_STRING_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_trim_string_suffix) | Picture not numeric, if any. If pictures contains the following: 

  * `N` and `NSYMBOL == NATIONAL` use `UTF-16BE`
  * `N` and `NSYMBOL == DBCS` act as `DISPLAY-1`
  * `U` uses `UTF8`

| Bytes | `STRING` | The following character set transformation is performed:   
First, bytes are decoded into characters, and then those characters are encoded into UTF-8-based bytes stored into the column vector. Depending on the `EMPTY_STRING_AS_NULL`, data is stored as `NULL`. Depending on `TRIM_STRING_SUFFIX`, trailing whitespaces and low values are trimmed.  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `LocalDate`, `BigDecimal`, and `Timestamp` data types.  
  
###### `DISPLAY-1`

| [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) [EMPTY_STRING_AS_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_string_as_null) [TRIM_STRING_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_trim_string_suffix) | If the field name ends with `_DBCS` or `-DBCS` then use shift-out, shift-in encoding.  | Bytes | `STRING` | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3) | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3)  
  
###### `NATIONAL`

| [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) [EMPTY_STRING_AS_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_string_as_null) [TRIM_STRING_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_trim_string_suffix) | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3) | Bytes | `STRING` | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3) | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3)  
  
###### `UTF8`

| [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) [EMPTY_STRING_AS_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_string_as_null) [TRIM_STRING_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_trim_string_suffix) | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3) | Bytes | `STRING` | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3) | See [DISPLAY (*)](https://docs.cloud.google.com/mainframe-connector/docs/data-types#display_3)  
  
###### `DISPLAY (GROUP)`

| [VARIABLE_LENGTH_ENABLED](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_variable_length_enabled) [VARIABLE_LENGTH_LEN_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_variable_length_len_suffix) [VARIABLE_LENGTH_DATA_SUFFIX](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_variable_length_data_suffix) | If `VARIABLE_LENGTH_ENABLED` is set, the field is of variable length, and marked by a group structure of two or three fields, depending on an extra [NULL_INDICATOR](https://docs.cloud.google.com/mainframe-connector/docs/copybook-reference#null-indicator) field: 

  * The first field either ends with `-LEN` or with the value set by `VARIABLE_LENGTH_LEN_SUFFIX`. 
  * The second field either ends with `-TEXT` or with the value set by `VARIABLE_LENGTH_DATA_SUFFIX`.

| Bytes | `STRING` | The data part is decoded as `DISPLAY`, but is never stored as `NULL`. | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `LocalDate`, and `BigDecimal` data types.  
  
###### `PACKED DECIMAL`

| [EMPTY_VALUES_ARE_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_values_are_null) [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) |  | Decimal64 | `NUMERIC` | Decode as `NULL`, if all the bytes are: 

  * Either spaces, high, or low, and
  * Not `FAIL_ON_INVALID_DATA` or,
  * `FAIL_ON_INVALID_DATA` and,
  * `EMPTY_VALUES_ARE_NULL`.

  
If the data is invalid, and `FAIL_ON_INVALID_DATA` is set, an error is displayed, and the record is ignored.  | If the value is `NULL`, returns an empty byte array. Encodes the `String` and `BigDecimal` data type.  
  
###### `ZONED`

| [EMPTY_VALUES_ARE_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_values_are_null) [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) | `precision <= 18 && scale == 0` | Long | `INT64` | Decode as `NULL`, if all the bytes are: 

  * Either spaces, high, or low, and
  * Not `FAIL_ON_INVALID_DATA` or,
  * `FAIL_ON_INVALID_DATA` and,
  * `EMPTY_VALUES_ARE_NULL`.

  
If the data is invalid, and `FAIL_ON_INVALID_DATA` is set, an error is displayed, and the record is ignored.   
Decode into `long` assuming `EBCDIC` encoding for The `sign` nibble.  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `Long` and `BigDecimal` data types.  
  
###### `ZONED`

| [EMPTY_VALUES_ARE_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_values_are_null) [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) | `precision <= 18` | Decimal64 | `NUMERIC` | Decode as `NULL`, if all the bytes are: 

  * Either spaces, high, or low, and,
  * Not `FAIL_ON_INVALID_DATA` or,
  * `FAIL_ON_INVALID_DATA` and,
  * `EMPTY_VALUES_ARE_NULL`.

  
If the data is invalid, and `FAIL_ON_INVALID_DATA` is set, an error is displayed, and the record is ignored.   
Decode into `long` assuming `EBCDIC` encoding for `sign` nibble.  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `Long` and `BigDecimal` data types.  
  
###### `ZONED`

| [EMPTY_VALUES_ARE_NULL](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_empty_values_are_null) [FAIL_ON_INVALID_DATA](https://docs.cloud.google.com/mainframe-connector/docs/environment-variables#bqsh_feature_fail_on_invalid_data) | `18 < precision <= 38` | Decimal | `BIGNUMERIC` | Decode as `NULL`, if all the bytes are: 

  * Either spaces, high, or low, and,
  * Not `FAIL_ON_INVALID_DATA` or,
  * `FAIL_ON_INVALID_DATA` and,
  * `EMPTY_VALUES_ARE_NULL`.

  
If the data is invalid, and `FAIL_ON_INVALID_DATA` is set, an error is displayed, and the record is ignored.   
Decode into `long` assuming `EBCDIC` encoding for `sign` nibble.  | If the value is `NULL`, returns an empty byte array. Encodes the `String`, `Long`, `BigInteger`, and `BigDecimal` data type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
