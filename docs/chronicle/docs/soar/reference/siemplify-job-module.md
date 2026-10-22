---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-job-module/
title: SiemplifyJob module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:21.741866+00:00
---

# SiemplifyJob module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-job-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SiemplifyJob module

## _class_ `SiemplifyJob.SiemplifyJob`

Bases: [**Siemplify**](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module)

Endpoints: `external/v1/sdk/GetFailedETLOperations`

### extract_job_param
    
    
    extract_job_param(param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False)
    

Get a configuration parameter from the integration instance.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
param_name | {string} | Name of the parameter to fetch | N/A | N/A  
default_value | {any} | The default value of the parameter |  | (Optional)  
The given value will be returned if the parameter was not set  
(if is_mandatory is set to `False`).  
`None` by default  
input_type | {obj} | The type of the parameter | N/A | (Optional)  
The returned value will be cast to the selected input type.  
{str} by default  
is_mandatory | {boolean} | Defines whether the parameter is mandatory | N/A | (Optional)  
If set to True and the parameter was not filled, an exception will be raised. `False` by default  
print_value  | {boolean} | Defines whether to output the fetched value of the parameter to the logs. | N/A | (Optional)  
`False` by default  
  
#### Returns

The parameter value, string by default, unless `input_type` is specified.

#### Example
    
    
    from SiemplifyJob import SiemplifyJob
    siemplify = SiemplifyJob()
    param_value= siemplify.extract_job_param(
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
    
    
    fetch_and_save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683034181430)
    

Fetch timestamp and save it to the case context.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | Format for date/time | `True` for getting in datetime format,  
`False` for Unix | `False` by default (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {int} | The timestamp to save | N/A | Unix epoch time by default (optional)  
  
### fetch_timestamp
    
    
    fetch_timestamp(datetime_format=False, timezone=False)
    

Get the timestamp saved with `save_timestamp`.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | If `True`, return timestamp as datetime.  
Else, return in Unix | True/False | `False` by default (optional)  
timezone | Parameter not supported anymore  
  
#### Returns

Saved Unix time/datetime.

### get_configuration
    
    
    get_configuration(provider, environment=None, integration_instance=None)
    

Get the integration configuration.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
provider | {string} | Integration name | VirusTotal | Integration Provider name is case sensitive.  
An error will be thrown if the integration is not installed  
or the string does not exist  
environment | {string} | Configuration for specific environment or 'all' | N/A | (Optional)  
If provided, the credentials will be retrieved from the corresponding  
environment configuration. If no environment is stated,  
the case environment is used by default.  
If there is no configuration for that specific  
environment, the default configuration will be returned  
integration_instance | {string} | Identifier of the integration instance | N/A | N/A  
  
#### Returns

{dict} configuration details

#### Example
    
    
    from SiemplifyJob import SiemplifyJob
    siemplify = SiemplifyJob()
    siemplify.get_configuration(provider="VirusTotal", environment="")
    

#### Result behavior

Dictionary with saved credentials for the integration from the Google Security Operations Marketplace will be returned.

#### Result value
    
    
    {
    u'AgentIdentifier': None,
    u'Api Key': u'c0c412#########################4f85b22e707',
    u'Verify SSL': u'True',
    u'RunRemotely': u'False'
    }
    

### get_failed_actions
    
    
    get_failed_actions(number_of_hours)
    

Get all the ETL jobs that have failed in the specified number of hours.

#### Returns

{dict} failed jobs
    
    
    {'Id':{string}, 'Name':{string}, 'Message':{string}, WorkflowId = {string}, CreationTime: {string}, CaseId:{string}}
    

### get_failed_etljobs
    
    
    get_failed_etljobs(number_of_hours)
    

Get all the ETL jobs that have failed in the specified number of hours.

#### Returns

{dict} failed jobs
    
    
    { 'Id': {string}, 'Name': {string}, Message: {string}, CreationTime: {string}}
    

### get_faulted_connectors
    
    
    get_faulted_connectors(start_unix_time, end_unix_time)
    

Get all the connectors that had failed time between `start_unix_time` and `end_unix_time`.

#### Returns

{dict} failed connectors

#### Result value
    
    
    {'Name': {string}, 'Message': {string}, 'CreationTime': {string}}
    

### get_faulted_jobs
    
    
    get_faulted_jobs(number_of_hours)
    

Get all the jobs that have failed in the specified number of hours.

#### Returns

{[dict]} failed jobs

#### Result value
    
    
    [{'Id': {long}, 'Name':{string}, 'Message':{string}, 'CreationTime':{string}}]
    

### get_job_context_property
    
    
    get_job_context_property(identifier, property_key)
    

Get a job context value by the given key.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
identifier | {string} | Context identifier | N/A | N/A  
property_key | {string} | The key of the property to fetch | N/A | N/A  
  
### get_scoped_job_context_property
    
    
    get_scoped_job_context_property(property_key)
    

Get scoped job context property using the unique identifier of a job.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | The key of the job's context property | N/A | N/A  
  
#### Returns

Value of a specific key.

### get_system_info
    
    
    get_system_info(start_time_unixtime_ms)
    

### property log_location

### save_publisher_logs
    
    
    save_publisher_logs(records)
    

Save publisher log records.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
records | {list} | Records to save | N/A | N/A  
  
### save_timestamp
    
    
    save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683034181430)
    

Save timestamp.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | N/A | `True` for datetime format, `False` for Unix | Default is `False` (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {long} | Timestamp to save to context | N/A | Timestamp defaults to Unix timestamp of calling the method  
  
### send_mail
    
    
    send_mail(subject, message, recipients, attachment_file_name, attachment_content)
    

Send an email (attachments allowed).

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
subject | {string} | Email subject | N/A | N/A  
message | {string} | Email message | N/A | N/A  
attachment_file_name | {string} | Attachment filename | N/A | N/A  
recipients | {[{string}]} | List of recipients | N/A | N/A  
  
### set_job_context_property
    
    
    set_job_context_property(identifier, property_key, property_value)
    

Set scoped job context property using the unique identifier of a job.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
identifier | {string} | Context identifier | N/A | N/A  
property_key | {string} | The key of the job's context property | N/A | N/A  
property_value | {string} | The value of the job's context property | N/A | N/A  
  
### set_scoped_job_context_property
    
    
    set_scoped_job_context_property(property_key, property_value)
    

Set scoped job context property using the unique identifier of a job.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | The key of the job's context property | N/A | N/A  
property_value | {string} | The value of the job's context property | N/A | N/A  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
