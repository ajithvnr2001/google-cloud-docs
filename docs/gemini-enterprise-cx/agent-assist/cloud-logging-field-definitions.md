---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/cloud-logging-field-definitions/
title: Cloud Logging field definitions \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:00.620967+00:00
---

# Cloud Logging field definitions  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/cloud-logging-field-definitions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Cloud Logging field definitions Stay organized with collections  Save and categorize content based on your preferences. 

After you enable Cloud Audit Logs, the Google Cloud console logging explorer records the contents of the following categories:

  * AuditLog proto
  * API-level log



## Enable and view

Cloud Audit Logs allow you to view administrative activities and permissions within Google Cloud resources.

### Enable logging

Follow these steps to enable the logs.

  1. Navigate to the Google Cloud console, select **IAM & Admin** > **Audit Logs**.
  2. Enter the `Dialogflow API` filter for **Data access audit logs configuration** , and select the following API types: **Admin read** , **Data read** , and **Data write**.

**Note:** To enable logging for either all or no methods in a category, you configure logging by data access type, not individual method.

### View logs

You must acquire the _project owner_ and _private logs viewer_ [IAM roles](https://docs.cloud.google.com/iam/docs/roles-overview), then follow these steps to view the logs.

  1. Navigate to the Google Cloud console, then select **Logging** > **Logs Explorer**.
  2. Optional: In Logs Explorer, add a filter or adjust the timeline as preferred.
  3. Select an entry to view details.

**Note:** Many fields in the request or response body are logged, but not all. Engineering annotates the RPC definition to indicate the fields to expose for logging. For example, the `protoPayload` filter exposes the JSON object with the audit log entry.

## The logging proto

Each log entry will be an instance of the `AuditLog proto`, which contains the following fields:

Field Type | Field Name  
---|---  
string | service_name  
string | method_name  
string | resource_name  
ResourceLocation | resource_location  


  * current_locations
  * original_locations

  
google.protobuf.Struct | resource_original_state  
int64 | num_response_items  
google.rpc.Status | status  
AuthenticationInfo | authentication_info  


  * principal_email
  * principal
  * authority_selector
  * third_party_principal
  * service_account_key_name
  * service_account_delegation_info
  * service_account_delegation_session_id
  * principal_subject
  * service_delegation_history

  
repeated AuthorizationInfo | authorization_info  


  * authorization_logging_options
  * resource_attributes
  * admin_access_control_authorization_info
  * permission_type  

    * ADMIN_READ
    * ADMIN_WRITE
    * DATA_READ
    * DATA_WRITE
  * impersonation_peer_borg_role

  
PolicyViolationInfo | policy_violation_info  
repeated PolicyViolationInfo | policy_violations  
RequestMetadata | request_metadata  


  * caller_ip
  * caller_supplied_user_agent
  * caller_network
  * caller_location
  * caller_region_code
  * caller_internal_gce_vnid
  * caller_gce_network_project_number
  * caller_is_gce_client
  * request_attributes
  * destination_attributes

  
google.protobuf.Struct | request  
google.protobuf.Struct | response  
google.protobuf.Struct | metadata  
bytes | audit_loggable_mint  
bytes | loggable_ubermint  
bytes | audit_loggable_service_control_token  
Redaction | redactions  


  * type 
    * CLEARED
    * REPLACED
    * FAILED_TO_PROVIDE
    * NOT_REQUIRED
    * PARTIAL
  * field
  * reason

  
  
Depending on the enabled Cloud Audit Logs fields, the log explorer populates the API's request and response bodies into the request and response fields of the logging proto.

## API-level logged fields

API | Logged field  
---|---  
AnalyzeContent | Request  


  * participant

  
StreamingAnalyzeContent | Request  


  * participant

| Response  


  * speech_model

  
CreateConversation | Request  


  * parent
  * conversation 
    * conversation_profile

| Response  


  * conversation_profile
  * lifecycle_state
  * name
  * start_time

  
CreateParticipant | Request  


  * parent
  * participant 
    * role

| Response  


  * name
  * role

  
SuggestConversationSummary | Request  


  * conversation

| Response  


  * latest_message
  * answer_record

  
SearchKnowledge | Request  


  * parent
  * conversation_profile
  * conversation
  * latest_message

| Response  


  * answer_record

  
SuggestKnowledgeAssist | Request  


  * parent
  * latest_message

| Response  


  * latest_message
  * answer_record

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
