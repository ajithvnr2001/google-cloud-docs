---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-transformation-module/
title: Transformation module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:05.170226+00:00
---

# Transformation module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-transformation-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Transformation module

### TIPCommon.transformation.add_prefix_to_dict

`TIPCommon.transformation.add_prefix_to_dict(given_dict: dict, prefix: str) → dict`

Adds a prefix to the keys of a given dictionary.

#### Parameters

Parameters  
---  
`given_dict` | `dict`The dictionary to add the prefix to.  
`prefix` | `str`The prefix applied to the dictionary keys.  
  
#### Returns

The dictionary with the prefix added to the keys.

#### Return type

`dict`

#### TIPCommon.transformation.add_prefix_to_dict_keys

`TIPCommon.transformation.add_prefix_to_dict_keys(target_dict: dict, prefix: str) → dict`

Adds a prefix to the keys of a given dictionary.

#### Parameters

Parameters  
---  
`target_dict` | `dict`The dictionary to add the prefix to.  
`prefix` | `str`The prefix applied to the dictionary keys.  
  
#### Returns

The dictionary with the prefix added to the keys.

#### Return type

`dict`

### TIPCommon.transformation.adjust_to_csv

`TIPCommon.transformation.adjust_to_csv(value)`

Adjusts a value to be suitable for inclusion in a CSV.

Parameters  
---  
`value` | `Any`The value to adjust.  
  
#### Returns

The adjusted value.

#### Return type

`str`

### TIPCommon.transformation.construct_csv

`TIPCommon.transformation.construct_csv(list_of_dicts)`

Constructs a CSV from a list of dictionaries.

Parameters  
---  
`list_of_dicts` | `list[dict]`The list of dictionaries to add to the CSV.   
  
#### Returns

The CSV formatted list.

#### Return type

`list[str]`

### TIPCommon.transformation.convert_comma_separated_to_list

`TIPCommon.transformation.convert_comma_separated_to_list(comma_separated, delimiter=',')`

Converts a comma-separated string to a list of values.

Parameters  
---  
`delimiter` | The delimiter to parse the string with.  
Default is `','`.   
`comma_separated` | `str`The comma-separated string to convert.  
  
#### Returns

The list of values.

#### Return type

`list`

### TIPCommon.transformation.convert_dict_to_json_result_dict

`TIPCommon.transformation.convert_dict_to_json_result_dict(json_result, title_key='Entity', results_key='EntityResult')`

Converts the `key, value` JSON result into the JSON result object list and organizes the entity JSON result object to a set format.

The example of how a `dict` transforms to the JSON result is as follows:
    
    
    {k1: v1, k2:v2, ...} =>
    [
       {
           title_key: k1,
           result_key: v1
       },
       {
           title_key: k2,
           result_key: v1
       }
       ...
    ]
    

Parameters  
---  
`json_result` | `dict[str, Any] | str` The `key, value` JSON result.  
`title_key` | `str` The key under which the name of each key will be.  
`result_key` | `str` The key under which the name of each value will be.  
  
#### Examples

The default example for the entity result JSON format where `title_key='Entity'`, `results_key='EntityResult'` is as follows:
    
    
    [
       {
           'Entity': 'key1 in json_result',
           'EntityResult: {
               json_result['key1']
           }
       },
       {
           'Entity': 'key2 in json_result',
           'EntityResult: {
               json_result['key2']
           }
       }
    ]
    

#### Returns

`(list[dict[str, Any]])` A list of entity JSON result objects

#### Raises

  * [`InternalJSONDecoderError`](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-exceptions-module#int-json-error) – if `json_result` is a string and couldn't be parsed to dictionary using `json.loads()`.
  * `ValueError` – if the `json_result` isn't a `dict` (the check is done after loading it from a string, if needed).



### TIPCommon.transformation.convert_list_to_comma_string

`TIPCommon.transformation.convert_list_to_comma_string(values_list, delimiter=',')`

Converts a list of values to a comma-separated string.

Parameters  
---  
`delimiter` | The delimiter to be used in the string.   
Default is `','`.  
`values_list` | `list`The list of values to convert.  
  
#### Returns

The comma-separated string.

#### Return type

`str`

### TIPCommon.transformation.dict_to_flat

`TIPCommon.transformation.dict_to_flat(target_dict)`

Receives a nested dictionary and returns it as a flat dictionary.

Parameters  
---  
`target_dict` | `dict`The dictionary to flatten.  
  
#### Returns

The flattened dictionary.

#### Return type

`dict`

### TIPCommon.transformation.flat_dict_to_csv

`TIPCommon.transformation.flat_dict_to_csv(flat_dict, property_header='Property', value_header='Value')`

Converts a flat dictionary into a list of strings in CSV format.

The `property_header` and `value_header` arguments are used to customize the CSV header.

Parameters  
---  
`flat_dict` | `dict`The dictionary to convert to CSV format.  
`property_header` | `str`The header for the property column.   
Default is _Property_.  
`value_header` | `str`The header for the value column.   
Default is _Value_.  
  
#### Returns

The list of strings in CSV format.

#### Return type

`list`

### TIPCommon.transformation.get_unicode

`TIPCommon.transformation.get_unicode(value)`

Gets the unicode of a value.

Parameters  
---  
`value` | `Any`The value to convert to unicode.  
  
#### Returns

The unicode representation of value.

#### Return type

`unicode (unicode)`

### TIPCommon.transformation.removeprefix

`TIPCommon.transformation.removeprefix(string: str, prefix: str) → str`

Self-implementation for `str.removeprefix()` that exists in Python 3.9 and later.

If the string starts with the prefix string, the method returns `string[len(prefix):]`. Otherwise, returns a copy of the original string.

Parameters  
---  
`string` | `str`The string to remove the prefix from.  
`prefix` | `str`The prefix to remove from the string.  
  
#### Returns

The resulting string.

### TIPCommon.transformation.removesuffix

`TIPCommon.transformation.removesuffix(string: str, suffix: str) → str`

Self-implementation for `str.removesuffix()` that exists in Python 3.9 and later.

If the string ends with the suffix string, the method returns `string[:-len(prefix)]`. Otherwise, returns a copy of the original string.

Parameters  
---  
`string` | `str`The string to remove the suffix from.  
`suffix` | `str`The suffix to remove from the string.  
  
#### Returns

The resulting string.

### TIPCommon.transformation.rename_dict_key

`TIPCommon.transformation.rename_dict_key(a_dict: dict, current_key: Hashable,new_key: Hashable) → None`

Renames a key in a dictionary.

Parameters  
---  
`a_dict` | `dict` The dict to rename a key in.  
`current_key` | `Hashable`The key in `a_dict` to rename.  
`new_key` | `Hashable`The renamed key.  
  
### TIPCommon.transformation.string_to_multi_value

`TIPCommon.transformation.string_to_multi_value(string_value, delimiter=',', only_unique=False)`

Converts a string containing a comma-separated list of values to a list of values.

Parameters  
---  
`string_value` | `str`The string to convert.  
`delimiter` | _Optional_`str` The delimiter to split the string on. Default is `','`.  
`only_unique` | _Optional_`bool` If set to `True`, the parameter only includes unique values in the returned list. Default is `False`.  
  
#### Returns

The list of values.

#### Return type

`list`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
