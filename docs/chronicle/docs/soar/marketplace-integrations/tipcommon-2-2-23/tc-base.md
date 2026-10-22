---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-base/
title: TIPCommon.base \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:08.414167+00:00
---

# TIPCommon.base  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon-2-2-23/tc-base/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# TIPCommon.base

The **TIPCommon.base** module serves as the foundational technical reference for integration development within Google SecOps, providing core logic for actions, background jobs, and cross-platform data normalization.

## Action data parsing

This section contains utility functions required to parse case data from raw API responses into structured objects for use in automation tasks.

### TIPCommon.base.action.action_parser.parse_case_attachment

`TIPCommon.base.action.action_parser.parse_case_attachment(attachment: MutableMapping[str, Any]) → CaseAttachment`

This utility converts raw JSON attachment data from an API response into a structured `CaseAttachment` object.

#### Parameters

Parameters  
---  
`attachment` | The raw JSON data of the attachment as retrieved from the API response.  
  
### TIPCommon.base.action.action_parser.parse_case_comment

`TIPCommon.base.action.action_parser.parse_case_comment(comment: MutableMapping[str, Any]) → CaseComment`

This function parses raw JSON comment data into a `CaseComment` object for easier access to comment metadata.

#### Parameters

Parameters  
---  
`comment` | The raw JSON data of the comment as retrieved from the API response.  
  
## _class_ TIPCommon.base.action.base_action.Action

_class_ `TIPCommon.base.action.base_action.Action(name: str)`

Bases: `ABC`, `Generic`[`ApiClient`]

The **Action** base class provides a unified infrastructure for automation development, including property management and general execution flows.

**Warning:** This class requires Python 3. Legacy Python 2 environments aren't supported.

#### Parameters

Parameters  
---  
`name` | The identifier for the action's script.  
  
### Attributes

The following attributes manage the internal state of the action and provide access to SDK resources and integration clients.

Attributes  
---  
`_soar_action` |  `SiemplifyAction` The `SiemplifyAction` SDK object.  
`_api_client` |  `Apiable` The API client of the integration.  
`_name` |  `str` The name of the script using this action.  
`_action_start_time` |  `int` The action start time in Unix.  
`_logger` |  `SiemplifyLogger` The logger object used for logging in actions.  
`_params` |  `Container` The parameter container for this action.  
`global_context` |  `dict` A dictionary to store the context, if needed.  
`_entity_types` |  `list[EntityTypesEnum]` The entity types supported by the action.  
`_entities_to_update` |  `list[Entity]` The entities to update when the action ends.  
`json_results` |  `JSON` The action's JSON results.  
`_attachments` |  `list[Attachment]` The case result attachments to add.  
`_contents` |  `list[Content]` The case result contents to add.  
`_data_tables` |  `list[DataTable]` The case result data tables to add.  
`_html_reports` |  `list[HTMLReport]` The case result HTML reports to add.  
`_links` |  `list[Link]` The case result links to add.  
`_markdowns` |  `list[Markdown]` The case result markdowns to add.  
`_entity_insights` |  `list[EntityInsight]` The case entity insights to add.  
`_case_insights` |  `list[CaseInsight]` The case insights to add.  
`_execution_state` |  `ExecutionState` The action's final execution state indicator.  
`_result_value` |  `bool` The action final result value.  
`_output_message` |  `str` The action's output message when it succeeds.  
`_error_output_message` |  `str` The action's output message when it fails.  
  
### Methods

Standard methods used to manage the lifecycle and output formatting of an action script.

`- run()` | Runs the action execution.  
---|---  
`- _get_adjusted_json_results()` | Adjusts the JSON result to a particular structure.  
  
### Abstract methods

Developers must override these methods to define the unique logic for a custom action.

Abstract methods  
---  
`_validate_params()` | Validates the parameters for this action.  
`_init_api_clients()` | Initializes the API clients of the action.  
`_perform_action()` | Performs the action's main logic.  
  
### Additional methods

These optional methods are triggered during specific phases of the action execution lifecycle to handle alerts or clean up resources.

  * `_get_entity_types()`
  * `_finalize_action_on_success()`
  * `_finalize_action_on_failure()`
  * `_on_entity_failure()`
  * `_handle_timeout()`
  * `_extract_action_parameters()`
  * `_finalize()`



### SDK wrapper methods

These methods provide convenient access to the underlying SDK, allowing actions to interact with cases, alerts, and platform configurations.

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



#### Example implementation

The following example demonstrates how to implement a custom action by inheriting from the **Action** base class.
    
    
    from TIPCommon.base.actions.action_base import Action
    from TIPCommon.validation import ParameterValidator
    
    SOME_ACTION_SCRIPT_NAME = 'Some Integration - Some Action'
    
    class SomeAction(Action):
    
     def _validate_params(self) -> None:
     validator = ParameterValidator(self.soar_action)
     ... # validation logic
    
     def _perform_action(self, entity: Entity) -> None:
     try:
     self.logger.info('Querying Api client')
     data = self.api_client.do_something(
     param=self.params.query,
     entity=entity.original_identifier
     )
    
     ... # Some logic to process the data
    
     except SomeCustomException as err:
     self.error_output_message = (
     "Action wasn't able to successfully do its thing."
    
     )
     raise err from err
    
    
    def main() -> None:
     SomeAction(SEARCH_GRAPHS_SCRIPT_NAME).run()
    
    
    if __name__ == '__main__':
     main()
    

### Properties

The following properties provide read-only or managed access to action metadata, results, and SDK objects.

#### action_start_time

`property action_start_time: int`

Returns an `int` representing the action's start time in Unix format.

#### api_client

`property api_client: ApiClient | Collection[ApiClient] | Type[Tuple[ApiClient, ...]] | None`

Returns an `Apiable` object representing the API client configured for the integration.

#### attachments

`property attachments: list[Attachment]`

Returns a list of `Attachment` objects representing the case result attachments associated with this action. All attachments in this list are sent to the case result by default.

#### case_insights

`property case_insights: list[CaseInsight]`

Returns a list of `CaseInsight` objects representing high-level findings associated with this action. All case insights in this list are sent to the case result by default.

#### contents

`property contents: list[Content]`

Returns a list of `Content` objects representing text results for the case. All contents in this list are sent to the case result by default.

#### data_tables

`property data_tables: list[DataTable]`

Returns a list of `DataTable` objects representing tabular data insights for the case. All data tables in this list are sent to the case result by default.

#### entities_to_update

`property entities_to_update: list[DomainEntityInfo]`

Returns a list of `Entity` objects to update in the platform once the action concludes.

#### entity_insights

`property entity_insights: list[EntityInsight]`

Returns a list of `EntityInsight` objects representing findings tied to specific entities. All entity insights in this list are sent to the case result by default.

#### entity_types

`property entity_types: list[EntityTypesEnum]`

Returns a list of `EntityTypesEnum` objects representing the entity types the action is designed to process. If an action runs on entities, it only processes types appearing in this list.

#### error_output_message

`property error_output_message: str`

Gets or sets the message displayed in the platform in the event of a failed run. The default value is `Action ACTION_NAME failed`.

#### execution_state

`property execution_state: ExecutionState`

Returns an `ExecutionState` object representing the final processing status indicator. The possible statuses are:

  * `ExecutionState.COMPLETED = 0`
  * `ExecutionState.IN_PROGRESS = 1`
  * `ExecutionState.FAILED = 2`
  * `ExecutionState.TIMED_OUT = 3`



#### global_context

`global_context: dict`

A dictionary used to store and retrieve context information during action execution.

#### html_reports

`property html_reports: list[HTMLReport]`

Returns a list of `HTMLReport` objects representing visual reports for the case result. All HTML reports in this list are sent to the case result by default.

#### is_first_run

`property is_first_run: bool`

Returns `true` if this is the initial execution of the action, or `false` otherwise.

#### json_results

`property json_results: Dict[str, Any] | List[Dict[str, Any]]`

Returns the formatted JSON result to display on the case wall and use in downstream playbook logic.

#### links

`property links: list[Link]`

Returns a list of `Link` objects representing external reference URLs for the case result. All links in this list are sent to the case result by default.

#### logger

`property logger: NewLineLogger`

Returns the `NewLineLogger` instance used for script-specific logging.

#### markdowns

`property markdowns: list[Markdown]`

Returns a list of `Markdown` objects representing formatted text insights. All markdowns in this list are sent to the case result by default.

#### name

`property name: str`

Returns the string name of the action script.

#### output_message

`property output_message: str`

Gets or sets the message displayed in the platform summarizing a successful action run.

#### params

`property params: Container`

Returns a `Container` object describing the action's input parameters, with each parameter exposed as a `snake_case` attribute.

#### result_value

`property result_value: bool`

Gets or sets the success indicator returned to the platform.

  * `True`: The action succeeded.
  * `False`: The action failed.



#### run

`run(**kwargs)`

Standard method to trigger the action execution logic.

#### soar_action

`property soar_action: SiemplifyAction`

Returns the underlying SDK `SiemplifyAction` object used for direct platform interaction.

## _class_ TIPCommon.base.action.base_enrich_action.EnrichAction

_class_ `TIPCommon.base.action.base_enrich_action.EnrichAction(name: str)`

Bases: **Action**

**EnrichAction** is a specialized base class designed for actions that update entity properties with external data.

#### Parameters

The following parameter is required to initialize the enrichment action and register it within the platform.

Parameters  
---  
`name` | The unique identifier for the enrichment action script.  
  
### Attributes

The following attributes manage the data used during entity iterations and define the content included in the action's output results.

Attributes  
---  
`enrichment_data` |  `dict` The enrichment data for the current entity in each of the entity iterations. At the end of each iteration, the entity's `additional_properties` attribute is updated with `self.enrichment_data`, meaning that this value is set every time with the new value.  
`entity_results` |  `Any` Entity results included in the JSON output for this object.  
`global_context` |  `dict` A dictionary used to store and share context data across different phases of the enrichment action execution.  
  
### Abstract methods

The following abstract methods must be implemented in subclasses to define the specific entity types and enrichment logic for the action.

Abstract methods  
---  
`_get_entity_types()` | Gets the type of entities the action runs on.  
`_perform_enrich_action()` | Perform the main enrichment logic on an entity.  
  
### Private methods

These internal methods handle the orchestration of enrichment logic and shouldn't be modified.

Private methods  
---  
`_perform_action()` |  This method combines the other abstract methods with more OOTB enrichment logic and passes it to the parent class to use in the `start()` method. **Warning:** Don't override this method.   
  
## Data Models module

This module provides structured definitions for cross-integration objects, enums, and constants.

### _class_ TIPCommon.base.action.data_models.ActionParamType

_class_ `TIPCommon.base.action.data_models.ActionParamType(value)`

Bases: **Enum**

**ActionParamType** defines the supported UI data types for action script parameters.

#### Constants

Constant| Value  
---|---  
`BOOLEAN`| 1  
`CASE_PRIORITIES`| 7  
`CLOSE_CASE_REASONS`| 5  
`CLOSE_ROOT_CAUSE`| 6  
`CODE`| 20  
`CONTENT`| 11  
`DDL`| 15  
`EMAIL_CONTENT`| 10  
`ENTITY_TYPE`| 13  
`MULTI_VALUES`| 14  
`NULL`| -1  
`PASSWORD`| 12  
`PLAYBOOK_NAME`| 2  
`STAGE`| 4  
`STRING`| 0  
`USER`| 3  
  
###  _class_ TIPCommon.base.action.data_models.Attachment

_class_ `TIPCommon.base.action.data_models.Attachment(filename: str, file_contents: bytes, title: str = 'Script Result Attachment', additional_data: dict | None = None)`

Bases: **object**

This model represents a script-result attachment to upload to the case wall.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Parameters

The following parameters are required to initialize an attachment object, defining its metadata and the binary data to upload to the case.

Parameters  
---  
`filename` | The name of the file to create within the case results.  
`file_contents` | The raw binary data representing the content of the file.  
`title` | The display title for the attachment as it appears in the platform UI; defaults to `'Script Result Attachment'`.  
  
#### Attributes

The following attributes define the metadata and binary content of the file attachment generated by the action script.

Attributes  
---  
`title` |  `str | None` The title of the attachment displayed in the platform interface.  
`filename` |  `str` The specific name of the file to create.  
`file_contents` |  `bytes` The raw binary content of the attachment file.  
`additional_data` |  `dict | None` A dictionary containing supplementary data associated with the attachment.  
  
### _class_ TIPCommon.base.action.data_models.CaseAttachment

_class_ `TIPCommon.base.action.data_models.CaseAttachment(attachment_id: int, attachment_type: str, description: str, is_favorite: bool)`

Bases: **object**

This class represents an immutable attachment associated with a case.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes represent the specific metadata of an attachment that has already been associated with a case within the platform.

Attributes  
---  
`attachment_id` |  `int` The unique platform-assigned identifier for the attachment.  
`attachment_type` |  `str` The classification or MIME type of the attachment (for example, `txt`, `csv`, or `json`).  
`description` |  `str` A user-defined or system-generated description of the attachment's content.  
`is_favorite` |  `bool` Indicates whether the attachment has been marked as a favorite for quick access on the case wall.  
  
### _class_ TIPCommon.base.action.data_models.CaseComment

_class_ `TIPCommon.base.action.data_models.CaseComment(comment: str, creator_user_id: str, comment_id: int, comment_type: int, case_id: int, is_favorite: bool, modification_time_unix_time_in_ms: int, creation_time_unix_time_in_ms: int, alert_identifier: str, creator_full_name: str | None = None, is_deleted: bool | None = None, last_editor: str | None = None, last_editor_full_name: str | None = None, modification_time_unix_time_in_ms_for_client: int | None = None, comment_for_client: str | None = None)`

Bases: **object**

**CaseComment** represents an immutable record of a comment associated with a case or alert, capturing creator details and audit timestamps.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes define the content and administrative metadata of a case comment.

Attributes  
---  
`comment` |  `str` The primary text content of the comment.  
`comment_for_client` |  `str | None` An optional version of the comment tailored for client visibility.  
`modification_time_unix_time_in_ms_for_client` |  `int` The modification timestamp for the `comment_for_client` in Unix milliseconds.  
`last_editor` |  `str` The ID of the last editor, such as `77bdb7a4-8484-481d-9482-2449e33f9518`.  
`last_editor_full_name` |  `str` The full display name of the user who last edited the comment, such as `admin admin`.  
`is_deleted` |  `bool` Indicates whether the comment has been marked as deleted.  
`creator_user_id` |  `str` The creator user ID, such as `77bdb7a4-8484-481d-9482-2449e33f9518`.  
`creator_full_name` |  `str` The creator's full display name, such as `System`.  
`comment_id` |  `int` The unique platform-assigned integer identifier for the comment.  
`comment_type` |  `int` The type classification of the comment.  
`case_id` |  `int` The ID of the case associated with this comment.  
`is_favorite` |  `bool` Indicates whether the comment is pinned as a favorite.  
`modification_time_unix_time_in_ms` |  `int` The comment's last modification time in Unix milliseconds, such as `1686040471269`.  
`creation_time_unix_time_in_ms` |  `int` The comment's creation time in Unix milliseconds, such as `1686040471269`.  
`alert_identifier` |  `str` The specific identifier of the alert related to the comment, such as `SUSPICIOUS PHISHING EMAIL_83765943-9437-4771-96F6-BD0FB291384E`.  
  
### _class_ TIPCommon.base.action.data_models.CaseInsight

_class_ `TIPCommon.base.action.data_models.CaseInsight(triggered_by: str, title: str, content: str, severity: InsightSeverity, insight_type: InsightType, entity_identifier: str = '', additional_data: Any | None = None, additional_data_type: Any | None = None, additional_data_title: str | None = None)`

Bases: **object**

**CaseInsight** represents an immutable structured finding or alert summary displayed on the case wall.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes manage how insights are categorized and presented to analysts within the platform.

Attributes  
---  
`title` |  `str` The headline displayed for the insight on the case wall.  
`triggered_by` |  `str` The name of the integration or user that generated the insight.  
`content` |  `str` The detailed message body or finding of the insight.  
`severity` |  `InsightSeverity` The urgency level of the insight. The possible values are as follows:
* `info`
* `warning`
* `error`  
`insight_type` |  `InsightType` Categorizes the insight. The possible values are as follows:
* `general`
* `entity`  
`entity_identifier` |  `str | None` The specific identifier for an entity if the insight is entity-focused.  
`additional_data` |  `Any | None` Supplementary data associated with the insight.  
`additional_data_type` |  `Any | None` The data type classification for the `additional_data` attribute.  
`additional_data_title` |  `str | None` The display title for the supplementary data block.  
  
### _class_ TIPCommon.base.action.data_models.CasePriority

_class_ `TIPCommon.base.action.data_models.CasePriority(value)`

Bases: **Enum**

**CasePriority** defines the integer-based severity levels assigned to cases within the platform.

#### Constants

Constant | Value  
---|---  
`CRITICAL`| 100  
`HIGH`| 80  
`INFORMATIONAL`| 0  
`LOW`| 40  
`MEDIUM`| 60  
  
###  _class_ TIPCommon.base.action.data_models.CaseStage

_class_ `TIPCommon.base.action.data_models.CaseStage(value)`

Bases: **Enum**

**CaseStage** specifies the operational phases a case can transition through during its lifecycle.

#### Constants

Constant | Value  
---|---  
`ASSESSMENT`| 'Assessment'  
`IMPROVEMENT`| 'Improvement'  
`INCIDENT`| 'Incident'  
`INVESTIGATION`| 'Investigation'  
`RESEARCH`| 'Research'  
`TRIAGE`| 'Triage'  
  
### _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertInconclusiveRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertInconclusiveRootCauses(value)`

Bases: **Enum**

**CloseCaseOrAlertInconclusiveRootCauses** provides root cause options for scenarios where a definitive determination cannot be made.

#### Constants

Constant | Value  
---|---  
`NO_CLEAR_CONCLUSION`| 'No clear conclusion'  
  
### _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertMaintenanceRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertMaintenanceRootCauses(value)`

Bases: **Enum**

**CloseCaseOrAlertMaintenanceRootCauses** defines root causes related to scheduled testing, system maintenance, or rule development.

#### Constants

Constant | Value  
---|---  
`LAB_TEST`| 'Lab test'  
`OTHER`| 'Other'  
`RULE_UNDER_CONSTRUCTION`| 'Rule under construction'  
  
### _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertMaliciousRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertMaliciousRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

**CloseCaseOrAlertMaliciousRootCauses** provides specific categories for confirmed threats, infrastructure issues, or system malfunctions.

#### Constants

Constant | Value  
---|---  
`EXTERNAL_ATTACK`| 'External attack'  
`INFRASTRUCTURE_ISSUE`| 'Infrastructure issue'  
`IRRELEVANT_TCP_UDP_PORT`| 'Irrelevant TCP/UDP port'  
`MISCONFIGURED_SYSTEM`| 'Misconfigured system'  
`OTHER`| 'Other'  
`SIMILAR_CASE_IS_ALREADY_UNDER_INVESTIGATION`|  'Similar case is already under investigation'  
`SYSTEM_APPLICATION_MALFUNCTION`|  'System/application malfunction'  
`SYSTEM_CLOCKED_THE_ATTACK`| 'System blocked the attack'  
`UNFORESEEN_EFFECTS_OF_CHANGE`| 'Unforeseen effects of change'  
`UNKNOWN`| 'Unknown'  
  
### _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertNotMaliciousRootCauses

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertNotMaliciousRootCauses(value, names=None, *, module=None, qualname=None, type=None, start=1, boundary=None)`

Bases: **Enum**

**CloseCaseOrAlertNotMaliciousRootCauses** defines categories for benign activities, legit actions, or errors that do not pose a threat.

#### Constants

Constant | Value  
---|---  
`EMPLOYEE_ERROR`| 'Employee error'  
`HUMAN_ERROR`| 'Human error'  
`LAB_TEST`| 'Lab test'  
`LEGIT_ACTION`| 'Legit action'  
`MISCONFIGURED_SYSTEM`| 'Misconfigured system'  
`NONE`| 'None'  
`NORMAL_BEHAVIOR`| 'Normal behavior'  
`OTHER`| 'Other'  
`PENETRATION_TEST`| 'Penetration test'  
`RULE_UNDER_CONSTRUCTION`| 'Rule under construction'  
`SIMILAR_CASE_IS_ALREADY_UNDER_INVESTIGATION`|  'Similar case is already under investigation'  
`UNKNOWN`| 'Unknown'  
`USER_MISTAKE`| 'User mistake'  
  
### _class_ TIPCommon.base.action.data_models.CloseCaseOrAlertReasons

_class_ `TIPCommon.base.action.data_models.CloseCaseOrAlertReasons(value)`

Bases: **Enum**

**CloseCaseOrAlertReasons** provides standardized high-level categories for why a case or alert is being closed.

#### Constants

Constant | Value  
---|---  
`MALICIOUS`| 0  
`NOT_MALICIOUS`| 1  
`MAINTENANCE`| 2  
`INCONCLUSIVE`| 3  
  
###  _class_ TIPCommon.base.action.data_models.Content

_class_ `TIPCommon.base.action.data_models.Content(content: str, title: str = 'Script Result Content')`

Bases: **object**

**Content** represents an immutable text result generated by a script to add to the case wall.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes define the textual or markdown-based content displayed within the case results on the platform.

Attributes  
---  
`title` |  `str | None` The display title for the content block as it appears in the script results UI.  
`content` |  `str` The core message content, which can be provided as a raw text string or formatted as markdown.  
  
### _class_ TIPCommon.base.action.data_models.DataTable

_class_ `TIPCommon.base.action.data_models.DataTable(data_table: list[str], title: str = 'Script Result Data Table')`

Bases: **object**

**DataTable** represents a list of CSV-formatted strings rendered as a structured table in the case results.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes define the structure and display of tabular data within the action's result set.

Attributes  
---  
`title` |  `str | None` The heading displayed above the data table in the platform interface.  
`data_table` |  `list[str]` A list of strings where each element represents a CSV-formatted row that constructs the table.  
  
### _class_ TIPCommon.base.action.data_models.EntityInsight

_class_ `TIPCommon.base.action.data_models.EntityInsight(entity: DomainEntityInfo, message: str, triggered_by: str | None = None, original_requesting_user: str | None = None)`

Bases: **object**

**EntityInsight** is used to create specific findings associated with an entity, often displayed within the entity's details view.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

The following attributes define the relationship between an entity and the findings generated by an integration script.

Attributes  
---  
`entity` |  `Entity` The entity object that is being enriched with new findings.  
`message` |  `str` The core observation, finding, or descriptive message for the entity.  
`triggered_by` |  `str | None` The name of the integration that identified the finding.  
`original_requesting_user` |  `str | None` The unique identifier of the user who originally initiated the request.  
  
### _class_ TIPCommon.base.action.data_models.EntityTypesEnum

_class_ `TIPCommon.base.action.data_models.EntityTypesEnum(value)`

Bases: **Enum**

**EntityTypesEnum** provides constants for all entity types recognized by Google SecOps.

#### Constants

The following constants define the standardized entity types supported by the platform for enrichment and automation tasks.

Constant | Value  
---|---  
`ADDRESS`| 'ADDRESS'  
`ALERT`| 'ALERT'  
`APPLICATION`| 'APPLICATION'  
`CHILD_HASH`| 'CHILDHASH'  
`CHILD_PROCESS`| 'CHILDPROCESS'  
`CLUSTER`| 'CLUSTER'  
`CONTAINER`| 'CONTAINER'  
`CREDIT_CARD`| 'CREDITCARD'  
`CVE`| 'CVE'  
`CVE_ID`| 'CVEID'  
`DATABASE`| 'DATABASE'  
`DEPLOYMENT`| 'DEPLOYMENT'  
`DESTINATION_DOMAIN`| 'DESTINATIONDOMAIN'  
`DOMAIN`| 'DOMAIN'  
`EMAIL_MESSAGE`| 'EMAILSUBJECT'  
`EVENT`| 'EVENT'  
`FILE_HASH`| 'FILEHASH'  
`FILE_NAME`| 'FILENAME'  
`GENERIC`| 'GENERICENTITY'  
`HOST_NAME`| 'HOSTNAME'  
`IP_SET`| 'IPSET'  
`MAC_ADDRESS`| 'MacAddress'  
`PARENT_HASH`| 'PARENTHASH'  
`PARENT_PROCESS`| 'PARENTPROCESS'  
`PHONE_NUMBER`| 'PHONENUMBER'  
`POD`| 'POD'  
`PROCESS`| 'PROCESS'  
`SERVICE`| 'SERVICE'  
`SOURCE_DOMAIN`| 'SOURCEDOMAIN'  
`THREAT_ACTOR`| 'THREATACTOR'  
`THREAT_CAMPAIGN`| 'THREATCAMPAIGN'  
`THREAT_SIGNATURE`| 'THREATSIGNATURE'  
`URL`| 'DestinationURL'  
`USB`| 'USB'  
`USER`| 'USERUNIQNAME'  
  
### _class_ TIPCommon.base.action.data_models.ExecutionState

_class_ `TIPCommon.base.action.data_models.ExecutionState(value)`

Bases: **Enum**

**ExecutionState** represents the final status indicator returned to the platform to determine the success or failure of an action.

#### Constants

Constant | Value  
---|---  
`COMPLETED`| 0  
`IN_PROGRESS`| 1  
`FAILED`| 2  
`TIMED_OUT`| 3  
  
###  _class_ TIPCommon.base.action.data_models.FullDetailsConfigurationParameter

_class_ `TIPCommon.base.action.data_models.FullDetailsConfigurationParameter(input_dict: dict[str, Any])`

Bases: **object**

**FullDetailsConfigurationParameter** encapsulates a general integration configuration parameter with its full metadata as retrieved from the API.

#### Attributes

The following attributes manage parameter metadata, identification, and configuration constraints.

table>

Attributes  
`full_dict` |  `dict[str, Any]` The original dictionary received from the API response.  
`id` |  `int | None` The unique platform-assigned identifier for the parameter.  
`integration_identifier` |  `str` The identifier for the integration associated with this parameter, such as `VirusTotalV3`.  
`creation_time` |  `int` The timestamp indicating when the parameter was created, in Unix milliseconds.  
`modification_time` |  `int` The timestamp indicating when the parameter was last modified, in Unix milliseconds.  
`is_mandatory` |  `bool` Defines whether the parameter is required for the integration to function.  
`description` |  `str | None` The detailed description of the parameter's purpose.  
`name` |  `str` The internal identifier name for the parameter.  
`display_name` |  `str` The human-readable name of the parameter as displayed in the platform interface.  
`value` |  `Any` The default value assigned to the parameter.  
`type` |  `IntegrationParamType` The data type classification of the parameter.  
`optional_values` |  `list` A list of optional values provided for drop-down list (DDL) parameter types.  
  
### _class_ TIPCommon.base.action.data_models.HTMLReport

_class_ `TIPCommon.base.action.data_models.HTMLReport(report_name: str, report_contents: str, ...)`

Bases: **object**

**HTMLReport** represents a custom HTML-based visualization to add to the case results.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

Attributes  
---  
`title` |  `str | None` The display title for the report on the case wall.  
`report_name` |  `str` The internal identifier or filename for the report.  
`report_contents` |  `str` The raw HTML string defining the report's content.  
  
### _class_ TIPCommon.base.action.data_models.IntegrationParamType

_class_ `TIPCommon.base.action.data_models.IntegrationParamType(value)`

Bases: **Enum**

**IntegrationParamType** specifies the supported data types for integration configuration settings.

#### Constants

Constant | Value  
---|---  
`NULL`| -1  
`BOOLEAN`| 0  
`INTEGER`| 1  
`STRING`| 2  
`PASSWORD`| 3  
`IP`| 4  
`EMAIL`| 8  
  
###  _class_ TIPCommon.base.action.data_models.Link

_class_ `TIPCommon.base.action.data_models.Link(link: str, title: str = 'Script Result Link')`

Bases: **object**

**Link** represents an external URL result to display as a hyperlink on the case wall.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

Attributes  
---  
`title` |  `str | None` The display text for the hyperlink.  
`link` |  `str` The target URL for the link.  
  
### _class_ TIPCommon.base.action.data_models.Markdown

_class_ `TIPCommon.base.action.data_models.Markdown(markdown_name: str, markdown_content: str, ...)`

Bases: **object**

**Markdown** provides a structured way to return rich-text formatted content using markdown syntax.

**Note:** This class is immutable; after assigning values and creating the object, new values cannot be assigned to the attributes. The class supports hashing (stored in a set or as a dict key) and the `==` operator.

#### Attributes

Attributes  
---  
`title` |  `str | None` The display title for the markdown block.  
`markdown_content` |  `str` The content formatted in markdown syntax.  
`markdown_name` |  `str` The unique name assigned to this markdown result.  
  
### _class_ TIPCommon.base.action.data_models.ScriptParameter

_class_ `TIPCommon.base.action.data_models.ScriptParameter(input_dict: dict[str, Any])`

Bases: **object**

**ScriptParameter** represents a single input parameter for an action script, managing its value, default state, and visibility within playbooks or manual actions.

#### Attributes

The following attributes manage the metadata, value prioritization, and data constraints for individual script parameters.

Attributes  
---  
`full_dict` |  `dict[str, Any]` The original dictionary received from the API response.  
`id` |  `int | None` The unique platform-assigned identifier for the parameter.  
`creation_time` |  `int` The timestamp indicating when the parameter was created, in Unix milliseconds.  
`modification_time` |  `int` The timestamp indicating when the parameter was last modified, in Unix milliseconds.  
`custom_action_id` |  `int | None` The identifier of the custom action associated with this parameter.  
`is_mandatory` |  `bool` Indicates whether the parameter must be provided for the action script to execute.  
`default_value` |  `Any` The default value of the parameter. This value is prioritized over `value` in playbook executions.  
`description` |  `str | None` The detailed description of the parameter's purpose.  
`name` |  `str | None` The internal identifier name for the parameter.  
`value` |  `Any` The current value of the parameter. This value is prioritized over `default_value` in manual action executions.  
`type` |  `ActionParamType` The data type classification of the parameter.  
`optional_values` |  `list` A list of optional values provided for drop-down list (DDL) parameter types.  
  
## Script execution results

The following classes and functions define the standardized structures for returning data from actions and connectors to the platform.

### _class_ TIPCommon.base.data_models.ActionJsonOutput

_class_ `TIPCommon.base.data_models.ActionJsonOutput(title='JsonResult', content='', type=None, is_for_entity=False, json_result=None)`

Bases: **object**

**ActionJsonOutput** represents the structured JSON payload for an action, allowing for specific categorization and entity-level targeting.

#### Attributes

Attributes  
---  
`title` |  `str` The display title for the JSON result block.  
`content` |  `str` Textual content or a summary accompanying the JSON data.  
`type` |  `str | None` An optional classification type for the JSON output.  
`is_for_entity` |  `bool` Indicates if the JSON result is specifically associated with an entity.  
`json_result` |  `JSON | None` The actual structured JSON data payload.  
  
### _class_ TIPCommon.base.data_models.ActionOutput

_class_ `TIPCommon.base.data_models.ActionOutput(output_message, result_value, execution_state, json_output, debug_output='')`

Bases: **object**

**ActionOutput** encapsulates the complete result structure for an action, combining human-readable messages, state, and structured JSON.

#### Attributes

Attributes  
---  
`output_message` |  `str` The main summary message displayed to the analyst.  
`result_value` |  `str | bool` The logical result of the action (e.g., success/failure).  
`execution_state` |  `ExecutionState` The final lifecycle state of the action execution.  
`json_output` |  `ActionJsonOutput | None` The structured JSON results of the action.  
`debug_output` |  `str` Optional diagnostic information for troubleshooting.  
  
### _class_ TIPCommon.base.data_models.ConnectorJsonOutput

_class_ `TIPCommon.base.data_models.ConnectorJsonOutput(alerts, overflow_alerts=<factory>, log_items=<factory>, log_rows=<factory>, variables=<factory>)`

Bases: **object**

**ConnectorJsonOutput** defines the structured data returned by a connector, including ingested alerts, overflow details, and execution logs.

#### Attributes

Attributes  
---  
`alerts` |  `list[AlertInfo | CaseInfo]` A list of successfully ingested alert or case objects.  
`overflow_alerts` |  `list[OverflowAlertDetails]` A list of alerts that exceeded ingestion limits and were handled as overflow.  
`log_items` |  `list` A list of structured log entries generated during the connector run.  
`variables` |  `dict` A dictionary of state variables persisted between connector executions.  
  
### _class_ TIPCommon.base.data_models.ConnectorOutput

_class_ `TIPCommon.base.data_models.ConnectorOutput(json_output, debug_output='')`

Bases: **object**

**ConnectorOutput** represents the top-level container for connector execution results, wrapping the structured JSON data and optional debug strings.

#### Attributes

Attributes  
---  
`json_output` |  `ConnectorJsonOutput | None` The structured JSON results containing ingestion and log data.  
`debug_output` |  `str` Optional debugging string for internal diagnostic tracking.  
  
### TIPCommon.base.data_models.alert_info_from_json

`TIPCommon.base.data_models.alert_info_from_json(json_) → AlertInfo`

Creates an `AlertInfo` object by parsing a dictionary of attributes. This is typically used to reconstruct alert objects during data transformation or testing.

#### Returns

Returns a fully initialized `AlertInfo` object based on the properties defined in the provided JSON dictionary.

## Interfaces module

This module defines standard abstract contracts for foundational script components.

### _class_ TIPCommon.base.interfaces.apiable.Apiable

_class_ `TIPCommon.base.interfaces.apiable.Apiable(authenticated_session: AuthenticatedSession, configuration: ApiParams)`

Bases: **ABC** , **Generic[ApiParams]**

**Apiable** is an abstract base interface for classes that encapsulate API communication logic, ensuring a consistent structure for external service interactions.

### _class_ TIPCommon.base.interfaces.authable.Authable

_class_ `TIPCommon.base.interfaces.authable.Authable`

Bases: **ABC** , **Generic[AuthParams]**

**Authable** is an abstract base interface for classes that manage authentication workflows, providing a standardized blueprint for establishing secure sessions with external services.

#### Abstract methods

The following abstract methods must be implemented in subclasses to define the specific authentication logic required by the target service.

Abstract methods  
---  
`authenticate_session()` |  `authenticate_session(params: AuthParams) → None` Authenticates the `self.session` attribute using the provided `params` (such as a `dataclass`, `TypedDict`, or `namedtuple`). Use this method to establish authentication with the service associated with the session after the session object has been initialized.  
  
### _class_ TIPCommon.base.interfaces.logger.Logger

_class_ `TIPCommon.base.interfaces.logger.Logger`

Bases: **ABC**

The **Logger** interface ensuring Content Hub scripts provide standardized diagnostic output.

#### Abstract Methods

The following methods must be implemented to handle various logging severity levels and exception reporting.

Abstract methods  
---  
`debug()` |  `debug(msg: str, *args, **kwargs) → None` Logs a message with the `DEBUG` severity level.  
`info()` |  `info(msg: str, *args, **kwargs) → None` Logs a message with the `INFO` severity level.  
`warn()` |  `warn(warning_msg: str, *args, **kwargs) → None` Logs a message with the `WARNING` severity level.  
`error()` |  `error(error_msg: str, *args, **kwargs) → None` Logs a message with the `ERROR` severity level.  
`exception()` |  `exception(ex: Exception, *args, **kwargs) → None` Logs a message with the `ERROR` severity level, including the exception stack trace.  
  
### _class_ TIPCommon.base.interfaces.session.Session

_class_ `TIPCommon.base.interfaces.session.Session`

Bases: **ABC** , **Generic[_R]**

The **Session** interface provides a consistent blueprint for managing API sessions using various HTTP libraries.

#### Attributes

The following attributes manage the configuration and security settings of the established HTTP communication session.

Attributes  
---  
`headers` |  `dict` A dictionary containing the HTTP headers to send with each request in the session.  
`verify` |  `bool` A boolean indicating whether the session should verify the server's SSL certificate.  
  
#### Abstract methods

The following abstract methods define the standard HTTP verbs and the primary request dispatcher that subclasses must implement.

Abstract methods  
---  
`get()` |  `get(url: str, *args, **kwargs) → _R` Retrieves a resource from the server using an HTTP GET request.  
`post()` |  `post(url: str, *args, **kwargs) → _R` Sends data to the server to create a resource using an HTTP POST request.  
`put()` |  `put(url: str, *args, **kwargs) → _R` Updates or creates a resource on the server using an HTTP PUT request.  
`patch()` |  `patch(url: str, *args, **kwargs) → _R` Applies partial modifications to a resource using an HTTP PATCH request.  
`delete()` |  `delete(url: str, *args, **kwargs) → _R` Removes a specified resource from the server using an HTTP DELETE request.  
`request()` |  `request(method: str, *args, **kwargs) → _R` The core request dispatcher used to perform an HTTP request with a specified method.  
  
## Jobs module

This provides the framework for background processing scripts that execute on a defined schedule within the platform.

### _class_ TIPCommon.base.job.base_job.Job

_class_ `TIPCommon.base.job.base_job.Job(name: str)`

Bases: **ABC** , **Generic[ApiClient]**

**Job** is an abstract base class designed for scheduled tasks that perform independent background operations, such as data synchronization or health checks.

#### Parameters

The following parameter is required to initialize the job and register it within the platform.

Parameters  
---  
`name` | The unique identifier used to register and identify the job script.  
  
#### Attributes

The following properties provide access to the job's execution context, configuration, and integrated service clients.

Attributes  
---  
`api_client` |  `ApiClient | None` Provides the initialized API client or collection of clients for interacting with external services.  
`error_msg` |  `str` Stores any error messages encountered during the execution of the job for diagnostic reporting.  
`job_start_time` |  `int` The Unix timestamp representing when the job execution began.  
`logger` |  `ScriptLogger` Provides the logging interface for capturing informational, warning, and error data during execution.  
`name` |  `str` The registered name of the job script.  
`params` |  `Container` A container holding the specific configuration parameters provided to the job instance.  
`soar_job` |  `SiemplifyJob` Represents the underlying platform job instance, providing access to low-level execution hooks.  
  
#### Methods

The following methods manage the orchestration and execution lifecycle of the job.

Methods  
---  
`start()` |  **Signature:** `start(**kwargs) → None` The primary entry point that triggers the job's execution logic.  
  
### _class_ TIPCommon.base.job.base_job_refresh_token.RefreshTokenRenewalJob

_class_ `TIPCommon.base.job.base_job_refresh_token.RefreshTokenRenewalJob(name: str, integration_identifier: str)`

Bases: **Job** , **Generic[ApiClient]**

**RefreshTokenRenewalJob** provides the lifecycle methods that influence job processing for token maintenance. Subclasses aren't required to override these methods.

#### Attributes

Attributes  
---  
`api_client` |  `ApiClient | Collection[ApiClient] | Type[Tuple[ApiClient, ...]] | None` The initialized API client or clients used for external service interactions.  
  
### _class_ TIPCommon.base.job.base_job_refresh_token.SuccessFailureTuple

_class_ `TIPCommon.base.job.base_job_refresh_token.SuccessFailureTuple(success_list, failure_list)`

Bases: **tuple**

**SuccessFailureTuple** is a specialized named tuple used to categorize the outcomes of batch job operations into successes and failures.

#### Attributes

Attributes  
---  
`success_list` |  `list` A list containing the identifiers or objects that were processed successfully.  
`failure_list` |  `list` A list containing the identifiers or objects that failed processing.  
  
### TIPCommon.base.job.base_job_refresh_token.validate_param_csv_to_multi_value

`TIPCommon.base.job.base_job_refresh_token.validate_param_csv_to_multi_value(param_name, param_csv_value, delimiter=',') → list[str]`

This function validates and parses a comma-separated (CSV) parameter string into a list of unique elements. It is designed to handle complex formats, including single values, quoted strings, and mixed input.

#### Parameters

Parameters  
---  
`param_name` |  `str` The name or key of the parameter being validated.  
`param_csv_value` |  `str | None` The raw CSV string provided in the job configuration. Returns an empty list if `None`.  
  
#### Raises

A **ValueError** exception is raised if the input string contains an invalid number of double quotes, mismatched quotes, or if any individual values within the CSV fail validation.

#### Returns

A **list[str]** list of unique, validated strings parsed from the input. If no valid values are identified or if the input is `None`, an empty list is returned.

### _class_ TIPCommon.base.job.data_models.JobParameter

_class_ `TIPCommon.base.job.data_models.JobParameter(input_dict: MutableMapping[str, Any])`

Bases: **object**

**JobParameter** represents an individual configuration parameter for a job script, managing its metadata and value state.

#### Attributes

Attributes  
---  
`full_dict` |  `dict[str, Any]` The original dictionary received from the API during job initialization.  
`id` |  `int | None` The unique platform-assigned identifier for the job parameter.  
`is_mandatory` |  `bool` Indicates whether the parameter must be provided for the job to run.  
`name` |  `str | None` The internal identifier name for the parameter.  
`type` |  `ActionParamType` The data type classification of the parameter.  
`value` |  `Any` The default value of the parameter; this value is typically prioritized in automated job executions.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
