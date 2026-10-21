---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-session-metadata/
title: Chat session metadata \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:39.462363+00:00
---

# Chat session metadata  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-session-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat session metadata Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the schema of the **chat session metadata** record. The metadata record is the JSON document that Contact Center AI Platform creates for a support chat session. CCAI Platform delivers the metadata record to your CRM integration as part of the chat `session-end` command. When you enable external storage, CCAI Platform also writes the record to your external-storage configuration using a `metadata.json` file. Each chat produces one record, which the top-level `id` uniquely identifies. Use this schema to ingest records into downstream systems, validate received payloads, or map fields onto data-warehouse columns.

## Schema root

The chat session metadata record is a single JSON object representing one chat session. Three concepts at the top level determine the record's identity and shape.

**Primary key:`id` (integer)**

Uniquely identifies the chat session within your tenant. One record exists per chat. All other top-level fields, arrays, and nested objects describe attributes of the chat that this `id` identifies.

**Handler discriminator:`agent_info` (object, oneOf)**

A single object whose shape varies depending on the chat's last handler. The two variants are mutually exclusive — only one is ever present:

  * Human-agent variant: Present when the chat's last handler was a human agent. Carries `email`, `first_name`, `last_name`, and `agent_number` in addition to the shared `id`, `name`, and `avatar_url` fields.

  * Virtual-agent variant: Present when the chat's last handler was a virtual agent. Carries `va_alias` and omits `email`, `first_name`, `last_name`, and `agent_number`.




To detect which variant a record carries, check for the presence of a variant-specific field, typically `agent_info.email` for the human-agent variant or `agent_info.va_alias` for the virtual-agent variant. Full definitions for each variant appear in Definitions: `agent` and Definitions: `virtual_agent`.

**Chat-shape discriminators:`chat_type`, `session_type`, `session_type_v2` (string)**

Three parallel views of the same underlying chat type. They never disagree on which chat type a record represents; they differ only in the vocabulary used to name it.

  * `chat_type`: Uses the legacy enum vocabulary, such as Messaging Inbound (App Chat), Messaging (SMS), and Messaging (WhatsApp).

  * `session_type`: Always returns the same string as `chat_type`. It exists for backward compatibility with integrations that key on this field; treat it as a deprecated alias of `chat_type`.

  * `session_type_v2`: Uses the current enum vocabulary, which may include finer-grained distinctions such as Messaging Inbound (Mobile Chat). For chat types that don't have a v2-specific value, `session_type_v2` returns the same string as `chat_type`. New integrations should parse `session_type_v2`.




For the values of each field, see Core information.

### Core information

  * `id` (integer): A unique identifier for each chat session. This primary key distinguishes one chat from another.

  * `lang` (string): The ISO 639 language code used during the chat (for instance, `"en"` for English, `"es"` for Spanish).

  * `chat_type` (string): The type of chat, using the legacy type vocabulary. Values include `"Messaging Inbound (App Chat)"`, `"Messaging Inbound (Web Chat)"`, `"Messaging (SMS)"`, `"Messaging (WhatsApp)"`, and `"Messaging (Apple Messaging for Business)"`.

  * `session_type` (string): A duplicate of `chat_type` (same values), retained for backward compatibility. See Versioning and deprecations: Legacy duplicates.

  * `session_type_v2` (string): The type of chat, using the current type vocabulary. It refines the `chat_type` values with finer-grained distinctions. Values include `"Messaging Inbound (Mobile Chat)"`, `"Messaging Inbound (Web Chat)"`, `"Messaging (WhatsApp)"`, `"Messaging (Apple Messaging for Business)"`, `"Messaging (SMS)"`, `"Messaging Inbound (SMS)"`, `"Messaging Outbound (SMS)"`, `"Messaging Outbound (SMS using the API)"`, `"Messaging Inbound (SMS Direct)"`, `"Messaging Outbound (SMS Direct)"`, and `"Messaging Outbound (SMS Direct using the API)"`.

  * `status` (string): The current status of the chat. Possible values: `"queued"`, `"selecting"`, `"assigned"`, `"va_assigned"`, `"dismissed"`, `"va_dismissed"`, `"check_in_timeout"`, `"finished"`, `"no_response"`, `"canceled"`, and `"failed"`. (CCAI Platform reports a finished chat that received no consumer reply as `"no_response"`.)

  * `sub_status` (string or null): More specific status detail for the chat, when one is available. Possible values: `"selecting"`, `"queued"`, `"ongoing"`, `"dismissed"`, `"finished"`, `"timeout"`, `"deflected"`, `"abandoned"`, `"expired"`, `"failed"`, `"disconnected_by_agent"`, `"disconnected_by_end_user"`, `"no_messages"`, `"no_messages_disconnected_by_agent"`, `"no_messages_disconnected_by_end_user"`, and `"end_user_opt_out"`.

  * `created_at` (string, date-time): The timestamp when CCAI Platform created the chat session.

  * `assigned_at` (string, date-time, or null): The timestamp when CCAI Platform assigned the chat to an agent, or null if it wasn't assigned.

  * `ends_at` (string, date-time, or null): The timestamp when the chat session ended.

  * `updated_at` (string, date-time): The timestamp when CCAI Platform last updated the chat data.

  * `first_msg_sent_at` (string, date-time, or null): The timestamp when a participant sent the first message in the chat.

  * `last_msg_sent_at` (string, date-time, or null): The timestamp when a participant sent the last message in the chat.

  * `wait_duration` (integer): The total time the consumer spent waiting, in seconds.

  * `chat_duration` (integer): The total duration of the chat, in seconds.

  * `verified` (boolean): Indicates whether the verification smart action verified the interaction.

  * `rating` (integer or null): The customer satisfaction (CSAT) rating that the consumer provided, or null if the consumer didn't give a rating.

  * `has_feedback` (boolean): Indicates whether the consumer provided feedback after the chat.

  * `out_ticket_id` (string or null): The identifier of the ticket that CCAI Platform created in the external CRM system.

  * `out_ticket_url` (string, uri, or null): The URL of the CRM ticket.

  * `is_out_ticket_account` (boolean or null): Indicates whether the CRM ticket represents a customer (true) or a chat interaction (false).

  * `fail_reason` (string): The reason for any failure during the chat, or `"nothing"` when the chat didn't fail. Possible values: `"nothing"`, `"unknown"`, `"expired"`, `"after_hours"`, `"escalation_failed"`, `"check_in_timed_out"`, `"check_in_timed_out_expired"`, `"expired_menu_selection"`, `"end_user_opt_out"`, `"over_cap_email"`, `"group_deleted_no_substitute"`, `"presession_deflection_unknown"`, `"presession_deflection_timeout"`, `"presession_deflection_message_delivery_failed"`, `"sms_error"`, and `"force_ended"`.

  * `provider_type` (string): The type of chat provider used. Possible values: `"unknown"`, `"messaging"`, `"twilio_conversations"`, `"nexmo_conversations"`, and `"ujet_conversations"`.

  * `provider_channel_id` (string or null): Provider-specific channel identifier for the chat.

  * `message_count` (integer): The total number of messages exchanged in the chat.

  * `average_response_time` (integer): The average time it took for agents to respond during the chat, in seconds.

  * `longest_response_time` (integer): The longest time it took for an agent to respond during the chat, in seconds.

  * `transcript` (boolean): Indicates whether a chat transcript exists for the session.




### Agent and virtual agent information

  * `agent_info` (object): Information about the human agent or virtual agent that last handled the chat. This field uses the `oneOf` keyword to specify that it can be one of two types.

    * `agent` (object): Information about the human agent:

      * `id` (integer): The agent's unique ID.

      * `agent_number` (string or null): An identifier assigned to the agent.

      * `email` (string, email): The agent's email address.

      * `name` (string): The agent's full name.

      * `last_name` (string): The agent's last name.

      * `first_name` (string): The agent's first name.

      * `avatar_url` (string, uri, or null): The URL of the agent's avatar image.

    * `virtual_agent` (object): Information about the virtual agent:

      * `id` (integer): The virtual agent's unique ID.

      * `name` (string): The virtual agent's name.

      * `avatar_url` (string, uri, or null): The URL of the virtual agent's avatar image.

      * `va_alias` (string or null): The virtual agent's display alias, if one is configured. Always present in the payload; null when no alias is set.




### Menu navigation

  * `selected_menu` (object or null): Information about the menu that the consumer selected during the chat.

    * `id` (integer): The unique ID of the menu.

    * `name` (string): The name of the menu.

    * `parent_id` (integer or null): The ID of the parent menu, if any.

    * `position` (integer or null): The menu position relative to other menus at the same level.

    * `deleted` (boolean): Indicates whether an administrator deleted the menu.

    * `menu_type` (string): The type of menu (for example, `"sms_menu"`, `"web_menu"`).

    * `hidden` (boolean): Whether the menu is visible or available for use.

    * `menu_path` (object or null): Describes the hierarchical path of menus that the customer navigated.

    * `items_count` (integer): The number of menus in the path.

    * `name` (string or null): A slash-separated string of menu names (for example, `"Support/Billing"`), or null if the menu path is unavailable.

    * `materialized_path` (string): A slash-separated string of menu IDs.

  * `queue_priority_level` (integer): The queue priority assigned to the chat's selected queue. Present only when queue priority is enabled on your account.




### End-user details

  * `end_user` (object or null): Information about the consumer:

    * `id` (integer or null): The consumer's internal ID.

    * `identifier` (string or null): An external identifier for the consumer.

    * `out_contact_id` (string or null): The consumer's ID in the CRM.




### Customer flags and SDK-provided data

  * `customer_flag` (object): Flags marking notable consumer attributes that external systems provided or updated during the session. Present only when external systems provided or updated authentication-related customer flags during the session.

    * `verified_customer` (boolean): Indicates whether an external system flagged the consumer as verified.

    * `bad_actor` (boolean): Indicates whether an external system flagged the consumer as a bad actor.

    * `repeat_customer` (boolean): Indicates whether an external system flagged the consumer as a repeat customer.

  * `custom_data_secured` (object or null): Custom, securely signed data that the SDK or Apps API provided.

  * `custom_data_not_secured` (object or null): Custom, non-securely signed data that the SDK or Apps API provided.

  * `sip_headers` (object): Inbound SIP headers captured for the chat. Keys and values reflect the SIP headers received from the upstream provider. Present only when you enable SIP header capture on your account and configure it to appear in session metadata




### Media attachments

  * `photos` (array): Photos or screenshots associated with the chat.

    * `id` (integer): Unique identifier for the photo.

    * `photo_type` (string): The type of photo. Possible values include `"photo"` and `"screenshot"`.

    * `url` (string, uri): URL to the stored photo.

    * `smart_action_type` (string or null): The smart action associated with the photo, if any.

    * `transfer_id` (integer or null): Transfer event identifier associated with the photo, if a participant uploaded it after a completed transfer.

  * `videos` (array): Videos associated with the chat.

    * `id` (integer): Unique identifier for the video.

    * `url` (string, uri): URL to the stored video.

    * `smart_action_type` (string or null): The smart action associated with the video, if any.

    * `transfer_id` (integer or null): Transfer event identifier associated with the video, if a participant uploaded it after a completed transfer.




### Chat transfers

  * `transfers` (array): One entry per transfer event during the chat. Records transfers between agents, virtual agents, and menus.

    * `id` (integer): Unique identifier of the transfer.

    * `status` (string): Current status of the transfer. Possible values include `"transferring"`, `"transferred"`, `"failed"`, and `"deflected"`.

    * `fail_reason` (string): Reason the transfer failed, or `"nothing"` if it didn't fail. Possible values: `"nothing"`, `"timeout"`, `"canceled"`, `"ag_connection_timeout"`, `"va_failure"`, `"agent_detection_missed"`, `"unknown"`, and `"unreachable_phone_number"`.

    * `created_at` (string, date-time): Timestamp when the transfer began.

    * `assigned_at` (string, date-time, or null): Timestamp when CCAI Platform assigned the transfer.

    * `connected_at` (string, date-time, or null): Timestamp when the transfer connected.

    * `updated_at` (string, date-time, or null): Timestamp when CCAI Platform last updated the transfer record.

    * `call_duration` (integer or null): Duration of the transferred chat segment, in seconds.

    * `wait_duration` (integer or null): Time the consumer waited during the transfer, in seconds.

    * `deflection` (string): Deflection type associated with the transfer. See Definitions: `deflection` for allowed values.

    * `answer_type_path` (string or null): Path describing how agents or menus answered the original and destination chats.

    * `from_menu_path` / `to_menu_path` (object or null): Menu path before and after the transfer; same shape as `menu_path` in Definitions.

    * `from_agent` / `to_agent` (object or null): Human agent on each side of the transfer; same shape as the `agent` object in Definitions.

    * `from_virtual_agent` / `to_virtual_agent` (object or null): Virtual agent on each side of the transfer; same shape as the `virtual_agent` object in Definitions.

    * `from_queue_priority_level` / `to_queue_priority_level` (integer or null): Queue priority before and after the transfer.




### Chat handling durations

  * `handle_durations` (array): An array of objects, each representing a segment of the chat handled by an agent.

    * `id` (integer): Unique identifier for the handle duration.

    * `agent_id` (integer or null): Identifier of the agent.

    * `acw_duration` (integer): After chat work duration, in seconds.

    * `chat_duration` (integer): Chat duration during this segment, in seconds.

    * `menu_path_id` (integer or null): ID of the menu path.

    * `menu_path` (string): Name of the menu path.

    * `lang` (string): Language used.

    * `transfer` (boolean): Whether a transfer occurred.

    * `transfer_id` (integer or null): ID of the transfer.

    * `started_at` (string, date-time, or null): Start timestamp.

    * `ended_at` (string, date-time, or null): End timestamp.

    * `response_count` (integer): Number of agent responses.

    * `response_time_total` (integer): Total agent response time, in seconds.

    * `response_time_max` (integer): Longest agent response time, in seconds.

    * `response_time_avg` (number or null): Average agent response time, in seconds. This value may include decimal precision.

    * `assigned_connection_duration` (integer): Duration that the consumer waited while the assigned agent connected during this segment.




### Queue durations

  * `queue_durations` (array): An array of objects, each representing a segment of the chat where the consumer was waiting in a queue.

    * `id` (integer): Unique identifier.

    * `agent_id` (integer or null): Agent identifier.

    * `ended_at` (string, date-time): End timestamp.

    * `lang` (string): Language.

    * `menu_path_id` (integer or null): Menu path identifier.

    * `menu_path` (string): Menu path.

    * `queue_duration` (integer or null): Queue duration, in seconds.

    * `started_at` (string, date-time): Start timestamp.

    * `transfer_cold` (boolean or null): Whether the chat was cold transferred.

    * `transfer` (boolean): Whether a transfer occurred.

    * `transfer_id` (integer or null): Transfer identifier.

    * `service_level_abandon_time_threshold` (integer): Service level abandonment threshold, in seconds.

    * `service_level_event` (string): Service level event status. Possible values include `"excluded"`, `"in_sla"`, and `"not_in_sla"`.

    * `service_level_target_percent` (integer): Service level target percentage.

    * `service_level_target_time` (integer): Service level target time, in seconds.




### Virtual-agent-to-human escalations

  * `escalations` (array): Each entry represents an escalation from a virtual agent to a human agent.

    * `id` (integer): Unique identifier for the escalation.

    * `status` (string): Current status of the escalation. Possible values: `"escalating"`, `"escalated"`, `"canceled"`, `"deflecting"`, and `"deflected"`.

    * `reason` (string): Reason the chat was escalated. Possible values: `"unknown"`, `"by_end_user_ask"`, `"by_end_user_message"`, `"by_virtual_agent"`, `"payload_failure"`, `"could_not_resume"`, `"by_human_agent"`, `"invalid_queue"`, and `"dismissed"`.

    * `created_at` (string, date-time): Timestamp when the escalation began.

    * `escalated_at` (string, date-time, or null): Timestamp when the escalation completed.

    * `from_virtual_agent` (object or null): Virtual agent that escalated the chat. Same shape as the `virtual_agent` object in Definitions.

    * `to_agent` (object or null): Human agent the chat was escalated to. Same shape as the `agent` object in Definitions.

    * `from_menu_path` / `to_menu_path` (object or null): Menu path before and after escalation.




### Virtual agent deflected escalations

  * `virtual_agent_deflected_escalations` (array): Details of escalations from virtual agents that deflected to another destination.

    * `id` (integer): Unique identifier.

    * `deflection` (string): Deflection type for the deflected escalation. Possible values: `"no_deflection"`, `"over_cap"`, `"over_cap_email"`, `"over_cap_virtual_agent"`, `"over_cap_human_agent"`, `"over_cap_sip"`, `"over_cap_extension"`, `"after_hours"`, `"after_hours_email"`, and `"after_hours_virtual_agent"`.

    * `escalation_id` (integer): Escalation event identifier.

    * `escalation_reason` (string): Reason for escalation. Same values as `escalations[].reason` (see 10\. Virtual-agent-to-human escalations).

    * `escalated_at` (string, date-time): Escalation timestamp.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `virtual_agent` (object): Virtual agent details. See Definitions: `virtual_agent`.




### Virtual agent handling durations

  * `virtual_agent_handle_durations` (array): Segments of time the chat was handled by a virtual agent.

    * `id` (integer): Unique identifier.

    * `virtual_agent` (object): Virtual agent details. See Definitions: `virtual_agent`.

    * `chat_duration` (integer): Duration of the segment, in seconds.

    * `escalation_reason` (string): Reason for escalation.

    * `finish_reason` (string): Reason the interaction finished.

    * `response_count` (integer): Virtual agent response count.

    * `response_time_total` (integer): Total virtual agent response time, in seconds.

    * `response_time_max` (integer): Longest virtual agent response time, in seconds.

    * `response_time_avg` (number or null): Average virtual agent response time, in seconds. This value may include decimal precision.

    * `fallback_response_count` (integer): Fallback response count.

    * `initiated_by` (string): How the virtual agent session was initiated. Possible values: `"end_user"`, `"human_agent"`, and `"post_session"`.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `transfer` (boolean): Whether the chat was transferred.

    * `transfer_id` (integer or null): Transfer event identifier.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time): End timestamp.




### Consumer handling durations

  * `consumer_handle_durations` (array): Durations the consumer was in the chat.

    * `id` (integer): Unique identifier.

    * `chat_duration` (integer): Consumer segment duration, in seconds.

    * `started_at` (string, date-time, or null): Start timestamp.

    * `ended_at` (string, date-time, or null): End timestamp.

    * `message_count` (integer): Number of consumer messages.

    * `response_count` (integer): Number of consumer responses.

    * `response_time_total` (integer): Total consumer response time, in seconds.

    * `response_time_max` (integer): Longest consumer response time, in seconds.

    * `response_time_avg` (integer): Average consumer response time, in seconds.




### Consumer event durations

  * `consumer_event_durations` (array): Details of consumer chat events (for instance, CSAT, payment).

    * `id` (integer): Unique identifier.

    * `duration` (integer): Event duration, in seconds.

    * `type` (string): Event type. Possible values: `"csat"`.

    * `event` (string): Event outcome. Possible values: `"finished"` and `"abandoned"`.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time): End timestamp.




### Participants

  * `participants` (array): Information about each participant in the chat (for example, end user, agent, virtual agent).

    * `id` (integer): Unique identifier for the participant.

    * `type` (string): Type of participant. Possible values: `"end_user"`, `"agent"`, `"manager"`, `"virtual_agent"`, `"external_agent"`, and `"task_virtual_agent"`.

    * `entry_type` (string): How the participant entered the chat. Possible values: `"queue_or_transfer"`, `"barge"`, and `"post_session"`.

    * `user_id` (integer or null): User ID if the participant is an agent.

    * `end_user_id` (integer or null): Consumer identifier, if the participant is the consumer.

    * `virtual_agent_id` (integer or null): Virtual agent ID if the participant is a virtual agent.

    * `virtual_agent_params` (object): Custom metadata used by the virtual agent. Present only when you configure virtual-agent custom metadata inclusion.

    * `status` (string): Status of the participant. Possible values: `"waiting"`, `"connecting"`, `"invited"`, `"connected"`, `"wrapping_up"`, `"finished"`, `"failed"`, `"resuming"`, and `"post_session_in_progress"`.

    * `fail_reason` (string): Reason for failure, if any. Possible values: `"nothing"`, `"canceled"`, `"ag_connection_timeout"`, and `"unknown"`.

    * `connected_at` (string, date-time, or null): Timestamp when the participant connected.

    * `phone_number` (string): Phone number of the participant. Present only on consumer participants.

    * `chat_id` (integer): Identifier for the chat.

    * `chat_duration` (integer or null): Chat duration for the participant, in seconds.

    * `finished_at` (string, date-time, or null): Timestamp when the participant's involvement ended.

    * `agent_assist` (object): Agent Assist settings active for the participant. Always present; an empty-default object when Agent Assist is not configured.

    * `virtual_agent` (object or null): Details of the virtual agent serving as this participant; distinct from the top-level `agent_info` and from `virtual_agent_params`.

    * `sip_headers` (object or null): SIP headers associated with this participant. Always present in the payload; null when CCAI Platform captures none.

    * `location` (string or null): The agent's configured location. Present only on agent participants.

    * `location_id` (integer or null): The location's identifier. Present only on agent participants.

    * `email` (string, email): The agent's email address. Present only on agent participants.

    * `first_name` (string or null): The agent's first name. Present only on agent participants.

    * `last_name` (string or null): The agent's last name. Present only on agent participants.

    * `middle_name` (string or null): The agent's middle name. Present only on agent participants.

    * `teams` (array): Array of `{ id, name }` objects describing the teams the agent belongs to. Present only on agent participants.




### Check-in logs

  * `check_in_logs` (array): Check-in events recorded during the chat session. Each item groups check-in events for one check-in flow.

    * `check_in_id` (integer): Identifier of the check-in flow.

    * `check_in_modal_displayed` (string, date-time): Timestamp when CCAI Platform showed the check-in modal to the consumer. Present only when CCAI Platform displayed the check-in modal.

    * `check_in_modal_confirmed` (string, date-time): Timestamp when the consumer confirmed they were still Present. present only when the consumer confirmed the check-in modal.

    * `check_in_modal_timed_out` (string, date-time): Timestamp when the check-in prompt timed out. Present only when the check-in modal timed out.

    * `timeout_modal_rejoin_success` (string, date-time): Timestamp when the rejoin action succeeded. Present only when the consumer successfully rejoined after timeout.

    * `timeout_modal_rejoin_failed_after_hour` (string, date-time): Timestamp when the rejoin action failed due to after-hours behavior. Present only when rejoin failed because the queue was after hours.

    * `timeout_modal_exit_chat` (string, date-time): Timestamp when the consumer chose to exit the chat. Present only when the consumer exited the chat from the timeout modal.

    * `timeout_modal_time_out_sdk_closed` (string, date-time): Timestamp when the timeout modal flow ended because the SDK closed. Present only when the SDK closed after timeout.




### Offer events

  * `offer_type` (string or null): Manner in which CCAI Platform offered the chat to the agent.

  * `offer_events` (array): Events where CCAI Platform offered the chat to agents.

    * `casting_time` (string, date-time): Time CCAI Platform offered the chat.

    * `group` (string): Group to which CCAI Platform offered the chat.




### Other details

  * `dismiss_duration` (integer): Duration the chat spent in the dismissed status, in seconds. Present only when the chat spent time in the dismissed status.

  * `answer_type` (string or null): How the chat was answered. Possible values: `"manual"`, `"auto"`, `"outbound"`, and `"deflection"`.

  * `inbound_number` (string): Inbound phone number associated with the chat. Present only when an inbound phone number is associated with the chat.

  * `outbound_number` (string): Outbound phone number associated with the chat. Present only when an outbound phone number is associated with the chat.

  * `after_hours` (boolean): Whether the chat occurred after hours.

  * `dispositions` (array): Wrap-up codes and notes that agents recorded. Present only when you enable wrap-up codes or notes on your account. Each entry may contain fields conditionally rendered based on your wrap-up configuration:

    * `user_id` (integer): Agent identifier.

    * `transfer_id` (integer or null): Transfer event identifier, if recorded after a transfer.

    * `participant_id` (integer): Participant identifier.

    * `note` (string): Free-text agent note.

    * `original_note` (string): Original (pre-edit) version of the note.

    * `code` (string): Disposition code name.

    * `ujet_code_id` (integer or empty string): The CCAI Platform-assigned identifier of the disposition code; a stable key for the code (the code display name can change). Empty string when unavailable.

    * `list` (string): Name of the list the code belongs to.

    * `list_path` (string): Slash-separated path of the code's list.

    * `ujet_list_id` (integer or empty string): The CCAI Platform-assigned identifier of the list the disposition code belongs to; a stable key for the list. Empty string when unavailable.

    * `custom_list_id` (string or integer): Customer-defined list identifier, if mapped.

    * `custom_code_id` (string or integer): Customer-defined code identifier, if mapped.

  * `auto_session_summaries` (array): AI-generated session summaries saved to the CRM record. Present only when you enable conversation summarization on your account and AI successfully generates a summary. Each entry contains:

    * `user_id` (integer): Identifier of the agent participant the summary is associated with.

    * `participant_id` (integer): Participant identifier.

    * `session_summary` (string): The summary text.

    * `session_summary_sections` (array or object): The summary broken into structured sections, when available.

  * `transfer_limit` (object or null): Transfer limit data for the chat.

    * `enabled` (boolean): Whether transfer-limit tracking was enabled for the chat.

    * `limit_count` (integer): Number of transfers allowed.

    * `limit_reached` (boolean): Whether the chat reached the configured transfer limit.

  * `email` (string, email, or null): The consumer's email address.

  * `feedback` (string or null): Consumer feedback.

  * `smart_action_text` (string or null): Text of any smart action taken.




## Definitions

The following sub-schemas appear at multiple points in the chat session metadata document. Each sub-schema appears once. Property groups that reference them point back to this section rather than redefining their shape inline.

### `menu_path` (object)

Describes a hierarchical menu path the chat traversed. See Menu navigation for the full list of its fields.

**Referenced from:** the top-level `menu_path` field; each `transfers[].from_menu_path` and `transfers[].to_menu_path`; each `escalations[].from_menu_path` and `escalations[].to_menu_path`.

### `agent` (object)

Describes a human agent. This is one of the two variants of the top-level `agent_info` discriminator (see Schema root). See Agent and virtual agent information for the full list of its fields.

**Referenced from:** the `agent_info` field when the chat's last handler was a human agent; each `transfers[].from_agent` and `transfers[].to_agent`; each `escalations[].to_agent`.

### `virtual_agent` (object)

Describes a virtual agent. This is one of the two variants of the top-level `agent_info` discriminator (see Schema root). See Agent and virtual agent information for the full list of its fields.

**Referenced from:** the `agent_info` field when the chat's last handler was a virtual agent; each `transfers[].from_virtual_agent` and `transfers[].to_virtual_agent`; each `escalations[].from_virtual_agent`; each `virtual_agent_handle_durations[].virtual_agent`; each `virtual_agent_deflected_escalations[].virtual_agent`; each `participants[].virtual_agent`.

### `deflection` (string, enum)

The deflection state associated with a transfer. Values follow a `<trigger>_<destination>` pattern, where the prefix identifies the condition that triggered the deflection and the suffix identifies the destination or treatment (for example, `_phone`, `_voicemail`, `_message`, `_queue`, `_sip`, `_extension`, `_callback`, `_wait`).

**Allowed values, grouped by trigger family:**

  * No deflection: `no_deflection`, `deflecting`

  * Over-capacity, when the queue was over its capacity threshold: `over_cap_phone`, `over_cap_voicemail`, `over_cap_callback`, `over_cap_wait`, `over_cap_message`, `over_cap_ewt_only`, `over_cap_queue`, `over_cap_sip`, `over_cap_extension`, `over_cap_phone_with_extension`

  * After-hours, when the chat arrived outside the menu's configured operating hours: `after_hours_voicemail`, `after_hours_phone`, `after_hours_message_only`, `after_hours_message`, `after_hours_queue`, `after_hours_sip`, `after_hours_extension`, `after_hours_phone_with_extension`

  * Temporary redirection, when a temporary redirection was configured on the menu: `temp_redirection_phone`, `temp_redirection_message`, `temp_redirection_voicemail`, `temp_redirection_queue`, `temp_redirection_sip`, `temp_redirection_extension`, `temp_redirection_phone_with_extension`

  * IVR pre-session: `ivr_presession_deflection`

  * Virtual-agent redirection, when a virtual agent redirected the chat: `va_redirection_phone`, `va_redirection_sip`




**Referenced from:** each `transfers[].deflection`. (Virtual-agent deflected escalations in Virtual agent deflected escalations use a separate, smaller deflection vocabulary, documented inline there.)

### `transfer` (object)

Describes a transfer that occurred during the chat. A transfer can move a chat between menus, agents, and virtual agents. See Chat transfers for the full list of its fields.

**Referenced from:** the top-level `transfers` array. (Other fields named `transfer_id` throughout the document are integer references to a transfer's `id`, not inlined `transfer` objects.)

### `participant` (object)

Describes one participant in the chat. Participant shape varies by participant type; agent participants can include agent profile, location, team, and Agent Assist fields, while consumer and virtual-agent participants include type-specific identifiers. See Participants for the full list of documented fields.

**Referenced from:** the top-level `participants` array; `auto_session_summaries[].participant_id`; disposition records.

### Duration row (object)

Describes a measured interval within the chat, such as agent handle time, queue time, consumer handle time, consumer event time, or virtual-agent handle time. Each duration array has its own row shape because similarly named fields can have different precision or nullability across tables.

**Referenced from:** `handle_durations`, `queue_durations`, `virtual_agent_handle_durations`, `consumer_handle_durations`, and `consumer_event_durations`.

## Versioning and deprecations

The chat session metadata document is designed for backward-compatible schema evolution. New fields and arrays may be added at any time, and integrations should disregard any unrecognized keys to ensure continued functionality. The following fields are legacy or otherwise soft-superseded; they remain in the payload for backward compatibility, but new integrations should follow the guidance for each.

### Legacy duplicates

  * `session_type` (string): Legacy alias of `chat_type`. Always returns the same value as `chat_type` and uses the same legacy enum vocabulary. Retained for backward compatibility with integrations that key on `session_type`. New integrations should parse `chat_type` directly, or for finer-grained distinctions `session_type_v2` (see Vocabulary evolution below).



### Vocabulary evolution

`chat_type` and `session_type_v2` describe the same underlying chat type with two different vocabularies. CCAI Platform emits both fields on every record; they aren't duplicates of each other:

  * `chat_type` uses the legacy enum vocabulary. Values such as Messaging Inbound (App Chat) and Messaging (SMS) describe the original chat-type categories.

  * `session_type_v2` uses the current enum vocabulary. It may introduce finer-grained distinctions for the chat types that have v2-specific values. For chat types that don't have a v2-specific value, `session_type_v2` returns the same string as `chat_type`.




New integrations should parse `session_type_v2`. The values for each field are listed in Core information.

### Additive fields

The chat session metadata payload may gain new top-level fields, nested fields, array item fields, or enum values over time. Integrations should ignore unrecognized keys and preserve raw records where possible. Avoid strict parsing that fails when a new property appears.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
