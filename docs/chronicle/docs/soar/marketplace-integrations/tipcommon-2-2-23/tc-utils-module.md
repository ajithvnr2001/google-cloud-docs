---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-utils-module/
title: TIPCommon.utils \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:20:31.484127+00:00
---

# TIPCommon.utils  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-utils-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.utils

The **TIPCommon.utils** module serves as a foundational toolkit for integration developers. It provides essential helpers for string manipulation, secure type casting, OData query construction, and environment-specific checks to ensure that integrations run smoothly across different platform versions and execution states.

## Data cleaning and type casting

These functions handle the "pre-processing" of data, ensuring variables are in the correct format before being used in logic or sent to external APIs.

Function | Parameters | Description & Returns  
---|---|---  
`camel_to_snake_case()` | 

  * `string`: (str) Target `camelCase` string.

| Returns: `str` Converts `camelCase` or `PascalCase` strings to `snake_case`. Essential for normalizing API responses to Pythonic naming conventions.  
`cast_keys_to_int()` | 

  * `data`: (dict) Dictionary with numeric string keys.

| Returns: `dict` Creates a new dictionary where all keys are cast to integers. Often used when processing JSON data that represents IDs as strings.  
`clean_result()` | 

  * `value`: (str) Target string.

| Returns: `str` Strips leading and trailing whitespace. A svital utility for cleaning user input from integration parameters.  
`none_to_default_value()` | 

  * `value_to_check`: (Any) Input value.
  * `value_to_return_if_none`: (Any) Fallback.

| Returns: `Any` Checks if a value is `None`. If so, returns the default fallback; otherwise, returns the original value.  
`safe_cast_bool_value_from_str()` | 

  * `default_value`: (Any) The value to evaluate.

| Returns: `bool | Any` Converts string booleans (like "true") to actual booleans. Returns the `default_value` if casting fails.  
`safe_cast_int_value_from_str()` | 

  * `default_value`: (Any) The value to evaluate.

| Returns: `int | Any` Attempts to cast a value to an integer. Returns the `default_value` if the cast is unsuccessful.  
  
## Environment and execution logic

These utilities allow scripts to identify their runtime context, such as whether they are running as a test, an asynchronous action, or on a specific version of the platform.

Function | Parameters | Description & Returns  
---|---|---  
`is_first_run()` | 

  * `sys_argv`: (list) Arguments from `sys.argv`.

| Returns: `bool` Determines if an action is being executed asynchronously for the first time. Used to manage state in polling actions.  
`is_test_run()` | 

  * `sys_argv`: (list) Arguments from `sys.argv`.

| Returns: `bool` Identifies if the script is running in "Test" mode within the IDE. Use this to bypass real API calls during development.  
`is_overflowed()` | 

  * `siemplify`: (SiemplifyConnectorExecution)
  * `alert_info`: (AlertInfo)
  * `is_test_run`: (bool)

| Returns: `bool` Checks if an alert meets the platform's overflow criteria. Essential for connectors to prevent redundant alert ingestion.  
`is_python_37()` | None | Returns: `bool` Checks if the current Python version is at least 3.7. Useful for toggling between legacy and modern language features.  
`platform_supports_1p_api()` | None | Returns: `bool` Checks if the instance supports First-Party (1P) unified APIs. Enables dynamic fallback logic for multi-platform support.  
`platform_supports_db()` | 

  * `siemplify`: (ChronicleSOAR) SDK object.

| Returns: `bool` Determines if the environment supports DataStreams. If `False`, the integration should fall back to file-based state.  
  
## Data validation and filtering

Utilities for ensuring data integrity, performing set operations, and retrieving values from complex JSON structures.

Function | Parameters | Description & Returns  
---|---|---  
`escape_odata_literal()` | 

  * `value`: (Any) The raw query value.

| Returns: `Any` Doubles single quotes in a string for OData compliance. **Important:** This prevents query injection and syntax errors in `$filter` expressions.   
`get_unique_items_by_difference()` | 

  * `item_pool`: (Iterable) The source items.
  * `items_to_remove`: (Iterable) Exclusion list.

| Returns: `list` Calculates the set difference (Pool - Remove) and returns unique items as a list. Useful for filtering processed alerts.  
`get_value_from_json()` | 

  * `data`: (dict) JSON data to search.
  * `*keys`: (str) Ordered fallback keys.
  * `default`: (Any) Fallback value.

| Returns: `Any` Retrieves values from nested JSON using a "waterfall" of keys. Returns the `default` if none of the keys exist.  
`is_empty_string_or_none()` | 

  * `data`: (str) String to check.

| Returns: `bool` Returns `True` if the input is `None` or only contains an empty string `""`. Essential for safety-checks on API responses.  
`is_valid_email()` | 

  * `email_addr`: (str) String to check.

| Returns: `bool` Validates an email address format using standard regular expression. Useful for pre-validating parameters before external API calls.  
`is_valid_uuid()` | 

  * `string`: (str) String to check.

| Returns: `bool` Ensures a string is a valid UUID version 4. Prevents 400 errors when passing IDs to platform endpoints.  
  
## System and file utilities

Helpers for interacting with the operating system, managing temporary files, and handling entity metadata.

Function | Parameters | Description & Returns  
---|---|---  
`create_and_write_to_tempfile()` | 

  * `content`: (str | bytes) Data to write.

| Returns: `Path` Writes content to a secure temporary file. Useful for actions that require passing data to command-line tools.  
`get_entity_original_identifier()` | 

  * `entity`: (Entity) Target entity object.

| Returns: `str` Retrieves the original identifier for an entity, ensuring accurate mapping back to source alerts.  
`get_function_arg_names()` | 

  * `func`: (Callable) Target function.

| Returns: `list` Uses reflection to retrieve all argument names defined in a function. Essential for building dynamic wrappers.  
`get_sdk_api_uri()` | 

  * `chronicle_soar`: (ChronicleSOAR) SDK instance.

| Returns: `str` Retrieves the base API URI for the current environment. Vital for constructing custom REST calls outside standard wrappers.  
`safe_json_for_204()` | 

  * `response`: (Response) HTTP response object.
  * `default_for_204`: (Any) Fallback value.

| Returns: `list | dict | Any` Safely handles 204 (No Content) responses. Returns an empty list or the `default_for_204` value instead of crashing during JSON parsing.  
`temporarily_remove_header()` | 

  * `header_name`: (str) Header to suppress.

| Returns: `callable` **Decorator:** Temporarily removes a header (like `'Prefer'`) from a session for the duration of a single call.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
