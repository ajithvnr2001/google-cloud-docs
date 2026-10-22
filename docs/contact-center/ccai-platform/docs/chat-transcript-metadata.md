---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcript-metadata/
title: Chat transcript metadata \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:56.094574+00:00
---

# Chat transcript metadata  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcript-metadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Chat transcript metadata Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the schema of the chat transcript metadata record. This is the JSON file that Contact Center AI Platform (CCAI Platform) generates for a completed chat transcript. The chat transcript metadata record is produced by the chat-history JSON export and can be delivered through CRM transcript uploads and external-storage transcript files, depending on your instance configuration. Use this schema to parse transcript JSON, validate received payloads, or map transcript messages into downstream systems.

## Schema root

The chat transcript metadata record is a single JSON object representing one chat transcript artifact. The fields at the root identify the communication, the transcript format version, and the ordered set of transcript entries.

### Communication identifiers `comm_type` and `comm_id`

Together, `comm_type` and `comm_id` identify the communication that this transcript record represents.

  * `comm_type` identifies the communication type. The value is usually `chat`. It may be `call` for a voice call that includes blended SMS transcript content.

  * `comm_id` is the identifier of the chat or call represented by the transcript.




### Format version `transcript_version`

Identifies the version of the JSON transcript format. Integrations should use this field for forward-compatible parsing and should ignore unrecognized fields.

### Entry discriminator - `entries[].type` and `entries[].body.type`

Each item in `entries` represents one transcript message or event. The entry-level `type` field mirrors the message body type. The nested `body` object carries the payload whose shape varies by type - for example, `text`, `markdown`, `photo`, `noti`, or `action`.

## Chat transcript metadata schema

This schema describes the data structure of chat transcripts. The following sections describe the core components.

### Core transcript information

The following properties provide the fundamental information about the transcript itself:

  * `comm_type` (string): The communication type that the transcript represents. Possible values: `chat`, `call`. The value `call` indicates a voice call with blended SMS transcript content.

  * `comm_id` (integer): Unique identifier of the communication represented by the transcript.

  * `transcript_version` (string): Version of the transcript JSON format. The current value is `"1.0"`. See Versioning and deprecations.

  * `assigned_at` (string, date-time): Timestamp when the chat was assigned.

  * `timezone` (string): Time zone for the transcript context, such as `"America/Los_Angeles"`.




### Transcript entries

  * `entries` (array): Ordered list of transcript entries. Each entry represents one message, notification, or action in the conversation.

    * `timestamp` (integer): Unix epoch timestamp, in seconds, when the system created the entry.

    * `type` (string): Message body type. This value mirrors `body.type`. See Definitions for supported body types.

    * `body` (object): Entry payload. Its shape depends on the value of `type` / `body.type`.

    * `role` (string): Role of the participant or system component that produced the entry. Possible values: `end_user`, `agent`, `manager`, `virtual_agent`, `external_agent`, `task_virtual_agent`, `system`.

    * `user_data` (object): Sender metadata. For `agent`, `manager`, `virtual_agent`, `external_agent`, and `task_virtual_agent` entries, this object contains the sender's display data. For `end_user` and `system` entries, this object is empty.

      * `name` (string; present only when sender metadata is available): Display name of the sender.

      * `id` (integer; present only when sender metadata is available): Identifier of the sender.

      * `avatar_url` (string, uri; present only when sender metadata is available): URL of the sender's avatar image.




### Text message bodies

  * `text` (object): Plain text message body.

    * `type` (string): Always `text`.

    * `content` (string): Message text.

    * `lang` (string; present only when language metadata is available): Language code associated with the message.

  * `text_template` (object): Templated text message body.

    * `type` (string): Always `text_template`.

    * `content` (string): Template text.

  * `markdown` (object): Markdown-formatted message body.

    * `type` (string): Always `markdown`.

    * `content` (string): Markdown content.

    * `lang` (string; present only when language metadata is available): Language code associated with the message.

  * `markdown_template` (object): Templated Markdown message body.

    * `type` (string): Always `markdown_template`.

    * `content` (string): Markdown template content.




### Media and file message bodies

  * `photo` (object): Photo or screenshot message body.

    * `type` (string): Always `photo`.

    * `media_id` (integer): Identifier of the stored photo media.

  * `video` (object): Video message body.

    * `type` (string): Always `video`.

    * `media_id` (integer; present when the system stores the video as CCAI Platform media): Identifier of the stored video media.

    * `title` (string; present when an embedded video object represents the video): Title of the video.

    * `video` (object; present when an embedded video object represents the video): Video details.

      * `url` (string, uri): URL of the video.

      * `text` (string): Text alternative or fallback URL for the video.

  * `image` (object): Image message body.

    * `type` (string): Always `image`.

    * `title` (string; present when the message sender supplies it): Title of the image.

    * `image` (object): Image details.

      * `url` (string, uri): URL of the image.

      * `text` (string): Text alternative or fallback URL for the image.

  * `document` (object): Document message body.

    * `type` (string): Always `document`.

    * `media_id` (integer; present when the system stores the document as CCAI Platform media): Identifier of the stored document media.

    * `title` (string; present when an embedded document object represents the document): Title of the document.

    * `document` (object; present when an embedded document object represents the document): Document details.

      * `url` (string, uri): URL of the document.

      * `text` (string): Text alternative or fallback URL for the document.

  * `audio` (object): Audio message body.

    * `type` (string): Always `audio`.

    * `media_id` (integer; present when the system stores the audio as CCAI Platform media): Identifier of the stored audio media.

    * `title` (string; present when an embedded audio object represents the audio file): Title of the audio file.

    * `audio` (object; present when an embedded audio object represents the audio file): Audio details.

      * `url` (string, uri): URL of the audio file.

      * `text` (string): Text alternative or fallback URL for the audio file.




### Interactive message bodies

  * `inline_button` (object): Inline-button message body.

    * `type` (string): Always `inline_button`.

    * `title` (string): Title to display above the buttons.

    * `buttons` (array): List of button definitions.

      * `title` (string): Button label.

      * `action` (string): Action associated with the button.

      * `link` (string, uri; present only for link-style quick replies): URL associated with the button.

  * `sticky_button` (object): Sticky-button message body.

    * `type` (string): Always `sticky_button`.

    * `title` (string): Title to display above the buttons.

    * `buttons` (array): List of button definitions.

      * `title` (string): Button label.

      * `action` (string): Action associated with the button.

      * `link` (string, uri; present only for link-style quick replies): URL associated with the button.

  * `content_card` (object): Content-card message body.

    * `type` (string): Always `content_card`.

    * `cards` (array): List of content cards.

      * `title` (string): Card title.

      * `body` (string; present only when you configure card body text): Card body text.

  * `form_complete` (object): Form-completion message body that the client sends when a consumer completes, fails, or cancels a form.

    * `type` (string): Always `form_complete`.

    * `signature` (string; present only when the completion event contains a signature): Signature for the form-completion payload.

    * `data` (object): Form-completion details.

      * `status` (string): Completion status. Possible values: `success`, `error`, `cancelled`.

      * `smart_action_id` (integer): Identifier of the smart action associated with the form.

      * `timestamp` (string, date-time): Timestamp when the form-completion event occurred. This is distinct from the entry-level `timestamp`, which is an integer Unix epoch timestamp in seconds.

      * `details` (object; present only when the payload provides additional completion details): Additional status details.

        * `error_code` (string; present only for errors with a code): Error code associated with the completion result.

        * `message` (string): Human-readable status detail.




### Server-generated and passthrough message bodies

  * `server_message` (object): Server-generated message body. The transcript includes `server_message` entries only if you enable task virtual agent transcript content for your account; otherwise, the transcript omits these entries. Use this object when the transcript references a stored server-side message.

    * `type` (string): Always `server_message`.

    * `message_id` (integer): Identifier of the stored server message.

    * `visibility` (string or null): Visibility setting for the stored server message.

  * `passthrough` (object): A custom payload that the system passes through CCAI Platform for a virtual-agent or CCaaS integration. Your integration defines its `content`, which isn't part of the CCAI Platform schema; treat it as opaque.

    * `type` (string): Always `passthrough`.

    * `content` (string or object): Integration-defined payload. Its structure varies by integration, and CCAI Platform doesn't interpret it.




### Action message bodies

  * `action` (object): Action that a virtual agent or chatbot flow requests. The `action` field determines the action payload shape.

    * `type` (string): Always `action`.

    * `action` (string): Action type. Possible values include `escalation`, `deflection`, and `end`.

    * `escalation_reason` (string; present only when `action` is `escalation`): Reason the conversation escalated.

    * `menu_id` (integer; present only when `action` is `escalation`): Identifier of the menu to which the conversation should escalate.

    * `language` (string; present only when `action` is `escalation`): Language code of the destination queue.

    * `deflection_type` (string; present only when `action` is `deflection`): Type of deflection requested.

    * `sip_parameters` (object or null; present only when `action` is `deflection`): SIP parameters to forward as part of the deflection.




### Notification message bodies

  * `noti` (object): Notification message body. Notifications describe system events that occurred during the chat.

    * `type` (string): Always `noti`.

    * `event` (string): Notification event name.

    * `agent` (object; present only for events associated with a human agent): Agent associated with the event.

      * `id` (integer): Agent identifier.

      * `email` (string, email): Agent email address.

      * `name` (string): Agent display name.

    * `from_agent` (object; present only for transfer events with a source agent): Source agent for the event.

      * `id` (integer): Agent identifier.

      * `email` (string, email): Agent email address.

      * `name` (string): Agent display name.

    * `to_agent` (object; present only for transfer or escalation events with a destination human agent): Destination human agent for the event.

      * `id` (integer): Agent identifier.

      * `email` (string, email): Agent email address.

      * `name` (string): Agent display name.

    * `from_virtual_agent` (object; present only for escalation events from a virtual agent): Source virtual agent for the event.

      * `id` (integer): virtual-agent identifier.

      * `name` (string): virtual-agent display name.

      * `avatar_url` (string, uri, or null): URL of the virtual agent's avatar image.

    * `to_virtual_agent` (object; present only for transfer events to a virtual agent): Destination virtual agent for the event.

      * `id` (integer): virtual-agent identifier.

      * `name` (string): virtual-agent display name.

      * `avatar_url` (string, uri, or null): URL of the virtual agent's avatar image.

    * `target` (string; present only for transfer events): Destination type of the transfer. Possible values include `menu` and `agent`.

    * `status` (string; present only for events that carry a chat status): Chat status associated with the event.

    * `timeout` (boolean; present only for timeout-related events): Whether a timeout caused the event.

    * `memberIdentity` (string; present only for participant join or leave events): Identity of the participant.

    * `memberName` (string; present only for participant join or leave events): Display name of the participant.

    * `name` (string; present only for virtual-agent or task-va events): Display name associated with the event.

    * `reason` (string; present only for task-va completion events): Reason the task-va session ended.

    * `escalation_reason` (string; present only for escalation events): Reason for the escalation.

    * `deflection` (object; present only for deflection events): Deflection details.

    * `detail` (object; present only for custom notification events): Custom event detail.

      * `key` (string): Custom event key.

      * `data` (object): Custom event payload.




#### Notification event names

The `event` field identifies the notification event. The chat provider, which serves as the single source of truth, persists all notification events in the following list to the transcript JSON. The list groups these events by family.

#### Smart-action requests

  * `verificationRequested`

  * `photoRequested`

  * `videoRequested`

  * `screenshotRequested`

  * `textRequested`

  * `cobrowseRequestedFromAgent`




#### Smart-action outcomes

  * Finished: `photoFinished`, `videoFinished`, `screenshotFinished`, `textFinished`

  * Canceled: `photoCanceled`, `videoCanceled`, `screenshotCanceled`, `textCanceled`, `cobrowseCanceled`

  * Failed: `photoFailed`, `videoFailed`, `screenshotFailed`, `textFailed`, `verificationFailed`




#### Verification

  * `endUserVerified`



#### Co-browse

  * `cobrowseRequestedFromEndUser`

  * `cobrowseCodeGenerated`

  * `cobrowseStarted`

  * `cobrowseEnded`

  * `cobrowseFailed`




#### Forms

  * `formRequested`

  * `formSent`

  * `formCompleted`




#### Transfers

  * `transferStarted`

  * `transferAccepted`

  * `transferFailed`




#### Virtual-agent escalations

  * `escalationStarted`

  * `escalationAccepted`

  * `escalationDeflected`

  * `escalationFailed`




#### Task virtual agent

  * `taskVaStarted`

  * `taskVaFinished`




#### Membership

  * `memberJoined`

  * `memberLeft`




#### Session lifecycle

  * `chatEnded`

  * `chatEndedWithPostSession`

  * `chatDismissed`

  * `checkInRequired`

  * `checkInTimedOut`

  * `transcriptRequested`

  * `transcriptUpdated`




#### Custom

  * `custom`



For records with `comm_type` set to `call`, additional call-transcript notification events may appear. These events are associated with call or Agent Assist transcript handling rather than the ordinary chat event families.

## Definitions

The following sub-schemas appear in the chat transcript metadata document. This section defines each sub-schema once; property groups that reference them point back to this section rather than redefining their shape inline.

### entry (object)

Represents one transcript message, notification, or action. Each entry has a Unix-epoch `timestamp`, a top-level `type`, a `body` object whose type matches that shape, a sender `role`, and a `user_data` object. See Transcript entries for the full list of fields.

### user_data (object)

Describes the sender of a transcript entry when sender metadata is available. Agent, manager, virtual-agent, external-agent, and task-virtual-agent entries can carry `name`, `id`, and `avatar_url`. Consumer and system entries carry an empty object.

### message body (object, oneOf)

The `body` object on each entry uses the value of `body.type` to select one of the supported message-body shapes. Supported body types include text bodies, media or file bodies, interactive bodies, server-generated bodies, action bodies, and notification bodies. See Text message bodies through Notification message bodies for the full list of documented variants.

### participant role (string, enum)

Identifies the sender category for a transcript entry.

#### Allowed values

  * `end_user` \- The consumer.

  * `agent` \- A human agent.

  * `manager` \- A manager participant.

  * `virtual_agent` \- A virtual agent.

  * `external_agent` \- An external agent participant.

  * `task_virtual_agent` \- A task virtual agent.

  * `system` \- A system-generated entry.




## Versioning and deprecations

The chat transcript metadata document supports backward-compatible schema evolution. The system may add new fields and message-body variants over time, and integrations should disregard any unrecognized keys to ensure continued functionality.

### Current format version

  * `transcript_version` (string) - Current value: `"1.0"`. Integrations should parse the transcript based on the fields present in the payload and shouldn't fail if future versions add new fields or message-body types.



### Unknown message-body types

When a transcript entry contains an unrecognized `type` or `body.type`, preserve the raw entry if possible and continue parsing the rest of the transcript. The system may add new message-body types without changing the meaning of existing fields.

### Deprecated fields

This document does not list any deprecated fields for the chat transcript metadata record.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
