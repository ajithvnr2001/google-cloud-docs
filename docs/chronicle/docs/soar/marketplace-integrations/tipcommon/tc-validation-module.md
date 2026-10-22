---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-validation-module/
title: Validation module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:13.289016+00:00
---

# Validation module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-validation-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Validation module

This module contains the `Validator` class for validating various types of parameters. Each method takes a parameter name, a value, and optional keyword arguments. The functions raise the `ParameterValidationError` error if the parameter value is invalid.

The validation functions return the provided value in its validated type.

_Example:_
    
    
    validator = ParameterValidator(siemplify) # siemplify SDK object 
    
    validated_value = validator.validate_float(param_name='something', value='3.7') print(validated_value) # 3.7 as float
    
    validated_value = validator.validate_int(param_name='something', validated_value) print(validated_value) # 3 as integer
    

## _class_ TIPCommon.validation.ParameterValidator

_class_ `TIPCommon.validation.ParameterValidator(siemplify)`

Bases: **object**

A class that contains parameters validation functions.

### validate_csv

`validate_csv(param_name, csv_string, delimiter=', ', possible_values=None, default_value=<object object>, print_value=True, print_error=False)`

Validates a comma-separated value (CSV) string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`csv_string` | `str` The CSV string to validate.  
`delimiter` | `str` The character that separates the values in the CSV string.  
`possible_values` | `list`A list of possible values.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool` Define whether to printrint the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the CSV string is invalid.

#### Returns

The list of values in the CSV string.

#### Return type

`list`

### validate_ddl

`validate_ddl(param_name, value, ddl_values, case_sensitive=False, default_value=<object object>, print_value=True, print_error=False)`

Validates a DDL string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The DDL string to validate.  
`ddl_values` | `list`A list of valid DDL values.  
`case_sensitive` | `bool` Define whether to printerform a case-sensitive validation or not.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool` Define whether to printrint the exception error as part of the message.  
  
#### Returns

The validated DDL string.

#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the DDL string is invalid.

### validate_email

`validate_email(param_name, email, default_value=<object object>, print_value=True, print_error=False)`

Validates an email string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`email` | `str`The email address string to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool` Define whether to printrint the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the email address string is invalid.

#### Returns

The email address string.

#### Return type

`str`

### validate_float

`validate_float(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates a float string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool` Define whether to printrint the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value isn't a float.

#### Returns

The validated value.

#### Return type

`float`

### validate_integer

`validate_integer(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates an integer string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool` Define whether to printrint the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value isn't an integer.

#### Returns

The validated value.

#### Return type

`int`

### validate_json

`validate_json(param_name, json_string, default_value=<object object>, print_value=True, print_error=False, **kwargs)`

Validates a JSON string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`json_string` | `str`The JSON string to validate.  
`default_value` | `any`The default value to return in case of a validation error.  
`print_value` | `bool`Define whether to printrint the parameter value as part of the message.  
`print_error` | `bool`Define whether to printrint the exception error as part of the message.  
`**kwrags` | `dict`Keyword arguments for the `json.loads()` function.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the JSON string is invalid.

#### Returns

The parsed JSON object.

### validate_lower_limit

`validate_lower_limit(param_name, value, limit, default_value=<object object>, print_value=True, print_error=False)`

Validates a lower limit string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`limit` | `int`The lower limit.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value is less than the limit.

#### Returns

The validated value.

#### Return type

`int`

### validate_non_negative

`validate_non_negative(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates a non-negative integer string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value is negative.

#### Returns

The validated value.

#### Return type

`int`

### validate_non_zero

`validate_non_zero(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates a non-zero integer string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value is zero.

#### Returns

The validated value.

#### Return type

`int`

### validate_percentage

`validate_percentage(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates a percentage string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value isn't a percentage.

#### Returns

The validated value.

#### Return type

`int`

### validate_positive

`validate_positive(param_name, value, default_value=<object object>, print_value=True, print_error=False)`

Validates a positive integer string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value isn't positive.

#### Returns

The validated value.

#### Return type

`int`

### validate_range

`validate_range(param_name, value, min_limit, max_limit, default_value=<object object>, print_value=True, print_error=False)`

Validates a range string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`min_limit` | `int`The lower limit.  
`max_limit` | `int`The upper limit.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value is out of range.

#### Returns

The validated value.

#### Return type

`int`

### validate_severity

`validate_severity(param_name, severity, min_limit=None, max_limit=None, possible_values=None, default_value=<object object>, print_value=True, print_error=False)`

Validates a severity string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`severity` | `str`The severity value to validate.  
`min_limit` | `int`The lower limit.  
`max_limit` | `int`The upper limit.  
`possible_values` | `list`A list of possible values.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool` Define whether to print the parameter value as part of the message.  
`print_error` | `bool` Define whether to print the exception error as part of the message.  
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value is invalid.

#### Returns

The validated value.

#### Return type

`int`

### validate_upper_limit

`validate_upper_limit(param_name, value, limit, default_value=<object object>, print_value=True, print_error=False)`

Validates an upper limit string.

Parameters  
---  
`param_name` | `str`The name of the parameter.  
`value` | `str`The value to validate.  
`limit` | `int`The upper limit.  
`default_value` | `any` The default value to return in case of a validation error.  
`print_value` | `bool`Define whether to print the parameter value as part of the message.   
`print_error` | `bool`Define whether to print the exception error as part of the message.   
  
#### Raises

[ParameterValidationError](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#param-valid-error) \- When the value exceeds the limit.

#### Returns

The validated value.

#### Return type

`int`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
