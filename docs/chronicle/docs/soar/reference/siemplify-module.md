---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module/
title: Siemplify module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:42:00.086057+00:00
---

# Siemplify module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Siemplify module

## _class_ `Siemplify.Siemplify`

Bases: SiemplifyBase

Endpoints: `external/v1/sdk/CaseFullDetails`

### add_agent_connector_logs
    
    
    add_agent_connector_logs(agent_id, connector_id, logs_package)
    

Add logs of the remote agent's `connector_id` connector.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
agent_id | {string} | Agent's identifier | N/A | N/A  
connector_id | {string} | Connector instance identifier | N/A | N/A  
logs_package | {dict} | ConnectorLogPackage | N/A | N/A  
  
### add_attachment
    
    
    add_attachment(file_path, case_id, alert_identifier, description=None, is_favorite=False)
    

This function adds an entry to the case wall with a file attachment (that can be then downloaded from the client into the user's local machine). The function does essentially the same thing as adding evidence (on the bottom of the case overview screen).

**Note:** To upload a file to the case wall, make sure that the file is available in the file system of the server or on a shared location accessible from the server.

#### Parameters

Param name  | Param type  | Definition  | Possible values  | Comments   
---|---|---|---|---  
file_path  | {string}  | Path for the file  | Any accessible path  | A path can also be a remote location. You need read permissions to that file   
case_id  | {string}  | Case identifier  | A case ID to add the attachment to its case wall  | Default is the current case   
alert_identifier  | {string}  | Alert identifier  | Alert identifier string of the alert you want to associate the attachment with  | Default is the current running alert   
description  | {string}  | Attachment description  | Any string  | None by default.  
Optional parameter.   
is_favorite  | {boolean}  | Attachment favorite  | True/False  | `False` by default.  
Optional parameter.   
  
#### Returns

{long} attachment_id

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.add_attachment(r'C:/temp/investigation.txt', description='Deep investigation report by TIER3 team', is_favorite=True)
    

#### Result behavior

In this example, we will upload the `investigation.txt` from `C:/temp` on the local machine (the server itself) to the case wall. A comment will be added to that entry on the case wall, with the string in the description. The `is_favorite` flag was set to `True`, and so this new entry will also be starred (favorite).

### add_comment
    
    
    add_comment(comment, case_id, alert_identifier)
    

Add a new comment to the specific case.

**Note:** Related concepts: [Case manipulation](https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation)

#### Parameters

Param name  | Param type  | Definition  | Possible values  | Comments   
---|---|---|---|---  
comment  | {string}  | Comment to be added to a case wall  | "This events in this alert seems suspicious"  | Comments related to the case   
case_id  | {string}  | Case identifier  | 234  | N/A   
alert_identifier  | {string}  | Alert identifier  | ad6879f1-b72d-419f-990c-011a2526b16d  | N/A   
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    add_comment = "This alert is important"
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    siemplify.add_comment(comment, case_id, alert_identifier)
    

#### Result behavior

The provided comment gets added to the case 234.

#### Result value

None

### add_entities_to_custom_list
    
    
    add_entities_to_custom_list(custom_list_items)
    

Add the custom list provided with the added entities to the custom list.

**Note:** Related concepts: [Custom lists](https://docs.cloud.google.com/chronicle/docs/soar/reference/custom-lists)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
custom_list_items | {string} | A list of custom list items | N/A | N/A  
  
#### Returns

{[CustomList]} a list of with the added custom list item.

#### Result behavior

Entity is added to a custom list category.

**Note:** You can add multiple values from the _CustomList_ or manipulate multiple lists with the same call.

### add_entity_insight
    
    
    add_entity_insight(domain_entity_info, message, case_id, alert_id)
    

Add an entity insight.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
domain_entity_info | {string} | Entity identifier | "192.0.2.1" | {DomainEntityInfo}  
message | {string} | Insight message | This is Example DNS | N/A  
case_id | {string} | Case identifier to add to an entity insight | 234 | N/A  
alert_id | {string} | Alert identifier to add to an entity insight | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

{boolean} `True` if success

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    entity = "192.0.2.1"
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    siemplify.add_entity_insight(domain_entity_info=entity, message=message, case_id=case_id, alert_id=alert_identifier)
    

#### Result behavior

The given message gets added as insight to the entity 192.0.2.1 of the given alert identifier in the case 234.

#### Result value

True.

False if the insight is not added.

### add_entity_to_case
    
    
    add_entity_to_case(case_id, alert_identifier, entity_identifier, entity_type, is_internal, is_suspicious, is_enriched, is_vulnerable, properties, environment)
    

Add entity to case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
entity_identifier | {string} | Entity identifier | 192.0.2.1, example.com | N/A  
entity_type | {string} | Entity type of the entity identifier | "ADDRESS" | N/A  
is_internal | {boolean} | N/A | True/False | N/A  
is_suspicious | {boolean} | N/A | True/False |   
is_enriched  | {boolean} | N/A | True/False | False by default  
is_vulnerable | {boolean} | N/A | True/False | False by default  
properties | {dict} | Property of the entity | {"property":"value"} | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    case_id = "234"
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    entity = "192.0.2.1"
    entity_type = "ADDRESS"
    properties = {"property": "value"}
    siemplify.add_entity_to_case(case_id=case_id,
                                              alert_identifier = alert_identifier,
                                              entity_identifier = entity,
                                              entity_type = entity_type,
                                              is_internal = True,
                                              is_suspicious = False,
                                              is_enriched = False,
                                              is_vulnerable = False,
                                              properties = properties,
                                              environment=None)
    

#### Result behavior

The entity with the provided information will be added to the given alert within the case 234.

#### Result value

None

### add_or_update_case_task
    
    
    add_or_update_case_task(task)
    

Add or update a task case: update if there's a task ID, add (create) otherwise.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
task | {Task} | The task object which should be added to the case or updated | N/A | N/A  
  
#### Returns

{int} the ID of the new or updated task.

### add_tag
    
    
    add_tag(tag, case_id, alert_identifier)
    

Add new tag to a specific case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
tag | {string} | Tag to be added | N/A | N/A  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
### any_entity_in_custom_list
    
    
    any_entity_in_custom_list(custom_list_items)
    

Check if there's any entity from the given list, which has a custom list record with the given category.

**Note:** Related concepts: [Custom lists](https://docs.cloud.google.com/chronicle/docs/soar/reference/custom-lists)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
custom_list_items | {[CustomList]} | A list of custom list items to check for entities | N/A | N/A  
  
#### Returns

{boolean} `True` if there's an entity found, `False` otherwise.

#### Result value

True or False

### assign_case
    
    
    assign_case(user, case_id, alert_identifier)
    

This function assigns the current case to the user.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
user | {string} | User/role | Admin, @Tier1 | N/A  
case_id | {string} | Case identifier to assign user | 234 | N/A  
alert_identifier | {string} | Alert identifier to assign user | ad6879f1-b72d-419f-990c-011a2526b16d | This value is fetched during the run time of the action  
  
#### Returns

`NoneType`

#### Result behavior

The case gets assigned to the specified user.

#### Result value

None

### attach_workflow_to_case
    
    
    attach_workflow_to_case(workflow_name, cyber_case_id, indicator_identifier)
    

Attach a playbook to the case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
workflow_name | {string} | Workflow name | N/A | N/A  
cyber_case_id | {string} | Case identifier | 234 | N/A  
indicator_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

{string} status code of the server operation

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    workflow_name = "Workflow 234"
    siemplify.attach_workflow_to_case(workflow_name=workflow_name, cyber_case_id=case_id, indicator_identifier=alert_identifier)
    

#### Result behavior

Workflow 234 will be attached to case 234.

#### Result value

None

### batch_update_case_id_matches
    
    
    batch_update_case_id_matches(case_id_matches)
    

Batch update of cases with the suitable external case IDs.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id_matches | {list} | List of [SyncCaseIdMatch](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#SyncCaseIdMatch) objects |  |   
  
#### Returns

{list} List of case IDs that were updated successfully.

### change_case_priority
    
    
    change_case_priority(priority, case_id, alert_identifier)
    

Change case priority.

**Note:** Related concepts: [Case manipulation](https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
priority | {int} | Case priority to change | 40/60/80/100 | See [ApiSyncCasePriorityEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncCasePriorityEnum).  
The priority mapping: {"Low": 40, "Medium": 60, "High": 80, "Critical": 100}  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    priority = 40
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    siemplify.change_case_priority(priority=priority, case_id=case_id, alert_identifier=alert_identifier)
    

#### Result behavior

The priority of the case 234 gets changed to 40, which is mapped to low.

#### Result value

None

### change_case_stage
    
    
    change_case_stage(stage, case_id, alert_identifier)
    

Change case stage.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
stage | {string} | The current stage of the case. | Incident | N/A  
case_id | {string} | Case identifier | N/A | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
### check_marketplace_status
    
    
    check_marketplace_status()
    

Check marketplace status.   
If there is no error, the function returns `none`. Otherwise, an exception is returned.

#### Parameters

N/A

#### Returns

None

### close_alert
    
    
    close_alert(root_cause, comment, reason, case_id, alert_id)
    

This function closes the current alert. It is the same as manually closing the alert from the case overview. Function requires the reason for closure, a root cause and a comment, just like the close case alert.  
Closing an alert closes the new case with only one alert.

**Note:** Related concepts: [Case manipulation](https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
root_cause | {string} | Close case root cause | N/A | N/A  
comment | {string} | A comment | N/A | N/A  
reason | {ApiSyncAlertCloseReasonEnum} | N/A | N/A | See [SiemplifyDataModel.ApiSyncAlertCloseReasonEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncAlertCloseReasonEnum)  
case_id | {string} | Case identifier that alert is in | 234 | N/A  
alert_id | {string} | Alert identifier to close | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

{dict} result of server operation

### close_case
    
    
    close_case(root_cause, comment, reason, case_id, alert_identifier)
    

Close a case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
root_cause | {string} | The root cause for closing a case | N/A | N/A  
comment | {string} | A comment | N/A | N/A  
reason | {ApiSyncAlertCloseReasonEnum} | Close case reason |  | See [SiemplifyDataModel.ApiSyncAlertCloseReasonEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncAlertCloseReasonEnum)  
case_id | {string} | Case identifier | 234 | N/A  
alert_id | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
### create_case
    
    
    create_case(case_info)
    

This function creates a case with the alerts and events contained in the `case_info` dictionary.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_info | {CaseInfo} | Case info object | N/A | See `SiemplifyConnectorsDataModel.CaseInfo`  
  
#### Returns

`NoneType`

#### Result behavior

The case with the provided case data is created.

#### Result value

None

### create_case_insight_internal
    
    
    create_case_insight_internal(case_id, alert_identifier, triggered_by, title, content, entity_identifier, severity, insight_type, additional_data=None, additional_data_type=None, additional_data_title=None, original_requesting_user=None, entity_type=None)
    

Add insight.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
triggered_by | {string} | Integration name | N/A | N/A  
title | {string} | Insight title | N/A | N/A  
content | {string} | Insight message | N/A | N/A  
entity_identifier | {string} | Entity identifier | N/A | N/A  
severity | {int} | Severity identifier | 0 = info,   
1 = warning,   
2 = error | N/A  
insight_type | {int} | Insight type | 0 = general,   
1 = entity | N/A  
additional_data | N/A | N/A | N/A | N/A  
additional_data_type | N/A | N/A | N/A | N/A  
additional_data_title | N/A | N/A | N/A | N/A  
original_requesting_user | N/A | N/A | N/A | N/A  
entity_type | {string} | Entity type | "ADDRESS" | N/A  
  
#### Returns

{boolean} `True` if success.

### create_connector_package
    
    
    create_connector_package(connector_package)
    

Create a connector package in the system.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
connector_package  | {string} | Connector package as a json | N/A | N/A  
  
### dismiss_alert
    
    
    dismiss_alert(alert_group_identifier, should_close_case_if_all_alerts_were_dismissed, case_id)
    

**Deprecated:** The function is deprecated.

### end
    
    
    end(message, result_value, execution_state=0)
    

End the script.  
No other code after the `end()` function is executed.  
The end result value is written in the stdout.  
The end function is not mandatory for scheduled jobs.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
message | {string} | Output message to be displayed to the client | Action completed | N/A  
result_value | {int/string/dict} | Return value | N/A | N/A  
execution_state | {int} | Indicator for the current action's state. Mainly used in async actions for marking whether the action has completed or not.  | 0 (EXECUTION_STATE_COMPLETED),   
1 (EXECUTION_STATE_INPROGRESS),   
2 (EXECUTION_STATE_FAILED),   
3 (EXECUTION_STATE_TIMEDOUT) | Default is 0  
  
#### Returns

Returning the result data to the host process.

**Important:** If the end function is not called, the script shows the following error: `Script did not return expected data. Did you call build_result/end_script? Check DebugOutput for details.`

### end_script
    
    
    end_script()
    

**Deprecated:** Do not use. Kept for reverse compatibility with old scripts.

### escalate_case
    
    
    escalate_case(comment, case_id, alert_identifier)
    

Escalate a case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
comment | {string} | Escalate comment | N/A | N/A  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
### extract_configuration_param
    
    
    extract_configuration_param(provider_name, param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False)
    

Get a configuration parameter from the integration instance.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
provider_name | {string} | Name of the integration | N/A | N/A  
param_name | {string} | Name of the parameter | N/A | N/A  
default_value | {any} | If the parameter is not passed, use this value by default | N/A | None by default (optional)  
input_type | {obj} | Cast the parameter to a different type | N/A | For example, int.  
str by default (optional)  
is_mandatory | {bool} | Raise an exception if the parameter is empty | N/A | `False` by default (optional)  
print_value | {bool} | Print the value to the log | N/A | `False` by default (optional)  
  
#### Returns

The parameter value (string by default), unless `input_type` is specified.

### _static_ generate_serialized_object
    
    
    generate_serialized_object(object_filter)
    

### get_agent_by_id
    
    
    get_agent_by_id(agent_id)
    

Gets the agent details by ID.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
agent_id | {str} | The ID of the agent | N/A | N/A  
  
#### Returns

{dict} The publisher details

### get_alerts_ticket_ids_from_cases_closed_since_timestamp
    
    
    get_alerts_ticket_ids_from_cases_closed_since_timestamp(timestamp_unix_ms, rule_generator)
    

Get alerts from cases that were closed since timestamp.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
timestamp_unix_ms | {long} | Timestamp | 1550409785000L | N/A  
rule_generator | {string} | N/A | 'Phishing email detector' | N/A  
  
#### Returns

{list} alerts

### get_attachment
    
    
    get_attachment(attachment_id)
    

Get attachment data by identifier.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
attachment_id | {string} | Attachment identifier | N/A | N/A  
  
#### Returns

{BytesIO} attachment data

### get_attachments
    
    
    get_attachments(case_id)
    

Get attachments from the case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
  
#### Returns

{dict} attachments

#### Result value

`[{"is_favorite": False, "description": "", "type": ".txt", "id": 1, "name": "test.py"}]`

### _get_case_by_id
    
    
    _get_case_by_id(case_id)
    

Get a case using its case ID.

This function interacts with the following endpoint: `external/v1/sdk/CaseFullDetails`

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {[string]} | Case ID | N/A | N/A  
  
#### Returns

{dict} case data.

### get_case_closure_details
    
    
    get_case_closure_details(case_id_list)
    

Get case closure details.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id_list | {[string]} | List of case IDs | N/A | N/A  
  
#### Returns

{[dict]} list of dict containing case closure details.

#### Result value

`[{'case_closed_action_type': 1, 'reason': NotMalicious', 'root_cause': 'Other'}]`

For the `case_closed_action_type` parameter, the possible values are as follows:

  * 0 = Automatic
  * 1 = Manual



### get_case_comments
    
    
    get_case_comments(case_id)
    

This function gets the comments from the provided case.

**Note:** Related concepts: [Case manipulation](https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
  
#### Returns

List

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.get_case_comments(case_id)
    

#### Result behavior

All comments belonging to the case will be fetched.

#### Result value
    
    
    [
        {
                 u 'comment': u 'Test',
                 u 'case_id': 10085,
                 u 'is_favorite': False,
                 u 'alert_identifier': None,
                 u 'creator_user_id': u 'Admin',
                 u 'type': 5,
                 u 'id': 1,
                 u 'modification_time_unix_time_in_ms': 1563272078332L
          }, {
                 u 'comment': u 'jhfksdh',
                 u 'case_id': 10085,
                 u 'is_favorite': False,
                 u 'alert_identifier': None,
                 u 'creator_user_id': u 'Admin',
                 u 'type': 5,
                 u 'id': 2,
                 u 'modification_time_unix_time_in_ms': 1563272079941L
    
           }, {
                  u 'comment': u 'kjfhsdm',
                  u 'case_id': 10085,
                  u 'is_favorite': False,
                  u 'alert_identifier': None,
                  u 'creator_user_id': u 'Admin',
                  u 'type': 5,
                  u 'id': 3,
                   u 'modification_time_unix_time_in_ms': 1563272080598L
           }
     ]
    

### get_case_tasks
    
    
    get_case_tasks(case_id)
    

Retrieve all tasks by the Case ID.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {int/str} | Case ID  | 234 | The function can receive either int or str  
  
#### Returns

{[Task]} the list of tasks objects belonging to the case.   
See [SiemplifyDataModel.Task](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#DataModelTask).

### get_cases_by_filter
    
    
    get_cases_by_filter(environments=None, analysts=None, statuses=None, case_names=None, tags=None, priorities=None, stages=None, case_types=None, products=None, networks=None, ticked_ids_free_search='', case_ids_free_search='', wall_data_free_search='', entities_free_search='', start_time_unix_time_in_ms=-1, end_time_unix_time_in_ms=-1)
    

Get cases by requested filters.
    
    
    *caseFilterValue* object - { 'Title':'Merged Case', 'Value': 'Merged', 'Title':'Involved Suspicious Entity', 'Value': 'InvolvedSuspiciousEntity', 'Title':'Manual', 'Value': 'Manual', 'Title':'Simulated Alerts', 'Value': 'Simulated',}
    

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
environments | {[string]} | List of environment names (environment) | N/A | If no environments are provided, `None` is used (optional)  
analysts | {[string]} | List of analysts names (case assigned user/role), | N/A | If no analyst is provided, `None` is used (optional)  
statuses | {[int]} | List of statues to filter by | N/A | See [ApiSyncCaseStatusEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncCaseStatusEnum).  
If no statuses is provided, `None` is used (optional)  
case_names | {[string]} | List of case names | N/A | If no `case_names` are provided, `None` is used (optional)  
tags | {[string]} | List of case tags | N/A | If no tags are provided, `None` is used (optional)  
priorities | {[int]} | List of priorities |  | See [ApiSyncAlertPriorityEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncAlertPriorityEnum).  
If no priorities is provided, `None` is used (optional)  
stages | {list}  | List of stages (caseFilterValue object) | N/A | If no stages are provided, `None` is used (optional)  
case_types | {list} | List of object types ([caseFilterValue object)](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#CaseFilterValue) | N/A | Valid `case_types` values are: `0 = Merged`  
`1 = Important`  
`2 = InvolvedSuspiciousEntity`  
`3 = Manual`  
`4 = Simulated` If no `case_types` are provided, `None` is used (optional)  
products | {list} | List of products ([caseFilterValue object)](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#CaseFilterValue) | N/A | If no products are provided, `None` is used (optional)  
networks | {list} | List of network ([caseFilterValue object)](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#CaseFilterValue) | N/A | If no networks are provided, `None` is used (optional)  
ticked_ids_free_search | {string}  | Ticket identifier | N/A | If not provided, default is '' (optional)  
case_ids_free_search | {string}  | Case identifier | N/A | If not provided, default is '' (optional)  
wall_data_free_search | {string} | String to search | N/A | If not provided, default is '' (optional)  
entities_free_search | {string} | Entity identifier | N/A | If not provided, default is '' (optional)  
start_time_unix_time_in_ms | {long} | N/A | N/A | Default -1   
(optional)  
end_time_unix_time_in_ms | {long} | N/A | N/A | Default -1   
(optional)  
  
#### Returns

Case_ids ''

### get_cases_by_ticket_id
    
    
    get_cases_by_ticket_id(ticket_id)
    

Get a case by ticket identifier.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
ticket_id | {string} | Ticket identifier | N/A | N/A  
  
#### Returns

{[int]} list of case IDs.

### get_cases_ids_by_filter
    
    
    get_cases_ids_by_filter(status, start_time_from_unix_time_in_ms=None, start_time_to_unix_time_in_ms=None, close_time_from_unix_time_in_ms=None, close_time_to_unix_time_in_ms=None, update_time_from_unix_time_in_ms=None, update_time_to_unix_time_in_ms=None, operator=None, sort_by='START_TIME', sort_order='DESC', max_results=1000)
    

Get case IDs by filter.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
status | {str} | Case status to retrieve | 'OPEN', 'CLOSE', 'BOTH' | N/A  
start_time_from_unix_time_in_ms | {int} | Case start time start range inclusive | N/A | Default is 30 days prior (optional)  
start_time_to_unix_time_in_ms | {int} | Case start time end range inclusive | N/A | Default is time now (optional)  
close_time_from_unix_time_in_ms | {int} | Case close time start range inclusive | N/A | Default is 30 days prior (optional)  
close_time_to_unix_time_in_ms | {int} | Case close time end range inclusive. | N/A | Default is time now (optional)  
update_time_from_unix_time_in_ms | {int} | Case modification time start range inclusive | N/A | Default is start time (optional)  
update_time_to_unix_time_in_ms | {int} | Case modification time end range inclusive | N/A | Default is time now (optional)  
operator | {str} | Operator for time filters | OR, AND | Optional  
sort_by | {str} | Sort results by time | START_TIME, UPDATE_TIME, CLOSE_TIME | Optional  
sort_order | {str} | Sort order | ASC, DESC | Default is descending order (optional)  
max_results | {int} | Max results to return | N/A | Default value is 1000, maximum value is 10000 (optional)  
**Note:**

  * Sort order of type CLOSE_TIME must be provided with 'CLOSE' status only
  * Close time range filter is disregarded with 'BOTH' and 'OPEN' statuses



### get_configuration
    
    
    get_configuration(provider, environment, integration_instance)
    

Get integration configuration.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
provider | {string} | Integration name | "VirusTotal" | N/A  
environment | {string} | Configuration for specific environment or 'all' | N/A | N/A  
integration_instance | {string} | Identifier of the integration instance | N/A | N/A  
  
#### Returns

{dict} configuration details.

### get_configuration_by_provider
    
    
    get_configuration_by_provider(identifier)
    

Get integration configuration.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
provider | {string} | Integration name | "VirusTotal" | N/A  
  
#### Returns

{dict} configuration details

### get_existing_custom_list_categories
    
    
    get_existing_custom_list_categories()
    

Get all existing custom list categories.  
This function returns a list object of all the categories in the _CustomList_ settings irrespective of environments.

#### Parameters

N/A

#### Returns

{[unicode]} list of unicode type with existing categories.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction siemplify = SiemplifyAction() result = siemplify.get_existing_custom_list_categories()
    

#### Result behavior

A list of all existing custom lists is returned.

#### Result value

["DenyListed IPs", "AllowListed HOSTs"]

### get_external_configuration
    
    
    get_external_configuration(config_provider, config_name)
    

Get external integration configuration.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
config_provider | {string} | N/A | N/A | N/A  
config_name | {string} | N/A | N/A | N/A  
  
### get_integration_version
    
    
    get_integration_version(integration_identifier)
    

Get an integration version.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
integration_identifier | {string} | Integration identifier | N/A | N/A  
  
#### Returns

{float} integration version

### get_publisher_by_id
    
    
    get_publisher_by_id(publisher_id)
    

Get publisher details by ID.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
publisher_id | {string} | The id of the publisher | N/A | N/A  
  
#### Returns

{dict} The publisher details

### get_remote_connector_keys_map
    
    
    get_remote_connector_keys_map(publisher_id)
    

Get remote connectors encryption keys by publisher ID.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
publisher_id | {string} | The id of the publisher | N/A | N/A  
  
#### Returns

{dict} The keys map

### get_similar_cases
    
    
    get_similar_cases(case_id, ports_filter, category_outcome_filter, rule_generator_filter, entity_identifiers_filter, start_time_unix_ms, end_time_unix_ms)
    

Get similar cases.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
ports_filter | {boolean} | True/False use port filter | True/False | N/A  
category_outcome_filter | {boolean} | True/False use category_outcome filter | True/False | N/A  
rule_generator_filter | {boolean} | True/False use rule_generator filter | True/False | N/A  
entity_identifiers_filter | {boolean} | True/False use entity_identifiers filter | True/False | N/A  
start_time_unix_ms | N/A | N/A | N/A | N/A  
end_time_unix_ms | N/A | N/A | N/A | N/A  
  
#### Returns

{dict}

### get_sync_alerts
    
    
    get_sync_alerts(alert_group_ids)
    

Retrieve alerts information needed for systems synchronization.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
alert_group_ids | {list} | A list of alert group IDs to retrieve | N/A | N/A  
  
#### Returns

{[SyncAlert]} list of SyncAlert objects.

### get_sync_cases
    
    
    get_sync_cases(case_ids)
    

Retrieve the case information needed for systems synchronization.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_ids | {list} | A list of case IDs to retrieve | N/A | N/A  
  
#### Returns

{[SyncCase]} A list of `SyncCase` objects.

### get_system_info
    
    
    get_system_info(start_time_unixtime_ms)
    

### get_system_version
    
    
    get_system_version()
    

Get the current Google Security Operations SOAR version.

#### Parameters

N/A

#### Returns

{string} current Google Security Operations SOAR version

### get_temp_folder_path
    
    
    get_temp_folder_path()
    

Gets the path to the temp folder.

#### Parameters

N/A

#### Returns

{string} path to temp folder

### get_ticket_ids_for_alerts_dismissed_since_timestamp
    
    
    get_ticket_ids_for_alerts_dismissed_since_timestamp(timestamp_unix_ms)
    

**Deprecated:** The function is deprecated.

### get_updated_sync_alerts_metadata
    
    
    get_updated_sync_alerts_metadata(start_timestamp_unix_ms, count, allowed_environments=None, vendor=None)
    

Retrieve updated tracked alerts metadata.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
start_timestamp_unix_ms | {long} | Search for updated alerts starting at  
`start_timestamp_unix_ms` or later | N/A | If `end_timestamp_unix_ms` is `None`,  
the end time is the time of the request.  
count | {int} | Maximum alerts group IDs to fetch | N/A | N/A  
allowed_environments | {[string]} | Environments to search in | N/A | If `allowed_environments` is None,  
search in all environments  
vendor | {string} | Filter alerts by vendor | N/A | N/A  
  
#### Returns

{[SyncAlertMetadata]} List of `SyncAlertMetadata` objects, sorted by `SyncAlertMetadata.tracking_time`.

### get_updated_sync_cases_metadata
    
    
    get_updated_sync_cases_metadata(start_timestamp_unix_ms, count, allowed_environments=None, vendor=None)
    

Retrieve updated tracked cases metadata.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
start_timestamp_unix_ms | {long} | Search for updated cases starting at  
`start_timestamp_unix_ms` or later | N/A | If `end_timestamp_unix_ms` is None,  
end time will be the time of the request  
count | {int} | Maximum cases ids to fetch | N/A | N/A  
allowed_environments | {[string]} | Environments to search in | N/A | If `allowed_environments` is None,  
search in all environments  
vendor | {string} | Return only cases with alerts originated in `vendor` | N/A | N/A  
  
#### Returns

`{[SyncCaseMetadata]}` List of `SyncCaseMetadata` objects, sorted by `SyncCaseMetadata.tracking_time`.

### init_proxy_settings
    
    
    init_proxy_settings()
    

#### Parameters

N/A

### is_existing_category
    
    
    is_existing_category(category)
    

Checks if the given category exists.  
Given a category name, this function returns `True` (Boolean) if the exact _category name_ string is defined as a category in the _CustomList_ settings.  
This function ignores the environment and returns `True` if the item exists; otherwise, it returns `False`.

**Note:** Related concepts: [Custom lists](https://docs.cloud.google.com/chronicle/docs/soar/reference/custom-lists)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
category | {string} | The category to check if exists | "DenyListed IPs" | N/A  
  
#### Returns

{bool} True if the category exists, False otherwise.

#### Example 1
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.is_existing_category("WhiteListed HOSTs")
    

#### Example 2
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.is_existing_category("SpecialHosts")
    

#### Result behavior

The result in Sample Code 1 returns `True`, and the result in the Sample Code 2 returns `False`.

#### Result value

True or False

### mark_case_as_important
    
    
    mark_case_as_important(case_id, alert_identifier)
    

This function marks the current case with the given alert identifier as important.

**Note:** Related concepts: [Case manipulation](https://docs.cloud.google.com/chronicle/docs/soar/reference/case-manipulation)

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    siemplify.mark_case_as_important(case_id=case_id, alert_identifier=alert_identifier)
    

#### Result behavior

The case with the provided alert identifier is marked as important.

#### Result value

None

### raise_incident
    
    
    raise_incident(case_id, alert_identifier)
    

This function raises the current case with the alert identifier as incident.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | ad6879f1-b72d-419f-990c-011a2526b16d | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    alert_identifier = "ad6879f1-b72d-419f-990c-011a2526b16d"
    case_id = "234"
    siemplify.raise_incident(case_id=case_id, alert_identifier=alert_identifier)
    

#### Result behavior

The case 234 will be raised as an incident.

#### Result value

None

### remove_entities_from_custom_list
    
    
    remove_entities_from_custom_list(custom_list_items)
    

Remove the entities from the custom list with the given category.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
custom_list_items | {[CustomList]} | A list of custom list items | N/A | N/A  
  
#### Returns

{[CustomList]} list of removed `CustomList` objects.

### remove_temp_folder
    
    
    remove_temp_folder()
    

Deletes the temp folder and its subfolders.

#### Parameters

N/A

### _property_ result

### send_system_notification
    
    
    send_system_notification(message, message_id='SDK_CUSTOM_NOTIFICATION')
    

Send system notification with an optional message ID.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
message | {string} | Notification message | N/A | N/A  
message_id | {string} | Notification message identifier | N/A | N/A  
  
### send_system_notification_message
    
    
    send_system_notification_message(message, message_id)
    

#### Example

#### Result behavior

#### Result value

### set_alert_sla
    
    
    set_alert_sla(period_time, period_type, critical_period_time, critical_period_type, case_id, alert_identifier)
    

Sets the SLA of the given `alert_identifier` of `case_id`. SLA being set using this API should surpass all other alert SLA types.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
period_time | {int/str} | Represents the total SLA period | N/A | period_time > 0  
period_type | {str} | Time units of period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
critical_period_time | {int/str} | Represents the critical SLA period | N/A | critical_period_time >= 0  
Critical period (after scaling with its time units)  
should be smaller than the total period  
critical_period_type | {str} | Time units of critical_period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
case_id | {long} | Case identifier | N/A | N/A  
alert_identifier | {str} | Alert identifier | N/A | N/A  
  
### set_case_sla
    
    
    set_case_sla(period_time, period_type, critical_period_time, critical_period_type, case_id)
    

Sets the SLA of the given `case_id`. SLA being set using this API should surpass all other case SLA types.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
period_time | {int/string} | Represents the total SLA period | N/A | period_time > 0  
period_type | {string} | Time units of period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/a  
critical_period_time | {int/string} | Represents the critical SLA period | N/A | critical_period_time >= 0  
Critical period (after scaling with its time units)  
should be smaller than the total period  
critical_period_type | {string} | Time units of critical_period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
case_id | {long} | Case identifier | 234 | N/A  
  
### update_alerts_additional_data
    
    
    update_alerts_additional_data(case_id, alerts_additional_data)
    

Update alerts additional data.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alerts_additional_data | {dict} | Any additional data of the alert | N/A | N/A  
  
### update_entities
    
    
    update_entities(updated_entities)
    

This function updates entities.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
updated_entities | {[{string:string}]} | N/A | N/A | N/A  
  
#### Returns

`NoneType`

#### Result behavior

Using the scope, the selected alert adds new entities if they're not already present.

#### Result value

None

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
