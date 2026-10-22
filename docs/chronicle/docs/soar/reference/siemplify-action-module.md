---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module/
title: SiemplifyAction module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:59:07.926198+00:00
---

# SiemplifyAction module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-action-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SiemplifyAction module

## _class_ `SiemplifyAction.SiemplifyAction`
    
    
    SiemplifyAction.SiemplifyAction(mock_stdin=None, get_source_file=False)
    

Bases: [**Siemplify**](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-module)

### add_alert_entities_to_custom_list
    
    
    add_alert_entities_to_custom_list(category_name)
    

Add the alert's entities to the custom list record with the given category.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
category_name | {string} | Custom list category | "CustomList" | N/A  
  
#### Returns

{[CustomList]} list of the added objects.

#### Example

Input: Explicitly, `category_name`. Implicitly, entities using scope.  
Running `add_alert_entities_to_custom_list` will result in a list of "CustomList" objects and a configuration change in the settings.
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.add_alert_entities_to_custom_list("WhiteListed HOSTs")
    

#### Result behavior

Adds the `WhiteListed HOSTs` category.

#### Result value
    
    
    [<SiemplifyDataModel.CustomList object at 0x0000000003476E10>, <SiemplifyDataModel.CustomList object at 0x0000000003476B00>]
    

### add_attachment
    
    
    add_attachment(file_path, case_id=None, alert_identifier=None, description=None, is_favorite=False)
    

Add an attachment to the case wall.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
file_path | {string} | File path | "C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe" | N/A  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | 12345 | N/A  
description | {string} | The description for the file | N/A | N/A  
is_favorite | boolean | N/A | True/False | N/A  
  
#### Returns

{long} attachment_id

#### Example

Input: Explicitly, File path, description, and `is_favorite`. Implicitly, `case_id` and `alert_identifier`.
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.add_attachment("C:\Program Files (x86)\Google\Chrome\Application\chrome_proxy.exe", case_id="234", alert_identifier=None, description=None, is_favorite=True)
    

#### Result behavior

The file mentioned in the path will be attached to case ID 234 and the attachment ID will be returned.

#### Result value

5 [The attachment ID]

### add_comment
    
    
    add_comment(comment, case_id=None, alert_identifier=None)
    

Add a new comment to a specific case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
comment | {string} | Comment to be added to case wall | N/A | N/A  
case_id | {string} | Case identifier | 234 | If a `case_id` is not provided,  
the current case will be used.   
None by default (optional)  
alert_identifier | {string} | Alert identifier | 12345 | If an `alert_identifier` is not provided,  
the current alert will be used.   
None by default (optional)  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    comment = "Ran some tests on the hash and it seems fine"
    siemplify.add_comment(comment=comment)
    

#### Result behavior

The specified comment is added to the current case.

#### Result value

None

### add_entity_insight
    
    
    add_entity_insight(domain_entity_info, message, triggered_by=None, original_requesting_user=None)
    

Add an entity insight to the case it is being used in.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
domain_entity_info | {DomainEntityInfo} | The entity object that represents an entity to add insight to | N/A | N/A  
message | {string} | Insight message | N/A | N/A  
triggered_by | {string} | Integration name | N/A | If no integration name is provided, the selected integration for the action will be used.  
None by default (optional)  
original_requesting_user | {string} | Requesting user | N/A | None by default (optional)  
  
#### Returns

{boolean} `True` if success. Otherwise, `False`.

#### Example

#### Result behavior

#### Result value

### add_entity_to_case
    
    
    add_entity_to_case(entity_identifier, entity_type, is_internal, is_suspicious, is_enriched, is_vulnerable, properties, case_id=None, alert_identifier=None, environment=None)
    

Add an entity to the current case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
entity_identifier | {string} | Entity identifier | 192.0.2.1, example.com | N/A  
entity_type | {string} | Entity type | "ADDRESS" | N/A  
is_internal | {boolean} | N/A | Internal/External | N/A  
is_suspicious | {boolean} | N/A | Suspicious/Not suspicious | N/A  
is_enriched  | {boolean} | N/A | True/False | False by default  
is_vulnerable | {boolean} | N/A | True/False | False by default  
properties | {dict} | {"Property1":"PropertyValue", "Property2":"PropertyValue2"} | N/A | N/A  
  
#### Returns

`NoneType`

If there is an existing Entity, the following error appears: /

> `500 Server Error: Internal Server Error for url:` `https://localhost:8443/api/external/v1/sdk/CreateEntity?format=snake:` `\"ErrorMessage\":\"Cannot add entity [Identifier:Entities Identifies -` `Type:siemplify.parameters[] to alert [MONITORED MAILBOX` `<EXAMPLE@EXAMPLE.COM>``_633997CB-D23B-4A2B-92F2-AD1D350284FF] in case [12345]` `because the entity already exists >there.\"`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.add_entity_to_case(entity_identifier, entity_type, is_internal, is_suspicious, is_enriched, is_vulnerable, properties, case_id, alert_identifier, environment)
    

#### Result behavior

This function will add a new entity to the case if it is not present in the case.

#### Result value

None

### add_tag
    
    
    add_tag(tag, case_id=None, alert_identifier=None)
    

Add a new tag to a specific case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
tag | {string} | Tag to be added | Any string to be used as a tag | N/A  
case_id | {string} | Case identifier | 12345 | If a `case_id` is not provided,  
then the current case ID will be used.  
None by default (optional)  
alert_identifier | {string} | Alert identifier | 123 | If an `alert_identifier` is not provided,  
then the current alert ID will be used.  
None by default(optional)  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    tag_to_be_added = "MaliciousMail"
    siemplify.add_tag(tag=tag_to_be_added)
    

#### Result behavior

The "MaliciousMail" tag is added to the current case.

#### Result value

None

**Caution:** Do not create tags that are too specific because tags are used in the system to help search and filter cases. Avoid using tags with entity identifiers or any other unique strings.  
Tags created either manually or by an action do not apply to the playbook trigger "By Tag".

### any_alert_entities_in_custom_list
    
    
    any_alert_entities_in_custom_list(category_name)
    

Check if any of the alert's entities has a custom list record with the given category.  
This function gets a category name from CustomLists and returns `True` (Boolean) if any of the entities in the scope is in that category. An entity is considered in the category if its identifier is listed with this category in the settings in the CustomLists table.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
category_name | {string} | The custom list category name | `BlackListed IPs` | N/A  
  
#### Returns

{boolean} `True` if there is an entity in the category, `False` otherwise.

#### Example 1
    
    
    from SiemplifyAction import SiemplifyAction \
    siemplify = SiemplifyAction() \
    result = siemplify.any_entity_in_custom_list("BlackListed IPs")
    

#### Example 2
    
    
    from SiemplifyAction import SiemplifyAction \
    siemplify = SiemplifyAction() \
    result = siemplify.any_entity_in_custom_list("Executive IPs")
    

#### Result behavior

Sample Code 1 result is `True`. Sample Code 2 result is `False`.

#### Result value

True or False

### assign_case
    
    
    assign_case(user, case_id=None, alert_identifier=None)
    

Assign case to user.

This function works with the user ID or user role.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
user | {string} | User ID or user role | USER_ID, Admin, @Tier1 | N/A  
case_id | {string} | Case identifier | 12345 | If a `case_id` is not provided,  
then the current case ID will be used.  
None by default (optional)  
alert_identifier | {string} | Alert identifier | 123 | If an `alert_identifier` is not provided,  
then the current alert ID will be used.  
None by default (optional)  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    assigned_user= "Admin"
    siemplify.assign_case(assigned_user)
    

#### Result behavior

The case gets assigned to the Admin user.

#### Result value

None

### attach_workflow_to_case
    
    
    attach_workflow_to_case(workflow_name, cyber_case_id=None, indicator_identifier=None)
    

Attach a playbook to the current alert.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
workflow_name | {string} | Workflow (playbook) name | N/A | N/A  
cyber_case_id | {string} | Case identifier | 234 | If no case is provided, the current case is used.  
None by default (optional)  
indicator_identifier | {string} | Alert identifier | 12345 | If no alert identifier is provided,  
the current alert is used.  
None by default (optional)  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.attach_workflow_to_case(workflow_name, cyber_case_id, indicator_identifier)
    

#### Result behavior

Attaches the given workflow to the case for the given indicator identifier.

#### Result value

None

### _property_ case

### change_case_priority
    
    
    change_case_priority(priority, case_id=None, alert_identifier=None)
    

Change case priority.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
priority | {int} | Priority represented by each number, respectively, is:  
Low, Medium, High, and Critical | {"Low": 40, "Medium": 60, "High": 80, "Critical": 100} | N/A  
case_id | {string}  | Case identifier | 12345 | If no case is provided, the current case is used  
alert_identifier | {string}  | Alert identifier | 123 | If no alert identifier is provided, the current alert is used  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    priority_to_change_to = 60
    siemplify.change_case_priority(priority=priority_to_change_to )
    

#### Result behavior

The case priority gets changed to "Medium".

#### Result value

None

**Note:** _Case Priority_ is a property of the case. Be mindful when changing it from a playbook or alert perspective.

### change_case_stage
    
    
    change_case_stage(stage, case_id=None, alert_identifier=None)
    

Change case stage

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
stage | {string} | Stage should match exactly the string that is defined in the _case stages_ table | Incident,  
Investigation | N/A  
case_id | {string}  | Case identifier | 12345 | If no case is provided, the current case is used  
alert_identifier | {string}  | Alert identifier | 123 | If no alert identifier is provided, the current alert is used  
  
#### Returns

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    stage_to_change_to = "Investigation"
    siemplify.change_case_stage(stage=stage_to_change_to)
    

#### Result behavior

The case state is changed to "investigation".

#### Result value

None

**Note:** _Case Stage_ is a property of the case. Be mindful when changing it from a playbook or alert perspective.

### close_alert
    
    
    close_alert(root_cause, comment, reason, case_id=None, alert_id=None)
    

Close current alert.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
root_cause | {string} | Close case root cause | A string taken from the "Case close root cause"  
table in the settings | N/A  
comment | {string} | Comment | Any string could be used here | Comment should describe the case,  
but is not restricted  
reason | {ApiSyncAlertCloseReasonEnum} |  | One of three predefined strings available in the dialog  
when done manually: "NotMalicious", "Malicious",  
and "Maintenance" | See [SiemplifyDataModel.ApiSyncAlertCloseReasonEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiSyncAlertCloseReasonEnum)  
  
#### Returns

{dict} result of server operation

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    reason = "Maintenance"
    root_cause = "Employee Error"
    comment = "User accidentally activated a correlation before it was ready to be used and triggered this alert"
    siemplify.close_alert(reason=reason, root_cause=root_cause, comment=comment)
    

#### Result behavior

The current alert is moved to a new case and subsequently closed with the alert.

#### Result value

None

### close_case
    
    
    close_case(root_cause, comment, reason, case_id=None, alert_identifier=None)
    

Close case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
root_cause | {string} | Close case root cause | N/A | N/A  
comment | {string} | Comment | Any string could be used here | Comment should describe the case, but is not restricted  
reason | {ApiSyncAlertCloseReasonEnum} | Close case reason | One of three predefined strings available in the dialog when done manually: "NotMalicious", "Malicious", and "Maintenance" |   
case_id | {string}  | Case identifier | 12345 | If no case is provided, the current case is used  
alert_identifier | {string}  | Alert identifier | 123 | If no alert identifier is provided, the current alert is used  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    reason = "Maintenance"
    root_cause = "Employee Error"
    comment = "User accidentally activated a correlation before it was ready to be used and triggered this alert"
    siemplify.close_case(reason=reason, root_cause=root_cause, comment=comment)
    

#### Result behavior

The case gets closed with the specified reason, root cause and comment.

#### Result value

None

### create_case_insight
    
    
    create_case_insight(triggered_by, title, content, entity_identifier, severity, insight_type, additional_data=None, additional_data_type=None, additional_data_title=None)
    

Add insight to the case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
triggered_by | {string} | Integration name | VirusTotal, XForce | N/A  
title | {string} | Insight title | Enriched by VirusTotal | N/A  
content | {string} | Insight message | Insight Message | N/A  
entity_identifier | {string} | Entity identifier | example.com | N/A  
severity | {int}  | Severity level | 0 = info,  
1 = warning,  
2 = error |   
insight_type | {int} | Insight type | 0 = general,  
1 = entity | N/A  
additional_data | {string} | Additional data for insight | {"checked against": "VT", "malicious": "No"} | N/A  
additional_data_type | {int} | Type of the additional data | 'General'=0,  
'Entity'=1 | N/A  
additional_data_title | {string} | Additional data title for insight | VT check | N/A  
  
#### Returns

{boolean} `True` if success. Otherwise, `False`.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.create_case_insight(triggered_by, title, content, entity_identifier, severity, insight_type, additional_data, additional_data_type, additional_data_title)
    

#### Result behavior

Creates the insight for a case with defined data.   
`True` if case insight is created. Otherwise, `False`.

#### Result value

True or False

### _property_ current_alert

### dismiss_alert
    
    
    dismiss_alert(alert_group_identifier, should_close_case_if_all_alerts_were_dismissed, case_id=None)
    

**Deprecated:** This function is deprecated.

### _property_ environment

### escalate_case
    
    
    escalate_case(comment, case_id=None, alert_identifier=None)
    

Escalate case.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
comment | {string} | Escalate comment | N/A | N/A  
case_id | {string}  | Case identifier | 12345 | N/A  
alert_identifier | {string}  | Alert identifier | 123 | N/A  
  
### extract_action_param
    
    
    extract_action_param(param_name, default_value=None, input_type=<class 'str'>, is_mandatory=False, print_value=False)
    

Get an action script parameter.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
param_name | {string} | Name of the parameter | Any of the parameters names available for the action | N/A  
default_value | {any} | The default value of the parameter | The given value will be returned if the parameter was not set  
(if `is_mandatory` is set to False) | If the parameter is not passed, use this value by default.  
None by default (optional)  
input_type | {obj} | Cast the parameter to a different type | int | str by default (optional)  
is_mandatory | {boolean} | Raise an exception if the parameter is empty | True/False | False by default  
print_value | {boolean} | Print the value to the log | True/False | False by default  
  
#### Returns

The parameter value, {string} by default, unless `input_type` is specified.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    param_value= siemplify.extract_action_param(
     "Threshold",
     default_value=-1,
     input_type=int,
     is_mandatory=False,
     print_value=False)
    

#### Result behavior

The value of the selected parameter will be returned, casted to the selected type.

#### Result value

20

### fetch_and_save_timestamp
    
    
    fetch_and_save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683033493671)
    

Fetch timestamp and save it to case context.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | Format for date/time | True for getting in date time format, False for Unix | False by default (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {int} | The timestamp to save | N/A | Unix epoch time by default (optional)  
  
#### Returns

{int} datetime.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    sa = SiemplifyAction()
    sa.fetch_and_save_timestamp(self, datetime_format=False, new_timestamp=SiemplifyUtils.Unix_now())
    

#### Result behavior

The latest timestamp is fetched and is saved as TIMESTAMP file in the current directory.

#### Result value

`datetime.datetime(2019, 7, 16, 14, 26, 2, 26000)/1563276380`

### fetch_timestamp
    
    
    fetch_timestamp(datetime_format=False, timezone=False)
    

Get the timestamp saved with save_timestamp.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | If True, return timestamp as datetime. Else, return in Unix | True/False | False by default (optional)  
timezone | Parameter not supported anymore  
  
#### Returns

Saved Unix epoch time and datetime.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    sa = SiemplifyAction()
    result = sa.fetch_timestamp(datetime_format=True)
    

#### Result behavior

The latest timestamp is fetched and is saved as TIMESTAMP file in the current directory.

#### Result value

`datetime.datetime(2019, 7, 16, 14, 26, 2, 26000)/1563276380`

### get_alert_context_property
    
    
    get_alert_context_property(property_key)
    

Get context property from current alert.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | The key of the requested property | N/A | N/A  
  
#### Returns

{string} The property value

### get_alerts_ticket_ids_from_cases_closed_since_timestamp
    
    
    get_alerts_ticket_ids_from_cases_closed_since_timestamp(timestamp_unix_ms, rule_generator)
    

Get alerts from cases that were closed since timestamp.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
timestamp_unix_ms | {long} | Timestamp | 1550409785000L | N/A  
rule_generator | {string} | N/A | Phishing email detector | N/A  
  
#### Returns

{[string]} list of alert IDs

### get_attachments
    
    
    get_attachments(case_id=None)
    

Get attachments from a case.   
This function gets a list of custom list items from category and entities list and returns a list of custom list item objects.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | If no case provided, the current case will be used (optional)  
  
#### Returns

{dict} attachments

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.get_attachments(case_id="234")
    

#### Result behavior

A list of dictionaries of attachments will be returned for the case ID 234.

#### Result value

`[{u'is_favorite': False, u'description': u'test', u'type': u'.exe', u'id': 4, u'name': u'chrome_proxy'}]`

### get_case_comments
    
    
    get_case_comments(case_id=None)
    

Get case comments.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | If no case provided, the current case will be used  
  
#### Returns

{[dict]} of case comments

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.get_case_comments(case_id)
    

#### Result behavior

All comments belonging to the case will be fetched.

#### Result value
    
    
    [{'comment': u'this is a comment',
    u'is_deleted': False,
    u'last_editor_full_name': u'example user',
    u'modification_time_unix_time_in_ms_for_client': 0,
    u'creation_time_unix_time_in_ms': 1681904404087, u'id': 12,
    u'modification_time_unix_time_in_ms': 1681904404087,
    u'case_id': 234,
    u'is_favorite': False,
    u'alert_identifier': None,
    u'creator_user_id': u'cd1c112a-0277-44a9-b68d-98ceef9b0399',
    u'last_editor': u'cd1c112a-0277-44a9-b68d-98ceef9b0399',
    u'type': 5,
    u'comment_for_client': None,
    u'creator_full_name': u'example user'}]
    

### get_case_context_property
    
    
    get_case_context_property(property_key)
    

Get a case context property.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | The requested key property | N/A | N/A  
  
#### Returns

{string} the property value

### get_configuration
    
    
    get_configuration(provider, environment=None, integration_instance=None)
    

Get integration configuration.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
provider | {string} | Integration name | VirusTotal |   
environment | {string} | Configuration for specific environment or 'all' |  | Optional.  
If provided, the credentials will be retrieved from the corresponding  
environment configuration. If no environment is specified,  
the case environment is used by default.  
If there is no configuration for the specific environment,  
the default configuration will be returned.  
integration_instance | {string} | The identifier of the integration instance | N/A | N/A  
  
#### Returns

{dict} configuration details

### get_similar_cases
    
    
    get_similar_cases(consider_ports, consider_category_outcome, consider_rule_generator, consider_entity_identifiers, days_to_look_back, case_id=None, end_time_unix_ms=None)
    

Get similar cases.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
consider_ports | {boolean} | Parameter configures whether to use a port filter or not | True/false | N/A  
consider_category_outcome | {boolean} | Parameter configures whether to consider category outcome of the events | True/false | N/A  
consider_rule_generator | {boolean} | Parameter configures whether to consider the rule generator for the alerts | True/false | N/A  
consider_entity_identifiers | {boolean} | Parameter configures whether to consider entity identifiers for the alerts | True/false | N/A  
days_to_look_back | {int} | Parameter configures the number of days prior to look for similar cases | 365 | N/A  
  
#### Returns

{[int]} list of case IDs

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.get_similar_cases(consider_ports=True,
     consider_category_outcome=False,
     consider_rule_generator=False,
     consider_entity_identifiers=False,
     days_to_look_back=30, case_id="234", end_time_unix_ms=None)
    

#### Result behavior

A list of case IDs similar to the case 234 will be returned.

#### Result value

[4, 231]

### get_ticket_ids_for_alerts_dismissed_since_timestamp
    
    
    get_ticket_ids_for_alerts_dismissed_since_timestamp(timestamp_unix_ms)
    

**Warning:** Not supported.

### _property_ is_timeout_reached

### load_case_data
    
    
    load_case_data()
    

This function loads the case data.

#### Parameters

No parameters required.

#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.load_case_data()
    

#### Result behavior

The case data gets loaded.

#### Result value

None

### _property_ log_location

### mark_case_as_important
    
    
    mark_case_as_important(case_id=None, alert_identifier=None)
    

Mark case as important.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | 12345 | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.mark_case_as_important()
    

#### Result behavior

The current case is marked as important.

#### Result value

None

### raise_incident
    
    
    raise_incident(case_id=None, alert_identifier=None)
    

Raise incident.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alert_identifier | {string} | Alert identifier | 12345 | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    siemplify.raise_incident(case_id, alert_identifier)
    

#### Result behavior

The case raised to Incident status.

#### Result value

None

### remove_alert_entities_from_custom_list
    
    
    remove_alert_entities_from_custom_list(category_name)
    

Remove the alert's entities to the custom list record with the given category.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
category_name | {string} | The custom list category | `WhiteListed HOSTs` | N/A  
  
#### Returns

{[CustomList]} list of the removed `CustomList` objects.

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    result = siemplify.remove_alert_entities_from_custom_list("WhiteListed HOSTs")
    

#### Result behavior

The `WhiteListed HOSTS` is removed.

#### Result value
    
    
    [<SiemplifyDataModel.CustomList object at 0x0000000003476E10>,
    <SiemplifyDataModel.CustomList object at 0x0000000003476B00>]
    

### save_timestamp
    
    
    save_timestamp(datetime_format=False, timezone=False, new_timestamp=1683033493671)
    

Save timestamp to current script context.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
datetime_format | {boolean} | N/A | True for datetime format, False for Unix | Default is False (optional)  
timezone | Parameter not supported anymore  
new_timestamp | {long} | Timestamp to save to context | N/A | Timestamp will default to Unix timestamp of calling the method  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    sa = SiemplifyAction()
    sa.save_timestamp(self, datetime_format=False, new_timestamp=SiemplifyUtils.unix_now())
    

#### Result behavior

New timestamp will be saved as TIMESTAMP file in the current directory.

#### Result value

None

### set_alert_context_property
    
    
    set_alert_context_property(property_key, property_value)
    

Set an alert context property by key and value pairs.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | Key of the property to store to context | N/A | N/A  
property_value | {string} | Value of the property to store to context | N/A | N/A  
  
### set_alert_sla
    
    
    set_alert_sla(period_time, period_type, critical_period_time, critical_period_type, case_id=None, alert_id=None)
    

Sets the SLA of the given `alert_identifier` of `case_id`. SLA being set using this API should surpass all other alert SLA types.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
period_time | {int/str} | The total SLA period | N/A | period_time > 0  
period_type | {string} | Time units of period_time, represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
critical_period_time | {int/str} | The critical SLA period | N/A | critical_period_time >= 0  
Critical period (after scaling with its time units)  
should be smaller than the total period.  
critical_period_type | {string} | the time units of critical_period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) |  |   
case_id | {long} | Case identifier | 234 | N/A  
alert_id | {string} | Alert identifier | 12345 | N/A  
  
### set_case_context_property
    
    
    set_case_context_property(property_key, property_value)
    

Set a case context property using the key-value pair.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
property_key | {string} | Key of the property | N/A | N/A  
property_value | {string} | Value of the property | N/A | N/A  
  
### set_case_sla
    
    
    set_case_sla(period_time, period_type, critical_period_time, critical_period_type, case_id=None)
    

Sets the SLA of the given `case_id` if given, otherwise sets the SLA of the current case. SLA being set using this API should surpass all other case SLA types.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
period_time | {int/str} | The total SLA period | N/A | period_time > 0  
period_type | {string} | Time units of period_time, represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
critical_period_time | {int/str} | The critical SLA period | N/A | critical_period_time >0  
Critical period (after scaling with its time units)  
should be smaller than the total period.  
critical_period_type | {string} | the time units of critical_period_time,  
represented by [ApiPeriodTypeEnum](https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module#ApiPeriodTypeEnum) | N/A | N/A  
case_id | {long} | Case identifier | N/A | N/A  
  
### signal_handler
    
    
    signal_handler(sig, frame)
    

### _property_ target_entities

The `target_entities` object is a list of entity objects that the configured action can run against. Each entity object exposes the following properties and methods:

### Entity properties

The following are direct data-holding attributes of an entity object:

Property | Data Type | Description  
---|---|---  
`identifier` | `string` | The unique identifier (UUID) of the entity.  
`creation_time` | `int` | The Unix timestamp of when the entity was created.  
`modification_time` | `int` | The Unix timestamp of when the entity was last modified.  
`additional_properties` | `dict` | A dictionary containing extra details about the entity.  
`case_identifier` | `string` | The ID of the parent case that the entity belongs to.  
`alert_identifier` | `string` | The ID of the alert associated with the entity.  
`entity_type` | `string` | The entity type (for example, 'HOSTNAME', 'USERUNQNAME').  
`is_internal` | `bool` | Indicates if the entity is an internal asset.  
`is_suspicious` | `bool` | Indicates if the entity is flagged as suspicious.  
`is_artifact` | `bool` | Indicates if the entity is an artifact.  
`is_enriched` | `bool` | Indicates if the entity has been enriched.  
`is_vulnerable` | `bool` | Indicates if the entity is flagged as vulnerable.  
`is_pivot` | `bool` | Indicates if the entity is a pivot entity.  
  
### Entity methods

The following are executable functions available on an entity object:

Method | Description  
---|---  
`to_dict()` | Converts the entity object into a standard Python dictionary.  
  
### try_set_alert_context_property
    
    
    try_set_alert_context_property(property_key, property_value)
    

### try_set_case_context_property
    
    
    try_set_case_context_property(property_key, property_value)
    

### update_alerts_additional_data
    
    
    update_alerts_additional_data(alerts_additional_data, case_id=None)
    

Update alerts additional data.

#### Parameters

Param name | Param type | Definition | Possible values | Comments  
---|---|---|---|---  
case_id | {string} | Case identifier | 234 | N/A  
alerts_additional_data | {string:string} | N/A | N/A | N/A  
  
#### Returns

`NoneType`

#### Example
    
    
    from SiemplifyAction import SiemplifyAction
    siemplify = SiemplifyAction()
    additional_data = {"testKey":"testValue"}
    siemplify.update_alerts_additional_data(alerts_additional_data=additional_data, case_id=caseid)
    

#### Result behavior

Updates the alert with additional data, such as `testKey:testValue`.

#### Result value

None

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
