---
url: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module/
title: SiemplifyDataModel module \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:09.393248+00:00
---

# SiemplifyDataModel module  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/reference/siemplify-data-model-module/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SiemplifyDataModel module

### class SiemplifyDataModel.ActionLogRecord
    
    
    class SiemplifyDataModel.ActionLogRecord(record_type, message, original_source_file_name=None, case_id=None, alert_id=None, workflow_id=None, environment=None, source_system_name=None, exception_message=None, integration=None, action_definition_name=None, timestamp=None)
    

Bases: object

### class SiemplifyDataModel.Alert
    
    
    class SiemplifyDataModel.Alert(identifier, alert_group_identifier, creation_time, modification_time, case_identifier, reporting_vendor, reporting_product, environment, name, description, external_id, severity, rule_generator, tags, detected_time, security_events, domain_relations, domain_entities, additional_properties, additional_data)
    

Bases: AlertInfo

#### get_alert_start_time(creation_time, security_events)

#### _static_ get_prop_if_exists(dictionary, prop_name, default_value)

### class SiemplifyDataModel.AlertInfo
    
    
    class SiemplifyDataModel.AlertInfo(identifier, alert_group_identifier, creation_time, modification_time, case_identifier, reporting_vendor, reporting_product, environment, name, description, external_id, severity, rule_generator, tags, detected_time, additional_properties, additional_data)
    

Bases: Base

### class SiemplifyDataModel.ApiPeriodTypeEnum
    
    
    class SiemplifyDataModel.ApiPeriodTypeEnum
    

Bases: object   
This object represents the time units of an SLA period.

`DAYS= 'Days'`

`HOURS= 'Hours'`

`MINUTES= 'Minutes'`

#### _classmethod_ validate(value)

#### _classmethod_ values()

### class SiemplifyDataModel.ApiSyncAlertCloseReasonEnum
    
    
    class SiemplifyDataModel.ApiSyncAlertCloseReasonEnum
    

Bases: object

`INCONCLUSIVE= 3`

`MAINTENANCE= 2`

`MALICIOUS= 0`

`NOT_MALICIOUS= 1`

`UNKNOWN= 4`

### class SiemplifyDataModel.ApiSyncAlertPriorityEnum
    
    
    class SiemplifyDataModel.ApiSyncAlertPriorityEnum
    

Bases: object

`CRITICAL= 5`

`HIGH= 4`

`INFORMATIVE= 0`

`LOW= 2`

`MEDIUM= 3`

`UNCHANGED= 1`

### class SiemplifyDataModel.ApiSyncAlertStatusEnum
    
    
    class SiemplifyDataModel.ApiSyncAlertStatusEnum
    

Bases: object

`CLOSED= 1`

`OPENED= 0`

### class SiemplifyDataModel.ApiSyncAlertUsefulnessEnum
    
    
    class SiemplifyDataModel.ApiSyncAlertUsefulnessEnum
    

Bases: object

`NONE= 0`

`NOT_USEFUL= 1`

`USEFUL= 2`

### class SiemplifyDataModel.ApiSyncCasePriorityEnum
    
    
    class SiemplifyDataModel.ApiSyncCasePriorityEnum
    

Bases: object

`CRITICAL= 5`

`HIGH= 4`

`INFORMATIVE= 0`

`LOW= 2`

`MEDIUM= 3`

`UNCHANGED= 1`

### class SiemplifyDataModel.ApiSyncCaseStatusEnum
    
    
    class SiemplifyDataModel.ApiSyncCaseStatusEnum
    

Bases: object

`ALL= 2`

`CLOSED= 1`

`CREATION_PENDING= 4`

`MERGED= 3`

`OPENED= 0`

### class SiemplifyDataModel.Attachment
    
    
    class SiemplifyDataModel.Attachment(case_identifier, alert_identifier, base64_blob, attachment_type, name, description, is_favorite, orig_size, size)
    

Bases: Base

#### _static_ fromfile(path, case_id=None, alert_identifier=None, description=None, is_favorite=False)

#### _property_ is_identifier_mandatory

### class SiemplifyDataModel.Base
    
    
    class SiemplifyDataModel.Base(identifier, creation_time=None, modification_time=None, additional_properties=None)
    

Bases: object

#### _property_ is_identifier_mandatory

### class SiemplifyDataModel.CaseFilterOperatorEnum
    
    
    class SiemplifyDataModel.CaseFilterOperatorEnum
    

Bases: object

`AND= 'AND'`

`OR= 'OR'`

### class SiemplifyDataModel.CaseFilterSortByEnum
    
    
    class SiemplifyDataModel.CaseFilterSortByEnum
    

Bases: object

`CLOSE_TIME= 'CLOSE_TIME'`

`START_TIME= 'START_TIME'`

`UPDATE_TIME= 'UPDATE_TIME'`

### class SiemplifyDataModel.CaseFilterSortOrderEnum
    
    
    class SiemplifyDataModel.CaseFilterSortOrderEnum
    

Bases: object

`ASC= 'ASC'`

`DESC= 'DESC'`

### class SiemplifyDataModel.CaseFilterStatusEnum
    
    
    class SiemplifyDataModel.CaseFilterStatusEnum
    

Bases: object

`BOTH= 'BOTH'`

`CLOSE= 'CLOSE'`

`OPEN= 'OPEN'`

### class SiemplifyDataModel.CaseFilterValue
    
    
    class SiemplifyDataModel.CaseFilterValue(value, title)
    

Bases: object

### class SiemplifyDataModel.CaseStatus
    
    
    class SiemplifyDataModel.CaseStatus
    

Bases: object

`CLOSE= 'CLOSE'`

`OPEN= 'OPEN'`

### class SiemplifyDataModel.CasesFilter
    
    
    class SiemplifyDataModel.CasesFilter(environments=None, analysts=None, statuses=None, case_names=None, tags=None, priorities=None, stages=None, case_types=None, products=None, networks=None, ticked_ids_free_search='', case_ids_free_search='', wall_data_free_search='', entities_free_search='', start_time_unix_time_in_ms=-1, end_time_unix_time_in_ms=-1)
    

Bases: object

### class SiemplifyDataModel.ConnectorLogRecord
    
    
    class SiemplifyDataModel.ConnectorLogRecord(record_type, message, connector_identifier, result_data_type, original_source_file_name=None, result_package_items_count=None, environment=None, source_system_name=None, exception_message=None, integration=None, connector_definition_name=None, timestamp=None)
    

Bases: object

### class SiemplifyDataModel.CustomList
    
    
    class SiemplifyDataModel.CustomList(identifier, category, environment)
    

Bases: Base

#### _property_ is_identifier_mandatory

### class SiemplifyDataModel.CyberCase
    
    
    class SiemplifyDataModel.CyberCase(identifier, creation_time, modification_time, alert_count, priority, is_touched, is_merged, is_important, environment, assigned_user, title, description, status, is_incident, stage, has_suspicious_entity, high_risk_products, is_locked, has_workflow, sla_expiration_unix_time, cyber_alerts, additional_properties)
    

Bases: CyberCaseInfo

### class SiemplifyDataModel.CyberCaseInfo
    
    
    class SiemplifyDataModel.CyberCaseInfo(identifier, creation_time, modification_time, alert_count, priority, is_touched, is_merged, is_important, assigned_user, title, description, status, environment, is_incident, stage, has_suspicious_entity, high_risk_products, is_locked, has_workflow, sla_expiration_unix_time, additional_properties)
    

Bases: Base

### class SiemplifyDataModel.DomainEntityInfo
    
    
    class SiemplifyDataModel.DomainEntityInfo(identifier, creation_time, modification_time, case_identifier, alert_identifier, entity_type, is_internal, is_suspicious, is_artifact, is_enriched, is_vulnerable, is_pivot, additional_properties)
    

Bases: Base

#### to_dict()

### class SiemplifyDataModel.DomainRelationInfo
    
    
    class SiemplifyDataModel.DomainRelationInfo(identifier, creation_time, modification_time, case_identifier, alert_identifier, security_event_identifier, relation_type, event_id, from_identifier, to_identifier, device_product, device_vendor, event_class_id, severity, start_time, end_time, destination_port, category_outcome, additional_properties, to_type=None, from_type=None)
    

Bases: Base

### class SiemplifyDataModel.EntityTypes
    
    
    class SiemplifyDataModel.EntityTypes
    

Bases: object

`ADDRESS= 'ADDRESS'`

`ALERT= 'ALERT'`

`APPLICATION= 'APPLICATION'`

`CHILDHASH= 'CHILDHASH'`

`CHILDPROCESS= 'CHILDPROCESS'`

`CLUSTER= 'CLUSTER'`

`CONTAINER= 'CONTAINER'`

`CREDITCARD= 'CREDITCARD'`

`CVE= 'CVE'`

`CVEID= 'CVEID'`

`DATABASE= 'DATABASE'`

`DEPLOYMENT= 'DEPLOYMENT'`

`DESTINATIONDOMAIN= 'DESTINATIONDOMAIN'`

`DOMAIN= 'DOMAIN'`

`EMAILMESSAGE= 'EMAILSUBJECT'`

`EVENT= 'EVENT'`

`FILEHASH= 'FILEHASH'`

`FILENAME= 'FILENAME'`

`GENERIC= 'GENERICENTITY'`

`HOSTNAME= 'HOSTNAME'`

`IPSET= 'IPSET'`

`MACADDRESS= 'MacAddress'`

`PARENTHASH= 'PARENTHASH'`

`PARENTPROCESS= 'PARENTPROCESS'`

`PHONENUMBER= 'PHONENUMBER'`

`POD= 'POD'`

`PROCESS= 'PROCESS'`

`SERVICE= 'SERVICE'`

`SOURCEDOMAIN= 'SOURCEDOMAIN'`

`THREATACTOR= 'THREATACTOR'`

`THREATCAMPAIGN= 'THREATCAMPAIGN'`

`THREATSIGNATURE= 'THREATSIGNATURE'`

`URL= 'DestinationURL'`

`USB= 'USB'`

`USER= 'USERUNIQNAME'`

### class SiemplifyDataModel.InsightSeverity
    
    
    class SiemplifyDataModel.InsightSeverity
    

Bases: object

`ERROR= 2`

`INFO= 0`

`WARN= 1`

### class SiemplifyDataModel.InsightType
    
    
    class SiemplifyDataModel.InsightType
    

Bases: object

`Entity= 1`

`General= 0`

### class SiemplifyDataModel.LogRecordTypeEnum
    
    
    class SiemplifyDataModel.LogRecordTypeEnum
    

Bases: object

`ERROR= 1`

`INFO= 0`

`KEEP_ALIVE= 2`

### class SiemplifyDataModel.LogRow
    
    
    class SiemplifyDataModel.LogRow(message, log_level, timestamp)
    

Bases: object

### class SiemplifyDataModel.SecurityEventInfo
    
    
    class SiemplifyDataModel.SecurityEventInfo(identifier=None, creation_time=None, modification_time=None, case_identifier=None, alert_identifier=None, name=None, description=None, event_id=None, device_severity=None, device_product=None, device_vendor=None, device_version=None, event_class_id=None, severity=None, start_time=None, end_time=None, event_type=None, rule_generator=None, is_correlation=None, device_host_name=None, device_address=None, source_dns_domain=None, source_nt_domain=None, source_host_name=None, source_address=None, source_user_name=None, source_user_id=None, source_process_name=None, destination_dns_domain=None, destination_nt_domain=None, destination_host_name=None, destination_address=None, destination_user_name=None, destination_url=None, destination_port=None, destination_process_name=None, file_name=None, file_hash=None, file_type=None, email_subject=None, usb=None, application_protocol=None, transport_protocol=None, category_outcome=None, signature=None, deployment=None, additional_properties=None, threat_actor=None, source_mac_address=None, destination_mac_address=None, credit_card=None, phone_number=None, cve=None, threat_campaign=None, generic_entity=None, process=None, parent_process=None, parent_hash=None, child_process=None, child_hash=None, source_domain=None, destination_domain=None, ipset=None, cluster=None, application=None, database=None, pod=None, container=None, service=None)
    

Bases: Base

#### _property_ is_identifier_mandatory

### class SiemplifyDataModel.SyncAlert
    
    
    class SiemplifyDataModel.SyncAlert(alert_group_id, alert_id, case_id, environment, priority, status, ticket_id, creation_time, close_comment, close_reason, close_root_cause, close_usefulness)
    

Bases: object

### class SiemplifyDataModel.SyncAlertMetadata
    
    
    class SiemplifyDataModel.SyncAlertMetadata(alert_group_id, tracking_time)
    

Bases: object

### class SiemplifyDataModel.SyncCase
    
    
    class SiemplifyDataModel.SyncCase(case_id, environment, priority, stage, status, external_case_id, title)
    

Bases: object

### class SiemplifyDataModel.SyncCaseIdMatch
    
    
    class SiemplifyDataModel.SyncCaseIdMatch(case_id, external_case_id)
    

Bases: object  
This object represents a matching between a Siemplify internal case ID and an external case ID in an external system.

### class SiemplifyDataModel.SyncCaseMetadata
    
    
    class SiemplifyDataModel.SyncCaseMetadata(case_id, tracking_time)
    

Bases: object

### class SiemplifyDataModel.Task
    
    
    class SiemplifyDataModel.Task(case_id, content, creator_user_id, due_date_unix_time_ms=None, is_important=False, is_favorite=False, owner_comment=None, priority=0, owner=None, status=0, completion_comment=None, completion_date_time_unix_time_in_ms=None, alert_identifier=None, id=0, title=None, creator_full_name=None, owner_full_name=None, creation_time_unix_time_in_ms=0, modification_time_unix_time_in_ms=0, last_modifier=None, last_modifier_full_name=None, completor=None, completor_full_name=None)
    

Bases: Base

#### _property_ is_identifier_mandatory

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
