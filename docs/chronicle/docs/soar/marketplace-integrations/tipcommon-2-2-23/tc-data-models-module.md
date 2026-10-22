---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-data-models-module/
title: data_models module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:52.315419+00:00
---

# data_models module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-data-models-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# `data_models` module

This module contains data classes for representing the following:

  * Data models
  * Alerts
  * Variable containers
  * General parameters
  * Connector parameters



### _class_ TIPCommon.data_models.AlertCard

_class_ `TIPCommon.data_models.AlertCard(id_: int, creation_time_unix_time_ms: int, modification_time_unix_time_ms: int, identifier: str, status: int, name: str, priority: [AlertPriority](#TIPCommon.data_models.AlertPriority) | int | None, workflow_status: int | None, sla_expiration_unix_time: int | None, sla_critical_expiration_unix_time: int | None, start_time: int, end_time: int, alert_group_identifier: str, events_count: int, title: str, rule_generator: str, device_product: str, device_vendor: str, playbook_attached: bool | None, playbook_run_count: int | None, is_manual_alert: bool | None, sla: [SLA](#TIPCommon.data_models.SLA) | None, fields_groups: list[[FieldsGroup](#TIPCommon.data_models.FieldsGroup)], source_url: str | None, source_rule_url: str | None, siem_alert_id: str | None, additional_properties: str | None, case_id: int | None, ticket_id: str | None, closure_details: MutableMapping[str, Any] | None, event_count: int | None = None, product_families: list[str] | None = None, entity_cards: list[MutableMapping[str, Any]] | None = None, security_event_cards: list[MutableMapping[str, Any]] | None = None, involved_relations: list[MutableMapping[str, Any]] | None = None)`

Bases: **object**

**AlertCard** represents a summary card for an alert, encapsulating critical metadata and status indicators used for visualization and tracking within the platform.

#### Methods

The following methods facilitate the serialization and reconstruction of alert cards from structured data.

Methods  
---  
`from_json()` |  `from_json(alert_card_json: dict[str, Any]) → AlertCard` A class method that creates an `AlertCard` instance from a JSON dictionary.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `AlertCard` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary structural attributes and complex data models associated with the alert.

Attributes  
---  
`fields_groups` |  `list[FieldsGroup]` A list of grouped fields associated with the alert, used for structured data presentation in the UI.  
`sla` |  `SLA` The Service Level Agreement object defining the response and resolution timeframes for the alert.  
  
### _class_ TIPCommon.data_models.AlertEvent

_class_ `TIPCommon.data_models.AlertEvent(fields: list[EventPropertyField], identifier: str, case_id: int, alert_identifier: str, name: str, product: str, port: str | None, source_system_name: str, outcome: str | None, time: int, type_: str, artifact_entities: list[str])`

Bases: **object**

**AlertEvent** represents an individual event associated with an alert, containing specific telemetry data, field properties, and entity relationships.

#### Methods

The following method fƒconacilitates the reconstruction of event objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(event_json: MutableMapping[str, Any]) → AlertEvent` A class method that creates an `AlertEvent` instance from a JSON dictionary representing its attributes.  
  
#### Attributes

The following table highlights the primary structural attributes and complex data models associated with the event.

Attributes  
---  
`fields` |  `list[EventPropertyField]` A list of property fields specific to the event, defining its unique data points.  
`artifact_entities` |  `list[str]` A list of entity identifiers extracted from the event telemetry.  
  
### _class_ TIPCommon.data_models.AlertPriority

_class_ `TIPCommon.data_models.AlertPriority(value)`

Bases: **Enum**

**AlertPriority** defines the standardized integer-based severity levels used to categorize and prioritize alerts within the platform.

##### Constants

The following constants represent the specific priority values assigned to alerts.

Constants  
---  
`CRITICAL` | `100`  
`HIGH` | `80`  
`MEDIUM` | `60`  
`LOW` | `40`  
`UNCHANGED` | `0`  
`INFORMATIVE` | `-1`  
  
### _class_ TIPCommon.data_models.AttachmentMetadata

_class_ `TIPCommon.data_models.AttachmentMetadata(raw_data: SingleJson)`

Bases: **object**

**AttachmentMetadata** encapsulates the descriptive data and properties associated with a file attachment, providing methods for structured data conversion and retrieval.

#### Methods

The following method provides a standardized way to reconstruct case objects from JSON payloads.

Methods  
---  
`from_json()` |  `from_json(result_data: MutableMapping[str, Any]) → Self` A class method that initializes a new `AttachmentMetadata` instance using a provided dictionary of metadata properties.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Serializes the `AttachmentMetadata` object back into a JSON-compatible dictionary format.  
  
#### Attributes

The following table highlights the primary data structures used to store the attachment's metadata properties.

Attributes  
---  
`raw_data` |  `MutableMapping[str, Any]` The underlying dictionary containing the raw metadata attributes as received from the source.  
  
### _class_ TIPCommon.data_models.BaseAlert

_class_ `TIPCommon.data_models.BaseAlert(raw_data, alert_id)`

Bases: **object**

**BaseAlert** is a foundational model representing a generic security alert. It provides a standardized structure for storing raw telemetry alongside a unique platform identifier.

#### Methods

The following method allows for the serialization of the alert into a standard format.

Methods  
---  
`to_json()` |  `to_json() → dict[str, Any]` Converts the alert into a JSON-serializable dictionary as returned by `json.loads()`.  
  
#### Attributes

The following table highlights the core data points managed by this model.

Attributes  
---  
`raw_data` |  `dict[str, Any]` The raw data payload associated with the alert.  
`alert_id` |  `Any` The unique identifier assigned to the alert.  
  
#### Example

The following example demonstrates how to initialize a `BaseAlert` and access its raw data and serialized output.
    
    
    >>> from data_models import BaseAlert
    >>> alert = BaseAlert({'foo': 'bar'}, 100)
    >>> alert.raw_data
    {'foo': 'bar'}
    >>> alert.alert_id
    100
    >>> alert.to_json()
    {'foo': 'bar'}
    

### _class_ TIPCommon.data_models.BaseDataModel

_class_ `TIPCommon.data_models.BaseDataModel(raw_data)`

Bases: **object**

**BaseDataModel** acts as the parent class for various data structures within the library, ensuring consistent handling of raw input data and serialization.

#### Methods

The following method ensures that raw data is retrieved in a format compatible with JSON operations.

Methods  
---  
`to_json()` |  `to_json() → dict[str, Any]` Serializes the raw data stored in the model into a dictionary format.  
  
#### Attributes

The following table describes the primary data storage for the base model.

Attributes  
---  
`raw_data` |  `dict[str, Any]` The original raw data payload used to initialize the model.  
  
#### Example

The following example shows the basic initialization of the data model and the use of the serialization method.
    
    
    >>> from data_models import BaseDataModel
    >>> data = BaseDataModel({'foo': 'bar'})
    >>> data.raw_data
    {'foo': 'bar'}
    >>> data.to_json()
    {'foo': 'bar'}
    

### _class_ TIPCommon.data_models.CaseDataStatus

_class_ `TIPCommon.data_models.CaseDataStatus(value)`

Bases: **Enum**

**CaseDataStatus** defines the supported operational statuses for cases within the platform, ranging from initial ingestion to final closure or merging.

##### Constants

The following constants represent the specific status indicators assigned to case data.

Constants  
---  
`NEW` | `0`  
`OPENED` | `1`  
`CLOSED` | `2`  
`ALL` | `3`  
`MERGED` | `4`  
`CREATION_PENDING` | `5`  
  
### _class_ TIPCommon.data_models.CaseDetails

Bases: **object**

**CaseDetails** provides an extensive view of a security case, including state-checking properties and methods for reconstructing or serializing case data.

#### Methods

The following methods manage the conversion of case details between object instances and structured JSON formats.

Methods  
---  
`from_json()` |  `from_json(case_details_json: MutableMapping[str, Any]) → CaseDetails` A class method that initializes a `CaseDetails` instance from a dictionary of case attributes.  
`to_json()` |  `to_json(include_activities: bool = False) → MutableMapping[str, Any]` Converts the `CaseDetails` object into a JSON-serializable dictionary. Set `include_activities` to `True` to include case activity logs.  
  
#### Attributes

The following properties provide logical indicators regarding the current state of the case.

Attributes  
---  
`is_closed` |  `bool` A boolean property indicating whether the case is in a closed state.  
`is_open` |  `bool` A boolean property indicating whether the case is active or open.  
  
### _class_ TIPCommon.data_models.CaseOverviewInfo

_class_ `TIPCommon.data_models.CaseOverviewInfo(id: 'int', create_time_ms: 'int', update_time_ms: 'int', display_id: 'str', display_name: 'str', alert_count: 'int', stage: 'str', priority: 'CasePriority', important: 'bool', description: 'str | None' = None, type: 'int | None' = None, assignee_full_name: 'str | None' = None, environment_data: 'EnvironmentData | None' = None, status: 'CaseDataStatus | None' = None, score: 'int | None' = None, case_sla: 'CaseSLAInfo | None' = None, alerts_sla: 'CaseSLAInfo | None' = None, incident: 'bool | None' = None, has_suspicious_entity: 'bool | None' = None, workflow_status: 'int | None' = None, tags: 'list[str]' = <factory>, products: 'list[str]' = <factory>, touched: 'bool | None' = None, merged: 'bool | None' = None, has_incident: 'bool | None' = None, alert_names: 'list[str]' = <factory>)`

Bases: **object**

**CaseOverviewInfo** provides a high-level summary of a security case, aggregating metadata, Service Level Agreement (SLA) status, and organizational details used for dashboarding and queue management.

#### Methods

The following method facilitates the reconstruction of case overview objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → CaseOverviewInfo` A class method that initializes a `CaseOverviewInfo` instance from a dictionary of case summary attributes.  
  
#### Attributes

The following table highlights the primary structural attributes, enums, and key operational metrics associated with the case overview.

Attributes  
---  
`priority` |  `CasePriority` The severity level assigned to the case.  
`status` |  `CaseDataStatus | None` The current operational status of the case data.  
`workflow_status` |  `int | None` The current step or state within the platform's automated workflow engine.  
`score` |  `int | None` The calculated risk or importance score assigned to the case.  
`case_sla` |  `CaseSLAInfo | None` SLA tracking information specifically for the case resolution lifecycle.  
`alerts_sla` |  `CaseSLAInfo | None` SLA tracking information for the individual alerts contained within the case.  
`environment_data` |  `EnvironmentData | None` Metadata regarding the specific organizational environment where the case originated.  
`tags` |  `list[str]` A list of user-defined or system-generated labels associated with the case.  
  
### _class_ TIPCommon.data_models.CasePriority

_class_ `TIPCommon.data_models.CasePriority(value)`

Bases: **Enum**

**CasePriority** defines the standardized integer-based severity levels used to categorize and prioritize cases within the platform.

##### Constants

The following constants represent the specific priority values assigned to cases.

Constants  
---  
`CRITICAL` | `100`  
`HIGH` | `80`  
`MEDIUM` | `60`  
`LOW` | `40`  
`UNCHANGED` | `0`  
`INFORMATIVE` | `-1`  
  
### _class_ TIPCommon.data_models.CaseSLAInfo

_class_ `TIPCommon.data_models.CaseSLAInfo(expiration_time_ms: int | None = None, critical_expiration_time_ms: int | None = None, expiration_status: int | None = None, last_pause_remaining_time_ms: int | None = None)`

Bases: **object**

**CaseSLAInfo** encapsulates Service Level Agreement (SLA) tracking data, providing timestamps for expiration and status indicators to ensure timely incident response.

#### Methods

The following method allows for the creation of SLA info objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → CaseSLAInfo` A class method that initializes a `CaseSLAInfo` instance from a dictionary of SLA attributes.  
  
#### Attributes

The following table highlights the primary timing and status attributes used to monitor case deadlines.

Attributes  
---  
`expiration_time_ms` |  `int | None` The Unix timestamp (in milliseconds) when the standard SLA is set to expire.  
`critical_expiration_time_ms` |  `int | None` The Unix timestamp (in milliseconds) when the critical SLA threshold is reached.  
`expiration_status` |  `int | None` An integer indicator representing the current status of the SLA.  
`last_pause_remaining_time_ms` |  `int | None` The amount of time remaining on the SLA clock at the moment it was last paused.  
  
### _class_ TIPCommon.data_models.CaseWallAttachment

_class_ `TIPCommon.data_models.CaseWallAttachment(name, file_type, base64_blob, is_important, case_id=None, description=None)`

Bases: **object**

**CaseWallAttachment** represents a file or data object attached to a case's evidence wall, including the raw content in base64 format and associated metadata.

#### Attributes

The following table highlights the primary properties and content data associated with the attachment.

Attributes  
---  
`name` |  `str` The filename or display name of the attachment.  
`file_type` |  `str` The MIME type or file extension indicating the format of the attached data.  
`base64_blob` |  `str` The actual content of the file, encoded as a base64 string.  
`is_important` |  `bool` A flag indicating if the attachment is marked as critical evidence for the investigation.  
  
### _class_ TIPCommon.data_models.ConnectorCard

_class_ `TIPCommon.data_models.ConnectorCard(integration, display_name, identifier, is_enabled, is_remote, status)`

Bases: **object**

**ConnectorCard** provides a summary of a specific connector's configuration and

current operational state within the platform.

#### Methods

The following method facilitates the creation of connector card instances from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(connector_card_json: MutableMapping[str, Any]) → ConnectorCard` A class method that initializes a `ConnectorCard` instance from a dictionary of connector attributes.  
  
#### Attributes

The following table highlights the operational status and identification properties of the connector.

Attributes  
---  
`status` |  `ConnectorConnectivityStatusEnum` The current connectivity and health status of the connector.  
`is_enabled` |  `bool` Indicates whether the connector is active and processing data.  
  
### _class_ TIPCommon.data_models.ConnectorConnectivityStatusEnum

_class_ `TIPCommon.data_models.ConnectorConnectivityStatusEnum(value)`

Bases: **Enum**

**ConnectorConnectivityStatusEnum** defines the possible connectivity states for a connector, indicating whether it is successfully communicating with its target integration.

##### Constants

The following constants represent the health status of the connector's connection.

Constants  
---  
`LIVE` | `0`  
`NO_CONNECTIVITY` | `1`  
  
### _class_ TIPCommon.data_models.ConnectorParamTypes

_class_ `TIPCommon.data_models.ConnectorParamTypes(value)`

Bases: **Enum**

**ConnectorParamTypes** defines the supported data types for connector configuration parameters. These types ensure proper validation and UI rendering within the platform's settings.

##### Constants

The following constants represent the specific data types available for parameters.

Constants  
---  
`BOOLEAN` | `0` (boolean toggle)  
`INTEGER` | `1` (numeric integer)  
`STRING` | `2` (standard text string)  
`PASSWORD` | `3` (masked password field)  
`IP` | `4` (IP address)  
`HOST` | `5` (host name)  
`URL` | `6` (URL string)  
`DOMAIN` | `7` (domain name)  
`EMAIL` | `8` (email address)  
`SCRIPT` | `12` (legacy script parameter)  
`NULL` | `-1` (invalid parameter type)  
  
### _class_ TIPCommon.data_models.ConnectorParameter

_class_ `TIPCommon.data_models.ConnectorParameter(raw_param)`

Bases: **Parameter**

**ConnectorParameter** represents an individual configuration setting for a connector. It extends the base parameter model to include specific metadata such as validation types and mandatory requirements.

#### Attributes

The following properties provide access to the configuration details and constraints of the connector parameter.

Attributes  
---  
`name` |  `str` The unique name used to identify the parameter within the connector configuration.  
`value` |  `Any` The current value assigned to the parameter.  
`type` |  `ConnectorParamTypes` The data type of the parameter, used for validation and UI rendering.  
`mode` |  `int` The operational mode or visibility setting of the parameter.  
`is_mandatory` |  `bool` Indicates whether a value must be provided for this parameter before the connector is saved or executed.  
  
#### Example

The following example demonstrates how to initialize a `ConnectorParameter` using a raw dictionary and access its properties.
    
    
    >>> from data_models import ConnectorParameter, ConnectorParamTypes
    >>> p = ConnectorParameter({
        'param_name': 'api_root',
        'type': ConnectorParamTypes.STRING,
        'param_value': '[http://foo.bar](http://foo.bar)',
        'is_mandatory': True,
        'mode': 0
        })
    >>> print(p)
    ConnectorParameter(name='api_root', value='[http://foo.bar](http://foo.bar)', type=2, mode=0, is_mandatory=True)
    

### _class_ TIPCommon.data_models.Container

_class_ `TIPCommon.data_models.Container()`

Bases: **object**

**Container** acts as a generic, dynamic object for storing variables as attributes. It is useful for passing arbitrary data collections between different components of the platform.

#### Example

The following example shows how to initialize a container and dynamically assign and retrieve a variable.
    
    
    >>> from data_models import Container
    >>> container = Container()
    >>> container.one = 1
    >>> container.one
    1
    

### _class_ TIPCommon.data_models.CreateEntity

_class_ `TIPCommon.data_models.CreateEntity(case_id, alert_identifier, entity_type, entity_identifier, entity_to_connect_regex, types_to_connect=None, is_primary_link=False, is_directional=False)`

Bases: **object**

**CreateEntity** encapsulates the instructions needed to create and link a new entity to an existing case and alert. It includes logic for regex-based connection and relationship mapping.

#### Methods

The following method handles the conversion of entity creation instructions into a platform-compatible format.

Methods  
---  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `CreateEntity` object into a JSON-serializable dictionary.  
  
#### Attributes

The following table highlights the primary properties used to define the new entity and its relationships within the platform.

Attributes  
---  
`case_id` |  `int` The unique identifier of the case where the entity will be created.  
`alert_identifier` |  `str` The identifier of the alert to which this entity is associated.  
`entity_type` |  `str` The classification of the entity.  
`entity_identifier` |  `str` The specific value or name identifying the entity.  
`entity_to_connect_regex` |  `str` A regular expression used to identify other entities that to connect to this one.  
`types_to_connect` |  `list[str] | None` A specific list of entity types eligible for connection based on the regex.  
`is_primary_link` |  `bool` Indicates if this connection represents the primary relationship between the entities.  
`is_directional` |  `bool` Determines if the connection has a defined direction (source to target) or is reciprocal.  
  
### _class_ TIPCommon.data_models.CustomField

_class_ `TIPCommon.data_models.CustomField(id, display_name, description, type, scopes)`

Bases: **object**

**CustomField** represents a user-defined data field within the platform. It allows for the extension of standard data models by adding specific metadata tailored to organizational requirements.

#### Methods

The following method allows for the reconstruction of custom field objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → CustomField` A class method that initializes a `CustomField` instance from a dictionary of field attributes.  
  
#### Attributes

The following table highlights the primary properties and scope constraints of the custom field.

Attributes  
---  
`id` |  `int` The unique identifier for the custom field.  
`display_name` |  `str` The human-readable label shown in the platform UI.  
`type` |  `str` The data type of the field.  
`scopes` |  `list[CustomFieldScope]` A list of application areas where this field is available  
  
### _class_ TIPCommon.data_models.CustomFieldScope

_class_ `TIPCommon.data_models.CustomFieldScope(value)`

Bases: **Enum**

**CustomFieldScope** defines the valid targets where a custom field is applied within the platform hierarchy.

#### Methods

The following method provides utility for resolving the path of the scoped object.

Methods  
---  
`build_parent_path()` |  `build_parent_path(identifier: int) → str` Constructs the internal platform path for the specified parent object identifier.  
  
##### Constants

The following constants represent the specific scopes available for custom fields.

Constants  
---  
`ALERTS` | `'Alert'`  
`CASE` | `'Case'`  
  
### _class_ TIPCommon.data_models.CustomFieldValue

_class_ `TIPCommon.data_models.CustomFieldValue(custom_field_id, values, scope, identifier)`

Bases: **object**

**CustomFieldValue** represents the specific data assigned to a custom field instance. It links the field definition to the actual content provided by a user or automated process.

#### Methods

The following method facilitates the reconstruction of custom field values from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → CustomFieldValue` A class method that initializes a `CustomFieldValue` instance from a dictionary of value attributes.  
  
#### Attributes

The following table highlights the primary properties and contextual identifiers for the custom field value.

Attributes  
---  
`custom_field_id` |  `int` The identifier of the `CustomField` definition to which this value belongs.  
`values` |  `list[str]` A list of strings representing the actual data stored in the field.  
`scope` |  `CustomFieldScope` The application area where this specific value is applied.  
`identifier` |  `int` The unique identifier for the specific object that holds this value.  
  
### _class_ TIPCommon.data_models.DataAccessContext

_class_ `TIPCommon.data_models.DataAccessContext(global_access, assigned_scopes)`

Bases: **object**

**DataAccessContext** defines the permissions and visibility constraints for a user or process, determining which data scopes are accessible during execution.

#### Methods

The following methods manage the conversion of access context data between object instances and JSON formats.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → DataAccessContext` A class method that initializes a `DataAccessContext` instance from a dictionary of access properties.  
`to_json()` |  `to_json() → dict` Converts the `DataAccessContext` object into a dictionary format.  
  
#### Attributes

The following table highlights the primary access controls defined within the context.

Attributes  
---  
`global_access` |  `bool` Indicates whether the context allows for unrestricted access across all data scopes.  
`assigned_scopes` |  `list[Any]` A list of specific scopes or organizational units to which access has been explicitly granted.  
  
### _class_ TIPCommon.data_models.DatabaseContextType

_class_ `TIPCommon.data_models.DatabaseContextType(value)`

Bases: **Enum**

**DatabaseContextType** specifies the operational context for database interactions, ensuring that data is persisted or retrieved from the correct logical segment of the platform.

##### Constants

The following constants represent the specific areas of the platform where database operations occur.

Constants  
---  
`GLOBAL` | `0` (global system-wide context)  
`CASE` | `1` (specific security case context)  
`ALERT` | `2` (individual alert context)  
`JOB` | `3` (scheduled job or automation context)  
`CONNECTOR` | `4` (data connector context)  
  
### _class_ TIPCommon.data_models.DynamicParameter

_class_ `TIPCommon.data_models.DynamicParameter(key: str, value: str)`

Bases: **object**

**DynamicParameter** represents a flexible key-value pair used to pass runtime configuration or custom metadata between system components.

#### Methods

The following method handles the reconstruction of dynamic parameters from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → DynamicParameter` A class method that initializes a `DynamicParameter` instance from a dictionary of key and value properties.  
  
#### Attributes

The following table describes the properties of the dynamic parameter.

Attributes  
---  
`key` |  `str` The name or identifier for the parameter.  
`value` |  `str` The data content associated with the key.  
  
### _class_ TIPCommon.data_models.EmailTemplate

_class_ `TIPCommon.data_models.EmailTemplate(template_type, name, content, creator_user_name, for_migration, environments, _id, creation_time_unix_time_in_ms, modification_time_unix_time_in_ms)`

Bases: **object**

**EmailTemplate** represents a standardized communication format used for notifications and reporting within the platform. It encapsulates the message content, metadata, and environmental constraints.

#### Methods

The following methods manage the serialization and reconstruction of email templates.

Methods  
---  
`from_json()` |  `from_json(data: MutableMapping[str, Any]) → EmailTemplate` A class method that initializes an `EmailTemplate` instance from a dictionary containing template data.  
`to_json()` |  `to_json() → dict` Converts the `EmailTemplate` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary properties and structural data of the email template.

Attributes  
---  
`content` |  `str` The body text or HTML structure of the email template.  
`environments` |  `list[str]` A list of organizational environments where this template is available for use.  
`template_type` |  `int | str` The classification or category of the template.  
  
### _class_ TIPCommon.data_models.Entity

_class_ `TIPCommon.data_models.Entity(raw_data, case_id, entity_type, enriched, artifact, vulnerable, suspicious, attacker, pivot, internal, manually_created, fields)`

Bases: **object**

**Entity** represents a specific observable or object of interest within a security case (such as an IP address, file hash, or user). It tracks both the raw telemetry and various boolean "tags" that indicate the entity's role or risk level in the investigation.

#### Methods

The following methods manage the serialization and reconstruction of entity objects.

Methods  
---  
`from_json()` |  `from_json(entity_response: MutableMapping[str, Any]) → Entity` A class method that initializes an `Entity` instance from a dictionary containing entity telemetry and flags.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `Entity` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary classification flags and data structures associated with the entity.

Attributes  
---  
`entity_type` |  `str | None` The category of the entity.  
`suspicious` |  `bool` Indicates if the entity has been flagged as potentially malicious by system logic or external intelligence.  
`vulnerable` |  `bool` Indicates if the entity is known to have existing security vulnerabilities.  
`attacker` |  `bool` Flagged if the entity is identified as the source of malicious activity.  
`internal` |  `bool` Indicates if the entity belongs to the organization's internal network or infrastructure.  
`fields` |  `list[MutableMapping[str, Any]]` A list of additional properties or enriched data points associated with the entity.  
  
### _class_ TIPCommon.data_models.EntityCard

_class_ `TIPCommon.data_models.EntityCard(identifier, entity_type, is_suspicious, linked_entities)`

Bases: **object**

**EntityCard** represents a summarized view of an entity, typically used for UI components. It aggregates the entity's identification, type, and relationships with other entities in a simplified structure.

#### Methods

The following methods manage the serialization and reconstruction of entity cards.

Methods  
---  
`from_json()` |  `from_json(entity_data: MutableMapping[str, Any]) → EntityCard` A class method that initializes an `EntityCard` instance from a dictionary of entity summary data.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `EntityCard` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary properties used for identifying and linking entities within the card.

Attributes  
---  
`identifier` |  `str` The unique value or name that identifies the entity.  
`entity_type` |  `str` The classification category of the entity.  
`is_suspicious` |  `str` A string indicator (often `True` or `False`) representing the suspicious status of the entity.  
`linked_entities` |  `list[str]` A list of identifiers for other entities that are related to this specific entity card.  
  
### _class_ TIPCommon.data_models.EnvironmentData

_class_ `TIPCommon.data_models.EnvironmentData(environment, dynamic_parameters=<factory>, base64_image=None, platform=None)`

Bases: **object**

**EnvironmentData** encapsulates configuration and branding information for a specific organizational environment. This includes environment-specific parameters and visual assets used for multi-tenant or multi-environment deployments.

#### Methods

The following method facilitates the creation of environment data objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → EnvironmentData` A class method that initializes an `EnvironmentData` instance from a dictionary of environmental properties.  
  
#### Attributes

The following table highlights the configuration parameters and branding assets associated with the environment.

Attributes  
---  
`environment` |  `str` The name of the organizational environment.  
`dynamic_parameters` |  `list[DynamicParameter]` A list of custom key-value pairs specific to this environment's configuration.  
`base64_image` |  `str | None` An optional base64-encoded string representing the environment's logo or icon.  
`platform` |  `int | None` An integer identifier representing the specific platform or infrastructure provider.  
  
### _class_ TIPCommon.data_models.EventCard

_class_ `TIPCommon.data_models.EventCard(case_id, alert_identifier, event_id, name, time, product, port, outcome, artifact_entities, fields)`

Bases: **object**

**EventCard** represents a concise, visual-friendly summary of a specific security event. It is designed to surface the most critical telemetry—such as timing, source product, and outcome—for use in investigative dashboards and event queues.

#### Methods

The following methods manage the conversion of event card data between object instances and JSON formats.

Methods  
---  
`from_json()` |  `from_json(event_data: MutableMapping[str, Any]) → EventCard` A class method that initializes an `EventCard` instance from a dictionary of event attributes.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `EventCard` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary telemetry and organizational identifiers stored within the event card.

Attributes  
---  
`event_id` |  `str` The unique identifier for the specific event record.  
`time` |  `int` The Unix timestamp representing when the event occurred.  
`product` |  `str` The security product or tool that generated the event telemetry.  
`outcome` |  `str` The recorded result of the event.  
`artifact_entities` |  `list[MutableMapping[str, Any]]` A list of entities identified within the event telemetry that serve as artifacts for the case.  
`fields` |  `list[MutableMapping[str, Any]]` A collection of additional key-value properties specific to this event's data payload.  
  
### _class_ TIPCommon.data_models.EventPropertyField

_class_ `TIPCommon.data_models.EventPropertyField(order, group_name, is_integration, is_highlight, items)`

Bases: **object**

**EventPropertyField** defines a structured collection of event attributes, organized by priority and grouping. It is used to categorize telemetry data for display, highlighting critical fields for investigative focus.

#### Methods

The following method handles the reconstruction of property field objects from structured JSON data.

Methods  
---  
`from_json()` |  `from_json(event_property_field: MutableMapping[str, Any]) → EventPropertyField` A class method that initializes an `EventPropertyField` instance from a dictionary of field attributes.  
  
#### Attributes

The following table highlights the metadata and content items that define the event property field.

Attributes  
---  
`group_name` |  `str` The name of the logical group to which these fields belong.  
`is_highlight` |  `bool` Indicates if this field should be visually emphasized in the platform UI as a high-priority data point.  
`items` |  `list[FieldItem]` A list of specific data items contained within this property group.  
  
### _class_ TIPCommon.data_models.FieldGroupItem

_class_ `TIPCommon.data_models.FieldGroupItem(original_name, name, value)`

Bases: **object**

**FieldGroupItem** represents a specific data point within a field group, maintaining a mapping between the original source name and the human-readable display name.

#### Methods

The following methods manage the serialization and reconstruction of field group items.

Methods  
---  
`from_json()` |  `from_json(field_group_json: MutableMapping[str, Any]) → FieldGroupItem` A class method that initializes a `FieldGroupItem` instance from a JSON dictionary.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `FieldGroupItem` object into a JSON-serializable dictionary format.  
  
### _class_ TIPCommon.data_models.FieldItem

_class_ `TIPCommon.data_models.FieldItem(original_name, name, value)`

Bases: **object**

**FieldItem** is a base data structure for individual properties, storing the raw key, the mapped label, and the associated value.

#### Methods

Methods  
---  
`from_json()` |  `from_json(field_json: MutableMapping[str, Any]) → FieldItem` A class method that creates a `FieldItem` instance from a dictionary of field properties.  
  
### _class_ TIPCommon.data_models.FieldsGroup

_class_ `TIPCommon.data_models.FieldsGroup(order, group_name, is_integration, is_highlight, hide_options, items)`

Bases: **object**

**FieldsGroup** serves as a container for organizing multiple field items into a logical collection. It is primarily used to control the layout and visibility of data within the platform's user interface.

#### Methods

The following methods manage the conversion of field group data between object instances and structured JSON.

Methods  
---  
`from_json()` |  `from_json(field_group_json: MutableMapping[str, Any]) → FieldsGroup` A class method that initializes a `FieldsGroup` instance from a dictionary of group attributes.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `FieldsGroup` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the properties that define the display behavior and contents of the group.

Attributes  
---  
`group_name` |  `str` The label used to identify the group in the UI.  
`is_highlight` |  `bool` Determines if the group should be visually emphasized.  
`items` |  `list[FieldGroupItem]` A list of specific data points contained within the group.  
  
### _class_ TIPCommon.data_models.GoogleServiceAccount

_class_ `TIPCommon.data_models.GoogleServiceAccount(account_type, project_id, private_key_id, private_key, client_email, client_id, auth_uri, token_uri, auth_provider_x509_url, client_x509_cert_url)`

Bases: **object**

**GoogleServiceAccount** provides a structured representation of Google Cloud service account credentials. It is used to manage authentication details for integrations interacting with Google services.

#### Methods

The following method facilitates the export of credential data into the standard format required by client libraries.

Methods  
---  
`to_dict()` |  `to_dict() → dict[str, str]` Serializes the service account properties into a dictionary compatible with the standard `service-account-file.json` format.  
  
### _class_ TIPCommon.data_models.Insight

_class_ `TIPCommon.data_models.Insight(raw_data)`

Bases: **object**

**Insight** represents a discrete analytical finding or observation generated by the platform or an integration. It encapsulates raw data that provides additional context or recommended actions for a security investigation.

#### Methods

The following methods manage the serialization and reconstruction of insight objects.

Methods  
---  
`from_json()` |  `from_json(insights_response: MutableMapping[str, Any]) → Insight` A class method that creates an `Insight` instance from a dictionary of raw insight telemetry.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Serializes the `Insight` object back into a JSON-compatible dictionary format.  
  
#### Attributes

Attributes  
---  
`raw_data` |  `MutableMapping[str, Any]` The underlying raw data payload containing the specific findings and metrics of the insight.  
  
### _class_ TIPCommon.data_models.InstalledIntegrationInstance

_class_ `TIPCommon.data_models.InstalledIntegrationInstance(instance, identifier, integration_identifier, environment_identifier, instance_name)`

Bases: **object**

**InstalledIntegrationInstance** represents a specific, configured instance of an integration that has been deployed within an environment. It links the general integration definition to its specific environmental deployment and naming.

#### Methods

The following methods manage the conversion of integration instance data between object instances and structured JSON.

Methods  
---  
`from_json()` |  `from_json(integration_env_json: MutableMapping[str, Any]) → InstalledIntegrationInstance` A class method that parses JSON data into an `InstalledIntegrationInstance` object.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Serializes the integration instance data into a JSON-compatible dictionary format.  
  
#### Attributes

The following table highlights the identifiers used to track the integration across different organizational environments.

Attributes  
---  
`instance_name` |  `str` The user-defined name for this specific integration instance.  
`integration_identifier` |  `str` The unique identifier for the parent integration.  
`environment_identifier` |  `str` The identifier for the organizational environment where this instance is installed.  
  
### _class_ TIPCommon.data_models.InternalDomain

_class_ `TIPCommon.data_models.InternalDomain(alias_name, id_, domain_display_name, environments_json, creation_time_unix_time_in_ms, modification_time_unix_time_in_ms)`

Bases: **object**

**InternalDomain** represents a domain identifier that is recognized as part of the organization's internal infrastructure. These records are critical for distinguishing between internal traffic and external threats during security investigations.

#### Methods

The following methods manage the serialization and reconstruction of internal domain records.

Methods  
---  
`from_json()` |  `from_json(json_data: MutableMapping[str, Any]) → InternalDomain` A class method that creates an `InternalDomain` object from a JSON dictionary.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `InternalDomain` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the properties used to identify and categorize internal domains.

Attributes  
---  
`domain_display_name` |  `str` The primary domain name.  
`alias_name` |  `str` An alternative name or label used to identify the domain within the platform.  
`environments_json` |  `str` A JSON-formatted string listing the environments where this domain is considered internal.  
  
### _class_ TIPCommon.data_models.JobParamType

_class_ `TIPCommon.data_models.JobParamType(value)`

Bases: **Enum**

**JobParamType** defines the supported data types for parameters used within scheduled jobs or automation tasks. These types facilitate proper input validation and platform-level handling.

##### Constants

The following constants represent the specific data types available for job parameters.

Constants  
---  
`BOOLEAN` | `0`  
`INTEGER` | `1`  
`STRING` | `2`  
`PASSWORD` | `3`  
`IP` | `4`  
`HOST` | `5`  
`URL` | `6`  
`DOMAIN` | `7`  
`EMAIL` | `8`  
`NULL` | `-1`  
  
### _class_ TIPCommon.data_models.Parameter

_class_ `TIPCommon.data_models.Parameter(raw_param)`

Bases: **object**

**Parameter** serves as the primary base class for all parameter-related models in the library. It provides a consistent interface for handling raw configuration data.

#### Attributes

The following property provides access to the underlying data used to initialize the parameter.

Attributes  
---  
`raw_data` |  `dict[str, Any]` The original dictionary payload containing the parameter's configuration.  
  
#### Example

The following example demonstrates how to initialize the base `Parameter` class and access its raw data.
    
    
    >>> from data_models import Parameter
    >>> p = Parameter({'foo': 'bar'})
    >>> print(p)
    Parameter(raw_data={'foo': 'bar'})
    

### _class_ TIPCommon.data_models.SLA

_class_ `TIPCommon.data_models.SLA(sla_expiration_time, critical_expiration_time, expiration_status, remaining_time_since_last_pause)`

Bases: **object**

**SLA** (Service Level Agreement) encapsulates the timing constraints and status for an alert. It provides high-precision tracking for standard and critical deadlines, including logic for handled pauses.

#### Methods

The following methods manage the conversion of SLA data between object instances and structured JSON.

Methods  
---  
`from_json()` |  `from_json(sla_json: MutableMapping[str, Any]) → SLA` A class method that initializes an `SLA` instance from a JSON dictionary.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `SLA` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the core timing attributes used to track alert expiration.

Attributes  
---  
`sla_expiration_time` |  `int | None` The Unix timestamp representing the standard SLA expiration deadline.  
`critical_expiration_time` |  `int | None` The Unix timestamp representing the critical SLA expiration deadline.  
`expiration_status` |  `int` The current status of the SLA.  
  
### _class_ TIPCommon.data_models.ScriptContext

_class_ `TIPCommon.data_models.ScriptContext(target_entities: 'str' = '', case_id: 'int | str | None' = None, alert_id: 'str' = '', environment: 'str' = '', workflow_id: 'str' = '', workflow_instance_id: 'str | None' = None, parameters: 'SingleJson' = <factory>, integration_identifier: 'str' = '', integration_instance: 'str' = '', action_definition_name: 'str' = '', original_requesting_user: 'str' = '', execution_deadline_unix_time_ms: 'int' = 0, async_polling_interval_in_sec: 'int' = 0, async_total_duration_deadline: 'int' = 0, script_timeout_deadline: 'int' = 0, default_result_value: 'str' = '', use_proxy_settings: 'bool' = False, max_json_result_size: 'int' = 15, vault_settings: 'SiemplifyVault | None' = None, environment_api_key: 'str | None' = None, unique_identifier: 'str' = '', job_api_key: 'str' = '', connector_context: 'ConnectorContext | None' = None)`

Bases: **object**

**ScriptContext** is a comprehensive container that provides the necessary environment, identifiers, and parameters for script execution. It tracks everything from target entities and workflow IDs to security settings like proxy and vault configurations.

#### Methods

The following methods allow for the modification and serialization of the script's execution context.

Methods  
---  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Serializes the `ScriptContext` into a JSON-compatible dictionary format.  
`update()` |  `update(attributes: MutableMapping[str, Any]) → None` Updates the context attributes with values from a provided dictionary.  
  
#### Attributes

Given the extensive nature of the context, the following table highlights the most critical execution and environmental identifiers.

Attributes  
---  
`case_id` |  `int | str | None` The identifier of the case associated with the current script execution.  
`workflow_id` |  `str` The ID of the workflow currently being processed.  
`parameters` |  `SingleJson` A dictionary containing runtime parameters passed to the script.  
`execution_deadline_unix_time_ms` |  `int` The Unix timestamp indicating when the script execution must conclude.  
`vault_settings` |  `SiemplifyVault | None` Configuration settings for accessing sensitive data stored in the platform's vault.  
  
### _class_ TIPCommon.data_models.SmimeEmailConfig

_class_ `TIPCommon.data_models.SmimeEmailConfig(email, private_key_b64, certificate_b64, ca_certificate_b64)`

Bases: **object**

**SmimeEmailConfig** encapsulates the necessary cryptographic assets and the email message required to perform S/MIME operations, such as signing or encryption. It holds the raw email and the base64-encoded keys and certificates.

#### Attributes

The following table describes the cryptographic components managed by this configuration model.

Attributes  
---  
`email` |  `email.message.Message` The standard Python email message object to process.  
`private_key_b64` |  `str` The base64-encoded private key used for signing or decryption.  
`certificate_b64` |  `str` The base64-encoded public certificate associated with the private key.  
`ca_certificate_b64` |  `str` The base64-encoded Certificate Authority (CA) certificate used to verify the chain of trust.  
  
### _class_ TIPCommon.data_models.SmimeType

_class_ `TIPCommon.data_models.SmimeType(value)`

Bases: **Enum**

**SmimeType** defines the operational mode for S/MIME processing, distinguishing between securing the content via encryption or validating the sender using a digital signature.

##### Constants

The following constants represent the supported S/MIME message types.

Constants  
---  
`SIGNED` | `'signed'` (The message is digitally signed to ensure authenticity)  
`ENCRYPTED` | `'encrypted'` (The message body is encrypted for confidentiality)  
  
### _class_ TIPCommon.data_models.TypedContainer

_class_ `TIPCommon.data_models.TypedContainer()`

Bases: **Generic[T]**

**TypedContainer** is a generic wrapper designed to hold data of a specific type. It enhances developer productivity by providing type hints and intellisense, ensuring that the stored object is treated correctly by IDEs and static analysis tools.

### _class_ TIPCommon.data_models.UserDetails

_class_ `TIPCommon.data_models.UserDetails(id_: int, creation_time_unix_time_in_ms: int, modification_time_unix_time_in_ms: int, permission_group: str, permission_groups: list[str], soc_roles: list[str], is_disabled: bool, login_identifier: str, first_name: str, last_name: str, permission_type: int, role: int, soc_role_id: int, soc_role_ids: list[int], email: str, user_name: str, user_type: int, identity_provider: int, provider_name: str, advanced_reports_access: int, account_state: int, last_login_time: int, previous_login_time: int, last_password_change_time: int, last_password_change_notification_time: int, login_wrong_password_count: int, is_deleted: bool, deletion_time_unix_time_in_ms: int, environments: list[str], allowed_platforms: list[int], data_access_context: [DataAccessContext](#TIPCommon.data_models.DataAccessContext), soc_role: str | None, image_base64: str | None)`

Bases: **object**

**UserDetails** provides an exhaustive profile of a platform user, encompassing authentication metadata, organizational roles, and granular data access permissions. It is essential for managing user sessions and enforcing role-based access control (RBAC).

#### Methods

The following methods facilitate the reconstruction and serialization of user profile data.

Methods  
---  
`from_json()` |  `from_json(user_details_json: MutableMapping[str, Any]) → UserDetails` A class method that initializes a `UserDetails` instance from a JSON dictionary of user attributes.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Converts the `UserDetails` object into a JSON-serializable dictionary format.  
  
#### Attributes

The following table highlights the primary identification and permission structures for the user.

Attributes  
---  
`user_name` |  `str` The unique system username used for login and identification.  
`soc_roles` |  `list[str]` A list of SOC roles assigned to the user, defining their operational permissions.  
`data_access_context` |  `DataAccessContext` The context defining which data scopes and organizational units the user is permitted to access.  
`is_disabled` |  `bool` A boolean flag indicating whether the user account is currently restricted from logging in.  
  
### _class_ TIPCommon.data_models.UserProfileCard

_class_ `TIPCommon.data_models.UserProfileCard(raw_data, first_name, last_name, user_name, account_state)`

Bases: **object**

**UserProfileCard** provides a lightweight summary of a user's profile, intended for display in UI components like headers or contact cards where the full details are not required.

#### Methods

Methods  
---  
`from_json()` |  `from_json(user_profile_card_response: dict) → UserProfileCard` A class method that creates a `UserProfileCard` instance from a dictionary of basic profile attributes.  
  
### _class_ TIPCommon.data_models.WallData

_class_ `TIPCommon.data_models.WallData(raw_data, case_id, activity_kind, activity_data_json, favorite)`

Bases: **object**

**WallData** represents an entry on a case's "Wall" or timeline. This model tracks activity logs, notes, and system actions that occur during the lifecycle of an investigation.

#### Methods

Methods  
---  
`from_json()` |  `from_json(data: MutableMapping[str, Any]) → WallData` A class method that initializes a `WallData` instance from a JSON dictionary of wall activity.  
`to_json()` |  `to_json() → MutableMapping[str, Any]` Serializes the `WallData` object back into a JSON-compatible dictionary format.  
  
#### Attributes

Attributes  
---  
`activity_kind` |  `str | int | None` The category of the activity.  
`activity_data_json` |  `str | None` A JSON-formatted string containing the specific details or payload of the activity.  
`favorite` |  `bool` Indicates if the activity entry has been pinned or marked as a favorite for quick reference.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
