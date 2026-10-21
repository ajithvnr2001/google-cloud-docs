---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes/
title: Contact Center AI Platform release notes \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:58.121147+00:00
---

# Contact Center AI Platform release notes  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ Resources ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes)



Send feedback 

#  Contact Center AI Platform release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Contact Center AI Platform. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/ccai-platform-release-notes.xml) directly. 

## October 19, 2026

Announcement

**Google Cloud CCaaS 6.22**

We've released version 6.22 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Transcript separation for chat**

You can now configure Google Cloud CCaaS to deliver a separate transcript file for each participant segment in a chat, instead of one combined transcript per session. Under **Settings > Chat > Chat Transcript**, select **Per Segment** in **Transcript Separation** to generate individual transcript files for each agent, virtual agent, or supervisor who joins the chat—helpful for identifying which participant handled each part of a transferred or escalated conversation. Your consumers still receive a single, full-chat transcript regardless of this setting.

For more information, see [Chat transcripts and chat history](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts-and-chat-history).

By default, this capability is inactive. Contact Google Cloud Support to turn it on for your instance.

Feature

**Campaign-based scheduled callbacks**

Agents can now schedule a callback during an outbound campaign call. The callback belongs to the campaign, not to an individual agent, and the dialer calls the consumer back in the time slot they chose. Administrators set slot length, capacity, booking window, and expiry for each campaign, and supervisors can track upcoming, completed, and expired callbacks from the campaign list.

For more information, see [Campaign management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-management).

Fixed

This release addresses the following issues:

  * Fixed an issue where direct access point (DAP) greeting messages played twice when a call was deflected to an internal phone number due to queue overcapacity.

  * Fixed an issue where session metadata for top-level menu paths and selected menus was incorrectly displayed in English instead of the user's configured language.

  * Fixed an issue where a failed Salesforce lookup was incorrectly treated as having no matches, which resulted in the creation of duplicate records.

  * Fixed an issue where inbound transfer restrictions remained in force even after being hidden in the administrator interface, causing queues to become silently unreachable for transfers.

  * Fixed an issue where hold music continued to play throughout a call recording after a warm transfer was completed.

  * Fixed an issue where outbound virtual agent audio was prematurely truncated during multi-message turns.

  * Fixed an issue where the **Real-time Monitoring Queues** report didn't accurately count skill-matched agents for skills-based queues, often displaying zero available agents despite their availability.

  * Fixed an issue where calls deflected to an external phone number after entering a queue were incorrectly recorded as abandoned by the customer.

  * Fixed an issue where the credit card tokenizer was missing from the **SmartActions** menu during outbound callback calls.

  * Fixed an issue where mandatory call dispositions were discarded if an agent's voice connection dropped but their session remained active.

  * Fixed an issue where the text resize menu in the chat widget wasn't scrollable at 400% browser zoom, which prevented users from accessing all available text size options.

  * Fixed an issue where the system incorrectly prevented saving automatic call redirection settings when the target was a virtual agent-operated queue.

  * Fixed an issue where duplicate call records were created for a single inbound call, causing incorrect wait times to appear in the real-time queue view.

  * Fixed an issue where empty data attributes caused an error in the agent interface during call connections.

  * Fixed an issue where the **Transfer Restrictions** destination picker provided no feedback when a queue was ineligible, making it indistinguishable from a typo or search error.

  * Fixed an issue where incoming calls were rejected with a SIP 603 error due to high database latency and connection timeouts.

  * Fixed an issue where the documentation for the Apps API and call session metadata schema didn't define the top-level `parentId` and `finishReason` fields.

  * Fixed an issue where certain inbound call failures were incorrectly reported as a busy signal.

  * Fixed an issue where the event processor service crashed during scaling or rebalancing of the system.

  * Fixed an issue where the conversation ID was missing from chat events during active sessions.

  * Fixed an issue where report exports didn't download or remained stuck in a processing state indefinitely.

  * Fixed an issue where agents could transfer calls to queues that were already closed if their transfer list was loaded while the queue was still open.

  * Fixed an issue where queued chats were assigned to agents after the end-user had become unresponsive without being prompted to check in.

  * Fixed an issue where voice calls cold-transferred to an over-capacity queue generated duplicate reporting records and incorrect queue wait times if the callback leg failed.

  * Fixed an issue where direct inbound calls deflected to voicemail during after-hours played three separate audio prompts sequentially.

  * Fixed an issue where a single call was simultaneously assigned to two different agents if the pickup coincided with the cascade timer expiry.

  * Fixed an issue where direct inbound calls weren't projected to agents in a breakthrough-enabled status if another call was already waiting in their queue.

  * Fixed an issue where a gray empty area appeared below the chat container in the agent adapter when the iframe width was narrower than 449px.

  * Fixed an issue where several Kubernetes and Google Cloud service accounts were granted overly broad permissions, which could have allowed for unauthorized privilege escalation.

  * Fixed an issue where an agent's status sequence was recorded in the incorrect order following a brief connection loss during an active chat.

  * Fixed an issue where selecting a contact during a native campaign call didn't automatically open the corresponding record in the CRM.

  * Fixed an issue where AI-generated Smart Disposition suggestions were inconsistently displayed for outbound calls during the wrap-up period.

  * Fixed an issue where call recordings became distorted or garbled when multiple holds were placed during a call.

  * Fixed an issue where audio uploads were accepted based on the file extension rather than the actual file content, which caused call disconnections when incompatible formats were played.

  * Fixed an issue where the call duration timer in the external call adapter didn't match the **In-call** status timer in the agent desktop for inbound calls.

  * Fixed an issue where the sentiment score was incorrectly displayed in the call adapter for calls escalated from a virtual agent, even when the **Sentiment Analysis** setting was disabled.

  * Fixed an issue where duplicate reporting rows were generated for call and wrap-up durations due to concurrent system events.

  * Fixed an issue where agents couldn't sign in or refresh their status if their account was linked to a deleted or unknown status.

  * Fixed an issue where the Manager API documentation for agent activity logs omitted 17 chat routing and activity values, leading to incomplete reporting data for customers.

  * Fixed an issue where IVR custom callback numbers for certain international regions, including Norway and Denmark, were incorrectly dialed with a +1 prefix.

  * Fixed an issue where metadata for calls deflected between virtual agent assignment and connection wasn't exported to the Cloud Storage bucket.

  * Fixed an issue where virtual agent to human chat escalations experienced delays of up to 300 seconds during agent assignment.

  * Fixed an issue where the **Answer** button didn't appear for dial-by-extension calls when other calls were already waiting in an agent's queue.

  * Fixed an issue where a supervisor's name didn't appear in the chat widget when joining a conversation using the monitor then barge workflow.

  * Fixed an issue where ending a chat session in one browser tab didn't automatically close the chat widget in other open tabs.




## October 16, 2026

Announcement

**Advanced reporting dashboards prerelease notes 6.16**

Here are the pre-release notes for updates to the advanced reporting dashboards and other reporting in CCAI Platform. When we release these updates, we expect the new capabilities to be as shown here.

**Important:** The next version of the advanced reporting dashboards could be greater than 6.16.

Fixed

This release addresses the following issues:

  * Fixed an issue where the **Agent Performance** tile on the **Real-time Agent Monitoring** dashboard executed redundant database queries during auto-refreshes.

  * Updated advanced reporting filter prompts so they behave consistently across all dashboards and display the complete list of configured values:

    * List-backed filters now open directly into a searchable list on the first click.

    * Dropdowns that previously returned empty or partial lists now display the full configured list, including **Agent Name** , **Agent Email** , **Agent Custom ID** , **Agent Teams** , **Location** , **Language** , **Answered By** , and **Projection Result**.

    * **Disposition Codes** and **Disposition List** filters now display the codes configured for your instance.

    * **Agent Teams** and **Team Name** filters now match agents in any of their assigned teams.

    * Configuration renames (**Queue Group** , **Queue** , **Agent Team** , **Disposition Code** , **Location** , **Role** , and **Skill**) now appear in filter dropdowns within 30 minutes instead of up to six hours.

    * The **Projecting** filter on the live **Queued** dashboards is now clearable, so you can reset it to show all queued interactions, and offers only **Yes**.

    * Fields without a predefined list of values (such as consumer phone numbers and ID fields) now display a plain text box with an operator so you can type a value directly.

    * **Call Status** and **Deflection Type** filters now display values that existed in the data but were previously missing from the list.

    * **Channel** now reports a value on the live **Voice** and **Chat** dashboards, and on historical **Chat** dashboards, for interaction types that previously appeared blank (including internal, API-initiated, campaign, UCaaS, callback, and extension calls).

    * On the **Agent Audit** dashboard, the **Change Details** table now displays its timestamp column and sorts it correctly.

    * Consumer phone number filters now accept a single value instead of multiple values. Saved filters or links that pass multiple numbers apply only one.

    * On the **Missed Interactions** dashboards, the **Activity Status** column and filter are renamed to **Projection Result**.

    * Actor values describing who answered, ended, or disconnected an interaction are now standardized as **Human Agent** , **Virtual Agent** , **End User** , and **System**. Saved filters, Looks, and schedules that used the previous wording must be reselected.




## October 08, 2026

Announcement

**Google Cloud CCaaS 6.19**

We've released version 6.19 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Fixed

This release addresses the following issues:

  * Fixed an issue where agents could be assigned more concurrent chats than their configured maximum limit when multiple chat offers arrived almost simultaneously.

  * Fixed an issue where calls were unevenly distributed among available agents on skills-based queues.

  * Fixed an issue where supervisor-initiated sign-outs silently discarded mandatory interaction dispositions during an agent's wrap-up period.

  * Fixed an issue where an agent's corporate email address and internal ID were exposed in the browser's network metadata during a virtual agent to human escalation.

  * Fixed an issue where voice calls were incorrectly routed back to the virtual agent queue instead of the intended destination.

  * Fixed an issue where inbound callers experienced a 2-second delay when connecting to an agent.




## October 02, 2026

Announcement

**Google Cloud CCaaS 6.17**

We've released version 6.17 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Warm transfers auto-resume**

When an agent performs a warm transfer, the caller is now automatically taken off hold as soon as the transferring agent leaves the call, establishing two-way audio between the receiving agent and the caller without manual action. The caller stays on hold during the consultation between agents so that their conversation remains private. This applies to warm transfers routed through a queue and warm transfers sent directly to a specific agent. This change eliminates the silence that previously occurred when the caller remained on hold after the handoff.

For more information, see [Warm transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-transfer#warm-transfer).

Fixed

This release addresses the following issues:

  * Fixed an issue where the **Call ended** card in the session data feed incorrectly displayed a call length of `00:00` despite the actual duration being recorded correctly.

  * Fixed an issue where calls remained stuck on the live dashboard after a caller hung up during the transition from a virtual agent to a queue.

  * Fixed an issue where the **Virtual Agent Session Variables** section was missing from the call adapter after a successful credit card tokenization handback.

  * Fixed an issue where agents belonging to multiple teams were incorrectly granted access to all communication channels regardless of their team's specific availability settings.

  * Fixed an issue where emails containing specific formatting displayed a full-screen loading screen that prevented agents from viewing the message or interacting with the agent desktop.

  * Fixed an issue where the CCaaS portal displayed an incorrect **Off** or **Not Configured** status for Agent Assist after navigating between queues or refreshing the page.

  * Added a checkbox for Salesforce CRM integrations that, when selected, ignores ticket owner updates when an agent is assigned.

  * Fixed an issue where the automatic wrap-up timer didn't release agents when notes or disposition codes were configured as optional.

  * Fixed an issue where agents remained stuck in a busy **Wrap-up** status after the automatic wrap-up timer expired if they preselected **Wrap-up** as their next status.

  * Fixed an issue where calls escalated from a virtual agent to an available human agent were incorrectly deflected to the original queue's voicemail upon reaching a timeout.

  * Fixed an issue where callers were left on hold indefinitely during cold transfers to a direct agent extension when over-capacity deflection was enabled.

  * Fixed an issue where virtual agent interaction outcomes weren't fully mapped, leading to sessions being incorrectly categorized as "Undefined" or "Unknown".

  * Fixed an issue where Agent Assist message analysis background jobs failed and retried excessively for certain profiles.

  * Fixed an issue where transcript message updates caused excessive background processing load.

  * Fixed an issue where the microphone permission error was mistranslated as "Microphone désactivé!" instead of "Microphone turned off!" for agents using French (Canada) localization in the agent adapter.

  * Fixed an issue where calls meeting over-capacity deflection criteria didn't reach their destination queue, leaving callers connected without a route.

  * Fixed an issue where queue duration metrics weren't captured for scheduled callbacks escalating from a virtual agent to a human agent.

  * Fixed an issue where virtual agent conversations remained open after a call ended due to missing wrap-up events.

  * Fixed an issue where virtual agent voice sessions remained active after a caller disconnected, resulting in delayed error logs appearing 10 to 15 minutes after the call ended.

  * Fixed an issue where agents were incorrectly marked as **Unresponsive** because call offers were sent before their browser finished transitioning from a previous call.




## September 30, 2026

Announcement

**Headless mobile SDK**

The headless mobile SDK, for Android and iOS, is now available. With this SDK, you can embed the capabilities of Google Cloud CCaaS into your mobile app while retaining full control over the UI. The headless mobile SDK supports calls (including scheduled calls), chats, and email.

The following is a comparison of the headless mobile SDK and the mobile SDK v2.

Headless mobile SDK:

  * Google Cloud CCaaS provides the core SDK engine: sessions, routing, channel logic, and more.

  * You build the UI using your own design and components.

  * Best for organizations that need brand consistency and full control over the look and feel of their mobile app.




Mobile SDK v2:

  * Google Cloud CCaaS provides a pre-built UI with customization options.

  * Best for organizations that want faster product deployment with less design and engineering effort.




For more information, see the following:

  * [Headless Mobile SDK v3 for iOS: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-ios-getting-started)

  * [Headless Mobile SDK v3 for Android: Get started](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-mobile-sdk-android-getting-started)




## September 25, 2026

Announcement

**Advanced reporting dashboards 6.14**

We've released version 6.14 of the advanced reporting dashboards.

Feature

**Two new tables in the Real-time Queue Monitoring - Calls dashboard: Today's Scheduled Calls and Upcoming Scheduled Calls**

We've added two new tables to the **Real-time Queue Monitoring - Calls** dashboard: **Today's Scheduled Calls** and **Upcoming Scheduled Calls**. These tables display pending scheduled calls across your allowed scheduling window, regardless of when they were initially created. The tables provide actionable details for each scheduled call, including the time until the call is due, an overdue flag, and a direct CRM link to the scheduled call. With these tables, you can view your full schedule of pending callbacks to help you plan staffing.

For more information, see [Queue monitoring dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor).

Fixed

This release addresses the following issues:

  * Fixed an issue that caused delays when loading and refreshing real-time agent dashboards.

  * Fixed an issue where the **Queue Group** and **Queue Name** filters inflated agent counts by including historical, rather than just current, queue assignments. If you have alerts or thresholds based on the previously inflated counts, update them to reflect the new, accurate counts.

  * Fixed an issue where certain queues were incorrectly mapped or dropped entirely from **Queue Group** filter results.

  * Fixed an issue where the **Is Inbound Call** and **Is Inbound Chat** columns in the **Live Agent Data** table on the **Real-time Agent Monitoring** dashboard displayed inverted values, incorrectly showing `No` for inbound interactions and `Yes` for outbound. This update also standardizes how interaction direction is defined across all reports, ensuring accurate classification and filtering for API-dialed calls, scheduled callbacks, and direct inbound calls. Additionally, it introduces several enhancements to reporting dashboards to ensure accurate timezone formatting, correct CSAT population by direction, and proper queue time tracking for newer call types.

  * Fixed an issue where the **Queue Time** column of the **Queued Calls** tile in advanced reporting displayed inflated wait times for calls that re-entered a queue after being answered or transferred. 

  * Fixed an issue where agents performing mandatory after-call work were incorrectly classified as "In-Call" instead of "Wrap-up" on real-time reporting dashboards. You can expect a decrease in active "In-Call" agent counts and a corresponding increase in "Wrap-up" statuses across your live monitoring views. This change only affects dashboard reporting and doesn't affect agent routing or historical data. No action is required.

  * Fixed an issue where the SLA Target on the **Real-time Channel Performance** dashboards appeared blank for queues with no recent activity or when filters matched no configured queues.

  * Fixed an issue where the **Missed Interactions** dashboards double-counted declined calls and inflated missed chat volumes by incorrectly including agent response-time alerts. You can expect chat volumes to drop and average missed chat time to rise.

  * Fixed an issue where selecting the **Subtotals** option for call queue metrics for a Look returned an error.

  * Fixed an issue in downloadable call and chat history reports where French-language calls incorrectly appeared under English queue names.

  * Fixed an issue where scheduled calls disappeared from real-time reporting dashboards 12 hours after their creation, which caused the metric to undercount the total number of upcoming scheduled calls.




  * Fixed an issue where filter options for agent and team data in advanced reporting dashboards weren't correctly scoped to the user's assigned permissions.

  * Fixed an issue where the **Agents** monitoring page became unresponsive when displaying large numbers of agents, causing significant latency when navigating to other pages.

  * Fixed an issue that caused the following problems with raw data exports:

    * Poor export performance due to inefficient database queries.

    * In the `call_recordings` export, the `url` field incorrectly contained a timestamp instead of the actual recording URL.

The `url` field now contains the correct recording URL, and the timestamp has been moved to a newly added `updated_at` field. If you ingest `call_recordings` data using a fixed schema, update your data mappings to accommodate these changes.




## September 23, 2026

Announcement

**Google Cloud CCaaS 6.15**

We've released version 6.15 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Remove a user from all teams at once**

Using the new **Remove from all teams** button, you can remove a user from all of the teams that they belong to.

Administrators: There's a new **Remove from all teams** button in the **Teams** section of the **Edit User** dialog.

For more information, see [Remove a user from teams](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user#remove-user-from-teams).

Fixed

This release addresses the following issues:

  * Fixed an issue that led to increased startup latency and errors for mobile and web chat sessions.

  * Fixed an issue where agents were incorrectly demoted to an **Unresponsive** status and removed from the routing pool despite successfully receiving call offers.

  * Fixed an issue where dialed numbers on Twilio BYOC SIP inbound calls were incorrectly formatted with extra digits from the SIP host and port.

  * Fixed an issue that prevented chat transcripts from being generated and delivered for sessions containing structured message content.

  * Fixed an issue where the call adapter incorrectly showed a call as on hold after a carrier failed to process the hold request, leaving the audio channel open between the agent and the customer.

  * Fixed an issue where a failed media download caused the service to restart unexpectedly.

  * Fixed an issue that caused queue-specific wrap-up and disposition settings to reset to global defaults after changing unrelated fields on the **Queue Settings** page.

  * Fixed an issue where machine translation didn't activate for chats that were transferred into a non-English language queue if the session originated with a virtual agent.

  * Fixed an issue where generative knowledge assist answers that contain long URLs were cut off at the edge of the panel.

  * Fixed an issue where queued calls were neither routed to available agents nor offered a callback.

  * Fixed an issue where voicemails were automatically dismissed and marked as read if a playback error occurred.

  * Fixed an issue where agent call recordings were missing or attached to the wrong call record after a virtual agent deflection.

  * Fixed an issue where unanswered DCR calls that were routed using Nexmo disconnected the caller instead of requeuing the call.

  * Fixed an issue that prevented virtual agents from transferring calls to a human-agent queue.

  * Fixed an issue where calls lacking a carrier hangup reason were incorrectly categorized as "customer abandoned", even when the call center didn't answer the call.

  * Fixed an issue where the call event API payload for DCR calls contained incorrect virtual agent parameters.

  * Fixed an issue where custom data from chat interactions wasn't recorded in Salesforce records.

  * Fixed an issue where Mexico time zones were incorrectly applying daylight saving time adjustments.

  * Fixed an issue where agents and end-users were joined to separate conferences, preventing audio communication between them.

  * Fixed an issue where call recording deletion tasks entered an endless loop if the provider didn't return a successful response.

  * Fixed an issue where IVR voice calls didn't send custom wrap-up events to Dialogflow CX under certain configurations.

  * Fixed an issue where a trailing slash in the host URL caused the web SDK to unexpectedly re-enable features that had been previously disabled for specific deployments.




## September 18, 2026

Announcement

**Google Cloud CCaaS 6.13**

We've released version 6.13 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Fixed

This release addresses the following issues:

  * Fixed an issue where session metadata and data feed files were missing from external storage for chats that ended before the first message from the end-user.

  * Fixed an issue with Kustomer integrations where the caller's information didn't appear on the **Incoming call** page of the call adapter for direct-line inbound calls.

  * Fixed an issue with inbound mobile calls where the end-user leg of the call failed, returning `Unknown error`, while the agent leg connected normally.

  * Fixed an agent desktop issue where live call and chat data were lost.

  * Fixed an issue that occurred when the receiving agent in an agent-to-agent transfer didn't answer the call. The receiving agent was marked as active on the call indefinitely, even after the call ended.

  * Fixed an issue where the **Dismiss** button remained active after an agent sent a message, resulting in a 409 error when clicked.

  * Fixed an issue where duplicate "chat finished" events were reported when the end-user left a chat session at nearly the same time that the agent ended the chat session.

  * Fixed an issue where deflected calls were missing from the **All Call History** and **Voice Inbound (IVR) History** reports.

  * Fixed an issue that occurred when a direct inbound call was deflected to the agent's overcapacity queue, then that queue redirected to a SIP URI. The SIP redirect didn't include the custom SIP headers.

  * Fixed an issue where an in-queue announcement interval of several minutes for inbound IVR calls was incorrectly reduced to approximately 60 seconds.

  * Fixed an issue where calls that agents were unable to answer due to microphone failures were incorrectly reported as "picked up" in the **Agent Activity Timeline** report.

  * Fixed an issue where the system incorrectly marked agents as still being on a call after it ended, which either prevented them from changing their status to **Available** or silently blocked them from receiving new calls.

  * Fixed an issue where processing delays for ended calls caused timeout errors.

  * Fixed an issue where a sudden spike in calls bypassed capacity limits, causing agent availability to drop below required minimums.

  * Fixed an issue where the **Agent Activity Timeline** report incorrectly attributed manual agent logins and logouts to **System** instead of the appropriate agents.

  * Fixed an issue where calls with a missed offer became permanently stuck in the queue, preventing them from being routed to other available agents. This occurred with queues configured with multicast fallback disabled.

  * Fixed an issue where manual or cascade outbound calls that were canceled before connecting were missing from team-filtered **Call History** reports.

  * Fixed an issue that prevented over-capacity deflection from triggering when an agent warm-transferred an outbound call to a queue.

  * Fixed an issue where calls weren't correctly routed to the top-ranked agent when using agent priority overrides.

  * Fixed an issue where escalated voice calls were incorrectly reported as both answered and abandoned.

  * Fixed an issue where calls were missing from the **All Call History** and **Voice Inbound History** reports if the caller hung up before leaving a voicemail.

  * Fixed an issue where Salesforce click-to-dial outbound calls were incorrectly associated with the most recent open case instead of the case from which the call was initiated.

  * Fixed an issue where email accounts remained disconnected indefinitely after a temporary authentication failure.

  * Fixed an issue in Agent Assist where long periods of silence during calls caused connection timeouts, triggering false-positive error alerts.

  * Fixed an issue where the **arrow-down-icon** and **arrow-up-icon** arrows on the **Agents > Filter Settings** page were rendered at an incorrect scale.

  * Fixed an issue where incoming calls incorrectly created duplicate Salesforce accounts instead of linking to existing accounts.

  * Fixed an issue where the outbound call queue list displayed stale information, potentially causing calls to be placed in a queue that didn't match the agent's selected language.

  * Fixed an issue where the menus for transferring calls and forwarding calls to voicemail appeared in English instead of the agent's selected language.

  * Fixed an issue where the wrap-up disposition panel froze after a network reconnection even though the submission had completed successfully.

  * Fixed an issue where outbound, click-to-dial calls initiated in Salesforce incorrectly linked to and reassigned ownership of other cases associated with the same phone number.

  * Fixed an issue where the agent adapter went blank and prevented new calls from reaching the agent if an end-user hung up immediately after the agent received the call notification.

  * Fixed an issue where calls that failed to connect got stuck in a silent 'connecting' state in the call adapter.

  * Fixed an issue where Salesforce CRM connections dropped for organizations enforcing OAuth Refresh Token Rotation.

  * Fixed an issue where part of an agent's audio was dropped from recordings when a virtual task assistant ran in the middle of a call.

  * Fixed a web SDK issue where menus in the pre-chat and chat screens didn't comply with WAI-ARIA keyboard navigation standards.

  * Fixed a web SDK issue where screen readers couldn't identify the purpose of the **Text size** options for the chat screen.




Announcement

**Advanced reporting dashboards 6.4**

We've released version 6.4 of the advanced reporting dashboards.

Feature

**Real-time Agent Monitoring dashboard: new Active call ID(s) column**

The **Real-time Agent Monitoring** dashboard now has an **Active Call ID(s)** column in the **Live Agent Data** table. The column displays the call ID(s) for any call in a connecting, connected, or reconnecting state for the agent. If an agent is handling multiple concurrent calls, the call IDs appear in a comma-separated list. The **Active Call ID(s)** column reduces the number of steps required for supervisors to identify active calls during live monitoring.

Feature

**Improved filtering by team**

We made the following changes to team-based filtering:

  * Renamed the **Teams** filter to **Agent Teams** to clarify that it filters by the agent team handling the interactions. This change is in the **Real-time Queue Monitoring - Calls** , **Real-time Queue Monitoring - Chats** , **Real-time Connected - Calls** , and **Real-time Connected - Chats** dashboards. For more information, see [Queue monitoring dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor), [Real-time Connected - Calls dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-calls-connected), and [Real-time Connected - Chats dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-chats-connected).

  * Added a **Queue Teams** filter to the **Real-time Queued - Calls** and **Real-time Queued - Chats** dashboards. This lets you filter queued interactions by the team assigned to the queue.




Feature

**Improved the Real-time Calls and Real-time Chats dashboards**

We made the following dashboard improvements:

  * **Real-time Calls - Calls Connected dashboard**. Added the following columns to the **Connected Calls** table:

    * **Total Consumer Talk Time**. Total time since the call first connected to a virtual agent or a human agent.

    * **Total Hold Time**. Total time the call has spent on hold so far, including a hold currently in progress. 

  * **Real-time Chats - Chats Connected dashboard**. Added the following column to the **Connected Chats** table:

    * **Total Consumer Chat Time**. Total time since the chat first connected to a virtual agent or a human agent.



Feature

**Real-time Calls - Calls Queued dashboard: new Projecting column**

The **Real-time Calls - Calls Queued** dashboard has a new **Projecting** column in the **Call Queued** table. Indicates whether the routing engine (deltacast) is currently projecting this queued call to an available agent.

Feature

**Advanced reporting available in French Canadian**

All advanced reporting dashboards and Explores are now available in French Canadian. When you select French Canadian as your profile language in the CCAI Platform portal, these dashboards and Explores display in that language.

Administrators: There's a new **Français (CAN)** option when you click **Admin > Change Language** in the CCAI Platform portal.

Fixed

This release addresses the following issues:

  * Fixed an issue where the formatting of numeric values was inconsistent across tiles.

  * Fixed an issue where column headers, filter labels, and tile titles didn't immediately switch to a newly selected language.

  * Fixed an issue where the **Productive Agents** column in the tables of the **Queue Group Performance - All** dashboard didn't display values appropriate to the queue group settings.

  * Fixed an issue in the **Call Queue Metrics (Historical)** Explore where filtering by **Agent Name** without including it as a visible column resulted in zero rows being returned.

  * Fixed an issue that affected calls to a sub-menu that were deflected using **Custom After Hours Deflection** to a message. These calls were incorrectly attributed to the parent menu in the **All Queued Interactions** report.

  * Fixed the effectiveness of the **Direction** filter in the following dashboards:

    * **Agent Performance**. The **Agent Productivity Detailed – Calls** and **Agent Productivity Detailed – Chats** tables correctly reflect the filter setting.

    * **Real-time Agent Monitoring**. The **Agent Performance** table and historical metrics tiles correctly reflect the filter setting.

    * **All Interactions – Calls** and **All Interactions – Chats**. The **IVR Interactions** (calls only) and **Virtual Agent Interactions** tables correctly reflect the filter setting.

  * Fixed an issue with the **Queue Performance - Calls** dashboard when short abandons were present in the specified date range. The **Avg Queue Time** column in the **Queue Summary** table incorrectly displayed the raw sum of queue durations instead of a true average.

  * Fixed an issue where team filters didn't apply correctly when generating the **Individual Call History Report** and the **Individual Chat History Report**. This resulted in the inclusion of data from unmanaged queues.

  * Fixed an issue where French Canadian translations for several dashboard metrics and labels were incorrect, incomplete, or missing.

  * Fixed the following issues with the **Real-time Calls - Calls Queued** dashboard:

    * The **Total Queued Now** metric didn't include callers who were returned to the queue after an automated-answer detection miss.

    * The **Current Max Queue Wait Time (H:M:S)** and **Current Avg Queue Wait Time (H:M:S)** metrics mistakenly measured from a caller's original entry into the queue, rather than from their most recent return to the queue.

  * Fixed an issue where a gray bar appeared at the bottom of the advanced reporting dashboards, preventing a full view of the dashboards.




## September 15, 2026

Announcement

**Mobile SDKs 2.16.2**

We've released version 2.16.2 of the mobile SDKs.

Feature

**Chat check-in for the Mobile SDKs**

Chat check-in is now available for the mobile SDKs. Chat check-in ensures that end-users are present and ready to engage before the system connects them to a human agent. This decreases the average agent handle time by eliminating the time lost when agents wait for end-users who have abandoned a chat.

For more information, see:

  * [Chat check-in](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-check-in)

  * [SDK configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#sdk-configuration) (Android)

  * [Chat check-in after-hours options](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#chat_check-in_after-hours_options) (iOS)




Feature

**New "is typing" indicator in the Mobile SDKs**

The mobile SDKs now display an "is typing" indicator to the end-user when an agent is typing.

Fixed

We've addressed the following issues.

Android and iOS SDKs:

  * Fixed an issue that occurred after force-closing a mobile app while the check-in timeout dialog was displayed. When the app was relaunched, the check-in dialog didn't reappear.

  * Fixed an issue where mobile inbound calls didn't connect.




iOS SDK only:

  * Fixed an issue where end-users received duplicate end-of-chat notifications when a virtual agent ended a conversation.

  * Fixed an issue where a virtual agent's final message appeared out of order during a chat escalation.

  * Fixed an issue where apps didn't upload logs when the server returned a relative URL.




Android SDK only:

  * Fixed an issue where a five-second delay occurred between session creation and the initial chat fetch, significantly delaying when the message appeared.



## September 11, 2026

Announcement

**Google Cloud CCaaS 6.12**

We've released version 6.12 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Cold transfers auto-resume**

When an agent performs a cold transfer, the call now resumes at the moment the receiving agent answers the call. The receiving agent no longer needs to manually take the caller off hold. This eliminates the silence that previously occurred between an agent answering a call and taking the caller off hold.

For more information, see [Cold transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-transfer#cold-transfer).

Feature

**Hubspot: Configure Do Not Call by phone number**

In HubSpot integrations, you can now configure Do Not Call for specific phone numbers instead of for an entire contact or company record. Opt-out matching is no longer case-sensitive.

Administrators: There's a new **Do Not Call Configuration** section in the **CRM** pane, located at **Settings > Developer Settings** (with **HubSpot** selected).

For more information, see [Configure Do Not Call for HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-do-not-call).

Feature

**Agent desktop: New network diagnostics tool**

The agent desktop has a new network diagnostics tool in the navigation menu that displays network strength and diagnostics information. This tool can help you quickly assess your network's health and troubleshoot connection issues.

For more information, see [Get network diagnostic information](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop#get-network-diagnostic-information).

Feature

**Agent desktop: Open from the CCaaS portal**

You can now access the Agent Desktop using the new **Apps** menu. In the CCaaS portal, click **Apps > Agent Desktop** to open the Agent Desktop in a new browser tab. This lets you move between the portal and the Agent Desktop without ending your portal session.

For more information, see [Open the agent desktop](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop#open-agent-desktop).

Fixed

This release addresses the following issues:

  * Fixed an issue where SmartAction statuses were incorrectly marked as "failed" when a call ended before a photo or video upload completed.

  * Fixed an issue where loading the outbound numbers list timed out or caused significant delays for organizations with large teams and custom roles.

  * Fixed an issue where estimated wait times of less than one minute were incorrectly rounded down to zero, preventing the system from accurately triggering over-capacity actions.

  * Fixed an issue where sudden spikes in call volume bypassed a team's capacity protections and reduced the team's agent availability to below configured minimums.

  * Fixed an issue where nested object values in custom data were incorrectly displayed as `[object Object]` in the agent desktop session data feed.

  * Fixed an agent desktop issue where the navigation bar in the **Previous Interactions** page of the call adapter was overlapped by summary text and didn't stay fixed while scrolling.

  * Fixed an issue where answered voice calls triggered a second, unrequested callback after the end-user hung up.

  * Fixed an issue where intermittent IMAP connection rejections caused email fetch workers to enter an extended backoff loop, resulting in several hours of mailbox downtime.

  * Fixed an issue where inbound voice call recordings weren't exported to external storage when a virtual agent escalation was deflected to voicemail due to over-capacity.

  * Fixed an issue where manual wrap-up sessions were incorrectly attributed to the most recent call in the **Agent Activity Timeline** and in raw data exports, even when the wrap-up was unrelated to that call.

  * Fixed an issue where the "agent leg" of a call connection stalled in a connecting state for the full timeout duration before failing silently and moving the agent to an available status.

  * Fixed an issue where custom form responses weren't exported to external storage for instances without an external CRM integration.

  * Fixed an issue where a queue name saved in the **SLA thresholds for queues** dialog didn't persist after saving.

  * Fixed an issue where virtual agent voice calls triggered a session error during wrap-up.

  * Fixed an issue during high-capacity redirections where voicemails weren't saved.

  * Fixed an issue where completed call transfers generated duplicate queue duration records, leading to inflated reporting for queue volume and SLA metrics.

  * Fixed an agent desktop issue where the sentiment banner in the call adapter didn't immediately appear at the start of a call.

  * Fixed an issue where saving the **Upload audio recording for Language Selection** option of the **Languages** dialog didn't persist and switched to **Text-to-speech**.

  * Fixed an issue where inefficient database queries caused high CPU utilization and performance degradation across all communication channels.

  * Fixed an issue where transient connection errors during Twilio ICE token fetching caused agent call setup to fail or take longer to connect.

  * Fixed an issue where temporary connection drops during chat webhook delivery caused unnecessary delays.

  * Fixed an issue where work time and wait time durations overlapped in reporting metrics.

  * Fixed an issue where the agent adapter call history incorrectly displayed English queue names for French-Canadian calls.

  * Fixed an issue where agents were assigned calls from secondary queues even when their primary queue fell below the minimum availability threshold.

  * Fixed an issue where canceled virtual-agent-to-human escalations incorrectly reported negative queue durations and inaccurate SLA metrics in chat session data and reports.

  * Fixed an issue where creating or updating queues failed and returned a timeout error.

  * Fixed an agent desktop issue where an outbound call canceled by an agent while connecting was recorded as an unknown failure instead of an agent cancellation.

  * Fixed an issue where clicking the rewind and forward buttons on the voicemail page of the call adapter restarted the voicemail from the beginning.

  * Fixed an agent desktop issue where the chat adapter displayed a loading progress indicator instead of the chat transcript when a chat session was assigned.

  * Fixed an issue where a disposition prompt didn't appear in the call adapter after a disconnected call, even when mandatory disposition was configured.

  * Fixed an issue where Agent Assist real-time transcription didn't start on Vonage BYOC calls.

  * Fixed an issue where changes made outside of browser-originated HTTP requests (such as from API clients or background jobs) failed to generate audit log records.

  * Fixed an issue where over-capacity phone deflection didn't activate for direct agent calls, resulting in an error message or callers waiting indefinitely.

  * Fixed an issue where transient network connection failures during call and chat DAP lookups caused inbound calls to route to default queues or prevented chat sessions from starting.

  * Fixed a web SDK issue where static, non-interactive text within the chat widget incorrectly received keyboard focus, disrupting the navigation flow for keyboard and screen reader users.

  * Fixed an issue where temporary asset errors during deployments were cached by the CDN, leading to web SDK initialization failures.

  * Fixed an agent desktop issue where incomplete configuration settings prevented call control buttons from updating or rendering properly.

  * Fixed an issue where the audio for an over-capacity deflection played in the source queue's language instead of the destination queue's language following a cross-language transfer.

  * Fixed an issue where waiting chats weren't immediately offered to available agents who became eligible for a queue through a team membership update or direct queue assignment.




## September 03, 2026

Announcement

**Google Cloud CCaaS 6.9**

We've released version 6.9 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Agent desktop supports email**

The agent desktop now supports email. Agents can handle email interactions using the email adapter in a desktop layout.

Administrators: There's a new **Email Adapter** checkbox in the following locations:

  * The **Desktop Layout Builder** dialog at **Settings > Operation Management > Agent Desktop > Manage Desktop Layout Lists > Add desktop layout**.

  * The **Desktop Layout Builder** at **Settings > Operation Management > Agent Desktop > Manage Desktop Layout Lists > Add desktop layout > Next**.




User experience change: There's a new **new emails** menu in the menu bar of the agent desktop.

For more information, see [Create a desktop layout](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts#create-desktop-layout) and [Handle an email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-use-agent-desktop#handle-an-email).

Fixed

This release addresses the following issues:

  * Fixed an issue where agents couldn't send new outbound emails.

  * Fixed an issue where the disposition panel in the call adapter was incorrectly hidden or visible due to inconsistent state updates.

  * Fixed an issue where direct inbound voicemails appeared multiple times in the **History** tab of the call adapter.

  * Fixed an issue where voice callbacks were canceled at the end of operating hours instead of rolling over to the next day.

  * Fixed an issue where using click-to-dial from a Salesforce case incorrectly overwrote the parent account's mobile phone number with the dialed number.

  * Fixed an issue where ending a call resulted in significant latency or connection errors in the instance.

  * Fixed an issue where hold music in call recordings overlapped live conversation.

  * Fixed an issue where the deletion of a custom hours of operation group didn't appear in the **Audit Dashboard**.

  * Fixed an issue in Zendesk integrations where the system mistakenly navigated from the active ticket tab to the customer profile page when a voice call ended.




## August 27, 2026

Announcement

**Google Cloud CCaaS 6.7**

We've released version 6.7 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Bulk email status updates**

You can use the new `apps/api/v1/email/update_status` endpoint to change the status of multiple email sessions to the status that you specify.

The new endpoint includes the following capabilities:

  * You can optionally specify the status that you expect email sessions to be in. Email sessions that aren't in that status aren't updated.

  * For each email session, the response reports whether it was updated, required no change, or couldn't be updated (and why). This means that integrations can handle partial success and identify which sessions still need attention.




For more information, see [Bulk email status endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-email-status-endpoint).

Fixed

This release addresses the following issues:

  * Fixed an issue where blended SMS transcripts were incorrectly identified as call audio recordings when uploaded to Customer Experience Insights, causing them to appear as missing or unanalyzable data.

  * Fixed an issue where the chat text-input field was unresponsive after an agent accepted a new chat.

  * Fixed an issue where call-cascade agent availability safeguards weren't enforced for terminal queue paths, which resulted in agents being assigned calls from secondary queues even when their primary queue fell below the minimum availability threshold.

  * Fixed an issue where chats that were connected to an agent continued to appear on the **Queued Chats** dashboard with a status of **Ongoing**.

  * Fixed an issue where direct inbound and dial-by-extension calls didn't reach an agent when multiple calls were waiting in the agent's queue.

  * Fixed an issue where chat messages from supervisors were incorrectly attributed to the end-user in Customer Experience Insights transcripts.

  * Fixed an issue where changes to hours of operation didn't appear in the **Audit Dashboard**.

  * Fixed an issue with Salesforce integrations where outbound calls were incorrectly labeled as **Inbound** and didn't pass the CCAI Platform call ID into Salesforce case activity comments.

  * Fixed an issue where requests for agent activity logs resulted in high database latency and gateway timeouts.

  * Fixed an agent desktop issue where an agent sent a chat form to an end-user but the end-user didn't receive it.

  * Fixed an issue where a chat that was escalated from a virtual agent to a human agent was stuck in the queue and couldn't be successfully offered to available agents.

  * Fixed an issue where the **Queue** dashboard displayed `{{Count}}` and `{{Level}}` variables instead of numerals.

  * Fixed an issue where the wait times API incorrectly reported zero available agents for chat queues that had agent availability.

  * Fixed an issue where the **Queues > Calls** dashboard didn't load and timed out for instances with a large number of queues.

  * Fixed an agent desktop issue where the sentiment score didn't appear in the call adapter in the agent desktop or in Salesforce for calls that were escalated from a virtual agent to a human agent.

  * Fixed an issue where newly created voice queues didn't correctly inherit the global whisper and countdown settings.

  * Fixed an issue where queue duration metrics incorrectly included IVR timeout time for calls that were cold transferred into a closed queue.

  * Fixed an issue where an agent who reopened a previously read voicemail was stuck in **In-call** status, preventing them from accepting new contacts or changing their status.

  * Fixed an issue where an agent's assigned call ID was cleared during wrap-up, which prevented them from submitting their wrap-up disposition after refreshing the page.




## August 21, 2026

Announcement

**Google Cloud CCaaS 6.4**

We've released version 6.4 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Automatic SIP parameter mapping in contact lists**

Contact lists now support automatic SIP header mapping for outbound call destinations.

Administrators: In the **Add Destination** dialog at **Settings > Call > Contact Lists > Contact list management > `CREATE OR EDIT CONTACT LIST`> Add Destination**, toggle **Pass Data Parameters** to the on position to see the new **Automatically Include and Pass all Inbound SIP Headers** checkbox.

For more information, see [Add a SIP URI address destination to a contact list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list#add-sip-uri-address-destination).

Feature

**Email OAuth profiles and Microsoft 365 client credentials**

You can now create email OAuth profiles for Microsoft 365 using the client credentials grant type. This lets shared mailboxes authenticate through an app registration instead of relying on an individual user sign-in. OAuth IMAP setup is more resilient for support inboxes and other application-managed mailboxes.

For more information, see [Email OAuth profiles and Microsoft 365 client credentials](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-oauth-profiles-ms).

Feature

**Improved connection times for predictive dialing**

We reduced the connection time for predictive dialing to under two seconds to comply with CRTC and FTC regulations.

Fixed

This release addresses the following issues:

  * Fixed an issue where a long delay occurred when an agent clicked **Chat Shortcuts** in the chat adapter.

  * Fixed an agent desktop issue where the **Session Data Feed** pane displayed data from the previous chat and the chat transcript stopped updating.

  * Fixed an issue where conversation history loaded slowly for agents using the CCaaS widget embedded in Salesforce.

  * Fixed an issue where outbound calls with zero duration time were missing from **Individual Call History** reports that were scoped to agents and teams.

  * Fixed an issue where customers couldn't leave a voicemail during a warm transfer.

  * Fixed an issue where the **Queued Calls** dashboard displayed the incorrect originating queue and transferring agent for a cold-transferred call.

  * Fixed an issue where the agent desktop experienced significant loading delays.

  * Fixed an issue where calls transferred from a virtual agent directly to a human agent bypassed the **Keep Waiting** overcapacity setting, causing callers to be incorrectly routed to a fallback queue or to voicemail.

  * Fixed a raw data export issue where file names for the `MENU_PATH_ITEMS` dataset incorrectly contained `path_items`.

  * Fixed an issue where a parent queue was incorrectly marked as after-hours even though one or more of its child queues were in operation.

  * Fixed an issue with chats that were escalated from a virtual agent to a human agent and then reached a terminal status (canceled, finished, or failed). These chats mistakenly appeared in the **Queued Chats** dashboard.

  * Fixed an issue where the agent desktop froze and the **Call Adapter** pane displayed **Call on hold** after a call was terminated or dropped.

  * Fixed an issue where agents couldn't change their chat status while a call was in the wrap-up stage.

  * Fixed an issue where the call adapter displayed calls waiting when there were actually no calls waiting.

  * Fixed an issue where outbound calls that failed immediately caused the call adapter to be stuck in the In-call state with the timer running.




## August 19, 2026

Announcement

**Google Cloud CCaaS 6.3**

We've released version 6.3 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Agent desktop supports parameters in custom panel URLs**

In the agent desktop, you can now configure fixed and dynamic parameters to include in the URLs of custom panels. This lets you pass relevant session, agent, and customer context into custom panels.

For more information, see [Parameters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets#parameters).

Feature

**Callback offer restrictions**

You now have greater control over when callbacks are offered. You can configure the following:

  * Prevent callback offers from being made outside of callback hours.

  * Prevent callback offers that will likely occur outside of callback hours. If conditions improve (that is, EWT decreases), the system adjusts and can offer callbacks.




Administrators: We've added the following checkboxes to the CCAI Platform portal:

  * **Restrict callback offer outside of callback window**

  * **Restrict callback offer that will exceed hours of operation. If queue condition improve offer callbacks**




These checkboxes are available in the following locations:

  * The **Settings > Call > Callback Settings** pane (to configure globally).

  * The **Settings > Queue > IVR (Interactive Voice Response) > Edit / View > `QUEUE_NAME` > Callback Settings > Configure > Callback Management** pane (to configure a queue).




For more information, see [Manage callbacks](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#callback-fulfillment-hours).

Fixed

This release addresses the following issues:

  * Fixed an issue where chat transcripts incorrectly displayed **undefined joined** instead of the agent's name during a chat transfer when real-time redaction was enabled.

  * Fixed an issue where agents were incorrectly placed into **Unresponsive** status after answering a call if the customer declined the system's callback attempt.

  * Fixed an issue where overcapacity deflection didn't trigger when agent-initiated outbound or direct-inbound calls were transferred to a queue, causing users to wait indefinitely.

  * Fixed an issue where the **Answer** button didn't appear for incoming calls in the agent desktop, preventing agents from accepting calls.

  * Fixed an issue where live translation didn't activate (or translated in the wrong direction) after a chat was transferred between queues.

  * Fixed an issue where predictive campaign calls became stuck in a queued state, causing agents to appear available despite being unable to receive new calls.

  * Fixed an issue where web chats became stuck in a queued state and were never assigned to an agent.

  * Fixed an issue where previously closed chat sessions briefly reappeared and gained focus when launching agent desktop.

  * Fixed an issue where agents couldn't submit disposition codes and notes during wrap-up.

  * Fixed an issue where agents couldn't change their status after a call ended abnormally, causing them to remain stuck in the wrap-up state.

  * Fixed an issue where the **Call History** list incorrectly displayed the same customer phone number for all Acqueon campaign calls.

  * Fixed an issue where an agent's status incorrectly remained **Available** during outbound calls and wrap-up periods, allowing the routing engine to offer new inbound calls to occupied agents.

  * Fixed an issue where agents were forced to re-authenticate when opening the chat adapter or email adapter despite having an active session.

  * Fixed an issue where the text screen in the email adapter suddenly re-rendered while typing, causing characters to disappear or be displaced.

  * Fixed an issue where the headings in Generative AI session summaries in chat wrap-up notes lost their bold formatting when saved.

  * Fixed an issue where the global after-hours deflection message played despite a queue-level custom redirect to a phone number being configured.

  * Fixed an issue where calls abandoned by a customer while waiting in a transfer queue were incorrectly reported as queue failures.

  * Fixed an issue where transient CRM errors caused significant delays in retrieving ticket IDs during active calls.

  * Fixed an issue where the CCAI Platform portal incorrectly displayed a chat status as **Unknown** (instead of **Check In Timeout**) when a consumer didn't check in.

  * Fixed an issue where the call adapter incorrectly displayed **Portuguese BR** instead of **Portuguese (Portugal)** during call handoffs.

  * Fixed an issue where agents making outbound calls remained in an **Available** status, which incorrectly allowed new inbound calls to be routed to them while they were already engaged.

  * Fixed an issue where Agent Assist live transcription and generative summary stopped working mid-call following a transfer or a hold-and-resume cycle.

  * Fixed an issue where the transfer menu delayed loading queues.

  * Fixed an issue where the agent adapter incorrectly displayed an agent's status as **Unavailable** when a custom status, such as **Break** or **Special Task** , was selected.

  * Fixed an issue where chats escalated from a virtual agent to a human agent queue bypassed menu-level after-hours and over-capacity deflection messages.

  * Fixed an issue where the call adapter defaulted to English in the **Outbound call** screen regardless of the agent's system language.

  * Fixed an issue where **Call** and **Chat** each appeared twice in the **Dashboard** menu when using high browser zoom levels or small window resolutions.

  * Fixed an issue where legacy dashboards were restricted to English-only labels.

  * Fixed an issue where users in SAML-only or SSO-enabled environments received invitation emails directing them to a non-existent **Forgot Password** flow.

  * Fixed an issue where the user activity logs incorrectly recorded an end-user ID instead of the agent's ID when a chat disconnected.

  * Fixed an issue where customer calls were abandoned during payment transactions when DTMF inputs were provided.

  * Fixed an issue where agents could see and select outbound caller IDs that weren't assigned to their teams or queues.

  * Fixed an issue where post-session virtual agent transfers stalled if a customer left the chat while still in a queue for a human agent.

  * Fixed an issue where agents and end-users could hear each other's voices despite the agent putting the call on hold.

  * Fixed an issue where the agent adapter incorrectly reverted to displaying English when initiating an outbound call in a non-default language.

  * Fixed an issue where the **Hide Agent Assist** button wasn't appearing in the user interface during the call disposition phase.

  * Fixed an issue where cascade agent availability conditions weren't enforced, causing regional agents to be incorrectly routed into international queues and leaving local queues understaffed.

  * Fixed an issue where agents appeared available but weren't receiving calls.

  * Fixed an issue where administrators received multiple email notifications instead of a single notification after deactivating a call channel.

  * Fixed an issue where Telnyx error handling was incorrectly configured, causing system alerts to fail during call disconnect or hold actions.

  * Fixed an issue where inbound IVR calls were stuck in a queued state if a caller disconnected during initial call processing.

  * Fixed an issue where callbacks became permanently stuck in a queued state if an agent missed a projected call.

  * Fixed an issue where calls using Telnyx or Nexmo numbers received an "An Application error has occurred" message during overcapacity deflection or automatic redirection.

  * Fixed an issue where call recordings weren't delivered or processed correctly.

  * Fixed an issue under **Settings > Operation Management > Localization > Manage Location Setting** where configured locations with **Portuguese (Portugal)** or **Spanish (Spain)** selected incorrectly displayed as **Unknown** in the **Language** column, and locations with **Spanish (Mexico)** selected incorrectly displayed as **Spanish (Spain)**.

  * Fixed an issue in iOS and Android SDKs where the end user's initial message and custom data weren't correctly passed to the routing API during the chat menu fetch.

  * Fixed an issue where inbound calls cancelled by the caller within the first second incorrectly remained active in the system for several hours.

  * Fixed an issue where custom SIP headers were dropped. This occurred when a directly dialed agent was over capacity, the call was redirected to the agent's queue, and that queue was configured to redirect to a SIP URI.

  * Fixed an agent desktop issue where the chat screen went blank when an agent accepted or dismissed a chat.

  * Fixed an issue where the **Deflections - Calls** dashboard incorrectly reported the queues that calls were redirected to when using percent allocation.

  * Fixed an issue where auto-answered interactions became stuck in a **Queued** status despite being accepted by an agent.

  * Fixed an issue where the chat adapter in a CRM integration didn't post outbound messages when using rich text formatting.

  * Fixed an issue where the `agent_activity_logs` endpoint experienced timeouts and degraded performance when processing large data requests.

  * Fixed an agent desktop issue where outbound calls appeared to start successfully but didn't connect to the end-user.

  * Fixed an issue where **New photo received** notifications appeared whenever an agent switched between chat tabs.

  * Fixed an issue where short outbound calls incorrectly displayed a **This call was abandoned by the customer** message.

  * Fixed an issue where agents experienced significant delays when switching between multiple concurrent web chats.

  * Fixed an issue where attaching PDF or text files in the chat adapter failed or timed out.

  * Fixed an issue where calls transferred from a virtual agent to an agent extension were incorrectly deflected.

  * Fixed an issue where reordering queues in the CCAI Platform portal experienced extreme latency and didn't update visually without a manual page refresh.

  * Fixed an issue where chat history for added agents became unavailable after a page refresh.

  * Fixed an issue where calls to the `user_activity_logs` endpoint experienced significant delays.

  * Fixed an issue where repeated voicemail re-reads caused duplicate participant entries and inflated session data.

  * Fixed an issue where callback sessions remained in a **Connected** status indefinitely after completion.

  * Fixed an issue where agents using IdP-initiated SAML SSO were automatically routed to the default home page instead of the agent desktop.

  * Fixed an issue where DTMF options in the softphone didn't register with external IVR systems during outbound calls.

  * Fixed an issue where agents were unable to receive or fetch incoming calls.

  * Fixed an issue where supervisors using Telnyx who ended a monitoring session were unable to monitor subsequent calls.

  * Fixed an issue where empty chat bubbles appeared in the chat adapter when an end-user used suggestion chips to respond to a virtual agent.

  * Fixed an issue where duplicated contact handle-duration events caused inaccurate reporting for call and chat interactions.

  * Fixed an issue where agents didn't receive the correct error messages when their microphone was disabled or inaccessible during a call.

  * Fixed an issue where incoming calls were incorrectly multicasted and didn't auto-answer when an agent was already in an active chat session.

  * Fixed an issue where calls deflected to external SIP or phone destinations were missing the `ends_at` timestamp in call data.

  * Fixed an issue where the chat timeout event wasn't correctly emitted to the headless web SDK, causing sessions to remain active for up to 120 minutes, regardless of the configured settings.

  * Fixed an issue where agents using Salesforce-Lightning or Zendesk embeds couldn't maintain a stable presence connection.

  * Fixed an issue where headless web SDK client methods didn't work after a mid-session authentication update.

  * Fixed an issue where agents were unexpectedly logged out of all active sessions.

  * Fixed an issue where calls producing multiple recording segments resulted in duplicate entries in Customer Experience Insights.

  * Fixed an issue where the `parent_id` field was missing from callback call responses in the manager API.

  * Fixed an issue where virtual agent transcripts were lost during escalations to human agents.

  * Fixed an issue in the agent desktop where the sentiment score appeared in the **Call details** panel despite sentiment analysis being turned off in the conversation profile.

  * Fixed an issue where the **Escalated To Language** column in the **Escalations** table of the **Virtual Agent - Calls** dashboard incorrectly displayed `Unknown` for French (Canada) calls.

  * Fixed an issue where calls didn't advance to the next cascade group after the timer threshold was reached.




## August 10, 2026

Announcement

**Google Cloud CCaaS 6.0**

We've released version 6.0 of Google Cloud CCaaS.

Version 6.0 updates internal Google Cloud CCaaS infrastructure. It contains no customer-facing changes from version 5.2.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

## August 06, 2026

Announcement

**Advanced reporting dashboards 5.1**

We've released version 5.1 of the advanced reporting dashboards.

Feature

**Sub teams are included when top-level teams are selected in the Team filter**

When you select a team in a **Team** filter on a dashboard, the data for that team's sub-teams is now included.

Feature

**The Agent Metrics (Historical) Explore contains the Avg Chat Concurrency metric**

The **Agent Metrics (Historical)** Explore now contains the **Ave Chat Concurrency** metric to capture concurrency trends for agents, teams, and queues.

Feature

**Metrics for warm transfers and agent consultations**

The **Transfers - Calls** and **Transfers - Chats** dashboards now have the following metrics in the **Call Transfers** and **Chat Transfers** tables:

  * **Agent Connection Time (H:M:S)**. Reports the time spent consulting with another agent and then warm transferring to that agent.

  * **Agent Consult Time (H:M:S)**. Reports the time spent consulting with another agent before returning to the call.




Fixed

This release addresses the following issues:

  * Fixed an issue where the **This Week** and **This Month** per-hour figures on the **Performance Overview** and **Agent Performance** dashboards were inaccurate.

  * Fixed an issue where the **Queue Abandons** and **Abandon %** fields on the **Queue Group Performance - All** and **Queue Group Performance - Chats** dashboards always displayed `0` for chats.

  * Fixed an issue where the virtual agent call metrics on the **Virtual Agent - Calls** , **All Interactions - Calls** , and **Performance Overview** dashboards were incorrect.

  * Fixed an issue where agents appeared under **Assigned Agent** for calls that they weren't connected to.

  * Fixed an issue where exporting data from dashboards using date ranges greater than seven days failed.

  * Fixed an issue in the **Real-time Queue Monitoring** and **Queued Calls** dashboards where transferred calls were incorrectly displayed as **Queued** when they were active with an agent.

  * Fixed an issue where queue groups that were turned off remained visible in advanced reporting dashboards.

  * Fixed an issue where the **Queue Time** filter on the **All Interactions** dashboard wasn't displaying data.

  * Fixed an issue where the **SLA Target** field in the **Queue Group Performance - All** dashboard was empty.

  * Fixed an issue where the **No** checkbox of the **Child Queues** filter disappeared when cleared. No child queues is the default for this filter, so we removed the **No** checkbox, leaving only the **Yes** checkbox.

  * Fixed an issue where the **Available Agents** field overstated real capacity.

  * Fixed an issue on the **Queue Groups - Calls** and **Queue Groups - Chats** dashboards where the **Ave Current Queue Time** metric displayed incorrect data.

  * For time-related exports, there's now a column that displays time in HH:MM:SS format (in addition to seconds). You can't apply conditional formatting to this format in an Explore.

  * Fixed an issue where **Max Queue Wait Time** , **Max Speed To Answer** , and **Max Queue Abandon Time** displayed incorrect data in Explores.

  * Fixed an issue where changes to an agent's availability preferences in the agent adapter weren't reflected in the **Agent Activity** dashboard.

  * Updated the labels in the **Agent Metrics (Historical)** Explore to be channel-agnostic for metrics that include both calls and chats.




## July 30, 2026

Announcement

**Google Cloud CCaaS 5.2**

We've released version 5.2 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Answering machine detection for progressive campaigns**

Answering machine detection (AMD) is now supported for progressive outbound campaigns. When enabled, Contact Center AI Platform analyzes call audio in the background to determine whether a call reaches a live person, or whether it reaches an answering machine or voicemail. If an answering machine or voicemail is detected, the call ends and the dialer proceeds to the next contact.

Administrators: In the **Settings > Campaigns > Dialer Modes** pane, there's a new **Enable Answering Machine Detection** toggle.

User experience change: When CCAI Platform detects voicemail or an answering machine, a green banner appears in the call adapter to indicate this.

For more information, see [Answering machine detection for progressive campaigns](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-progressive-amd).

Feature

**New endpoints for getting email sessions and messages**

Two new read-only endpoints are now available, allowing external systems to retrieve the parsed contents of an email interaction. This includes the sender, recipients, subject, body, and attachment metadata. Here are the endpoints:

  * `/apps/api/v1/email/sessions/EMAIL_SUPPORT_ID`: Returns email session summary information and a list of message IDs with metadata.

  * `/apps/api/v1/email/messages/EMAIL_THREAD_ID`: Returns the full content of a single message.




For more information, see [Get email sessions and messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-email-sessions-and-messages).

Feature

**Email forwarding with attachments**

Agents can now forward emails to external recipients directly from the email adapter. When forwarding, all attachments from the original email are automatically included. Agents can remove attachments before sending, if needed. The original email remains in its assigned queue with its status unchanged.

User experience change: A new **Forward** button is available in the email adapter.

For more information, see [Forward an email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#forward-an-email).

Feature

**Smart disposition**

Smart disposition is a new AI-powered capability that automatically suggests a disposition code at the end of a session. This reduces manual work for agents and improves data consistency.

Administrators: There's a new **Smart Disposition** toggle in the following locations:

  * The **Settings > Operation Management > Wrap-up > Automatic wrap-up for inbound calls > Disposition Codes & Notes for calls > Disposition Codes** section.

  * The **Settings > Operation Management > Wrap-up > Automatic wrap-up for outbound calls > Disposition Codes & Notes for calls > Disposition Codes** section.

  * The **Settings > Operation Management > Wrap-up > Automatic wrap-up for chats > Disposition Codes & Notes for chats > Disposition Codes** section.




User experience change: When smart disposition is turned on, a suggested disposition displays in the **Disposition** field of the **Wrap-up** screen in the agent adapter.

For more information, see [Smart disposition](https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-disposition).

Fixed

This release addresses the following issues:

  * Fixed an issue where voice calls became stuck in a virtual agent state after a session ended abnormally or an escalation handoff didn't complete.

  * Fixed an issue where using invalid sorting parameters on agent activity logs caused a server error.

  * Fixed an issue where canceling a warm transfer to a queue at overcapacity caused the caller to become stranded in an automated menu loop.

  * Fixed an issue where the agent activity logs API allowed unbounded time ranges, which led to system performance degradation and gateway timeouts.

  * Fixed an issue where the team and menu endpoints experienced performance delays.

  * Fixed an issue where calls transferred to a queue with overcapacity deflection (OCD) enabled didn't redirect, causing callers to hear indefinite ringing.

  * Fixed an issue where the call duration in the call adapter and in the in-call status timer of the agent desktop didn't match for outbound calls.

  * Fixed an issue where the **Agent Activity** dashboard displayed time zones inconsistently.

  * Fixed an issue where the inactivity timer didn't force a session to end if the agent closed the browser or browser tab before the inactivity timer expired.

  * Fixed an issue where the **All Call History** and **Individual Call History** reports displayed incorrect cascade group numbers for transferred calls and chats.

  * Fixed an issue where the sentiment score appeared in the **Call Details** panel of the agent desktop despite sentiment analysis being turned off in the conversation profile.

  * Fixed an issue with IVR calls routed through Nexmo, where the virtual agent missed the first several seconds of caller audio, forcing callers to repeat themselves.

  * Fixed an issue where chats became stuck in the queue after a deltacast routing projection expired or an agent didn't connect.

  * Fixed an issue where reordering queues in the CCAI Platform portal caused significant latency and required a manual page refresh to display the changes.

  * Fixed an issue with Salesforce integrations where adding a third party to a call incorrectly displayed their contact name in the customer field in the agent desktop **Participants** panel.

  * Fixed an issue where direct inbound SMS chats that were sent to an unavailable agent expired and failed instead of being rerouted.

  * Fixed an issue where anonymous inbound calls incorrectly displayed an agent's contact information instead of indicating an unknown caller.

  * Fixed an issue where database deadlocks caused transactions to run against the wrong database, causing failed lookups and chat sessions getting stuck.

  * Fixed an issue where manual status changes to **Available** after an automatic wrap-up were incorrectly attributed to the system instead of the agent in activity reports.

  * Fixed an issue where retrieving large datasets using the manager API caused connection timeouts and incomplete data synchronization for downstream systems.

  * Fixed an issue where the **Agent Assist Hub** incorrectly displayed `The Agent Assist Hub feature is not enabled` during voice sessions despite the **Agent Assist Hub** being enabled.

  * Fixed a web SDK issue where navigating between pages on the host website during an active chat resulted in a duplicate session being created.

  * Fixed an issue where the **AgentSystemData** historical report incorrectly showed zero login time for agents who were actively handling calls.

  * Fixed an issue where Dialogflow agents incorrectly escalated or disconnected calls when responding with only pre-recorded audio.

  * Fixed an issue where transfer completion events appeared twice in the agent desktop session data feed when a user was transferred to a task virtual agent.

  * Fixed an issue where virtual agent interactions failed and escalated prematurely.

  * Fixed an issue where a single wrap-up event was incorrectly dispatched twice to Dialogflow on bidirectional-enabled voice calls.

  * Fixed an issue where session summarization sections weren't displayed in the order that they were configured.

  * Fixed an issue where sensitive information in the CC and BCC fields of email requests was visible in system logs.

  * Fixed an issue where the email adapter displayed a blank gray screen when an agent attempted to transfer emails between queues.

  * Fixed an issue in Kustomer integrations where abandoned or failed calls weren't finalized, leaving records in the `Call In Progress` state.

  * Fixed an issue in ServiceNow integrations where starting a chat from a queue caused duplicate cases for a single chat ID.

  * Fixed an issue where mobile chat sessions ended unexpectedly after successfully escalating to a human agent.

  * Fixed an issue where chat transcript PDF headers remained in English for non-English queues.

  * Fixed an issue where placeholder text (`Content cards displayed here`) didn't appear in the agent adapter or live chat view when content cards weren't supported.

  * Fixed an issue where agents received duplicate SMS messages from end-users.

  * Fixed an issue where the inactivity timeout didn't trigger for chats waiting in a transfer queue.

  * Fixed an issue where chats waiting in a transfer queue remained open indefinitely and created duplicate metadata files.

  * Fixed an issue where chat transcripts were missing from data exports when a CRM ticket wasn't created.

  * Fixed an issue where chats escalated from a virtual agent remained in queued status after being assigned to an agent.

  * Fixed an issue where calls escalated from a virtual agent to a holiday-closed queue bypassed the holiday message and played the after-hours deflection message.

  * Fixed an issue where call recording URLs weren't saved or synced to the CRM for calls with multiple audio segments, such as those involving an IVR followed by an agent conference.

  * Fixed an issue where voice calls remained in an assigned state without progressing or requeueing if a system error occurred during the assignment process.

  * Fixed an issue where callers were disconnected from voicemail greetings after an agent completed their wrap-up following a call transfer.

  * Fixed an issue where manual wrap-up session data was incorrectly recorded across multiple sessions, leading to inflated duration reports.

  * Fixed an issue where duplicate call recording files with an `.N` suffix were created in external storage.

  * Fixed an issue where calls prematurely disconnected or experienced audio loss during the hangup process.

  * Fixed an issue where Telnyx VoIP calls silently dropped without notification if the connection was interrupted.

  * Improved internal instrumentation to diagnose poor call quality scores and improve call reliability.

  * Fixed an issue where agents configured for Deltacast and auto-answer received unexpected multicast call offers.

  * Fixed an issue where the agent desktop didn't save call-related settings such as mute status.

  * Fixed an issue where queue-level automatic wrap-up settings were unexpectedly disabled.

  * Fixed an issue where the switch to chat button wasn't accessible from the keyboard.

  * Fixed an issue where an agent ended the wrap-up session of another agent.

  * Fixed an issue where agents experienced delays of up to 30 seconds when transitioning from "Wrap" to "Available" status.

  * Fixed an issue where an `An error has occurred` message incorrectly appeared when a user created a direct access point for instances without a configured CRM.

  * Fixed an issue where message timestamps weren't visible to supervisors and administrators when monitoring active chats in the CCAI Platform portal.

  * Fixed an issue where historical data syncs to Calabrio failed.

  * Fixed an issue where the bulk user upload process allowed unauthorized role assignments.

  * Fixed an issue where deleting a notification rule removed all associated historical notifications without warning.

  * Fixed an issue where call events in timeline reports appeared out of chronological order.

  * Fixed an issue where technical connection timeouts during call offers weren't correctly tracked as skipped interactions.

  * Fixed an issue where chats remained in the queue following a virtual agent escalation.

  * Fixed an issue where importing a contact list CSV for a native power dial campaign failed if the file contained malformed rows or encoding issues.




## July 24, 2026

Announcement

**Google Cloud CCaaS 5.0**

We've released version 5.0 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Disposition timing**

You can now configure CCAI Platform so agents can attribute wrap-up time, disposition code, and notes to a previous interaction. You can also let agents modify the disposition code and notes of previously completed sessions.

Administrators: In the **Settings > Operation Management > Wrap-up** pane, a new **Manual Wrap-up** section is available.

User experience change: If configured, a new **Previous Sessions** list appears in the agent adapter.

For more information, see [Configure disposition timing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-disposition-timing).

Feature

**API direct access point for chat**

The API direct access point (DAP) for chat lets you automatically route incoming chat sessions to a queue based on a response from an external API endpoint that you configure. This eliminates the need for end-users to select from a queue menu.

By default, this capability is inactive. Contact Google Cloud Support to turn it on for your instance.

For more information, see [API direct access point for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/api-dap-for-chat).

Fixed

This release addresses the following issues:

  * Fixed an issue where the **Session Data** report incorrectly calculated the after call work (ACW) duration specifically for manual wrap-up scenarios.

**Note:** This is different from the known issue where auto wrap-up time is capped at 10 seconds. This issue is targeted for resolution in a future release.
  * Fixed an issue where emails were stuck in a **Transferring** state when moved between queues.

  * Fixed an issue where end-users didn't receive messages from agents during web chats.

  * Fixed an issue where calls or chats remained in a queue without being offered to available agents.

  * Fixed an issue where voice calls were prematurely moved from an agent's queue during a multi-group cascade.

  * Fixed an issue where the disposition panel didn't appear after a call ended, leaving agents unable to change their status without signing out and signing in.

  * Fixed an issue where end-users were incorrectly assigned to teams and skills they weren't originally part of during bulk CSV imports.

  * Fixed an issue where interaction transcripts for calls in non-English languages were incorrect.

  * Fixed an issue in Salesforce integrations where incoming chat audio and desktop notifications didn't play for agents using the embedded CCAI Platform widget.

  * Fixed an issue where the inactive chat dismissal timer didn't reset after a chat was transferred from a virtual agent to a human agent.

  * Fixed an issue where voicemails disappeared from the queue immediately after being opened.

  * Fixed an issue where the reporting dashboard incorrectly displayed call and agent status during a cold transfer to another queue.

  * Improved rendering performance in the agent desktop mini chat adapter.

  * Fixed an issue where the storage path for screen recordings didn't align with the folder structure displayed in the user interface.

  * Fixed an issue where missing public files were incorrectly cached by the CDN for up to seven days.

  * Fixed an issue where agents were automatically redirected to the **Closed** inbox view after changing an interaction status to **Closed**.

  * Fixed an issue where the **You cannot log out when in a chat** notification was truncated in the chat adapter.

  * Fixed an issue with Salesforce integrations where rapid, concurrent data requests caused information to be lost.

  * Fixed an issue where duplicate call recording links were posted to Zendesk tickets for multi-segment calls.

  * Fixed an issue with Salesforce integrations where the UI retained settings from a previous Salesforce organization after switching to a new organization.

  * Fixed an issue where duplicate customer satisfaction surveys were submitted and recorded for a single live chat session.

  * Fixed an issue where the message field in the chat adapter was inactive when an agent accepted a new chat.

  * Fixed an issue where task virtual agents were incorrectly identified as **Nobody** when joining a conversation after a transfer from a human agent.

  * Fixed an issue that occurred when a chat entered a queue and the greeting message was sent before an agent was assigned. In these cases, the associated push notification crashed and logged an error, producing excessive noise in logs.

  * Fixed an issue where the agent's final message in a chat session appeared after **This chat is ended** in the chat adapter and the CRM transcript.

  * Fixed an issue where agents using instances without a CRM configuration received a **No Account Detected** warning when making outbound calls.

  * Fixed an issue where notification chimes played after an agent had connected to an active call.

  * Fixed an issue where the country code list didn't automatically update the country flag when a phone number was entered without the `+` prefix.

  * Fixed an issue where calls to an agent's personal queue didn't break through if the agent was also assigned to an inbound queue with breakthrough disabled.

  * Fixed an issue where outbound calls that were transferred to a queue didn't adhere to the queue's deltacast configuration.

  * Fixed an issue where the agent desktop became unstable or didn't load.

  * Fixed an issue where wrap-up time was incorrectly reported when agents exceeded the configured wrap-up time.

  * Fixed an issue where the IVR queues dashboard didn't load for instances with a large volume of queues.

  * Fixed an issue where calls to the `manager/api/v1/agent_activity_logs` endpoint timed out when `sort_direction` was turned off.




## July 01, 2026

Announcement

**Google Cloud CCaaS 4.45**

We've released version 4.45 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Emergency queue shutdown**

You can temporarily shut down a specific queue during unexpected events such as system issues, an unexpected staffing shortage, a building emergency, or unplanned maintenance. This lets you provide fast, controlled call deflection for the affected queue without impacting the rest of your call center. You can shut down a queue using the CCAI Platform portal or programmatically, using the `/apps/api/v1/menus/shutdown` API.

By default, this capability is inactive. Contact Google Cloud Support to turn it on for your instance.

Administrators: We've made the following updates to the CCAI Platform portal:

  * In the **Settings > Queue > IVR (Interactive Voice Response) > Edit / View > MENU_NAME > Settings** pane, there's a new **Emergency Shutdown** section.

  * On the **Settings > Developer Settings > Audible Messages** page, there's a new **Enable Remote Shutdown via API** toggle.




For more information, see [Emergency queue shutdown](https://docs.cloud.google.com/contact-center/ccai-platform/docs/emergency-queue-shutdown).

Feature

**Do Not Call capability in HubSpot**

You can configure your HubSpot integration to display **This number is on the Do Not Call list** in the call adapter when an agent initiates a call to a contact configured for Do Not Call (DNC). The agent can proceed with the DNC call if needed. If the agent proceeds with the call, the following comment is logged in the CRM: "The contact is in TPS, the agent chose to proceed with the call."

This capability is for non-campaign outbound calls. It doesn't affect outbound campaign calls.

Administrators: In the **Settings > Developer Settings > Agent Platform > HubSpot > Account Lookup** section, there's a new **Do-Not-Call CRM Field** section.

User experience update: The call adapter displays **This number is on the Do Not Call list** when an agent initiates a call to a contact configured for DNC.

For more information, see [Do Not Call for HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-do-not-call).

Feature

**Return to queue after disconnection**

You can configure CCAI Platform to offer a disconnected caller the option to return to their queue. If they accept, they're returned to the top of the queue. Virtual agents in the queue are skipped. This capability is for IVR calls only.

Administrators: We've made the following updates to the CCAI Platform portal:

  * In the **Settings > Call > Call Details** pane, there's a new **Return to Queue After Disconnection** section.

  * In the **Settings > Queue > IVR (Interactive Voice Response) > Edit / View > MENU_NAME > Settings** pane, there's a new **Return to Queue after disconnection** section.

  * In the **Settings > Languages & Messages > Audible Messages** pane, there's a new **Return to Queue After Disconnection Messages** section.




For more information, see [Return to queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/return-to-queue).

Fixed

This release addresses the following issues:

  * Fixed an issue where campaigns that didn't complete prevented subsequent campaigns from starting.

  * Fixed an issue where callers weren't correctly connected to voicemail during a warm transfer to an agent's direct number.

  * Fixed an issue where incoming calls were assigned to agents but didn't appear in the agent adapter, resulting in "ghost assignments" and abandoned calls.

  * Fixed an issue where cold-transferring a call from a queue while the transferring agent was in a wrap-up state caused the connection to become unresponsive and silent.

  * Fixed an issue where calls that disconnected before entering a queue were incorrectly displayed in the **Queued Calls** dashboard.

  * Fixed an issue in the agent desktop where the call disposition panel failed to load for queues with forced disposition enabled, leaving agents stuck and unable to proceed without logging out.

  * Fixed an issue where streaming conversations failed due to connection errors.

  * Fixed an issue where outbound calls initiated from a HubSpot company profile created duplicate anonymous contacts instead of matching existing records by phone number.

  * ~~Fixed an issue where the**Session Data** report incorrectly calculated the after call work (ACW) duration specifically for manual wrap-up scenarios.~~

**Note:** This is different from the known issue where auto wrap-up time is capped at 10 seconds. This issue is targeted for resolution in a future release.

This fix was released in version 5.0.

  * Fixed an issue where the **Start Call** button didn't display in the call adapter.

  * Fixed an issue where voicemails from cold transfers were lost or routed to the wrong queue.

  * Fixed an issue in the agent desktop where active calls appeared to be on hold while the agent was in a "wrap-up exceeded" state.




## June 30, 2026

Announcement

**In the Agent Desktop, the Knowledge Assist panel is being replaced with a new Agent Assist Hub panel**

**Who's affected?**

Customers who use the Agent Desktop and the Knowledge Assist panel in a desktop layout are affected. If you don't use Agent Desktop and the Knowledge Assist panel, you can ignore this announcement.

**What's changing?**

We're replacing the Knowledge Assist panel in Agent Desktop with a new Agent Assist Hub panel. The Agent Assist Hub panel contains a Knowledge Assist module that is a 1:1 functional replacement of the Knowledge Assist panel.

**How does this affect my contact center?**

For any agents that are signed into your contact center at the moment we update it, the new Knowledge Assist module will stop working. To fix this problem, the agent needs to sign out of the contact center and sign in again. The Knowledge Assist module will begin working. Agents who sign into your contact center after we update it won't be affected by this issue.

**What do I need to do?**

When we roll out this change, your Google Cloud CCaaS instance will be updated automatically - you don't need to change any configurations. However, you should tell your agents to sign out of your contact center and sign in again if the Knowledge Assist module within the Agent Assist Hub panel isn't working for them. Your agents do not need to take action If your instance is configured as a Critical deployment and is updated outside of the contact center hours of operation.

**When is this happening?**

We expect to make this change in early Q3 of 2026, around mid to late July. We'll publish prerelease notes and release notes to keep you informed of this change.

## June 25, 2026

Announcement

**Web SDK version 2 will be shut down on June 26, 2026**

On June 26, 2025, we announced the launch of [Web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025). Starting on **June 26, 2026** , the web SDK v2 will no longer be supported. Be sure to [update your website](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 to avoid disrupting your integration with the web SDK. We are no longer adding new features to the web SDK v2.

## June 22, 2026

Announcement

**Google Cloud CCaaS 4.43**

We've released version 4.43 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Calls to direct numbers display language selection in the call adapter**

When an agent receives a direct call, the call adapter now displays the language that the caller chose during language selection.

For more information, see [Direct phone numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers).

Feature

**HubSpot: Control the display of CRM account fields and record fields in the agent adapter**

You can now control how CRM account fields (contact and company) and record fields (ticket and deal) appear in the agent adapter for HubSpot integrations. This gives agents immediate access to important context such as VIP status, account ownership, and ticket priority during live interactions.

Administrators: In the **Settings > Developer Settings > CRM > Agent Platform > HubSpot > Account Lookup** section, there are two new **CRM Account Display Fields** sections and a new **CRM Record Display Fields** section.

For more information, see [HubSpot lookups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups).

Feature

**The chat API supports CSAT surveys**

You can now conduct customer satisfaction (CSAT) surveys using the chat API. You can configure CSAT surveys at the global level and at the queue level.

Administrators: On the **Settings > Chat** page, there's a new **Chat API** section.

For more information, see [CSAT in the chat API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/csat-chat-api#adding_translations_for_multiple_languages).

Fixed

This release addresses the following issues:

  * Fixed an issue where uploading a PDF document to a chat made the conversation history unavailable during a session transfer or page refresh.

  * Fixed an issue where direct SMS chats didn't send termination notifications at the end of the chat.

  * Fixed an issue where the after-hours voicemail greeting didn't play during agent-to-agent call deflections.

  * Fixed an issue where SIP and IVR calls intermittently failed if the caller disconnected before a virtual agent was assigned.

  * Fixed an issue where calls deflected to voicemail during after-hours were incorrectly reported as errors in the **All Call History** report.

  * Fixed an issue where direct inbound calls were incorrectly deflected to voicemail during an agent's available hours when agent deflections were enabled.

  * Fixed an issue where inbound voice calls failed with an application error during the initial lookup phase.

  * Fixed a Kustomer issue where Agent Assist transcripts were delivered to the CRM as file attachments instead of timeline notes.

  * Fixed an issue where the **In Progress** banner and the **Cancel** button didn't appear immediately after a virtual task assistant request was initiated.

  * Fixed an issue where campaigns stayed in a paused state instead of transitioning to a completed state after finishing.

  * Fixed a Deltacast issue where chats weren't routed correctly to available agents when the company-wide concurrency setting was disabled but individual agent limits were active.

  * Fixed an issue where supervisor monitoring and whisper features caused system errors during call recording.

  * Fixed an issue where agents couldn't dismiss forwarded voicemails if the source queue had been deleted.

  * Fixed an issue where Telnyx calls that ended normally didn't generate a disconnect event, resulting in missing recordings, missing transcripts, and calls appearing to still be active in the CCAI Platform portal.

  * Fixed an issue where consecutive IVR queue deletions caused performance delays and timeout errors.

  * Fixed an issue where queue-level automatic wrap-up settings were disabled without an end-user action.

  * Fixed an issue where the queue settings page displayed inconsistent whisper announcement statuses and didn't play queue names during calls.

  * Fixed an issue where the **Queues** page displayed incorrect overcapacity deflection settings when end-users navigated quickly between different queues.

  * Fixed an issue where virtual agents attempted to fail over to a human agent during outages even when no human agent was configured.

  * Fixed a Salesforce issue where initiating an outbound call from an active case linked to a separate case assigned to a different user, incorrectly overriding ownership of the second case.

  * Fixed a Kustomer issue where duplicate conversation records were created in the CRM during calls.

  * Fixed a Kustomer issue where SMS chat sessions didn't create tickets in the CRM.

  * Fixed an issue where underscores in an email address in a shortcut were converted to double backslashes when an agent sent the email address to an end-user.

  * Fixed an issue where deleting Twilio records caused unnecessary errors.

  * Fixed an issue where disabling the global CSAT setting prevented IVR surveys from being offered to callers, even when the surveys were enabled for specific queues.




## June 15, 2026

Announcement

**Advanced reporting dashboards 4.36**

We've released version 4.36 of the advanced reporting dashboards.

Feature

**New child queues filter option**

Dashboards that have the **Queue Name** filter now also have a **Child Queues** checkbox. Select **Yes** if you want to include all child queues of the specified queue. There's also a new **Child Queues (Yes / No)** filter available in Explores that have the **Queue Name** filter.

Feature

**The Agent & Queue Status (Live) Explore contains new real-time agent and queue metrics**

The **Agent & Queue Status (Live)** Explore contains the following new metrics:

  * **In Call** : the number of agents currently on a call

  * **Available / Waiting** : the number of agents available and waiting for the next contact

  * **Contacts in Queue** : the number of calls currently waiting in the queue




Feature

**Link directly to CSAT scores in your CRM from the CSAT dashboards**

In the **CSAT Interactions** table of the **CSAT - Calls** and **CSAT - Chats** dashboards, next to the **Session ID** numbers, links to the associated CSAT scores in your CRM are now available. You can go directly to the CSAT scores without needing to search for them in your CRM.

For more information, see [CSAT dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-csat).

Feature

**Updates to the Real-time Queue Monitoring - Calls dashboard**

The **Real-time Queue Monitoring - Calls** dashboard now includes the following metrics tiles:

  * **Total Rolled Over Pending Callbacks**

  * **Total Rolled Over Completed Callbacks**

  * **Avg CSAT Calls**




For more information, see [Queue monitoring dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor).

Feature

**Updates to the Queue Performance dashboards**

  * The **Queue Performance - Calls** and **Queue Performance - Chats** dashboards now include the following:

    * A new **Interaction Type** filter

    * A new **Interaction Type** column in the **Queue Detailed Table**

  * The **Queue Performance - Calls** dashboard now includes the following metrics tiles:

    * **Total Rolled Over Completed Callbacks**

    * **Total Rolled Over Pending Callbacks**




Feature

**Repeat contact data in the Queue Performance dashboards**

The **Queue Summary Table** of the **Queue Performance - Calls** and **Queue Performance - Chats** dashboards now includes the following columns:

  * **Total Repeat Contacts**

  * **Repeat Contact %**




For more information, see [Queue Performance dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-performance).

Fixed

This release addresses the following issues:

  * Fixed an issue where **Repeat Contact %** values in the **Queue Summary Table** of the **Queue Performance - Calls** dashboard exceeded 100%.

  * Fixed an issue where the **Date** filter in Explores returned no results when **is on or after** was set for an absolute date.

  * Removed the **Total Logged in Time** metrics tile from the **Agent Availability** dashboard.

  * Fixed an issue where language labels were missing from the advanced reporting dashboards.

  * Fixed an issue that occurred when filtering by chat ID in the **All Interactions - Chats** dashboard. The wrong chat ID appeared in the **Virtual Agent Chats** table.

  * Fixed an issue where disposition codes were missing or blank for outbound calls in the **Call Agent Metrics (Historical)** dashboard.




## June 12, 2026

Announcement

**Google Cloud CCaaS 4.40**

We've released version 4.40 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Fixed

This release addresses the following issues:

  * Fixed an issue with Salesforce where virtual agent responses appeared out of order in transcripts.

  * Fixed an issue where the advanced reporting dashboards didn't load.

  * Fixed an issue where PDF and audio attachments weren't visible to agents after a chat transfer.

  * Fixed an issue where end-users were incorrectly placed on hold following a cold transfer to a queue.

  * Fixed an issue where MP3 audio files for agent call deflections couldn't be uploaded.

  * Fixed an issue where agents were automatically logged out due to inactivity while still engaged in active calls or chats.

  * Fixed an issue where a bulk user upload with blank phone number columns caused existing direct inbound phone numbers to become unassigned from agent profiles.




## June 09, 2026

Announcement

**Mobile SDK for Android version 2.15.3 patch**

We've released version 2.15.3 of the Mobile SDK for Android.

Fixed

This release addresses the following issues:

  * Fixed an issue where `UjetWebFormCallback` in the Android SDK lacked the necessary methods to pass form data.

  * Fixed an issue where chat messages and content cards in the Mobile SDK displayed out of order.

  * Fixed an issue where the Android SDK didn't start a new chat session after the previous session ended.

  * Fixed an issue where customers couldn't customize the Android SDK to display the timeout message to end-users.




## June 08, 2026

Announcement

**Google Cloud CCaaS 4.39**

We've released version 4.39 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Fixed

This release addresses the following issues:

  * Fixed an issue with Salesforce where cases weren't created when a virtual agent connected to a call.

  * Fixed an issue where agents on teams with transfer restrictions couldn't transfer chats to agents not assigned to a team.

  * Fixed an issue where agents who weren't available for chat transfers still appeared in the transfer list, causing transfer attempts to fail.

  * Fixed an issue where the **Submit** wrap-up button didn't appear in the call adapter after agents completed outbound calls.

  * Fixed an issue where an agent and caller still heard each other after the agent placed the caller on hold.

  * Fixed an issue in the agent desktop that occurred after an agent transferred a call to a different queue. The agent desktop layout of the source queue displayed to the receiving agent instead of the layout of the destination queue.

  * Fixed an issue where the reporting for after call work (ACW) time was artificially high for calls transferred to a third party.

  * Fixed an issue where overcapacity deflection settings interfered with after-hours deflections, causing calls to be incorrectly queued.

  * Fixed an issue where the inactivity timeout didn't function as configured.




## June 03, 2026

Announcement

**Google Cloud CCaaS 4.38**

We've released version 4.38 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Sort and filter emails**

Agents can now sort and filter emails by date in the email adapter.

User experience changes: The email adapter has the following new UI elements:

  * A button to toggle between **Oldest to newest** and **Newest to oldest** in the email list.

  * A **Filter by Date** list to filter by preset filters or by a configurable date range.




For more information, see [Email lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#email-lists).

Fixed

This release addresses the following issues:

  * Fixed an issue where Canadian French translations for notifications and error messages were appearing in English.

  * Fixed an issue where the Alvaria WFM **Agent Performance** report was exporting every minute instead of once daily.

  * Fixed an issue where the **Agent Preferences** table on the **Agent Availability** dashboard didn't update when an agent modified their availability preferences.

  * Fixed an issue that occurred when an agent manually changed their status to **Available** before the point in time that automatic wrap-up was configured to do so. In the **Activity Timeline** report, the status change was mistakenly attributed to the system.

  * Fixed an agent desktop issue where clicking the **Transfer** button in an SMS chat displayed an error instead of starting a transfer.

  * Fixed an issue where a delay in Salesforce task creation caused a lag in updating the ticket ID on calls.

  * Fixed an issue where agents couldn't transfer SMS chats.

  * Fixed an issue where incoming chats were routed to newly signed-in agents instead of to those who had been available the longest.

  * Fixed an issue where messages in the chat adapter's chat history weren't labeled or aligned to distinguish agent messages from end-user messages.

  * Fixed an issue in the IVR **Queue Menu Settings** pane where the text input field didn't appear when users selected **Text-to-speech**.

  * Fixed an issue in the SMS **Queue Menu Settings** pane where phone numbers weren't appearing in the incoming and outbound **Assigned Numbers** fields.

  * Fixed an issue where the web SDK didn't load.

  * Fixed an issue where live transcripts and conversation summarization didn't display in the agent desktop following an instance update.




## May 27, 2026

Announcement

**Advanced reporting dashboards 4.22**

We've released version 4.22 of the advanced reporting dashboards.

Feature

**Added a Location filter to dashboards**

The following dashboards now include a **Location** filter:

  * [Real-time Channel Performance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-channel-perf)

  * [Transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-transfers)

  * [Queue Interval](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-interval)




Feature

**Queue Performance dashboard improvements**

We've made the following improvements to the **Queue Performance - Calls** and **Queue Performance - Chats** dashboards:

  * Added the dashboards to the Advanced Reporting Landing Page.

  * Added a **Support Phone Number** filter.

  * Renamed the **Total Inbound Handled** tile (calls only) to **Total Queue Answered**.

  * Added a **Total Failed** tile.

  * In the **Queue Summary** table, removed the **Total Inbound Calls Handled** column and added the following columns: **Total Queue Interactions** , **Total Queue Entries** , **Total Queue Answered** , **Total Failed** , and **Total Transfers**.




For more information, see [Queue Performance dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-performance).

Feature

**General dashboard updates**

  * In the [Performance Overview](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-perf-overview) dashboard, we renamed the following tiles:

    * **Queued Now** to **Current Queued Now**

    * **Max Queue Time** to **Current Max Queue Time**

  * The [Real-time Connected - Calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-calls-connected) and [Real-time Connected - Chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-chats-connected) dashboards now include the following tiles:

    * **Total Connected Calls** (calls only)

    * **Total Connected Chats** (chats only)

    * **Avg Current Sentiment Score**

  * In the [Queue Group Performance - All](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-group-perf) dashboard, we renamed the **Lang** filter to **Language**.




Fixed

The following issues were addressed in this release:

  * Fixed an issue where the CSAT scores in the **Performance Overview** and **CSAT** dashboards didn't match.

  * Fixed an issue where the **Queue Performance** dashboard incorrectly totaled queue interactions, resulting in lower counts than expected.

  * Fixed an issue in the **All Interactions - Chat** dashboard where the **Virtual Agents Chats** table displayed the wrong chat.

  * Fixed an issue in the **All Interactions - Chat** dashboard where the **Failed Interaction** column of the **Chat Metric Detail** table displayed `False` for a failed interaction.

  * Fixed an issue in the **All Interactions - Chat** dashboard where the **Failed Interaction** column of the **Chat Metric Detail** table displayed `False` for a failed interaction.

  * Fixed an issue where the **Chat ID** filter on the **Queue Performance - Chats** dashboard incorrectly displayed placeholder values.

  * Fixed an issue where scheduled exports of large queries were limited to 500 rows, causing reporting delays.

  * Fixed an issue in the **Historical Data** table of the **Agent Activity** dashboard where the **Start Time** and **End Time** columns indicated incorrect durations for agents belonging to multiple teams.

  * Fixed an issue where short abandoned calls and chats were incorrectly included in the **Abandons** dashboard, causing inaccurate reporting of queue abandon times.

  * Fixed an issue where dashboard windows didn't fully display their contents.




## May 26, 2026

Announcement

**Google Cloud CCaaS 4.35**

We've released version 4.35 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Fixed

This release addresses the following issues:

  * Fixed an issue where URLs copied from Microsoft Word into SMS chat sessions were incorrectly formatted, causing links to merge with adjacent text.

  * Fixed an issue with Alvaria campaigns where the dialer didn't correctly use the country code from the **@COUNTRYCODE** field when selecting the contact number to dial.

  * Fixed an issue where live transcription didn't resume after an agent enabled and then disabled redaction during IVR payment card collection.

  * Fixed an issue where agents couldn't upload PDF files in chat sessions.

  * Fixed an issue where end-users encountered errors or empty details when accessing call history immediately after a call ended.

  * Fixed an issue where agents became stuck in the `In-call` status and couldn't end calls or change their status, preventing them from handling new interactions.

  * Fixed an issue where the deletion of the default greeting message for a language didn't persist.

  * Fixed a web SDK issue where scheduling a call in one queue incorrectly showed the **Reschedule Call** screen from a different queue.

  * Fixed an issue that occurred when a human agent invoked the payment virtual task assistant to collect card details. When the call was transferred back to the human agent, live transcription and sentiment analysis didn't resume.

  * Fixed an issue where HubSpot ticket creation failed when **Skip CRM Account Creation** and **Skip Account Lookup** were enabled. This resulted in tickets being created without an associated phone number.

  * Fixed an issue where, after transferring a call from one queue to another, the receiving agent's desktop temporarily showed the source queue's agent desktop layout instead of the destination queue's layout.

  * Fixed an issue where outbound Telnyx calls got stuck on the agent adapter **Connecting** screen when **Agent Voice Detection** was enabled globally.

  * Fixed an issue where Alvaria Advanced Outreach outbound campaign batch files weren't ingested by Contact Center AI Platform, preventing campaigns from loading contacts.

  * Fixed an issue where a single inbound call in Salesforce created two cases.

  * Fixed an issue where the **Agents** dashboard showed an invalid `-10` agent status during wrap-up and after calls.

  * Fixed an issue where Alvaria WFM Agent Performance reports displayed no agent activity.

  * Fixed an issue where the NICE WFM exporter reported higher abandoned call counts than Contact Center AI Platform reporting.

  * Fixed an issue where chats escalated from a virtual agent to a human agent were dismissed shortly after assignment.

  * Fixed an issue where the **Ticket URL** column in the **Individual Call History CSV report** was blank for newly recorded calls, preventing customers from accessing and downloading call recordings from the report.

  * Fixed an issue where newly created teams couldn't be reordered in the CCAI Platform portal.

  * Fixed an issue where the agent desktop **Previous Interactions** panel didn't show Agent Assist summaries from past calls.

  * Fixed an issue where conversation history didn't display correctly in the agent adapter when a chat was escalated from a virtual agent to a human agent and then a large number of messages were sent by the end-user.




## May 19, 2026

Announcement

**Google Cloud CCaaS 4.30**

We've released version 4.30 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Skip the IVR greeting message**

You can now configure your instance to skip the IVR greeting message.

Administrators: A new **Skip IVR Greeting** option is available in the **Settings > Languages & Messages > IVR-specific Messages** section.

For more information, see [Customize IVR-specific messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/customizing_languages_recordings_messages#configure-ivr-specific-messages).

Feature

**Headless web SDK: advanced call scheduling is turned on by default**

The `useAdvancedCallScheduling` parameter in the headless SDK is now set to `true` by default.

Feature

**Queue status endpoint**

The new queue status endpoint provides real-time data for leaf queues, including estimated wait times, agent availability, callback slot capacity, hours of operation, and holidays. This capability lets voice AI systems dynamically decide whether to escalate a call to a live agent or offer scheduled callback windows to the caller. You can access the queue status endpoint in the apps API: `GET /apps/api/v1/queues/status`.

For more information, see [The queue status endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-status-endpoint).

Feature

**For call transfers in HubSpot, the ticket owner is automatically updated**

When a call is transferred from one agent to another with a HubSpot integration, HubSpot tickets now automatically update to reflect the new ticket owner. This provides an accurate record of ownership throughout the interaction lifecycle. No configuration is required.

Fixed

This release addresses the following issues:

  * Fixed an issue where email messages in queues displayed a blank white panel when opened.

  * Fixed an issue that occurred when a closed ticket ID was passed to HubSpot using the SDK. The ticket wasn't reopened, resulting in new tickets being created.

  * Fixed an issue where agents pasted images into the chat adapter even when the **Allow agents to attach files** setting was turned off.

  * Fixed an issue where the agent adapter displayed generic error messages instead of call failure reasons such as `Busy` or `No answer`.

  * Fixed an issue where chat history wasn't deleted after a session ended, causing the agent desktop to become unstable for high-volume agents.

  * Fixed an issue where the NICE WFM ASCWS heartbeat timed out, causing agents to appear inactive and disrupting adherence reporting.

  * Fixed an issue where virtual agents unexpectedly disconnected during inbound IVR calls, causing the calls to escalate to a human agent.

  * Fixed an issue where customer utterances were missing from the Live Transcript when conversations were transferred from a Dialogflow CX agent to a human agent.

  * Fixed an issue where, when an agent searched for a queue during a chat transfer, the queue appeared with `No logged in agents` when agents were available.

  * Fixed an issue where launching a task virtual assistant during a chat caused the agent's screen to freeze.

  * Fixed an issue where call transcripts from CX Agent Studio agent conversations were added to CRM records as garbled and unreadable text, with repeated words and incorrect turn order.

  * Fixed an issue where the **Wait Time** custom field on Zendesk tickets displayed an incorrect value when using custom fields for **Account** and **Record**.

  * Fixed an issue where agents assigned a direct SMS-capable line didn't receive visual notifications for incoming SMS chats in the agent adapter while their status was set to `Unavailable`.

  * Fixed an issue where chat transcripts couldn't be downloaded from the **Completed Chats** page.

  * Fixed an issue where customer calls were unexpectedly abandoned during payment transactions when DTMF inputs were provided.

  * Fixed an issue where agents heard repeated call notification sounds during active calls, even when no new call was assigned.

  * Fixed an issue where only English IVR queues appeared when configuring agent-specific deflection settings, even when other language queues were available.



  * Fixed an issue where email messages in queues displayed a blank white panel when opened.

  * Fixed an issue where chat transcript and metadata files were generated as empty files, causing API timeouts and blocking reporting pipelines.

  * Fixed an issue where chat sessions that ended due to end-user inactivity were marked as **Disconnected by end user** instead of **Timeout: end user stopped responding**.

  * Fixed an issue where agents couldn't receive more than 12 concurrent chats despite being configured for up to 30.

  * Fixed an issue where virtual agent calls were routed back to the original queue instead of being handled as expected.

  * Fixed an issue that occurred when a third party was added to a call. After all participants left the call, the call still appeared to be connected.

  * Fixed an issue where cascade conditions for agent queues didn't correctly enforce the minimum number of available UK agents before allowing calls to cascade from the US queue, resulting in calls being routed incorrectly.

  * Fixed an issue where bulk user import incorrectly limited the chat concurrency value to the global default, preventing valid per-agent settings from being uploaded.




## May 13, 2026

Announcement

**Mobile SDK for iOS version 2.15.4 patch**

This patch includes the following updates for the mobile SDK for iOS:

  * Fixed an issue where the iOS app crashed during disconnections.

  * Updated the Twilio Voice and Chat SDKs.




## May 06, 2026

Announcement

**Mobile SDK for iOS version 2.15.3 patch**

This patch updates the following for the mobile SDK for iOS:

  * Fixes an issue where the iOS SDK app crashed when a user clicked **End chat**.



## May 04, 2026

Announcement

**Google Cloud CCaaS 4.26**

We've released version 4.26 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Fewest Agents Routing**

Fewest Agents Routing has been added to chat Deltacast configuration. Fewest Agents Routing keeps busy agents engaged while preserving idle agents for future workload spikes.

Administrators:

  * The following new settings are available at **Settings > Operation Management > Routing > Chat Routing > Deltacast Routing Logic**:

    * **Longest Idle Routing to distribute workload equally between agents**. This is the same as the previous default routing behavior.

    * **Fewest Agents Routing to maximize utilization and call availability**. This is the new routing behavior that concentrates new chats on busy agents.




For more information, see [Deltacast routing logic for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#deltacast-routing-logic-for-chat).

Feature

**Skip account or record creation for HubSpot**

You can configure your instance to prevent the automatic creation of accounts and records in HubSpot while ensuring that data such as media files and transcripts is preserved. You can configure how the system handles closed records when a record ID is passed using the SDK.

Administrators:

  * The following new settings are available at **Settings > Operation Management > CRM Record Creation Details**:

    * **Skip CRM account creation**

    * **Skip CRM account lookup**

    * **Skip CRM record creation**

    * **Closed record options when record ID is passed in via SDK**

      * **Create new record**

      * **Reopen record**




For more information, see [Configure HubSpot record creation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-configure-record-creation).

Feature

**Improved Agent Assist visibility during transfers**

When a chat is transferred, the originating agent and the receiving agent see Agent Assist as it's configured for their respective teams or queues. This behavior now also applies to transfers of direct inbound calls.

For more information, see [Configure Agent Assist at the team level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#configure-team-for-agent-assist).

Feature

**Breakthrough for wrap-up improvements**

If breakthrough is configured for `Wrap-up` and `Wrap-up Exceeded` statuses, agents can now answer breakthrough calls even if they haven't completed the following:

  * Submitted disposition codes and notes.

  * Manually switched to `Available` status.




Additionally, agents in `Wrap-up` status who accept breakthrough calls before submitting disposition codes and notes can now switch between the call and the wrap-up screen.

User experience changes include the following:

  * The call adapter contains a switcher button that lets agents switch between an ongoing call and the wrap-up screen for a previous call.

  * The mini-adapter on the agent desktop expands to let you switch between an ongoing call and the wrap-up screen for a previous call.




For more information, see [Breakthrough for wrap-up](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#breakthrough_for_wrap-up).

Feature

**Custom field mapping for HubSpot**

You can map your web or mobile SDK custom data fields to your HubSpot installation's custom fields. At runtime, when the SDK sends a custom data value, the system writes the value to the mapped HubSpot custom field.

Administrators: On the **Settings > Operation Management** page, there's a new **Custom Field Mapping** pane.

For more information, see [HubSpot custom field mapping](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-custom-field-mapping).

Feature

**Call scheduling improvements**

We've made the following improvements to call scheduling for web SDK v3 and the headless web SDK:

  * **Configurable time slots**. You can configure the length of call-scheduling time slots.

  * **Day-based time slot selection**. End-users can browse available time slots organized by day.

  * **Rescheduling**. If an end-user reopens the web SDK and has an existing scheduled call, they're prompted to manage that appointment (reschedule or cancel) before starting a new flow.

  * **Cancellation**. End-users can cancel a previously scheduled call.

  * **Queue-level configuration**. You can configure call scheduling at the queue level.


**Note:** Headless web SDK users must specify `useAdvancedCallScheduling: true` with calls to the `getTimeSlots` method to access these call scheduling improvements.

Administrators:

  * There's a new **Scheduled Calls** pane on the **Settings > Calls** page.

  * There's a new **Scheduled Calls** section in the **Settings > Queue > Web > `SELECT_QUEUE`** pane.

  * We moved **Scheduled Call Countdown** and **Scheduled Call Expiration** from **Settings > Calls > Call Details** to **Settings > Calls > Scheduled Calls**.

  * We've added the following settings to the **Settings > Calls > Scheduled Calls** pane:

    * **Consumers can schedule calls up to` SELECT_INTEGER` day(s) in the future**

    * **Static > Maximum calls per time slot**




User experience changes:

  * For **Scheduled Calls** , if you select **Consumers can schedule calls up to` SELECT_INTEGER` day(s) in the future**, a new **Select a day** screen appears to end-users who reschedule a call.



For more information, see [Scheduled calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#scheduled-calls).

Feature

**Headless web SDK updates**

We've made the following updates to the headless web SDK:

  * New methods:

    * **fetchTimeSlotAvailability**. Check if time slots are available for a given menu.

    * **restoreCobrowseSession**. Restores a cobrowse session after the browser window is reopened.

    * **getLogs**. Gets the internal debug logs collected by the SDK.

  * Updated signatures:

    * **getTimeSlots**. Includes the `GetTimeSlotsRequest` interface.

    * **updatePostSession**. Includes an `optInSelection` parameter.




For more information, see [getTimeSlots](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-api#get-time-slots).

Feature

**Accessibility and design improvements**

We've made the following accessibility and design improvements to the web SDK v3 and the headless web SDK:

  * **WCAG Compliance**. Updated to comply with Web Content Accessibility Guidelines (WCAG).

  * **Right-to-left support**. Now supports right-to-left languages: Arabic, Hebrew, Farsi, and Urdu.

  * **Improved screen reader compatibility**. Improved support for screen readers.

  * **Improved spacing**. Uses 4px-based spacing to improve the look and feel of page displays.




Fixed

This release addresses the following issues:

  * Fixed an issue where the Telnyx integration attempted to reconnect websockets after a failure, even when this behavior wasn't desired.

  * Fixed an issue where Agent Assist disappeared for the third agent during consecutive queue transfers.

  * Fixed an issue where empty responses from Dialogflow were passed through to CCAI Platform, resulting in undefined call behavior.

  * Fixed an issue where active outbound campaigns stopped dialing when a concurrent campaign encountered timezone restrictions, requiring manual intervention to resume calls.

  * Fixed an issue where campaigns didn't resume after being paused, resulting in call session failures and missing participant information.

  * Fixed an issue where chat transfers involving multiple agents failed, causing agents to become stuck in an "in chat" status even when no active chats were present.

  * Fixed an issue where incoming chats were routed to newly signed-in agents instead of agents who had been available the longest.

  * Fixed an issue where chat messages sent by end-users immediately after starting a chat, but before an agent joined, weren't delivered to the agent.

  * Fixed an issue where the `recording_url` field in session data wasn't populated after calls ended.

  * Fixed an issue where call transfers were incorrectly tagged as **Warm** instead of **Cold** when the transferring agent disconnected before the receiving agent answered.

  * Fixed an issue where call recordings for sessions ending with a virtual agent post-call survey were truncated. This resulted in the main human agent conversation not being saved.

  * ~~Fixed an issue where outbound call restrictions incorrectly blocked calls to Japanese numbers, even when settings allowed them.~~

  * Fixed an issue where agents became stuck in **Wrap-up** status after a call was transferred to another agent's voicemail and the end user disconnected during the voicemail greeting.

  * Fixed an issue where, in third-party transfer calls with **Call recording for third-party transfers** set to off, redaction didn't begin immediately after the agent disconnected.

  * Fixed an issue where calls didn't connect and re-queued, resulting in long queue times for agents.

  * Fixed an issue where disposition lists in the call adapter didn't appear in alphabetical order, as configured in the portal.

  * Fixed an issue where chats in the agent desktop didn't transition to the **End Wrap-Up** state after the agent clicked **Submit**.

  * Fixed an issue where the `apps/api/v1/users` API returned only 100 records per page, even when a higher limit was specified.

  * Fixed an issue where filtering by queue name on the **Queued Chats** and **Queued Calls** pages didn't return accurate results.

  * Fixed an issue where updating an agent's skills from the **Agents** page mistakenly removed their extension number.

  * Fixed an issue where users of the **Dialer Admin** role couldn't add teams to a queue.

  * Fixed an issue where call wrap-up interactions recorded inaccurate data, such as excessive wrap-up times, redundant instances, and incorrect chronological sequencing.

  * Fixed an issue that occurred when an agent with Agent Assist transferred a call to a second agent with Agent Assist. After the transfer, the second agent no longer had access to Agent Assist.

  * Fixed an issue with Salesforce integrations in the agent desktop where notification flags overlapped the Salesforce Utility Bar navigation, which prevented agents from accessing navigation controls.

  * Fixed an issue where agents were incorrectly reported as `Available` for an extended period after signing out.

  * Fixed an issue where calls waiting in a queue with no available agents weren't connected when an agent became available.

  * Fixed an issue where the previous CCAI Insights name appeared in the portal instead of Customer Experience Insights.

  * Fixed an issue for Alvaria users where the Agent Performance Report was mistakenly generated and sent at 7:00 PM instead of midnight, which resulted in incomplete 24-hour performance data.

  * Fixed an issue where agents who left a predictive campaign pool were incorrectly left in `Available` status.

  * Fixed an issue where chat sessions returned an error during post-session transfer if no virtual agent participant was active.

  * Fixed an issue where, after a call failure, the agent adapter displayed a generic error message instead of an error message that included the failure reason.

  * Fixed an issue for Telnyx users where the instance stopped responding.

  * Fixed an issue that occurred when users tried to delete a queue. A message was returned saying that the queue was assigned as a deflection or redirection option even though these settings weren't activated for the queue.

  * Fixed an issue where adding multiple voice queues resulted in long loading times, request timeouts, and incorrect concurrency errors.

  * Fixed an issue where overcapacity deflection options messages mistakenly played twice instead of once.

  * Fixed an issue where chats escalated by a virtual agent disconnected seconds after assignment to a human agent, which prevented the human agent and the end-user from interacting.

  * Fixed an issue where spurious chat interactions appeared in the **All Interactions** dashboard, which caused discrepancies in handled chat reporting and incorrect failed session filtering.

  * Fixed a web SDK v3 issue where the out-of-office deflection message that appeared in the end-user's chat window didn't match the message in the chat transcript.

  * Fixed an issue where agents received incorrect **Missed target response time** notifications in agent desktop SMS chats, even when responding promptly.

  * Fixed an issue where agents attempting to access their contact center using private ingress couldn't connect.

  * Fixed an issue where the **Allow transfers to queues outside of hours of operation** checkbox was unexpectedly unavailable.

  * Fixed an issue where verified outbound phone numbers couldn't be added to a queue because the selection field was empty, which prevented administrators from assigning new phone numbers.

  * Fixed an issue where attempts to rename IVR queues using redirection data in legacy YAML files resulted in errors.




## April 24, 2026

Announcement

**Mobile SDK for iOS version 2.15.2 patch**

This patch updates the following for the mobile SDK for iOS:

  * Fixed an issue with the mobile SDK on iOS 26 where the chat text field was partially obscured because it appeared too low on the screen.



## April 15, 2026

Announcement

**Google Cloud CCaaS 4.21**

We've released version 4.21 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Language selection support for direct calls**

End-users making direct calls to agent phone numbers and agent extension numbers can select their language at the start of a call.

Administrators: The **Add Number** and **Edit a Number** dialogs, located at **Settings > Call > Phone Numbers > Phone Number Management**, have a new **Set languages** checkbox (when the **Set as a direct number** checkbox is selected). When you select the **Set languages** checkbox, the **Select languages** list appears.

For more information, see [Create a direct phone number](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#create-direct-phone-number).

Feature

**"Improved controls for predictive campaigns" is available without assistance from the Google account team**

This feature was announced on [March 24, 2026](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#March_24_2026) but previously required the Google account team to enable it. You no longer need assistance from the Google account team to use this capability. For more information, see [Predictive campaigns](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-predictive).

Feature

**Virtual agents can transfer calls to a specific human agent**

Virtual support agents can transfer calls directly to a specific human agent using the agent ID or agent extension number. Include the `agent_extension` or `agent_id` field in the transfer payload to direct the call to the correct agent. Transferring directly to a human agent eliminates the intermediate step of transferring to a queue before transferring to the agent. This can improve wait times and customer satisfaction. For more information, see [Virtual agent to human agent transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent-to-human-agent-transfers).

Fixed

The following issues were addressed in this release:

  * Fixed an issue where backslash characters in chat shortcuts and chat messages weren't displayed correctly, resulting in missing or empty message chat bubbles.

  * Fixed an issue where virtual agent chat transcripts didn't match the actual conversation.

  * Fixed an issue where call times in session metadata for virtual agent to human agent escalations were shorter than the actual call times.

  * Fixed an issue where agents were able to join a conference call despite receiving microphone permission errors.

  * Fixed an issue where direct inbound calls to Twilio numbers assigned at the user level continuously rang without reaching the agent.

  * Fixed an issue where chat transfers from auto-answer queues to manual-answer queues were incorrectly recorded as manual-to-manual in reporting.

  * Fixed an agent desktop issue where French (Canadian) translations were missing or incorrect during outbound calls.

  * Fixed an issue where the **All Teams** filter didn't block interactions with background elements, which caused unintended end-user interactions with the UI.

  * Fixed an issue where missed call volumes didn't appear on the agent monitoring page.

  * Fixed an issue that occurred when the **Display transfer history in agent adapter** capability was enabled. After a virtual agent escalation, escalated queue names were shown in English instead of the correct target language.

  * Fixed an issue where virtual agent audio sessions ended after 15 minutes, causing calls to be escalated unexpectedly.

  * Fixed an issue where underscores within email addresses were incorrectly removed in CRM transcripts.

  * Fixed an issue where chat transcript PDFs weren't generated when real-time redaction was enabled and conversations included non-text message types such as inline buttons or content cards.

  * Fixed an issue where content cards sent by virtual agents during conversations were missing from the PDF chat transcript.

  * Fixed an issue where chat transcripts created through the API weren't appearing in agent conversations.

  * Fixed an issue where voicemails disappeared from the agent's queue and didn't appear in voicemail history or reports.

  * Fixed an issue where the agent adapter displayed **Escalated Virtual Agent Call** instead of **IVR Callback** after connecting during a callback.

  * Fixed an issue where chat disposition selections reset during wrap-up, particularly when Agent Assist was enabled.

  * Fixed an issue where custom fields in dialer list uploads worked only if the column headers were in all caps.

  * Fixed an issue where the email adapter didn't start up.




## April 07, 2026

Announcement

**Advanced reporting dashboards 4.12**

We've released version 4.12 of the advanced reporting dashboards.

Feature

**Repeat contacts data added to advanced reporting dashboards**

Repeat contacts data is now available in the following advanced reporting dashboards:

  * **Real-time Queue Monitoring - Calls** and **Real-time Queue Monitoring - Chats** : new **Total Repeat Contacts** tile. For more information, see [Queue monitoring dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-real-time-queue-monitor).

  * **All Interactions - Calls** and **All Interactions - Chats** : new **Repeat Contact** column in the **Call Metric Detail** and **Chat Metric Detail** tables.

  * **Real-time Calls - Calls Connected** and **Real-time Chats - Chats Connected** : new **Repeat Contact** column in the **Connected Calls** and **Connected Chats** tables.




Feature

**New Total Queued Answered metric in the Chat Queue Metrics Explore**

The **Chat Queue Metrics** Explore now includes the **Total Queued Answered** metric. This metric provides a precise count of chats answered from the queue, providing accurate Service Level Agreement (SLA) and answer rate calculations where the standard "handled" metric might not apply—for example, if a chat is answered and then immediately disconnected.

Fixed

The following issues were addressed in this release:

  * Fixed an issue where dashboard names and favorite buttons were missing, preventing users from renaming dashboards and marking them as favorites.



  * Fixed an issue where fields for hourly and 30-minute intervals in call queue metrics didn't display detailed data over long date ranges.

  * Fixed an issue where the **Teams Filter** filter displayed incorrect data.

  * Fixed an issue where calls that started at a specific time didn't appear in their corresponding time windows.




  * Fixed an issue in the Agent Activity dashboard where the **Created By** column attributed status changes to an agent when an administrator performed the changes.

  * Fixed an issue where historical call and chat metrics displayed incorrect timestamps.

  * On the **Real-time Queue Monitoring - Calls** and **Real-time Queue Monitoring - Chats** dashboards, in the **Historical Data** tables, the **Avg CSAT** column was renamed **CSAT**.

  * Fixed an issue on the **Channel Interval - Calls** and **Channel Interval - Chats** dashboards where drill-down views in the trend tiles displayed incorrect information or were empty.

  * Fixed an issue in the **Queue Group Performance - All** dashboard where blue highlighting wasn't applied to populated fields in the **Queue Group Performance Calls** and **Queue Group Performance Chats** tables.




## April 02, 2026

Announcement

**Google Cloud CCaaS 4.16**

We've released version 4.16 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Agent Assist is available for calls and chats that are unassociated with a queue**

You can now turn on Agent Assist for calls and chats at the team level. That means that Agent Assist is available for interactions that aren't associated with a queue, such as direct inbound calls and outbound calls with no queue selected.

Administrators: In the **Settings > Users & Teams > Manage Users & Teams >** edit **TEAM_NAME** pane, there's a new **Agent Assist** section.

For more information, see [Configure Agent Assist at the team level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#configure-team-for-agent-assist).

Feature

**New HubSpot CRM ticket view: Help desk view**

You can now configure which CRM ticket view your HubSpot integration uses: **Standard view** , or the new real-time **Help desk view**.

Administrators: In the **Settings > Developer Settings >** select **HubSpot** pane, there's a new **CRM Ticket View** section.

For more information, see [Configure HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot#configure-hubspot).

Feature

**Play pre-recorded audio for virtual agents**

Dialogflow lets virtual agents respond with pre-recorded audio. This lets you use high-quality audio files instead of standard text-to-speech. This capability is available for all voice channels, including inbound and outbound calls. It's available for support virtual agents, task virtual agents, and post-session virtual agents. For more information, see [Play pre-recorded audio](https://docs.cloud.google.com/contact-center/ccai-platform/docs/play-prerecorded-audio).

Feature

**Configure the ringing timeout for virtual agent transfers to SIP endpoints**

Twilio users can configure the ringing timeout for outbound calls that virtual agents transfer to SIP endpoints. Add the `sip_ring_timeout` field to the virtual agent's custom payload to set the ringing period for up to 600 seconds. This allows calls to internal extensions or Unified Communications (UC) destinations sufficient time to be answered before disconnection. For more information, see [Transfer a call to a SIP endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#transfer-to-SIP-endpoint).

Fixed

The following issues were addressed in this release:

  * Fixed an issue with React Native integrations where the email adapter wouldn't load. TBD - confirm that there's only one bug related to the email adapter not loading with React Native integrations.

  * Fixed an issue where enabling chat redaction caused the unredacted messages to be redacted in the chat adapter.

  * Fixed an issue where calls continued to be recorded after being transferred to a third-party number, even when the **Continue Call recording to Third Party Numbers after the agent leaves the call** setting was cleared.

  * Fixed an issue where emails were automatically assigned to users without agent roles.

  * Fixed an issue where the global **Overcapacity Deflection Messages** setting was configured for **Uploading Audio Recordings** , but queues inheriting global settings incorrectly displayed **Text-to-speech** in the UI.

  * Fixed an issue where agents couldn't transfer a chat within the same queue.

  * Fixed an issue where incoming calls unexpectedly ended with 603 decline errors after ringing for 13 seconds.

  * Fixed an issue in the Agent Desktop where the session ID didn't match the call ID for the same interaction.

  * Fixed an issue where user search results didn't display users in locations with the same first three letters of the name when searching for partial locations.

  * Fixed an issue that let end-users interact with a mailbox immediately after switching to a different mailbox, causing synchronization issues.

  * Fixed an issue where overcapacity deflection didn't work for direct inbound calls.

  * Fixed an issue where the Reporting API changed the data types of some response fields. This caused data type mismatches in the reports that the API returned.




Announcement

**Mobile SDK for Android version 2.15.2 patch**

This patch updates the following for the mobile SDK for Android:

  * Updates `minSdkVersion` to `25`.

  * Upgrades the following dependencies:

    * Twilio Conversations to 6.2.1

    * Twilio Voice to 6.10.2




## March 25, 2026

Announcement

**Web SDK version 2 will be shut down on June 26, 2026**

On June 26, 2025, we announced the launch of [Web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025). Starting on **June 26, 2026** , the web SDK v2 will no longer function. Be sure to [update your website](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

## March 24, 2026

Announcement

**Google Cloud CCaaS 4.12**

We've released version 4.12 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Support for creating chat virtual agents using CX Agent Studio**

Contact Center AI Platform supports creating chat virtual agents using [Customer Experience Agent Studio](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps) (CX Agent Studio). This expands on its existing support for creating voice virtual agents with CX Agent Studio.

For more information, see [Create and integrate Customer Experience Agent Studio agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-cx-agent-studio-agent).

Feature

**Callback fulfillment hours**

You can configure callback fulfillment hours, which are the hours when your contact center fulfills callbacks. If you enable callback rollovers to the next day, callbacks that are scheduled outside of these hours are rolled over to the next day. If you don't enable callback rollovers, callbacks that are scheduled outside of these hours are canceled. Callback fulfillment hours aren't available by default. To use this capability, ask your Google contact to turn it on for your instance. For more information, see [Callback fulfillment hours](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#callback-fulfillment-hours).

Feature

**Improved support for multiple agent matches for agent extension searches**

When an end-user inputs an agent extension number at the beginning of a call and there are multiple agent matches, the system now reads agent matches in groups of eight. This gets the end-user to the correct agent faster. We've added the following new extension directory messages to help guide the end-user to the correct agent:

  * Multiple agents found

  * Search results next page

  * End of search results




For more information, see [Extension directory messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#extension-directory-messages).

Feature

**HubSpot lookup against company profiles**

HubSpot integrations now support lookups against Company profiles. Administrators can configure primary and secondary lookup objects, allowing the system to search for end-users across both Contacts and Companies to ensure accurate identification during active sessions.

For more information, see [HubSpot lookup against company profiles](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups).

Feature

**HubSpot: Mobile Phone Number Lookup**

Admins can now enable mobile phone number lookups for HubSpot integrations to ensure callers are accurately matched with existing contacts. To activate this, navigate to **Settings > Developer Settings > CRM** and check the **Mobile phone number lookup** box in the new **Phone Number Lookup** section. Once enabled, the system will automatically search both the "Phone number" and "Mobile phone number" fields in HubSpot during incoming voice or chat sessions. For more information, see [HubSpot mobile phone number lookup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-mobile-phone-lookup).

Feature

**Improved controls for predictive campaigns**

We've added the following controls to predictive campaigns to reduce the risk of call abandonment due to overdialing. These controls let you ramp up dialing rates more naturally and consistently.

  * **Max Calls Per Agent**

  * **Target Agent Occupancy**




We've also made the **Max Abandonment %** setting optional, for campaigns that don't require maintaining a maximum abandonment percentage.

Administrators: When you click **Campaigns > Add Campaign > Mode > Predictive**, the new controls appear in the **Add Campaign** dialog.

For more information, see [Predictive campaigns](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-predictive).

Feature

**Resume chat endpoint**

You can use the new `chats/CHAT_ID/resume` endpoint to resume chat sessions that are in `dismissed` or `va_dismissed` status. Resumed chat sessions display the chat history to both the end-user and the agent.

For more information, see [Resume a chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/resume-a-chat).

Fixed

The following issues were addressed in this release:

  * Fixed an issue for Zendesk users where using click-to-dial from a private note failed to display existing tickets for outbound calls, forcing agents to create new tickets.

  * Fixed an issue for Brightspeed users where the CRM link in the agent adapter didn't open during calls or chats.

  * Fixed an issue where call recordings between agents and end-users didn't upload to Salesforce promptly.

  * Fixed an issue where agents placing an outbound call couldn't select queues from their parent team.

  * Fixed an issue where agent status durations continued to accrue even after agents logged out or went offline.

  * Fixed an issue where web queue redirects didn't work with domains ending in `.today`.

  * Fixed an issue in the **Agent** dashboard where team names with a forward slash displayed the HTML character entity (`&#x2F;`) instead of the forward slash.

  * Fixed an issue where changing agent status after completing wrap-up displayed the wrap-up screen instead of the new status.

  * Fixed an issue where the default global contact list was missing, despite being enabled, preventing end-users from accessing this directory.

  * Fixed an issue where virtual agent calls weren't recorded and uploaded to external storage even when call recording was turned on.

  * Fixed an issue where outbound calls were incorrectly prompting for customer satisfaction (CSAT) feedback when a menu was assigned.

  * Fixed an issue where the French Canadian translation for "wrap-up" was inconsistent between the chat adapter and notes panel.

  * Fixed an issue where filtering agents by Team on the Agents tab resulted in significant delays.

  * Fixed an issue where users were unable to download reports from the virtual agent dashboard and chat history if the requested date range exceeded the storage retention period.

  * Fixed an issue where SMS, WhatsApp, and AMB queues that were copied from Web or IVR channels incorrectly inherited transfer restrictions, preventing agents from transferring chats.

  * Fixed an issue where users were unable to upload a key when adding or editing a redaction platform under developer settings.

  * Fixed an issue where call recording links were not being pushed to HubSpot cases as expected.

  * Fixed an issue where agents intermittently failed to connect to incoming calls and were immediately disconnected, causing calls to requeue or drop unexpectedly.

  * Fixed an issue where chat and call queues appeared unavailable for transfers when destination agents reached maximum capacity or were in an unavailable status.

  * Fixed an issue where toggling the Whisper Announcement or Countdown settings in Automatic Redirection would unintentionally disable the Customize Greetings Announcement option.

  * Fixed an issue where callback selections made after a virtual agent handover were not accurately reflected in downloadable reports.

  * Fixed an issue where the **Available** filter didn't display agents that were available to receive a transfer.

  * Fixed an issue with Alvaria Workforce integrations where files were rejected due to a random suffix added to the RECORDKEY value.

  * Fixed an issue where two end-users could be connected simultaneously to a single agent during campaign calls.

  * Fixed an issue where the inactive chat dismissal timer did not reset after a conversation was escalated from a virtual agent to a live agent queue.

  * Fixed an issue where transcript metadata files were sometimes stored in the folder for the following day instead of matching the transcript file date, ensuring all metadata and transcript files are now consistently organized by the correct chat end date.

  * Fixed an issue where agents appeared available but were unable to receive or be re-offered calls due to repeated WebSocket presence updates and connection expirations.

  * Fixed an issue where Direct Access Points configured with SIP URIs containing spaces or non-standard formats failed to route calls correctly.

  * Fixed an issue where the Agents tab filter in the UJET Portal displayed "All undefined" and was unclickable, preventing manual agent selection.

  * Fixed an issue where managers could access queue reports requested by other managers, even if they were not involved in the relevant queues.

  * Fixed an issue where searching by Location on the Users & Teams page could return agents who no longer matched the search criteria. Search results now accurately reflect current agent locations.

  * Fixed an issue where users did not see a message indicating that no time slots were available when selecting a queue with no available time slots.

  * Fixed an issue where the fetch time slots endpoint incorrectly included non-working days when calculating available future time slots.

  * Fixed an issue where call recordings failed to convert from MP3 to WAV, preventing playback in Call Quality Assurance tools that require WAV format.

  * Fixed an issue where, after a warm call transfer, if Agent 1 left the call and Agent 2 resumed the conversation, there was no audio between Agent 2 and the end user.

  * Fixed a 500 Internal Server Error that occurred when administrators tried to add a new language (for example, Danish) under the "Languages and Message" settings. This error prevented the language from being added to the list.

  * Fixed an issue where the chat widget landmark was missing an accessible label. The chat widget now includes an aria-label matching the chat button label.

  * We have updated the session metadata to provide a strict distinction between Escalations and Transfers. This ensures that reporting accurately reflects the business context of how a session moves between resources. The session metadata will now categorize these events as follows:

    * **Escalation** : Recorded only when a Virtual Agent transfers a session to a Human Agent.

    * **Transfer** : Recorded for all other routing scenarios, including:

      * Human Agent > Human Agent

      * Virtual Agent > Virtual Agent (Support or Task)

      * Human Agent > Virtual Agent

  * Fixed an issue where updating a contact's mobile phone number during an interaction would incorrectly overwrite the existing phone number field.

  * Fixed an issue where chats that ended due to end user timeout or disconnection were incorrectly shown as "undefined" in the Interaction Outcome column of platform reports.

  * Fixed an issue in WFM data where the handle count was showing incorrect information if a chat spanned multiple intervals.

  * Fixed a data discrepancy in NICE WFM interval reports where chat metrics (specifically ContactsReceived and HandledLong) were incorrectly showing activity during time intervals where no chats actually occurred.

  * Fixed an issue where calls transferred using warm transfer to another queue were incorrectly deflected due to overcapacity, resulting in a cold transfer instead.

  * Fixed an issue where agents with multiple custom roles were incorrectly prevented from changing to certain statuses due to role restriction logic.

  * Fixed an issue where changing the "Custom After Hours Deflection" setting in queue configuration would incorrectly reset wrap up settings from "Queue" to "Global."

  * Fixed an issue where users with custom roles and correct permissions for Queues were unable to add teams.

  * Fixed an issue where the right-side columns on the outbound phone numbers page were not visible and could not be accessed when the browser window was too small.

  * Fixed a web SDK issue where the chat modal on Android Chrome was not recognized by screen readers due to a missing dialog role.

  * Fixed a web SDK issue where elements behind the Text size menu overlay were focusable, ensuring that keyboard focus now remains on the Text size menu until it is dismissed by the user.

  * Fixed a web SDK issue where the "Request a call" option in the chat widget was not accessible to screen reader or keyboard-only users.

  * Fixed an issue where agents were incorrectly presented with a manual "Answer" button and placed in "Missed Call" status after a single missed Deltacast, even when auto answer was enabled.

  * Fixed an issue where transferring a direct outbound call to a queue could fail with a "Not Found" error, even when the target menu and agents were available.

  * Fixed an issue where the disposition list was not displaying in the configured custom order and instead appeared alphabetically in both Agent Desktop and standard Agent Adapter.

  * Fixed an issue where the user inactivity timeout setting did not consistently log out users as configured.

  * Fixed an issue where queue channels and menu options would intermittently disappear or fail to load correctly due to delays in feature flag initialization.

  * Fixed an issue where adding multiple agents to a team would fail if any selected user was already a member, resulting in a vague error and no agents being added.

  * Fixed an issue in Progressive Campaigns where agents were intermittently connected to two outbound call targets simultaneously. This occurred when a dial attempt terminated immediately but failed to detach from the conference bridge before the next attempt connected.

  * Fixed an issue where deleting a queue that was the target of an automatic redirection could cause transfer options to fail to load for agents.

  * Fixed an issue where adding multiple agents to a team would fail if any selected user was already a member, resulting in a vague error and no agents being added. 

  * Fixed the following issues that occurred with dual-channel and segmented call recordings:

    * Calls escalated from virtual agents weren't being recorded properly.

    * Recordings of conversations with transferred agents were missing.

  * Fixed an issue where chats escalated from a virtual agent to a human agent queue were incorrectly set to auto answer.

  * Fixed an issue where the call recording warning message didn't play for callbacks initiated by virtual agent escalation when the destination queue exceeded capacity.

  * Fixed an issue where search results in the **Directory** tab of the **Transfer/Add party** screen in the call adapter persisted after closing and reopening the screen.

  * Fixed an issue where the call adapter displayed an error when the **Call** button was clicked.

  * Fixed an issue where uploading an automatic-redirection audio recording in one IVR queue caused the recording to incorrectly appear in a different IVR queue.

  * Fixed an issue where custom agent statuses restricted to specific roles weren't visible to users assigned those roles.

  * Fixed an issue where contacts added to an outbound campaign using the `/outbound_dialer/campaigns/CAMPAIGN_ID/contacts` endpoint weren't dialed.

  * Fixed an issue where users who authenticated with Single Sign-On (SSO) couldn't update their profiles due to an invalid password error.

  * Fixed an issue where the queue list on the **Settings > Queues** page didn't load for instances with a large number of queues.

  * Fixed an issue where the interaction history in the agent adapter incorrectly displayed as empty.

  * Fixed an issue where Salesforce account lookup settings couldn't be saved when selecting the `Person Account` object and record types.

  * Fixed an issue in the chat adapter where the **Previous Interactions** summary displayed duplicate section headings (**Customer Satisfaction** and **Action**) and an incorrect section heading (**Label**).

  * Fixed an issue where team managers couldn't download agent reports when selecting the **All Agents** filter.

  * Fixed an issue where the system didn't record the failure reason when a virtual agent tried to escalate a chat to a human agent outside of operating hours.

  * Fixed an issue where using the **Bulk User Management** tool to deactivate users failed.

  * Fixed an issue where the **Monitoring Chat** screen displayed chats incorrectly, with misaligned chat bubbles, incorrectly formatted bullets, and missing sender names and timestamps.

  * Fixed an issue where the **Directory** screen in the call adapter appeared empty when an agent tried to start an internal call transfer to another agent.

  * Fixed an issue where agent prioritization for deltacast selection was incorrect.

  * Fixed an issue that occurred when a human agent didn't respond to a transferred or auto-answered session. The system incorrectly recorded the termination reason as "agent stopped responding" instead of "timeout waiting for agent message".

  * Fixed a web SDK issue where underscores in text (for example, in email addresses like user_name@example.com) were incorrectly removed in messages to end-users.

  * Fixed a web SDK issue for iOS users where the **Yes** and **No** buttons in the survey request at the end of a chat were hidden.




## March 14, 2026

Announcement

**Advanced reporting dashboards 4.0**

We've released version 4.0 of the advanced reporting dashboards.

Feature

**Voicemails dashboard**

With the **Voicemails** dashboard, get insights into the volume of voicemails received by your contact center and the performance of your agents in responding to them. This includes the number of voicemails received, the number of voicemails accessed by agents, and the average agent response time. For more information, see [Voicemails dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-voicemails).

Feature

**Queue Performance dashboard**

With the **Queue Performance - Calls** and **Queue Performance - Chats** dashboards, get performance metrics by queue for your call and chat sessions. This includes queue interaction volume, abandons, handle time, callbacks, sentiment, and CSAT. For more information, see [Queue Performance dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-performance).

Feature

**Update to the Virtual agent dashboard for wait-time virtual agent metrics**

The **Virtual agent** dashboard includes the following new tiles to measure the activity of wait-time virtual agents while end-users wait in queue:

  * **Total VA In-Queue Interactions** (calls only): the number of calls where wait-time virtual agents were active while end-users were in a queue

  * **Total VA In-Queue Time** (calls only): the total time that wait-time virtual agents were active while end-users were in a queue

  * **Avg VA In-Queue Time** (calls only): the average time that wait-time virtual agents were active while end-users were in a queue




For more information, see [Virtual agent dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent).

Feature

**Advanced reporting is available in French Canadian**

Advanced reporting dashboards are now available in French Canadian. For more information about configuring your instance for location and language, see [Configure location and language](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-location#configure-location-and-language).

Feature

**Improved analytics for Queue Interval and Channel Interval dashboards**

We've improved the detailed information available for the **Queue Interval** and **Channel Interval** dashboards:

  * **Queue Interval dashboards** : Click a bar in the **SLA by Interval** tile to get historical call or chat queue metrics for that interval.

  * **Channel Interval dashboards** : Click a data point on the trend line in the **Service Level Trend** , **AHT Trend** , **Queue Time Trend** , **CSAT Trend** , or **Transfer Trend** tile to get historical call or chat queue metrics for that interval.




Fixed

The following issues were addressed in this release:

  * Fixed an issue where the **Start Time** and **End Time** filters weren't correctly applied to summary metrics on the **Agent Performance** dashboard and historical reports.

  * Fixed an issue where calls returned to queues due to agent connectivity or microphone errors didn't appear in the **Queued Calls** dashboard.

  * Fixed an issue on the **CSAT Dashboard - Calls** dashboard where the direction in the **Direction** filter couldn't be selected.

  * Fixed an issue in dashboards with a **Time Format** filter. When users selected **Seconds** in this filter, single-value tiles displayed decimals instead of whole numbers.

  * Updated the format of time duration fields in Explores from HH:MM:SS to MM:SS for durations of less than one hour. For example, `00:10:20` changed to `10:20`.

  * Fixed an issue where the **Total Failed** metric incorrectly counted a maximum of one failure per call or chat session.

  * Fixed time duration fields so that values represent the number of seconds rather than a fraction of a day.

  * Fixed an issue where the **Queue Abandon %** tile was missing from the **Abandons** dashboards.

  * Fixed an issue on the **Failed Sessions** dashboards where the **Queue Name** column of the **Historical** table and the **Queue Name** filter weren't appearing.

  * Fixed an issue where the **Time Format** filter was missing from dashboards.

  * In the **Real-time Calls** , **Real-time Chats** , **Queue Group Performance** , and **Email** dashboards, the naming of fields such as "assigned at", "created at", and "ended at" was improved in the Explores to make them clearer. For example, on the **Real-time Chats - Chats Connected** dashboard, in the **Chat Metrics (Live)** Explore, **Chat > Started At Date > Date** and **Chat > Started At Date > Month** changed to **Chat > Started At > Started At Date** and **Chat > Started At > Started At Month**.

  * Fixed an issue where the **Agent preferences** table displayed an incorrect date and timestamp.

  * Fixed an issue where the **Location** filter on the **All interactions for Chats** dashboard didn't display data in some tiles.

  * Fixed an issue where deactivated users appeared in dashboards.

  * Fixed an issue where outbound calls that weren't associated with queues appeared in the Queue Performance dashboard.

  * Fixed performance issues on the Agent Performance dashboard.

  * Fixed an issue on the Failed Interactions dashboard where the **Outbound Phone Numbers** filter didn't display any values.

  * Fixed an issue where the **Queue Interactions** metric included the short abandons count.

  * Fixed an issue on the Queue Group Performance - All dashboard where the **Locations** filter didn't display all values.




## March 10, 2026

Announcement

**Mobile SDK patch**

This patch fixes an iOS SDK issue where end-users were directed to an unresponsive support page after closing a chat session and completing the post-chat survey.

## February 25, 2026

Announcement

**Google Cloud CCaaS 4.0 patch**

This patch does the following:

  * Fixes an issue where voicemails were being routed to agents who were not assigned to the intended queue.

  * Adds the ability to disable the IVR greeting message, both at the global level and at the Direct Access Point queue level.

  * Lets an agent and an end-user join a call simultaneously.




## February 17, 2026

Announcement

**Google Cloud CCaaS 4.0**

We've released version 4.0 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Salesforce Service Cloud: new secondary lookup object**

The Salesforce Service Cloud integration can now use a secondary lookup object to identify customer records when the primary lookup object returns no results. This helps prevent the creation of duplicate records.

Administrators: When you click **Settings > Developer Settings > CRM > Salesforce > SFDC Cloud Selection > Service Cloud**, a new **Secondary Lookup Object** checkbox appears in the **Account Lookup** section.

For more information, see [Configure account lookup and field mapping](https://docs.cloud.google.com/contact-center/ccai-platform/docs/salesforce-integration-guide#configure-account-lookup).

Feature

**Raw data export: new call_participants data type**

We've added the `call_participants` data type to raw data export. This data type helps you track the following escalation details for wait-time virtual agents:

  * The amount of time the wait-time virtual agent spent in queue.

  * The number of events sent to the wait-time virtual agent while it was in queue.




For more information, see [Raw data export dictionary](https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export-dictionary).

Fixed

The following issues were addressed in this release:

  * Fixed the following issues with the standard (non-advanced reporting) dashboards:

    * The **Dashboard > Queue Reports** dashboard had broken table headers.

    * The **Dashboard > Call** dashboard was missing metrics labels in the **LOGGED IN AGENT** tile.

  * Fixed an issue where calls were mistakenly saved in MP3 format rather than WAV format in external storage.

  * Fixed an issue that occurred after an agent put an end-user on hold, transferred the call to another agent, and then left the call. When the remaining agent took the end-user off hold, the agent and the end-user couldn't hear each other.

  * Fixed an issue with NICE WFM export where queue abandoned calls were inaccurately reported to the WFM system.

  * Fixed an issue where the **Assign Human Agents** page for queues appeared blank, preventing administrators from viewing or managing agent assignments.

  * Fixed an issue where an email with a message ID longer than 255 characters failed to process and blocked the processing of other emails.

  * Fixed an issue where agents in the **In-email** status didn't receive incoming calls or chats.

  * Fixed an issue where CSAT ratings were missing from metadata files and raw data exports.

  * Fixed an issue where Salesforce integrations incorrectly created duplicate cases for a single outbound call.

  * Fixed an issue where unsupported settings, such as **Cascade Conditions** and **Wrap-up settings** , mistakenly appeared in the queue menu settings for Apple Messages for Business queues.

  * Fixed an issue where attempting to barge into a chat while monitoring it returned a `You are already in Chat` error instead of completing the action.

  * Fixed an agent desktop issue where the **New photo received** banner reappeared after viewing a photo and switching between active chat tabs.

  * Fixed an issue where Direct Access Points failed to route calls correctly for SIP URIs with spaces or non-standard formats.

  * Fixed an issue where an agent's personal contact name was mistakenly displayed as the caller ID to other agents when they received a call from the agent.

  * Fixed an issue where agents appeared as `Available` in the **Agent Activity Timeline** report after signing out.

  * Fixed an issue where Salesforce integrations created duplicate cases for a single outbound call.




## February 03, 2026

Announcement

**Advanced reporting dashboards 3.43**

We've released version 3.43 of the advanced reporting dashboards.

Feature

**Performance overview dashboard**

The performance overview dashboard now includes the following tiles:

  * **Avg Queue Time** : the average time a session (call or chat) spent in a queue until an agent accepted it or the end-user abandoned it

  * **Avg Queue Abandon Time** : the average time that sessions (calls or chats) waited in a queue before being disconnected without an agent accepting them

  * **Sentiment Score** : the average sentiment score for sessions (calls or chats)




For more information, see [Performance overview dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-perf-overview).

Feature

**Email dashboard**

The Email dashboard now includes the following table:

  * **Queue Transfers Detail** : email transfer information at the instance, queue, and session levels



For more information, see [Email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-email-performance).

Fixed

The following issues were addressed in this release:

  * Fixed an issue on the Agent Performance dashboard where the **Disconnect Status** field for chats incorrectly displayed `Unknown` or was empty.

  * Fixed an issue on the All Interactions - Calls dashboard where the **SLA%** and **SLA% by 30 Minute Interval** tiles displayed the wrong calculations.

  * Fixed an issue where the `Voice Inbound (Direct)` and `Voice Outbound (Direct)` values were missing from the **Interaction Type** filter on the following dashboards:

    * Real-time Calls - Calls Queued

    * Real-time Queue Monitoring - Calls

  * Fixed an issue where the **Call Type** field on the **Agent Productivity Detailed - Calls** table of the Agent Performance dashboard displayed `Unknown` instead of `Voice Inbound (Direct)` or `Voice Outbound (Direct)`.

  * Fixed the experience for filtering on the consumer phone number for the following dashboards:

    * All Interactions - Calls

    * Real-time Calls - Calls Connected

    * Abandons - Calls

  * Fixed an issue on the All Interactions - Calls dashboard where widgets weren't loading.

  * Fixed an issue on the Email dashboard where agent information was missing for email sessions that were started by the end-user.

  * Fixed an issue where the **Consumer Phone Number** field was missing from the following dashboards:

    * Agent Activity

    * Failed Sessions - Calls

    * Missed Interactions - Calls

    * Abandons - Calls

    * CSAT - Calls

We also renamed the **Customer ANI** field to **Consumer Phone Number**.




## February 02, 2026

Announcement

**Google Cloud CCaaS 3.44**

We've released version 3.44 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Support for French Canadian in the Google Cloud CCaaS portal**

You can now view the Google Cloud CCaaS portal in French Canadian.

**Note:** System messages and error messages aren't translated and appear in English.

Feature

**Agent desktop: dynamically control the custom panel language**

You can now use the `{AGENT_LOCATION_LANGUAGE}` or the `{AGENT_LANGUAGE}` variable in a query parameter in your custom URL to dynamically control the language for a custom panel:

  * **Agent location language** : Add the `{AGENT_LOCATION_LANGUAGE}` variable to your URL to display the custom panel in the language of the agent's assigned location.

  * **Agent language** : Add the `{AGENT_LANGUAGE}` variable to your URL to display the custom panel in the language selected by the agent in the agent desktop language selector.




For more information, see [Dynamically control the custom-panel language](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets#dynamically-control-custom-panel-language).

Feature

**Assigned agent tags**

Assigned agent tags let you see at a glance which agent is assigned to each email in an email list and which emails are unassigned. An agent assignment tag is a round tag containing an agent's initials, which indicate the agent assigned to an email.

Administrators: In the **Settings > Email > General > Email Management** section, there's a new **Enable Assigned Agent Initials on Email List View** checkbox.

For more information, see [Assigned agent tags](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-assigned-agent-tags).

Feature

**Edit email subject lines**

Agents can now modify email subject lines when replying to or forwarding email messages. This lets agents add context to the subject line, such as ticket numbers or case details. The system maintains the session ID and keeps the conversation thread intact.

Administrators: In the **Settings > Email > General > Email Management** section, there's a new **Enable Subject Line Editing** checkbox.

For more information, see [Let agents edit the subject lines in emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#let-agents-edit-subject-lines).

Feature

**Send DTMF tones in the agent adapter using the keyboard**

An agent can now use their keyboard to type or paste alphanumeric strings directly into the call adapter to play DTMF tones, with the appropriate pauses. This capability eliminates the need to click number buttons on a virtual keypad. This streamlines data entry during IVR, web, and mobile calls and improves accessibility.

User experience change: The **Dial** button on the call adapter has been renamed **Keypad**.

For more information, see [In-call interface](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-in-call).

Feature

**New @{END_USER_NUMBER} variable**

You can use the new `@{END_USER_NUMBER}` variable to read out the end-user's phone number in a message to leave a voicemail or request a callback. Reading out the end-user's phone number helps them confirm whether they want to use it or a different number. To use this capability, add the `@{END_USER_NUMBER}` variable to the **Callback - Request Phone Number** and **Voicemail - Request Phone Number** text-to-speech message fields. You can configure this at the global or queue level.

For more information, see [Read out a phone number in a voicemail or callback message](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#read-out-phone-number).

Feature

**Disable multicast for call routing**

You can now disable multicast to ensure that the system offers calls to only one agent at a time through deltacast. When you disable multicast, the system uses only deltacast attempts to find an agent. If no agent accepts the deltacast, the call isn't multicasted to all available agents. Instead, it follows your logic for cascade groups or overcapacity deflection. All other deltacast rules, such as maximum queue time, remain in effect.

Administrators: The new **Disable Multicast fallback after all Deltacast attempts** checkbox appears in the following places:

  * **Settings > Operation Management > Routing > Call Routing**

  * **Settings > Operation Management > Routing > Chat Routing**

  * **Settings > Queue > IVR** or **Mobile** or **Web > Edit / View > `QUEUE_NAME` > Routing > Configure > Call Routing**

  * **Settings > Queue > IVR** or **Mobile** or **Web > Edit / View > `QUEUE_NAME` > Routing > Configure > Chat Routing**




For more information, see [Turn on deltacast for calls globally](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#turn-on-deltacast-for-calls-globally) and [Turn on deltacast for calls at the queue level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/multicast_deltacast#turn-on-deltacast-for-calls-at-the-queue-level).

Feature

**Improvements to end-user to agent calling**

The following improvements are available for end-user to agent calling:

  * You can control whether end-users can input an agent's extension number at the beginning of a call.

  * You can add a message at the beginning of a call prompting the end-user to enter an extension number.

  * End-users can input an agent's extension number in the extension directory.




Administrators:

  * A new **Extension Input Settings** section appears in the **Settings > Call > Agent Extensions > Consumer to Agent Calls** section.

  * New and updated messages appear in the **Settings > Languages & Messages > Audible Messages > Extension Directory Messages** section.




For more information, see [End-user to agent calling](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#end-user-to-agent-calling).

Feature

**Improvements to deflection message management**

Agents can now upload message files from the call adapter to use for message and voicemail greetings. These files support after-hours deflection, overcapacity deflection, and automatic redirection.

A new **Upload audio recording** option appears in the call adapter in the following locations:

  * **Options > Agent Deflections > After hours deflection**

  * **Options > Agent Deflections > Overcapacity deflection**

  * **Options > Agent Deflections > Automatic redirections**




If you make changes to an agent's after-hours deflection settings, overcapacity deflection settings, or automatic redirection settings, you can now revert to the settings that the agent selected in the call adapter. The **Revert to agent settings** button appears in the **Agent Call Deflections** section on the agent's **Edit User** page. To access the agent's **Edit User** page, go to the **Settings > Users & Teams** page.

For more information, see [Configure deflections at the agent level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure-deflections-at-agent-level) and [Set deflections for extension calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-extensions-guide#set-deflections-for-internal-calls).

Feature

**Apps API: new end_user.phone parameter**

The apps API accepts an optional `end_user.phone` parameter during chat creation. This parameter enables CRM lookup using the end-user's phone number, which lets the chat adapter display the end-user's name.

For more information, see [Create chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-platform-api-endpoints#create-chat).

Feature

**Apps API: new endpoint for adding a third party to a call**

The apps API now includes an endpoint (`/calls/add/CALL_ID/dial`) to add a third party to an ongoing call. When you make a request to this endpoint, the system automatically dials the third-party's phone number, and the agent's call adapter displays the **Calling** screen.

For more information, see [Add a third party to a call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-add-third-party-to-call).

Feature

**Custom data-collection forms for chats are available in the web SDK**

Your human agents and virtual agents can now send custom data-collection forms to end-users using the web SDK.

Administrators: The **Web chat** checkbox appears at **Settings > Forms > Add template > Custom form**.

For more information, see [Add a custom form](https://docs.cloud.google.com/contact-center/ccai-platform/docs/data-collection-forms#add-custom-form).

Fixed

The following issues were addressed in this release:

  * Fixed an issue where calls were incorrectly deflected to voicemail during scheduled holidays instead of connecting to the virtual agent.

  * Fixed an issue where the `queue_id` value passed to post-session virtual agents was incorrect during complex transfer flows, such as human-agent to virtual-agent to human-agent transfers.

  * Fixed an Agent Assist issue where the autogenerated session summary didn't include the conversation context from the virtual agent segment after a transfer to a human agent.

  * Fixed an issue where the virtual agent incorrectly terminated a chat session immediately after escalating it to a human agent.

  * Fixed an issue causing inaccurate reporting for chats escalated from a virtual agent to a human agent. The system failed to record the initial virtual agent to human agent escalation in the transfer history and used an incorrect originating queue for subsequent transfers.

  * Fixed an issue where source links were missing from knowledge assist answers in the agent adapter during calls.

  * Fixed an issue affecting Telnyx users where selecting **Stop Monitoring** didn't fully terminate monitoring sessions.

  * Fixed an issue where call transcript and session summary files saved to external storage had incorrect filenames. The variables in the filenames, such as `{{date}}` and `{{session_start_time}}`, didn't resolve correctly.

  * Fixed an issue for Salesforce users where cases were not generated during calls, even when the **Always use the admin user for all record creations/updates** checkbox was selected.

  * Fixed an issue where photos received via blended SMS didn't display in the agent adapter.

  * Fixed an issue that caused errors when creating CRM records for abandoned calls in multi-language queues.

  * Fixed an issue where CRM skip options (for example, skipping CRM account creation or lookup) didn't correctly reset when switching between different CRM integrations.

  * Fixed an issue for Salesforce users where the dialpad appeared during click-to-dial.

  * Fixed an issue where the `callParticipantFinished` event didn't emit when an agent performed a cold transfer.

  * Fixed an issue where WhatsApp messages received after business hours were mishandled. The system queued messages to agents instead of sending after-hours messages and ending the sessions.

  * Fixed an issue where the status timer in the chat adapter displayed incorrect elapsed times.

  * Fixed an issue where the agent desktop displayed agent statuses that were inconsistent with the standalone agent adapter.

  * Fixed an issue that caused 503 and 431 errors.

  * Fixed an issue in the chat adapter where the `agent_joined_chat` event specified the wrong chat ID when the agent was handling multiple chats.

  * Fixed an issue where the chat adapter incorrectly labeled SMS message events as chat inbound messages when agents sent SMS chat messages.

  * Fixed an issue where newly created instances didn't create a global contact list, preventing the initial custom contact list from appearing.

  * Fixed an issue where attempting to copy a queue from the IVR channel to the SMS channel returned an error.

  * Fixed an issue where the menu language selected in **Settings > Call > Fallback IVR Navigation** reverted to English.

  * Fixed an issue where CRM records were created for outbound calls that ended with a `Connection Declined` status, despite the **Create CRM records for abandoned calls** checkbox being cleared.

  * Fixed an issue where the **Agents** dashboard filter incorrectly displayed agents in both parent and child queues.

  * Fixed an issue where notification rules based on average wait time didn't trigger alerts or send emails.

  * Improved the French Canadian translations for several default agent statuses. The changes include the following:

    * "Appel entrant" is now "Appel en cours."

    * "Dans la discussion" is now "Clavardage en cours."

    * "Synthèse" is now "Conclusion."

    * "Synthèse prolongée" is now "Temps de conclusion dépassé."

  * Fixed an issue where the **Agents** dashboard stopped refreshing, causing agent statuses to appear outdated or incorrect.

  * Fixed an issue where the agent directory appeared empty when an agent attempted to start an internal call transfer, preventing the agent from seeing available teammates.

  * Fixed a web SDK issue where the `Content-Encoding` response header was missing for the widget.




## December 26, 2025

Announcement

**Google Cloud CCaaS 3.42.121 and 3.43.153 patches**

These patches fix a security vulnerability that could expose customers' Personally Identifiable Information (PII). There is no change to the agent experience.

## December 23, 2025

Announcement

**Web SDK version 2 will be shut down on June 26, 2026**

On June 26, 2025, we announced the launch of [Web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025). Starting on **June 26, 2026** , the web SDK v2 will no longer function. Be sure to [update your website](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

## December 16, 2025

Announcement

**Google Cloud CCaaS 3.43.144 patch**

This patch does the following:

  * Fixes an issue where chats routed using Deltacast didn't auto answer.

  * Fixes an issue where virtual agents weren't playing a welcome message when connected to a caller.

  * Fixes an issue that occurred when an agent put a caller on hold and then transferred the call to a different agent. When the call was transferred, the caller was taken off hold, but the agent adapter mistakenly indicated that the caller was still on hold.

  * Fixes an issue where the transfer restriction settings in a queue sometimes disappeared.




## December 09, 2025

Announcement

**Mobile SDK version 2.15.1 patch**

This patch adds the following updates to the Android SDK:

  * **Android 16 compatibility** : Mobile SDK 2.15.1 is compatible with Android 16.

  * **Edge-to-edge screen support** : Mobile SDK 2.15.1 supports edge-to-edge.

  * **No predictive back system animations** : Mobile SDK 2.15.1 doesn't support predictive back system animations. We expect to support this Android 16 capability in a future release.




## December 06, 2025

Announcement

**Google Cloud CCaaS 3.43**

We've released version 3.43 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Cloud Logging for Google Cloud CCaaS is Generally Available**

You can use Cloud Logging to capture logging data and events for your Google Cloud project. The Logs Explorer displays log entries for your project. You can use the `contactcenteraiplatform.googleapis.com/ContactCenter` resource type to filter your results to view only the log entries for Google Cloud CCaaS. For more information, see [View log entries](https://docs.cloud.google.com/contact-center/ccai-platform/docs/view-log-entries).

Feature

**Wait-time virtual agent for calls**

You can now configure a virtual agent to handle incoming calls requiring escalation to a human agent. The wait-time virtual agent can place an incoming call into a queue and then provide personalized, interactive updates based on real-time events that your instance sends to the virtual agent. These events include estimated wait time, queue position, and agent availability. When an agent is available, the virtual agent transfers the call. For more information, see [Wait-time virtual agents for calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/wait-time-va-calls).

Feature

**New web SDK event: exited**

We've added the `exited` event to the web SDK. This event triggers when an end-user exits a chat session after an agent ends the session. For more information, see [exited](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-api-reference#exited).

Fixed

We addressed the following issues in this release:

  * Fixed an issue that occurred when a call was connected directly to an agent using the agent's extension (either from another agent or from an end-user). The system didn't apply the settings of the receiving agent's queue.

  * Fixed a web SDK issue where responses from virtual agents displayed markup code for headings, bold, italics, etc., instead of the rendered formatting.

  * Fixed a web SDK issue where the timeout dialog for chat check-in didn't dismiss after a chat session expired.

  * Fixed a web SDK issue where an error was incorrectly returned in the browser console log.

  * Fixed a web SDK issue where the "new message" alert in the chat screen used a text color that didn't adequately contrast with the background.

  * Fixed an issue where red boxes incorrectly appeared in the chat screen when an agent's message was undelivered.

  * Fixed an issue where inbound calls were routed incorrectly to agents outside of their personal hours of operation.

  * Fixed an issue that prevented users from downloading web chat transcripts using the **Download** button.

  * Fixed an issue that occurred during overcapacity deflection. The "redirect to queue" action didn't route calls to the configured Dialogflow menu ID.

  * Fixed an issue where virtual agents disconnected calls during after-hours deflection or automatic redirection instead of routing them to the configured location.

  * Fixed an issue where virtual agents incorrectly remained in a session if an agent answered a call immediately after an overcapacity deflection announcement.

  * Fixed an issue where calls didn't end after an end-user selected the "message" option during overcapacity deflection.

  * Fixed an issue where manually adding users to multiple teams returned an error.

  * Fixed an issue where administrators couldn't save queue reordering actions in the SMS channel.

  * Fixed an issue where the BYOC configuration incorrectly overwrote the domain of target SIP URIs during outbound calls.

  * Fixed an issue that incorrectly returned `Cannot read properties` console errors.

  * Fixed an issue where a service name was misspelled, which caused errors in batch user creation and team assignment.

  * Fixed an issue with historical data bulk import where uploading historical data without dates generated empty import reports instead of returning an error.

  * Fixed an issue with historical data bulk import where the system accepted and processed data with future dates instead of returning an error.

  * Fixed an issue where queue priority sliders for users and teams were active when they were configured to be inactive.

  * Fixed an issue that prevented languages from being added to an instance.

  * Fixed an issue where the agent directory was empty when an agent attempted to transfer a call to another agent.

  * Addressed latency in Telnyx calls.

  * Fixed a billing calculation issue where concurrent agent counts were inaccurate.

  * Fixed an agent desktop issue where, when auto answer was enabled, incoming chats mistakenly took focus from active chats that agents were engaged with.




## December 03, 2025

Announcement

**Google Cloud CCaaS patch 3.42.113**

We've released patch 3.42.113 for Google Cloud CCaaS. This patch does the following:

  * Fixes an issue where calls were not routed to available agents.

  * Reverts a fix for inaccurate reporting for chats escalated by a virtual agent to a human agent. This fix caused a regression.




## December 02, 2025

Announcement

**Mobile SDKs version 2.15.0**

We've released version 2.15.0 of the mobile SDKs.

Feature

**Turn off push notifications at the global level**

You can configure your Android SDK or iOS SDK to turn off push notifications at the global level. This bypasses all push notification dependencies and prevents push notifications from reaching end-users. For more information, see the following:

  * **Android SDK** : [SDK configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#sdk-configuration)

  * **iOS SDK** : [Turn off push notifications at the global level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#turn-off-push-notifications-at-global-level)




Fixed

We addressed the following iOS SDK issues in this release:

  * Fixed an issue where the **RATE YOUR EXPERIENCE** dialog contained text that didn't adequately contrast with the background.

  * Fixed an issue where smart action requests from an agent (for example, request verification or request photo) triggered push notifications to the end-user despite **Allow Push Notifications** being turned off in the end-user's app.

  * Fixed an issue in the end-user's chat screen where the screen reader incorrectly announced that the "We are connecting you, please hold" message was a button.




## November 19, 2025

Announcement

**Google Cloud CCaaS 3.42**

We've released version 3.42 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Alvaria Advanced List Management integration with outbound dialer**

You can now integrate Alvaria Advanced List Management (ALM) with the outbound dialer. This lets you combine Alvaria's list and campaign management capabilities with the dialing capability of Google Cloud CCaaS. This integration exchanges contact and result files through a shared Cloud Storage bucket.

Capabilities:

  * Multi-tenancy support: helps ensure that each tenant's data remains separate and secure

  * Flexible delimiter support: supports files using comma, pipe, tab, or semicolon delimiters




For more information, see [Alvaria Advanced List Management integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/alvaria-alm).

Feature

**New standalone queue settings page**

Google Cloud CCaaS now includes a standalone **Queue Menu Settings** page for each queue in your instance. These pages are separate from (but identical to) the **Queue Menu Settings** pages at **Settings > Queue > Edit / View > YOUR_QUEUE**. The standalone pages load faster and you can quickly access them in the following ways:

  * From the **Queues** page (access this by clicking the **Queues** menu). Links to the standalone **Queue Menu Settings** pages are in the **Queue Name** column.

  * From the **Phone Number Management** pane at **Settings > Call > Phone Numbers > Phone number management**. Links to the **Queue Menu Settings** pages are in the **Assigned Queues / Agents** column.

  * Using a URL that identifies the queue. Example: `https://YOUR_CCAAS_HOST/queues/QUEUE_ID/LANGUAGE_CODE`




Links to standalone **Queue Menu Settings** pages are active only for users with permissions to view queue settings. For more information, see [Access queue menu settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/access-queue-menu-settings).

Feature

**Restrict the transfer of email sessions to a queue**

You can now configure queues to prevent them from receiving email session transfers.

Administrators: A new **Allow incoming Email Transfers** toggle appears in the settings pane at **Settings > Queue > Email > Edit / View > YOUR_QUEUE**.

For more information, see [Transfer email sessions to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue).

Feature

**Email signatures**

You can now define standardized signatures for all outgoing emails sent from a specific queue.

Administrators: A new **Email Signatures** section appears in the settings pane at **Settings > Queue > Email > Edit / View > YOUR_QUEUE**.

For more information, see [Email signatures](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#email-signatures).

Feature

**Dial pad improvements**

The dial pad in the agent adapter now includes the following:

  * Country code selector

  * Outbound number, Language, and Queue selectors




If you use a CRM with flexible outbound dialing turned on, the **Outbound number** and **Language** selectors appear in the **Outbound call details** screen.

For more information, see [Make an outbound call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-calls#make-outbound-call).

Feature

**Click-to-call: show the dial pad screen**

If you have a CRM configured for click-to-call, you can configure your instance to display the dial pad screen after an agent clicks a phone number in the CRM but before a call starts. This lets the agent make changes on the dial pad screen. For more information, see [Click-to-call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#click-to-call).

Feature

**Virtual agent aliases**

You can assign a public-facing alias to each of your virtual agents. When all of your virtual agents have the same alias, they each appear to have the same name to end-users. This gives the impression that a single virtual agent is handling a session even if the session is transferred between virtual agents. You can assign virtual agent aliases to both support agents and virtual task assistants. Virtual agent aliases are used in the web SDK, the mobile SDKs, in system messages, and in transcripts.

Administrators: A new **Virtual Agent Alias** checkbox appears in the following dialogs:

  * The **Add a Customer Support Agent** dialog at **Settings > Virtual Agent > Virtual Agents > Add virtual agent > Customer Support**

  * The **Add a Virtual Task Assistant** dialog at **Settings > Virtual Agent > Virtual Agents > Add virtual agent > Task Assistant**




For more information, see [Virtual agent aliases](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-va-aliases).

Feature

**Sensitive data redaction**

You can now automatically identify and redact sensitive data from chat conversations, both in real time and in transcripts. This helps to prevent unauthorized people from accessing sensitive information and can help you comply with security standards. You can configure redaction for incoming messages from end-users, outgoing messages from agents, and session notes. You can also let agents temporarily view redacted messages during a session. This capability is available for the web SDK.

Administrators: You can find the settings for configuring automatic redaction in the following locations:

  * To add a redaction platform: **Settings > Developer Settings > Redaction Platform**

  * To configure automatic redaction at the global level: **Settings > Chat > Automatic Redaction**

  * To configure automatic redaction at the queue level: **Settings > Queue > Web > Edit / View > SELECT_QUEUE > Automatic Redaction**




For more information, see [Sensitive data redaction](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sensitive-data-redaction#sensitive-data-redaction).

Feature

**New chat platform API endpoint for getting media files**

You can use the new chat platform API endpoint to get the media file that an agent sends to an end-user during a chat session. Your custom chat application can then make the media file available to the end-user during the session.

New endpoint: `/apps/api/v1/chats/CHAT_ID/media/MEDIA_ID`

For more information, see [Agent file attachments with the chat platform API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-attachments-chat-api).

Feature

**Virtual task assistant support in the chat platform API**

The chat platform API now provides improved support for virtual task assistants. When an agent transfers a chat to a virtual task assistant, your application can send and receive messages from the virtual task assistant. Enhanced webhooks provide the virtual task assistant's message content instantly, streamlining private, automated workflows like collecting sensitive information.

For more information, see [Use virtual task assistants with the chat API platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/task-va-chat-api).

Feature

**Chat check-in**

Users of the web SDK can use chat check-in to help ensure that end-users are present and ready to engage before connecting them to a human agent. This helps to reduce the time lost when agents wait for end-users who have abandoned a chat.

When an end-user reaches the front of the chat queue, the system asks if they're still available. If there's no response after the amount of time you configure, the system removes the end-user from the queue. If the end-user rejoins the queue, you can configure whether they rejoin at the front or the back of the queue.

For more information, see [Chat check-in](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-check-in#chat-check-in).

Fixed

We addressed the following issues in this release:

  * Fixed an issue where Agent Assist generated incomplete or inaccurate chat summaries.

  * ~~Fixed inaccurate reporting for chats escalated by a virtual agent to a human agent.~~

  * Fixed incorrect labeling and routing of French voicemails to the English-language queue in the agent adapter.

  * Fixed the missed response timer, which added an extra 30 minutes to the calculated time.

  * Fixed a significant slowdown in background job processing.

  * Fixed an issue where the global default voicemail greeting failed to save when applied to an individual user's settings.

  * Fixed an issue that caused agents to be assigned a call and a chat at the same time, even when this was disabled in the settings.

  * Fixed an issue that prevented users from testing Android push notifications.

  * Fixed an issue where editing a phone number's settings on the **Phone Number Management** page removed it from queues where it was assigned for outbound calls.

  * Fixed an issue that caused a **Custom roles permissions is invalid** error when attempting to save a change to the **Audit Dashboard** permission in a custom role.

  * Fixed an issue that caused the handle time for queued chats to display an incorrect value, particularly after a session transfer.

  * Fixed an issue where the call ID was missing in the **Activity Timeline** report.

  * Fixed an issue where the **Auto answered** label on a chat tab in the chat adapter persisted even after an agent opened the chat.

  * Fixed an issue where the agent directory in the call adapter appeared empty when an agent attempted to transfer a call.

  * Fixed an issue that prevented an agent from adding another agent to a call using their extension number.

  * Fixed an agent desktop issue where unsigned data appeared before signed data in the **Session Data Feed** panel. This was inconsistent with the display order in the agent adapter.

  * Fixed an issue at **Settings > Developer Settings > CRM > Custom CRM > CRM lookup method > Custom Link**. In the **Custom link CRM lookup** section, we replaced the incorrect `{Custom UID}` variable name with `{CUID}` in the UI text.

  * Fixed a web SDK issue where the **Select an option** channel selection screen appeared unnecessarily when a chat started, when the Direct Action Parameter was enabled.

  * Improved web SDK page loading speed.

  * Fixed a web SDK issue where external deflection links weren't working correctly.




## November 17, 2025

Announcement

**Advanced reporting dashboards version 3.41**

We've released version 3.41 of the advanced reporting dashboards.

Feature

**Campaigns dashboard**

We've added a new **Campaigns** dashboard that displays real-time and historical performance metrics for call campaigns, including call outcomes, campaign volumes, and agent metrics. Managers can use this information to monitor call campaigns and make data-driven decisions to improve campaign performance. For more information, see [Campaigns dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-campaigns).

Feature

**Real-time dashboard optimization**

We've optimized real-time dashboards to provide faster loading and refresh times.

Feature

**All Interactions dashboards: updates to tables**

On the **All Interactions - Calls** dashboard, we did the following:

  * Renamed the **All Call Interactions (Historical)** table to **Call Metrics Detail**.
  * Updated the formatting of the column headings in the **Virtual Agent Interactions** table.



On the **All Interactions - Chats** dashboard, we renamed the **All Chat Interactions (Historical)** table to **Chat Metric Detail**.

For more information, see [All interactions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions).

Fixed

We addressed the following issues in this release:

  * Fixed an issue where the **Chat Agent Metrics (Historical)** explore and the **Agent Metrics (Historical)** explore returned different data for chats handled. This resulted in inconsistent chat handling metrics in dashboards.
  * Fixed an issue where ambiguous metrics names appeared in the **Call Queue Metrics (Historical)** explore.
  * Fixed an issue where the average active concurrency metric appeared as a total instead of a percentage.
  * Fixed an issue where the CSAT values on the **CSAT** and **Agent Performance** dashboards were not consistent with each other.
  * Changed the **Caller ANI** table heading to **Consumer phone number** in all of the tables it appeared in.
  * Fixed an issue where Call ID on the **Calls Transfer** dashboard was not correctly formatted.
  * Fixed an issue where the column headings in the **Agent Productivity** table of the **Agent Performance** dashboard were ordered incorrectly.
  * Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Codes** filter wasn't working correctly.
  * Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Code** filter was unable to find existing disposition codes.
  * Fixed an issue on the **Dispositions - Chat** dashboard where the **Direction** filter didn't display the available values.
  * Fixed an issue on the **Dispositions - Chat** dashboard where the **Agent Name** filter wasn't working correctly.
  * Fixed an issue on the **Dispositions - Chat** dashboard where the **Disposition Distribution** tile displayed the disposition codes in the wrong order.
  * Fixed an issue on the **Dispositions - Calls** dashboard where the **Disposition Code** filter didn't find existing disposition lists.
  * Fixed an issue on the **Dispositions - Calls** dashboard where agents didn't appear in the **Dispositions by Agent** table when filtering by Agent ID.
  * Fixed an issue where dismissed chat time was being included with current chat time metrics on the **Agent Monitoring** dashboard.



## November 03, 2025

Feature

**Google Cloud CCaaS 3.41**

We've released version 3.41 of Google Cloud CCaaS.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Transfer an email session to a queue**

Agents can now transfer an email session to a queue. This resolves the problem of multiple email sessions being created when an agent forwards an email directly to an agent to transfer it.

Administrators: The **General** pane on the **Email** page at **Settings > Email** contains a new **Enable Email Transfer Between Queues** checkbox.

User experience change: In the email adapter, a new **Transfer** button appears when an agent views an assigned email.

For more information, see [Let agents transfer email sessions to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue).

Feature

**Skip language selection and IVR menu readout**

You can configure your call flow to skip language selection and the IVR menu readout. Instead, callers get the default language and are routed to the default queue. This creates a faster call connection experience for end-users.

Administrators:

  * In the **Settings > Languages & Messages > Languages** pane, there's a new **Skip language selection** option.

  * In the **Settings > Queue > IVR (Interactive Voice Response) > IVR Queue Menu Readout** section, there's a new **Skip IVR Menu readout** option.




For more information, see [Configure IVR messages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-ivr-messages#configure-ivr-messages).

Feature

**Extensions for support numbers**

You can assign a phone number extension to an agent that an end-user can use to directly call the agent. You can also set up an extension directory that end-users can use to find the extension for an agent that they want to call.

Administrators:

  * The **Agent Extensions** pane on the **Call** page at **Settings > Call** contains a new **Consumer to Agent Calls** section.

  * The **Add new menu** dialog at **Settings > Queue > IVR (Interactive Voice Response) > Menu Structure** contains a new **Extension Directory** toggle.




For more information, see [Turn on and configure agent extensions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#turn-on-and-configure-agent-extensions).

Feature

**Virtual agent to virtual agent direct chat transfers**

You can configure Dialogflow payloads to transfer chat sessions from one virtual agent directly to another virtual agent, using the destination virtual agent's agent ID.

For more information, see [Virtual agent to virtual agent direct transfer ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers#va-to-va-direct-transfer).

Feature

**Nested disposition lists**

You can now organize your disposition lists by grouping them into nested folders, making it easier for agents to find the disposition codes they need. This is available in the agent adapter and the agent desktop.

Administrators: The **Disposition Codes** dialog at **Settings > Operation Management > Wrap-up > Manage Disposition Codes** has a new **Tree** tab.

User experience change: If you've configured nested disposition lists, the **Disposition** screen in the agent adapter displays links to the nested disposition lists.

For more information, see [Configure nested disposition lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-lists-configure).

Fixed

We addressed the following issues in this release:

  * Fixed an issue where hyperlinks in the after-hours message of the web SDK were broken.
  * Fixed an issue where the language selector mistakenly appeared in the chat UI.
  * Fixed an issue where an authentication request with an invalid or expired authentication token caused an agent's browser to become unresponsive and crash.
  * Fixed an issue where an end-user using the iOS mobile SDK couldn't play a video that they had sent to an agent during a web chat session.
  * Fixed an issue for Android mobile SDK users where the **Send** icon in the end-user's chat input field didn't appear correctly.
  * Fixed an issue where an instance using an Agent Assist profile with Conversation Summarization disabled incorrectly returned errors.
  * Fixed an issue that caused inaccurate virtual agent chat analytics. Affected metrics included `response_count`, `response_time_total`, `response_time_avg`, and `response_time_max`.
  * Fixed an issue for Microsoft Windows users where the scroll down button in the web chat pane wasn't working correctly.
  * Fixed an issue that occurred after an administrator deactivated the chat channel or the email channel. Instead of sending a single notification email for this change, the system was sending multiple notification emails.
  * Fixed a reporting discrepancy between the **Agent Metrics (Historical)** explore and the **Chat Agent Metrics (Historical)** explore in the advanced reporting dashboards.
  * Fixed an issue in the **Operation Management > Virtual Agent** settings pane. After configuring the virtual agent to assign records to a specific user, subsequent changes to other settings couldn't be saved.
  * Fixed an issue where the `sub_status` property was missing from the session metadata file.
  * Fixed an issue for HubSpot users where the inbound phone number in the call adapter displayed as **null null**.
  * Fixed an issue for Kustomer users that caused calls to be disconnected and the agent to be moved to `Unavailable` status.
  * Fixed an issue where the target response time timer in the chat adapter was resetting when the end-user sent a message instead of when the agent sent a message.
  * ~~Fixed an issue that occurred when agents used the chat adapter to send email addresses containing underscores. The email addresses resolved incorrectly in the end-user's chat pane, breaking the links.~~
  * Fixed an issue that caused inaccurate chat analytics. Affected metrics included `response_time_total`, `response_time_avg`, and `chat_duration`.
  * Fixed an issue where the queue-level overcapacity callback limit was ignored, and the global setting was enforced instead.
  * Fixed an issue for Kustomer users where the ticket for an outbound call incorrectly showed the recipient's number in the **From** field and left the **To** field blank.
  * Fixed an issue where the agent adapter froze when an agent making an outbound call changed the outbound call number using their favorites list.
  * Fixed an issue that prevented a new chat from appearing in the agent desktop. This occurred when an agent had both the agent desktop and the standard chat adapter open in separate browser tabs.
  * Fixed an issue that caused a significant delay in displaying contact detail information in the call adapter for campaign calls.
  * Fixed an issue where users with read-only roles were able to change settings on the developer settings page.



## October 31, 2025

Announcement

**Google Cloud CCaaS 3.40**

We've released version 3.40 of Google Cloud CCaaS, including the web SDK.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Agent desktop maintains state after refresh**

While you're using the agent desktop, if you refresh your browser, the agent desktop now maintains its state. This means that active conversations, finished tabs, and recently closed sessions remain as they were before the refresh.

Feature

**Web SDK: Support for hiding the download transcript option**

You can now configure the web SDK to do the following on the end-user's chat screen:

  * [Hide the command to download a transcript during a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-command-to-download-transcript-during-session).

  * [Hide the button to download a transcript at the end of a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-button-to-download-transcript-at-end-of-session).




Feature

**New variables for custom lookup URLs**

We've added the following five variables for custom lookup URLs:

  * **CUSTOMER_PHONE_NUMBER** : the end-user's phone number
  * **SUPPORT_PHONE_NUMBER** : your call center's phone number that an end-user calls in on
  * **OUTBOUND_NUMBER** : the phone number an agent uses when making an outbound call
  * **SESSION_ID** : the session ID
  * **CUSTOM_AGENT_ID** : an optional agent ID



For more information, see [Custom lookup URL configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#custom_lookup_url_configuration).

Feature

**Customize the color of the Start Screen Share button**

You can now control the color of the **Start Screen Share** button to match the color palette of your brand. For more information, see [Customize the Start Screen Share button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/cobrowse#customize-start-screen-share-button).

Feature

**The europe-west4 and europe-west6 regions are available for Agent Assist conversation profiles**

The `europe-west4` and `europe-west6` regions are now available when you create an Agent Assist conversation profile for a Dialogflow CX virtual agent. For more information, see [Create conversation profile for Dialogflow CX virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-a-dialogflow-agent#create-cp).

Feature

**Search in email channel by email address and name**

Agents can now search for email sessions by email address and name in the email adapter.

User experience change: The search pane in the email adapter includes two new fields: **Email Address** and **Name**.

For more information, see [Search for emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#search-for-emails).

Feature

**Web SDK: Support for hiding the Start a new conversation button**

You can now configure the web SDK to hide the **Start a new conversation** button on the end-user's chat screen after the session ends. For more information, see [Hide the button to download a transcript at the end of a session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started#hide-start-new-conversation-button).

Fixed

The following issues were addressed in this release:

  * Fixed an issue that prevented administrators from configuring virtual agents on the top level for IVR queues.

  * Fixed an issue where attempting to configure automatic redirection settings for the top level of an IVR queue returned an error.

  * Fixed in issue that caused incorrect agent monitoring and reporting data when a virtual agent escalated a call to a queue in a different language.

  * Fixed issue for HubSpot users where the call adapter got stuck on a non-functional reconnect page after a session expired.

  * Fixed an issue for HubSpot users where the **Delay call record creation until the call is connected to agent** checkbox didn't appear in the **CRM Record Creation Details** pane.

  * Fixed an issue that prevented agents from ending direct SMS chat sessions.

  * Fixed an issue for Microsoft Windows 11 users that prevented agents from entering Japanese characters in the chat screen during chat sessions and into the notes during wrap-up.

  * Fixed an issue where SDK custom data that was passed using the web SDK didn't appear in the agent adapter.

  * Fixed an issue that prevented custom links entered in the chat adapter from being converted into clickable links.

  * Fixed an issue in the chat screen of the chat adapter where the **Missed target response time** message was partially obscured by the formatting toolbar.

  * Fixed an issue where agents couldn't initiate a callback to a missed agent-to-agent call from the **History** tab of the agent adapter.

  * Fixed an issue where predictive outbound calling campaigns stalled and incorrectly moved contacts to the **Redialed** list before retrying them. This prevented the campaigns from completing successfully.

  * Fixed an issue in the **Call Details** pane where the **Recording Message Sequence** settings were incorrectly inactive when the **Play Call Recording Messages** checkboxes were cleared.

Administrators: In the **Call Details** pane, we changed **Recording Message Sequence** to **Recording Message Sequence for Outbound Calls** for clarity.

  * Fixed an issue where the customized greeting for an automatic redirection rule didn't play for calls that entered the queue using a Direct Access Phone (DAP) number.

  * Fixed an issue that occurred when a call was made from the global contact list. On the **Details** tab of the call adapter, the destination name didn't display. Instead, the destination phone number displayed.

  * Fixed an agent desktop issue where an agent status that was configured with a role restriction mistakenly appeared in the status list for a user assigned to that restricted role.

  * Fixed an issue where searching for an inbound-only queue on the **Phone Number Management** page failed to return a result.

  * Fixed an issue that caused queue duration and wait duration to be reported as `0`. This occurred when the **Call Service Level Target** on a queue settings page was set to a number that exceeded the maximum allowed limit.

  * Fixed an issue where a team assigned to a preference profile added only 1 user to the profile's users count, instead of adding the total number of users on the team.

  * Fixed an issue where agents were timed out for inactivity while composing an email in the email adapter.

  * Fixed an issue where users with a custom role were unable to save changes in the **Chat Settings** pane, even when their role had **View** and **Edit** permissions.

  * Fixed an issue that occurred after an agent configured their own hours of operation settings in the agent adapter. Those settings didn't appear for administrators in the agent's user profile on the **Settings > Users & Team > Manage Users & Teams** page. This prevented the administrator from making other edits to the agent's profile without overwriting the agent's hours of operation settings.

  * Fixed an issue where CRM tickets weren't created for some calls.

  * Fixed an issue where outbound SIP calls incorrectly appended data parameters, causing calls to fail.

  * Fixed a Web SDK security vulnerability associated with DOMPurify.

  * Fixed an issue where chat metadata wasn't saved to external storage. This occurred when an end-user ended a chat after escalating from a virtual agent but before being connected to a human agent.




## October 30, 2025

Announcement

**Advanced reporting dashboards version 3.40**

We've released version 3.40 of the advanced reporting dashboards.

Feature

**New Agent Preference table in the Agent Availability dashboard**

We've added a new **Agent Preference** table to the **Agent Availability** dashboard. This table can help you ensure that queues have properly skilled agents assigned to them. It can also help identify agents who improperly change their availability filters. For more information, see [Agent availability dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-availability).

Feature

**New Audit Log dashboard**

We've added a new **Audit log** dashboard to help you track changes to the configuration of your instance. The dashboard tracks changes to the settings on the **Developer Settings** page, and displays information such as the type of change, who made the change, and when. This dashboard is similar in format to the advanced reporting dashboards, but you can't save it as a new dashboard. You access the **Audit Log** dashboard from the **Settings** menu. For more information, see [Audit log dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-audit-log).

Fixed

We addressed the following issues in this release:

  * Fixed an issue where the queue groups dashboard failed to display data for users with a custom role assigned to a queue or queue group.

  * Fixed an issue that caused the **Agent Activity Timeline** dashboard to display inaccurate or incomplete data.

  * Fixed an issue on the **Virtual Agent - Calls** dashboard where the **Virtual Agent Name** and **Queue** filters didn't display available values.

  * Fixed an issue on the **Dispositions - Chats** dashboard that prevented the **Agent Email** , **Agent ID** , and **Location** filters from displaying available values.

  * Fixed an issue on the **Virtual Agent - Chats** dashboard that prevented the **Virtual Agent Name** filter from displaying available values.

  * Fixed an issue on the **Virtual Agent - Chats** dashboard where the **Date** filter was incorrectly labeled **Time Range**.

  * Fixed an issue on the **Abandons - Calls** dashboard where **Customer ANI** values weren't appearing in the **Queue Abandon Details** and **IVR Abandon Details** tables despite the customer signing the waiver.

  * Fixed an issue on the **Agent Activity Timeline** dashboard where the **Agent Name** filter wasn't working properly.




## October 15, 2025

Announcement

**Mobile SDK patch 2.14.1 is released**

This patch adds the `didHandleUjetError` function to the iOS SDK. The `didHandleUjetError` function can listen for and handle the following errors:

  * `networkError`
  * `authenticationError`
  * `authenticationJwtError`
  * `voipConnectionError`
  * `voipLibraryNotFound`
  * `chatLibraryNotFound`



For more information, see [Fallback](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#fallback).

## October 09, 2025

Announcement

**Version 3.39 is released**

All release notes published on this date are part of version 3.39.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Search in the email channel**

Agents can now search for emails in the agent adapter by keyword, session ID, or subject. For more information, see [Search for emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter#search-for-emails).

Feature

**Destination queue name and session history is available in the agent adapter**

The agent adapter now displays the destination queue during transfers and deflections for IVR calls. The agent adapter also displays transfer history in the **Call details** and **Chat details** tabs.

User experience changes:

  * The **Call details** and **Chat details** tabs in the agent adapter have a new **Transfer History** section.
  * The chat pane in the chat adapter has a new **Transfers** button that opens the **Transfer History** pane.



Administrators: There's a new checkbox at **Settings > Operation Management > Transfer history** for turning on transfer history in the agent adapter.

For more information, see [Transfer history and queue information in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/queue-info-transfer-history-agent-adapter).

Feature

**Virtual agents for the SMS channel**

Virtual agents are now available for the SMS channel. This lets you create virtual agents and assign them to SMS queues, offering virtual agent support to end-users in SMS chat sessions. For more information, see [Virtual agents for SMS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agents-for-sms).

Feature

**Improved controls over the ordering of key-value pairs in the agent adapter and CRM records**

Google Cloud CCaaS has improved controls over the ordering of the key-value pairs that appear in the agent adapter and in CRM records. Here's how the ordering controls work:

  * **Virtual agents** : When you configure session variables, you can use the new `display_order_in_adapter` property to specify the order that the session variables appear in the agent adapter and in CRM records. For more information, see [Capture from intent response](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#capture_from_intent_response).

  * **Web SDK** : Web SDK custom data is displayed in the agent adapter and CRM records in the order that the key-value pairs appear in the JSON custom data file. For more information about JSON custom data files, see [Chat unsigned custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk#chat-unsigned-custom-data).




Feature

**Advanced reporting dashboard updates**

We've made the following updates to the advanced reporting dashboards:

  * **Queue Group Dashboards All dashboard** : The tiles and tables on this dashboard have been replaced with the following tables:

    * **Queue Group Performance Calls** : displays detailed performance information for calls by queue group.

    * **Queue Group Performance Chats** : displays detailed performance information for chats by queue group.

For more information, see [Queue Group Dashboards All](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-group-perf#queue-group-dashboards-all).

  * **Queue interval dashboards** : The **Queue Interval - Calls** and **Queue Interval - Chats** dashboards have a new **Total Queue Entries** column in the table tile. This is the sum of all inbound interactions that have entered a queue, excluding transfers.

For more information, see [Queue interval dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-queue-interval).

  * **Virtual agent dashboards** : On both the **Virtual Agent Dashboard Calls** and **Virtual Agent Dashboard Chats** dashboards, the virtual agent metrics table contains a new **Interaction Outcome** column.

For more information, see [Virtual agent dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-virtual-agent).

  * **All Interactions - Chat dashboard** : In the **All Chat Interactions (Historical)** table, if you configure chat transcript storage for your CRM, the values in the **Chat ID** column become links to the chat transcripts.

For more information, see [All interactions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-all-interactions).

  * **New metrics in the Call Queue Metrics (Historical) Explore** : We've added the following two metrics to the **Call Queue Metrics (Historical)** Explore:

    * **CSL %** : Custom Service Level. This is calculated as follows: The number of queued interactions within SLA / The number of queued interactions answered.

    * **Total Queued Answered** : The number of queued interactions answered by a human agent.

For information about metrics in an Explore, see [Create a new metrics tile in a dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-add-tiles-to-dashboard#create_a_new_metrics_tile_in_a_dashboard).

  * **Additional dashboards with advanced capabilities** : the following dashboards now appear on the **Advanced Reporting Landing Page**. This means you can use them to create new custom dashboards or create Looks to link to custom dashboards.

**Performance**

    * **Dispositions / Calls**

    * **Dispositions / Chats**

    * **Deflections / Calls**

    * **Deflections / Chats**

    * **CSAT / Calls**

    * **CSAT / Chats**

    * **Co-browse / Calls**

    * **Co-browse / Chats**

    * **Failed / Calls**

    * **Failed / Chats**

    * **Missed / Calls**

    * **Missed / Chats**

**Agent Reporting**

    * **Agent Activity Timeline**

**Monitoring Dashboards**

    * **Calls Connected**

    * **Chats Connected**

    * **Calls Queued**

    * **Chats Queued**

For more information, see [Advanced capabilities](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-advanced-capabilities).




Feature

**Cancel scheduled calls with the callback calls API**

You can now use the callback calls API to cancel a single scheduled callback call or a list of calls. For more information, see [Callback call API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/callback-call-api).

Feature

**Mid-session authentication is supported by all CRM types**

Mid-session authentication is supported by all CRM types, not just custom CRMs. For more information, see [Mid-Session authentication by API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mid-session-authentication-apps-api).

Feature

**New advanced reporting dashboards**

The following new advanced reporting dashboard is available:

  * **Deflections**. Get deflection information by queue and for your entire contact center. For more information, see [Deflections dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-deflections).

  * **Agent activity timeline**. See the historical activity for an agent. For more information, see [Agent activity timeline dashboard](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-agent-activity-timeline).




Fixed

The following issues were addressed in this release:

  * Fixed an issue where incoming chats took precedence over the in-progress chat.

**User experience change** : When a new chat appears in the agent adapter, it no longer takes focus away from the in-progress chat. The in-progress retains focus.

  * Fixed a web SDK issue where sensitive data sent by an end-user was redacted for both the end-user and the agent, instead of just for the agent.

  * Fixed an issue where the contact list in the agent adapter wouldn't load the full list of contacts.

  * Fixed an issue where an agent clicking an email in the agent adapter returned an **Email Not Found** error.

  * Fixed an issue where managers assigned to multiple teams were unable to view agent statistics for every team they were assigned to.

  * Fixed an issue for ServiceNow users where `call_duration` was using the earliest `connected_at` time instead of the latest `connected_at` time, causing call durations to appear longer than they actually were.

  * Fixed an issue in the **Settings > Developer Settings > External Storage** pane where language checkboxes were associated with the **Co-browse Recordings** checkbox instead of the **Session Data Feed** checkbox.

**Administrators** : In the **Settings > Developer Settings > External Storage** pane, the languages checkboxes have moved from the **Co-browse Recordings** checkbox to the **Session Data Feed** checkbox.

  * Fixed an issue where agent-initiated outbound calls were using the default number for the selected queue instead of the number chosen by the agent.

  * Fixed an issue where the downloaded session chat data report contained an extra quotation mark.

  * Fixed an issue where users received an email telling them to create a password after Single Sign-On (SSO) was turned on.

  * Fixed an issue where SSO configuration settings in the user's instance were deleted after they turned off SSO.

  * Fixed an issue where an administrator couldn't configure agent status restrictions without exposing them to agents.

  * Fixed an issue where custom contact lists could only be replaced, and not removed, after they were assigned to a team.

  * Fixed an issue where the inheritance indicator and **Reset to parent** button was missing from the queue level **Contact List Management** pane.

  * Fixed an issue where the SMS and Web chat availability preferences in the agent adapter were the reverse of how they were configured.

  * Fixed an issue where queue transfer restrictions were not saved after being configured.

  * Fixed an issue that occurred when a user attempted to name a new queue. The name field abruptly lost focus after the first character, forcing the user to enter the queue name again.

  * Fixed an issue where creating an instance would time out and fail.

  * Fixed an issue that prevented reports from being downloaded.

  * Fixed an issue where the chat history for blended SMS sessions failed to save.

  * Fixed an issue where the **Transfer failed** message didn't appear. This occurred when an agent failed to pick up a transferred call before the transferred call expiration time expired.

  * Fixed an issue where IVR call recordings failed to save or were corrupted. This resulted in recordings that were only one second long, were saved in the wrong format, or weren't saved at all.

  * Fixed an issue where completed chat sessions appeared in the chats waiting area of agent desktop.

  * Fixed an issue for CRM users with voicemails that are attached directly to tickets. An incorrect "External Storage must be configured" warning appeared when configuring voicemail options for IVR queues.

  * Fixed an issue where transfer restrictions that were configured and saved for a web queue did not appear correctly the next time the **Transfer Restrictions** pane for that queue was viewed.

  * Fixed an issue where the unread message count in the chat pane was inconsistent when viewing it from multiple browser tabs.

  * Fixed an issue in virtual assistant reporting where the `finish_reason` property was incorrectly assigned to the `undefined` value. Now the `finish_reason` property is assigned to descriptive values that describe the reason for the conclusion of the chat session.

  * Fixed an issue where PDF transcripts of chat sessions contained malformed links.

  * Fixed an issue in historical reports where the fields in the **Failed Reason Description** column were blank.

  * Fixed an issue where CSAT scores were missing from some advanced reporting dashboards.

  * Fixed an issue for HubSpot users that caused long delays in case creation for inbound calls.

  * Fixed an issue where the photo and video files that the agent provided in pre-session Smart Actions didn't appear in the CRM.

  * Fixed an issue where agents in `Unavailable` status couldn't see waiting web chats.

  * Fixed an issue where HTML was not rendering properly in virtual agent messages in the agent adapter

  * Fixed an issue where agents were not switching into `Wrap-up Exceeded` status after a breakthrough call.

  * Fixed an agent desktop issue where administrators were unable to assign announcements to some teams or agents.

  * Fixed an agent desktop issue where agents couldn't copy text to the clipboard from an agent desktop custom panel.

  * Fixed an agent desktop issue where the term "Anonymous User" wasn't being translated into French.

  * Fixed an issue where the `UJET_ID` and `ANI` variables weren't passed correctly for SIP calls.

  * Fixed an issue where the chat adapter froze when agents switched between chats.

  * Fixed an issue on the **Agents** page of the Google Cloud CCaaS portal where administrators couldn't switch between session types.

  * Fixed an issue where a newly added Agent Assist platform displayed as `Invalid` even though it was valid.

  * Fixed an issue for Salesforce users where the call button didn't work when an agent attempted to call a number that was attached to a record for a previous call.

  * Fixed an issue where audio files with accented characters in their file names failed to play back when using a storage proxy.

  * Fixed an agent desktop issue where the `UJET_ID` variable in the custom URL for a custom panel wasn't being passed correctly.

  * Fixed an issue where calls originating from a native campaign generated two CRM tickets for the same interaction.

  * Fixed latency issues with web SDK Telnyx calls.

  * Fixed an issue where outbound Bring Your Own Carrier (BYOC) calls used a number other than the one agents selected in the agent adapter.

  * Fixed a Telnyx chatbot worker failure issue where background jobs related to call processing and chatbot escalations were failing and consuming excessive system resources.

  * Fixed an issue where calls to the bulk user upload endpoint returned a success status even when the uploads failed.

  * Fixed an issue in the chat waiting field of the agent desktop when multiple chats were in wrap-up. Instead of displaying **Wrap-up in progress** for all sessions in wrap-up, some sessions displayed **Auto answered**.

  * Fixed an issue in the queue group dashboard where the **Callbacks waiting** tile incorrectly included callbacks that were completed, abandoned, or failed.

  * Fixed an issue that caused inbound calls to disconnect if they were routed to an agent with a disabled microphone.

  * Fixed an issue for HubSpot users where logging the "call started" event (`create_activity`) in the ticket was delayed.

  * Fixed an issue that prevented transferred calls from being routed to available agents.

  * Fixed an issue in the agent adapter for French (Canada) where words weren't translated or were translated incorrectly.

  * Fixed an issue in call queue reporting where the Failed Reason Description for voice-scheduled mobile calls was not appearing.

  * Fixed an issue that prevented external chat transcripts from being passed into new chat sessions. 

  * Fixed an advanced reporting issue where CSAT ratings were not appearing correctly when creating custom dashboards.

  * Fixed an advanced reporting issue where callbacks waiting metrics didn't match in the following dashboards: **Queue Groups Dashboard Calls** and **Queued Calls Status Dashboard**.




## September 25, 2025

Announcement

**Web SDK version 2 will be shut down on June 26, 2026**

On June 26, 2025, we announced the launch of [Web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes#June_26_2025). Starting on **June 26, 2026** , the web SDK v2 will no longer function. Be sure to [update your website](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

## September 04, 2025

Announcement

**Agent desktop is GA**

Agent desktop is now [generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Agent desktop is a customizable interface that provides agents quick access to the information and tools they need to handle customer sessions. The desktop layout includes the agent adapter as well as configurable panels that display information or tools. You can configure a distinct desktop layout for each session type: inbound calls, outbound calls, or chats. You can then configure which desktop layout that an agent sees when they answer an inbound call, place an outbound call, or handle a chat. You can also configure announcements to communicate updates, alerts, and other important information directly to agents. For more information, see [Agent desktop](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-overview).

The agent desktop provides the following capabilities:

  * **Create desktop layouts**. With agent desktop, you can create customized desktop layouts for different use cases for your human agents. These include receiving inbound calls, placing outbound calls, and handling chat sessions. Your layouts can contain call adapters, chat adapters, and a wide variety of panels for other capabilities such as live transcripts, knowledge assist, disposition codes, and session data feeds. You can also configure custom panels to use as widgets that you can drag into panels. For more information, see [Create desktop layouts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).

  * **Configure custom panels**. A custom panel displays one or more URLs for external resources. These can be documentation, tools, or other resources. A custom panel appears as a widget in the desktop layout builder. Then, when you create desktop layouts, you can drag widgets into panels. For more information, see [Configure custom panels](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-widgets).

  * **Use widgets**. Widgets are containers of specific functionality that you can drag into panels in the desktop layout builder. The desktop layout builder comes with a number of pre-defined widgets, such as **Session Data Feed** , **Disposition Codes and Notes** , **Knowledge Assist** , and **Live Transcript**.

  * **Configure desktop layouts for agents**. You can configure which desktop layout that agents see when they answer an inbound call, place an outbound call, or handle a chat. You can configure this globally, at the queue level, and at the team level. Queue-level layout settings take priority over global settings. Team-level settings take priority over both queue-level settings and default settings. For more information, see [Configure desktop layouts for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-set-desktop-layouts).

  * **Configure announcements**. With announcements, you can communicate updates, alerts, and other important information directly to agents. Announcements appear in the agent desktop as notification banners that persist until the agent dismisses them. Announcements also appear in the agent's announcement list. For more information, see [Configure announcements](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-configure-announcements).




## September 02, 2025

Announcement

**Mobile SDK 2.14 is released**

Mobile SDK 2.14 includes the following updates:

  * Android SDK and iOS SDK:

    * Support for virtual agent to virtual agent chat transfers by queue.

    * Support for hiding the download transcript button in the options menu, the post-chat screen, or both. For the Android SDK, see [SDK configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#sdk-configuration). For the iOS SDK, see [Show or hide the download transcript button](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-sdk-guide#show-or-hide-download-transcript-button).

    * Improved accessibility, including better navigation and screen reader support.

  * Android SDK:

    * Support for hiding the SDK using the `Ujet.hideSDK()` method. For more information, see [Hide the SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#hide-sdk).

    * New event types: `MessageLinkClicked` and `QuickReplyClicked`. For more information, see [Event Notifications](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-sdk-guide#UUID-b0019caa-2311-8ca3-64d7-f181ea921d77).




To support the new virtual agent chat transfer capabilities of this release, we've added a new configuration setting in the Google Cloud CCaaS portal. You can use this setting to hide transfer system messages in chat sessions with virtual agent to virtual agent transfers.

**Administrators** : In the **Settings > Chat > Web & Mobile Chat Settings** pane, there's a new **Transfers** checkbox.

For more information, see [Hide transfer messages in chat sessions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers#hide-transfer-messages-in-chat-sessions).

## August 29, 2025

Fixed

Fixed an issue where the Android SDK wouldn't minimize when an end-user clicked a deep link.

## August 20, 2025

Announcement

**Version 3.37 is released**

All release notes published on this date are part of version 3.37.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Skip the connecting message playback**

You can now configure your instance to skip playback of the connecting message when calls are connected to agents.

Administrators: The **Settings > Call > Call Details** pane contains a new **Skip the Connecting Message playback** checkbox.

For more information, see [Configure global call settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure-global-call-settings).

Feature

**New advanced reporting dashboards**

The following new advanced reporting dashboards are available:

  * **Missed interactions**. Get data on missed interactions to help you optimize operations. For more information, see [Missed interactions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-missed-interactions).
  * **Failed sessions**. Get insight into why your sessions are failing. For more information, see [Failed sessions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-failed-sessions).
  * **Screen share**. Get data on your agents' Screen Share interactions with end-users. For more information, see [Screen shared dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-screenshare).
  * **CSAT**. Get insights into the customer satisfaction (CSAT) ratings that end-users give to their sessions with agents. For more information, see [CSAT dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-csat).
  * **Dispositions**. Get disposition information to gain insights into common end-user issues and concerns. For more information, see [Dispositions dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-dispositions).



Feature

**Web SDK version 3.37**

Starting with version 3.37, web SDK releases align with portal releases and share the same version number.

Web SDK version 3.37 includes the following update: we've improved the accessibility of the web SDK to be in compliance with the European Accessibility Act.

Feature

**Restrict email transfers**

You can now configure your instance to prevent users with the agent role from transferring email sessions to other agents. Agents can still assign unassigned emails to themselves, and users with the manager role can still transfer email sessions from agent to agent.

Administrators: There's a new **Transfer Restrictions** pane at **Settings > Queue > Email > Edit / View > [queue] > Transfer Restrictions > Configure**.

For more information, see [Prevent email reassignment](https://docs.cloud.google.com/contact-center/ccai-platform/docs/prevent-email-reassignment).

Feature

**Generative knowledge assist is available in the agent adapter**

Generative knowledge assist is now available in the agent adapter.

Feature

**Generative knowledge assist is available in Agent Desktop**

Generative knowledge assist is now available in Agent Desktop as a widget that you can drag into a desktop panel.

For more information, see [Create desktop layouts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-desktop-create-desktop-layouts).

Feature

**Workforce Management terminology update**

We've updated the terminology in the Workforce Management interface to align with Google Cloud CCaaS terminology. For example, we've changed "supervisor" to "manager", "employee" to "agent", and "Supervisor Portal" to "Manager Portal".

Fixed

The following issues were addressed in this release:

  * Fixed an issue where a blank error message box appeared in the agent adapter when a call connected.
  * Fixed an issue where the notification icon for a new message or event in the chat adapter didn't clear after the agent viewed the message or event.
  * ~~Fixed a Conversational Insights issue where conversation recordings were split into a file for the human agent segment and a file for the virtual agent segment. Now all call segments are aggregated into a single recording file, which is more useful for conversational analysis.~~
  * Fixed an issue where a single call was being reported as two separate calls after the following occurred: (1) A call was escalated from a virtual agent to a queue, (2) An agent clicked **Answer** in the agent adapter, and (3) The end-user hung up before the countdown was complete.
  * Fixed an issue where agents were unsure whether their action of declining a call was taking effect. Now, after an agent declines a call, the **Decline** button changes to **Declining...** , the **Answer** button is deactivated, and a message displays indicating that the call was declined.
  * Fixed the message that appeared in the agent adapter when an agent left a multi-party session. Instead of saying that the session will be transferred to the remaining agents(s), the message now says that the session will be transferred to the remaining participant(s). This is because the remaining participants might not be agents.
  * Fixed an issue where administrators were unable to monitor or barge into calls.
  * Fixed an issue where the **Decline** button didn't display or didn't work correctly in the agent adapter when the following occurred: (1) An agent was in an active call, and (2) The agent received a second call on their direct number.
  * Fixed an issue where clearing the **Play Call Recording Message** checkbox in **Settings > Call > Call Details** pane didn't work if the queue was configured for human agents and virtual agents or virtual agents only.
  * Fixed an issue where the **Transfer failed** error message failed to appear in the call adapter after the following occured: a transferred call wasn't answered before the unanswered call expiration time expired.
  * Fixed an issue where an agent on a team that was assigned to a queue wasn't able to select their desired queue to make an outbound call. We also improved the text at **Settings > Call > Call Details > Queue Selection for Outbound Call** to better describe the call adapter behavior.
  * Fixed an issue where the missed chat message didn't appear after the missed chat threshold expired.
  * Fixed an issue where end-users were unable to download chat transcripts containing special characters, emoji, or redacted content.
  * Fixed an issue with the web SDK where configuring custom system messages with empty quotes or NULL values didn't fully suppress the messages.
  * Fixed an issue with the web SDK where some non-English characters in downloaded chat transcripts were appearing as question marks.
  * Fixed an issue in Hubspot where recordings of transferred calls were failing to save.
  * Fixed an issue in Salesforce where the **Call** button in the call adapter wasn't working for outbound calls to a phone number that was associated with a previous record.
  * Fixed an issue where the data in reports didn't match the data in the dashboards.
  * Fixed an issue where virtual agent calls using Dialogflow CX failed, ending unexpectedly.
  * Fixed two cross-site scripting vulnerabilities in the agent adapter.
  * Fixed an issue where deltacast selected the agent with the longest time in the Available status instead of the agent with the longest time since their last customer interaction.
  * Fixed an issue where escalations from a virtual agent to a human agent failed, and audio from the last agent response before human agent escalation was truncated.
  * Fixed an issue where transcriptions weren't being created for IVR calls.
  * Fixed an issue where agents could become stuck in wrap-up status, particularly with concurrent calls or quick callbacks.



## August 13, 2025

Announcement

**Check the version number of your instance**

You can now check the version number of your instance and compare it with the version numbers of the updates and patches that Google announces in these release notes. In this way you can know which capabilities are available in your instance. For more information, see [Check the version number of your instance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#check_the_version_number_of_your_instance).

## August 11, 2025

Announcement

**Availability in three additional regions**

Google Cloud CCaaS is now available in the following three additional regions:

  * northamerica-northeast2 (Toronto)
  * us-east4 (Virginia)
  * me-west1 (Tel Aviv)



In each of these regions, Workforce Management is available and advanced reporting isn't available. For more information, see [Google Cloud regions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/localities#regions).

## July 24, 2025

Announcement

**Mobile SDK patch 2.13.1 is released**

This patch fixes an issue where the Android SDK didn't support deep linking in the customizable link format.

## July 08, 2025

Announcement

**Mobile SDK 2.13 is released**

Mobile SDK 2.13 includes the following updates:

  * End-users can download chat transcripts to their devices during a session or after a session ends. For more information, see [Download chat transcripts using the web SDK and mobile SDKs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts#download_chat_transcripts_using_the_web_sdk_and_mobile_sdks).

  * The user experience with post-session virtual assistants is improved in the following ways:

    * You can configure an opt-in banner to appear for the post-session virtual assistant experience.

    * The user interface makes it easier for an end-user to know whether they are speaking to a human agent or a post-session virtual agent.

  * End-users can navigate the user interface using keyboard shortcuts in conformance with the W3C Web Content Accessibility Guidelines.

  * You can configure your instance to let end-users skip customer satisfaction surveys.




Fixed

The following issues were addressed in this release:

  * Android SDK:

    * Fixed an issue where system messages containing an empty space were being sent, even though the message strings were set to NULL.
  * iOS SDK:

    * Fixed an issue where the "Skip the human agent" button was displayed after an end-user was transferred to a virtual agent.

    * Fixed an issue where a notification sound played for new chat messages despite the end-user disabling notifications.




## July 07, 2025

Announcement

**Session metadata in Conversational Insights conversations is GA**

The Google Cloud CCaaS capability of including session metadata when creating conversations in Conversational Insights is now [generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages). Metadata values are available for each conversation. For more information, see [Conversational Insights and Quality AI](https://docs.cloud.google.com/contact-center/ccai-platform/docs/conversational-insights).

## July 02, 2025

Announcement

**Version 3.36 is released**

All release notes published on this date are part of version 3.36.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Salesforce: New closed record options for scheduled calls**

If you've integrated Google Cloud CCaaS with the Salesforce CRM, you can configure how your instance handles scheduled calls for closed records. Here are the configuration options that are available with Salesforce integrations:

  * **Don't look up record status**. Your instance doesn't look up record status and makes the scheduled call regardless of whether the record is open or closed.

  * **Look up record status and reopen closed records**. Your instance looks up record status before making a scheduled call and reopens records that are closed.

  * **Look up record status and cancel scheduled calls for closed records**. Your instance looks up record status before making a scheduled call and cancels scheduled calls for records that are closed.




Administrators: The **CRM Record Creation Details** pane at **Settings > Operation Management** has new settings at **Closed record options when initiating an API-scheduled call**.

For more information, see [Schedule calls with Salesforce](https://docs.cloud.google.com/contact-center/ccai-platform/docs/schedule-calls-salesforce).

Feature

**Configure storage of Screen Share recordings**

You can now configure how long to store Screen Share recordings in your external storage settings. You can also now store Screen Share recordings that originated from the Screen Share adapter. 

Administrators: The **CRM Comments Creation Details** pane at **Settings > Operation Management** has new **Post Cobrowse recording link to CRM record** settings. You need to contact Google support to enable Screen Share recordings.

For more information, see [Set up external storage for CRMs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage).

Feature

**Restrict auto-assignment for email queues**

You can now configure email queues so that incoming emails are auto-assigned only during queue operating hours or to agents who are signed in.

Administrators: The **Auto assignment** dialog at **Settings > Queue > Email Edit/View > [queue name] > Automatic assignment > Configure** has two new checkboxes.

For more information, see [Email auto assignment](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#email-auto-assignment).

Fixed

The following issues were addressed in this release:

  * Fixed an issue where calls weren't being assigned to the correct agent in Google Cloud CCaaS reporting.
  * Fixed an issue where calls weren't being assigned to the correct agent in the CRM.
  * Fixed an issue where the communication between a virtual task assistant and an end-user was not included in the Agent Assist live transcript in the agent adapter.
  * Fixed an issue where agent outbound calls generated incorrect URLs in reporting. URLs contained `ticket` instead of `tickets`.
  * Fixed an issue where newly created global contact list destinations were not available in the **Overcapacity Deflection** settings for IVR queues.
  * Fixed an issue where the `on_email_thread_created` event listener was mistakenly logging customer names and email addresses.
  * Fixed an issue where uploading a new overcapacity deflection message didn't replace the existing message.
  * Fixed an issue where agents were not being assigned chat sessions while routing was configured for deltacast.
  * Fixed an issue where attachments were lost when: (1) A chat session was transferred to another agent, or (2) After a chat auto-dismissed, an end-user restarted the chat with the same agent in the same queue.
  * Fixed an issue where chats didn't time out after being inactive for longer than the chat timeout setting for the queue.
  * Fixed an issue where agents who were removed from a chat session using the **Connected Chats** page were not fully disconnected from the session. These agents remained in the conversation tile, couldn't remove themselves from the session, and couldn't receive new chats.
  * Fixed an issue where chats initiated outside of working hours generated incorrect chat transcripts. Instead of indicating that the support center was closed, the transcripts indicated that customer support was experiencing high volume.
  * Fixed an issue where an external agent and an end-user couldn't communicate after an internal agent did the following: (1) Answered the call, (2) Put the end-user on hold, (3) transferred the call to a queue with auto redirect to an external number, and (4) failed to release the hold before leaving the call.
  * Fixed an issue where end-users with a blocked phone number were able to contact support using chat.
  * Fixed an issue where the global disposition list appeared in the chat adapter during wrap-up instead of the disposition list for the agent's queue.
  * Fixed an issue where a barge-in event interrupted an agent's audio.
  * Fixed an issue where call session recordings were either not being sent to external storage or they were sent in the wrong file format.
  * Fixed an issue in advanced reporting dashboards where chats appeared in the chat waiting menu even after the chat sessions ended.
  * Fixed an issue where the agent desktop translations in French (Canada) and Japanese were not complete.
  * Fixed an issue where the system was generating duplicate After Call Work records for a single wrap-up.
  * Fixed an issue where bulk upload containing new users assigned to teams failed.
  * Fixed an issue where the chat adapter failed to appear after Nexmo VOIP initialization failed.
  * Fixed an issue where saving chat transcripts to a CRM failed.



## June 26, 2025

Announcement

**Web SDK version 3**

We're pleased to announce that the web SDK v3 is now [generally available (GA)](https://cloud.google.com/products#product-launch-stages). The web SDK v3 is built on the [headless web SDK](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide), so all of the methods that are available on a headless SDK client are also available with the web SDK v3 widget.

**Deprecation notice**

Starting on ~~**December 31, 2025**~~ **June 26, 2026** , the web SDK v2 will no longer function. Be sure to [update your website](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade) to use the web SDK v3 before that date to avoid breaking your integration with the web SDK. We are no longer adding new features to the web SDK v2.

**Capabilities**

The web SDK v3 provides the following new capabilities:

  * **View previous chats and download chat transcripts**. End-users can view previous chats and download chat transcripts from the web SDK widget. For more information, see [View previous chats and download chat transcripts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-transcripts).
  * **Web forms**. You can set up HTML web forms to collect data from end-users. For more information, see [Use data collection forms](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms).
  * **Include conditional operators with proactive chat triggers**. When configuring proactive chat triggers, you can include OR operators with keywords and AND operators with multiple conditions. For more information, see [Proactive Web SDK Triggers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/proactive-web-sdk-triggers#UUID-ff948643-7f0c-2db5-ff46-a3e121b180d4).
  * **Agents can attach files during chats**. An agent can attach a wide variety of file types using the web SDK widget during a chat session. For more information, see [Configure rich messaging and file attachments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-rich-messaging#rich-messaging).
  * **Disable chat audio**. An end-user can disable chat audio using the web SDK widget.
  * **System message categorization**. System messages are categorized as standard, confirmation, or error types.
  * **Post-session transfers when the end-user ends a session**. Post-session transfers can be triggered when an end-user ends a call or chat session. For more information, see [Post-session transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-session-transfer).



**Documentation**

Here's the web SDK v3 documentation:

  * [Web SDK v3 guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-getting-started)
  * [Web SDK v3 strings guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-strings)
  * [Upgrade from web SDK version 2 to web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade)



**Upgrade**

For help upgrading to web SDK v3, see [Upgrade from web SDK version 2 to web SDK version 3](https://docs.cloud.google.com/contact-center/ccai-platform/docs/web-sdk-v3-upgrade). If you've been using the Private Preview version of web SDK v3, be sure to update your implementations to access `widget.js` from your Google Cloud CCaaS instance.

## June 09, 2025

Announcement

**Salesforce ICU Update**

This is for Google Contact Center as a Service (CCaaS) customers that use Salesforce integration with CCaaS.

On **June 15th, 2025** , Salesforce is rolling out an automatic upgrade to its International Components for Unicode (ICU) locale data. This affects how date, time, number, and currency formatting are handled across Apex, Visualforce, and Lightning components.

This change affects Salesforce integrations that are using Apex API versions earlier than 45.0. These integrations use the legacy Java locale behavior, which could cause formatting discrepancies, incorrect parsing, or runtime errors.

**Solution**

Google has reviewed the CCaaS managed package and has updated the impacted classes to use safe, ICU-compatible parsing and formatting methods. This includes cleaning up legacy code that uses older API versions, which might affect this transition.

The following table shows the affected classes:

**Affected classes**

Name | API version  
---|---  
`UJETUtilsController` | 35.0  
`UJETUtilsControllerTests` | 35.0  
`UJETJWT` | 43.0  
`UJETJWTTests` | 43.0  
`UJETPageController` | 43.0  
  
**Required action**

To ensure compatibility with the Salesforce ICU update and prevent any operational impact, you must complete the following action before **June 15th, 2025** :

  * Install the [v1.40 update](https://login.salesforce.com/?ec=302&startURL=%2Fpackaging%2FinstallPackage.apexp%3Fp0%3D04tKk0000011MNw%26InstHostname%3Dlogin.salesforce.com).



This installation updates the affected classes. No further action is required.

**What happens if you don't upgrade?**

If any part of your integration or Apex code uses versions earlier than 45.0 after June 15th, Salesforce will not apply the ICU formatting to those sections. This could potentially lead to issues, including the following:

  * Incorrect date and time parsing

  * Unexpected errors in workflows or automations

  * Mismatch between Lightning and Classic behavior

  * Breakage in integrations expecting consistent locale handling




Google considers the affected classes in CC_AGENT_APP v1.38 to be safe. While some of the affected classes have legacy methods that are affected by this update, they are not being actively used and will be deprecated in version 1.40. Regardless, Google still recommends installing the v1.40 update. Not upgrading can potentially impact other solutions that are installed on the environment, as described in this communication.

**Defer the update**

As described in [Enable the ICU Locale Formats](https://help.salesforce.com/s/articleView?id=xcloud.icu_migration_enable.htm&type=5), you can defer the automatic rollout of this update.

To defer this update, follow these steps:

  1. From the Quick Find search box in **Setup** , enter **User Interface**.

  2. On the User Interface page, deselect the **Enable ICU locale formats as part of the scheduled rollout** checkbox.




**Important** : This will only be effective if completed before **June 15th 2025**.

## June 05, 2025

Announcement

**Patch 3.35.15 is released**

This patch does the following:

  * Fixes an issue in agent desktop. When an agent had active chat sessions with two end-users simultaneously, the chat history was missing for one of the chats.

  * ~~Fixes an issue where bulk user upload jobs on the**Bulk User Management** page got stuck and didn't complete.~~

  * Fixes an issue in agent desktop where the chat adapter was unavailable when a chat was received.




## May 28, 2025

Announcement

**Headless web SDK 3.6.5 is released**

This release does the following:

  * Fixes an issue where duplicate messages from the virtual assistant appeared in the end-user's chat pane.

  * Fixes an issue where end-users were able to reactivate inactive chats outside of operating hours.

  * Fixes an issue with data collection forms, where the SDK timed out during the form server's first load attempt, causing a delay in the appearance of the form in the end-user's chat pane.




## May 27, 2025

Announcement

**Version 3.35 is released**

All release notes published on this date are part of version 3.35.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**New sender email with auto-response emails**

You can now configure an outbound-only email address and use it as the sender address for auto-response emails. The outbound-only address is a "no-reply" email address that prevents the receiver from responding.

User experience changes:

  * The **Auto-response** dialog at **Settings > Queue > Email > [your-email-queue] > Auto-response** has a new **Sender email** field.
  * The **Add an email** dialog at **Settings > Developer Settings > Email Account Management > Email account list > Add email account** has a new **This is an outbound only email account** checkbox.



For more information, see [Configure an outbound-only email account](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-outbound-only-email-account) and [Configure an auto-response email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-auto-response-email).

Feature

**Remove email subject lines from interaction data**

We now support removing email subject lines when you delete interaction data from your instance for specified end-users. The email subjects are removed when you delete data for an end-user in the **Consumer Privacy** dialog at **Settings > Consumer Management > Consumer Privacy**. To completely remove an end-user's data, you must also delete their emails from your mail server. You must also delete chat transcripts, call recordings, and other session-related files from your CRM or external storage, depending on your configuration.

For more information, see [Remove subject lines from end-user email interactions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/remove-end-user-data#remove-subject-lines-from-email-interactions).

Feature

**QM integration now includes chat session events**

You can now export chat session events to an external quality management (QM) system. After you configure the endpoint of your QM system in Google Cloud CCaaS, your chat session events can be streamed to the endpoint in real time.

User experience change:

  * The **QM Integration** dialog at **Settings > Developer Settings > Session Data Export > QM Integration** has a new **QM Chat Events - send chat sessions events** checkbox.



For more information, see [QM, SIPREC, and WFM integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/qm-siprec-integration).

Feature

**Include images in outbound emails**

You can now include images in outbound emails. This includes emails from an agent in an email session and outbound auto-response emails.

User experience change:

  * The **Auto-response** dialog at **Settings > Queue > Email > [your-email-queue] > Auto-response** has a new **Insert Image** button.
  * The email adapter has a new **Insert Image** button.



For more information, see [Agent email adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter) and [Configure an auto-response email](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-auto-response-email).

Fixed

The following issues were addressed in this release:

  * Fixed an issue where calls were being logged as **Call with unknown contact** in HubSpot instead of under the correct contact name.
  * Fixed an issue where the client secret couldn't be saved when a user attempted to set up authentication (using either basic authentication or OAuth) for a custom CRM with the **Generic API** CRM lookup method.
  * Fixed an issue where the setup dialog for **Find an account by query endpoint** could not be reached due to an authentication error when configuring OAuth for a custom CRM.
  * Fixed an issue where calls were being passed to a custom CRM with the incorrect phone number format.
  * Fixed an issue for ServiceNow users where records were created for outbound calls despite the agent selecting **Do not create a record** in the call adapter.
  * Fixed an issue where a queue did not have access to the global contact list even though it was configured to have access to it.
  * Fixed an issue where the **Directory** tab didn't appear when an agent was transferring a call.
  * Fixed an issue where the **Voice Campaign** checkbox didn't appear for **Select Call Types** in the **Create Reports** pane, despite the user having the appropriate report access permissions.
  * Fixed an issue where agent extension deflection recordings didn't upload after appearing to be successfully uploaded.
  * Fixed an issue that occurred when the `@{NEXT_REOPEN_HOUR}` dynamic variable was put in the **Message** field for **After Hour Messaging** in the **Web & Mobile Messages** pane. The variable always resolved as the next time the chat queue opened on the _following_ day. This happened even when the next time the chat queue opened was on the _current_ day.
  * Fixed an issue that occurred when an end-user on the global contact list placed an inbound call to a queue with access to the global contact list turned off. The agent adapter displayed the destination name of the caller, despite access to the global contact list being turned off.
  * Extended the search conditions for the **Directory** tab in the agent adapter to include search by an extension number.
  * Fixed an issue where the "next open hours" message was incorrect when a chat ended after midnight.
  * Fixed an issue where the call transcript failed to continue after an agent returned from hold.
  * Fixed an issue where the default disposition list appeared in the agent adapter instead of the custom disposition list, which was configured to appear.
  * Fixed an issue where a user with a manager role received a "Not Authorized" error when attempting to use the **Operation Management** and **Disposition Codes** pages.
  * Fixed an issue where the `failReason` and `afterHours` fields in the session metadata file were incorrect for chats that failed because they were attempted after hours.
  * Fixed an issue where the **Assign agents** button wasn't working for custom after hours deflection and automatic redirection.
  * Fixed an issue where the client secret was not saved when configuring OAuth for a custom CRM.
  * Fixed an issue where calling the current queue status endpoint of the Manager API intermittently returned a 404 error.
  * Fixed an issue where the wrong disposition code list appeared for an agent after transferring a chat to an agent in a different queue.
  * Fixed an issue where chat shortcuts were not working in the agent adapter for mobile chats.
  * Fixed issues where agents were unable to successfully move beyond the wrap-up state to handle the next call.



## May 14, 2025

Announcement

**Mobile SDK 2.12 is released**

Mobile SDK 2.12 includes the following updates:

  * Added support for the following languages: 
    * Ukrainian
    * English - India
    * Hindi
    * Romanian
    * Croatian
    * Russian
    * Tagalog
  * End-users can receive and download attachments during sessions. The following file types are supported: 
    * Images: JPEG, JPG, PNG, GIF, WebP
    * Video: MP4, MOV, AVI, WMV, WebM
    * Audio: MP3, WAV, M4A, WEBA
    * Other file types: PDF, DOC, XLS, PPT, CSV, TXT



## May 13, 2025

Announcement

**Version 3.34 is released**

All release notes published on this date are part of version 3.34.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Spelling and grammar check is available for SMS and WhatsApp sessions**

Spelling and grammar check is now available for SMS and WhatsApp chat sessions. For more information, see [Agent Assist for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#agent-assist-chat).

Feature

**Co-browse is renamed to Screen Share**

We've renamed the Co-browse capability to Screen Share. We've made this change in the user interface and in the documentation. However, we haven't renamed any endpoint, property, object, or other programmatic element in the APIs or the SDKs for this update.

Feature

**Manual wrap-up is automatically assigned to the last completed chat**

When an agent manually enters wrap-up status, wrap-up is automatically assigned to the agent's last completed chat. For more information, see [Manual wrap-up](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#manual-wrap-up).

Feature

**Virtual agent to virtual agent chat transfers**

A virtual agent can now transfer a chat session to another virtual agent by transferring to the queue that the destination virtual agent is assigned to. For more information, see [Virtual agent to virtual agent transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-to-va-transfers).

Fixed

The following issues were addressed in this release:

  * Fixed an issue that prevented agents from calling other agents using a phone number with an extension.
  * Fixed an issue where a phone number with an extension and a comma separator was not displaying correctly.
  * Fixed an issue where some properties in the session metadata file were not correct for a session that was monitored by another user.
  * Fixed an issue where chat duration was incorrect in reporting.
  * Fixed an issue where a user was unable to change from the wrap-up status to another status.
  * Fixed an issue where call IDs mistakenly appeared in agent activity timeline reports.
  * Fixed an issue where the scroll bar didn't appear in the chat navigation panel of the chat adapter. This prevented agents from scrolling to chats that were hidden from view.
  * Fixed an issue where error messages were mistakenly sent to end-users while they were waiting for a virtual agent to connect to their session.
  * Fixed an issue where the **Performance Overview Dashboard** was displaying incorrect information on the **Chats > Queue Abandoned** and **Virtual Agent Chat > Total Escalations** tiles.
  * Fixed an issue where sessions that were escalated by a virtual agent arrived in the destination queue and were never assigned to an agent because of an error in prioritization.
  * Fixed an issue where auto-generated session summaries for the virtual agent segments of a session were not appearing in the agent adapter.
  * Fixed an issue where a Screen Share error message mistakenly appeared the next time Screen Share was attempted.
  * Fixed an issue where links that agents sent to end-users in a chat session did not have underscores, despite rich messaging being turned on. 
  * Fixed an issue where email was causing abnormally high CPU usage.
  * Fixed an issue where message preview was not working in the agent adapter for web SDK and chat.
  * Fixed an issue where the incorrect error message appeared when SSO sign-in failed.
  * Fixed an issue where manual wrap-up caused high CPU usage.
  * Fixed an issue where **Chat ID** was not available as an incoming field type when adding a parameter for post-session chat transfers.
  * Fixed an issue where agents were unable to send messages in the chat adapter.
  * Fixed an issue where the chat shortcut list continued to display after the agent deleted the shortcut keyword from the chat text field.
  * Fixed an issue where chat shortcut categories were appearing in the shortcut list in the chat adapter despite the fact that they contained no chat shortcuts.
  * Fixed an issue in the chat adapter where the **View original** and **View translation** links were not translated into the language of the chat adapter.
  * Fixed a Workforce Management issue where login durations for events that spanned multiple intervals were incorrectly reported.
  * Fixed a Workforce Management issue where short abandoned chat counts were incorrectly reported.
  * Fixed a Workforce Management issue where the historical or ready time values exceeded 900 seconds.
  * Fixed an Workforce Management issue where reporting data was missing for sessions over 45 minutes.
  * Fixed a Workforce Management issue where hold duration was counted multiple times in reporting.
  * Fixed a Workforce Management issue where query performance was sub-optimal.
  * Fixed a Workforce Management issue where the OutboundCount and OutboundHandleTime calculations were incorrect in the AgentSystem report.
  * Fixed a Workforce Management issue where agent queue data was not given the same treatment for calls as it was for chats.
  * Fixed an agent desktop issue where the calls waiting and chats waiting fields in the menu bar displayed incorrect text when the French language was selected.
  * Fixed an agent desktop issue where the **Insert summary** button (for inserting a generated session summary) appeared during wrap-up even when session summarization was turned off.
  * Fixed an agent desktop issue where a **View Previous** banner mistakenly appeared when clicking the chats field in the menu bar.
  * Fixed an agent desktop issue in the session data feed, where the date and time were not formatted correctly in French.
  * Fixed an agent desktop issue where an agent who transferred a session and then left it was unable to see the chat adapter after being re-added to the session.



## April 29, 2025

Announcement

**Advanced reporting dashboards are released for GA**

Advanced reporting dashboards can help you gain insights into the performance of your contact center. You can create new custom dashboards based on tiles from other dashboards and use powerful editing capabilities to customize dashboards to suit your business needs. Advanced reporting dashboards are released for [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Advanced reporting dashboards](https://docs.cloud.google.com/contact-center/ccai-platform/docs/dashboards-overview).

## April 14, 2025

Announcement

**Headless web SDK 3.6.4 is released**

Headless web SDK 3.6.4 fixes a problem where the virtual agent was sending multiple repeated messages to end-users in chat sessions.

## April 09, 2025

Announcement

**Web SDK 2.24.4 patch is released**

This patch fixes a cross-site scripting vulnerability.

## April 08, 2025

Announcement

**Headless web SDK 3.6.3 is released**

Headless web SDK 3.6.3 fixes a cross-site scripting vulnerability.

## April 02, 2025

Announcement

**Version 3.33 is released**

All release notes published on this date are part of version 3.33.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**View transcripts for completed chats**

~~If you save chat transcripts in external storage, you can view them from the**Completed Chats** dashboard.~~ This capability is not available in version 3.33. We expect to include it in an upcoming release.

Feature

**Conditional overcapacity deflections**

You can now enable conditional overcapacity deflections for calls. You can choose from a number of wait-time conditions or time-of-day conditions, and you can create a distinct deflection message for each condition that you configure.

**Administrators** : be aware that configuring conditional overcapacity deflections can override queue-level settings.

For more information, see [Configure call settings ](https://cloud.google.com/contact-center/ccai-platform/docs/call-settings#Configure-call-settings).

Feature

**New call type in reports: Voice Outbound (UCaaS)**

We've added the **Voice Outbound (UCaaS)** report type to the **Create Reports** page for calls and chats so you can generate reports that contain this type of call. For more information, see [Call and chat types](https://docs.cloud.google.com/contact-center/ccai-platform/docs/standard-reports#call-and-chat-types).

Feature

**New post events for virtual task assistants**

The following new virtual task assistant post events are available:

  * Virtual task assistant joined
  * Virtual task assistant left
  * Virtual task assistant session variables received



The agent adapter can use the browser's `postMessage()` method to send events to the parent iFrame to trigger various actions in your custom CRM application.

**Administrators** : if you use virtual agents to capture session variables and display them in any downstream integrations such as a CRM or the agent adapter, you must use these new [post events](https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-events-for-vtas) in your [virtual agent custom payloads](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload). This is a mandatory change. Review your current implementation and remap session variable associations as needed. The existing Dialogflow payload for custom session variables has also been updated to support data selection for virtual task assistant post events.

For more information, see [Post events for virtual task assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-events-for-vtas).

Feature

**New options for CRM comments when saving call recordings and chat transcripts to external storage**

When you save call recordings and chat transcripts to external storage, you can control how these are referenced in the CRM record. You now have the following options:

  * Add a call recording or chat transcript link as a comment in the CRM record.
  * Add the call recording or chat transcript filename as a comment in the CRM record.
  * Don't add any reference to the call recording or chat transcript in the CRM record.



To make comments consistent across CRM platforms, we've standardized on the following phrases in CRM comments: **Chat Transcripts** , **Call Recordings** , and **Voicemails**.

For more information, see [Configure CRM comments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-external-storage#configure-crm-comments).

Feature

**Configure a contact list destination to pass data parameters to a SIP header**

You can configure a contact list destination to pass data parameters to a SIP URI when an agent uses the destination to make an outbound call or transfer a call. For more information, see [Add a destination to a contact list](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list#add-destination-to-contact-list).

Feature

**Session metadata contains conversation IDs for virtual agents and Agent Assist**

The session metadata file now contains the conversation ID for a virtual agent or for Agent Assist if either of those are involved in a session.

**Administrators** : if you're directly mapping session metadata fields in downstream systems, review your current implementation and remap your field associations as needed.

For more information, see [Sessions metadata content](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata#sessions_metadata_content).

Feature

**Bulk agent status import improvements**

When you import agent statuses in bulk, the **Import Statuses** dialog now indicates when the upload is complete and sends you a confirmation email. For more information, see [Bulk status management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#bulk-status-management).

Feature

**Salesforce CRMs: attach a CCaaS session object to a CRM record if a matching CRM record is found**

For Salesforce CRMs, when you append a call or chat session to the latest open record, you have the option to attach a CCaaS session object to a CRM record if a matching CRM record is found. For more information, see [Session data mapping by CRM](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-data-mapping-by-crm).

Fixed

**Fixed a cross-site scripting vulnerability**

This update fixes a cross-site scripting vulnerability.

Fixed

The following issues were addressed in this release:

  * Fixed an issue where users couldn't deactivate a disposition code or list that was assigned to a queue when the queue was deleted prior to the deactivation.
  * Fixed an issue in Kustomer integrations where an outbound call to a number that wasn't in the CRM wasn't creating a record.
  * Fixed an issue where the button to assign a record ID to a session was missing from the agent adapter.
  * Fixed an issue for the **Customer End User Dial '0' Behavior** queue settings. After a user selected and saved the **Dialing '0' moves user back up one level in IVR** setting, an error was returned when they attempted to select a different setting.
  * Fixed an issue where NICE call recordings failed and returned an `Exception 12` error.
  * Fixed an issue where agents couldn't transfer call or chat sessions to another queue. This occurred when all assigned agents in the destination queue were unavailable or at the concurrency limit.
  * Fixed an issue where searches for chat shortcuts were case sensitive. These searches are now case insensitive.
  * Fixed an issue where the option to select the account ID and record ID for a session appeared in the agent adapter even when they were configured in the platform to not appear.
  * Fixed an issue where the call flexible inbound record ID for a session was not automatically suggested in the agent adapter.
  * Fixed an issue where no records were displayed in the **Record ID** field during wrap up.
  * Fixed an issue where the first open record created by the end-user was selected instead of **Create New Record** being selected.
  * Fixed an issue where the default value for the record ID for a session was not the most recently closed and updated record.
  * Fixed an issue in Salesforce integrations where the **Answer** button in the agent adapter didn't appear for incoming calls. This happened after the agent clicked the **Assign** button multiple times while attempting to assign a record ID or account ID to a session during wrap up.
  * Fixed an issue where the **Assign** button appeared in the agent adapter during wrap-up even when the account ID and record ID were already assigned to the session.
  * Fixed an issue where the **Assign** button in the agent adapter was clickable multiple times during wrap up. Now, after an agent assigns a record ID or account ID to a session, the **Assign** button is no longer active.
  * Fixed an issue where the option to assign a record ID or account ID to a session didn't appear during wrap up even though the agent didn't make these assignments during the call.
  * Fixed an issue where the **Next** button for assigning a record ID or account ID to a session was inactive until the agent made a different selection.
  * Fixed an issue where the Agent Assist icon didn't appear in the agent adapter when an agent returned to an inactive chat.
  * Fixed an issue where an error was returned when a user attempted to assign an email session to another user.
  * Fixed an issue in workforce management where the day planner didn't display the green checkmark after a file was imported.
  * Fixed an issue in workforce management where the green success message didn't appear for some forecast types.
  * Fixed an intermittent issue where the chat adapter was not appearing when incoming chat sessions arrived.
  * Fixed an issue to preserve expected chat adapter behavior when switching to a custom CRM.
  * Fixed an issue where the data passed in SIP headers was malformatted if the SIP endpoint was selected from the contact list.
  * Fixed an issue in the agent desktop where the chat window was unavailable after an agent ended a session that was transferred or routed from a virtual agent chat session.
  * Fixed an issue to ensure that a customer who returns to an inactive chat after hours sees an "after hours" message.
  * Fixed an issue where agents couldn't add attachments to emails.
  * Fixed a date and time mismatch issue in Alvaria agent productivity files generated by Google Cloud CCaaS.
  * Fixed an issue where Chrome's built-in spelling checker was not working in the chat adapter.



## February 27, 2025

Announcement

**Patch 3.31.36**

This patch does the following:

  * Fixes an issue where the chat adapter was not appearing in the agent desktop when an incoming chat was received.
  * Fixes an issue where agents in Unavailable or Wrap up status were not receiving incoming contacts and were put into Unresponsive status.
  * Fixes a security vulnerability.



## February 17, 2025

Announcement

**Version 3.31 is released**

All release notes published on this date are part of version 3.31.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Interaction history retrieval is extended to 90 days**

There are two new settings for specifying how many days of interaction history to retrieve: **60 days** and **90 days**. For more information, see [Set up interaction history](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#set-up-interaction-history).

Feature

**Additional options for maximum transfer limits for chats**

You can now specify whether you want virtual agents, human agents, or both to be included in transfer counts. You can also specify whether you want the transfer count reset to zero when a chat is dismissed. For more information, see [Configure transfer limits for chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-settings-web-and-mobile#configure-transfer-limits-for-chats).

Feature

**Restrict outbound calling to emergency or special services**

You can restrict outbound calling to emergency or special services by agent and location. The following configuration options are available:

  * Restrict specific agents from calling emergency or special service phone numbers.

  * Configure from which locations agents are permitted to call emergency or special service phone numbers.




For more information, see [Restrict outbound calling for agents (new number)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#restrict-outbound-calling-agents).

Feature

**Custom agent status lists**

You can create lists of custom statuses and assign them to queues or teams. This gives you control over the statuses that agents in queues and teams can use. For more information, see [Agent status lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#agent-status-lists).

Feature

**Automatic redirect with percent allocation**

You can configure automatic redirection so that specified percentages of sessions are redirected to the redirection groups that you specify. For more information, see [Automatic redirection](https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection).

Feature

**Blended inbound and outbound calling**

You can automatically transition agents between handling outbound campaign calls and inbound calls, based on call volumes and conditions that you configure. For more information, see [Call blending](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-management#call-blending).

Feature

**Availability preferences**

You can create availability preferences filters and apply them to users and teams. This lets you filter incoming contacts so only the appropriate types of contacts enter their queues. You can also give agents the ability to create their own availability preference filters. Filtering criteria include channel, session direction, schedule, transfers, and more. For more information, see [Availability preferences](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-status#availability-preferences).

Feature

**Transfer restrictions for teams**

Transfer restrictions, which let you control the source and destination of transfers, is now available for teams. For more information, see [Configure team transfer restrictions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#configure-team-transfer-restrictions).

Feature

**Get user configuration data using the Apps API**

You can now use the Apps API to get user configuration data. For more information, see [Get user configuration data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-user-configuration-data).

Feature

**Agents can configure spelling and grammar check in the chat adapter**

You can let agents turn spelling and grammar check on and off in the chat adapter. You can also let agents select the language for spell and grammar check. For more information, see [Turn on and configure Agent Assist for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#aa-turn-on-chat) and [Check spelling and grammar](https://docs.cloud.google.com/contact-center/ccai-platform/docs/check-spelling-and-grammar).

Feature

**Pass data parameters to a virtual agent mid-session**

You can pass data parameters to a virtual agent while a session is in progress. For more information, see [Pass data parameters to virtual agents mid-session](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters#virtual-agent-custom-data).

Fixed

Fixed an issue where the summary box in the chat adapter was not sized correctly when using a CRM.

Fixed

Fixed an issue where the SIP URI format was not accepted in the user interface.

Fixed

Fixed an issue for custom CRM users where the CRM record was not appearing when a session started.

Fixed

Fixed an issue where chats that were escalated from a virtual agent were assigned the wrong priority and never connected with an agent.

Fixed

Fixed an issue where chat shortcuts were not entered into message input fields when selected from the chat shortcut list.

Fixed

Fixed an issue where agents couldn't see waiting chat contacts when their statuses were set to **Unavailable**.

Fixed

Fixed an issue with Co-browse taking too long to start.

Fixed

Fixed an issue where the **Dismiss** button in the agent adapter didn't meet accessibility requirements for contrast.

Fixed

Fixed an issue where changing deflection settings for agent extensions in the call adapter failed.

Fixed

Fixed an issue where character limits were causing errors when email templates were being created.

Fixed

Fixed an issue where attempting to cancel a call transfer failed.

Fixed

For workforce management, fixed an issue where an error was returned when searching for an employee in the **Assign Shift** pane.

Fixed

Fixed an issue where agents could not set their statuses to **Busy** after calls.

## January 08, 2025

Announcement

**Version 3.29 Patch 1**

This Patch 1 of version 3.29.

Fixed

Fixed the Twilio webhook order for multi-region instances.

Fixed

Fixed an issue with Alvaria Workforce integration where the Alvaria Agent Productivity file was showing incorrect dates.

Fixed

Fixed an issue with the Zendesk CRM where the queue name field was not populated for chats.

## January 07, 2025

Announcement

**Version 3.30 is released**

All release notes published on this date are part of version 3.30.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Support for additional languages**

We've added support for seven additional languages, as follows:

  * Agent facing and end-user facing languages: Croatian, Hindi, Romanian, Russian, Ukrainian, and Tagalog .
  * End-user facing language: English (India).



For more information, see [Supported languages](https://docs.cloud.google.com/contact-center/ccai-platform/docs/languages).

Feature

**Greater control over custom data**

You have greater control over the types of SDK custom data that is sent to session metadata files and CRM records and that is displayed in the agent adapter. You can control these at the global and at the queue level. For more information, see [Send SDK custom data](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-sdk-custom-data).

Feature

**Direct SMS numbers and configuring SMS chat in the agent adapter**

You can assign direct SMS numbers to agents, allowing end-users to send SMS chat messages directly to agents without passing through a queue. You can also let agents configure SMS chat deflections and chat greeting messages in the chat adapter. For more information, see [Direct SMS numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/direct-sms-numbers) and [Configure SMS chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-sms-chat).

Feature

**Web forms for chat**

You can create data-collection forms that agents can present to end-users using the agent adapter. For more information, see [Data collection forms](https://docs.cloud.google.com/contact-center/ccai-platform/docs/use-data-collection-forms).

Feature

**Support for call waiting**

We now support call waiting, which enables agents to simultaneously manage multiple inbound calls from different channels. For more information, see [Call waiting](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-waiting).

Feature

**Short call recovery timer is shortened**

After a short call, the countdown timer to available status is reduced from 180 seconds to 15 seconds. For more information, see [Scheduled calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#scheduled-calls).

Feature

**Configure wrap-up separately for inbound and outbound calls**

You can now configure wrap-up separately for inbound and outbound calls, both globally and at the queue level. For more information, see [Wrap-up settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#wrap-up-settings).

Feature

**Cascade conditions**

~~You can add cascade conditions such as SLA, agent availability, and queue length to your cascade group logic.~~ This capability is not available in version 3.30. We expect to include it in an upcoming release.

Feature

**Configure transfer limit for chats**

You can set a limit on the number of times a chat session can be transferred. In addition, you can determine an agent's options when the limit has been reached. You can disable the transfer button or specify a queue for one final transfer. For more information, see [Configure transfer limits for chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-settings-web-and-mobile#configure-transfer-limits-for-chats).

Feature

**Agents can select the queue for outbound calls**

You can configure your instance so that agents can select the queue that they want to use when making an outbound call. For more information, see [Configure global call settings](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure-global-call-settings).

Fixed

Fixed an issue where the queued chat dashboard showed the source queue instead of the destination queue.

Fixed

Fixed an issue where the **Extension Number** field disappeared from the **User & Team Settings** page.

Fixed

Fixed an issue where YouTube data was missing from the billing report.

Fixed

Fixed an issue where an email JSON file was re-uploaded to a Google Cloud Storage bucket when it already existed there.

Fixed

Fixed an issue where chats were not connecting when an Android app sent signed custom data with an empty payload.

Fixed

Adjusted the agent inclusion criteria in billing for Co-browse.

Fixed

Added `AgentValue` to the NICE WFM reports.

Fixed

Fixed an issue where wait times were incorrectly represented as handle times in reports.

Fixed

Fixed an issue where phone number DAPs weren't handled properly for inbound Telnyx SIP calls.

Fixed

Fixed a problem with the user interface for ServiceNow Next Experience.

Fixed

Fixed an issue where the queue name field was empty for chats and emails in Zendesk.

Fixed

Fixed the NICE WFM Daily Activity Data Summary report to be generated at 12:00 AM in the configured timezone

Fixed

Fixed errors in smart compose and in spelling and grammar.

Fixed

Fixed copy and paste in the agent adapter.

Fixed

Fixed an issue with Alvaria WFM where the productivity file contained the incorrect dates.

Fixed

Improved queue settings page performance.

Fixed

Fixed NICE WFM data export so it has consistent naming conventions.

Fixed

Fix an issue where an agent extension continued to appear in the Complete List of Users CSV file even after it was removed from an instance.

## November 13, 2024

Announcement

**Flutter for the Mobile SDKs**

You can now use Flutter to help you integrate the Mobile SDKs (the Android SDK and the iOS SDK) into your Android or iOS app. For more information, see [Integrate using Flutter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/mobileSDK-overview#integrate-using-flutter).

## November 12, 2024

Announcement

**Mobile SDK 2.10 is released**

Mobile SDK 2.10 includes the following updates:

  * iOS SDK: 
    * **Text resizing**. End-users can increase text size up to 200%. Text is resized using the device settings.
  * Android SDK: 
    * Fixed the sticky button behavior so that it matches iOS. 
  * Android SDK and iOS SDK: 
    * Fixed an issue where content card text was misaligned.



## November 07, 2024

Announcement

**Version 3.29 is released**

All release notes published on this date are part of version 3.29.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Generative knowledge assist using Agent Assist**

Agents can now view knowledge articles while on a call or chat. These knowledge articles appear as clickable tiles in the agent adapter and are generated based on the ongoing conversation between the agent and end-user. Agents can click a tile to open the article in a browser tab. Agents can also search for knowledge articles using a search field in the agent adapter. For more information, see [Turn on and configure Agent Assist for calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#aa-turn-on-calls) and [Turn on and configure Agent Assist for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#aa-turn-on-chat).

Feature

**Alvaria WFM for chat**

Customers with Alvaria integrations can now receive chat session data. For more information, see [Alvaria Workforce integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/alvaria-wfm).

Feature

**Clickable authentication icon**

The authentication icon in the agent adapter can now be clicked by the agent to mark the customer as either authenticated or unauthenticated. For more information, see [User profile flags for calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide#user-profile-flags-calls) and [User profile tags for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-profile-flags-chat).

Feature

**New Agent_Assist_Added event**

A new `Agent_Assist_Added` event is now available. This event contains the conversation ID for a specific agent assist session. For more information, see [Agent Assist added](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#agent-assist-started).

Feature

**Support for direct SIP REFER in virtual agent call transfers**

Virtual assistant call transfers now support the direct SIP REFER method. This means you can pass useful information in the call transfer, such as caller intent and account information. Call transfer data is recorded as Planned Transfers in virtual assistant metrics. For more information, see [Transfer a call to a SIP endpoint using the SIP REFER method](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-custom-payload#transfer-to-SIP-endpoint-using-sip-refer).

Feature

**Queue operation statuses endpoint**

We added a new API endpoint that lets you check whether a queue is in After Hours (AH) or Overcapacity (OC) status. For more information, see [Queue operation statuses endpoint](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-queue-operation-statuses).

Feature

**Clear the voicemails in a queue**

You can now clear the voicemails in any queue from the **Call** settings page. For more information, see [Clear voicemails from queues](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#clear-voicemails).

Feature

**New SDK data parameters for CRM lookup**

The following new SDK data parameters are now available for CRM lookup: `SDK Name`, `SDK Email`, `SDK Phone`, and `SDK Identifier`. For more information, see [Request URL Parameters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#request-url-parameters).

Feature

**Skip CRM account and record creation (Zendesk and ServiceNow)**

You can now skip CRM account and record creation for Zendesk and ServiceNow. For more information, see [Skip CRM account and record creation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation).

Feature

**Interaction history**

In the agent adapter, agents can view an end-user's interactions from previous call and chat sessions. This provides context to help agents provide a better support experience and improve handle time. Supervisors can also see interaction history when viewing connected call or chat sessions. For more information, see [Interaction history](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#interaction-history).

Feature

**SDK parameters in the custom CRM lookup flow**

You can now use SDK data parameters in the CRM lookup flow. For more information, see [CRM lookup URLs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#crm_lookup_urls).

Feature

**Agent status translation**

You can translate the default, system, and custom agent statuses for the languages supported by Google Cloud Contact Center as a Service (CCaaS). Google Cloud CCaaS provides automatic translation of default and system statuses. It also lets you do translations manually. For more information, see [Agent status translation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management#agent-status-translation).

Feature

**Queue transfer restrictions**

You can control which queues or teams that agents can transfer sessions to. This provides more granular control over call flows and helps prevent improper transfers. For more information, see [Restrict queue transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#restrict-queue-transfers).

Feature

**Display email session ID in the email adapter and email subject**

You can now display the session ID in the email adapter and in the subject line of an email thread. For more information, see [Append the session ID to email subject lines](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#append-session-id-to-email-subject-lines) and [Agent email adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter).

Feature

**Chat transcripts download**

This capability is currently not available.

Feature

**Use the admin user for CRM API calls with Salesforce**

Using Salesforce, you can now use the admin user for all CRM API calls for record creation and updating, while still allowing agents to retain ownership of CRM-specific actions. For more information, see [Salesforce configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-default-admin#salesforce_configuration).

Feature

**Segment summarization**

Generative session summarization now includes segment summarization if there are multiple segments in a session. A segment is created each time there is a transfer to a human agent or a virtual agent. For more information, see [Agent Assist for calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#aa-for-voice-calls) and [Agent Assist for chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-assist#agent-assist-chat).

Fixed

Fixed an issue where transferring calls to a parent queue sometimes caused calls to drop.

Fixed

Fixed an issue that sometimes prevented agents from going into Available status after wrapping up a call while still in a chat session.

Fixed

Fixed an issue where wrap-up and disposition settings were not following destination queue settings when calls and chats were transferred.

Fixed

Fixed an issue where the wait time for transferred sessions sometimes displayed incorrectly on the "Queued Calls" and "Queued Chats" dashboards.

Fixed

Fixed an issue where the session summary wouldn't automatically scale with the height of the chat adapter.

Fixed

Improved the user interface for the email transcript capability.

## October 15, 2024

Announcement

**Version 3.27 is released**

All release notes published on this date are part of version 3.27.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Spelling and grammar check**

The agent adapter now provides spelling and grammar checking. Agents can choose from spelling and grammar suggestions while entering text in the agent adapter. You can enable spelling and grammar check globally or at the queue level. For more information, see [Check spelling and grammar](https://docs.cloud.google.com/contact-center/ccai-platform/docs/check-spelling-and-grammar).

Feature

**New destinations for incoming SIP header data**

You can now pass incoming SIP header data to session metadata files and CRM records. For more information, see [Capture data parameters from inbound SIP headers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/va-pass-data-parameters?_gl=1*1qxkhpp*_ga*MTMxNDA1MDk5MS4xNzI5MDk4NDA5*_ga_4LYFWVHBEB*MTczMDE0NjIyOC41Mi4xLjE3MzAxNDgzOTUuMC4wLjA.#capture-data-parameters-from-inbound-sip-headers).

Feature

**Emergency calling**

Agents in the US and Canada can now make calls to emergency services. Agents in Canada can make calls to other special services. You can set up queues for callback from emergency or special services. For more information, see [Set up emergency and special services calling (US and Canada only)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#set-up-emergency-and-special-services-calling).

Feature

**Conversational Agents (Dialogflow CX) is supported in additional regions**

Conversational Agents (Dialogflow CX) is now supported in additional regions. This can help you optimize performance by keeping your support agents closer to your services and end-users. For more information, see [Regionalization and location settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region).

Feature

**Voice detection for auto-answer**

You can now configure auto-answer to listen for an agent's voice after a call is connected. If no voice is detected after the specified time, the call is considered missed by the agent. For more information, see [Auto answer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/auto_answer).

Fixed

Fixed an issue where queue-level caller announcements were not working properly.

Fixed

Fixed an issue where multiple contacts could be created for the same contact.

## September 23, 2024

Feature

**Agent-level deflections**

With agent-level deflections, you can let your agents set their own deflection options for agent to agent calls. There are deflections for over-capacity, after-hours, and automatic redirection. Agents can choose to deflect to a queue, a phone number, an outbound SIP transfer, voicemail, callback, or keep waiting. Agent-level deflections can also be configured globally. For more information, see [Let an agent configure their own deflection options](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#let-an-agent-configure-deflection-options).

Announcement

**Version 3.26 is released**

All release notes published on this date are part of version 3.26.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Direct inbound calling**

With direct inbound calling, you can create direct phone numbers and assign them to agents or queues. This lets end-users call directly to an individual agent or queue, bypassing IVR queue trees. Administrators can enable inbound call recording and configure deflection options for direct inbound calls. For more information, see [Direct phone numbers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#direct-phone-numbers).

Feature

**First In First Out queue routing**

With First In First Out queue routing, you can set equal priority for transferred calls and chats and non-transferred (standard) calls and chats. By default, transferred calls and chats have priority. For more information, see [First in first out queue routing](https://docs.cloud.google.com/contact-center/ccai-platform/docs/fifo-queue-routing).

Feature

**Rich messaging**

With rich messaging, you can do the following when creating and sending messages: use bold, italic, and underline formatting; create bulleted and numbered lists; and add links. You can also add emojis to messages. This capability is available to agents in the chat adapter. It's also available to administrators when they configure chat shortcuts and the initial chat messages for the web SDK and the mobile SDKs. For more information, see [Rich messaging](https://docs.cloud.google.com/contact-center/ccai-platform/docs/configure-rich-messaging#rich-messaging).

Feature

**UPDATE: Session data is available in the agent adapter**

You can configure CCAI Platform so that users can view session data in the agent adapter. This includes virtual agent session variables and custom data from the web and mobile SDKs. This information can be useful for an agent to get additional information during a session, or for a supervisor to get an overview of a session that they barge into. For more information, see [View session data in the agent adapter](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management#view-session-data-in-the-agent-adapter).

Fixed

Fixed an issue where the generic message was played for custom after hours deflection.

Fixed

Fixed an issue where co-browse session events were not generated at session start and end.

Fixed

Fixed an issue where the Interaction JSON metadata file was sometimes not being sent to the Kustomer CRM after a chat or call ended.

Fixed

Fixed an issue where agents had more permissions than that role permits.

Fixed

Fixed an issue where messages were not sent to chat participants for chats initiated by the chat API.

Fixed

Fixed an issue where co-browse metadata was not saved when the recording option was disabled.

Fixed

Fixed an agent assist integration timeout issue.

Fixed

Implemented a change that prevents the administrator account from being deactivated or changed using bulk user update.

Announcement

**VPC Service Controls are GA**

[VPC Service Controls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/vpc-service-controls) in Contact Center AI Platform are GA. For more information, see [Product launch stages](https://cloud.google.com/products#product-launch-stages).

Fixed

Fixed an issue where users with a permission group in workforce management could not be created or edited .

Fixed

Made improvements to barge.

Fixed

Fixed an issue where the queue duration of a chat was sometimes doubled in reporting.

Announcement

**Web SDK 2.24 is released**

Web SDK 2.24 includes the following update:

  * **Support for rich messaging**. End-users can see the rich messaging that agents use in the chat adapter. For more information, see TBD.



Announcement

**Mobile SDK 2.9 is released**

Mobile SDK 2.9 includes the following updates:

  * Android SDK and iOS SDK: 
    * **Support for rich messaging**. End-users can see the rich messaging that agents use in the chat adapter. For more information, see TBD.
  * Android SDK: 
    * **Text resizing**. End-users can increase text size up to 200%. Text is resized using the device settings.



## September 03, 2024

Announcement

**Version 3.24 is released**

All release notes published on this date are part of version 3.24.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Reserved data attributes**

With reserved data attributes, you can tag sessions with one of the following labels: `Verified Customer`, `Bad Actor`, or `Repeat Customer`. You can send this information to Google at the start of a session using an SDK, a SIP header, or the Apps API. With the API you can also send this information after the session starts. After we receive this information we display it in the agent adapter so the agent or a supervisor can act accordingly. For more information, see [Reserved data attributes](https://docs.cloud.google.com/contact-center/ccai-platform/docs/send-reserved-data-properties).

Feature

**Raw data export**

With raw data export, you can export detailed CCAI Platform session data to an external storage bucket. With this data you can get insights into calls, chats, emails, queues, agent performance, virtual agents, and more. For more information, see [Raw data export](https://docs.cloud.google.com/contact-center/ccai-platform/docs/raw-data-export).

Feature

**Virtual agents can create and assign tickets for custom CRM apps**

Virtual agents can now create and assign incoming tickets for custom CRM apps prior to a human agent taking the ticket. This capability was previously available only for some commercial CRM apps. For more information, see [Configure the assignment of chat or call records created by virtual agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent#configure-assignment-of-records-created-by-vas).

Feature

**Barge is available for chat**

Barge, which lets supervisors join or take over calls with end-users, is now available for chat. For more information, see [Barge for calls and chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management#barge-for-calls-and-chat).

Fixed

Fixed an issue that prevented emails from being sent to external storage.

Fixed

Fixed an issue where listening to a voicemail would occasionally lead to the creation of a duplicate entry at the top of the list.

Fixed

Fixed an issue where integrating the Salesforce CRM with CCAI Platform was failing.

## August 30, 2024

Announcement

**VPC Service Controls and private egress**

You can now use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) with CCAI Platform to help mitigate the risk of data exfiltration from your contact center. When you include a CCAI Platform instance in a VPC Service Controls perimeter, the instance is restricted from exchanging data with Google Cloud services (such as Cloud Storage or Dialogflow) that are outside of the perimeter. You can further secure your instance by including Contact Center AI Platform API in your list of restricted services. You can then create an [access level](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels) to allow access to only your own administrators. For more information, see [VPC Service Controls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/vpc-service-controls).

In addition to private _ingress_ , you can now use Private Service Connect to set up private _egress_ from your CCAI Platform instances. For more information, see [Set up private egress](https://docs.cloud.google.com/contact-center/ccai-platform/docs/private-egress).

## August 09, 2024

Feature

**Private Service Connect and Organization Policy Service**

You can create Contact Center AI Platform (CCAIP) instances that are configured for private access, which restricts access to them over the public internet. You can then set up Private Service Connect, which lets your agents, managers, and CCAIP administrators access the private instances. This is done using your own internal IP address, keeping your traffic within Google Cloud. Private Service Connect doesn't prevent end-users from contacting your contact center as they normally would. Private Service Connect is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see [Set up Private Service Connect](https://docs.cloud.google.com/contact-center/ccai-platform/docs/set-up-psc).

You can also use Google Cloud Organization Policy to get centralized, programmatic control over your organization's resources. If you want more granular, customizable control over the specific fields that are restricted in your organization policies, you can create custom constraints. For more information, see [Manage Contact Center AI Platform resources using custom constraints ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccaip-custom-constraints).

## August 06, 2024

Announcement

**Web SDK 2.22 is released**

Web SDK 2.22 includes the following updates:

  * **Resize text**. You can change the font size for any text displayed in the agent adapter.

  * **Control link behavior**. You can control whether a link opens in the same tab or a new tab.




## August 05, 2024

Announcement

**Version 3.23 is released**

All release notes published on this date are part of version 3.23.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**New quality management (QM) session event field**

CCAIP now passes a new field in the session event payload for calls.

The new field is available in the following event payload streams:

  * QM call events

  * External call events




The new session event field is the same as the `agent_number` field in the CCAIP metadata. This field is passed in the payload for all session events that have an agent participant.

Here is an example of a session event field: `"agent_number":"1660"`

Feature

**Contact lists**

Agents can now use contact lists, which improve the organization and accessibility of external contacts. Agents can use a centralized workspace to create a personal contact list or a favorite contact list. Agents can access global and custom lists, depending on how your configure CCAIP. Administrators have the ability to: (1) Manage list visibility at the team or queue level, (2) Bulk upload CSV files containing contact lists, and (3) Add, edit, or delete contacts and destinations, including SIP URI addresses and phone numbers. For more information, see [Contact lists](https://docs.cloud.google.com/contact-center/ccai-platform/docs/contact-list?_gl=1*1pa49n6*_ga*Mzc3NzQxMjYuMTcyNTY0MjE0OQ..*_ga_4LYFWVHBEB*MTcyNTkzNzEwNi4xMy4xLjE3MjU5Mzc5MTcuMC4wLjA.) and [Use contacts](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide#use-contacts).

**Note:** The SIP directory in **Settings > Call** is now **Contact list**.

Feature

**Workforce management**

Workforce management (WFM) provides simple, flexible, real-time forecasting, scheduling, and adherence monitoring. Here are some key features:

  * **Dynamic scheduling to optimize staffing**. Save time by automating scheduling based on expected staffing needs. Allow agents to pick their schedule based on availability and skillset. WFM is customizable so you can create schedules that account for agent skills, time zones, channel coverage, employee time-off requests, and more.

  * **Intelligent, flexible forecasting**. Quickly create accurate omnichannel forecasts that model staffing requirements using both historical and real-time data. Interval, weekly, and monthly patterns and in-forecast updates provide day-to-day flexibility. You can make changes on the fly, or "set it and forget it."

  * **Schedule adherence**. WFM helps you avoid costly mistakes by providing agents and managers with real-time access to adherence and performance monitoring. This helps to ensure that agents are in the right place at the right time so there are no gaps in your customer service experience.




For more information, see [Workforce management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/wfm).

Feature

**Cancel partial responses for virtual agents**

You can now configure virtual agents (VAs) to enable cancellation of the playback of partial-responses fulfillment when the final fulfillment is returned. For example, if a webhook is called by the VA and partial responses is enabled, the fulfillment is returned to CCAI Platform and it starts playing the message to the end-user. If the final fulfillment is sent by Dialogflow to CCAI Platform while the partial-responses fulfillment is still being played, it is possible to interrupt this playback and play the final fulfillment.

For more information, see [Support for partial response in Dialogflow CX](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-agent#partial-response-dialogflow).

Feature

**End-of-session transfers for virtual agents**

You can now set up a virtual agent (VA) to handle end-of-session interactions. When a live agent ends a session, it's transferred to a VA for wrap-up. You can use end-of-session transfers for interactions such as post-session surveys or feedback. This feature is available for both calls and chats. For more information, see [Post-session transfers](https://docs.cloud.google.com/contact-center/ccai-platform/docs/post-session-transfer).

Feature

**Updated agent statuses endpoint**

The agent statuses endpoint, `apps/api/v1/agent_statuses`, now returns an agent's IP address.

Feature

**Queue-level configuration of the cascade group timer**

You can now configure the cascade group timer at the queue level, instead of only at the global level. This would be useful, for example, if you wanted the agents assigned to a VIP queue to have more time to answer before the session is moved to the next cascade group.

For more information, see [Configure a cascade group at the queue level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#configure-a-cascade-group-at-the-queue-level).

Feature

**Queue-level whisper settings for calls**

Whisper settings for calls are now available at the queue level. This feature allows you to turn off whisper messages for specific queues or customize the whisper message. For example, on a billing queue, you could provide agents with instructions such as, "Call coming through the billing queue. Remember to redact if taking any payments." In addition, you can customize the call countdown timer and enable **Use countdown** at the queue level for calls.

For more information, see [Configure whisper announcements at the queue level](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-messages-notifications#configure-whisper-announcements-at-the-queue-level).

Feature

**Queue-level configuration of the percent allocation group timer**

You can now configure the percent allocation group timer at the queue level, instead of only at the global level.

For more information, see [Percent allocation groups](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#percent_allocation_groups).

Feature

**Auto answer settings are relocated**

The following auto answer settings for calls and chats have been relocated. Functionality remains the same:

Global settings (moved to the **Operations Management Routing** page):

  * Old Locations:

    * Calls: **Settings > Call**

    * Chats: **Settings > Chat**

  * New Locations:

    * Calls: **Settings > Operation Management > Routing > Call Routing > Deltacast**

    * Chats: **Settings > Operation Management > Routing > Chat Routing > Deltacast**




Queue-level settings (moved to the **Deltacast Settings** page):

  * Old Locations:

    * Calls: **Settings > Queue > [IVR] [Mobile] [Web]**

    * Chats: **Settings > Queue > Web**

  * New Locations:

    * Calls: **Settings > Queue > [IVR] [Mobile] [Web] > Routing > Call Routing > Deltacast**

    * Chats: **Settings > Queue > Web > Routing > Call Routing > Deltacast**




For more information, see [Auto answer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#auto-answer).

Feature

**New force logout endpoint in the Apps API**

You can now do a force logout on agents, using agent ID or IP address, by making a POST call to a new Apps API endpoint: `POST /apps/api/v1/agent_statuses/force_logout`. This endpoint lets you immediately log out an agent who is not currently on a call or chat. If the agent is on a call or chat, they are automatically logged out after the call or chat ends.

Fixed

Fixed an issue where agents with chat concurrency set to 1 were incorrectly receiving new chat offers while already handling a chat.

Fixed

Fixed an issue where the Telnyx API was throwing an error when verifying a number, preventing BYOC numbers from being added.

Fixed

Fixed an issue where calls would sometimes not ring for an agent while connecting to a caller.

Fixed

Fixed an issue where chats continued to be translated after being transferred to a queue that had live translation turned off.

Fixed

Fixed a co-browse display issue.

Fixed

Fixed an issue where the agent adapter was not triggering events in an iframe when starting or ending a co-browse session.

## July 17, 2024

Announcement

**Version 3.20 is released**

All release notes published on this date are part of version 3.20.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**Agent chat adapter redesign**

We have redesigned the agent chat adapter to streamline workflows, boost productivity, and improve the agent experience. Here are the highlights:

  * A new chat details screen where agents can reference information about the end-user and the chat while the chat is active.

  * An improved chat transfer experience, including:

    * Separate tabs for agents and queues.

    * The ability to search by queue.

  * An expandable chat overview screen where agents can see additional information for each active chat. From this screen, agents can transfer chats, add users to chats, access chat options, and more.

  * An new action bar that puts an agent's most important actions within easy reach.




## July 15, 2024

Announcement

**Mobile SDK 2.8 is released**

Mobile SDK 2.8 includes the following update: added support for landscape mode.

For more information, see the following:

  * [Android SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-changelog#release-2.8)
  * [iOS SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-changelog#release-2.8)



## July 09, 2024

Announcement

**Version 3.18 is released**

All release notes published on this date are part of version 3.18.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**New session events for quality management**

The following session events are now available for quality management (QM) integration:

  * Hold
  * Mute 
  * Redaction
  * Recording indication
  * Queue information



Feature

**New custom data types for events**

The following custom data types for events are now available using the Web SDK:

  * `custom_data_secured`
  * `custom_data_not_secured`



For more information, see [Data for events](https://docs.cloud.google.com/contact-center/ccai-platform/docs/custom-crm#data_for_events).

Fixed

Fixed an issue where saving queue-level wrap-up settings to the global defaults was not behaving as expected.

Fixed

Fixed an issue where agents were not receiving audio notifications for breakthrough calls.

Fixed

Fixed an issue where viewing agent assignments was not possible for agents with a custom role.

## June 17, 2024

Announcement

**Web SDK 2.21 is released**

For more information, see [Web SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Web_SDK_Changelog/publication--en).

## June 10, 2024

Announcement

**New critical deployment schedule**

We've added a new _critical_ deployment schedule, which lets you get updates outside of peak business hours. We update instances set for the critical deployment schedule within one week after all regular deployment schedule instances are updated. We recommend the critical deployment schedule for instances that are in production environments. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

## June 05, 2024

Announcement

**Mobile SDK 2.7 is released**

For more information, see the following:

  * [Android SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-changelog#release-2.7)
  * [iOS SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-changelog#release-2.7)



## May 30, 2024

Announcement

**Web SDK 2.20 is released**

For more information, see [Web SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Web_SDK_Changelog/publication--en).

## May 28, 2024

Announcement

**Version 3.16 is released**

All release notes published on this date are part of version 3.16.

The timing of the update to your instance depends on the deployment schedule that you have chosen. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

Feature

**End co-browse sessions using the Apps API**

The Apps API has the following new endpoint that lets you end a co-browse session using an external session ID: `POST /apps/api/v1/cobrowse_sessions/{external_session_id}/end`. For more information, see [Co-browse](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Apps-API/publication#cobrowse).

Feature

**The agent adapter generates co-browse events**

The agent adapter generates events during co-browse sessions. You can use these events to get insights into co-browse session details, such as start and end times and the modes that are requested or accepted by the end-user. For more information, see [Event types](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM#event-types).

Feature

**The Next UI is supported in the ServiceNow integration**

The Next UI experience is supported in the ServiceNow CRM integration.

Fixed

Fixed the problem of the `created_at` field being missing from `add_started_activity`.

Fixed

Fixed an issue that prevented agents from selecting their next status to exit a campaign when the current call is concluded.

## April 23, 2024

Announcement

**Mobile SDK 2.6 is released**

For more information, see the following:

  * [Android SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-changelog#release-2.6.0)
  * [iOS SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-changelog#release-2.6.0)



Feature

**Deployment schedules**

With deployment schedules, you can control the timing of Google's automatic updates to your contact center instance. For more information, see [Deployment schedules](https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules).

## April 22, 2024

Announcement

**Version 3.15 is released**

All release notes published on this date are part of version 3.15.

Feature

**Chat dismissal warning for agents**

Agents receive a chat dismissal warning at the same time that an end-user receives one.

Feature

**Configure chat auto answer at the queue level**

You can configure auto answer settings for chat at the queue level. For more information, see [Auto-answer](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#auto-answer).

Feature

**Email channel endpoints in the Manager API**

The Manager API has the following two new endpoints for email data management and analysis:

  * **Email manager**. `GET /manager/api/v1/emails`
  * **Email session data report**. `GET /manager/api/v1/emails/managed`



Feature

**Skip CRM account and record creation**

With the Salesforce CRM and custom CRMs, you can skip account creation or record creation (or both) during a session. For more information, see [Skip CRM account and record creation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/skip-crm-account-record-creation).

Feature

**Authentication context**

You can select the authentication context that you want when you set up single sign-on (SSO) for CRMs that use the Security Assertion Markup Language (SAML) standard.

Feature

**New event field in session reports from the Manager API**

Session reports from the Manager API now include an `event` field. This field indicates how sessions end—for example, `finished`, `failed`, or `abandoned`. For more information, see [Calls Endpoints](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Manager-API/publication?_gl=1*1yybny2*_ga*NjUxODc2NjExLjE3MTM4MTA3MDM.*_ga_4LYFWVHBEB*MTcxMzgxMjUyMi4xLjEuMTcxMzgxMjUyMi4wLjAuMA..#calls_endpoints) and [Chats Endpoints](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Manager-API/publication?_gl=1*1yybny2*_ga*NjUxODc2NjExLjE3MTM4MTA3MDM.*_ga_4LYFWVHBEB*MTcxMzgxMjUyMi4xLjEuMTcxMzgxMjUyMi4wLjAuMA..#chats_endpoints).

Feature

**Glossary support in live translation**

Live translation supports glossaries, helping you ensure that specific terms are translated appropriately. For more information, see [Set up live translation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chat-settings-live-translation#set-up-live-translation).

Fixed

On the **Agents** page, the **All teams** filter now shows all teams, regardless of whether an agent is assigned.

Fixed

Fixed a reporting error that showed **Wait** , **Queue** , and **Handle** times as 0 for expired or abandoned chats that were escalated from a virtual agent to a queue.

Fixed

Fixed an issue with the Chat API where photos and videos sent by an end-user would sometimes not be visible to the agent in the adapter.

Fixed

Fixed an issue where virtual escalations canceled by an end-user were not being logged as abandoned.

Fixed

Fixed an issue where the Create a Record API used the user ID instead of the queue name.

Fixed

Fixed an issue where the virtual agent streaming service ended mid-session.

Fixed

Fixed an issue where a user with a custom role that included the **Settings > Queue** permission was not able to view the **Queues** page.

Fixed

Fixed an issue where the **All teams** filter on the **Agents** page didn't display the complete team hierarchy.

Fixed

Fixed an issue where a user could sometimes still hear a call after ending call monitoring.

Fixed

Fixed an issue with the ServiceNow CRM where selecting **Skip CRM record creation** disabled the contact lookup feature.

## April 17, 2024

Announcement

**Web SDK 2.19 is released**

For more information, see [Web SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Web_SDK_Changelog/publication--en#release-2.19).

## March 26, 2024

Announcement

**Version 3.13 is released**

All release notes published on this date are part of version 3.13.

Feature

**Deflections are available for agent-to-agent calls**

You can configure agent-to-agent calls to deflect to voicemail after a period of time that you set. You can also include these "voice internal" calls in your call reports. For more information, see [Turn on deflections](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#turn-on-deflections).

Feature

**Calls waiting indicator**

The call adapter includes a calls waiting indicator that indicates the number of calls in the queue waiting to be answered. You can find the calls waiting indicator in the **Calls** tab of the call adaptor.

Feature

**Support for multiple data parameters in API requests to the DAPs for your IVR queues**

You can capture data in the headers of incoming Session Initiation Protocol (SIP) calls and pass them in API requests to the Direct Access Points (DAPs) for your Interactive Voice Response (IVR) queues. For more information, see [API DAPs](https://docs.cloud.google.com/contact-center/ccai-platform/docs/routing#api-daps).

Feature

**Support phone number is included for incoming calls**

The incoming call screen shows the support phone number that the end-user used to call your support center. For more information, see [Receive an inbound call](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide#receive-inbound-call).

Feature

**Virtual task assistant for chats**

The virtual task assistant is available for chats. Configuration and use are similar to that of the virtual task assistant for calls. Available for the web SDK only. For more information, see [Virtual task assistants](https://docs.cloud.google.com/contact-center/ccai-platform/docs/virtual-task-assistants).

Feature

**Agent alias**

Agents can use aliases instead of their real names when communicating with end-users. Admins can configure agent aliases manually or with a bulk upload. Agents can also configure their own aliases. The agent alias feature is available when using the mobile and web SDKs. For more information, see [Agent alias](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent___Team_Configuration#agent-aliases).

Feature

**Country code of the outbound phone number is included with the added party's phone number**

When an agent adds a party to a call, the country code from the outbound phone number is automatically included with the added party's phone number.

Feature

**Configure SSO for your email channel using OAuth credentials from Google Cloud**

You can configure single sign-on (SSO) for your Contact Center AI Platform email channel using OAuth 2.0 credentials from Google Cloud. For more information, see [Configure your email channel for OAuth with Google Cloud](https://docs.cloud.google.com/contact-center/ccai-platform/docs/oauth-email-google).

Feature

**Time stamp in the chat adapter displays seconds**

The message time stamp in the chat adapter displays seconds.

Fixed

Fixed an issue where the **Assign Agents** button wasn't working on top-level queues.

Fixed

Fixed an issue where calls sometimes got stuck in a queued state when an agent had a poor network connection.

Fixed

Fixed an issue where the **Copy CRM Link** button in the call adapter sometimes copied the CRM ID instead of the URL.

Fixed

Fixed an issue where using keyboard shortcuts or arrow keys to scroll in a window did not allow scrolling beyond a single screen of text.

Fixed

Fixed an issue where a CRM page did not load in the Call Center AI Platform portal.

Fixed

Fixed an issue where the queue-level call music section was not displayed to users with a custom role.

Fixed

Fixed an issue that resulted in an error being returned whenever an agent tried to send a blended SMS message, despite preset SMS being disabled.

## March 04, 2024

Announcement

**Mobile SDK 2.5 is released**

For more information, see the following:

  * [Android SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-changelog#release-2.5.0)
  * [iOS SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-changelog#release-2.5.0)



## February 28, 2024

Announcement

**Web SDK 2.18 is released**

For more information, see [Web SDK changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Web_SDK_Changelog/publication--en#release-2.18)

## February 21, 2024

Announcement

**Version 3.11 is released**

All release notes published on this date are part of version 3.11.

Feature

**Support for partial response in Dialogflow**

CCAI Platform supports the partial response option in Dialogflow. This is particularly useful when the virtual agent needs to call a webhook that will likely take a while to run. With partial response enabled, Dialogflow can immediately send an initial fulfillment message to the end-user, such as, "One moment while I look that up." This way, while the webhook runs and the final fulfillment message is generated, the end-user expects a short wait instead of assuming that there is a problem. For information about configuring this capability in Dialogflow, see [Partial response for streaming API](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#partial-response).

Feature

**Cold chat transfer**

Agents can do a "cold transfer" for a chat. With a cold chat transfer, the agent assigns a chat session to a new agent or a queue, and then immediately leaves the chat without waiting for the new agent to join. This helps agents efficiently transfer chats without being bound to them. For more information, see [Transfer a Chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Transfer_for_Chat).

Feature

Added new response fields for indicating agent availability to the `manager/api/v1/agents/current_status` and `apps/api/v1/wait_times` APIs. These indicate the number of assigned agents, logged-in agents, available agents, and breakthrough agents.

Fixed

Updated virtual task assistants to support an unlimited number of data parameters.

Fixed

Fixed an issue where holiday-hours messages didn't play when the support center or queues were outside of their hours of operation.

Fixed

Fixed an issue where the **Agent** and **Supervisor** filters on the **Agents** page displayed as **All undefined**.

Fixed

Fixed an issue where the file name was not visible when the user held the pointer over the compose-email pane.

Fixed

Fixed an issue where the automatic redirect to a PSTN number used a direct PSTN dial instead of the configured BYOC SIP dial settings.

Fixed

Fixed an issue preventing the editing of user permissions for Microsoft Teams users.

Fixed

Fixed the error message that displays when an administrator disables an email queue with an invalid IMAP connection.

Fixed

Fixed an issue that prevented copying an IVR menu structure.

Fixed

Fixed an issue where the account ID in search results did not refresh after removing search input.

Fixed

Fixed an issue where the Contact Name displayed 'Chat User' instead of the end-user's name.

## January 29, 2024

Announcement

**All release notes published on this date are part of the 3.10 release**.

Feature

**Chat translations** : CCAI Platform now supports automatic translations in the Agent Chat Adapter. The end-user's message is automatically translated into the Agent Adapter's default language. Incoming messages are translated according to settings on the incoming queue. Responses from the agent are then automatically translated back into the end-user's language.

Feature

**Deltacast and Multicast, queue-level configuration** : Admins can now designate a cast type (Multicast or Deltacast) at the queue level. The following updates are included:

  * Updated queue and global settings in the CCAP Platform Portal, featuring a dedicated **Routing** section to configure call or chat routing.
  * A new **Deltacast Attempt Count** setting that lets you configure how many times to attempt to Deltacast to a single agent before Multicasting.



Feature

**OAuth for Email Channel** : Email channel authentication now supports [Microsoft OAuth](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-oauth).

Feature

**Pass CCAI Platform metadata to web chat Virtual Agent** : You can now pass CCAIP metadata parameters to a Virtual Agent for web queues. For more information on adding a dynamic parameter see [Pass Data Parameters](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters#pass_data_parameters_to_virtual_agents_and_task_assistants).

Fixed

Fixed an issue that caused a Dialogflow CX session to not last longer than 30 minutes.

Fixed

Fixed an issue that prevented the use of the clipboard copy function while using a CRM in **custom CRM** view.

Fixed

Fixed an issue where the **Smart Actions** menu wouldn't close if the agent was redacting the call.

Fixed

Fixed an issue where closing the participants' screen did not navigate the agent back to the call screen.

Fixed

Fixed an issue where the displayed time of the participants joining the call was marked as invalid.

Fixed

Fixed an issue that caused some screens in the Agent Call Adapter to be displayed with a black background when the agent had dark mode activated in the **Kustomer CRM**.

Feature

**Email Chrome notification** : CCAI Platform now offers Chrome push notifications to notify agents when they are assigned new emails.

Fixed

Fixed an issue that caused an agent to receive errors if they tried to send messages through the **Blended SMS** feature when custom messages were disabled.

Feature

**Agent Call Adapter, answer button** : The answer button has been updated to be more visible to agents.

Fixed

The search field for disposition codes is no longer case sensitive.

## January 09, 2024

Announcement

**All release notes published on this date are part of the 3.9 release.**

Feature

**Agent Extensions** : Agent Extensions allows agents to be assigned an extension for agent-to-agent calling. The agent adapter has a new directory tab. See the [agent guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-extensions-guide) and [configuration guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings#configure_agent_extensions) for details.

Feature

**Email Channel** : CCAI Platform now supports the new _Email Channel_ feature, which allows you to set up and provide email support. This features includes the following new functionalities:

  * Comprehensive configuration options including global settings, queue-level settings, auto-response, and email account data storage management.
  * An integrated email adapter providing agents an email workspace.
  * A new default agent status, **In-email**.
  * Various configuration options for pushing email details to the CRM.



For more information, see the [email channel documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel)

Deprecated

The existing Dialogflow CX **Chat, Voice (Legacy) onboarding flow** is now deprecated. We encourage customers to transition to the new onboarding flow for improved functionality. Dialogflow agents already onboarded using the legacy platform can still be used as normal.

Feature

**Virtual Agent platform improvements**

  * **Service drop-down selection** : The workflow selection drop-down in the _Add/Edit Virtual Agent Platform_ menu now offers the new Dialogflow CX onboarding flow for chats. 
  * Support for _Analyze Content_ in the Dialogflow API for chat VA sessions.



Feature

**Queue level EWT caller announcement** : You now have the ability to configure Estimated Wait Time (EWT) announcements at the queue level, enabling more personalized interactions. See the [call and chat setttings documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-settings?_gl=1*147x1b4*_ga*MTE1ODk2OTY1NC4xNzA1OTUwMzQ2*_ga_4LYFWVHBEB*MTcwNjI5OTM2NS4xLjEuMTcwNjI5OTM2NS4wLjAuMA..#configure_estimated_wait_time_announcements) for details.

Feature

**Display previous chats** : Display previous chats allows end-users and agents to see any prior support chat interactions. Previous chats are displayed above the new incoming chat, so agents and end-users can scroll up in the chat view to read through previous interactions.

Feature

**Support for WhatsApp** : CCAI Platform now supports WhatsApp. See the [social channel documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/social-channel) for details.

Feature

**Multiple disposition code lists** : Disposition code management is based on creating codes and organizing them into lists. You can now group a collection of _disposition codes_ into a _disposition list_. You can then apply the disposition list to queues that share a set of common disposition codes. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management#configure_global_and_queue_level_disposition_notes_code_and_lists) for details.

Fixed

**Enhanced Call Management** : The rules table columns for allowing/denying international calls can now be sorted.

Fixed

Fixed an issue that prevented agents from transferring to unavailable agents (even if this was configured to be possible).

Fixed

Fixed an issue that caused the volume to sometimes be recorded inaccurately in the Queue Groups Summary report.

Fixed

Fixed an issue that caused records to not be created if **Do not record** was configured for the queue.

Fixed

Fixed an issue that caused some actions during calls to not be recorded properly in Salesforce.

Fixed

Fixed an issue that would sometimes cause errors when tickets were created on Zendesk.

Fixed

Fixed an issue where the agent's next status selection could not be canceled.

Fixed

If no SmartActions are available to the agent, the SmartActions button will no longer be displayed.

Fixed

Fix for when an agent selected **do not create record** within the ServiceNow CRM and no outbound calls were recorded.

Fixed

**Expanded Agent Extensions** : You can now use extension numbers up to 10 characters in length.

Fixed

Added Dialogflow API timeout if it failed.

## December 11, 2023

Breaking

**The 3.6 CCAI Platform release might have inadvertently impacted some users' External Storage Settings**.

Navigate to **Settings >Developer** to view external storage settings. If **External Storage Settings** has been inadvertently toggled to **Off** , please [enable and configure external storage](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#configure_external_storage_with_google_service_account) to restore media uploads.

## December 06, 2023

Feature

**Mobile Release 2.4, iOS and Android SDK** : New functionality _Display Previous Chats_ allows end-users and agents to see any prior support chat interactions. Previous chats are available in the Web and Mobile SDK (for end-users) and in the agent chat adapter (for agents). Storing chat transcripts in _External Storage_ is required for this feature.

**iOS fixes**

  * Fixed an issue where the _End chat_ button was sometimes not displayed when using a Virtual Agent.
  * Fixed a crash that would sometimes occur when end-users returned to a chat.



**Android fixes**

  * Fixed an issue where the phone's default email app was not opened on Android 13.
  * Fixed an issue where Virtual Agent data parameters were sometimes not posted in the correct format.
  * Fixed an issue where returning to chat from _Notifications_ did not automatically scroll to display the latest message.



See the [iOS Changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ios-changelog) and [Android Changelog](https://docs.cloud.google.com/contact-center/ccai-platform/docs/android-changelog) for details.

Announcement

All release notes published on this date are part of the 3.6 release.

Feature

**Call history** : The new _call history_ feature allows agents to see a list of completed calls and associated metadata such as time stamps, call duration, and disposition notes. The call details view provides additional information to aid in determining whether a callback is necessary, for example whether the consumer received assistance from another agent. Call history can be enabled at **Settings > Call > Call Details**. See the [call details documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features?_gl=1*ftn5hh*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2NzA3Mi4wLjAuMA..#call_details) for details.

Feature

Two new voicemail features are included in this release:

  * **Voicemail forwarding** allows agents to forward voicemails to other queues, specific agents, or back to the same queue.
  * **Voicemail history** allows agents to access previous voicemails, providing them with the information they need to take further actions when required.



See the [voicemail documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features?_gl=1*6z0r50*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2NjYyNi4wLjAuMA..#voicemail_2) for details.

Feature

**Holidays Messaging Menu** : A new enhancement to the Holidays feature allows you to tailor your contact center's messaging during holidays. You can now customize voice-based and text-based greetings for each holiday under **Settings > Support Center Details > Holidays**. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Support_Center_Details?_gl=1*oobfc4*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2Njk1Ny4wLjAuMA..#create_folders_and_holidays) for details.

Feature

**Call Adapter** : The redesigned Call Adapter is now available, including the following enhancements:

  * **Enhanced transfer experience** : _Combined Transfer_ and _Add Party_ are now combined into one streamlined process. You can now use the _Outside Line_ tab during call transfer. 
    * **Separate Agent and Queue tabs** : Switch between Agent and Queue tabs for a smoother transfer management.
    * **Search by queue** : Find the right queue quickly with a new search feature.
  * **Improved blended SMS experience** : Blended SMS now has a dedicated tab, enhancing accessibility and user-friendliness. The user interface now mirrors a traditional chat experience, providing a more intuitive interaction for agents.
  * **New call details screen** : Provides ready access to call information during a call and allows the the CRM to be opened from the Call Adapter.



See the [Agent Call Adapter user guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-adapter-agent-guide) for more information.

Fixed

Fixed an issue that caused the reorder feature from functioning correctly on the queue structure editing page.

Feature

**Custom caller ID using SIP headers** : This feature allows you to set a custom caller ID from an incoming SIP header. You can configure this feature at **Settings > Operation Management > Data Parameters > Voice**. Select the _Use SIP Header Data for Caller ID_ checkbox and enter the _Field Name_ in the field box. The custom caller ID will be presented on the Call Connecting and Connected screens. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters?_gl=1*1qk8gi5*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2Njg5OS4wLjAuMA..#gather_data_from_session_initiation_protocol_sip_headers) for details.

Feature

**Phone number management, pagination and search** : The following updates have been made to the phone number management page (available at **Settings > Call> Phone Number Management**):

  * _Pagination_ : You can now browse entries page by page with a maximum of 100 entries per page.
  * _Search by Phone Number or Label_ : To find a specific entry, you can now enter your desired criteria in the ​ _Search Phone Number or Label_ search box​.



See the [phone number management documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features?_gl=1*6z0r50*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2NjYyNi4wLjAuMA..#phone_number_management) for details.

Feature

**Session data export settings updates** : Available at **Settings > Developer Settings > Session Data Export**.

  * _New Verint Face-to-Face recording settings_ : Configurable for those with a Verint integration. You can now add email domains in order to record calls made by agents with matching email domain addresses. See the [Verint documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/additional-integrations?_gl=1*1b3zna4*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2NzIyOC4wLjAuMA..#verint_face-to-face_voice_interaction_recording) for details.
  * The NICE integration section is renamed to [QM integration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings?_gl=1*u74o5h*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMjY2MTY4NC41LjEuMTcwMjY2NzI3MS4wLjAuMA..#enable_session_data_export_qm_or_siprec_integration).



Fixed

Fixed an issue causing the invalid HOLD button.

## November 07, 2023

Announcement

**Release 3.4**

All release notes published on this date are part of the 3.4 release.

Change

**Virtual Agents** : CCAI Platform now automatically sets the channel-specific value when calling the Dialogflow CX API. Voice calls are set to `voice`, chat conversations are set to `chat`. This applies to Virtual Agent support for mobile chat, web chat and IVR. This functionality enables you to create channel-specific responses within your virtual agents. For more information about channel-specific responses, see the [Dialogflow documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific).

Feature

**Campaigns, time zone management:** This release includes new time zone settings to simplify management of different time zones and calling time standards. You can now set up different time zone schemas and apply a specific time zone schema for each campaign. For example, you can use this feature to apply customized schemas to regions that have strict rules about when telemarketing calls are allowed. 

You can configure time zone settings at **Settings > Campaigns > Timezone Management**. See the [time zone list management documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Campaign_Management?_gl=1*ukvdod*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMTk3Mjc4Ni4zNC4xLjE3MDE5NzMwNzMuMC4wLjA.#time_zone_list_management) for details.

Feature

**Campaigns, Do Not Call (DNC) list:** You can now create your own Do Not Call (DNC) list for campaign calls. You can enable the Company DNC at **Settings > Campaigns > Company Do Not Call (DNC) List**. The DNC list is managed using the dedicated DNC API endpoints. Depending on configuration the DNC list can block direct, manual, and outbound calls as well as outbound and scheduled calls created by the Apps API. See the [campaign management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Campaign_Management) and [Apps API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Apps-API/publication?_gl=1*1t4zfmy*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTcwMTk3Mjc4Ni4zNC4xLjE3MDE5NzI5MjcuMC4wLjA.#company_do_not_call_dnc_list) documentation for details.

Feature

**Kustomer bi-directional agent status:** The Kustomer integration now offers bi-directional agent status syncing.

Fixed

CCAI Platform has added a fix for when the merge recording feature isn't working as expected.

Fixed

CCAI Platform has added "Virtual Agent" tags and prefixes in CCAI Insights for all Virtual Agent conversations.

Feature

**Virtual Agent, signed and unsigned data parameters** : You can now pass signed and unsigned (secured/unsecured) data parameters for Virtual Agent calls and chats using Mobile SDK in addition to the Web SDK.

Feature

**Pass voice and chat channel parameter to Virtual Agent:** Virtual Agents can now pass channel-specific parameters to CCAI Platform when invoking an Dialogflow Agent. This update applies to Voice Virtual Agents in IVR and Mobile channels. See the [ data parameters documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters) for details.

Feature

**Localization country code setting for calls:** A country code based on outgoing or dialed number has been added to the **dial dialog** and **add party dialog**.

## October 17, 2023

Announcement

**Release 3.2**

All release notes published on this date are part of the 3.2 release.

Feature

**New language support** : Polish, Czech, Australian English, Hungarian is now supported for all channels. You can set up these new languages on the **Settings > Languages & Messages** page. See the [language support page](https://docs.cloud.google.com/contact-center/ccai-platform/docs/languages) for a complete list of supported languages.

Feature

**Call management: Agent status breakthrough** : New feature Agent Status Breakthrough is now available. This feature allows you to to route incoming calls to agents, even when they are in a status that traditionally did not support receiving calls. This setting can be enabled at **Operations Management > Agent Status**. To designate a status as a breakthrough status, use the **Edit** function in the **Agent Status List**. The breakthrough status feature can be configured at the queue level as well as for specific DAPs. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management#agent_status_breakthrough) for details.

Feature

**Kustomer API rate limit improvements** : The API rate limits for customers integrating with Kustomer have been improved. see the [Kustomer documentation](https://help.kustomer.com/api-rate-limits-Sk2xoQgYX) for more information.

Feature

**Voice Virtual Agent assignment, transfers to parent queue** : You can now assign voice Virtual Agent transfers to top-level queues. In the IVR, the end-user will hear all of the sub and leaf queue options below the top-level queue as long as they are active. See the [Virtual Agents documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent#assign_voice_virtual_agent_transfers_to_top-level_queues) for details.

Feature

**New permissions added to call recordings and chat transcripts** : A new role permission `External Storage` is now available. This role offers you the ability to define whether users should have access to call recordings and/or chat transcripts when they are stored in external storage and without a CRM. When inactive, users won't be able to access these files from either the Completed Calls or Chats monitoring pages or associated downloadable reports. Shared links to these files fall under the same permissions. See the [Agent & team configuration](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent___Team_Configuration) page for more information.

Fixed

Fixed an issue where disabled Agent Statuses were still visible to custom roles.

Fixed

Fixed an issue where agents were not moving into wrap up status after completing transfer to a queue with a Virtual Agent assigned to it.

Feature

**Custom Notification Tones** : You can now upload custom audio files for incoming call and chat notifications, as well as new chat messages. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-messages-notifications#custom-notification-tones) for details.

Fixed

When an outbound campaign call fails during auto-dial due to telephony issues, the agent will now move into Available status rather than Wrap-up.

Feature

**Call recording: Third party recording without agent** : You can now record calls if an agent leaves after adding a third party. This can be configured at **Settings > Calls > Call Details > Call Recording**. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features#call_recording_third_party_call_recording_without_agent) for details.

Feature

**Virtual Agent pass data parameters updates** : CCAI Platform has enhanced the ability to pass session-based contextual data to Virtual Agents (VA). You can now leverage valuable real-time information during call routing and Dialogflow sessions. The following dynamic parameters are now available: DNIS / TFN (the number the user dialed), Latest Agent ID, Latest Agent Email, Queue Language, Latest Sentiment Score, and Overall Sentiment Score. Additionally, you can now configure static or dynamic CCAI Platform metadata parameters at the mobile queue level. See the [data parameters page](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters#pass_data_parameters_to_virtual_agents_and_task_assistants) for details.

Fixed

Fixed an issue where agents were seeing calls on the **Calls > Connected** page that were disconnected. Calls in which no participant is detected as active will now be automatically cleared and finished.

## September 25, 2023

Change

External Authentication/Single Sign On (SSO) has been removed from the CCAI Platform Portal and are now available in the [CCAI Platform Console](https://ccai.cloud.google.com/platform/projects). For details, see the [Create a CCAI Platform instance](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started#create_a_ccai_platform_instance) documentation.

Feature

**Assign virtual agent transfers to the top-level queue** : You can now assign a virtual agent to transfer to a top-level queue. The virtual agent will navigate consumers through any active sub and leaf queue options. If a top-level queue has no available leaf queues or is incorrectly configured, the IVR fallback will redirect the caller to the previous queue (if human agents are available) or provide an error message before disconnecting (if the top-level queue has no available agents).To enable this feature:

  * Enter the top-level queue ID in the Dialogflow destination (you can find parent queue IDs in the Virtual Agent queue menu settings).
  * Ensure all sub and leaf queues are active.



Feature

**Chat API suite** : A new set of APIs are now available that allow you to customize your chat experience. As a part of this feature, webhooks are available for receiving notifications about events that occur during the chat interaction. You can enable and manage them in **Developer Settings > Webhooks**. The new chat endpoints allow you to:

  * Create a chat, send and receive plain text messages, and end the chat with both agents and virtual agents.
  * Exchange messages with media attachments such as pictures, videos, and documents.



Feature

**NICE QM integration** : CCAI Platform now supports an out-of-the-box data export for NICE QM. You can enable this feature in **Developer Settings > Session Data Export > NICE Integration**. The following information is required to enable the NICE QM data export:

  * NICE API Endpoint
  * API Authentication credentials



After the integration is enabled, you can enable session data related to IVR call events and agent login/logout events in your NICE integration.

Feature

**Apps API: Change agent status** : Two new endpoints are now available to manage agent statuses:

  * `GET /apps/api/v1/agent_statuses`: Retrieve current agent statuses.
  * `POST /apps/api/v1/agent_statuses`: Update/change an agent status.



These endpoints allow you to modify agent statuses. You can change an agent's status from `Available` to any custom status and vice versa. Attempting to change an agent's status to a system status, such as `In-Call`, will result in an error. Similarly, attempting to change an agent's status from any system status will prompt an error message. These endpoints support bulk status updates, allowing you to update statuses for an entire team or selected agents simultaneously.

Feature

**Mobile release 2.2**

  * **iOS and Android SDK content cards** : You can use content cards to deliver specific messages to end-users during virtual agent chats. Content cards have customizable components including titles, text, carousel messages, banners, and much more. You can also embed a link that the end-user accesses when they click on the card. For example, if you have a list of restaurant options, you might create a content card for each one with a deep link that brings the user to the restaurant's website when they click.

  * **iOS SDK, improved accessibility** : The mobile iOS SDK now fulfills the following Web Content Accessibility Guidelines (WCAG) criteria for improved accessibility:

    * _Identify Input Purpose_ : Ensure that each input field is programmatically determinable, allowing users to autofill inputs.
    * _Identify Purpose_ : Ensure that the purpose of many elements on a page can be programmatically determined, making it easier for agents to extract and present the purpose to users using different modalities.
    * _Parsing_ : Ensure that there are no major code errors that affect accessibility so that agents can accurately interpret and parse content using assistive technologies. 
    * _Name, Role, Value_ : Ensure that assistive technologies can gather information about, activate (or set), and keep up to date on the status of user interface controls in the content. 
    * _Status Messages_ : Ensure that users of assistive technologies are notified when content is updated dynamically without receiving visual focus.
  * **Mobile bug fixes** :

    * Fixed an intermittent issue where quick reply buttons could be pressed outside their boundaries.
    * Fixed an issue where a virtual agent's avatar icon sometimes was not displayed alongside their message.



Feature

**ServiceNow enhanced capabilities** : This release brings new capabilities to the ServiceNow integration, including support for:

  * Default User: Reduced admin permission requirements.
  * More flexible field mapping and property assignment configuration options.
  * Support for new CRM features: 
    * Surveys
    * Agent Status inheritance
    * Custom Callback number
    * Improved support for OAuth authentication, for example now including admin tokens.



Feature

**POST events, chat message events** : Two new events added to the existing agent chat adapter events:

  * Chat Inbound Message: Event indicating that a new consumer message was received; includes the message content.
  * Chat Outbound Message: Event indicating that a new agent message was sent; includes the message content.



Feature

**ANI retention management** : You can now enable ANI storage by contacting Support.

Feature

**CRM record autoload** : A new setting is available to automatically update the CRM when an agent navigates between multiple active chats. This eliminates the need for the agent to manually search and load the corresponding CRM record each time they switch between chats. To enable this setting, go to **Settings > Chat > Global Settings > Global Chat Settings** and select the following checkbox: **Automatically load CRM Record when switching between chat tabs**.

Feature

**Restrict international calling by area code, short code, phone number** : The international calling configuration now includes the option to limit calls by area code, short code, and phone number. You can extend this configuration to a specific agent or have it applied as a rule to all agents.

Feature

**New permissions added to historical reports** : You can now limit access to `assigned teams only` or `assigned queues only`. For example, if you apply the `assigned teams only` permission option, only data for agents on that user's team(s) will be downloaded. There is also a new permission that allows Admins to manage who has access to the Session Data report, in addition the `assigned team only` permission.

Feature

**MS Dynamics, object type Contact** : You can now populate different fields on a "Case" object, when a "Contact" Object Type is used. The default action within MS Dynamics is to fill in the customer information only when a Case is created. This updated setting allows the contact field to be populated with the customer information from a Contact object at the same time. To enable this feature navigate to Developer Settings to access your MS Dynamics configuration. In the **Account Lookup** settings, select **Contact** under **Object Type**.

Feature

**Missed chat / Unresponsive status (while in-chat)** : Improved handling of agent statuses when a session cast to an agent fails due to network issues.

  * When a chat/call is cast to an agent but fails due to network or permission issues, the agent's next status will be moved to `Unresponsive` regardless of the status they're currently in.
  * If a call/chat is cast to an agent but the agent fails to pick up, the agent's next status will be moved to `Missed Chat` status regardless of the status they're currently in.



Feature

**Disable Whatsapp for CCAI Platform** : The Whatsapp flag for CCAI Platform is disabled until we have OEM compatibility for Whatsapp.

Feature

**Call settings, post-call session transfers** : You can now set up a cold transfer to a virtual agent at the end of a call. This configuration allows you to set up an automated workflow, such as a post-call survey. To enable this feature, go to **Settings > Call Settings** and toggle the **Post-call** session transfers to **ON**.

Feature

**Permission for access to call recording/chat transcript files** : A new role permission allows you to define whether users can have access to call recordings and/or chat transcripts when they are stored in external storage and without a CRM. When inactive, users won't be able to access these files from either the Completed Calls or Chats monitoring pages or associated downloadable reports. Shared links to these files fall under the same permissions.

Fixed

Fixed an issue that occasionally caused the _Queue Structure Edit_ page to jump places.

Fixed

Fixed an issue where a holiday was not respected by queues if it was configured to be observed on the last occurrence of the month.

## August 21, 2023

Feature

**UCaaS: MS Teams integration** : CCAI Platform now supports UCaaS integration capabilities. This integration allows you to seamlessly configure MS Teams users and teams directly within CCAIP. You can enjoy the advanced routing capabilities of CCAIP while taking calls in MS teams. Typical supported use cases include:

  * The ability to transfer calls between CCAIP and MS Teams agents.
  * Automatically routing calls to MS Teams agents or groups.
  * Assigning any MS Teams users to queues.
  * Ability to assign CCAIP and MS Teams users as part of Cascade groups.



In Add/Edit User menus, you will see an option for enabling UCaaS as well as integration settings in Developer Settings. Enabling this option allows users who only occasionally assist with customer support to take those calls using their principal UCaaS communication platform. For details, see the [Microsoft Teams integration guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ms-teams-integration)

Feature

**Mobile SDK 2.1: UI customizations** : The latest release of our Mobile SDK chat gives you even more customization options to tailor the UI to your specific branding needs. You can take full control of the appearance and style of elements within the chat interface. Some items that can be fully customized:

  * Agent and consumer message bubbles.
  * Menu bar (including the back and end chat buttons).
  * End Chat button.
  * Send button.
  * Message tray.
  * Time stamps.



Depending on the component, you have the flexibility to customize attributes such as the font, background color, icon, (and more!) to create a chat experience tailored to your brand. See the [iOS](https://docs.cloud.google.com/contact-center/ccai-platform/docs/iOS_SDK/publication--en) and [Android](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Android_SDK/publication--en) SDK guides for details.

Feature

**Data restriction for historical/downloadable reports** : New permission for the Session Data report with the supervisory ability to restrict editing permissions. Also, the permissions for the downloadable reports under Agents & Teams, Calls & Chats, Queues, and Campaigns now have the option to restrict the corresponding data to `assigned teams only` or `assigned queues only`.

Feature

**Session Variable: Enable Agent ID as a dynamic parameter** : We have introduced a change to dynamically include the agent ID as a session variable in automated messages and chat shortcuts. This allows an agent to send an outbound SMS to a consumer containing a deep link to a mobile app with our SDK embedded. The deep link contains the agent ID, which will trigger a DAP to a dedicated queue for that agent with a DAP value also reflecting that agent's ID. Scope extends to these channels: SMS messages, Mobile chat, Wed SDK chat, Chat shortcuts.

Feature

**Headless web SDK** : CCAIP Platform now supports a new Headless Web SDK, designed to empower you to build a fully customized and branded web support experience.

The Headless Web SDK comes equipped with a comprehensive API suite, providing you with the tools to leverage familiar Web SDK features and tailor the UI to suit your specific needs. Every detail, from colors and fonts to layouts and interactions, can be tailored to create a cohesive and engaging interface that resonates with your audience. See the [Headless web SDK guide](https://docs.cloud.google.com/contact-center/ccai-platform/docs/headless-web-guide?_gl=1*2y8jdg*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTY5Njk1MDA4MS4yOS4xLjE2OTY5NTA0NzUuMC4wLjA.) for details.

Feature

**Fallback IVR: Additional settings for fallback destination** : New IVR fallback options for when an end-user fails to select a queue during IVR navigation. New options are available globally as well as at the queue level. Additional options include:

  * Select the last available menu to route consumers to the last queue in the IVR menu.
  * Select a specific menu to route consumers to any queue in the IVR menu.



The configuration options are available at the global level (Call > Call Details > Fallback IVR Navigation). See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#custom_fallback_ivr_at_the_queue_level) for details.

Fixed

**Web SDK** :

  * Fixed an issue where the Co-browse session sometimes would not connect due to the end-user having multiple tabs open. 
  * Fixed an issue where end-users could sometimes get stuck on the After Hours screen, unable to start a new chat. 
  * Fixed an issue where a DAP was sometimes not maintained after the previous chat timed out.



Feature

**NICE QM integration** : CCAIP now supports an out-of-the-box data export for NICE QM. You can enable it in Developer Settings > Session Data Export > NICE Integration. You must enter the following information to enable the NICE QM data export:

  * NICE API Endpoint
  * API Authentication credentials



Feature

**Call Adapter: Improved error codes and messages** : We have improved our Call Adapter's error messages with more detailed content, including error codes and explanations.

Feature

**Improved Outbound SMS API** : Agents can now initiate outbound SMS sessions with number pairs that were previously engaged by other agents. This enhancement allows for seamless continuation with consumers, even if the number pair was recently used by a different agent. Agents can send appointment requests, SMS follow-ups, and other SMS messages without encountering errors. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/SMS?_gl=1*hk46ke*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTY5Njk1MDA4MS4yOS4xLjE2OTY5NTA3NTcuMC4wLjA.#UUID-deaac933-cb96-01de-a409-b74a4cafb35d_id_4408147882777_id_h_01FJMMYQRZ5SDZSQSD23H1QMKN) for details.

Feature

**Call Session Events generator and sender** : These applications are deployed when you enable the Call Session Events feature. The operators receive Call Events from `ujet-server` and process them before sending to your configured endpoints. `Ujet-server`, Generator and Sender all use RabbitMQ infrastructure to send messages.

Feature

**Custom POST events (also known as custom JavaScript events)** : This feature allows you to listen for events happening within CCAIP and take action accordingly. For example, when a call is transferred you could use your own JavaScript code to listen for a `call_transferred` event and specify actions based on the provided parameters (such as updating the destination agent's screen). These events give you more control over your workflows and allow for seamless integration with your business processes. With this release we are extending the existing mechanism of transmitting post events with 3 new events:

  * Transfer
  * Add Party
  * Agent connects to session
  * VA session data: We are capturing VA session data in the payload during a consumer interaction. This means alongside the existing event data, you will now have access to virtual agent session specific variables.



In addition, we're including:

  * The `agent_custom_id` parameter in the `Agent_Login` event. 
  * Custom SIP headers in incoming SIP calls within the POST events.



See the [custom CRM documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM?_gl=1*1apdbl7*_ga*NzkyNTU2NzEzLjE2OTI3MjU4NTI.*_ga_4LYFWVHBEB*MTY5Mjg5MDQxOC4yNS4xLjE2OTI4OTEwNDAuMC4wLjA.#data_for_events) for details.

Feature

**Skip Cascade Group Timer** : Improved functionality of our call and chat deltacast routing. We have introduced the Skip Cascade Group Timer setting, which allows you to bypass the cascade timer settings and route a call or chat to the next available agent, regardless of the cascade group. The setting is located in Operations Management > Deltacast settings. See the [Operations Management documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Operations_Management?_gl=1*1lims1n*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTY5Njk1MDA4MS4yOS4xLjE2OTY5NTAzNTAuMC4wLjA.#chat_routing_multicast_and_deltacast) for details.

Feature

**New dynamic parameter support for SIP redirect and Dialogflow** : New dynamic parameters to enhance the capabilities of SIP Redirect and Dialogflow. With these additions, you can now leverage valuable real-time information during call routing and Dialogflow sessions. The new dynamic parameters include DNIS / TFN (the number the user dialed), Latest Agent ID, Latest Agent Email, Queue Language, Latest Sentiment Score, and Overall Sentiment Score. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters?_gl=1*av5ip1*_ga*MTg4NzYwNjk1My4xNjM1NDUyMDgy*_ga_4LYFWVHBEB*MTY5Njk1MDA4MS4yOS4xLjE2OTY5NTA2MjcuMC4wLjA.#add_a_dynamic_parameter_from_ccaip_metadata) for details.

Feature

**DAP: Additional format** : Previously limited to E164 formatted numbers, we now support the input of SIP phone numbers in the incoming sip address format: sip:[number]@[domain].

Fixed

Fixed an issue where if a trailing "/" was added to the folder path for Google Cloud Storage upload settings, the files were written to a folder with no name. A safeguard has been added both in backend and frontend to remove any trailing slashes.

Feature

**Distinct queue names for the Alvaria data exporter** : You now have the ability to repeat names across multiple different queue-paths. Queue will appear in Alvaria as Queue Name - language code - ID, allowing you to easily identify which metrics correspond to what queue.

Fixed

**iOS** :

  * Fixed an issue where using a DAP to route to a queue that was After Hours could lead to consumers being stuck in a loop.
  * Fixed an intermittent issue where a SmartActions request would cause the app to crash.
  * Fixed an intermittent issue where the SDK credentials would not authenticate.
  * Fixed an issue where the app would crash when hold music was played to the end-user.



Feature

**Call Handling: Hold music during connection** : CCAI Platform has enhanced the call handling experience for end-users by ensuring a smoother transition when connecting with an agent. Instead of experiencing hold music followed by delays or silence, end-users will now enjoy uninterrupted music until the agent joins the call. Additionally, agents will be notified with a distinct sound when an end-user joins the call.

Fixed

**Android** :

  * Fixed an issue where using a DAP to route to a queue that was After Hours could lead to consumers being stuck in a loop.
  * Fixed an issue where the signed custom payload data was not triggered for calls and chats.



Fixed

**Billing service fixes** : Resolved two different incident tickets relating to the billing service; one edge case whereby agents were erroneously being counted as online and other that caused the billing service to temporarily incorrectly aggregate data.

## August 09, 2023

Feature

**Enhanced international calling configuration** : You can now configure international calling for each phone number at the country code level by using the Phone Number Management settings. After the international calling is configured, you can manage user-level access. An error message will appear in the Agent Adapter if the agent dials a restricted number. For details, see the [Phone number management](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Settings_and_Features#allowdeny_international_calls) and [Add and view users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent___Team_Configuration#add_and_view_users) documentation.

Fixed

Fixed an issue where the `Agent_Login` message event (supposed to be raised when an agent logs in) was not happening.

Fixed

Fixed an issue where when a manager/ admin tried to monitor or barge into a call for a second time, they received a 400 error "You are already in this call".

Fixed

Sessionless SMS implementation is now updated to support A2P 10DLC compliance requirements. The update ensures SMS sent via Session SMS APIs will not encounter any unexpected blockage.

Fixed

Fixed an issue where some page category names were displayed to users in the collapsed navigation menu even though they didn't have access to any pages within that category.

Fixed

Fixed an issue where some pages were not visible in the collapsed navigation menu.

Feature

**Outbound Dialer list management using the API** : You can now manage your campaign contact lists within our outbound dialer using your own software application. You can programmatically add, remove, and update contact information in your campaign lists using the [List Management API](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Manager-API/publication). This feature allows seamless integration between your software and our system, programmatic control using the API, and efficiency by automating list management tasks.

## June 30, 2023

Feature

**ServiceNow** is now available as a native, fully integrated CRM, providing a more efficient and streamlined configuration process that includes embedded agent adapters. Previously, ServiceNow could only be integrated using the Generic API Custom CRM solution. For details, see the [ServiceNow integration documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/additional-integrations#servicenow_crm_integration_guide).

Feature

**External Storage dynamic folder path and filename formats** : CCAIP offers this new capability for the External Storage configuration feature. Dynamic folder path and filename formats offer more flexibility for storing your call recordings, chat transcripts, voicemails, photos, videos, and co-browsing files. You can now include run-time variables like {DATE}, {SESSION_ID}, and {SESSION_TYPE} in the path and configure custom filename formats with sub-paths. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes/) for details.

Feature

**Alvaria WFM integration** is now available as an out-of-the box data export. You can enable it using **Developer Settings > Session Data Export > Manage Data Export Settings**. You have the option of exporting either a _basic session data report_ at intervals of 15, 30 or 60 minutes, or a _daily agent productivity report_. The reports can be delivered to either a Google Cloud or Amazon S3 storage bucket.

Feature

**Call recordings separated by segments** : You can now choose to receive one recording per call segment instead of all call segments in a single recording. Separate call recordings allow more flexible call analysis and more efficient issue resolution. See the [Queue and menu settings documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/release-notes/) for details.

Fixed

Resolved an intermittent issue that allowed a call to be transferred to a queue during hours that it should not have been available.

Fixed

Resolved a bug that caused the **custom holiday** feature to throw a "Can't create root directory" error and not be able to save or create holidays.

## June 16, 2023

Feature

CCAI Platform now supports the CCAI Insights feature. You can use CCAI Insights to detect and visualize patterns in your contact center data. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/ccai-insights) for details.

## May 25, 2023

Feature

Contact Center AI Platform now supports **Agent Assist Session Summarization**. This feature automatically provides a summary of the conversation transcript at the end of a chat or phone call. The summary includes brief overview of the conversation, key discussion points and resolutions or solutions agreed upon. For more information, see the Agent Assist [voice](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent_Assist#session_summarization) or Agent Assist [chat](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Agent_Assist#session_summarization_2) documentation.

## May 16, 2023

Feature

**SIP URI Directory - Call Routing** : With this release, you can now use the SIP Directory to configure SIP call routing and transfers in IVR queue settings. You can use this functionality to route incoming calls to appropriate destinations based on IVR menu selections or queue routing rules. You can set it up so that a customer calling a support line, for example, can select a department or agent from the IVR menu based on their inquiry. See the [SIP URI documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#sip_uri_directory) for details.

## May 12, 2023

Feature

**Unified Session Types** : The new session type variable, Session Type V2, is now available. This update introduces a range of new fields, variables, and columns that will provide you with access to valuable additional information such as the ability to distinguish between Inbound SMS, Outbound SMS, and Outbound SMS via API. For more information, see the [session type terminology](https://docs.cloud.google.com/contact-center/ccai-platform/docs/session-type-terminology) documentation.

To take advantage of the new fields and variables, you will need to update your scripts, code, automation triggers, and any third-party integrations. The legacy components will no longer be updated with new functionality and will be deprecated on **October 6, 2023**.

Feature

**Holiday hours** : With Holiday Hours, you now have the ability to create and manage your own set of holidays with complete control over the holiday name, time, and dates. Additionally, you can group your holidays together for easier management. See the [holiday hours documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Support_Center_Details) for details.

Feature

**Campaign Management: Outbound Number** : Outbound Number is a new feature for the Outbound Dialer that allows you to specify which outbound number to use when dialing out for each contact. With this new feature, you can rotate outbound phone numbers to have more control over the outbound phone numbers you use to make your outbound calls. For more information, see the [Outbound Number documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Campaign_Management#outbound_number).

Fixed

Resolved an issue with incoming calls not ringing for agents who have the Adapter tab in the background on Chrome. Now a chime sound is played when the agent switches to the Available status, which will allow the Adapter tab to play sounds while in the background. This ensures that incoming call notifications will be heard even if the agent has the tab in the background.

Fixed

Resolved an issue where if queue priority was enabled, then chat settings were not populated.

Fixed

Fixed unexpected newline characters in admin notification emails.

Fixed

Fixed an issue where when using the outbound call API to start a call, the call adapter would display the mobile SmartActions menu instead of the Start SMS option.

Fixed

Resolved an issue with Manager API endpoints returning "Internal Error".

Fixed

Fixed an issue where agents changing their status from Meeting to Available would not receive campaign calls, requiring the campaign to be paused and restarted. Now campaign calls are received without interruption.

Fixed

There were certain scenarios where frontend was showing `support@ujet.cx` email. This was updated to accept any string to support email branding and display it. For example, the string should change from "Please try again or contact `support@ujet.cx` for more help" to "Please try again or contact Company X for more help".

Fixed

Fixed an issue with chat escalations to a human agent, ensuring session variables are successfully posted to the CRM ticket, as configured in **Settings > Operation Management > Virtual Agent**.

Fixed

To address SSO management issues with various customers in CCAIP, we moved the setting of the SSO values into the create-company rake task which makes sure we only set this when we first create a tenant project. This value is set to allow customers to change their own SSO settings.

Fixed

Resolved an issue where the Target Pick Up Time under **Settings > Operations Management** was not updating in the Agent Adapter when receiving a call.

## April 27, 2023

Feature

**Custom CRM Virtual Agent transcripts** : We have updated our Custom CRM to allow Virtual Agent transcripts to be sent to your external storage. To enable this, go to **Developer Settings > External Storage** and select **Call Transcripts** (currently only supported for Agent Assist and Virtual Agent transcripts). The transcripts will be sent to your external storage. This feature allows the team managing your virtual agent(s) to review and analyze the conversations your virtual agents are having with your consumers, identifying areas for improvement and helping you evolve your virtual agent(s). In addition, VA transcripts can help businesses comply with regulatory requirements by maintaining a secure record of all consumer interactions.

For more information on Custom CRM see the [Custom CRM documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM).

Feature

**Campaign Management** : You now have the option to add a Unique ID column to your campaign management CSV upload. This ID can be any identifier of your choice, such as a CRM identifier or a SKU. This field allows you to associate your CRM data with each dialer call, providing a comprehensive view of your call data. You can view the Unique ID data in Standard Reporting Campaign reports. For more information see the [campaign management documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Campaign_Management#add_a_unique_id_for_campaign_reporting).

Feature

**Voice Virtual Agents** now has the ability to transfer a call to a specific phone number or SIP endpoint, ensuring that the consumer is connected to the appropriate person or department. For more information, see the [Virtual Agents custom payload documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent#va_transfer_to_phone_or_sip_endpoint).

Change

**Enhanced file storage options for custom CRM** : The process of uploading files has been simplified by separating the external storage upload from the endpoint validation. Before this change, uploading files to external storage required both the `Update a record` and `Upload a file` endpoints to be configured and files still underwent CRM validation.

Now, you can upload files to external storage even if the endpoints aren't set up, as long as external storage is configured. If both endpoints and external storage are configured, files will be sent to both.

For more information on Custom CRM see the [Custom CRM documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM).

Feature

**New Manager API`calls` endpoint fields**: We have added additional data to the `/manager/api/v1/calls` endpoint to provide more options for reviewing and analyzing campaign call status data. New fields include `Machine Detected` and `Skipped` information.

## April 25, 2023

Feature

**Queue-level wrap-up settings** : You can now customize wrap-up times for different queues, to ensure that agents have adequate time to complete their tasks without compromising service level agreements or taking another call/chat before they are ready. This is particularly useful for queues that handle escalations or complex issues, which may require more time to handle. See the [Queue and Menu Setup documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#queue-level_wrap-up_settings) for details.

Fixed

We have updated the **Calls > Queued and Chats > Queued** monitoring pages to retrieve data from the past 24 hours instead of only the current day. This update ensures consistency with the real-time queue metrics displayed on the Call and Chat dashboards, which also reflect the last 24 hours.

Feature

**Custom CRM background screen pop for embedded adapters** : We have improved the screen pop capability for our Custom CRM to better support embedded adapters. We now provide a way to do a CRM screen pop in the background, allowing for a smoother experience when using embedded adapters. For details, see the [Custom CRM documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Custom_CRM#background_screen_pop).

Fixed

We have fixed an issue that caused OEM Billing Service to take very long execution times (more than 4 hours) while executing 2.sql , after which our MySql server killed the query.

Fixed

Fixed a bug where some VA responses that should not be bargeable could be barged in to. There was a timing issue between parsing whether a response is bargeable and starting a new SAC stream, so some responses used the preceding response barge config instead of their own. This has been corrected to make sure the correct order of operations is always followed for this flow.

## March 14, 2023

Feature

**Twinning** : Twinning is a new feature that allows a primary extension (for example, web adapter) and a secondary extension (for example, mobile phone number) to operate as a single phone.

Twinning is ideal for support agents who are frequently on the go, since it allows them to forward support calls to their preferred phone number while also allowing them to handle calls at their desk using their web adapter. Another example is a front desk phone set up as the office's primary extension; you can use Twinning to forward those calls to a mobile phone.

For details, see the [Twinning documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Call_Routing#twinning)

Feature

**Dialogflow (DF) Wrap-up events** are now captured as custom events. Every time a customer ends their session with a Virtual Agent for any reason (for example, consumer abandon, call failure), a new DF Wrap-up custom event is sent to the Dialogflow CX (for example, handled by VA). This enables the VA to react to the event and perform any desired session wrap-up process(es). For more inforation, see the [Dialogflow documentation](https://docs.cloud.google.com/dialogflow/es/docs/events-custom).

Feature

**New data parameters for Virtual Task Assistant** : Virtual Task Assistant now has the ability to send parameters, supports multiple languages, and includes a dedicated settings panel. Admins can now specify the data parameters that can be gathered and sent to Virtual Task Assistants, including the new dynamic parameter `Agent Form`. See the [data parameters documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Pass_Data_Parameters#pass_data_parameters_to_virtual_agents_and_task_assistants) for details.

Feature

**Salesforce multi-number lookup** : You can now configure CCAIP to look up an account across multiple phone number fields in Salesforce. This makes it easier to connect different support sessions to a single account for consumers who have multiple phone numbers, such as mobile, home, or work numbers. Additionally, you can now assign all phone numbers to one account rather than having to set up separate contacts for each number. The Account Lookup section now offers the following settings:

  * **Phone number lookup fields** : This updated configuration enables you to select multiple phone numbers, such as mobile, account phone, account fax. You can then associate these numbers with the same account.
  * **Phone number primary fields** : This field enables you to select the phone number field to be used when you create a new CRM account.



For more information, see the [Salesforce CRM documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Salesforce#account_lookup_against_multiple_numbers).

Feature

The CCAIP integration with Kustomer now offers the following new custom enhancement options:

  * Call transfer information is now posted as a comment. 
  * Administrators can now create custom fields from CCAIP.
  * Administrators can now create custom Account and Record fields by going to: **Developer Settings** > **Custom fields** for Account and Record. See the [Kustomer documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Kustomer#create_custom_fields) for details.



Feature

**Domain Based Access Control** : You can configure CCAIP to restrict the set of domains able to frame the agent adapter and admin portal. This provides protection against clickjacking attacks.

An Admin can configure the domain allowlist by going to: **Developer Settings** > **Domain Based Access Control**. Configuration changes might take up to 1 minute to take effect.

Existing customers will have an empty allowlist by default. To enable this feature, the allowlist must be populated with each domain currently framing the agent adapter. Domains that are not configured will be blocked. New customers will have an allowlist containing the domain of the CCAIP instance itself to allow the agent adapter to be framed by the admin portal. Additional domains will be blocked from framing the agent adapter until they are configured in the allowlist.

See [Domain based access control](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#domain-based_access_control) for details.

Change

**Agent Adapter Improvements** :

  * Updated active state styling of the in-call buttons (for example, **Mute** and **Hold**) to provide agents with greater clarity when the buttons are in an active state.
  * The in-call button labels no longer update when you toggle between the active and inactive state. **Mute** and **Hold** no longer update to "Unmute" and "Pause" respectively.
  * Improved color contrast ratios of the following UI elements for better legibility: 
    * The **Logout** button.
    * The **Save & Close** button during the Wrap-up phase.
    * The **Wrap-up Exceeded** informational text.
    * The tabs in the chat overview list.



Feature

A new audio chime has been added to the Agent Adapter to indicate when an agent connects with a customer on a call. We also updated the existing audio chimes for these events:

  * Agent joins
  * Member joins 
  * Call Disconnects
  * Member Leaves



Fixed

We resolved an issue in the **Queue** settings where the menu numbers on a queue continued to display even when the queue setting was set to _Hide_.

Feature

**Custom CRM, Extended OAuth and nested parameter support** : The following enhancements have been added to the Custom CRM integration offering:

  * Extended OAuth Authentication support.
  * Handling nested parameters in the API endpoints configuration.



Change

**Co-browse disabled** : We have disabled and removed references to Co-browse functionality while the feature undergoes internal review/approval.

Fixed

We resolved an issue where chat shortcuts were not appearing consistently in the Agent Adapter.

Fixed

Fixed an issue where the ringtone would sometimes not play in the preview dialer.

Feature

**MS Dynamics: Updated default user functionality and improved Virtual Agent record assignment** : You can now assign a CRM Admin user as the default user for all CRM actions and events where no specific agent has been identified. After enabling this **Default User** option in **Developer Settings** , you can set the default user for all Customer Support Virtual Agent sessions as well. See the [Virtual Agent documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent#set_a_default_user_for_virtual_agent) for details.

Feature

DTMF Support Capability You can now select the DTMF checkbox during Virtual Task Assistant and [Virtual Agent](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent) setup to ensure that DTMF tones are supported.

## October 21, 2022

Feature

Agent Assist conversation profile settings are now configurable at **Developer Settings** > **Agent Assist Platform**. See the [documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#UUID-4976e24e-21d5-bf58-960a-7333bec9a170) for details. From here you can:

  * Onboard new Agent Assist profiles.
  * Edit or remove existing Agent Assist profiles.
  * View the current status of a linked profile.
  * View a list of configured conversation profiles.



Feature

Secure Payments: We now offer Braintree as a secure payment option in addition to Stripe and FreedomPay. There are also new improvements to the secure payments configuration (**Developer Settings** > **Credit Card Payment Providers**) and the agent experience:

  * The payment provider settings have been updated with new dynamic fields for entering credentials once the payment provider has been selected in the **Type** drop-down.
  * The agent adapter now has a **Currency** drop-down menu. 
  * For more information see the [Secure Payments](https://docs.cloud.google.com/contact-center/ccai-platform/docs/secure-payments-add-providers) documentation.



Feature

We've made the following updates to [Virtual Agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Virtual_Agent):

  * You can now onboard and use the Dialogflow Agents configured for the `global` region using the Dialogflow CX platform.
  * We now support Virtual Agent Dialogflow Barge-in through Dialogflow CX (Voice). See [Add a Virtual Agent platform](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#UUID-cfbc48d7-033f-3887-a3eb-9fb2c8b5e9d4) for details.



Feature

Secure Payments: Multi-currency payment options are now available for Stripe and Braintree. Along with USD, you can now select from the following international currencies:

  * British Pounds (GBP)
  * Euros (EUR) 
  * Canadian Dollars (CAD)



For more information see the [multi-currency documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/secure-payments-add-providers#UUID-94947d0e-feb0-d64c-d268-eadea6d78a64_id_115012393208_id_h_01EQGGW8S4MW1V86GCT4SXNJ73).

Feature

[Bring Your Own Carrier (BYOC)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Developer_Settings#UUID-2349134b-ea48-45bf-60b2-acee20b88f94): You can now bring your own phone numbers through your carrier.

Feature

Dual Channel Recording - You can now enable [dual channel audio recording](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup#UUID-390c8251-c50f-0351-77c7-d2655ceed7d8). When enabled, your calls will be recorded in two separate channels, for example a customer channel and an agent channel.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
