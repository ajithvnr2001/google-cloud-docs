---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-session-metadata/
title: Call session metadata \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:22.022284+00:00
---

# Call session metadata  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-session-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call session metadata Stay organized with collections  Save and categorize content based on your preferences. 

This document provides the schema of the **call session metadata** record — the JSON document UJET emits at the end of every voice call. UJET delivers the record to your CRM integration as the body of the session-end command and writes the record to your external-storage configuration as a `metadata.json` file. Each call produces exactly one record. The top-level `id` uniquely identifies each record. Use this schema to ingest records into downstream systems, validate received payloads, or map fields onto data-warehouse columns.

## Schema root

The call session metadata record is a single JSON object that represents a voice call session. Three concepts at the top level determine the record's identity and shape.

**Primary key —`id` (integer)**

The top-level `id` uniquely identifies the call session within your tenant. One record exists per call. All other top-level fields, arrays, and nested objects describe attributes of the call that this `id` identifies.

**Handler discriminator —`agent_info` (object, oneOf)**

A single object whose shape varies depending on the call's last handler. The two variants are mutually exclusive — the record contains only one variant:

  * Human-agent variant — present if a human agent handled the call last. Carries `email`, `first_name`, `last_name`, and `agent_number` in addition to the shared `id`, `name`, and `avatar_url` fields.

  * Virtual-agent variant — present if a virtual agent handled the call last. Carries `va_alias` and omits `email`, `first_name`, `last_name`, and `agent_number`.




To detect which variant a record carries, check for the presence of a variant-specific field — typically `agent_info.email` for the human-agent variant or `agent_info.va_alias` for the virtual-agent variant. For the full shape of each variant, see agent and virtual_agent.

**Call-shape discriminators —`call_type`, `session_type`, `session_type_v2` (string)**

Three parallel views of the same underlying call type. They never disagree on which call type a record represents; they differ only in the vocabulary they use to name the call type.

  * `call_type` uses the legacy enum vocabulary (for example, `Voice Inbound (App)`, `Voice Outbound`, or `Voice Internal`).

  * `session_type` always returns the same string as `call_type`. UJET provides this field for backward compatibility with integrations that key on this field; treat it as a deprecated alias of `call_type`. See Versioning and deprecations.

  * `session_type_v2` uses the current enum vocabulary. This vocabulary extends the `call_type` vocabulary with finer-grained inbound distinctions — for example, `Voice Inbound (Mobile)` and `Voice Inbound (IVR using Mobile)` in place of the broader `Voice Inbound (App)` and `Voice Inbound (IVR using App)`. For call types that don't have a v2-specific value, `session_type_v2` returns the same string as `call_type`. New integrations should parse `session_type_v2`.




For the values of each field, see Core information.

### Core information

These properties capture the core information of the call:

  * `id` (integer): A unique identifier for each call session. This is the primary key that distinguishes one call from another.

  * `call_uuid` (string or null): A unique identifier that correlates a call across origin and receiving tenants in dynamic call routing (DCR) interactions. Both legs of a DCR call share the same `call_uuid` value, allowing customers to bridge data between environments. The field is null or empty for any call that isn't a DCR interaction, and for calls that occurred before UJET added the field.

  * `lang` (string): The ISO 639 language code for the call (for example, "en" for English or "es" for Spanish). This code helps you perform language-specific analysis and reporting.

  * `call_type` (string): The type of call, using the legacy type vocabulary. Values include "Voice Inbound (App)", "Voice Inbound (Web)", "Voice Inbound (IVR)", "Voice Inbound (IVR using App)", "Voice Inbound (API)", "Voice Inbound (Direct)", "Voice Inbound (Extension)", "Voice Scheduled (App)", "Voice Scheduled (Web)", "Voice Scheduled (API)", "Voice Callback", "Voice Callback (Web)", "Voice Outbound", "Voice Outbound (API)", "Voice Outbound (Direct)", "Voice Outbound (UCaaS)", "Voice Internal", "Voice Campaign (Acqueon)", "Voice Campaign (<your brand name>)", and "Agent Scheduled Call".

  * `session_type` (string): A duplicate of `call_type` (same values) that UJET retains for backward compatibility. See Versioning and deprecations: Legacy duplicates.

  * `session_type_v2` (string): The type of call, using the current type vocabulary. It refines the `call_type` values with finer-grained inbound distinctions (for example, "Voice Inbound (Mobile)" and "Voice Inbound (IVR using Mobile)" in place of "Voice Inbound (App)" and "Voice Inbound (IVR using App)"). Values include "Voice Inbound (Mobile)", "Voice Inbound (Web)", "Voice Inbound (IVR)", "Voice Inbound (IVR using Mobile)", "Voice Inbound (API)", "Voice Inbound (Direct)", "Voice Inbound (Extension)", "Voice Scheduled (Mobile)", "Voice Scheduled (Web)", "Voice Scheduled (API)", "Voice Callback", "Voice Callback (Web)", "Voice Outbound", "Voice Outbound (API)", "Voice Outbound (Direct)", "Voice Outbound (UCaaS)", "Voice Internal", "Voice Campaign (Acqueon)", "Voice Campaign (<your brand name>)", and "Agent Scheduled Call".

  * `status` (string): The current status of the call. Possible values include "scheduled", "queued", "connected", "finished", "failed", and "deflected". This tracks the call's progression through its lifecycle.

  * `created_at` (string, date-time): The precise timestamp when UJET created the call record.

  * `queued_at` (string, date-time, or null): The timestamp when the call entered the queue, or null if the call didn't enter the queue.

  * `assigned_at` (string, date-time, or null): The timestamp when UJET assigned the call to an agent, or null if UJET didn't assign the call.

  * `connected_at` (string, date-time, or null): The timestamp when the call connected.

  * `ends_at` (string, date-time, or null): The timestamp when the call ended.

  * `scheduled_at` (string, date-time, or null): The timestamp when UJET scheduled the call, or null if the call was immediate.

  * `updated_at` (string, date-time): The timestamp when UJET last updated the call data.

  * `wait_duration` (integer or null): The total time the consumer spent in queue across the entire call, in seconds, or null if UJET didn't record any queue time. For queue time broken down by individual segment, see the `queue_durations` array (Queue durations). See Versioning and deprecations: Wait-time field nomenclature.

  * `call_duration` (integer or null): The total duration of the call, in seconds.

  * `hold_duration` (integer or null): The total time the consumer spent on hold, in seconds, or null if there was no hold time.

  * `rating` (integer or null): The customer satisfaction (CSAT) rating that the consumer submitted, or null if the consumer didn't submit a rating.

  * `has_feedback` (boolean): A flag indicating whether the consumer provided feedback after the call.

  * `voip_provider` (string): The VoIP provider for the call. (Note: this field is deprecated and always returns "deprecated".)

  * `out_ticket_id` (string or null): The ID of the ticket that UJET created in the external CRM system.

  * `out_ticket_url` (string, uri, or null): The URL of the CRM ticket.

  * `is_out_ticket_account` (boolean or null): Indicates whether the CRM ticket represents a customer (true) or a call interaction (false).

  * `verified` (boolean): Indicates whether the verification smart action verified the interaction.

  * `recording_url` (string, uri, or null): The URL of the call recording, or null if no recording is available.

  * `recording_permission` (string or null): The status of the consumer's recording permission. Possible values: "not_asked", "granted", "denied".

  * `voicemail_reason` (string): The reason for a voicemail, if applicable. Options include "not_voicemail", "temporary_redirection", and "after_hour_deflection".

  * `disconnected_by` (string or null): Indicates which party ended the call. Possible values: `disconnected_by_unknown`, `disconnected_by_agent`, `disconnected_by_end_user`, `disconnected_by_virtual_agent`, `disconnected_by_system`.

  * `fail_reason` (string or null): The reason a call failed, or "nothing" for calls that didn't fail. Possible values include `nothing`, `unknown`, `expired`, `eu_canceled`, `eu_rejected`, `eu_abandoned`, `eu_in_menu_abandoned`, `eu_busy`, `eu_wrong_number`, `eu_no_answer`, `eu_noti_failed`, `ag_canceled`, `ag_ignored`, `ag_mic_no_device`, `ag_mic_denied`, `voip_twilio_error`, `voip_tokbox_error`, `voip_invalid_token`, `voip_conn_general`, `voip_conn_timeout`, `voip_conn_signal`.

  * `fail_details` (string or null): Additional human-readable detail accompanying `fail_reason`, when available.

  * `adapter_fail_code` (integer or null): Numeric code corresponding to `fail_reason` at the call level. Null when the call didn't fail. The same enumeration is used on per-participant `adapter_fail_code` in §17.

  * `adapter_fail_message` (string or null): Human-readable message corresponding to `adapter_fail_code`. Null when the call didn't fail.

  * `support_number` (string or null): The phone number the consumer dialed to reach the contact center, in E.164 format. Populated for IVR-originated calls; may be null for other channels.

  * `queue_priority_level` (integer; present only when queue priority is enabled on your account): The queue priority assigned to the call.




### Agent and virtual agent information

These sections explain who or what handled the call:

  * `agent_info` (object): This field can hold information about either a human agent or a virtual agent. It uses the `oneOf` keyword to specify that it can be one of two types.

    * `agent` (object): Information about the human agent:

      * `id` (integer): The agent's unique ID.

      * `agent_number` (string or null): An identifier assigned to the agent.

      * `email` (string, email): The agent's email address.

      * `name` (string): The agent's full name.

      * `last_name` (string): The agent's last name.

      * `first_name` (string): The agent's first name.

      * `avatar_url` (string, uri): The URL of the agent's avatar image.

    * `virtual_agent` (object): Information about the virtual agent:

      * `id` (integer): The virtual agent's unique ID.

      * `name` (string): The virtual agent's name.

      * `avatar_url` (string, uri, or null): The URL of the virtual agent's avatar image.

      * `va_alias` (string or null): The display alias for the virtual agent, if you set one. Always present in the payload; null when no alias is set.




### Menu navigation

  * `selected_menu` (object or null): Information about the menu that the consumer selected during the call.

    * `id` (integer): The unique ID of the menu.

    * `name` (string): The name of the menu.

    * `parent_id` (integer or null): The ID of the parent menu, if any.

    * `position` (integer): The menu position relative to other menus at the same level.

    * `deleted` (boolean): Whether the menu was deleted.

    * `menu_type` (string): The type of menu (such as `ivr_menu` or `sms_menu`).

    * `hidden` (boolean): Whether the menu is visible and available for use.

  * `menu_path` (object or null): Describes the hierarchical path of menus that the consumer navigated.

    * `items_count` (integer): The number of menus in the path.

    * `name` (string): A slash-separated string of menu names (for example, "Support/Billing").

    * `materialized_path` (string): A slash-separated string of menu IDs.

  * `automation_redirection` (object; present only when the call's first deflection log is associated with a redirection group): Details about percent-based queue redirection that affected this call's routing.

    * `percent_redirection` (boolean): Whether you enabled percent-based redirection on the source menu.

    * `redirection_group` (array): One-element array containing the redirection group details:

      * `group_label` (string): Human-readable label for the redirection group (for example, "Redirection Group 1").

      * `destination` (object or null): The redirection destination that you configured on the group.

      * `after_hours` (boolean or null): Whether you enabled after-hours deflection options on the group.

      * `ah_destination` (object or null): The after-hours redirection destination that you configured on the group.




### End-user details

  * `end_user` (object or null): Information about the consumer:

    * `id` (integer or null): The consumer's internal ID.

    * `identifier` (string or null): An external identifier for the consumer.

    * `out_contact_id` (string or null): The consumer's ID in the CRM.




### Custom and SDK-provided data

  * `customer_flag` (object; present only when website passed custom authentication data): authentication-related custom data attributes that the consumer's app or website passed at the start of the session. The payload includes only the subset that you designate as authentication parameters.

  * `api_dap_request` (object; present only when you enable data parameters and configure them for inclusion in session metadata): A snapshot of the call's data parameter values, as you configure them on your account's external API settings. Keys and value types depend on your data parameter configuration.

  * `form_responses` (array; present only when the consumer submitted at least one form response): Responses that in-call SDK forms collected during the session. Each entry contains:

    * `id` (string or integer): Form response identifier.

    * `title` (string): Form title shown to the consumer.

    * `smart_action_id` (integer or null): Identifier of the smart action that triggered the form, if any.

    * `questions` (array): The collected question and answer pairs.




### Attachments

  * `photos` (array): Photos that the consumer uploaded during the call.

    * `id` (integer): Unique identifier for the photo.

    * `photo_type` (string): Type or source of the photo (such as "photo").

    * `url` (string, uri): URL to the stored photo.

    * `smart_action_type` (string or null): The smart action that produced the photo, if any.

    * `transfer_id` (integer or null): The transfer event ID for the photo, if the consumer uploaded it after a transfer.

  * `videos` (array): Videos that the consumer uploaded during the call.

    * `id` (integer): Unique identifier for the video.

    * `url` (string, uri): URL to the stored video.

    * `smart_action_type` (string or null): The smart action that produced the video, if any.

    * `transfer_id` (integer or null): The transfer event ID for the video, if the consumer uploaded it after a transfer.




### Call deflection

  * `deflection` (string): Indicates if and how the call deflected (for example, "no_deflection", "over_cap_phone", or "after_hours_voicemail").

  * `deflection_details` (array): Provides a detailed log of deflections during the call. The deflection field within each entry uses the enumeration defined in _Definitions: deflection_. Each entry includes:

    * `id` (integer): Unique identifier for the deflection log record.

    * `call_id` (integer): Unique identifier of the call.

    * `transfer_id` (integer or null): Unique identifier of the transfer associated with the deflection, if applicable.

    * `deflection` (string; see Definitions: deflection for allowed values): The type of deflection.

    * `created_at` (string, date-time): Timestamp when the deflection occurred.

    * `from_menu_path` (object or null): Menu path from which the deflection started.

    * `to_menu_path` (object or null): Menu path to which UJET deflected the call.

    * `to_sip_uri` (string; present only when UJET deflected the call to a SIP destination): SIP URI to which UJET deflected the call, if applicable.

    * `to_sip_headers` (object; present only when UJET deflected the call to a SIP destination): SIP headers that UJET deflected the call with, if applicable.




### Transfers

  * `transfers` (array): One entry per transfer event during the call. Records both warm and cold transfers between agents, virtual agents, and menus.

    * `id` (integer): Unique identifier for the transfer.

    * `status` (string): Current status of the transfer (for example, transferring, connected, or failed).

    * `fail_reason` (string): Reason the transfer failed, or "nothing" if it didn't fail.

    * `created_at` (string, date-time): When the transfer started.

    * `assigned_at` (string, date-time, or null): When UJET assigned the transfer to the receiving party.

    * `connected_at` (string, date-time, or null): When the transfer connected.

    * `updated_at` (string, date-time): When UJET last updated the transfer record.

    * `call_duration` (integer): Call duration of the transferred segment, in seconds.

    * `wait_duration` (integer): Time the consumer waited during the transfer, in seconds.

    * `deflection` (string): Deflection type associated with the transfer, if any.

    * `answer_type_path` (string or null): Path describing how the transferred call resolved.

    * `from_menu_path` / `to_menu_path` (object or null): Menu path before and after the transfer; same shape as `menu_path` in _Definitions_.

    * `from_agent` / `to_agent` (object or null): Human agent on each side of the transfer; same shape as the `agent` object in _Definitions_.

    * `from_virtual_agent` / `to_virtual_agent` (object or null): Virtual agent on each side of the transfer; same shape as the `virtual_agent` object in _Definitions_.

    * `from_queue_priority_level` / `to_queue_priority_level` (integer or null): Queue priority before and after the transfer. Present only when you enable queue priority on your account.




### Call handling durations

  * `handle_durations` (array): An array of objects, each representing a segment of the call handled by an agent. This supports analysis of agent handling time.

    * `id` (integer): Unique identifier for the handle duration.

    * `agent_id` (integer): ID of the agent.

    * `acw_duration` (integer): after-call work duration.

    * `bcw_duration` (integer): before-call work duration.

    * `call_duration` (integer): Call duration during this segment.

    * `menu_path_id` (integer or null): ID of the menu path.

    * `menu_path` (string): Name of the menu path.

    * `lang` (string): Language used.

    * `barged` (boolean): Whether the supervisor barged in on the call.

    * `transfer` (boolean): Whether a transfer occurred.

    * `transfer_id` (integer or null): ID of the transfer.

    * `transfer_cold` (boolean or null): Whether the transfer was cold.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time, or null): End timestamp.

    * `scheduled_at` (string, date-time, or null): Scheduled timestamp.

    * `hold_duration` (integer or null): Hold duration during this segment.

    * `assigned_connection_duration` (integer): Duration the consumer waited while the agent connected during this phase.

    * `session_breakthrough` (object; present only when the call broke through an agent's unavailable status): Details on assignment of the call breaking through an agent's unavailable status, if applicable.




### Queue durations

  * `queue_durations` (array): An array of objects, each representing a segment of the call where the consumer was in a queue. This supports analysis of wait times and service levels.

    * `id` (integer): Unique identifier for the queue duration.

    * `agent_id` (integer): ID of the agent.

    * `ended_at` (string, date-time): End timestamp.

    * `lang` (string): Language used.

    * `menu_path_id` (integer): ID of the menu path.

    * `menu_path` (string): Name of the menu path.

    * `queue_duration` (integer): Duration of the queue segment.

    * `started_at` (string, date-time): Start timestamp.

    * `transfer_cold` (boolean): Whether the call cold transferred.

    * `transfer` (boolean): Whether a transfer occurred.

    * `transfer_id` (integer or null): ID of the transfer.

    * `service_level_abandon_time_threshold` (integer): Time threshold for service level abandonment.

    * `service_level_event` (string): Service level event status ("excluded", "in_sla", "not_in_sla").

    * `service_level_target_percent` (integer): Target percentage for service level compliance.

    * `service_level_target_time` (integer): Target time for service level compliance.




### Virtual-agent-to-human escalations

  * `escalations` (array): Each entry represents an escalation from a virtual agent to a human agent.

    * `id` (integer): Unique identifier for the escalation.

    * `status` (string): Current status (for example, escalating, escalated, or failed).

    * `reason` (string): Reason the session escalated.

    * `created_at` (string, date-time): When the escalation started.

    * `escalated_at` (string, date-time, or null): When the escalation completed.

    * `from_virtual_agent` (object or null): Virtual agent that escalated the call. Same shape as the `virtual_agent` object in _Definitions_.

    * `to_agent` (object or null): Human agent the call escalated to. Same shape as the `agent` object in _Definitions_.

    * `from_menu_path` / `to_menu_path` (object or null): Menu path before and after escalation.




### Virtual agent escalations

  * `virtual_agent_deflected_escalations` (array): Details of deflected escalations from virtual agents.

    * `id` (integer): Unique identifier.

    * `deflection` (string): Deflection type.

    * `escalation_id` (integer): Escalation event identifier.

    * `escalation_reason` (string): Reason for escalation.

    * `escalated_at` (string, date-time): Escalation timestamp.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `virtual_agent` (object): Virtual agent details. See Definitions.




### Virtual agent handling durations

  * `virtual_agent_handle_durations` (array): Segments of time when a virtual agent handled the call.

    * `id` (integer): Unique identifier.

    * `virtual_agent` (object): Virtual agent details. See Definitions.

    * `call_duration` (integer): Duration of the segment.

    * `escalation_reason` (string): Reason for escalation.

    * `finish_reason` (string): Reason the interaction finished.

    * `sentiment` (integer): Consumer sentiment.

    * `response_count` (integer): Virtual agent response count.

    * `fallback_response_count` (integer): Fallback response count.

    * `initiated_by` (string): How the virtual agent session started.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `transfer` (boolean): Whether the call transferred.

    * `transfer_id` (integer or null): Transfer event identifier.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time, or null): End timestamp.




### Consumer handling durations

  * `consumer_handle_durations` (array): Durations the consumer was on the call.

    * `id` (integer): Unique identifier.

    * `call_duration` (integer): Consumer segment duration.

    * `hold_duration` (integer or null): Consumer hold duration.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time): End timestamp.




### Consumer event durations

  * `consumer_event_durations` (array): Details of consumer call events (such as CSAT or payment).

    * `id` (integer): Unique identifier.

    * `duration` (integer): Event duration.

    * `type` (string): Event type.

    * `event` (string): Event outcome.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time): End timestamp.




### Consumer in-menu durations

  * `consumer_in_menu_durations` (array): Durations of consumer interactions within menus.

    * `id` (integer): Unique identifier.

    * `duration` (integer): Duration within the menu.

    * `event` (string): Menu interaction outcome.

    * `menu_path_id` (integer): Menu path ID.

    * `menu_path` (string): Menu path.

    * `lang` (string): Language.

    * `started_at` (string, date-time): Start timestamp.

    * `ended_at` (string, date-time): End timestamp.




### Participants

  * `participants` (array): Information about each participant in the call (for example, the consumer, agent, or virtual agent).

    * `id` (integer): Unique identifier for the participant.

    * `type` (string): Type of participant ("end_user", "agent", "virtual_agent", etc.).

    * `entry_type` (string): How the participant entered the call.

    * `user_id` (integer or null): User ID if the participant is an agent.

    * `end_user_id` (integer or null): Consumer identifier if the participant is the consumer.

    * `virtual_agent_id` (integer or null): Virtual agent ID if the participant is a virtual agent.

    * `virtual_agent_params` (object; present only when you configure virtual-agent custom metadata for inclusion): Custom metadata that the virtual agent uses.

    * `status` (string): Status of the participant ("waiting", "connected", "finished", etc.).

    * `fail_reason` (string): Reason for failure, if any.

    * `connected_at` (string, date-time, or null): Timestamp when the participant connected.

    * `phone_number` (string; present only on consumer participants): Phone number of the participant.

    * `call_id` (integer): Identifier for the call.

    * `call_duration` (integer or null): Call duration for the participant.

    * `hold_duration` (integer or null): Hold duration for the participant.

    * `ended_at` (string, date-time, or null): Timestamp when the participant's involvement ended.

    * `adapter_fail_code` (integer or null): Numeric code corresponding to fail reason.

    * `adapter_fail_message` (string or null): Human-readable description of `fail_reason`, if present.

    * `agent_assist` (object; present only on agent participants when you configure agent assist): Active agent assist settings for this participant.

    * `virtual_agent` (object; present only on virtual-agent participants): Details of the virtual agent that serves as this participant — distinct from the top-level `agent_info` and from `virtual_agent_params`.

    * `caller_id` (string; present only when you enable SIP-header caller-ID on your account, and only on consumer participants): Caller ID that UJET extracts from inbound SIP headers for this consumer participant.

    * `sip_headers` (object or null): SIP headers associated with this participant. Always present in the payload; null when UJET doesn't capture headers.

    * `location` (string or null; present only on agent participants): The agent's location.

    * `location_id` (integer or null; present only on agent participants): The location ID.

    * `email` (string, email; present only on agent participants): The agent's email address.

    * `first_name` (string or null; present only on agent participants): The agent's first name.

    * `last_name` (string or null; present only on agent participants): The agent's last name.

    * `middle_name` (string or null; present only on agent participants): The agent's middle name.

    * `teams` (array; present only on agent participants): Array of { id, name } objects for the agent's teams.




### Recordings

  * `recordings` (array): Information about recording call audio.

    * `id` (integer): Unique identifier for the recording.

    * `call_id` (integer): Call identifier.

    * `conference_sid` (string or null): VoIP provider's call identifier.

    * `duration` (integer or null): Recording duration.

    * `recording_type` (string): Type of recording.

    * `redaction_times` (array): Redacted time segments.

      * `start` (string, date-time): When the redaction interval began.

      * `end` (string, date-time): When the redaction interval ended.

      * `duration` (integer): Redaction duration, in seconds.

      * `start_agent_id` (integer or null): The agent who started the redaction.

      * `end_agent_id` (integer or null): The agent who ended the redaction.

    * `started_at` (string, date-time): Recording start timestamp.

  * `post_processed_recordings` (array; present only when you enable post-processed recording on your account): Audio recordings that post-processing produces (such as format conversion or redaction).

    * `id` (integer): Unique identifier for the post-processed recording.

    * `call_id` (integer): Call identifier.

    * `duration` (integer): Recording duration, in seconds.

    * `started_at` (string, date-time): Recording start timestamp.

    * `recording_file_name` (string): Filename of the post-processed audio asset.

    * `recording_url` (string, uri): URL to the post-processed audio file.

    * `agent_id` (integer or string): Identifier of the agent associated with the segment.

    * `virtual_agent_id` (integer or string): Identifier of the virtual agent associated with the segment, if any.

    * `conversation_id` (string): Identifier that correlates this recording with its conversation record.

  * `segments` (array; present only when you enable post-processed insights recordings on your account): Per-participant audio (and optional screen-recording) segments that the system produces for downstream insights pipelines.

    * `id` (integer): Unique identifier for the segment.

    * `call_id` (integer): Call identifier.

    * `duration` (integer): Segment duration, in seconds.

    * `started_at` (string, date-time): Segment start timestamp.

    * `audio_file_name` (string): Filename of the segment's audio asset.

    * `audio_url` (string, uri): URL to the segment's audio file.

    * `agent_id` (integer or string): Identifier of the agent associated with the segment.

    * `virtual_agent_id` (integer or string): Identifier of the virtual agent associated with the segment, if any.

    * `participant_id` (integer or string): Identifier of the participant the segment belongs to.

    * `conversation_id` (string): Identifier correlating this segment to its conversation record.

    * `screen_recording_url` (string, uri, or null): URL to the matching screen-recording asset. Present only when you enable screen recording on your account.

    * `screen_recording_file_name` (string or null): Filename of the screen recording. Present under the same condition as `screen_recording_url`.




### Offer events

  * `offer_type` (string or null): How UJET offered the call to the agent.

  * `offer_events` (array): Events when UJET offered the call to agents.

    * `casting_time` (string, date-time): Time UJET offered the call.

    * `group` (string): Group to which UJET offered the call.




### Other details

  * `answer_type` (string or null): How the call resolved ("manual" or "auto").

  * `outbound_number` (string or null): Outbound phone number used.

  * `wait_time_sms` (array; present only when wait-time SMS interactions occurred on this call): SMS interactions UJET sent to the consumer about expected wait time. Each entry contains:

    * `transfer_id` (integer or null): Transfer event identifier, if associated with a transfer.

    * `status` (string): Status of the SMS. Possible values: `not_triggered`, `triggered`, `triggered_allowed`, `triggered_denied`, `triggered_no_selection`, `triggered_sent`, `triggered_failed`.

    * `received` (boolean): Whether the consumer received the SMS.

  * `in_call_sms` (array; present only when in-call SMS interactions occurred on this call): SMS interactions during the call. Each entry contains:

    * `transfer_id` (integer or null): Transfer event identifier, if associated with a transfer.

    * `preset_sent` (boolean): Whether UJET sent a preset message.

    * `custom_sent` (boolean): Whether the agent sent a custom (free-text) message.

    * `received` (boolean): Whether UJET received an SMS from the consumer.

  * `dispositions` (array; present only when you enable wrap-up codes or notes on your account): Wrap-up codes and notes that agents recorded. Each entry includes dynamically rendered fields based on your wrap-up configuration:

    * `user_id` (integer): Agent identifier.

    * `transfer_id` (integer or null): Transfer event identifier, if recorded after a transfer.

    * `participant_id` (integer): Participant identifier.

    * `note` (string): Free-text agent note.

    * `original_note` (string): Original (pre-edit) version of the note.

    * `code` (string): Disposition code name.

    * `ujet_code_id` (integer or empty string): The UJET ID of the disposition code — a stable key for the code (the code display name can change). Empty string when unavailable.

    * `list` (string): Name of the list the code belongs to.

    * `list_path` (string): Slash-separated path of the code's list.

    * `ujet_list_id` (integer or empty string): The UJET ID of the list the disposition code belongs to — a stable key for the list. Empty string when unavailable.

    * `custom_list_id` (string or integer): Customer-defined list identifier, if mapped.

    * `custom_code_id` (string or integer): Customer-defined code identifier, if mapped.

  * `email` (string, email, or null): Consumer email address.

  * `feedback` (string or null): Consumer feedback.

  * `smart_action_text` (string or null): Text of any smart action taken.

  * `custom_data_secured` (object or null): Custom, securely signed data.

  * `custom_data_not_secured` (object or null): Custom, non-securely signed data.

  * `in_queue_wait_time_va` (array; present only when you enable in-queue wait-time tracking for virtual agents on your account, and only when at least one preserved-VA escalation occurred): Time intervals when the consumer waited in queue while UJET preserved a virtual agent for them after escalation. Each entry contains:

    * `start` (string, date-time): When the queue wait began.

    * `end` (string, date-time, or null): When the queue wait ended; null if it didn't complete.

    * `duration` (integer or null): Wait duration in seconds; null when `end` is null.

  * `auto_session_summaries` (array; present only when you enable conversation summarization on your account and UJET successfully generated a summary): AI-generated session summaries that UJET saves to the CRM record. Each entry contains:

    * `user_id` (integer): Identifier of the agent participant the summary is associated with.

    * `participant_id` (integer): Participant identifier.

    * `session_summary` (string): The summary text.

    * `session_summary_sections` (array or object): The summary in structured sections, if available.

  * `sip_headers` (object; present only when you enable SIP header capture on your account and configure it for inclusion in session metadata): Inbound SIP headers that UJET captured for the call. Keys and values reflect the SIP headers received from the upstream telephony provider.




## Definitions

This section defines each sub-schema once. Property groups that reference the sub-schemas link to these definitions rather than redefining their shapes inline.

### menu_path (object)

Describes a hierarchical menu path the call traversed. See Menu navigation for the full list of its fields.

**Referenced from** : the top-level `menu_path` field; each `transfers[].from_menu_path` and `transfers[].to_menu_path`; each `escalations[].from_menu_path` and `escalations[].to_menu_path`; each `deflection_details[].from_menu_path` and `deflection_details[].to_menu_path`.

### agent (object)

Describes a human agent. This object is one of the two variants of the top-level `agent_info` discriminator (see Schema root). See Agent and virtual agent information for the full list of its fields.

**Referenced from** : the `agent_info` field when a human agent handled the call last; each `transfers[].from_agent` and `transfers[].to_agent`; each `escalations[].to_agent`.

### virtual_agent (object)

Describes a virtual agent. This object is one of the two variants of the top-level `agent_info` discriminator (see Schema root). See Agent and virtual agent information for the full list of its fields.

**Referenced from** : the `agent_info` field when a virtual agent handled the call last; each `transfers[].from_virtual_agent` and `transfers[].to_virtual_agent`; each `escalations[].from_virtual_agent`; each `virtual_agent_handle_durations[].virtual_agent`; each `virtual_agent_deflected_escalations[].virtual_agent`.

### deflection (string, enum)

The deflection state of a call or call segment. Values follow a `&lt;trigger&gt;_&lt;destination&gt;` naming pattern, where the prefix identifies the condition that triggered the deflection (for example, over-capacity, after-hours, or temporary redirection) and the suffix identifies the destination or treatment (for example, voicemail, queue, phone, or message).

**Common destination suffixes** :

  * `_phone` — Routes the call to an external phone number.

  * `_voicemail` — Directs the call to voicemail.

  * `_message` — Plays an informational message.

  * `_message_only` — Plays a message and ends the call without further routing.

  * `_callback` — Offers a scheduled callback.

  * `_wait` — Keeps the caller waiting.

  * `_queue` — Places the call into a different queue.

  * `_sip` — Routes the call to a SIP destination.

  * `_extension` — Routes the call to an extension.

  * `_phone_with_extension` — Routes the call to a phone destination with an extension.




**Allowed values, grouped by trigger family** :

  * No deflection: `no_deflection`, `deflecting`.

  * Over-capacity — when the queue was over its capacity threshold: `over_cap_phone`, `over_cap_voicemail`, `over_cap_callback`, `over_cap_wait`, `over_cap_queue`, `over_cap_message`, `over_cap_sip`, `over_cap_extension`, `over_cap_phone_with_extension`.

  * After-hours — when the call arrived outside the menu's configured operating hours: `after_hours_voicemail`, `after_hours_phone`, `after_hours_message_only`, `after_hours_queue`, `after_hours_message`, `after_hours_sip`, `after_hours_extension`, `after_hours_phone_with_extension`.

  * Temporary redirection — when you configure a temporary redirection on the menu: `temp_redirection_phone`, `temp_redirection_message`, `temp_redirection_voicemail`, `temp_redirection_queue`, `temp_redirection_sip`, `temp_redirection_extension`, `temp_redirection_phone_with_extension`.

  * IVR pre-session: `ivr_presession_deflection`.

  * Virtual-agent-initiated — when a virtual agent redirected or handed off the call: `va_redirection_phone`, `va_redirection_sip`, `va_third_party_phone`, `va_third_party_sip`.

  * Internal-call after-hours: `internal_call_after_hours_message`, `internal_call_after_hours_queue`, `internal_call_after_hours_phone`, `internal_call_after_hours_extension`, `internal_call_after_hours_sip`, `internal_call_after_hours_voicemail`.

  * Internal-call over-capacity: `internal_call_over_capacity_message`, `internal_call_over_capacity_queue`, `internal_call_over_capacity_phone`, `internal_call_over_capacity_extension`, `internal_call_over_capacity_sip`, `internal_call_over_capacity_voicemail`, `internal_call_over_capacity_wait`.

  * Internal-call automatic redirection: `internal_call_automatic_redirection_message`, `internal_call_automatic_redirection_queue`, `internal_call_automatic_redirection_phone`, `internal_call_automatic_redirection_extension`, `internal_call_automatic_redirection_sip`, `internal_call_automatic_redirection_voicemail`.

  * Call-transfer after-hours: `call_transfer_after_hours_message`, `call_transfer_after_hours_queue`, `call_transfer_after_hours_phone`, `call_transfer_after_hours_extension`, `call_transfer_after_hours_sip`, `call_transfer_after_hours_voicemail`.

  * Call-transfer over-capacity: `call_transfer_over_capacity_message`, `call_transfer_over_capacity_queue`, `call_transfer_over_capacity_phone`, `call_transfer_over_capacity_extension`, `call_transfer_over_capacity_sip`, `call_transfer_over_capacity_voicemail`, `call_transfer_over_capacity_wait`.

  * Call-transfer automatic redirection: `call_transfer_automatic_redirection_message`, `call_transfer_automatic_redirection_queue`, `call_transfer_automatic_redirection_phone`, `call_transfer_automatic_redirection_extension`, `call_transfer_automatic_redirection_sip`, `call_transfer_automatic_redirection_voicemail`.

  * Emergency shutdown — when an administrator triggered an emergency shutdown: `emergency_shutdown`, `emergency_shutdown_message`, `emergency_shutdown_after_hours`, `emergency_shutdown_over_capacity`.

  * Dynamic call routing (DCR): `dcr_transferred`, `dcr_missed`, `dcr_redirected`, `dcr_finished`.




**Referenced from** : the top-level `deflection` field; each `deflection_details[].deflection`; each `transfers[].deflection`.

## Versioning and deprecations

The call session metadata schema supports backward-compatible evolution. UJET may add new fields and arrays at any time. Integrations should ignore unrecognized keys to ensure continued functionality. The fields in this section are deprecated, legacy, or soft-superseded. They remain in the payload for backward compatibility, but new integrations must follow the guidance for each field.

### Deprecated fields

  * `voip_provider` (string) — Deprecated. Always returns the literal string "deprecated". UJET no longer surfaces provider information to integrations through this document. There is no replacement field; if your integration needs to identify the upstream telephony provider, contact your account team.



### Legacy duplicates

  * `session_type` (string) — Legacy alias of `call_type`. Always returns the same value as `call_type` and uses the same legacy enum vocabulary. UJET retains this field for backward compatibility with integrations that key on `session_type`. New integrations should parse `call_type` directly, or — for finer-grained inbound distinctions — `session_type_v2` (see Vocabulary evolution below).



### Vocabulary evolution

`call_type` and `session_type_v2` describe the same underlying call type using two different vocabularies. UJET emits both fields on every record; they aren't duplicates of each other:

  * `call_type` uses the legacy enum vocabulary. Values such as `Voice Inbound (App)` and `Voice Inbound (IVR using App)` cover all inbound mobile and in-app SDK origins under a single label. `call_type` isn't deprecated. UJET will continue to emit this field, but its vocabulary won't gain new fine-grained values.

  * `session_type_v2` uses the current enum vocabulary. It introduces finer-grained inbound distinctions — for example, `Voice Inbound (Mobile)` and `Voice Inbound (IVR using Mobile)` — for the call types that have v2-specific values. For call types that don't have a v2-specific value, `session_type_v2` returns the same string as `call_type`.




New integrations should parse `session_type_v2`. The values for each field are listed in Core information.

### Wait-time field nomenclature

The call session metadata document reports queue wait time at two scopes, under two field names:

  * Call total — the top-level `wait_duration` field holds the total time the consumer spent in queue across the entire call.

  * Per segment — each entry in the top-level `queue_durations` array (Queue durations) carries its own `queue_duration` field, holding the queue time for that individual queue segment.




Both names refer to the same kind of measurement — time spent in queue — at different scopes. The call-total `wait_duration` reflects the consumer's overall queue time, while the per-segment `queue_duration` values describe each queue segment. This document doesn't emit a separate top-level `queue_duration` field; per-segment values are available only inside `queue_durations`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
