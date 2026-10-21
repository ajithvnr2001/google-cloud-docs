---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-smp-time-module/
title: TIPCommon.smp_time \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:43:11.360654+00:00
---

# TIPCommon.smp_time  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-smp-time-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.smp_time

The **TIPCommon.smp_time** module offers a comprehensive set of tools for handling temporal data within integrations. It simplifies complex tasks such as timezone shifting, timestamp persistence for connectors, and critical monitoring functions to detect approaching execution timeouts in actions and connectors.

## Time conversion and manipulation

These utilities provide standardized methods for transforming time data between various formats, including Unix timestamps, RFC 3339 strings, and Python datetime objects.

Function | Parameters | Description  
---|---|---  
`change_timezone()` | 

  * `dtime`: (datetime) The source object.
  * `current_tz`: (str) Current timezone name.
  * `new_tz`: (str) Target timezone name.

| Returns: `datetime.datetime` Shifts a datetime object to a new timezone. Raises `ValueError` if either timezone string is invalid.  
`convert_string_to_timestamp()` | 

  * `datetime_string`: (str) The source string.

| Returns: `int` Parses a datetime string and returns its equivalent Unix timestamp.  
`datetime_to_rfc3339()` | 

  * `datetime_obj`: (datetime) The source object.

| Returns: `str` Converts a datetime object into an RFC 3339 compliant string.  
`get_timestamps()` | 

  * `range_string`: (str) Named time range.
  * `start_time_string`: (str) Start bound.
  * `end_time_string`: (str) End bound.
  * `error_message`: (str) Custom exception text.
  * `time_in_milliseconds`: (bool) Defaults to `False`.

| Returns: `tuple[int, int]` Calculates start and end Unix timestamps based on range descriptions and bound strings.  
`get_timestamps_from_range()` | 

  * `range_string`: (str) Named platform range.
  * `include_timezone`: (bool) Includes TZ info if `True`.

| Returns: `tuple[datetime, datetime]` Calculates start and end datetime objects derived from platform-specific time range strings.  
  
## State and persistence

Persisting the "Last Run Time" is vital for connectors to avoid duplicate ingestion. These functions interface directly with the platform to manage execution checkpoints.

Function | Parameters | Description  
---|---|---  
`get_last_success_time()` | 

  * `siemplify`: (ChronicleSOAR) SDK instance.
  * `offset_with_metric`: (dict) Fallback offset.
  * `time_format`: (int) DATETIME (1) or UNIX (2).
  * `print_value`: (bool) Logs to console if `True`.
  * `microtime`: (bool) Precision toggle.

| Returns: `time` (DataModel) Retrieves the last successful execution time. If none exists, it calculates a fallback based on the offset.  
`save_timestamp()` | 

  * `siemplify`: (ChronicleSOAR) SDK instance.
  * `alerts`: (dict) Batch of processed alerts.
  * `timestamp_key`: (str) Defaults to `'timestamp'`.
  * `incrementation_value`: (int) ms to add to the result.
  * `log_timestamp`: (bool) Logs to console if `True`.
  * `convert_timestamp_to_micro_time`: (bool) Toggle.
  * `convert_a_string_timestamp_to_unix`: (bool) Toggle.

| Returns: `bool` Finds the latest timestamp in an alert batch and saves it. Returns `True` if the state was updated.  
`siemplify_fetch_timestamp()` | 

  * `siemplify`: (ChronicleSOAR) SDK instance.
  * `datetime_format`: (bool) Toggle for object return.
  * `timezone`: (bool) Forces UTC if `True`.

| Returns: `int | datetime` Directly fetches the current execution checkpoint from the platform database.  
`siemplify_save_timestamp()` | 

  * `siemplify`: (ChronicleSOAR) SDK instance.
  * `new_timestamp`: (int) Value to save.
  * `datetime_format`: (bool) Defaults to `False`.
  * `timezone`: (bool) Defaults to `False`.

| Returns: `None` Updates the platform's execution checkpoint with a specific new value.  
`validate_timestamp()` | 

  * `last_run_timestamp`: (datetime) The check value.
  * `offset_in_hours`: (int) Max lookback window.
  * `offset_is_in_days`: (bool) Day-based logic toggle.

| Returns: `datetime` Ensures a timestamp is within the allowed window. Raises `ValueError` if out of range.  
  
## Execution monitoring

Timeout monitoring is a critical safety feature. These functions help scripts identify when they are nearly out of processing time, allowing them to stop gracefully and save their current state.

Function | Parameters | Description  
---|---|---  
`is_approaching_action_timeout()` | 

  * `action_execution_deadline_in_unix`: (int) Deadline.
  * `timeout_threshold_in_sec`: (int) Buffer. Defaults to `10`.

| Returns: `bool` Checks if an action script is within its final buffer period before termination.  
`is_approaching_timeout()` | 

  * `connector_starting_time`: (int) Start time.
  * `python_process_timeout`: (int) Max duration.
  * `timeout_threshold`: (float) `0.9` (TIMEOUT_THRESHOLD).

| Returns: `bool` Detects if a connector has consumed its time budget based on the 90% `TIMEOUT_THRESHOLD`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
