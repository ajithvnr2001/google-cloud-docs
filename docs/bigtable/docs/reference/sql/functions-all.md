---
url: https://docs.cloud.google.com/bigtable/docs/reference/sql/functions-all/
title: Functions (alphabetical) \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:04:36.894334+00:00
---

# Functions (alphabetical)  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/reference/sql/functions-all/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Reference ](https://docs.cloud.google.com/bigtable/docs/apis)



Send feedback 

#  Functions (alphabetical) Stay organized with collections  Save and categorize content based on your preferences. 

This topic contains all functions supported by GoogleSQL for Bigtable.

## Function list

Name | Summary  
---|---  
[`ABS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#abs) |  Computes the absolute value of `X`.   
[`ACOS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#acos) |  Computes the inverse cosine of `X`.   
[`ACOSH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#acosh) |  Computes the inverse hyperbolic cosine of `X`.   
[`ANY_VALUE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#any_value) |  Gets an expression for some row.   
[`APPROX_COUNT_DISTINCT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/approximate_aggregate_functions#approx_count_distinct) |  Gets the approximate result for `COUNT(DISTINCT expression)`.   
[`APPROX_QUANTILES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/approximate_aggregate_functions#approx_quantiles) |  Gets the approximate quantile boundaries.   
[`APPROX_TOP_COUNT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/approximate_aggregate_functions#approx_top_count) |  Gets the approximate top elements and their approximate count.   
[`APPROX_TOP_SUM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/approximate_aggregate_functions#approx_top_sum) |  Gets the approximate top elements and sum, based on the approximate sum of an assigned weight.   
[`ARRAY_AGG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#array_agg) |  Gets an array of values.   
[`ARRAY_CONCAT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_concat) |  Concatenates one or more arrays with the same element type into a single array.   
[`ARRAY_CONCAT_AGG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#array_concat_agg) |  Concatenates arrays and returns a single array as a result.   
[`ARRAY_FILTER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_filter) |  Takes an array, filters out unwanted elements, and returns the results in a new array.   
[`ARRAY_FIRST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_first) |  Gets the first element in an array.   
[`ARRAY_INCLUDES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_includes) |  Checks if there is an element in the array that is equal to a search value.   
[`ARRAY_INCLUDES_ALL`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_includes_all) |  Checks if all search values are in an array.   
[`ARRAY_INCLUDES_ANY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_includes_any) |  Checks if any search values are in an array.   
[`ARRAY_IS_DISTINCT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_is_distinct) |  Checks if an array contains no repeated elements.   
[`ARRAY_LAST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_last) |  Gets the last element in an array.   
[`ARRAY_LAST_N`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_last_n) |  Gets the suffix of an array, consisting of the last `n` elements.   
[`ARRAY_LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_length) |  Gets the number of elements in an array.   
[`ARRAY_OFFSET`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_offset) |  Searches an array from the beginning or ending and produces the zero-based offset for the first matching element.   
[`ARRAY_OFFSETS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_offsets) |  Searches an array and gets the zero-based offsets for matching elements.   
[`ARRAY_REVERSE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_reverse) |  Reverses the order of elements in an array.   
[`ARRAY_SLICE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_slice) |  Produces an array containing zero or more consecutive elements from an input array.   
[`ARRAY_TO_STRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_to_string) |  Produces a concatenation of the elements in an array as a `STRING` value.   
[`ARRAY_TRANSFORM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#array_transform) |  Transforms the elements of an array, and returns the results in a new array.   
[`ASCII`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#ascii) |  Gets the ASCII code for the first character or byte in a `STRING` or `BYTES` value.   
[`ASIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#asin) |  Computes the inverse sine of `X`.   
[`ASINH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#asinh) |  Computes the inverse hyperbolic sine of `X`.   
[`ATAN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#atan) |  Computes the inverse tangent of `X`.   
[`ATAN2`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#atan2) |  Computes the inverse tangent of `X/Y`, using the signs of `X` and `Y` to determine the quadrant.   
[`ATANH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#atanh) |  Computes the inverse hyperbolic tangent of `X`.   
[`AVG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#avg) |  Gets the average of non-`NULL` values.   
[`BIT_AND`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#bit_and) |  Performs a bitwise AND operation on an expression.   
[`BIT_OR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#bit_or) |  Performs a bitwise OR operation on an expression.   
[`BIT_XOR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#bit_xor) |  Performs a bitwise XOR operation on an expression.   
[`BYTE_LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#byte_length) |  Gets the number of `BYTES` in a `STRING` or `BYTES` value.   
[`CAST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_functions#cast) |  Convert the results of an expression to the given type.   
[`CEIL`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#ceil) |  Gets the smallest integral value that isn't less than `X`.   
[`CEILING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#ceiling) |  Synonym of `CEIL`.   
[`CHAR_LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#char_length) |  Gets the number of characters in a `STRING` value.   
[`CHR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#chr) |  Converts a Unicode code point to a character.   
[`CODE_POINTS_TO_BYTES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#code_points_to_bytes) |  Converts an array of extended ASCII code points to a `BYTES` value.   
[`CODE_POINTS_TO_STRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#code_points_to_string) |  Converts an array of extended ASCII code points to a `STRING` value.   
[`CONCAT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#concat) |  Concatenates one or more `STRING` or `BYTES` values into a single result.   
[`CORR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#corr) |  Computes the Pearson coefficient of correlation of a set of number pairs.   
[`COS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#cos) |  Computes the cosine of `X`.   
[`COSH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#cosh) |  Computes the hyperbolic cosine of `X`.   
[`COSINE_DISTANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#cosine_distance) | Computes the cosine distance between two vectors.  
[`COT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#cot) |  Computes the cotangent of `X`.   
[`COTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#coth) |  Computes the hyperbolic cotangent of `X`.   
[`COUNT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#count) |  Gets the number of rows in the input, or the number of rows with an expression evaluated to any value other than `NULL`.   
[`COUNTIF`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#countif) |  Gets the number of `TRUE` values for an expression.   
[`COVAR_POP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#covar_pop) |  Computes the population covariance of a set of number pairs.   
[`COVAR_SAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#covar_samp) |  Computes the sample covariance of a set of number pairs.   
[`CSC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#csc) |  Computes the cosecant of `X`.   
[`CSCH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#csch) |  Computes the hyperbolic cosecant of `X`.   
[`CUME_DIST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#cume_dist) |  Gets the cumulative distribution (relative position (0,1]) of each row within a window.   
[`CURRENT_DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#current_date) |  Returns the current date as a `DATE` value.   
[`CURRENT_TIMESTAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#current_timestamp) |  Returns the current date and time as a `TIMESTAMP` object.   
[`DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date) |  Constructs a `DATE` value.   
[`DATE_ADD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date_add) |  Adds a specified time interval to a `DATE` value.   
[`DATE_DIFF`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date_diff) |  Gets the number of unit boundaries between two `DATE` values at a particular time granularity.   
[`DATE_FROM_UNIX_DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date_from_unix_date) |  Interprets an `INT64` expression as the number of days since 1970-01-01.   
[`DATE_SUB`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date_sub) |  Subtracts a specified time interval from a `DATE` value.   
[`DATE_TRUNC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#date_trunc) |  Truncates a `DATE`, `DATETIME`, or `TIMESTAMP` value at a particular granularity.   
[`DENSE_RANK`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#dense_rank) |  Gets the dense rank (1-based, no gaps) of each row within a window.   
[`DIV`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#div) |  Divides integer `X` by integer `Y`.   
[`ENDS_WITH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#ends_with) |  Checks if a `STRING` or `BYTES` value is the suffix of another value.   
[`EXP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#exp) |  Computes `e` to the power of `X`.   
[`EXTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#extract) |  Extracts part of a date from a `DATE` value.   
[`EXTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#extract) |  Extracts part of a `TIMESTAMP` value.   
[`EUCLIDEAN_DISTANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#euclidean_distance) | Computes the Euclidean distance between two vectors.  
[`FIRST_VALUE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#first_value) |  Gets a value for the first row in the current window frame.   
[`FLOOR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#floor) |  Gets the largest integral value that isn't greater than `X`.   
[`FORMAT_DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#format_date) |  Formats a `DATE` value according to a specified format string.   
[`FORMAT_TIMESTAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#format_timestamp) |  Formats a `TIMESTAMP` value according to the specified format string.   
[`FORMAT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#format_string) |  Formats data and produces the results as a `STRING` value.   
[`FROM_BASE32`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#from_base32) |  Converts a base32-encoded `STRING` value into a `BYTES` value.   
[`FROM_BASE64`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#from_base64) |  Converts a base64-encoded `STRING` value into a `BYTES` value.   
[`FROM_HEX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#from_hex) |  Converts a hexadecimal-encoded `STRING` value into a `BYTES` value.   
[`GENERATE_ARRAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#generate_array) |  Generates an array of values in a range.   
[`GENERATE_DATE_ARRAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#generate_date_array) |  Generates an array of dates in a range.   
[`GENERATE_TIMESTAMP_ARRAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/array_functions#generate_timestamp_array) |  Generates an array of timestamps in a range.   
[`GREATEST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#greatest) |  Gets the greatest value among `X1,...,XN`.   
[`HLL_COUNT.EXTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions#hll_countextract) |  Extracts a cardinality estimate of an HLL++ sketch.   
[`HLL_COUNT.INIT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions#hll_countinit) |  Aggregates values of the same underlying type into a new HLL++ sketch.   
[`HLL_COUNT.MERGE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions#hll_countmerge) |  Merges HLL++ sketches of the same underlying type into a new sketch, and then gets the cardinality of the new sketch.   
[`HLL_COUNT.MERGE_PARTIAL`](https://docs.cloud.google.com/bigtable/docs/reference/sql/hll_functions#hll_countmerge_partial) |  Merges HLL++ sketches of the same underlying type into a new sketch.   
[`IEEE_DIVIDE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#ieee_divide) |  Divides `X` by `Y`, but doesn't generate errors for division by zero or overflow.   
[`IFERROR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/debugging_functions#iferror) |  Evaluates a try expression, and if an evaluation error is produced, returns the result of a catch expression.   
[`INITCAP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#initcap) |  Formats a `STRING` as proper case, which means that the first character in each word is uppercase and all other characters are lowercase.   
[`INSTR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#instr) |  Finds the position of a subvalue inside another value, optionally starting the search at a given offset or occurrence.   
[`IS_INF`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#is_inf) |  Checks if `X` is positive or negative infinity.   
[`IS_NAN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#is_nan) |  Checks if `X` is a `NaN` value.   
[`ISERROR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/debugging_functions#iserror) |  Evaluates a try expression, and if an evaluation error is produced, returns `TRUE`.   
[`JSON_EXTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_extract) |  (Deprecated) Extracts a JSON value and converts it to a SQL JSON-formatted `STRING` value.   
[`JSON_EXTRACT_SCALAR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_extract_scalar) |  (Deprecated) Extracts a JSON scalar value and converts it to a SQL `STRING` value.   
[`JSON_QUERY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_query) |  Extracts a JSON value and converts it to a SQL JSON-formatted `STRING` value.   
[`JSON_QUERY_ARRAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_query_array) |  Extracts a JSON array and converts it to a SQL `ARRAY<JSON-formatted STRING>` value.   
[`JSON_VALUE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#json_value) |  Extracts a JSON scalar value and converts it to a SQL `STRING` value.   
[`LAG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#lag) |  Gets a value for a preceding row.   
[`LAST_DAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#last_day) |  Gets the last day in a specified time period that contains a `DATE` value.   
[`LAST_DAY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/datetime_functions#last_day) |  Gets the last day in a specified time period that contains a `DATETIME` value.   
[`LAST_VALUE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#last_value) |  Gets a value for the last row in the current window frame.   
[`LEAD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#lead) |  Gets a value for a subsequent row.   
[`LEAST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#least) |  Gets the least value among `X1,...,XN`.   
[`LEFT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#left) |  Gets the specified leftmost portion from a `STRING` or `BYTES` value.   
[`LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#length) |  Gets the length of a `STRING` or `BYTES` value.   
[`LN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#ln) |  Computes the natural logarithm of `X`.   
[`LOG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#log) |  Computes the natural logarithm of `X` or the logarithm of `X` to base `Y`.   
[`LOG10`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#log10) |  Computes the natural logarithm of `X` to base 10.   
[`LOGICAL_AND`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#logical_and) |  Gets the logical AND of all non-`NULL` expressions.   
[`LOGICAL_OR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#logical_or) |  Gets the logical OR of all non-`NULL` expressions.   
[`LOWER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#lower) |  Formats alphabetic characters in a `STRING` value as lowercase.   
  
Formats ASCII characters in a `BYTES` value as lowercase.   
[`LPAD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#lpad) |  Prepends a `STRING` or `BYTES` value with a pattern.   
[`LTRIM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#ltrim) |  Identical to the `TRIM` function, but only removes leading characters.   
[`MAP_CONTAINS_KEY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/map-functions#map_contains_key) | Checks if a key is in a map.  
[`MAP_EMPTY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/map-functions#map_empty) | Checks if a map is empty.  
[`MAP_ENTRIES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/map-functions#map_entries) | Gets an array of key-value pairs from a map, sorted in ascending order by key.  
[`MAP_KEYS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/map-functions#map_keys) | Gets an array of keys from a map, sorted in ascending order.  
[`MAP_VALUES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/map-functions#map_values) | Gets an array of values from a map, sorted in ascending order by key.  
[`MAX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#max) |  Gets the maximum non-`NULL` value.   
[`MIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#min) |  Gets the minimum non-`NULL` value.   
[`MOD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#mod) |  Gets the remainder of the division of `X` by `Y`.   
[`NORMALIZE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#normalize) |  Case-sensitively normalizes the characters in a `STRING` value.   
[`NORMALIZE_AND_CASEFOLD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#normalize_and_casefold) |  Case-insensitively normalizes the characters in a `STRING` value.   
[`NTH_VALUE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#nth_value) |  Gets a value for the Nth row of the current window frame.   
[`NTILE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#ntile) |  Gets the quantile bucket number (1-based) of each row within a window.   
[`NULLIFERROR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/debugging_functions#nulliferror) |  Evaluates a try expression, and if an evaluation error is produced, returns `NULL`.   
[`OCTET_LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#octet_length) |  Alias for `BYTE_LENGTH`.   
[`PARSE_DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#parse_date) |  Converts a `STRING` value to a `DATE` value.   
[`PARSE_TIMESTAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#parse_timestamp) |  Converts a `STRING` value to a `TIMESTAMP` value.   
[`PERCENT_RANK`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#percent_rank) |  Gets the percentile rank (from 0 to 1) of each row within a window.   
[`PERCENTILE_CONT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#percentile_cont) |  Computes the specified percentile for a value, using linear interpolation.   
[`PERCENTILE_DISC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/navigation_functions#percentile_disc) |  Computes the specified percentile for a discrete value.   
[`POW`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#pow) |  Produces the value of `X` raised to the power of `Y`.   
[`POWER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#power) |  Synonym of `POW`.   
[`RAND`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#rand) |  Generates a pseudo-random value of type `FLOAT64` in the range of `[0, 1)`.   
[`RANK`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#rank) |  Gets the rank (1-based) of each row within a window.   
[`REGEXP_CONTAINS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#regexp_contains) |  Checks if a value is a partial match for a regular expression.   
[`REGEXP_EXTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#regexp_extract) |  Produces a substring that matches a regular expression.   
[`REGEXP_EXTRACT_ALL`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#regexp_extract_all) |  Produces an array of all substrings that match a regular expression.   
[`REGEXP_INSTR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#regexp_instr) |  Finds the position of a regular expression match in a value, optionally starting the search at a given offset or occurrence.   
[`REGEXP_REPLACE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#regexp_replace) |  Produces a `STRING` value where all substrings that match a regular expression are replaced with a specified value.   
[`REPEAT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#repeat) |  Produces a `STRING` or `BYTES` value that consists of an original value, repeated.   
[`REPLACE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#replace) |  Replaces all occurrences of a pattern with another pattern in a `STRING` or `BYTES` value.   
[`REVERSE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#reverse) |  Reverses a `STRING` or `BYTES` value.   
[`RIGHT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#right) |  Gets the specified rightmost portion from a `STRING` or `BYTES` value.   
[`ROUND`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#round) |  Rounds `X` to the nearest integer or rounds `X` to `N` decimal places after the decimal point.   
[`ROW_NUMBER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/numbering_functions#row_number) |  Gets the sequential row number (1-based) of each row within a window.   
[`RPAD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#rpad) |  Appends a `STRING` or `BYTES` value with a pattern.   
[`RTRIM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#rtrim) |  Identical to the `TRIM` function, but only removes trailing characters.   
[`S2_CELLIDFROMPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#s2_cellidfrompoint) |  Gets the S2 cell ID covering a point `GEOGRAPHY` value.   
[`S2_COVERINGCELLIDS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#s2_coveringcellids) |  Gets an array of S2 cell IDs that cover a `GEOGRAPHY` value.   
[`SAFE_ADD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_add) |  Equivalent to the addition operator (`X + Y`), but returns `NULL` if overflow occurs.   
[`SAFE_CAST`](https://docs.cloud.google.com/bigtable/docs/reference/sql/conversion_functions#safe_casting) |  Similar to the `CAST` function, but returns `NULL` when a runtime error is produced.   
[`SAFE_CONVERT_BYTES_TO_STRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#safe_convert_bytes_to_string) |  Converts a `BYTES` value to a `STRING` value and replace any invalid UTF-8 characters with the Unicode replacement character, `U+FFFD`.   
[`SAFE_DIVIDE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_divide) |  Equivalent to the division operator (`X / Y`), but returns `NULL` if an error occurs.   
[`SAFE_MULTIPLY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_multiply) |  Equivalent to the multiplication operator (`X * Y`), but returns `NULL` if overflow occurs.   
[`SAFE_NEGATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_negate) |  Equivalent to the unary minus operator (`-X`), but returns `NULL` if overflow occurs.   
[`SAFE_SUBTRACT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#safe_subtract) |  Equivalent to the subtraction operator (`X - Y`), but returns `NULL` if overflow occurs.   
[`SEC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sec) |  Computes the secant of `X`.   
[`SECH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sech) |  Computes the hyperbolic secant of `X`.   
[`SIGN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sign) |  Produces -1 , 0, or +1 for negative, zero, and positive arguments respectively.   
[`SIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sin) |  Computes the sine of `X`.   
[`SINH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sinh) |  Computes the hyperbolic sine of `X`.   
[`SOUNDEX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#soundex) |  Gets the Soundex codes for words in a `STRING` value.   
[`SPLIT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#split) |  Splits a `STRING` or `BYTES` value, using a delimiter.   
[`SQRT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#sqrt) |  Computes the square root of `X`.   
[`ST_ACCUM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_accum) |  Aggregates `GEOGRAPHY` values into an array of `GEOGRAPHY` elements.   
[`ST_ANGLE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_angle) |  Takes three point `GEOGRAPHY` values, which represent two intersecting lines, and returns the angle between these lines.   
[`ST_AREA`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_area) |  Gets the area covered by the polygons in a `GEOGRAPHY` value.   
[`ST_ASBINARY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_asbinary) |  Converts a `GEOGRAPHY` value to a `BYTES` WKB geography value.   
[`ST_ASGEOJSON`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_asgeojson) |  Converts a `GEOGRAPHY` value to a `STRING` GeoJSON geography value.   
[`ST_ASKML`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_askml) |  Converts a `GEOGRAPHY` value to a `STRING` KML geometry value.   
[`ST_ASTEXT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_astext) |  Converts a `GEOGRAPHY` value to a `STRING` WKT geography value.   
[`ST_AZIMUTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_azimuth) |  Gets the azimuth of a line segment formed by two point `GEOGRAPHY` values.   
[`ST_BOUNDARY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_boundary) |  Gets the union of component boundaries in a `GEOGRAPHY` value.   
[`ST_BOUNDINGBOX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_boundingbox) |  Gets the bounding box for a `GEOGRAPHY` value.   
[`ST_BUFFER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_buffer) |  Gets the buffer around a `GEOGRAPHY` value, using a specific number of segments.   
[`ST_BUFFERWITHTOLERANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_bufferwithtolerance) |  Gets the buffer around a `GEOGRAPHY` value, using tolerance.   
[`ST_CENTROID`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_centroid) |  Gets the centroid of a `GEOGRAPHY` value.   
[`ST_CLOSESTPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_closestpoint) |  Gets the point on a `GEOGRAPHY` value which is closest to any point in a second `GEOGRAPHY` value.   
[`ST_CONTAINS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_contains) |  Checks if one `GEOGRAPHY` value contains another `GEOGRAPHY` value.   
[`ST_CONVEXHULL`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_convexhull) |  Returns the convex hull for a `GEOGRAPHY` value.   
[`ST_COVEREDBY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_coveredby) |  Checks if all points of a `GEOGRAPHY` value are on the boundary or interior of another `GEOGRAPHY` value.   
[`ST_COVERS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_covers) |  Checks if all points of a `GEOGRAPHY` value are on the boundary or interior of another `GEOGRAPHY` value.   
[`ST_DIFFERENCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_difference) |  Gets the point set difference between two `GEOGRAPHY` values.   
[`ST_DIMENSION`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_dimension) |  Gets the dimension of the highest-dimensional element in a `GEOGRAPHY` value.   
[`ST_DISJOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_disjoint) |  Checks if two `GEOGRAPHY` values are disjoint (don't intersect).   
[`ST_DISTANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_distance) |  Gets the shortest distance in meters between two `GEOGRAPHY` values.   
[`ST_DUMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_dump) |  Returns an array of simple `GEOGRAPHY` components in a `GEOGRAPHY` value.   
[`ST_DUMPPOINTS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_dumppoints) |  Produces an array of `GEOGRAPHY` points with all points, line vertices, and polygon vertices in a `GEOGRAPHY` value.   
[`ST_DWITHIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_dwithin) |  Checks if any points in two `GEOGRAPHY` values are within a given distance.   
[`ST_ENDPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_endpoint) |  Gets the last point of a linestring `GEOGRAPHY` value.   
[`ST_EQUALS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_equals) |  Checks if two `GEOGRAPHY` values represent the same `GEOGRAPHY` value.   
[`ST_EXTENT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_extent) |  Gets the bounding box for a group of `GEOGRAPHY` values.   
[`ST_EXTERIORRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_exteriorring) |  Returns a linestring `GEOGRAPHY` value that corresponds to the outermost ring of a polygon `GEOGRAPHY` value.   
[`ST_GEOGFROM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogfrom) |  Converts a `STRING` or `BYTES` value into a `GEOGRAPHY` value.   
[`ST_GEOGFROMGEOJSON`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogfromgeojson) |  Converts a `STRING` GeoJSON geometry value into a `GEOGRAPHY` value.   
[`ST_GEOGFROMKML`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogfromkml) |  Converts a `STRING` KML geometry value into a `GEOGRAPHY` value.   
[`ST_GEOGFROMTEXT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogfromtext) |  Converts a `STRING` WKT geometry value into a `GEOGRAPHY` value.   
[`ST_GEOGFROMWKB`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogfromwkb) |  Converts a `BYTES` or hexadecimal-text `STRING` WKT geometry value into a `GEOGRAPHY` value.   
[`ST_GEOGPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogpoint) |  Creates a point `GEOGRAPHY` value for a given longitude and latitude.   
[`ST_GEOGPOINTFROMGEOHASH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geogpointfromgeohash) |  Gets a point `GEOGRAPHY` value that's in the middle of a bounding box defined in a `STRING` GeoHash value.   
[`ST_GEOHASH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geohash) |  Converts a point `GEOGRAPHY` value to a `STRING` GeoHash value.   
[`ST_GEOMETRYTYPE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_geometrytype) |  Gets the Open Geospatial Consortium (OGC) geometry type for a `GEOGRAPHY` value.   
[`ST_HAUSDORFFDISTANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_hausdorffdistance) | Gets the discrete Hausdorff distance between two geometries.  
[`ST_HAUSDORFFDWITHIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_hausdorffdwithin) |  Checks if the Hausdorff distance between two `GEOGRAPHY` values is within a given distance.   
[`ST_INTERIORRINGS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_interiorrings) |  Gets the interior rings of a polygon `GEOGRAPHY` value.   
[`ST_INTERSECTION`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_intersection) |  Gets the point set intersection of two `GEOGRAPHY` values.   
[`ST_INTERSECTS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_intersects) |  Checks if at least one point appears in two `GEOGRAPHY` values.   
[`ST_INTERSECTSBOX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_intersectsbox) |  Checks if a `GEOGRAPHY` value intersects a rectangle.   
[`ST_ISCLOSED`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_isclosed) |  Checks if all components in a `GEOGRAPHY` value are closed.   
[`ST_ISCOLLECTION`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_iscollection) |  Checks if the total number of points, linestrings, and polygons is greater than one in a `GEOGRAPHY` value.   
[`ST_ISEMPTY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_isempty) |  Checks if a `GEOGRAPHY` value is empty.   
[`ST_ISRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_isring) |  Checks if a `GEOGRAPHY` value is a closed, simple linestring.   
[`ST_LENGTH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_length) |  Gets the total length of lines in a `GEOGRAPHY` value.   
[`ST_LINEINTERPOLATEPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_lineinterpolatepoint) |  Gets a point at a specific fraction in a linestring `GEOGRAPHY` value.   
[`ST_LINELOCATEPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_linelocatepoint) |  Gets a section of a linestring `GEOGRAPHY` value between the start point and a point `GEOGRAPHY` value.   
[`ST_LINESUBSTRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_linesubstring) |  Gets a segment of a single linestring at a specific starting and ending fraction.   
[`ST_MAKELINE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_makeline) |  Creates a linestring `GEOGRAPHY` value by concatenating the point and linestring vertices of `GEOGRAPHY` values.   
[`ST_MAKEPOLYGON`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_makepolygon) |  Constructs a polygon `GEOGRAPHY` value by combining a polygon shell with polygon holes.   
[`ST_MAKEPOLYGONORIENTED`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_makepolygonoriented) |  Constructs a polygon `GEOGRAPHY` value, using an array of linestring `GEOGRAPHY` values. The vertex ordering of each linestring determines the orientation of each polygon ring.   
[`ST_MAXDISTANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_maxdistance) |  Gets the longest distance between two non-empty `GEOGRAPHY` values.   
[`ST_NPOINTS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_npoints) |  An alias of `ST_NUMPOINTS`.   
[`ST_NUMGEOMETRIES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_numgeometries) |  Gets the number of geometries in a `GEOGRAPHY` value.   
[`ST_NUMPOINTS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_numpoints) |  Gets the number of vertices in the a `GEOGRAPHY` value.   
[`ST_PERIMETER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_perimeter) |  Gets the length of the boundary of the polygons in a `GEOGRAPHY` value.   
[`ST_POINTN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_pointn) |  Gets the point at a specific index of a linestring `GEOGRAPHY` value.   
[`ST_REGIONSTATS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_regionstats) |  Computes statistics describing the pixels in a geospatial raster image that intersect a `GEOGRAPHY` value.  
[`ST_SIMPLIFY`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_simplify) |  Converts a `GEOGRAPHY` value into a simplified `GEOGRAPHY` value, using tolerance.   
[`ST_SNAPTOGRID`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_snaptogrid) |  Produces a `GEOGRAPHY` value, where each vertex has been snapped to a longitude/latitude grid.   
[`ST_STARTPOINT`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_startpoint) |  Gets the first point of a linestring `GEOGRAPHY` value.   
[`ST_TOUCHES`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_touches) |  Checks if two `GEOGRAPHY` values intersect and their interiors have no elements in common.   
[`ST_UNION`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_union) |  Gets the point set union of multiple `GEOGRAPHY` values.   
[`ST_UNION_AGG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_union_agg) |  Aggregates over `GEOGRAPHY` values and gets their point set union.   
[`ST_WITHIN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/geography_functions#st_within) |  Checks if one `GEOGRAPHY` value contains another `GEOGRAPHY` value.   
[`STARTS_WITH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#starts_with) |  Checks if a `STRING` or `BYTES` value is a prefix of another value.   
[`STDDEV`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#stddev) |  An alias of the `STDDEV_SAMP` function.   
[`STDDEV_POP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#stddev_pop) |  Computes the population (biased) standard deviation of the values.   
[`STDDEV_SAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#stddev_samp) |  Computes the sample (unbiased) standard deviation of the values.   
[`STRING` (Timestamp)](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#string) |  Converts a `TIMESTAMP` value to a `STRING` value.   
[`STRING_AGG`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#string_agg) |  Concatenates non-`NULL` `STRING` or `BYTES` values.   
[`STRPOS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#strpos) |  Finds the position of the first occurrence of a subvalue inside another value.   
[`SUBSTR`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#substr) |  Gets a portion of a `STRING` or `BYTES` value.   
[`SUBSTRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#substring) | Alias for `SUBSTR`  
[`SUM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/aggregate_functions#sum) |  Gets the sum of non-`NULL` values.   
[`TAN`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#tan) |  Computes the tangent of `X`.   
[`TANH`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#tanh) |  Computes the hyperbolic tangent of `X`.   
[`Temporal filters`](https://docs.cloud.google.com/bigtable/docs/reference/sql/table-functions-built-in#temporal_filters) |  Access temporal elements of a table by using the Bigtable table name as a function.   
[`TIMESTAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp) |  Constructs a `TIMESTAMP` value.   
[`TIMESTAMP_ADD`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_add) |  Adds a specified time interval to a `TIMESTAMP` value.   
[`TIMESTAMP_DIFF`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_diff) |  Gets the number of unit boundaries between two `TIMESTAMP` values at a particular time granularity.   
[`TIMESTAMP_FROM_UNIX_MICROS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_from_unix_micros) |  Similar to `TIMESTAMP_MICROS`, except that additionally, a `TIMESTAMP` value can be passed in.   
[`TIMESTAMP_FROM_UNIX_MILLIS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_from_unix_millis) |  Similar to `TIMESTAMP_MILLIS`, except that additionally, a `TIMESTAMP` value can be passed in.   
[`TIMESTAMP_FROM_UNIX_SECONDS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_from_unix_seconds) |  Similar to `TIMESTAMP_SECONDS`, except that additionally, a `TIMESTAMP` value can be passed in.   
[`TIMESTAMP_MICROS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_micros) |  Converts the number of microseconds since 1970-01-01 00:00:00 UTC to a `TIMESTAMP`.   
[`TIMESTAMP_MILLIS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_millis) |  Converts the number of milliseconds since 1970-01-01 00:00:00 UTC to a `TIMESTAMP`.   
[`TIMESTAMP_SECONDS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_seconds) |  Converts the number of seconds since 1970-01-01 00:00:00 UTC to a `TIMESTAMP`.   
[`TIMESTAMP_SUB`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_sub) |  Subtracts a specified time interval from a `TIMESTAMP` value.   
[`TIMESTAMP_TRUNC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#timestamp_trunc) |  Truncates a `TIMESTAMP` or `DATETIME` value at a particular granularity.   
[`TO_BASE32`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_base32) |  Converts a `BYTES` value to a base32-encoded `STRING` value.   
[`TO_BASE64`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_base64) |  Converts a `BYTES` value to a base64-encoded `STRING` value.   
[`TO_CODE_POINTS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_code_points) |  Converts a `STRING` or `BYTES` value into an array of extended ASCII code points.   
[`TO_FLOAT32`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_float32) |  Converts the big-endian bytes of a 32-bit IEEE 754 floating point number into a `FLOAT32` value.   
[`TO_FLOAT64`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_float64) |  Converts the big-endian bytes of a 64-bit IEEE 754 floating point number into a `FLOAT64` value.   
[`TO_HEX`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_hex) |  Converts a `BYTES` value to a hexadecimal `STRING` value.   
[`TO_INT64`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_int64) |  Converts the big-endian bytes of a 64-bit signed integer into an `INT64` value.   
[`TO_JSON_STRING`](https://docs.cloud.google.com/bigtable/docs/reference/sql/json_functions#to_json_string) |  Converts a SQL value to a JSON-formatted `STRING` value.   
[`TO_VECTOR32`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_vector32) |  Converts the big-endian bytes of one or more 32-bit IEEE 754 floating point numbers into an `ARRAY<FLOAT32>` value.   
[`TO_VECTOR64`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#to_vector64) |  Converts the big-endian bytes of one or more 64-bit IEEE 754 floating point numbers into an `ARRAY<FLOAT64>` value.   
[`TRANSLATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#translate) |  Within a value, replaces each source character with the corresponding target character.   
[`TRIM`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#trim) |  Removes the specified leading and trailing Unicode code points or bytes from a `STRING` or `BYTES` value.   
[`TRUNC`](https://docs.cloud.google.com/bigtable/docs/reference/sql/mathematical_functions#trunc) |  Rounds a number like `ROUND(X)` or `ROUND(X, N)`, but always rounds towards zero and never overflows.   
[`UNICODE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#unicode) |  Gets the Unicode code point for the first character in a value.   
[`UNIX_DATE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/date_functions#unix_date) |  Converts a `DATE` value to the number of days since 1970-01-01.   
[`UNIX_MICROS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#unix_micros) |  Converts a `TIMESTAMP` value to the number of microseconds since 1970-01-01 00:00:00 UTC.   
[`UNIX_MILLIS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#unix_millis) |  Converts a `TIMESTAMP` value to the number of milliseconds since 1970-01-01 00:00:00 UTC.   
[`UNIX_SECONDS`](https://docs.cloud.google.com/bigtable/docs/reference/sql/timestamp_functions#unix_seconds) |  Converts a `TIMESTAMP` value to the number of seconds since 1970-01-01 00:00:00 UTC.   
[`UNPACK`](https://docs.cloud.google.com/bigtable/docs/reference/sql/table-functions-built-in#unpack) |  Expands the timestamped values in an input row into multiple rows, each row representing a different timestamp; and moves the timestamps into a `_timestamp` column.   
[`UPPER`](https://docs.cloud.google.com/bigtable/docs/reference/sql/string_functions#upper) |  Formats alphabetic characters in a `STRING` value as uppercase.   
  
Formats ASCII characters in a `BYTES` value as uppercase.   
[`VAR_POP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#var_pop) |  Computes the population (biased) variance of the values.   
[`VAR_SAMP`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#var_samp) |  Computes the sample (unbiased) variance of the values.   
[`VARIANCE`](https://docs.cloud.google.com/bigtable/docs/reference/sql/statistical_aggregate_functions#variance) |  An alias of `VAR_SAMP`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
