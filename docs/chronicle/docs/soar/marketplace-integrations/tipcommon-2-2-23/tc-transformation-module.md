---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-transformation-module/
title: TIPCommon.transformation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:10.656475+00:00
---

# TIPCommon.transformation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-transformation-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.transformation

The **TIPCommon.transformation** module contains a comprehensive suite of utilities designed to modify and restructure data formats within integrations. It handles frequent tasks such as flattening nested dictionaries, converting data to CSV formats, and performing string-based manipulations to ensure compatibility between different API schemas.

## Dictionary and JSON transformation

These functions facilitate the restructuring of dictionary objects, which is critical when mapping data from third-party security vendors to the standardized Google SecOps schema.

Function | Parameters | Description & Returns  
---|---|---  
`add_prefix_to_dict()` | 

  * `given_dict`: (SingleJson) Source dictionary.
  * `prefix`: (str) String to prepend to keys.

| Returns: `SingleJson` Prepends a prefix to every key in a dictionary. `add_prefix_to_dict_keys()` is available as an alias for backward compatibility.  
`convert_dict_to_json_result_dict()` | 

  * `json_result`: (str | SingleJson) The raw data.
  * `title_key`: (str) Defaults to `'Entity'`.
  * `results_key`: (str) Defaults to `'EntityResult'`.

| Returns: `list[SingleJson]` Converts a key-value JSON structure into a list of JSON result objects. Raises `InternalJSONDecoderError` if parsing fails or `ValueError` if the result is not a dictionary.  
`dict_to_flat()` | 

  * `target_dict`: (SingleJson) Nested dictionary.

| Returns: `SingleJson` Recursively flattens a nested dictionary into a single-level dictionary where nested keys are typically joined by underscores or dots.  
`rename_dict_key()` | 

  * `a_dict`: (dict[Hashable, Any]) Dictionary to modify.
  * `current_key`: (Hashable) Existing key name.
  * `new_key`: (Hashable) Target key name.

| Returns: `None` Renames a specific key in a dictionary **in-place**. This is more memory-efficient than creating a new dictionary for large datasets.  
  
## CSV and string utilities

Utilities for generating report-ready data and parsing delimited strings into usable Python lists.

Function | Parameters | Description & Returns  
---|---|---  
`construct_csv()` | 

  * `list_of_dicts`: (Sequence[SingleJson]) List of row data.

| Returns: `list[str]` Converts a list of dictionaries into CSV rows. Fixes column ordering issues and preserves legacy comma-replacement logic for values containing the delimiter.  
`flat_dict_to_csv()` | 

  * `flat_dict`: (SingleJson) Dictionary to convert.
  * `property_header`: (str) Defaults to `'Property'`.
  * `value_header`: (str) Defaults to `'Value'`.

| Returns: `list[str]` Turns a flattened dictionary into a two-column CSV format representing key-value pairs.  
`convert_comma_separated_to_list()` | 

  * `comma_separated`: (str) The source string.
  * `delimiter`: (str) Defaults to `','`.

| Returns: `list[str]` Splits a string based on a delimiter into a Python list of values.  
`convert_list_to_comma_string()` | 

  * `values_list`: (list[Any]) The source list.
  * `delimiter`: (str) Defaults to `','`.

| Returns: `str` Joins list elements into a single string using the specified delimiter.  
`string_to_multi_value()` | 

  * `string_value`: (str) The source string.
  * `delimiter`: (str) Defaults to `','`.
  * `only_unique`: (bool) Defaults to `False`.

| Returns: `list[str]` Advanced string-to-list conversion that optionally filters for unique values only.  
`to_string()` | 

  * `value`: (Any) The object to convert.

| Returns: `str` General-purpose utility to ensure a value is represented as a string. Returns an empty string if the input is `None`, preventing common `TypeError` crashes during concatenation.  
  
## Legacy and compatibility methods

The following functions are provided for backward compatibility. In Python 3.9+, it is recommended to use the built-in string methods directly.

Function | Parameters | Description & Returns  
---|---|---  
`removeprefix()` | 

  * `string`: (str) Target string.
  * `prefix`: (str) Prefix to strip.

| Returns: `str` **Deprecated.** Internally calls `str.removeprefix()`. Use the built-in method directly in new code.  
`removesuffix()` | 

  * `string`: (str) Target string.
  * `suffix`: (str) Suffix to strip.

| Returns: `str` **Deprecated.** Internally calls `str.removesuffix()`. Use the built-in method directly in new code.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
