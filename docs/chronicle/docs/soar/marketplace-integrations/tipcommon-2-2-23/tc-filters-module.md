---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-filters-module/
title: filters module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:11.277690+00:00
---

# filters module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-filters-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `filters` module

The **`filters` module** offers a robust set of tools for refining data during the ingestion and processing phases of an integration. These functions allow developers to purify lists by type, remove null arguments from function calls, and implement sophisticated deduplication logic for alerts based on IDs or timestamps.

### TIPCommon.filters.filter_list_by_type

`TIPCommon.filters.filter_list_by_type(array, inner_type) → list`

Filters out any items in a list that don't match the requested data type. This ensures that downstream logic receives a purified array containing only valid object types.

#### Parameters

Parameters  
---  
`array` | `list[Any]` The original list to clean.  
`inner_type` | `type` The required data type for items in the list.  
  
#### Example

The following example shows how to separate integers and strings from a mixed list:
    
    
    arr = [1, 2, '3', 4]
    
    # Get only the integers
    arr1 = filter_list_by_type(arr, int)
    # Result: [1, 2, 4]
    
    # Get only the strings
    arr2 = filter_list_by_type(arr, str)
    # Result: ['3']
    

#### Returns

A new list containing only items that match the specified `inner_type`.

### TIPCommon.filters.filter_none_kwargs

`TIPCommon.filters.filter_none_kwargs(**kwargs) → dict`

Filters out any keyword arguments that have a value of `None`. This is particularly useful for preparing API requests where null parameters must be omitted rather than sent as empty values.

#### Parameters

Parameters  
---  
`**kwargs` | `Any` A collection of keyword arguments to evaluate.  
  
#### Returns

A dictionary containing only the keyword arguments where the value isn't `None`.

### TIPCommon.filters.filter_old_alerts

`TIPCommon.filters.filter_old_alerts(siemplify, alerts, existing_ids, id_key='alert_id') → list`

Filters a list of alerts to exclude those that have already been processed.

#### Parameters

Parameters  
---  
`siemplify` | `obj` An instance of the SDK `SiemplifyConnectorExecution` class.  
`alerts` | `list` A list of alert objects to evaluate.  
`existing_ids` | `list` A list of identifiers that have already been processed to filter out.  
`id_key` | `str` The attribute key used to find the identifier within the alert object. The default value is `alert_id`.  
  
#### Returns

A list of filtered alert objects that don't exist in the `existing_ids` list.

### TIPCommon.filters.filter_old_ids

`TIPCommon.filters.filter_old_ids(alert_ids, existing_ids) → list`

Filters a list of new identifiers against a list of previously processed identifiers.

#### Parameters

Parameters  
---  
`alert_ids` | `list` A list of new IDs to check.  
`existing_ids` | `list` A list of IDs to compare against for filtering.  
  
#### Returns

A list of IDs that are not present in the `existing_ids` collection.

### TIPCommon.filters.filter_old_ids_by_timestamp

`TIPCommon.filters.filter_old_ids_by_timestamp(ids, offset_in_hours, convert_to_milliseconds, offset_is_in_days) → dict`

Filters identifiers that exceed a specified time limit, ensuring the connector only processes recent data.

#### Parameters

Parameters  
---  
`ids` | `dict` The dictionary of IDs and their associated timestamps to filter.  
`offset_in_hours` | `int` The time limit threshold used for filtering.  
`offset_is_in_days` | `bool` Specifies whether the value provided in `offset_in_hours` represents days. When set to `True`, the function treats the offset value as a count of days and converts it to hours for the calculation.  
`convert_to_milliseconds` | `bool` If `True`, transforms Unix timestamps from seconds to milliseconds.  
  
#### Returns

A dictionary containing only the IDs that fall within the specified time limit.

### TIPCommon.filters.pass_whitelist_filter

`TIPCommon.filters.pass_whitelist_filter(siemplify, whitelist_as_a_blacklist, model, model_key, whitelist=None) → bool`

Determines if a specific value from a model attribute passes the defined allowlist or blocklist logic.

#### Parameters

Parameters  
---  
`whitelist_as_a_blacklist` | `bool` Specifies the filtering logic for the `Use whitelist as blacklist` setting. When enabled, the connector treats the provided list as a set of values to exclude rather than a set of values to permit.  
`model` | `obj` The alert or object containing the data to validate.  
`model_key` | `str` The attribute key within the model whose value is checked against the list.  
`whitelist` | `Iterable` An optional list of values to use for the filter. If no value is provided, the function uses the connector's default whitelist from the UI.  
  
#### Returns

`True` if the value passes the filtering logic; otherwise, `False`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
