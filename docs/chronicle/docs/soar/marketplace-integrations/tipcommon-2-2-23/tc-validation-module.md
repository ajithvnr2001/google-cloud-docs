---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-validation-module/
title: TIPCommon.validation \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:05.335613+00:00
---

# TIPCommon.validation  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-validation-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.validation

The **TIPCommon.validation** module contains the `ParameterValidator` class, a critical tool for ensuring data integrity within integrations. It automates the process of checking input types, enforcing constraints (such as numerical ranges or email formats), and providing safe fallback values to prevent runtime crashes.

## The `ParameterValidator` class

The `ParameterValidator` class provides a standardized interface for validating various parameter types. Each method accepts a parameter name and value, returning the validated value in its appropriate Python type. If validation fails and no `default_value` is provided, a `ParameterValidationError` is raised.

### Usage example

To use the validator, initialize it with the `siemplify` SDK object:
    
    
    from TIPCommon.validation import ParameterValidator
    
    # Initialize the validator
    validator = ParameterValidator(siemplify)
    
    # Validate and cast strings to specific types
    validated_float = validator.validate_float(param_name='Threshold', value='3.7')
    validated_int = validator.validate_integer(param_name='Retry Count', value='5')
    

## Numerical and limit validation

These methods ensure that numerical inputs fall within expected boundaries and are correctly cast to their appropriate Python types.

Function | Parameters | Description & Returns  
---|---|---  
`validate_float()` | 

  * `param_name`: (str)
  * `value`: (str | float)

| Returns: `float` Validates that a value can be cast to a float. Useful for thresholds or probability scores.  
`validate_integer()` | 

  * `param_name`: (str)
  * `value`: (str | int)

| Returns: `int` Validates and casts a value to an integer.  
`validate_range()` | 

  * `value`: (str | int)
  * `min_limit`: (int)
  * `max_limit`: (int)

| Returns: `int` Ensures an integer falls within the inclusive range defined by `min_limit` and `max_limit`.  
`validate_percentage()` | 

  * `value`: (str | int)

| Returns: `int` Ensures the value is an integer between `0` and `100` inclusive.  
`validate_non_negative()` | 

  * `value`: (str | int)

| Returns: `int` Ensures the value is an integer `≥ 0`.  
`validate_non_zero()` | 

  * `value`: (str | int)

| Returns: `int` Ensures the value is an integer and is not equal to `0`.  
`validate_positive()` | 

  * `value`: (str | int)

| Returns: `int` Ensures the value is an integer `> 0`.  
`validate_lower_limit()` | 

  * `value`: (str | int)
  * `limit`: (int)

| Returns: `int` Ensures the value is `≥` the specified `limit`.  
`validate_upper_limit()` | 

  * `value`: (str | int)
  * `limit`: (int)

| Returns: `int` Ensures the value is `≤` the specified `limit`.  
  
## Data structure and string validation

These methods validate more complex input types, such as delimited strings, JSON objects, and specific formats like email addresses.

Function | Parameters | Description & Returns  
---|---|---  
`validate_csv()` | 

  * `csv_string`: (str)
  * `delimiter`: (str) Defaults to `', '`.
  * `possible_values`: (list) Optional whitelist.

| Returns: `list` Splits a string into a list using the delimiter. If `possible_values` is provided, it validates each item against that list.  
`validate_json()` | 

  * `json_string`: (str)
  * `**kwargs`: Pass-through for `json.loads()`.

| Returns: `dict | list` Parses a string into a JSON object. Raises an error if the string is not valid JSON.  
`validate_email()` | 

  * `email`: (str)

| Returns: `str` Validates that the provided string follows a standard email format.  
`validate_ddl()` | 

  * `value`: (str)
  * `ddl_values`: (list) Whitelist of valid values.
  * `case_sensitive`: (bool) Defaults to `False`.

| Returns: `str` Validates that the input matches one of the values in a defined DDL.  
`validate_severity()` | 

  * `severity`: (str | int)
  * `possible_values`: (list)

| Returns: `int` Validates a platform severity input. Correctly maps between platform-standard severity labels (such as "High") and their equivalent integer ranks.  
  
## Global validation configuration

Every validation method in the `ParameterValidator` class supports the following optional keyword arguments to control behavior upon failure or for debugging:

  * `default_value`: If provided, this value is returned instead of raising a `ParameterValidationError` when validation fails.

  * `print_value`: (bool) When `True`, the invalid value that caused the failure is included in the log message. Defaults to `True`.

  * `print_error`: (bool) When `True`, the specific exception message is included in the platform logs. Defaults to `False`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
