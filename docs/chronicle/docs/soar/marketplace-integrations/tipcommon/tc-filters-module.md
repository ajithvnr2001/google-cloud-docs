---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-filters-module/
title: Filters module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:23.103546+00:00
---

# Filters module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-filters-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Filters module

### TIPCommon.filters.filter_list_by_type

`TIPCommon.filters.filter_list_by_type(array, inner_type)`

Filters out any items in the list that are not of the requested type.

Parameters  
---  
`array` | `list[Any]`The list to check.  
`inner_type` | `type`The requested type of the items in the list.  
  
#### Example
    
    
    >>> arr = [1, 2, '3', 4]
    >>> arr1 = purify_typed_list(arr, int)
    >>> arr2 = purify_typed_list(arr, str)
    >>> arr1
    [1, 2, 4]
    >>> arr2
    ['3']
    

#### Returns

A new array containing only the items of the `inner_type` type.

#### Return type

`list[type[inner_type]]`

### TIPCommon.filters.filter_none_kwargs

`TIPCommon.filters.filter_none_kwargs(**kwargs)`

Filters out arguments with `None` values.

Parameters  
---  
`**kwargs` | Keyword arguments.  
  
#### Returns

Keyword arguments where the argument value is not `None`.

#### Return type

`dict`

### TIPCommon.filters.filter_old_alerts

`TIPCommon.filters.filter_old_alerts(siemplify, alerts, existing_ids, id_key='alert_id')`

Filters alerts that were already processed.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`alerts` | `list`A list of Alert objects.  
`existing_ids` | `list`A list of IDs to filter.  
`id_key` | `str`The key of the identifier under which the IDs can be found in the alert.  
Default is `alert_id`.  
  
#### Returns

A list of filtered Alert objects.

### TIPCommon.filters.filter_old_ids

`TIPCommon.filters.filter_old_ids(alert_ids, existing_ids)`

Filters IDs that were already processed.

Parameters  
---  
`alert_ids` | `list`A list of new IDs from the alert to filter.  
`existing_ids` | `list`A list of IDs for comparison.  
  
#### Returns

A list of filtered IDs.

### TIPCommon.filters.filter_old_ids_by_timestamp

`TIPCommon.filters.filter_old_ids_by_timestamp(ids, offset_in_hours, convert_to_milliseconds, offset_is_in_days)`

Filters IDs that appeared earlier than `IDS_HOURS_LIMIT` hours.

Parameters  
---  
`ids` | `dict`The IDs to filter.  
`offset_in_hours` | `int`The IDs time limit (offset value) in hours.  
`offset_is_in_days` | `bool`If the offset supplied to this method is in days, set it to `True` for converting the offset days into hours.  
`convert_to_milliseconds` | `bool`Transform each ID's timestamp (UNIX) from seconds to milliseconds.  
  
#### Returns

(`dict`) The filtered IDs.

### TIPCommon.filters.pass_whitelist_filter

`TIPCommon.filters.pass_whitelist_filter(siemplify, whitelist_as_a_blacklist, model, model_key, whitelist=None)`

Determines whether values from a key in a model pass the allowlist filter.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`whitelist_as_a_blacklist` | `bool`The value of the connector's input checkbox to use allowlist as a blocklist.  
`model` | `obj`An alert object of some type from which to extract the specific type or ID which will be matched against the allowlist.  
`model_key` | `str`The key (attribute) whose value is the specific type or ID which will be matched against the allowlist.  
`whitelist` | `iterable`The list used to determine whether a value passes the filter. If no value is provided, the default is the full connector's allowlist as displayed in the Google Security Operations UI.  
  
#### Returns

`True` if the model passed the filter successfully. Else, `False`.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
