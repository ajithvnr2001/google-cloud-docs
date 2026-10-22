---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-connectors-module/
title: SiemplifyConnectors module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:29.390679+00:00
---

# SiemplifyConnectors module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-connectors-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SiemplifyConnectors module

## _class_ `SiemplifyConnectors.SiemplifyConnectorExecution`
    
    
    SiemplifyConnectors.SiemplifyConnectorExecution(mock_stdin=None)
    

Bases: SiemplifyBase

`MAX_NUM_LOG_ROWS= 5000`

### extract_connector_param
    
    
    extract_connector_param(param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False)
    

Get a connector script parameter.  
Each connector has parameters that are filled when it's configured. This method allows extracting the value of a selected parameter of the currently running connector.\

**Note:** Related concepts: [Integration configuration and script parameters](https://docs.cloud.google.com/chronicle/docs/soar/reference/integration-configuration-script-parameters)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
param_name | {string} | Name of the parameter | N/A | N/A  
default_value | {any} | The default value of the parameter. | N/A | (Optional)  
The given value will be returned if the parameter was not set  
(if `is_mandatory` is set to `False`).  
Default is _None_  
input_type | {obj} | The type of the parameter. For example, {int} | N/A | (Optional)  
The returned value will be cast to the selected input type.  
Default is _str_  
is_mandatory | {boolean} | Defines whether the parameter is mandatory | N/A | If set to `True` and the parameter was not filled,  
an exception will be raised.  
Default is `False`  
print_value | {boolean} | Defines whether to output the fetched value of the parameter to the logs | N/A | Default is `False`  
  
#### Returns

The parameter value, {string} by default, unless input_type is specified.

#### Example
    
    
    from SiemplifyConnectors import SiemplifyConnectorExecution
    siemplify = SiemplifyConnectorExecution()
    param_value= siemplify.extract_connectors_param(
                                           "Logs Folder",
                                           default_value="C:\\Siemplify_Server\\Scripting\\JobLogs",
                                           input_type=str,
                                           is_mandatory=False,
                                           print_value=False)
    

#### Result behavior

The value of the selected parameter will be returned, casted to the selected type.

#### Result value

`C:\Siemplify_Server\Scripting\SampleJob\Logs`

### fetch_and_save_timestamp
    
    
    fetch_and_save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683034181328)
    

Fetch timestamp and save it to the case context.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | Format for date/time | `True` for getting in datetime format,  
`False` for Unix | `False` by default (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {int} | The time stamp to save | N/A | Unix time by default (optional)  
  
### fetch_timestamp
    
    
    fetch_timestamp(datetime_format=False, timezone=False)
    

Get the timestamp saved with `save_timestamp`.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | If `True`, return timestamp as datetime.  
Else, return in Unix | True/False | False by default (optional)  
timezone | Parameter not supported anymore  
  
#### Returns

Saved Unix time/datetime.

### get_connector_context_property
    
    
    get_connector_context_property(identifier, property_key)
    

Get a connector context property.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
identifier | {string} | Context identifier | N/A | N/A  
property_key | {string} | The requested key property | N/A | N/A  
  
#### Returns

{string} the property value

### is_overflowed_alert
    
    
    is_overflowed_alert(environment, alert_identifier, ingestion_time=1683034181328, original_file_path=None, original_file_content=None, alert_name=None, product=None, source_ip=None, source_host=None, destination_ip=None, destination_host=None)
    

Check if the alert is overflowed.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
environment | {string} | Environment name | Example | N/A  
alert_identifier | {string} | Alert identifier | 12345 | N/A  
ingestion_time | {long} | Alert ingestion time | N/A | If not provided, defaults to current time (Unix time format)  
original_file_path | {string} | Path to the file containing the alert's original raw data | N/A | N/A  
original_file_content  | {string} | Content of the file containing the alert's original raw data | N/A | N/A  
alert_name | {string} | Alert name | N/A | N/A  
product | {string} | The product name for the device that generated the alert | QRadar, Trellix ESM | N/A  
source_ip | {string} | The source IP address associated with the alert | 198.51.100.1 | N/A  
source_host | {string} | The source host address associated with the alert | source@example.com,  
source.example.com | N/A  
destination_ip | {string} | Destination IP address associated with the alert | 203.0.113.1 | N/A  
destination_host | {string} | Destination host address associated with the alert | destination.example.com | N/A  
  
#### Returns

{boolean} True/False

#### Example
    
    
    from SiemplifyConnectors import SiemplifyConnectorExecution
    siemplify = SiemplifyConnectorExecution()
    siemplify.is_overflowed_alert(environment, alert_identifier, ingestion_time=SiemplifyUtils.unix_now(), original_file_path, original_file_content, alert_name, product, source_ip, source_host, destination_ip, destination_host)
    

#### Result behavior

`True` if the alert will be overflowed during the ingestion process. Otherwise, `False`.

#### Result value

True/False

### _property_ is_test_run

### _property_ log_location

### _property_ parameters

### return_package
    
    
    return_package(cases, output_variables={}, log_items=[])
    

Return data.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
cases | {[CaseInfo]} | The list of CaseInfo objects | N/A | N/A  
output_variables |  |  |  | Deprecated  
log_items |  |  |  | Deprecated  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyConnectors import SiemplifyConnectorExecution siemplify = SiemplifyConnectorExecution() siemplify.return_package(cases, output_variables, log_items)
    

#### Result value

None

### return_test_result
    
    
    return_test_result(is_success, result_params_dictionary)
    

**Deprecated:** The function is deprecated.

### _property_ run_folder

Build the `run_folder` based on the script name.

#### Returns

{string} full path

#### Result value

`C:Siemplify_ServerScriptingSiemplifyAction<script name>`

### save_timestamp
    
    
    save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683034181328)
    

Save timestamp to the current script context.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | N/A | `True` for datetime format,  
`False` for Unix | Default is `False` (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {long} | Timestamp to save to context | N/A | Timestamp defaults to Unix timestamp of calling the method  
  
### set_connector_context_property
    
    
    set_connector_context_property(identifier, property_key, property_value)
    

Set a case context property using the key/value pair.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
identifier | {string} | Context identifier | N/A | N/A  
property_key | {string} | Key of the property | N/A | N/A  
property_value | {string} | Value of the property | N/A | N/A  
  
### _property_ `whitelist`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
