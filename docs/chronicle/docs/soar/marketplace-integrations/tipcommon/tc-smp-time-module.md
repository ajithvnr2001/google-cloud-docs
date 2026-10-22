---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-smp-time-module/
title: smp_time module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:01.727613+00:00
---

# smp_time module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-smp-time-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# smp_time module

### TIPCommon.smp_time.change_timezone

`TIPCommon.smp_time.change_timezone(dtime: datetime, current_tz: str, new_tz: str)→ datetime`

Changes the time zone of a `datetime.datetime` object.

#### Parameters

Parameters  
---  
`dtime` | `datetime.datetime`The datetime object whose time zone is changed.  
`current_tz` | `str`The current time zone.  
`new_tz` | `str`The time zone to change to.  
  
#### Returns

A new datetime object with a new time zone.

#### Return type

`datetime.datetime`

#### Raises

`ValueError` – When one of the time zones is not valid.

### TIPCommon.smp_time.convert_string_to_timestamp

`TIPCommon.smp_time.convert_string_to_timestamp(datetime_string: str)→ int`

Converts a datetime string to a timestamp.

#### Parameters

Parameters  
---  
`datetime_string` | `str`A datetime string.  
  
#### Returns

The timestamp.

#### Return type

`int`

### TIPCommon.smp_time.datetime_to_rfc3339

`TIPCommon.smp_time.datetime_to_rfc3339(datetime_obj: datetime)→ str`

Converts a datetime object to RFC 3999 representation.

#### Parameters

Parameters  
---  
`datetime_obj` | `datetime.datetime`The datetime object to convert.  
  
#### Returns

The RFC 3339 representation of the datetime.

#### Return type

`str`

### TIPCommon.smp_time.get_last_success_time

`TIPCommon.smp_time.get_last_success_time(siemplify, offset_with_metric, time_format=2, print_value=True, microtime=False)`

Gets the last success time or datetime.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`offset_with_metric` | `dict`The metric and value.  
Example: `{'hours': 1}`  
`time_format` | `int`The format of the output time.  
Example: `DATETIME, UNIX`  
`print_value` | _Optional_`bool`Indicates whether to print the value or not.  
Default is `True`.  
`microtime` | _Optional_`bool`Indicates whether to return Unix time including microtime.  
Default is `False`.  
  
#### Returns

The last success time.

#### Return type

`Time`

### TIPCommon.smp_time.get_timestamps

`TIPCommon.smp_time.get_timestamps(range_string: str, start_time_string: str, end_time_string: str, error_message: str = None, time_in_milliseconds: bool = False)→ tuple[int, int]`

Gets start and end time timestamps.

#### Parameters

Parameters  
---  
`range_string` | `str`The time range string.  
`start_time_string` | `str`The start time.  
`end_time_string` | `str`The end time.  
`error_message` | `str`An error message for raised exception.Defaults to `None`.  
`time_in_milliseconds` | `bool`Define whether to return start time and end time in milliseconds.Defaults to `False`.  
  
#### Returns

The start time and end time timestamps.

#### Return type

`tuple`

### TIPCommon.smp_time.get_timestamps_from_range

`TIPCommon.smp_time.get_timestamps_from_range(range_string: str, include_timezone: bool = False)→ tuple[datetime, datetime]`

Gets start time and end time timestamps from a range.

#### Parameters

Parameters  
---  
`range_string` | `str`The time range string.  
`include_timezone` | `bool, optional`Define whether to include time zone information in timestamps.Defaults to `False`.  
  
#### Returns

The start time and end time timestamps.

#### Return type

`tuple`

### TIPCommon.smp_time.is_approaching_action_timeout

`TIPCommon.smp_time.is_approaching_action_timeout(action_execution_deadline_in_unix, timeout_threshold_in_sec=10)`

Checks if the action script is approaching its dedicated script deadline.

Each action script has a specific deadline dedicated to it. This function checks if the current time is less than the deadline by at least `timeout_threshold_in_sec` seconds. The default is 10 seconds, meaning that if the action is 10 or less seconds from its script deadline (at the time of the check) the function returns `True`. If the deadline is exceeded, the function returns `False`.

Parameters  
---  
`action_execution_deadline_in_unix` | `int`The deadline for action execution.  
`timeout_threshold_in_sec` | `int`The timeout threshold in seconds.  
  
#### Returns

`True` if timeout is approaching or `False` in any other case.

### TIPCommon.smp_time.is_approaching_timeout

`TIPCommon.smp_time.is_approaching_timeout(connector_starting_time, python_process_timeout, timeout_threshold=0.9)`

Checks if a timeout is approaching.

Parameters  
---  
`connector_starting_time` | `int`The time the connector started.  
`python_process_timeout` | `int`The maximum amount of time the connector is allowed to run.  
`timeout_threshold` | `float`The threshold at which the connector is considered to be approaching a timeout.  
Default is `TIMEOUT_THRESHOLD`.   
  
#### Returns

`True` if the connector is approaching a timeout or `False` in any other case.

### TIPCommon.smp_time.save_timestamp

`TIPCommon.smp_time.save_timestamp(siemplify, alerts, timestamp_key='timestamp', incrementation_value=0, log_timestamp=True, convert_timestamp_to_micro_time=False, convert_a_string_timestamp_to_unix=False)`

Saves the last timestamp for given alerts.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`alerts` | `dict`The list of alerts to find the last timestamp.  
`timestamp_key` | _Optional_`str`The key for getting timestamp from alert.  
Default is `timestamp`.  
`incrementation_value` | _Optional_`int`The value to increment the last timestamp in milliseconds.  
Default is 0.  
`log_timestamp` | _Optional_`bool`Indicates whether to log the timestamp or not.   
Default is `True`.  
`convert_timestamp_to_micro_time` | _Optional_`bool`Indicates whether to convert the timestamp to microtime.  
Default is `False`.  
`convert_a_string_timestamp_to_unix` | _Optional_`bool`Indicates whether to convert a string timestamp to Unix.  
Default is `False`.  
  
#### Returns

A boolean indicating whether the timestamp is updated.

### TIPCommon.smp_time.siemplify_fetch_timestamp

`TIPCommon.smp_time.siemplify_fetch_timestamp(siemplify, datetime_format=False, timezone=False)`

Fetches the timestamp from Siemplify.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`datetime_format` | _Optional_`bool` Indicates whether to return the timestamp in a `datetime` format.   
Default is `False`.  
`timezone` | _Optional_`bool` Indicates whether to return the timestamp in a UTC time zone.   
Default is `False`.  
  
#### Returns

The timestamp.

### TIPCommon.smp_time.siemplify_save_timestamp

`TIPCommon.smp_time.siemplify_save_timestamp(siemplify, datetime_format=False, timezone=False, new_timestamp=1696256382032)`

Saves the timestamp to Siemplify.

Parameters  
---  
`siemplify` | `obj` An instance of the SDK `SiemplifyConnectorExecution` class.   
`datetime_format` | _Optional_`bool` Indicates whether to save the timestamp in a `datetime` format.   
Default is `False`.  
`timezone` | _Optional_`bool` Indicates whether to save the timestamp in a UTC time zone.   
Default is `False`.  
`new_timestamp` | _Optional_`int` The new timestamp to save.  
  
#### Returns

None.

### TIPCommon.smp_time.validate_timestamp

`TIPCommon.smp_time.validate_timestamp(last_run_timestamp, offset_in_hours, offset_is_in_days=False)`

Validates the timestamp in a time range.

Parameters  
---  
`last_run_timestamp` | `datetime`The last run timestamp.  
`offset_in_hours` | `int`The time limit in hours.  
`offset_is_in_days` | _Optional_`bool` Indicates whether the offset is in days.   
Default is `False`.  
  
#### Raises

`ValueError` \- When the timestamp is not valid.

#### Returns

The validated timestamp.

#### Return type

`datetime`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
