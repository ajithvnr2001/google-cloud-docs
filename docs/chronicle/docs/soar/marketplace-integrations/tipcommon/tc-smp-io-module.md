---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-smp-io-module/
title: smp_io module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:53:05.850029+00:00
---

# smp_io module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-smp-io-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# smp_io module

### TIPCommon.smp_io.read_and_repair_existing_ids

`TIPCommon.smp_io.read_and_repair_existing_ids(siemplify: SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob, default_value_to_return: dict = None, identifier: str = None, ids_file_name: str = 'ids.json', db_key: str = 'ids')→ list`

Reads existing alert IDs and converts them to a list if they are a dictionary. This is needed to avoid regressions.

#### Parameters

Parameters  
---  
`siemplify` | `SiemplifyAction | SiemplifyConnectorExecution | SiemplifyJob`An instance of the Google SecOps SDK.  
`default_value_to_return` | `dict | list | string`The default value to be set when a new file or key is created. If no value is supplied, an internal default of `[]` (`list`) will be set as the new default value.  
`identifier` | `str`The connector's identifier attribute.  
`ids_file_name` | `str`The file name where IDs should be saved when a `FileStream` object has been created.  
`db_key` | `str`The key name where IDs should be saved when a `FileStream` object has been created.  
  
#### Returns

A list of IDs inside the DataStream object.

#### Return type

`list`

### TIPCommon.smp_io.read_content

`TIPCommon.smp_io.read_content(siemplify, file_name, db_key, default_value_to_return=None, identifier=None)`

Read the content of a ConnectorStream object. If the object contains no data or doesn't exist, return a default value.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`file_name` | `str`The name of the file to be validated (when the platform uses files).  
`db_key` | `str`The name of the key to be validated (when the platform uses a database).  
`default_value_to_return` | `dict/list/str`The default value set when new file and key are created. If no value is supplied, an internal default value of `{} (dict)` is set as the new default value.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

`(dict)` The content inside the `DataStream` object. The content passes through `json.loads` before returning.

### TIPCommon.smp_io.read_ids

`TIPCommon.smp_io.read_ids(siemplify, default_value_to_return=None, identifier=None, ids_file_name='ids.json', db_key='ids')`

Reads IDs from a ConnectorStream object. If the object contains no data or doesn't exist, return a default value.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`ids_file_name` | `sttr`The filename where IDs should be saved when a `FileStream` object has been created.  
`db_key` | `str`The key name where IDs should be saved when a `FileStream` object has been created.  
`default_value_to_return` | `dict/list/str`The default value to be set in case when new file and key are created. If no value is supplied, an internal default value `[] (list)` is set as the new default value.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

`(list)` A list of IDs inside the DataStream object. The content passes through `json.loads` before returning.

### TIPCommon.smp_io.read_ids_by_timestamp

`TIPCommon.smp_io.read_ids_by_timestamp(siemplify, offset_in_hours=72, default_value_to_return=None, convert_to_milliseconds=False, cast_keys_to_integers=False, offset_is_in_days=False, identifier=None, ids_file_name='ids.json', db_key='ids')`

Reads IDs from a ConnectorStream object. If the object contains no data or doesn't exist, return a default value.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`offset_in_hours` | `int`The time limit (offset value) of the ID in hours.   
`convert_to_milliseconds` | `bool`Transform each ID's timestamp (Unix) from seconds to milliseconds.  
`cast_keys_to_integers` | `bool`Cast the keys to integers.  
`offset_is_in_days` | `bool`If the offset supplied to this method is in days, set the parameter to `True` for converting the offset days into hours.  
`ids_file_name` | `str`The filename where IDs should be saved when a `FileStream` object has been created.  
`db_key` | `str`The key name where IDs should be saved when a `FileStream` object has been created.  
`default_value_to_return` | `dict/list/str`The default value to be set in case when new file and key are created.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

`(list)` A list of IDs inside the DataStream object. The content passes through `json.loads` before returning.

### TIPCommon.smp_io.write_content

`TIPCommon.smp_io.write_content(siemplify, content_to_write, file_name, db_key, default_value_to_set=None, identifier=None)`

Writes content into a ConnectorStream object.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`content_to_write` | `dict/list/str`The content to be written to the dedicated data stream.  
`file_name` | `str`The name of the file.  
`db_key` | `str`The name of the key.  
`default_value_to_set` | `dict/list/str`The default value set when new file and key are created.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

None.

### TIPCommon.smp_io.write_ids

`TIPCommon.smp_io.write_ids(siemplify, ids, default_value_to_set=None, stored_ids_limit=1000, identifier=None, ids_file_name='ids.json', db_key='ids')`

Writes the last 1000 IDs into a ConnectorStream object.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`ids` | `list/str`The IDs to be written to the dedicated data stream.  
`stored_ids_limit` | `int`The number of recent IDs from the existing IDs which will be written.  
`ids_file_name` | `str`The filename where IDs should be saved when a `FileStream` object has been created.  
`db_key` | `str`The key name where IDs should be saved when a `FileStream` object has been created.  
`default_value_to_set` | `dict/list/str`The default value set when new file and key are created.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

None.

### TIPCommon.smp_io.write_ids_with_timestamp

`TIPCommon.smp_io.write_ids_with_timestamp(siemplify, ids, default_value_to_set=None, identifier=None, ids_file_name='ids.json', db_key='ids')`

Writes IDs into a ConnectorStream object with a timestamp.

Parameters  
---  
`siemplify` | `obj`An instance of the SDK `SiemplifyConnectorExecution` class.  
`ids` | `list/str`The IDs to be written to the dedicated data stream.  
`ids_file_name` | `str`The filename where IDs should be saved when a `FileStream` object has been created.  
`db_key` | `str`The key name where IDs should be saved when a `FileStream` object has been created.  
`default_value_to_set` | `dict/list/str`The default value to be set in case when new file and key are created.  
`identifier` | `str`The connector's identifier attribute.  
  
#### Returns

None.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
