---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-base/
title: TIPCommon.base \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:05.687369+00:00
---

# TIPCommon.base  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-base/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.base

### TIPCommon.base.action.action_parser.parse_case_attachment

`TIPCommon.base.action.action_parser.parse_case_attachment(attachment: MutableMapping[str, Any]) → CaseAttachment`

Parses a JSON attachment and returns a `CaseAttachment` object.

#### Parameters

Parameters  
---  
`attachment` | A response JSON object representing the attachment.  
  
#### Returns

The parsed `CaseAttachment` object.

#### Return type

`CaseAttachment`

### TIPCommon.base.action.action_parser.parse_case_comment

`TIPCommon.base.action.action_parser.parse_case_comment(comment: MutableMapping[str, Any]) → CaseComment`

Parses a JSON comment and returns a `CaseComment` object.

#### Parameters

Parameters  
---  
`comment` | A response JSON object representing the comment.  
  
#### Returns

The parsed `CaseComment` object.

#### Return type

`CaseComment`

## _class_ TIPCommon.base.action.base_action.Action

_class_ `TIPCommon.base.action.base_action.Action(name: str)`

Bases: **ABC** , **Generic[ApiClient]**

A unified generic infrastructure implementation for the Google SecOps action development.

The **Action** base class provides template abstract methods to override in the inherited action classes, generic properties, and general flows as methods that are executed when calling the action's run method.

**Warning:** This class is not supported with Python 2.

#### Parameters

Parameters  
---  
`name` | `str` The action's script name.  
  
### Attributes

Attributes  
---  
`_soar_action` | The `SiemplifyAction` SDK object. Type: `SiemplifyAction`  
`_api_client` | The API client of the integration. Type: `Apiable`  
`_name` | The name of the script using this action. Type: `str`  
`_action_start_time` | The action start time. Type: `int`  
`_logger` | The logger object used for logging in actions. Type: `SiemplifyLogger`  
`_params` | The parameter container for this action. Type: `[Container](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module#data-models-container)`  
`global_context` | A dictionary to store the context, if needed. Type: `dict`  
`_entity_types` | The entity types supported by the action. Type: `list[EntityTypesEnum]`  
`_entities_to_update` | The entities to update when the action ends. Type: `list[Entity]`  
`json_results` | The action's JSON results. Type: `JSON`  
`_attachments` | The case result attachments to add. Type: `list[Attachment]`  
`_contents` | The case result contents to add. Type: `list[Content]`  
`_data_tables` | The case result data tables to add. Type: `list[DataTable]`  
`_html_reports` | The case result HTML reports to add. Type: `list[HTMLReport]`  
`_links` | The case result links to add. Type: `list[Link]`  
`_entity_insights` | The case entity insights to add. Type: `list[EntityInsight]`  
`_case_insights` | The case insights to add. Type: `list[CaseInsight]`  
`_execution_state` | The action's final execution state. Type: `ExecutionState`  
`_result_value` | The action final result value. Type: `bool`  
`_output_message` | The action's output message when it succeeds. Type: `str`  
`_error_output_message` | The action's output message when it fails. Type: `str`  
  
### Methods

`- run()` | Runs the action execution.  
---|---  
`- _get_adjusted_json_results()` | Adjusts the JSON result to a particular structure.  
  
### Abstract methods

Abstract methods  
---  
`_validate_params()` | Validates the parameters for this action.  
`_init_managers()` | Initializes and returns a manager object.  
`_perform_action()` | Performs the action's main logic.  
  
### Additional methods

These are methods that are called during the action execution and affect the alerts processing phase but are not mandatory to override.

  * `_get_entity_types()`
  * `_finalize_action_on_success()`
  * `_finalize_action_on_failure()`
  * `_on_entity_failure()`
  * `_handle_timeout()`
  * `_extract_action_parameters()`
  * `_finalize()`



### SDK wrapper methods

  * `_add_attachment_to_current_case()`
  * `_get_current_case_attachments()`
  * `_add_comment_to_case()`
  * `_get_current_case_comments()`
  * `_assign_case_to_user()`
  * `_add_tag_to_case()`
  * `_attach_playbook_to_current_alert()`
  * `_get_similar_cases_to_current_case()`
  * `_get_alerts_ticket_ids_from_cases_closed_since_timestamp()`
  * `_change_current_case_stage()`
  * `_change_current_case_priority()`
  * `_close_current_case()`
  * `_close_alert()`
  * `_escalate_case()`
  * `_mark_case_as_important()`
  * `_raise_incident()`
  * `_add_entity_to_case()`
  * `_update_alerts_additional_data()`
  * `_get_current_integration_configuration()`
  * `_any_alert_entities_in_custom_list()`
  * `_add_alert_entities_to_custom_list()`
  * `_remove_alert_entities_from_custom_list()`



#### Example
    
    
    from TIPCommon.base.actions.action_base import Action
    from TIPCommon.validation import ParameterValidator
    
    SOME_ACTION_SCRIPT_NAME = 'Some Integration - Some Action'
    
    class SomeAction(Action):
    
        def _validate_params(self) -> None:
            validator = ParameterValidator(self.soar_action)
            ...  # validation logic
    
        def _perform_action(self, entity: Entity) -> None:
            try:
                self.logger.info('Querying Api client')
                data = self.api_client.do_something(
                    param=self.params.query,
                    entity=entity.original_identifier
                )
    
                ...  # Some logic to process the data
    
            except SomeCustomException as err:
                self.error_output_message = (
                    "Action wasn't able to successfully do its thing."
    
                )
                raise err from err
    
    
    def main() -> None:
        SomeAction(SEARCH_GRAPHS_SCRIPT_NAME).run()
    
    
    if __name__ == '__main__':
        main()
    

### _property_ action_start_time

`property action_start_time: int`

Returns an `int` representing the action starting time in Unix.

### _property_ api_client

`propertyapi_client: ApiClient | Collection[ApiClient] | Type[Tuple[ApiClient, ...]] | None`

Returns an Apiable object.

### _property_ attachments

`property attachments: list[Attachment]`

All the attachments in the list are sent to the case result by default.

Returns a list of `Attachment` objects representing the insights for this case.

### _property_ case_insights

`property case_insights: list[CaseInsight] `

All the case insights in the list are sent to the case result by default.

Returns a list of `CaseInsight` objects representing the insights for this case.

### _property_ contents

`property contents: list[Content]`

All list contents are sent to the case result by default.

Returns a list of Content objects representing the insights for this case.

### _property_ data_tables

`property data_tables: list[DataTable]`

By default, all data tables in the list are sent to the case result.

Returns a list of DataTable objects representing the insights for this case.

### _property_ entities_to_update

`property entities_to_update: list[DomainEntityInfo]`

All entities in the list are sent to the platform for updating.

Returns a list of `Entity` objects representing the entities that should be updated in the case.

### _property_ entity_insights

`property entity_insights: list[EntityInsight]`

All entity insights in the list are sent to the case result by default.

Returns a list of `EntityInsight` objects representing the insights for this case.

### _property_ entity_types

`property entity_types: list[EntityTypesEnum]`

If the action works with entities, it only processes entities whose type is in the `entity_types` list. Otherwise, the action skips the entity.

Returns a list of `EntityTypesEnum` objects representing entity types the action can process.

### _property_ error_output_message

`property error_output_message: str`

The action output message in case of a failed run.

An output message that should appear in case of a failure during the action runtime. Default value is `Action``SCRIPT_NAME``failed`.

### _property_ execution_state

`property execution_state: ExecutionState `

The action's execution state—a status indicator represented by an integer to pass back to the platform.

Possible statuses are as follows:

  * `ExecutionState.COMPLETED = 0`
  * `ExecutionState.IN_PROGRESS = 1`
  * `ExecutionState.FAILED = 2`
  * `ExecutionState.TIMED_OUT = 3`



Returns the `ExecutionState` object representing the current execution state.

### _property_ html_reports

`property html_reports: list[HTMLReport] `

All the HTML reports in the list will be sent to the case result by default.

Returns a list of `HTMLReport` objects representing the insights for this case.

### _property_ is_first_run

`property is_first_run: bool`

Indicates whether this is the first run.

Returns:

`True` if this is the first run, `False` otherwise.

### _property_ json_results

`property json_results: Dict[str, Any] | List[Dict[str, Any]]`

Returns the action's JSON result to be sent to the case wall.

### _property_ links

`property links: list[Link]`

All the links in the list will be sent to the case result by default.

Returns a list of `Link` objects representing the insights for this case.

### _property_ logger

`property logger: NewLineLogger`

Returns the `NewLineLogger` object for actions.

### _property_ name

`property name: str`

### _property_ output_message

`property output_message: str`

The action's output message in case of a successful run.

The output message that summarizes the result of the action.

### _property_ params

`property params: [[Container](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon/tc-data-models-module#data-models-container)] `

Returns a `Container` object that describes the action's parameters, with each parameter exposed as a snake_case attribute.

### _property_ result_value

`property result_value: bool`

The action's result value to be passed back to the platform.

Possible values:

  * `True`: Action Succeeded
  * `False`: Action Failed



### _property_ soar_action

`property soar_action: SiemplifyAction`

Returns the SDK `SiemplifyAction` object.

## _class_ TIPCommon.base.action.base_enrich_action.EnrichAction

_class_ `TIPCommon.base.action.base_enrich_action.EnrichAction(name: str)`

Bases: **Action**

A class that represents an entity enrichment action.

This class inherits from the `TIPCommon.base.actions.base_action::Action` class.

#### Parameters

Parameters  
---  
`name` | `str`The name of the action.  
  
### Attributes

Attributes  
---  
`enrichment_data` | This attribute holds the enrichment data for the current entity in each of the entity iterations. At the end of each iteration, the entity's `additional_properties` attribute is updated with `self.enrichment_data`, meaning that this value is set every time with the new value. Type: `dict`  
`entity_results` | Entity results included in the JSON output for this object. Type: Any  
`global_context` | A dictionary to store the context if needed. Type: `dict`  
  
### Abstract methods

Abstract methods  
---  
`_get_entity_types()` | Gets the type of entities the action runs on.  
`_perform_enrich_action()` | Perform the main enrichment logic on an entity.  
  
### Private methods

Private methods  
---  
`_perform_action()` | This method combines the other abstract methods with more OOTB enrichment logic and passes it to the parent class to use in the `start()` method. **Warning:** Don't override this method.  
  
## _class_ TIPCommon.base.action.data_models.ActionParamType

_class_ `TIPCommon.base.action.data_models.ActionParamType(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `BOOLEAN = 1`

  * `CASE_PRIORITIES = 7`

  * `CLOSE_CASE_REASONS = 5`

  * `CLOSE_ROOT_CAUSE = 6`

  * `CODE = 20`

  * `CONTENT = 11`

  * `DDL = 15`

  * `EMAIL_CONTENT = 10`

  * `ENTITY_TYPE = 13`

  * `MULTI_VALUES = 14`

  * `NULL = -1`

  * `PASSWORD = 12`

  * `PLAYBOOK_NAME = 2`

  * `STAGE = 4`

  * `STRING = 0`

  * `USER = 3`




## _class_ TIPCommon.base.action.data_models.Attachment

_class_ `TIPCommon.base.action.data_models.Attachment(filename: str, file_contents: bytes, title: str = 'Script Result Attachment', additional_data: dict | None = None)`

Bases: **object**

An action script-result attachment.

This class is immutable: once created, its attributes cannot be modified. It supports hashing (for example, use in sets or as dictionary keys) and equality comparison using the `==` operator.

### Attributes

Attributes  
---  
`title` | The title of the attachment.Type: `str | None`  
`filename` | The filename of the attachment.Type: `str`  
`file_contents` | The content of the attachment file.Type: `bytes`  
`additional_data` | Additional data.Type: `dict | None`  
  
## _class_ TIPCommon.base.action.data_models.CaseAttachment

_class_ `TIPCommon.base.action.data_models.CaseAttachment(attachment_id: int, attachment_type: str, description: str, is_favorite: bool)`

Bases: **object**

A case attachment.

This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`attachment_id` | `int`The attachment ID.  
`attachment_type` | `str`The type of the attachment.  
`description` | `str`The description of the attachment.  
`is_favorite` | `bool`Indicates whether the attachment is marked as favorite.  
  
## _class_ TIPCommon.base.action.data_models.CaseComment

_class_ `TIPCommon.base.action.data_models.CaseComment(comment: str, creator_user_id: str, comment_id: int, comment_type: int, case_id: int, is_favorite: bool, modification_time_unix_time_in_ms: int, creation_time_unix_time_in_ms: int, alert_identifier: str, creator_full_name: str | None = None, is_deleted: bool | None = None, last_editor: str | None = None, last_editor_full_name: str | None = None, modification_time_unix_time_in_ms_for_client: int | None = None, comment_for_client: str | None = None)`

Bases: **object**

A case comment.

This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`comment` | `str`The comment.  
`comment_for_client` | `str | None`The comment for the client.  
`modification_time_unix_time_in_ms_for_client` | `int` The modification time for the `comment_for_client`.  
`last_editor` | `str` The ID of the last editor, such as _77bdb7a4-8484-481d-9482-2449e33f9518_.  
`last_editor_full_name` | `str` The full name of the last editor user, such as _admin admin_.  
`is_deleted` | `bool` Indicates whether the comment is already deleted.  
`creator_user_id` | `str` The creator user ID, such as _77bdb7a4-8484-481d-9482-2449e33f9518_.   
`creator_full_name` | `str` The creator's full name, such as _System_.  
`comment_id` | `int`The ID of the comment.  
`comment_type` | `int`The type of the comment.  
`case_id` | `int`The ID of the case.  
`is_favorite` | `bool` Indicates whether the comment is marked as favorite.  
`modification_time_unix_time_in_ms` | `int` The comment's last modification time in Unix, such as _1686040471269_.  
`creation_time_unix_time_in_ms` | `int` The comment's creation time in Unix, such as _1686040471269_.  
`alert_identifier` | `str`The alert's identifier, such as _SUSPICIOUS PHISHING EMAIL_83765943-9437-4771-96F6-BD0FB291384E_.  
  
## _class_ TIPCommon.base.action.data_models.CaseInsight

_class_ `TIPCommon.base.action.data_models.CaseInsight(triggered_by: str, title: str, content: str, severity: InsightSeverity, insight_type: InsightType, entity_identifier: str = '', additional_data: Any | None = None, additional_data_type: Any | None = None, additional_data_title: str | None = None)`

Bases: **object**

A case insight.

This class is immutable: after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`title` | `str`The title of the insight.  
`triggered_by` | `str`Integration name.  
`content` | `str`The insight message.  
`severity` | `InsightSeverity`Insight severity. Possible values are:

  * `info`
  * `warning`
  * `error`

  
`insight_type` | `InsightType`Insight type. Possible values are:

  * `general`
  * `entity`

  
`entity_identifier` | `str | None`The entity's identifier.  
`additional_data` | `Any | None`Additional data.  
`additional_data_type` | `Any | None`The type of additional data.  
`additional_data_title` | `str | None`The title of additional data.  
  
## _class_ TIPCommon.base.action.data_models.CasePriority

_class_ `TIPCommon.base.action.data_models.CasePriority(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `CRITICAL = 100`

  * `HIGH = 80`

  * `INFORMATIONAL = 0`

  * `LOW = 40`

  * `MEDIUM = 60`




## _class_ TIPCommon.base.action.data_models.CaseStage

_class_ `TIPCommon.base.action.data_models.CaseStage(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `ASSESSMENT = 'Assessment'`

  * `IMPROVEMENT = 'Improvement'`

  * `INCIDENT = 'Incident'`

  * `INVESTIGATION = 'Investigation'`

  * `RESEARCH = 'Research'`

  * `TRIAGE = 'Triage'`




## _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertInconclusiveRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertInconclusiveRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `NO_CLEAR_CONCLUSION = 'No clear conclusion'`



## _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertMaintenanceRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertMaintenanceRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `LAB_TEST = 'Lab test'`

  * `OTHER = 'Other'`

  * `RULE_UNDER_CONSTRUCTION = 'Rule under construction'`




## _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertMaliciousRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertMaliciousRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `EXTERNAL_ATTACK = 'External attack'`

  * `INFRASTRUCTURE_ISSUE = 'Infrastructure issue'`

  * `IRRELEVANT_TCP_UDP_PORT = 'Irrelevant TCP/UDP port'`

  * `MISCONFIGURED_SYSTEM = 'Misconfigured system'`

  * `OTHER = 'Other'`

  * `SIMILAR_CASE_IS_ALREADY_UNDER_INVESTIGATION = 'Similar case is already under investigation'`

  * `SYSTEM_APPLICATION_MALFUNCTION = 'System/application malfunction'`

  * `SYSTEM_CLOCKED_THE_ATTACK = 'System blocked the attack'`

  * `UNFORESEEN_EFFECTS_OF_CHANGE = 'Unforeseen effects of change'`

  * `UNKNOWN = 'Unknown'`




## _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertNotMaliciousRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertNotMaliciousRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `EMPLOYEE_ERROR = 'Employee error'`

  * `HUMAN_ERROR = 'Human error'`

  * `LAB_TEST = 'Lab test'`

  * `LEGIT_ACTION = 'Legit action'`

  * `MISCONFIGURED_SYSTEM = 'Misconfigured system'`

  * `NONE = 'None'`

  * `NORMAL_BEHAVIOR = 'Normal behavior'`

  * `OTHER = 'Other'`

  * `PENETRATION_TEST = 'Penetration test'`

  * `RULE_UNDER_CONSTRUCTION = 'Rule under construction'`

  * `SIMILAR_CASE_IS_ALREADY_UNDER_INVESTIGATION = 'Similar case is already under investigation'`

  * `UNKNOWN = 'Unknown'`

  * `USER_MISTAKE = 'User mistake'`




## _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertReasons

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertReasons(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `INCONCLUSIVE = 3`

  * `MAINTENANCE = 2`

  * `MALICIOUS = 0`

  * `NOT_MALICIOUS = 1`




## _class_ TIPCommon.base.action.data_models.Content

_class_ `TIPCommon.base.action.data_models.Content(content: str, title: str = 'Script Result Content')`

Bases: **object**

An action script-result content.

This class is immutable: after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==`operator.

### Attributes

Attributes  
---  
`title` | `str | None`The title of the content.  
`content` | `str`The content to add to the script results.  
  
## _class_ TIPCommon.base.action.data_models.DataTable

_class_ `TIPCommon.base.action.data_models.DataTable(data_table: list[str], title: str = 'Script Result Data Table')`

Bases: **object**

An action script-result data table.

This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`title` | `str | None`The title of the table.  
`data_table` | `list[str]`A list of CSV rows that construct the table.  
  
## _class_ TIPCommon.base.action.data_models.EntityInsight

_class_ `TIPCommon.base.action.data_models.EntityInsight(entity: DomainEntityInfo, message: str, triggered_by: str | None = None, original_requesting_user: str | None = None)`

Bases: **object**

An entity insight.

This class is immutable: after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`entity` | `Entity`The entity object.  
`message` | `str`The insight's message.  
`triggered_by` | `str | None`The integration's name.  
`original_requesting_user` | `str | None`The original user.  
  
## _class_ TIPCommon.base.action.data_models.EntityTypesEnum

_class_ `TIPCommon.base.action.data_models.EntityTypesEnum(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `ADDRESS = 'ADDRESS'`

  * `ALERT = 'ALERT'`

  * `APPLICATION = 'APPLICATION'`

  * `CHILD_HASH = 'CHILDHASH'`

  * `CHILD_PROCESS = 'CHILDPROCESS'`

  * `CLUSTER = 'CLUSTER'`

  * `CONTAINER = 'CONTAINER'`

  * `CREDIT_CARD = 'CREDITCARD'`

  * `CVE = 'CVE'`

  * `CVE_ID = 'CVEID'`

  * `DATABASE = 'DATABASE'`

  * `DEPLOYMENT = 'DEPLOYMENT'`

  * `DESTINATION_DOMAIN = 'DESTINATIONDOMAIN'`

  * `DOMAIN = 'DOMAIN'`

  * `EMAIL_MESSAGE = 'EMAILSUBJECT'`

  * `EVENT = 'EVENT'`

  * `FILE_HASH = 'FILEHASH'`

  * `FILE_NAME = 'FILENAME'`

  * `GENERIC = 'GENERICENTITY'`

  * `HOST_NAME = 'HOSTNAME'`

  * `IP_SET = 'IPSET'`

  * `MAC_ADDRESS = 'MacAddress'`

  * `PARENT_HASH = 'PARENTHASH'`

  * `PARENT_PROCESS = 'PARENTPROCESS'`

  * `PHONE_NUMBER = 'PHONENUMBER'`

  * `POD = 'POD'`

  * `PROCESS = 'PROCESS'`

  * `SERVICE = 'SERVICE'`

  * `SOURCE_DOMAIN = 'SOURCEDOMAIN'`

  * `THREAT_ACTOR = 'THREATACTOR'`

  * `THREAT_CAMPAIGN = 'THREATCAMPAIGN'`

  * `THREAT_SIGNATURE = 'THREATSIGNATURE'`

  * `URL = 'DestinationURL'`

  * `USB = 'USB'`

  * `USER = 'USERUNIQNAME'`




## _class_ TIPCommon.base.action.data_models.ExecutionState

_class_ `TIPCommon.base.action.data_models.ExecutionState(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `COMPLETED = 0`

  * `FAILED = 2`

  * `IN_PROGRESS = 1`

  * `TIMED_OUT = 3`




## _class_ TIPCommon.base.action.data_models.FullDetailsConfigurationParameter

_class_ `TIPCommon.base.action.data_models.FullDetailsConfigurationParameter(input_dict: dict[str, Any])`

Bases: **object**

A general script parameter object.

### Attributes

Attributes  
---  
`full_dict` | `dict[str, Any]`The original dictionary received from API.  
`id` | `int | None`The ID of the parameter.  
`integration_identifier` | `str`The integration identifier, such as _VirusTotalV3_.  
`creation_time` | `int`The time when the parameter was created.  
`modification_time` | `int`The time when the parameter was last modified.  
`is_mandatory` | `bool`Define whether the parameter is mandatory or not.  
`description` | `str | None`The parameter description.  
`name` | `str`The parameter name.  
`display_name` | `str`The parameter's displayed name.  
`value` | `Any`The default value of the parameter.  
`type` | `IntegrationParamType`The type of the parameter.  
`optional_values` | `list`A DDL of optional values for the type DDL.  
  
## _class_ TIPCommon.base.action.data_models.HTMLReport

_class_ `TIPCommon.base.action.data_models.HTMLReport(report_name: str, report_contents: str, title: str = 'Script Result HTML Report')`

Bases: **object**

An action script-result link.

This class is immutable: after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`title` | `str | None`The title of the link.  
`report_name` | `str`The name of the report.  
`report_contents` | `str`The HTML content of the report.  
  
## _class_ TIPCommon.base.action.data_models.IntegrationParamType

_class_ `TIPCommon.base.action.data_models.IntegrationParamType(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

### Constants

  * `BOOLEAN = 0`

  * `EMAIL = 8`

  * `INTEGER = 1`

  * `IP = 4`

  * `NULL = -1`

  * `PASSWORD = 3`

  * `STRING = 2`




## _class_ TIPCommon.base.action.data_models.Link

_class_ `TIPCommon.base.action.data_models.Link(link: str, title: str = 'Script Result Link')`

Bases: **object**

An action script-result link.

This class is immutable: after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

### Attributes

Attributes  
---  
`title` | `str | None`The title of the link.  
`link` | `str`The link.  
  
## _class_ TIPCommon.base.action.data_models.ScriptParameter

_class_ `TIPCommon.base.action.data_models.ScriptParameter(input_dict: dict[str, Any]`

Bases: **object**

A general script parameter object.

### Attributes

Attributes  
---  
`full_dict` | `dict[str, Any]`Original dictionary received from API.  
`id` | `int | None`ID of the parameter.  
`creation_time` | `int`Time when the parameter was created.  
`modification_time` | `int`Time when the parameter was last modified.  
`custom_action_id` | `int | None`The action ID.  
`is_mandatory` | `bool`Indicates whether the parameter is mandatory or not.  
`default_value` | `Any`The default value of the parameter.This parameter is prioritized over the `value` parameter in playbooks.  
`description` | `str | None`Parameter description.  
`name` | `str | None`Parameter name.  
`value` | `Any`The value of the parameter.This value is prioritized over the `default_value` parameter in manual actions.  
`type` | `ActionParamType`The type of the parameter.  
`optional_values` | `list`DDL of optional values for the type DDL.  
  
## _class_ TIPCommon.base.interfaces.apiable.Apiable

_class_ `TIPCommon.base.interfaces.apiable.Apiable(authenticated_session: AuthenticatedSession, configuration: ApiParams)`

Bases: **ABC** , **Generic[ApiParams]**

An interface for classes that manage API calls to external services.

## _class_ TIPCommon.base.interfaces.authable.Authable

_class_ `TIPCommon.base.interfaces.authable.Authable`

Bases: **ABC** , **Generic[AuthParams]**

An interface for classes that manage authentication with external services.

### Abstract methods

Abstract methods  
---  
`authenticat_session(params: Authparams) → None` | Authenticate the `self.session` attribute of the class using `params`. This method authenticates you to the service that the session interacts with, following the creation of an object using that session.  
  
#### Attributes

Attributes  
---  
`params` | `object`, `dataclass`, `TypedDict`, `namedtuple`, or anything holding all authentication parameters.Authentication parameters.  
  
## _class_ TIPCommon.base.interfaces.logger.Logger

_class_ `TIPCommon.base.interfaces.logger.Logger`

Bases: **ABC**

A logger interface designed for Content Hub scripts, verifying compatibility when the passed logger is replaced or mocked.

### Abstract methods

Abstract methods  
---  
`debug(msg: str, *args, **kwargs) → None` | Logs a debug message.  
`error(error_msg: str, *args, **kwargs) → None` | Logs an error message.  
`exception(ex: Exception, *args, **kwargs) → None` | Logs an exception message.  
`info(msg: str, *args, **kwargs) → None` | Logs an information message.  
`warn(warning_msg: str, *args, **kwargs) → None` | Logs a warning message.  
  
## _class_ TIPCommon.base.interfaces.session.Session

_class_ `TIPCommon.base.interfaces.session.Session`

Bases: **ABC** , **Generic[_R]**

This class manages API sessions using a session object. It supports various session types and mocks with libraries like `requests` or `httpx`.

### Attributes

Attributes  
---  
`headers` | `dict`  
`verify` | `bool`  
  
### Abstract methods

Abstract methods  
---  
`delete(url: str, *args, **kwargs)→ _R` | Deletes a resource from the server.  
`get(url: str, *args, **kwargs)→ _R` | Gets a resource from the server.  
`patch(url: str, *args, **kwargs) → _R` | Patches a resource on the server.  
`post(url: str, *args, **kwargs) → _R` | Posts a resource to the server.  
`put(url: str, *args, **kwargs) → _R` | Puts (updates or creates) a resource on the server.  
`request(method: str, *args, **kwargs) → _R` | Makes a request to the server.  
  
## _class_ TIPCommon.base.job.base_job.Job

_class_ `TIPCommon.base.job.base_job.Job(name: str)`

Bases: **ABC** , **Generic[ApiClient]**

A class that represents a job script in Google SecOps.

### Methods

  * `start(**kwargs) → None`



### _property_ api_client

`property api_client: ApiClient | Collection[ApiClient] | Type[Tuple[ApiClient, ...]] | None`

Provides the API client or clients for interacting with external services.

### _property_ error_msg

`property error_msg: str`

Stores any error message encountered during the job's execution.

### _property_ job_start_time

`property job_start_time: int`

Represents the timestamp when the job started.

### _property_ logger

`property logger: ScriptLogger`

Provides logging functionality for the job script.

### _property_ name

`property name: str`

Holds the name of the job script.

### _property_ params

`property params: Container`

Contains the configuration parameters provided to the job.

### _property_ soar_job

`property soar_job: SiemplifyJob`

Represents the underlying Google SecOps job instance.

## _class_ TIPCommon.base.job.base_job_refresh_token.RefreshTokenRenewalJob

_class_ `TIPCommon.base.job.base_job_refresh_token.RefreshTokenRenewalJob(name: str, integration_identifier: str)`

Bases: **Job** , **Generic[ApiClient]**

This section describes lifecycle methods that influence job processing. Subclasses are not required to override them.

### _property_ api_client

`property api_client: ApiClient | Collection[ApiClient] | Type[Tuple[ApiClient, ...]] | None`

Holds the API client or clients used for external service interactions.

## _class_ TIPCommon.base.job.base_job_refresh_token.SuccessFailureTuple

_class_ `TIPCommon.base.job.base_job_refresh_token.SuccessFailureTuple(success_list, failure_list)`

Bases: **tuple**

### Attributes

Attributes  
---  
`success_list` | Alias for field number 0.  
`failure_list` | Alias for field number 1.  
  
### TIPCommon.base.job.base_job_refresh_token.validate_param_csv_to_multi_value

`TIPCommon.base.job.base_job_refresh_token.validate_param_csv_to_multi_value(param_name: str, param_csv_value: str | None, delimiter: str = ',') → list[str]`

Validates and parses a comma-separated parameter value into a list of unique elements. This function handles single values, quoted strings and mixed formats.

#### Parameters

Parameters  
---  
`param_name` | The parameter key.  
`param_csv_value` | The parameter value provided in the `job` parameter. If `None`, an empty list is returned.  
  
#### Raises

`ValueError` – When the double quotes count is invalid, some values are invalid, or some values have mismatched double quotes.

#### Returns

A list of unique values provided in the job parameter. If no valid values are found, an empty list is returned.

#### Return type

`list[str]`

## _class_ TIPCommon.base.job.data_models.JobParameter

_class_ `TIPCommon.base.job.data_models.JobParameter(input_dict: MutableMapping[str, Any])`

Bases: **object**

A general script parameter object. 

### Attributes

Attributes  
---  
`full_dict` | `dict[str, Any]`The original dict received from the API.  
`id` | `int | None`The ID of the parameter.  
`is_mandatory` | `bool`Define whether the parameter is mandatory or not.Note: This attribute is prioritized over `value` in playbooks.  
`name` | `str | None`The name of the parameter.  
`type` | `ActionParamType`The type of the parameter.  
`value` | `Any`The default value of the parameter.Note: This attribute is prioritized over `default_value` in manual actions.  
  
### _class_ TIPCommon.base.data_models.ActionJsonOutput

_class_ `TIPCommon.base.data_models.ActionJsonOutput(title: 'str' = 'JsonResult', content: 'str' = '', type: 'str | None' = None, is_for_entity: 'bool' = False, json_result: 'JSON | None' = None)`

Bases: **object**

Represents the structured JSON output for an action.

## _class_ TIPCommon.base.data_models.ActionOutput

_class_ `TIPCommon.base.data_models.ActionOutput(output_message: 'str', result_value: 'str | bool', execution_state: 'ExecutionState', json_output: 'ActionJsonOutput | None', debug_output: 'str' = '')`

Bases: **object**

Represents the complete output structure for an action.

## _class_ TIPCommon.base.data_models.ConnectorJsonOutput

_class_ `TIPCommon.base.data_models.ConnectorJsonOutput(alerts: 'list[AlertInfo | CaseInfo]', overflow_alerts: 'list[OverflowAlertDetails]' = <factory>, log_items: 'list' = <factory>, log_rows: 'list[str]' = <factory>, variables: 'dict' = <factory>)`

Bases: **object**

Represents the structured JSON output for a connector.

## _class_ TIPCommon.base.data_models.ConnectorOutput

_class_ `TIPCommon.base.data_models.ConnectorOutput(json_output: 'ConnectorJsonOutput | None', debug_output: 'str' = '')`

Bases: **object**

Represents the complete output structure for a connector.

### TIPCommon.base.data_models.alert_info_from_json

`TIPCommon.base.data_models.alert_info_from_json(json_: MutableMapping[str, Any])→ AlertInfo`

Creates an AlertInfo object from a JSON of attributes.

#### Returns

The created AlertInfo object.

#### Return type

`AlertInfo`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
