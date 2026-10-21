---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-utils-module/
title: Utils module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:27:37.458763+00:00
---

# Utils module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-utils-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Utils module

### TIPCommon.utils.camel_to_snake_case

`TIPCommon.utils.camel_to_snake_case(string)`

Converts a camel case string to snake case.

Parameters  
---  
`string` | `str`The string to convert.  
  
#### Returns

The converted string.

#### Return type

`str`

### TIPCommon.utils.cast_keys_to_int

`TIPCommon.utils.cast_keys_to_int(data)`

Casts the keys of a dictionary to integers.

Parameters  
---  
`data` | `dict`The data which keys are cast to integers.  
  
#### Returns

A new dict with its keys as integers.

#### Return type

`dict`

### TIPCommon.utils.clean_result

`TIPCommon.utils.clean_result(value)`

Removes unnecessary spaces before or after the value.

Parameters  
---  
`value` | `str`The value to remove the spaces from.  
  
#### Returns

A plain version of the original value.

#### Return type

`str`

### TIPCommon.utils.create_and_write_to_tempfile

`TIPCommon.utils.create_and_write_to_tempfile(content: str | bytes)→ Path`

Creates a temporary file and writes content to it.

#### Parameters

Parameters  
---  
`content` | `str | bytes`The content to write to the temporary file.  
  
#### Returns

The path to the created temporary file.

#### Return type

`Path`

### TIPCommon.utils.get_entity_original_identifier

`TIPCommon.utils.get_entity_original_identifier(entity)`

A helper function for getting the original identifier for the entity.

Parameters  
---  
`entity` | `Entity` The entity from which the function gets the original identifier.  
  
#### Returns

The original identifier.

#### Return type

`str`

### TIPCommon.utils.get_function_arg_names

`TIPCommon.utils.get_function_arg_names(func)`

Retrieves all of the argument names of a specific function.

Parameters  
---  
`func` | The function or method to analyze.  
  
#### Returns

All of the argument keys defined in the given function.

#### Return type

`list`

#### TIPCommon.utils.get_unique_items_by_difference

`TIPCommon.utils.get_unique_items_by_difference(item_pool: Iterable, items_to_remove: Iterable) → list`

Gets the set difference items from two iterables (`item_pool` \- `items_to_remove`).

Parameters  
---  
`item_pool` | `iterable`The item pool to filter from.  
`items_to_remove` | `iterable` The items that should be removed, if any.  
  
#### Returns

A list containing unique items from `item_pool` that were not part of `items_to_remove`.

#### Return type

`list`

### TIPCommon.utils.is_empty_string_or_none

`TIPCommon.utils.is_empty_string_or_none(data)`

Checks if the data is an empty string or `None`.

Parameters  
---  
`data` | `str`The data to check.  
  
#### Returns

`True` if the supplied data is `None`, or if it only contains an empty string `""`.

#### Return type

`bool`

### TIPCommon.utils.is_first_run

`TIPCommon.utils.is_first_run(sys_argv)`

Returns a boolean value that indicates whether the action is being executed asynchronously.

### Parameters

Parameters  
---  
`sys_argv` | The command line arguments from the `sys.argv` module.  
  
#### Returns

`True` if the action is being executed asynchronously and `False` in any other case.

### TIPCommon.utils.is_overflowed

`TIPCommon.utils.is_overflowed(siemplify, alert_info, is_test_run)`

Checks if overflowed.

Parameters  
---  
`siemplify` | `obj` An instance of the SDK `SiemplifyConnectorExecution` class.   
`alert_info` | `AlertInfo`Alert information.  
`is_test_run` | `bool` The parameter indicates whether the current run is a test run or not.   
  
#### Returns

`True` if the alert is overflowed and `False` in any other case.

### TIPCommon.utils.is_python_37

`TIPCommon.utils.is_python_37()`

Checks if the Python version of the system is 3.7 or later.

#### Returns

`True` if the current Python version is at least 3.7; otherwise `False`.

#### Return type

`bool`

#### TIPCommon.utils.is_test_run

`TIPCommon.utils.is_test_run(sys_argv)`

Returns a boolean value that indicates the connector's execution state.

Parameters  
---  
`sys_argv` | `_type_`The command line arguments.  
  
#### Returns

`True` if the current run is a test run; otherwise `False`.

#### Return type

`bool`

### TIPCommon.utils.is_valid_email

`TIPCommon.utils.is_valid_email(email_addr: str)→ bool`

Checks if a provided value is a valid email address.

#### Parameters

Parameters  
---  
`email_addr` | `str`The email address to check.  
  
#### Returns

Returns `True` if the email is valid; otherwise, `False`.

#### Return type

`bool`

### TIPCommon.utils.none_to_default_value

`TIPCommon.utils.none_to_default_value(value_to_check, value_to_return_if_none)`

Checks if the current value is `None`.

If the value is `None`, the function replaces it with another value. If the value isn't `None`, the function returns the original value.

Parameters  
---  
`value_to_check` | `dict/list/str`The value to check.  
`value_to_return_if_none` | `dict/list/str` The value to return if `value_to_check` is `None`.   
  
#### Returns

If something is provided, the original value of `value_to_check` is returned.

If nothing is provided, then the `value_to_return_if_none` is returned.

#### Return type

`dict/list/str`

### TIPCommon.utils.platform_supports_1p_api

`TIPCommon.utils.platform_supports_1p_api()→ bool`

Checks whether the platform is 1P or not.

#### Parameters

Parameters  
---  
  
#### Returns

Returns `True` if the platform is 1P; otherwise, `False`.

#### Return type

`bool`

### TIPCommon.utils.platform_supports_db

`TIPCommon.utils.platform_supports_db(siemplify)`

Checks if the platform supports the database usage.

Parameters  
---  
`siemplify` | `object`The Siemplify SDK object.  
  
#### Returns

`True` if the Siemplify SDK object has any of the following attributes:

  * `set_connector_context_property`
  * `set_job_context_property`



Otherwise, `False` is returned.

### TIPCommon.utils.safe_cast_bool_value_from_str

`TIPCommon.utils.safe_cast_bool_value_from_str(default_value)`

Checks if a default value is a string containing a boolean value.

If the default value is a string containing a boolean value, the function converts the string to boolean. Otherwise, the function returns the value.

Parameters  
---  
`default_value` | The default value to return if the casting fails.  
  
#### Returns

The casted value or the default value.

### TIPCommon.utils.safe_cast_int_value_from_str

`TIPCommon.utils.safe_cast_int_value_from_str(default_value)`

Checks if a default value is a string containing the integer value.

If the default value is a string containing an integer value, the function converts the string to boolean. Otherwise, the function returns the value.

Parameters  
---  
`default_value` | The default value to return if the casting fails.  
  
#### Returns

The casted value or the default value.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
