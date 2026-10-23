---
url: https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference/
title: Data Mapping functions \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:04.470123+00:00
---

# Data Mapping functions  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/data-mapping-functions-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Reference ](https://docs.cloud.google.com/application-integration/docs/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data Mapping functions

The [**Data Mapping** task](https://docs.cloud.google.com/application-integration/docs/configure-data-mapping-task) provides various predefined mapping functions to transform and standardize the mapping data in your integration. A mapping function can have one or more input parameters, wherein each parameter can further hold a literal value, a variable, or a base function with mapping functions applied. You can use multiple mapping functions for a single input source, forming a mapping [transform expression](https://docs.cloud.google.com/application-integration/docs/data-mapping-overview#transform).

The following table lists the predefined mapping functions available in the **Data Mapping** task. 

Function | Description  
---|---  
[`ADD`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/add-function-reference) | Adds the specified number to an existing number.  
[`AND`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/and-function-reference) | Performs the logical AND operation on the specified boolean values.  
[`APPEND`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/append-function-reference) | Appends the specified value to an array.  
[`APPEND_ALL`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/append-all-function-reference) | Appends all the specified values to an array.  
[`APPEND_ELEMENT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/append-element-function-reference) | Appends an element to a JSON array.  
[`AVG`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/avg-function-reference) | Calculates the numerical average of all the values in an array.  
[`CEIL`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/ceil-function-reference) | Computes the smallest integer that is greater than or equal to the given input.  
[`CONCAT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/concat-function-reference) | Concatenates the specified characters to an existing string.  
[`CONTAINS`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/contains-function-reference) | Checks the occurrence of the specified value in a given string or string array.  
[`DECODE_BASE64_STRING`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/decode-base64-string-function-reference) | Decodes a base64 string to UTF-8 charset.  
[`DIVIDE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/divide-function-reference) | Divides an existing number by the specified number.  
[`EQUALS`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/equals-function-reference) | Compares the specified value with the existing value.  
[`EQUALS_IGNORE_CASE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/equals-ignore-case-function-reference) | Compares the specified value with the existing value.  
[`EPOCH_TO_HUMAN_READABLE_TIME`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/epoch-to-human-readable-time-function-reference) | Converts Unix epoch time (in milliseconds) to human-readable time format.  
[`EXPONENT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/exponent-function-reference) | Calculates the value of an existing number raised to the specified power.  
[`FILTER`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/filter-function-reference) | Filters the array elements that satisfy a given filter condition. Note that a filter condition must evaluate to TRUE or FALSE.  
[`FLATTEN`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/flatten-function-reference) | Flattens a JSON array recursively to create a new one-dimensional array.  
[`FLOOR`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/floor-function-reference) | Computes the greatest integer that is less than or equal to the provided input.  
[`FOR_EACH`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/for-each-function-reference) | Applies one or more transformation functions for each element in an array.  
[`GET`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-function-reference) | Returns the value in an array at a specified index. In an array, the first value is available at index 0 and the last value is available at index n-1 where n is the size of the array.  
[`GET_ELEMENT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-element-function-reference) | Returns the element at the specified index in a JSON array. In the array, the first value is available at index 0 and the last value is available at index n-1 where n is the size of the array.  
[`GET_PROPERTY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-property-function-reference) | Returns the value of the specified property in a JSON object.  
[`GREATER_THAN`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/greater-than-function-reference) | Checks if an existing number is greater than the specified number.  
[`GREATER_THAN_EQUAL_TO`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/greater-than-equal-to) | Checks if an integer is greater than or equal to the specified value.  
[`LENGTH`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/length-function-reference) | Calculates the length of a string. The length of a string is the number of characters in the string.  
[`LESS_THAN_EQUAL_TO`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/less-than-equal-to-function-reference) | Checks if an integer is less than or equal to the specified value.  
[`LESS_THAN`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/less-than-function-reference) | Checks if an existing number is less than the specified number.  
[`MAX`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/max-function-reference) | Finds the highest value in an array.  
[`MERGE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/merge-function-reference) | Merges two JSON variables (objects or arrays). If same value is present in both the variables, the function removes the duplicate value.  
[`MIN`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/min-function-reference) | Finds the lowest value in an array.  
[`MOD`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/mod-function-reference) | Divides two values and returns the remainder of the division operation.  
[`MULTIPLY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/multiply-function-reference) | Multiplies an existing number by the specified number.  
[`NAND`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/nand-function-reference) | Performs the logical NAND operation on the specified boolean values.  
[`NOR`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/nor-function-reference) | Performs the logical NOR operation on the specified boolean values.  
[`NOT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/not-function-reference) | Returns the opposite value of a boolean.  
[`OR`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/or-function-reference) | Performs the logical OR operation on the specified boolean values.  
[`REMOVE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/remove-function-reference) | Removes the specified value from an array.  
[`REMOVE_AT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/remove-at-function-reference) | Removes an element from an array at the specified index.  
[`REMOVE_PROPERTY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/remove-property-function-reference) | Removes a property from a JSON object.  
[`REPLACE_ALL`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/replace-all-function-reference) | Replaces all the occurrences of a substring in a string.  
[`RESOLVE_TEMPLATE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/resolve-template-function-reference) | Resolves references in a template string that contains $variable$ references.  
[`ROUND`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/round-function-reference) | Rounds a number to the nearest integer.  
[`SET`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/set-function-reference) | Updates the value of a string array at the specified index.  
[`SET_PROPERTY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/set-property-function-reference) | Adds or updates a property in a JSON object.  
[`SIZE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/size-function-reference) | Counts the number of elements in an array.  
[`SPLIT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/split-function-reference) | Splits a string based on the specified delimiter.  
[`SUBSTRING`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/substring-function-reference) | Returns the substring of the current string from the start index inclusive to the end index exclusive.  
[`SUBTRACT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/subtract-function-reference) | Subtracts the specified number from an existing number.  
[`SUM`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/sum-function-reference) | Adds all the values in an array.  
[`TO_BASE_64`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-base-64-function-reference) | Encodes a string to base64 format using the UTF-8 charset.  
[`TO_BOOLEAN_ARRAY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-boolean-array-function-reference) | Converts a JSON array to a boolean array.  
[`TO_BOOLEAN`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-boolean-function-reference) | Converts a string to a boolean data type.  
[`TO_DOUBLE_ARRAY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-double-array-function-reference) | Converts a JSON array to a double array.  
[`TO_DOUBLE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-double-function-reference) | Converts a string or an integer to a double.  
[`TO_INT_ARRAY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-int-array-function-reference) | Converts a JSON array to an integer array.  
[`TO_INT`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-int-function-reference) | Converts a string to an integer.  
[`TO_JSON`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-json-function-reference) | Converts the current value to a JSON object.  
[`TO_LOWERCASE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-lowercase-function-reference) | Converts all the characters in a string to lowercase.  
[`TO_SET`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-set-function-reference) | Removes duplicate values in an array.  
[`TO_STRING_ARRAY`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-string-array-function-reference) | Converts a JSON array to a string array.  
[`TO_UPPERCASE`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/to-uppercase-function-reference) | Converts all the characters in a string to uppercase.  
[`XNOR`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/xnor-function-reference) | Performs the logical XNOR operation on the specified boolean values.  
[`XOR`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/xor-function-reference) | Performs the logical XOR operation on the specified boolean values.  
[`GENERATE_UUID`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/generate-uuid-function-reference) | Generates a random UUID.  
[`GET_EXECUTION_ID`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-execution-id-function-reference) | Returns the execution ID of the current integration.  
[`GET_INTEGRATION_NAME`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-integration-name-function-reference) | Returns the name of the current integration.  
[`GET_INTEGRATION_REGION`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-integration-region-function-reference) | Returns the region of the current integration.  
[`GET_PROJECT_ID`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/get-project-id-function-reference) | Returns the Google Cloud project ID of the current integration.  
[`INT_LIST`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/int-list-function-reference) | Returns an integer list between the specified values. The returned list is inclusive of the starting value and exclusive of the ending value.  
[`NOW_IN_MILLIS`](https://docs.cloud.google.com/application-integration/docs/reference/data-mapping-reference/now-in-millis-function-reference) | Returns the current Unix epoch time of the integration in milliseconds.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
