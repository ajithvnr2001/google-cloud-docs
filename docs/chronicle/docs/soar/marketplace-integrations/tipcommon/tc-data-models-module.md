---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module/
title: data_models module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:01.872432+00:00
---

# data_models module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# data_models module

This module contains data classes for representing the following:

  * Data models
  * Alerts
  * Variable containers
  * General parameters
  * Connector parameters



## _class_ TIPCommon.data_models.AlertCard

_class_ `TIPCommon.data_models.AlertCard(id_: int, creation_time_unix_time_ms: int, modification_time_unix_time_ms: int, identifier: str, status: int, name: str, priority: int, workflow_status: int, sla_expiration_unix_time: int | None, sla_critical_expiration_unix_time: int | None, start_time: int, end_time: int, alert_group_identifier: str, events_count: int, title: str, rule_generator: str, device_product: str, playbook_attached: str | None, playbook_run_count: int, is_manual_alert: bool, sla: SLA, fields_groups: list[FieldsGroup], source_url: str | None, source_rule_url: str | None, siem_alert_id: str | None)`

Bases: **object**

Represents a summary card of an alert, containing its key details and metadata.

#### _classmethod_ `from_json(alert_card_json: Dict[str, Any])→ AlertCard`

Creates an `AlertCard` object from a JSON dictionary representing its attributes.

## _class_ TIPCommon.data_models.AlertEvent

_class_ `TIPCommon.data_models.AlertEvent(fields: list[EventPropertyField], identifier: str, case_id: int, alert_identifier: str, name: str, product: str, port: str | None, source_system_name: str, outcome: str | None, time: int, type_: str, artifact_entities: list[str])`

Bases: **object**

Represents a single event associated with an alert within a case.

#### _classmethod_ `from_json(event_json: MutableMapping[str, Any])→ AlertEvent`

Creates an `AlertEvent` object from a JSON dictionary.

## _class_ TIPCommon.data_models.AlertPriority

_class_ `TIPCommon.data_models.AlertPriority(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the priority levels for an alert.

### Constants

  * `CRITICAL = 100`

  * `HIGH = 80`

  * `INFORMATIVE = -1`

  * `LOW = 40`

  * `MEDIUM = 60`

  * `UNCHANGED = 0`




## _class_ TIPCommon.data_models.BaseAlert

_class_ `TIPCommon.data_models.BaseAlert(raw_data, alert_id)`

Bases: **object**

Represents a base alert. It has the following properties:

#### Attributes

`raw_data` | The raw data for the alert.  
---|---  
`alert_id` | The ID of the alert.  
  
#### Methods

  * `to_json()→ dict`

**Note:** The `to_json` method converts the alert to JSON format as returned from `json.loads()`.

##### Example
    
    
    >>> from data_models import BaseAlert
    >>> alert = BaseAlert({'foo': 'bar'}, 100)
    >>> alert.raw_data
    {'foo': 'bar'}
    >>> alert.alert_id
    100
    >>> alert.to_json()
    {'foo': 'bar'}
    

## _class_ TIPCommon.data_models.BaseDataModel

_class_ `TIPCommon.data_models.BaseDataModel(raw_data)`

Bases: **object**

Represents a base data model. 

#### Attributes

Attribute | Description  
---|---  
`raw_data` | The raw data for the data model.  
  
#### Methods

  * `to_json()→ dict`

**Note:** The `to_json` method converts the raw data to JSON format as returned from `json.loads()`.

##### Example
    
    
    >>> from data_models import BaseDataModel
    >>> data = BaseDataModel({'foo': 'bar'})
    >>> data.raw_data
    {'foo': 'bar'}
    >>> data.to_json()
    {'foo': 'bar'}
    

## _class_ TIPCommon.data_models.CaseDataStatus

_class_ `TIPCommon.data_models.CaseDataStatus(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `ALL = 3`

  * `CLOSED = 2`

  * `CREATION_PENDING = 5`

  * `MERGED = 4`

  * `NEW = 0`

  * `OPENED = 1`




## _class_ TIPCommon.data_models.CaseDetails

_class_ `TIPCommon.data_models.CaseDetails(id_: int, creation_time_unix_time_ms: int, modification_time_unix_time_ms: int, name: str, priority: int, is_important: bool, is_incident: bool, start_time_unix_time_ms: int, end_time_unix_time_ms: int, assigned_user: str, description: str | None, is_test_case: bool, type_: int, stage: str, environment: str, status: CaseDataStatus, incident_id: int | None, tags: list[str], alerts: list[AlertCard], is_overflow_case: bool, is_manual_case: bool, sla_expiration_unix_time: int | None, sla_critical_expiration_unix_time: int | None, stage_sla_expiration_unix_time_ms: int | None, stage_sla__critical_expiration_unix_time_in_ms: int | None, can_open_incident: bool, sla:SLA, stage_sla: SLA)`

Bases: **object**

#### _classmethod_ `from_json(case_details_json: Dict[str, Any])→ CaseDetails`

Creates a `CaseDetails` object from a JSON dictionary.

#### _property_ is_closed

_property_ `is_closed: bool`

Indicates if the case is closed.

#### _property_ is_open

_property_ `is_open: bool`

Indicates if the case is open.

## _class_ TIPCommon.data_models.CasePriority

_class_ `TIPCommon.data_models.CasePriority(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the priority levels for an alert.

### Constants

  * `CRITICAL = 100`

  * `HIGH = 80`

  * `INFORMATIVE = -1`

  * `LOW = 40`

  * `MEDIUM = 60`

  * `UNCHANGED = 0`




## _class_ TIPCommon.data_models.CaseWallAttachment

_class_ `TIPCommon.data_models.CaseWallAttachment(name: 'str', file_type: 'str', base64_blob: 'str', is_important: 'bool', case_id: 'int | None' = None)`

Bases: **object**

Represents an attachment to be added to a case wall.

#### Attributes

Attribute | Description | Type  
---|---|---  
`base64_blob` | The base64 encoded content of the attachment. | `str`  
`case_id` | The ID of the case the attachment belongs to. | `int | None`  
`file_type` | The file type of the attachment. | `str`  
`is_important` | Indicates if the attachment is marked as important. | `bool`  
`name` | The name of the attachment file. | `str`  
  
## _class_ TIPCommon.data_models.ConnectorCard

_class_ `TIPCommon.data_models.ConnectorCard(integration: str, display_name: str, identifier: str, is_enabled: bool, is_remote: bool, status: ConnectorConnectivityStatusEnum)`

Bases: **object**

Represents a summary card for a connector instance.

#### _classmethod_ `from_json(connector_card_json: MutableMapping[str, Any])→ ConnectorCard`

Creates a `ConnectorCard` object from a JSON dictionary.

## _class_ TIPCommon.data_models.ConnectorConnectivityStatusEnum

_class_ `TIPCommon.data_models.ConnectorConnectivityStatusEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the connectivity status of a connector.

### Constants

  * `LIVE = 0`

  * `NO_CONNECTIVITY = 1`




## _class_ TIPCommon.data_models.ConnectorParamTypes

_class_ `TIPCommon.data_models.ConnectorParamTypes(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

#### Constants

Represents the types of connector parameters.

  * `BOOLEAN = 0`

  * `DOMAIN = 7`

  * `EMAIL = 8`

  * `HOST = 5`

  * `INTEGER = 1`

  * `IP = 4`

  * `NULL = -1`

  * `PASSWORD = 3`

  * `SCRIPT = 12`

  * `STRING = 2`

  * `URL = 6`




## _class_ TIPCommon.data_models.ConnectorParameter

_class_ `TIPCommon.data_models.ConnectorParameter(raw_param)`

Bases: **Parameter**

Represents a connector parameter.

#### Attributes

Attribute | Description  
---|---  
`name` | The name of the parameter.  
`value` | The value of the parameter.  
`type` | The type of the parameter (according to `ConnectorParamTypes`).  
`mode` | The mode of the parameter.  
`is_mandatory` | Define whether the parameter is mandatory.  
  
##### Example
    
    
    >>> from data_models import ConnectorParameter, ConnectorParamTypes
    >>> p = ConnectorParameter({
        'param_name': 'api_root',
        'type': ConnectorParamTypes.STRING,
        'param_value': 'http://foo.bar',
        'is_mandatory': True,
        'mode': 0
        })
    >>> print(p)
    ConnectorParameter(name='api_root', value='http://foo.bar', type=2, mode=0, is_mandatory=True)
    

## _class_ TIPCommon.data_models.Container

Bases: **object**

Represents a container for variables.

##### Example
    
    
    >>> from data_models import Container
    >>> container = Container()
    >>> container.one = 1
    >>> container.one
    1
    

## _class_ TIPCommon.data_models.CustomField

_class_ `TIPCommon.data_models.CustomField(id: 'int', display_name: 'str', description: 'str', type: 'str', scopes: 'list[CustomFieldScope]')`

Bases: **object**

Represents a custom field definition within the platform.

#### Attributes

Attribute | Description  
---|---  
`description` | `str`The description of the custom field.  
`display_name` | `str`The display name of the custom field.  
`id` | `int`The unique ID of the custom field.  
`scopes` | `list[CustomFieldScope]`The scopes (e.g., Alert, Case) where the custom field is applicable.  
`type` | `str`The data type of the custom field.  
  
#### _classmethod_ `from_json(json_data: MutableMapping[str, Any])→ CustomField`

Creates a `CustomField` object from a JSON dictionary.

## _class_ TIPCommon.data_models.CustomFieldScope

_class_ `TIPCommon.data_models.CustomFieldScope(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the possible scopes where a custom field can be applied.

### Constants

  * `ALERTS = 'Alert'`

  * `CASE = 'Case'`




### Methods

  * `build_parent_path(identifier: int)→ str` Builds the parent path for the custom field value based on the identifier.



## _class_ TIPCommon.data_models.CustomFieldValue

_class_ `TIPCommon.data_models.CustomFieldValue(custom_field_id: 'int', values: 'list[str]', scope: 'CustomFieldScope', identifier: 'int')`

Bases: **object**

Represents the value set for a specific custom field.

#### Attributes

Attribute | Description  
---|---  
`custom_field_id` | `int`The ID of the custom field.  
`identifier` | `int`The ID of the entity (case/alert) to which the value belongs.  
`scope` | `CustomFieldScope`The scope (e.g., Alert, Case) where the custom field value applies.  
`values` | `list[str]`The list of values set for the custom field.  
  
#### _classmethod_ `from_json(json_data: MutableMapping[str, Any])→ CustomFieldValue`

Creates a `CustomFieldValue` object from a JSON dictionary.

## _class_ TIPCommon.data_models.DatabaseContextType

_class_ `TIPCommon.data_models.DatabaseContextType(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the types of database contexts for data storage.

### Constants

  * `ALERT = 2`

  * `CASE = 1`

  * `CONNECTOR = 4`

  * `GLOBAL = 0`

  * `JOB = 3`




## _class_ TIPCommon.data_models.EventPropertyField

_class_ `TIPCommon.data_models.EventPropertyField(order: int, group_name: str, is_integration: bool, is_highlight: bool, items: list[FieldItem])`

Bases: **object**

Represents a field group within an event's properties.

#### _classmethod_ `from_json(event_property_field: MutableMapping[str, Any])→ EventPropertyField`

Creates an `EventPropertyField` object from a JSON dictionary.

## _class_ TIPCommon.data_models.FieldGroupItem

_class_ `TIPCommon.data_models.FieldGroupItem(original_name: str, name: str, value: str)`

Bases: **object**

Represents a single key-value item within an event's field group.

#### _classmethod_ `from_json(field_group_json: MutableMapping[str, Any])→ FieldGroupItem`

Creates a `FieldGroupItem` object from a JSON dictionary.

## _class_ TIPCommon.data_models.FieldItem

_class_ `TIPCommon.data_models.FieldItem(original_name: str, name: str, value: str)`

Bases: **object**

Represents a single item within a field, containing its original name, formatted name, and value.

#### _classmethod_ `from_json(field_json: MutableMapping[str, Any])→ FieldItem`

Creates a `FieldItem` object from a JSON dictionary.

## _class_ TIPCommon.data_models.FieldsGroup

_class_ `TIPCommon.data_models.FieldsGroup(order: int, group_name: str, is_integration: bool, is_highlight: bool, items: list[[FieldGroupItem]])`

Bases: **object**

Represents a group of fields within a larger data structure, often used for display.

#### _classmethod_ `from_json(field_group_json: Dict[str, Any])→ FieldsGroup`

Creates a `FieldsGroup` object from a JSON dictionary.

## _class_ TIPCommon.data_models.GoogleServiceAccount

_class_ `TIPCommon.data_models.GoogleServiceAccount(account_type: str, project_id: str, private_key_id: str, private_key: str, client_email: str, client_id: str, auth_uri: str, token_uri: str, auth_provider_x509_url: str, client_x509_cert_url: str)`

Bases: **object**

Represents the attributes of a Google Service Account.

### Methods

  * `to_dict()→ dict` Serializes data model into dict.



#### Returns

A Service Account JSON dict.

#### Return type

`dict`

## _class_ TIPCommon.data_models.InstalledIntegrationInstance

_class_ `TIPCommon.data_models.InstalledIntegrationInstance(instance: MutableMapping[str, Any], identifier: str, integration_identifier: str, environment_identifier: str, instance_name: str)`

Bases: **object**

Represents an installed instance of an integration within an environment.

#### _classmethod_ `from_json(integration_env_json: MutableMapping[str, Any])→ InstalledIntegrationInstance`

Creates a InstalledIntegrationInstance object from a JSON dictionary.

##### Parameters

Parameters  
---  
`integration_env_json` | `SingleJson`JSON data containing integration environment information.  
  
##### Returns

An instance of the specified class initialized with data from `raw_data`.

##### Return type

`InstalledIntegrationInstance`

## _class_ TIPCommon.data_models.JobParamType

_class_ `TIPCommon.data_models.JobParamType(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `BOOLEAN = 0`

  * `DOMAIN = 7`

  * `HOST = 5`

  * `INTEGER = 1`

  * `IP = 4`

  * `NULL = -1`

  * `PASSWORD = 3`

  * `STRING = 2`

  * `URL = 6`




## _class_ TIPCommon.data_models.Parameter

_class_ `TIPCommon.data_models.Parameter(raw_param)`

Bases: **object**

A parent class representing a parameter.

#### Attributes

Attribute | Description  
---|---  
`raw_data` | The raw data for the parameter.  
  
##### Example
    
    
    >>> from data_models import Parameter
    >>> p = Parameter({'foo': 'bar'})
    >>> print(p)
    Parameter(raw_data={'foo': 'bar'})
    

## _class_ TIPCommon.data_models.SLA

_class_ `TIPCommon.data_models.SLA(sla_expiration_time: int | None, critical_expiration_time: int | None, expiration_status: int, remaining_time_since_last_pause: int | None)`

Bases: **object**

Represents Service Level Agreement (SLA) details for a case or alert.

#### _classmethod_ `from_json(sla_json: Dict[str, Any])→ SLA`

Creates an SLA object from a JSON dictionary.

## _class_ TIPCommon.data_models.ScriptContext

_class_ `TIPCommon.data_models.ScriptContext(target_entities: 'str' = '', case_id: 'int | str | None' = None, alert_id: 'str' = '', environment: 'str' = '', workflow_id: 'str' = '', workflow_instance_id: 'str | None' = None, parameters: 'SingleJson' = <factory>, integration_identifier: 'str' = '', integration_instance: 'str' = '', action_definition_name: 'str' = '', original_requesting_user: 'str' = '', execution_deadline_unix_time_ms: 'int' = 0, async_polling_interval_in_sec: 'int' = 0, async_total_duration_deadline: 'int' = 0, script_timeout_deadline: 'int' = 0, default_result_value: 'str' = '', use_proxy_settings: 'bool' = False, max_json_result_size: 'int' = 15, vault_settings: 'SiemplifyVault | None' = None, environment_api_key: 'str | None' = None, unique_identifier: 'str' = '', job_api_key: 'str' = '', connector_context: 'ConnectorContext | None' = None)`

Bases: **object**

Represents the execution context for a script or action, providing access to various runtime parameters and data.

#### Attributes

Attribute | Description  
---|---  
`action_definition_name` | `str`The name of the action definition being executed.Defaults to `''`.  
`alert_id` | `str`The ID of the alert associated with the current execution.Defaults to `''`.  
`async_polling_interval_in_sec` | `int`The interval for asynchronous polling in seconds.Defaults to `0`.  
`async_total_duration_deadline` | `int`The total duration deadline for asynchronous operations.Defaults to `0`.  
`case_id` | `int | str | None`The ID of the case associated with the current execution.Defaults to `None`.  
`connector_context` | `ConnectorContext | None`A context specific to connector execution.Defaults to `None`.  
`default_result_value` | `str`The default value for the action's result.Defaults to `''`.  
`environment` | `str`The execution environment.Defaults to `''`.  
`environment_api_key` | `str | None`The API key for the environment.Defaults to `None`.  
`execution_deadline_unix_time_ms` | `int`The Unix timestamp (in milliseconds) indicating the execution deadline.Defaults to `0`.  
`integration_identifier` | `str`The identifier of the integration being used.Defaults to `''`.  
`integration_instance` | `str`The name of the integration instance being used.Defaults to `''`.  
`job_api_key` | `str`API key specific to the job.Defaults to `''`.  
`max_json_result_size` | `int`The maximum allowed size for JSON results.Defaults to `15`.  
`original_requesting_user` | `str`The user who originally initiated the request.Defaults to `''`.  
`parameters` | `SingleJson`A JSON object containing the parameters for the script/action.  
`script_timeout_deadline` | `int`The deadline for script execution timeout.Defaults to `0`.  
`target_entities` | `str`Comma-separated string of target entities.Defaults to `''`.  
`unique_identifier` | `str`A unique identifier for the execution context.Defaults to `''`.  
`use_proxy_settings` | `bool`Indicates whether proxy settings should be used.Defaults to `False`.  
`vault_settings` | `SiemplifyVault | None`Vault settings for secure credential retrieval.Defaults to `None`.  
`workflow_id` | `str`The ID of the workflow.Defaults to `''`.  
`workflow_instance_id` | `str | None`The ID of the workflow instance.Defaults to `None`.  
  
### Methods

  * `to_json()→ MutableMapping[str, Any]` Serializes the context object into a mutable mapping (JSON dictionary).

  * `update(attributes: MutableMapping[str, Any])→ None` Updates the context object with new attributes from a mutable mapping.




## _class_ TIPCommon.data_models.SmimeEmailConfig

_class_ `TIPCommon.data_models.SmimeEmailConfig(email: 'email.message.Message', private_key_b64: 'str', certificate_b64: 'str', ca_certificate_b64: 'str')`

Bases: **object**

Represents the configuration for sending S/MIME encrypted or signed emails.

#### Attributes

Attribute | Description  
---|---  
`ca_certificate_b64` | `str`The base64 encoded CA certificate.  
`certificate_b64` | `str`The base64 encoded certificate.  
`email` | `Message`The email message object.  
`private_key_b64` | `str`The base64 encoded private key.  
  
## _class_ TIPCommon.data_models.SmimeType

_class_ `TIPCommon.data_models.SmimeType(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

Represents the types of S/MIME operations.

### Constants

  * `ENCRYPTED = 'encrypted'`

  * `SIGNED = 'signed'`




## _class_ TIPCommon.data_models.TypedContainer

_class_ `TIPCommon.data_models.TypedContainer(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Generic[T]**

Container for a specific type that provides type intellisense.

## _class_ TIPCommon.data_models.UserProfileCard

_class_ `TIPCommon.data_models.UserProfileCard(raw_data: dict, first_name: str, last_name: str, user_name: str, account_state: int)`

Bases: **object**

Represents a user profile summary card.

#### _classmethod_ `from_json(user_profile_card_response: dict)→ UserProfileCard`

Creates a `UserProfileCard` object from a JSON dictionary.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
