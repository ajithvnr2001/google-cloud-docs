---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-json-schema/
title: Raw data export JSON schema and data types \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:25.019942+00:00
---

# Raw data export JSON schema and data types  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-json-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Raw data export JSON schema and data types Stay organized with collections  Save and categorize content based on your preferences. 

This page contains the Contact Center AI Platform raw data export JSON schema and data types. For more information, see [Raw data export dictionary](https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-dictionary).

## calls
    
    
    {
        "id": "bigint",
        "agent_id": "int",
        "answer_type": "int",
        "assigned_at": "datetime",
        "auto_answered": "tinyint",
        "connected_at": "datetime",
        "created_at": "datetime",
        "deflection": "int",
        "disconnected_by": "int",
        "end_user_id": "int",
        "ends_at": "datetime",
        "fail_details": "varchar",
        "fail_reason": "int",
        "finish_reason": "int",
        "in_queue_priority": "int",
        "lang": "varchar",
        "materialized_menu_path": "varchar",
        "materialized_menu_path_name": "varchar",
        "menu_id": "int",
        "menu_path_id": "int",
        "menu_type": "varchar",
        "out_ticket_id_ext": "varchar",
        "parent_id": "bigint",
        "queue_priority_level": "int",
        "rating": "float",
        "recording_permission": "int",
        "repeated": "tinyint",
        "scheduled_at": "datetime",
        "session_id": "int",
        "smart_action_enabled": "tinyint",
        "status": "int",
        "support_number": "varchar",
        "transfer_count": "int",
        "type": "varchar",
        "voicemail_reason": "int",
        "answered_by": "int"
      }
    

## call_participants
    
    
    {
        "id": "bigint",
        "call_id": "bigint",
        "client_muted": "tinyint",
        "connected_at": "datetime",
        "created_at": "datetime",
        "end_user_id": "int",
        "ended_at": "datetime",
        "hold": "tinyint",
        "lang": "varchar",
        "menu_path_id": "int",
        "phone_number": "varchar",
        "status": "int",
        "transfer_id": "int",
        "type": "int",
        "user_id": "int",
        "placed_hold": "tinyint",
        "virtual_agent_id": "int"
      }
    

## call_recordings
    
    
    {
        "id": "int",
        "call_id": "bigint",
        "conference_sid": "varchar",
        "created_at": "datetime",
        "duration": "int",
        "extra": "text",
        "recording_type": "int",
        "redaction_times": "text",
        "s3_path": "varchar",
        "started_at": "datetime",
        "updated_at": "datetime",
        "url": "text",
        "voip_store": "varchar",
        "recording_sid": "varchar"
      }
    

## chat_participants
    
    
    {
        "id": "int",
        "chat_id": "int",
        "connected_at": "datetime",
        "created_at": "datetime",
        "end_user_id": "int",
        "finished_at": "datetime",
        "lang": "varchar",
        "menu_path_id": "int",
        "status": "int",
        "transfer_id": "int",
        "type": "int",
        "user_id": "int",
        "virtual_agent_id": "int"
      }
    

## chats
    
    
    {
        "id": "int",
        "agent_id": "int",
        "assigned_at": "datetime",
        "canceled_at": "datetime",
        "created_at": "datetime",
        "device_id": "int",
        "disconnected_by": "int",
        "dismissed_count": "int",
        "end_user_id": "int",
        "ends_at": "datetime",
        "fail_reason": "int",
        "finish_reason": "int",
        "first_msg_sent_at": "datetime",
        "in_queue_priority": "int",
        "lang": "varchar",
        "last_agent_msg_sent_at": "datetime",
        "last_end_user_msg_sent_at": "datetime",
        "last_msg_sent_at": "datetime",
        "materialized_menu_path": "varchar",
        "materialized_menu_path_name": "varchar",
        "menu_id": "int",
        "menu_path_id": "int",
        "out_ticket_id": "varchar",
        "out_ticket_url": "varchar",
        "rating": "float",
        "repeated": "tinyint",
        "status": "int",
        "timeout_at": "datetime",
        "transcript_sent": "tinyint",
        "type": "int",
        "verifiable": "tinyint",
        "verified": "tinyint",
        "auto_answered": "tinyint",
        "answer_type": "int",
        "after_hours": "tinyint"
      }
    

## comm_escalations
    
    
    {
        "id": "int",
        "comm_id": "bigint",
        "comm_type": "varchar",
        "escalated_at": "datetime",
        "from_virtual_agent_id": "int",
        "reason": "int",
        "status": "int",
        "to_agent_id": "int",
        "created_at": "datetime",
        "updated_at": "datetime",
        "deflection": "int",
        "sentiment": "int",
        "to_menu_id": "int",
        "to_menu_lang": "varchar",
        "escalation_type": "tinyint",
        "destination": "varchar",
        "to_menu_path_id": "int",
        "queued_at": "datetime",
        "menu_selection_offered": "tinyint",
        "agent_type": "tinyint",
        "to_virtual_agent_id": "int",
        "from_lang": "varchar",
        "from_menu_id": "int",
        "from_menu_path_id": "int",
        "preserve_va": "tinyint"
      }
    

## comm_transfers
    
    
    {
        "id": "int",
        "answer_type_path": "int",
        "assigned_at": "datetime",
        "cold": "tinyint",
        "comm_type": "varchar",
        "connected_at": "datetime",
        "created_at": "datetime",
        "current": "tinyint",
        "deflection": "int",
        "fail_reason": "int",
        "from_agent_id": "int",
        "from_menu_path_id": "int",
        "from_queue_priority_level": "int",
        "queue_priority_level": "int",
        "session_id": "int",
        "status": "int",
        "to_agent_id": "int",
        "to_menu_path_id": "int",
        "updated_at": "datetime",
        "to_virtual_agent_id": "int",
        "to_lang": "varchar",
        "from_lang": "varchar",
        "comm_id": "int"
      }
    

## company_locations
    
    
    {
        "id": "int",
        "created_at": "datetime",
        "lang": "varchar",
        "location": "varchar",
        "updated_at": "datetime",
        "pop_settings": "text"
      }
    

## dcr_call_pick_requests
    
    
    {
        "id": "bigint",
        "call_uuid": "varbinary",
        "call_routing_id": "bigint",
        "receiving_queue_id": "bigint",
        "available_agent_count": "int",
        "longest_waiting_time": "int",
        "created_at": "datetime"
      }
    

## dcr_call_routings
    
    
    {
        "id": "bigint",
        "call_uuid": "varbinary",
        "status": "int",
        "assigned_pick_request_id": "bigint",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    

## dcr_endpoint_bulk_verifications
    
    
    {
        "id": "bigint",
        "success_ids": "text",
        "failed_ids": "text",
        "job_id": "int",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    

## dcr_endpoints
    
    
    {
        "id": "bigint",
        "domain": "varchar",
        "verified": "tinyint",
        "deleted_at": "datetime",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    

## dcr_expansion_queue_assignments
    
    
    {
        "id": "bigint",
        "created_at": "datetime",
        "updated_at": "datetime",
        "menu_setting_id": "int",
        "dcr_receiving_queue_id": "bigint",
        "enabled": "tinyint"
      }
    

## dcr_external_calls
    
    
    {
        "id": "bigint",
        "call_uuid": "varbinary",
        "status": "int",
        "menu_id": "int",
        "menu_type": "varchar",
        "lang": "varchar",
        "origin_callback_url": "varchar",
        "created_at": "datetime",
        "updated_at": "datetime",
        "voip_provider": "varchar"
      }
    

## dcr_queue_assignments
    
    
    {
        "id": "bigint",
        "menu_setting_id": "bigint",
        "receiving_queue_id": "bigint",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    

## dcr_receiving_queues
    
    
    {
        "id": "bigint",
        "dcr_endpoint_id": "bigint",
        "menu_id": "int",
        "menu_type": "varchar",
        "name": "varchar",
        "deleted_at": "datetime",
        "created_at": "datetime",
        "updated_at": "datetime"
      }
    

## deflection_history_logs
    
    
    {
        "id": "int",
        "call_id": "bigint",
        "created_at": "datetime",
        "deflection": "int",
        "details": "text",
        "from_lang": "varchar",
        "from_materialized_menu_path": "varchar",
        "from_materialized_menu_path_name": "varchar",
        "from_menu_path_id": "int",
        "to_lang": "varchar",
        "to_materialized_menu_path": "varchar",
        "to_materialized_menu_path_name": "varchar",
        "to_menu_path_id": "int",
        "transfer_id": "int"
      }
    

## deflection_sip_uris
    
    
    {
        "id": "int",
        "uri": "text"
      }
    

## deflection_urls
    
    
    {
        "id": "int",
        "url": "text"
      }
    

## disposition_agent_inputs
    
    
    {
        "id": "bigint",
        "comm_id": "bigint",
        "comm_type": "varchar",
        "user_id": "int",
        "participant_id": "bigint",
        "transfer_id": "int",
        "code_id": "int",
        "crm_reference_id": "varchar",
        "created_at": "datetime",
        "updated_at": "datetime",
        "menu_path_id": "int",
        "lang": "varchar"
      }
    

## disposition_codes
    
    
    {
        "id": "int",
        "name": "varchar",
        "deleted_at": "datetime",
        "created_at": "datetime",
        "updated_at": "datetime",
        "enabled": "tinyint"
      }
    

## email_accounts
    
    
    {
        "id": "bigint",
        "email_service": "varchar",
        "incoming_server_host": "varchar",
        "incoming_server_port": "int",
        "sender_server_host": "varchar",
        "sender_server_port": "int",
        "has_folder": "tinyint",
        "email_id": "varchar",
        "status": "varchar",
        "imap_sync_info": "json",
        "created_at": "datetime",
        "updated_at": "datetime",
        "deleted_at": "datetime",
        "oauth_linked": "tinyint"
      }
    

## email_supports
    
    
    {
        "id": "bigint",
        "agent_id": "int",
        "session_id": "int",
        "email_account_id": "int",
        "priority": "tinyint",
        "end_user_id": "int",
        "out_ticket_id": "varchar",
        "out_ticket_url": "varchar",
        "latest_email_thread_id": "int",
        "transfer_count": "int",
        "total_thread_numbers": "int",
        "in_queue_priority": "int",
        "menu_id": "int",
        "menu_path_id": "int",
        "menu_type": "varchar",
        "lang": "varchar",
        "status": "int",
        "finished_at": "datetime",
        "queue_priority_level": "int",
        "user_priority": "int",
        "created_at": "datetime",
        "updated_at": "datetime",
        "materialized_menu_path": "varchar",
        "materialized_menu_path_name": "varchar",
        "is_out_ticket_account": "tinyint"
      }
    

## end_user_activity_logs
    
    
    {
        "id": "bigint",
        "end_user_id": "int",
        "activity": "int",
        "created_at": "datetime",
        "lang": "varchar",
        "menu_type": "int",
        "menu_path_id": "int",
        "materialized_menu_path": "varchar",
        "materialized_menu_path_name": "varchar",
        "call_id": "bigint",
        "chat_id": "int",
        "transfer_id": "int",
        "to_url_id": "int",
        "to_email": "varchar",
        "to_menu_type": "int",
        "to_menu_path_id": "int",
        "to_materialized_menu_path": "varchar",
        "to_materialized_menu_path_name": "varchar",
        "to_phone_number": "varchar",
        "to_sip_uri_id": "int"
      }
    

## end_users
    
    
    {
        "id": "int",
        "created_at": "datetime",
        "identifier": "varchar",
        "need_assignment": "tinyint",
        "out_contact_id": "varchar",
        "out_contact_type": "int",
        "to_be_deleted": "tinyint",
        "updated_at": "datetime"
      }
    

## menu_channel_assignments
    
    
    {
        "assignee_id": "int",
        "assignee_type": "varchar",
        "channel_type": "int",
        "group_id": "int",
        "lang": "varchar",
        "menu_id": "int"
      }
    

## menu_path_items
    
    
    {
        "id": "int",
        "menu_id": "int",
        "path_id": "int",
        "position": "int"
      }
    

## menu_paths
    
    
    {
        "id": "int",
        "items_count": "int",
        "materialized_path": "varchar",
        "name": "varchar"
      }
    

## menu_queue_groups
    
    
    {
        "id": "int",
        "channel": "int",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "group_level": "int",
        "lang": "varchar",
        "menu_id": "int",
        "percent": "int",
        "routing_algorithm": "int"
      }
    

## menu_settings
    
    
    {
        "id": "int",
        "after_hours": "text",
        "auto_answer_enabled": "tinyint",
        "collect_email_for_call": "tinyint",
        "collect_email_for_chat": "tinyint",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "dcr_enabled": "tinyint",
        "dcr_failover_menu_id": "int",
        "dcr_failover_menu_lang": "varchar",
        "dcr_queue_type": "int",
        "enabled": "tinyint",
        "enabled_self": "tinyint",
        "hidden": "tinyint",
        "lang": "varchar",
        "menu_id": "int",
        "name": "varchar",
        "output_msg": "varchar",
        "over_cap_deflection": "text",
        "redaction_enabled": "tinyint",
        "redirection": "text",
        "redirection_v2": "text",
        "return_to_queue": "text",
        "sms_smart_action_enabled": "tinyint",
        "updated_at": "datetime",
        "use_queue_priority": "tinyint",
        "use_voice_file": "tinyint",
        "voice_file": "varchar",
        "wait_time_sms": "text",
        "wait_time_sms_enabled": "tinyint",
        "sms": "text"
      }
    

## menus
    
    
    {
        "id": "int",
        "children_count": "int",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "hidden": "tinyint",
        "name": "varchar",
        "output_msg": "text",
        "parent_id": "int",
        "position": "int",
        "type": "varchar",
        "updated_at": "datetime"
      }
    

## native_campaigns
    
    
    {
        "id": "int",
        "queue_id": "int",
        "mode": "int",
        "name": "varchar",
        "starts_at": "datetime",
        "ends_at": "datetime",
        "status": "int",
        "target_number_to_process": "int",
        "ringing_timeout": "int",
        "overdial_adjustment_multiplier": "int",
        "max_abandonment_percent": "int",
        "abandoned_by_dialer_audio_setting": "text",
        "redial_interval_minutes": "int",
        "max_redial_count": "int",
        "campaign_type": "int",
        "external_campaign_id": "varchar",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "updated_at": "datetime",
        "lang": "varchar"
      }
    

## perf_call_campaign_contact_details
    
    
    {
        "id": "int",
        "call_id": "bigint",
        "session_id": "int",
        "event_id": "int",
        "campaign_id": "int",
        "contact_id": "int",
        "status": "int",
        "redial_attempts": "int",
        "active_talk_duration": "int",
        "abandoned_call_message_played_at": "datetime",
        "speak_started_at": "datetime",
        "speak_ended_at": "datetime",
        "ended_at": "datetime",
        "connected_at": "datetime",
        "dialed_at": "datetime",
        "created_at": "datetime"
      }
    

## perf_call_cobrowse_details
    
    
    {
        "id": "int",
        "agent_id": "int",
        "menu_path_id": "int",
        "lang": "varchar",
        "call_id": "bigint",
        "session_id": "int",
        "started_by": "int",
        "ended_by": "int",
        "started_at": "datetime",
        "ended_at": "datetime",
        "remote_controlled": "tinyint",
        "device_name": "varchar"
      }
    

## perf_call_handle_durations
    
    
    {
        "id": "int",
        "acw_duration": "int",
        "agent_id": "int",
        "call_duration": "int",
        "call_id": "bigint",
        "call_type": "varchar",
        "ended_at": "datetime",
        "event": "int",
        "inbound": "tinyint",
        "lang": "varchar",
        "menu_path_id": "int",
        "origin_call_id": "bigint",
        "started_at": "datetime",
        "transfer": "tinyint",
        "transfer_cold": "tinyint",
        "transfer_id": "int",
        "hold_duration": "int",
        "end_user_id": "int",
        "session_id": "int",
        "scheduled_at": "datetime",
        "wait_duration": "int",
        "bcw_duration": "int",
        "barged": "tinyint",
        "campaign_mode": "int",
        "network_quality_score": "int",
        "breakthrough_projection": "tinyint",
        "status_id_before_breakthrough": "int"
      }
    

## perf_call_presession_deflections
    
    
    {
        "id": "bigint",
        "event_id": "int",
        "call_id": "bigint",
        "call_menu_path_id": "int",
        "call_lang": "varchar",
        "to_comm_id": "int",
        "to_comm_type": "varchar",
        "to_menu_path_id": "int",
        "to_lang": "varchar",
        "deflection_channel": "tinyint",
        "status": "tinyint",
        "fail_reason": "int",
        "started_at": "datetime",
        "ended_at": "datetime",
        "duration": "int"
      }
    

## perf_call_queue_durations
    
    
    {
        "call_id": "bigint",
        "cold_transfer": "tinyint",
        "ended_at": "datetime",
        "event": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "queue_duration": "int",
        "started_at": "datetime",
        "transfer": "tinyint",
        "transfer_id": "int",
        "id": "int",
        "agent_id": "int",
        "call_type": "varchar",
        "fail_reason": "int",
        "fail_details": "varchar",
        "service_level_event": "tinyint",
        "service_level_target_time": "smallint",
        "service_level_target_percent": "tinyint",
        "service_level_abandon_time_threshold": "smallint"
      }
    

## perf_call_smart_actions
    
    
    {
        "id": "bigint",
        "agent_id": "int",
        "call_id": "bigint",
        "type": "int",
        "sub_type": "int",
        "menu_path_id": "int",
        "number_of_photos": "int",
        "result": "tinyint",
        "duration": "int",
        "end_user_input_duration": "int",
        "notification_duration": "int",
        "lang": "varchar",
        "started_at": "datetime",
        "ended_at": "datetime",
        "interaction_started_at": "datetime",
        "interaction_ended_at": "datetime"
      }
    

## perf_call_va_deflected_escalations
    
    
    {
        "id": "int",
        "call_id": "bigint",
        "deflection": "int",
        "escalation_id": "int",
        "escalation_reason": "int",
        "event": "int",
        "event_id": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "time": "datetime",
        "virtual_agent_id": "int"
      }
    

## perf_call_va_handle_durations
    
    
    {
        "id": "int",
        "call_duration": "int",
        "call_id": "bigint",
        "call_type": "varchar",
        "end_user_id": "int",
        "ended_at": "datetime",
        "escalation_reason": "int",
        "event": "int",
        "event_id": "int",
        "fallback_response_count": "int",
        "finish_reason": "int",
        "initiated_by": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "response_count": "int",
        "sentiment": "int",
        "started_at": "datetime",
        "time": "datetime",
        "transfer": "tinyint",
        "transfer_id": "int",
        "virtual_agent_id": "int"
      }
    

## perf_chat_cobrowse_details
    
    
    {
        "agent_id": "int",
        "menu_path_id": "int",
        "lang": "varchar",
        "chat_id": "int",
        "session_id": "int",
        "started_by": "int",
        "ended_by": "int",
        "started_at": "datetime",
        "ended_at": "datetime",
        "remote_controlled": "tinyint",
        "device_name": "varchar",
        "id": "bigint"
      }
    

## perf_chat_deflected_escalations
    
    
    {
        "id": "int",
        "chat_id": "int",
        "event": "varchar",
        "time": "datetime",
        "virtual_agent_id": "int",
        "menu_path_id": "int",
        "lang": "varchar",
        "deflection": "int",
        "escalation_reason": "int"
      }
    

## perf_chat_handle_durations
    
    
    {
        "id": "int",
        "acw_duration": "int",
        "agent_id": "int",
        "chat_duration": "int",
        "chat_id": "int",
        "ended_at": "datetime",
        "event": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "reactivated": "tinyint",
        "started_at": "datetime",
        "transfer": "tinyint",
        "transfer_id": "int",
        "type": "int",
        "end_user_id": "int",
        "session_id": "int",
        "response_count": "int",
        "response_time_avg": "decimal",
        "response_time_max": "int",
        "response_time_total": "int",
        "wait_duration": "int",
        "inbound": "tinyint",
        "sub_type": "int"
      }
    

## perf_chat_queue_durations
    
    
    {
        "chat_id": "int",
        "ended_at": "datetime",
        "event": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "queue_duration": "int",
        "reactivated": "tinyint",
        "started_at": "datetime",
        "transfer": "tinyint",
        "transfer_id": "int",
        "id": "int",
        "agent_id": "int",
        "type": "int",
        "fail_reason": "int",
        "service_level_event": "tinyint",
        "service_level_target_time": "smallint",
        "service_level_target_percent": "tinyint",
        "service_level_abandon_time_threshold": "smallint"
      }
    

## perf_chat_smart_actions
    
    
    {
        "id": "bigint",
        "agent_id": "int",
        "chat_id": "int",
        "type": "int",
        "sub_type": "int",
        "number_of_photos": "int",
        "menu_path_id": "int",
        "result": "tinyint",
        "duration": "int",
        "end_user_input_duration": "int",
        "notification_duration": "int",
        "lang": "varchar",
        "started_at": "datetime",
        "ended_at": "datetime",
        "interaction_started_at": "datetime",
        "interaction_ended_at": "datetime"
      }
    

## perf_chat_va_handle_durations
    
    
    {
        "id": "int",
        "chat_id": "int",
        "chat_duration": "int",
        "ended_at": "datetime",
        "escalation_reason": "varchar",
        "event": "int",
        "event_id": "int",
        "finish_reason": "varchar",
        "initiated_by": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "reactivated": "tinyint",
        "started_at": "datetime",
        "time": "datetime",
        "transfer": "tinyint",
        "transfer_id": "int",
        "virtual_agent_id": "int",
        "response_count": "int",
        "response_time_avg": "decimal",
        "response_time_max": "int",
        "response_time_total": "int",
        "fallback_response_count": "int"
      }
    

## perf_chat_va_skipped_assignments
    
    
    {
        "id": "int",
        "chat_id": "int",
        "reason": "int",
        "menu_path_id": "int",
        "lang": "varchar",
        "time": "datetime",
        "event_id": "int",
        "event": "varchar"
      }
    

## perf_chat_virtual_agent_summaries
    
    
    {
        "id": "int",
        "chat_id": "int",
        "chat_type": "varchar",
        "ended_at": "datetime",
        "lang": "varchar",
        "virtual_agent_id": "int",
        "response_count": "int",
        "response_time_total": "int",
        "fallback_response_count": "int"
      }
    

## perf_consumer_call_in_menu_durations
    
    
    {
        "id": "int",
        "end_user_id": "int",
        "call_id": "bigint",
        "session_id": "int",
        "event": "smallint",
        "call_type": "varchar",
        "lang": "varchar",
        "menu_path_id": "int",
        "in_menu_duration": "int",
        "started_at": "datetime",
        "ended_at": "datetime"
      }
    

## perf_email_handle_durations
    
    
    {
        "id": "bigint",
        "event": "int",
        "email_duration": "int",
        "email_support_id": "bigint",
        "inbound": "tinyint",
        "transfer": "tinyint",
        "transfer_id": "int",
        "lang": "varchar",
        "menu_path_id": "int",
        "agent_id": "int",
        "started_at": "datetime",
        "ended_at": "datetime",
        "end_user_id": "int",
        "status": "int",
        "assignment_type": "tinyint",
        "attachments_count": "int"
      }
    

## perf_email_queue_durations
    
    
    {
        "id": "bigint",
        "event": "int",
        "email_support_id": "bigint",
        "lang": "varchar",
        "menu_path_id": "int",
        "queue_duration": "int",
        "started_at": "datetime",
        "ended_at": "datetime",
        "agent_id": "int",
        "inbound": "tinyint",
        "status": "int",
        "assignment_type": "tinyint",
        "service_level_event": "tinyint",
        "service_level_target_time": "smallint",
        "service_level_target_percent": "tinyint"
      }
    

## perf_third_party_call_handle_durations
    
    
    {
        "id": "int",
        "participant_id": "bigint",
        "call_id": "bigint",
        "origin_call_id": "bigint",
        "session_id": "int",
        "call_type": "varchar",
        "call_duration": "int",
        "hold_duration": "int",
        "started_at": "datetime",
        "ended_at": "datetime"
      }
    

## queue_report_group_histories
    
    
    {
        "id": "int",
        "group_id": "int",
        "lang": "varchar",
        "menu_id": "int",
        "menu_path_id": "int",
        "menu_type": "varchar",
        "started_at": "datetime",
        "ended_at": "datetime"
      }
    

## queue_report_group_items
    
    
    {
        "id": "int",
        "group_id": "int",
        "lang": "varchar",
        "menu_id": "int"
      }
    

## queue_report_groups
    
    
    {
        "id": "int",
        "comm_type": "varchar",
        "created_at": "datetime",
        "hidden": "tinyint",
        "hidden_productive_agents": "tinyint",
        "name": "varchar",
        "updated_at": "datetime",
        "user_statuses": "varchar"
      }
    

## sessions
    
    
    {
        "id": "int",
        "agent_id": "int",
        "created_at": "datetime",
        "end_user_id": "int",
        "finished_at": "datetime",
        "in_queue_priority": "int",
        "lang": "varchar",
        "materialized_menu_path": "varchar",
        "materialized_menu_path_name": "varchar",
        "menu_id": "int",
        "menu_path_id": "int",
        "menu_type": "varchar",
        "out_event_id": "varchar",
        "out_ticket_id": "varchar",
        "out_ticket_url": "varchar",
        "queue_priority_level": "int",
        "rating": "int",
        "status": "int",
        "transfer_count": "int",
        "user_priority": "int",
        "verifiable": "tinyint",
        "verified": "tinyint"
      }
    

## skills
    
    
    {
        "id": "bigint",
        "created_at": "datetime",
        "name": "varchar",
        "updated_at": "datetime"
      }
    

## team_hierarchies
    
    
    {
        "ancestor_id": "int",
        "descendant_id": "int",
        "generations": "int"
      }
    

## team_memberships
    
    
    {
        "id": "int",
        "created_at": "datetime",
        "team_id": "int",
        "updated_at": "datetime",
        "user_id": "int",
        "membership_type": "int"
      }
    

## teams
    
    
    {
        "id": "int",
        "agents_count": "int",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "name": "varchar",
        "parent_id": "int",
        "position": "int",
        "updated_at": "datetime"
      }
    

## user_activity_logs
    
    
    {
        "id": "bigint",
        "activity": "int",
        "call_id": "bigint",
        "chat_id": "int",
        "duration": "int",
        "ended_at": "datetime",
        "started_at": "datetime",
        "user_id": "int",
        "user_status_id": "int"
      }
    

## user_projections
    
    
    {
        "id": "int",
        "call_id": "bigint",
        "chat_id": "int",
        "ended_at": "datetime",
        "matching_skills_payload": "json",
        "projected_at": "datetime",
        "result": "int",
        "user_id": "int"
      }
    

## user_queue_histories
    
    
    {
        "id": "int",
        "channel": "int",
        "current": "tinyint",
        "end_event": "int",
        "ended_at": "datetime",
        "group_id": "int",
        "lang": "varchar",
        "level": "int",
        "menu_id": "int",
        "start_event": "int",
        "started_at": "datetime",
        "user_id": "int"
      }
    

## user_skills
    
    
    {
        "id": "bigint",
        "created_at": "datetime",
        "learning": "tinyint",
        "skill_id": "int",
        "skill_level": "int",
        "updated_at": "datetime",
        "user_id": "int"
      }
    

## user_statuses
    
    
    {
        "id": "int",
        "deleted_at": "datetime",
        "name": "varchar"
      }
    

## user_team_histories
    
    
    {
        "id": "int",
        "current": "tinyint",
        "end_event": "int",
        "ended_at": "datetime",
        "start_event": "int",
        "started_at": "datetime",
        "team_id": "int",
        "user_id": "int"
      }
    

## users
    
    
    {
        "id": "int",
        "agent_number": "varchar",
        "call_queue_assigned": "tinyint",
        "chat_auto_answer": "tinyint",
        "chat_queue_assigned": "tinyint",
        "created_at": "datetime",
        "deleted_at": "datetime",
        "email": "varchar",
        "first_name": "varchar",
        "ignored_projection_count": "int",
        "last_login_time": "datetime",
        "last_name": "varchar",
        "location_id": "int",
        "max_chat_limit": "int",
        "max_chat_limit_enabled": "tinyint",
        "permissions": "int",
        "repr_status_name": "varchar",
        "roles": "int",
        "status_after_inquiries_by": "int",
        "status_after_inquiries_id": "int",
        "repr_status_id": "int",
        "location": "varchar"
      }
    

## virtual_agents
    
    
    {
        "id": "int",
        "name": "varchar",
        "enabled": "tinyint",
        "menu_types": "int",
        "chatbot_workflow_id": "int",
        "created_at": "datetime",
        "updated_at": "datetime",
        "avatar": "varchar",
        "deleted_at": "datetime",
        "langs": "int",
        "channel_types": "int",
        "agent_type": "int"
      }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
