---
url: https://docs.cloud.google.com/dialogflow/docs/release-notes/
title: Dialogflow release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:14.719196+00:00
---

# Dialogflow release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Resources ](https://docs.cloud.google.com/dialogflow/docs/resources)



Send feedback 

#  Dialogflow release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Dialogflow CX (and Dialogflow ES). We recommend that Dialogflow CX developers periodically check this list for any new announcements. Major changes will also be announced via [Cloud Blog: AI & Machine Learning](https://cloud.google.com/blog/products/ai-machine-learning).

**Note:** You can also read the [historic release notes](https://docs.cloud.google.com/static/dialogflow/docs/data/historic-release-notes.pdf) prior to November 16, 2017.

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/dialogflow-release-notes.xml) directly. 

## October 19, 2026

Feature

**Dialogflow CX** : You can set the `telephony_disable_voice_processing` session parameter to `true` to turn off speech recognition and accept only DTMF input for the rest of the session. This helps in noisy environments, where speech recognition can transcribe background noise as end-user input. See [Turn off speech recognition for telephony](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#session-disable-voice).

## October 16, 2026

Feature

`gemini-3.5-flash-lite` has become generally available (GA). See [Generative quotas](https://docs.cloud.google.com/dialogflow/quotas#generative) for how to request quota for Gemini 3 and later models.

## September 30, 2026

Fixed

**Dialogflow CX** : An issue in Dialogflow CX was identified where sensitive authentication tokens stored in conversational session parameters could be returned in cleartext via `DetectIntent` API responses. A server-side fix has been applied to redact and sanitize authentication credentials from conversational API outputs. No customer configuration changes or updates are required.

Deprecated

**All generative features** : `gemini-2.5-flash` and `gemini-2.5-flash-lite` models will be deprecated by Dec 23, 2026. Upgrade to newer Gemini models such as `gemini-3.1-flash-lite` before the deprecation date.

Feature

[BidiStreamingAnalyzeContent](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#participants) API has become generally available (GA).

## May 07, 2026

Fixed

A Missing Authorization vulnerability in the playbook import functionality in Dialogflow CX on Google Cloud Platform allows an authenticated user with specific roles to escalate privileges and potentially take over a project using a maliciously crafted playbook import. This vulnerability was patched on 15 March 2026, and no customer action is needed.

## December 11, 2025

Feature

**Conversational Agents (Dialogflow CX)** : New _Responsible AI_ fields are now available for the [`v3`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#raisettings) and [`v3beta1`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#raisettings) API endpoints. Responsible AI allows you to flag, filter or block harmful content.

Security

**Conversational Agents (Dialogflow CX)** : Dialogflow CX Messenger [integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) contained a vulnerability that allowed for authentication bypass when an agent was configured to use an authenticated API with a 3rd party identity. **All versions released after August 20th, 2025 have been updated to protect from this vulnerability. No user action is required.**

Feature

**Conversational Agents (Dialogflow CX)** : Conversational Agents now supports log splitting for [large Cloud Logging log entries](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#logging-settings).

## November 13, 2025

Feature

**Conversational Agents (Dialogflow CX)** : [Regular expression validation (Regex)](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf) is now available in Agent Settings and Entity Types.

## November 06, 2025

Feature

**Conversational Agents (Dialogflow CX)** :You can now specify custom voice in the **Conversation profiles** menu in the console.

## October 23, 2025

Feature

**Conversational Agents (Dialogflow CX)** : You can now configure service account authorization for both tools and webhooks. See the [reference documentation](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#serviceaccountauthconfig) for details.

Feature

**Conversational Agents (Dialogflow CX)** : New fields `temperature`, `input_token_limit` and `output_token_limit` are now available for [`LlmModelSettings`](https://cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#llmmodelsettings) in the v3beta1 API. This allows you to adjust the model per playbook.

Feature

**Conversational Agents (Dialogflow CX)** :The [Block none](https://cloud.google.com/dialogflow/cx/docs/concept/agent-settings) safety feature in agent settings is no longer restricted access.

Feature

**Conversational Agents (Dialogflow CX)** : The **Entity Types** console menu now allows you to set a page size for entity entries and excluded phrases. Pagination options are automatically displayed if there are more than 10 items listed.

## October 16, 2025

Change

**Dialogflow CX (Conversational Agents)** : The default models for data stores and playbooks have been upgraded as follows:

  * Data stores

    * Default voice mode summarization from `gemini-2.0-flash-lite-001` to `gemini-2.5-flash-lite`.
    * Default text mode summarization from `gemini-2.0-flash-001` to `gemini-2.5-flash`.
    * Default text mode rewriter from `gemini-2.0-flash-lite-001` to `gemini-2.5-flash-lite`.
  * Playbooks:

    * All newly-created playbooks use default model `gemini-2.5-flash`.



Deprecated

**Dialogflow CX (Conversational Agents)** : The [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects) will be deprecated on **October 31, 2025**. After that date all users will be automatically routed to the [Conversational Agents console](https://conversational-agents.cloud.google.com/projects).

## September 04, 2025

Announcement

**Dialogflow CX (Conversational Agents)** : _This is a correction of the release note posted on[August 7, 2025](https://docs.cloud.google.com/dialogflow/docs/release-notes#August_07_2025)_. All deactivated models are now automatically upgraded to model `gemini- 2.5-flash` with the exception of **generative fallback** , which is automatically upgraded to `gemini-2.5-flash-lite`.

Feature

**Dialogflow CX (Conversational Agents)** : The following regions are now available:

  * `asia-southeast2`
  * `europe-west4`
  * `europe-west6`



Feature

**Dialogflow CX (Conversational Agents)** The [model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-2.5-flash-lite` is now available in all regions, and `gemini-2.5-flash` is now GA. These changes apply to the following features:

  * Generators
  * Playbooks
  * Data store tools



Feature

**Dialogflow CX (Conversational Agents)** : New prompt security controls are available in **agent settings**. See the [agent settings documentation](https://cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-generative-prompt-security) for details.

## August 07, 2025

Deprecated

**Dialogflow CX and Vertex AI** : The `gemini-1.0-pro`, `gemini-1.5-pro` and `gemini-1.5-flash` models will be deprecated on **September 1, 2025** and automatically upgraded to the `gemini-2.0-flash-001` model. This change applies to Vertex AI agents and the following Conversational Agents generative features:

  * Playbooks
  * Data stores
  * Generators
  * Generative Fallback



After the upgrade on September 1, 2025, `gemini-2.0-flash-001` will be automatically selected in the console. We recommend that you upgrade to the new model early to allow enough time for testing and to ensure that your solution works as intended.

## July 31, 2025

Feature

**Conversational Agents** : [Routine playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook#routine) are now generally available.

Feature

**Conversational Agents** : [Parameter passing](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/parameter#passing-parameters) is now available and documented between routine playbooks, task playbooks, and flows.

## July 24, 2025

Feature

**Conversational Agents** : 21 new [Chirp 3 HD voices](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) are now available across 34 locales.

Feature

**Conversational Agents data stores** : Conversational Agents now supports AlloyDB AI, Bigtable, Firestore, Spanner and Cloud SQL data store source as public GA features; Microsoft Entra ID source has now private GA support. See the [data store documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store) for a complete list.

## July 17, 2025

Feature

**Conversational Agents** : CMEK is now available in EU regions.

Feature

**Conversational Agents** : The [conversational history flow analysis feature](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history#flow-analysis-table) is now available.

Feature

**Conversational Agents** : The [model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-2.5-flash` is now available in all regions. This change applies to the following features:

  * Generators
  * Playbooks (Public Preview)
  * Data stores tools (Public Preview)



## June 26, 2025

Feature

**Conversational Agents data stores** : You can now create some data store types directly within the Conversational Agents console rather than needing to use AI Applications. See the [data store creation documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#data-store-console) for details.

Feature

**Conversational Agents data stores** : Conversational Agents now supports AlloyDB, Bigtable, Firestore, Spanner and Cloud SQL [data store sources](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#sources) as public GA features. Microsoft Entra ID source has now private GA support.

## June 12, 2025

Feature

**Conversational Agents** : New [Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) Cloud Text-to-Speech voice **Autonoe** is now available.

Feature

**Conversational Agents** : Conversational Agents console now supports [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case).

Change

**Data store handlers** : Data store handler use tracking for billing purposes has been corrected.

Announcement

**Conversational Agents** : Service agent access tokens used for authentication by both webhooks and tools are now discontinued as mentioned in notification emails to customers earlier this year. Most customers can use service accounts instead.

## May 01, 2025

Feature

**Dialogflow CX (Conversational Agents)** : [Models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-2.0-flash-001` and `gemini-2.0-flash-lite-001` are now GA. They are available in all supported regions.

This change applies to the following features:

  * Playbooks
  * Data store tools in playbooks
  * Generators



## April 24, 2025

Feature

**Dialogflow CX (Conversational Agents)** : You can now create personalized voice models with [voice cloning](https://docs.cloud.google.com/dialogflow/cx/docs/concept/voice-cloning).

Feature

**Dialogflow CX (Conversational Agents)** : You can now use the console to [test your tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#testing).

Feature

**Dialogflow CX (Conversational Agents)** : You can now use [code blocks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/code-block) to get better control over playbooks.

## April 01, 2025

Feature

**Dialogflow CX (Conversational Agents)** : **Data store tools** no longer require the use of a playbook and can be used with any agent. For information about configuring data store tools for a flow-based agent, see the [data store tools documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler).

Change

**Dialogflow CX (Conversational Agents)** : The `gemini-1.0-pro` model is deprecated as of March 24, 2025 and has been automatically upgraded to the `gemini-1.5-flash-001` model. This change applies to the following features:

  * Playbooks
  * Data stores
  * Generators



Announcement

**Dialogflow CX (Conversational Agents)** : AI generation of [language-specific information](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#ai-generate-data), [entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-options#preview_use_ai_generation_to_auto-generate_synonyms) and [training phrases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#auto-generate-training-phrases) is now GA.

Feature

**Dialogflow CX (Conversational Agents)** : All [prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/prebuilt) are now GA.

## March 27, 2025

Feature

**Dialogflow CX (Conversational Agents) data stores** : Dialogflow now supports additional native and third-party data store sources as a private GA feature. For a list of data store sources, integration instructions, and the request form to be added to the allowlist, see the [data stores documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store#restricted_access_additional_data_store_sources).

Change

**Dialogflow CX (Conversational Agents) data store handlers** : The method of adding data store handlers to an agent has been streamlined. You are no longer required to create a Chat app on Agent Builder. For updated implementation instructions, see the [data stores tools documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/handler#create-agent).

## March 21, 2025

Feature

The [Conversational Agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) console is now generally available (GA). This console combines the power of Generative AI playbooks and data stores with deterministic flows. Additional features:

  * The console is now hosted at `https://conversational-agents.cloud.google.com/`.
  * There is a new menu option for managing languages. Selecting **Manage languages** from the language drop-down menu at the top of the console now automatically redirects you to the **Agent Settings** language management section in the **Deterministic Flows** tab.
  * The simulator now has feature parity with the Dialogflow CX console.



Feature

**Conversational Agents** : Conversational Agents now supports multiple tool versions in addition to playbooks and flows. See the [versions and environments documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) for details.

Feature

**Conversational Agents playbooks** : Playbooks now support 38 languages. Playbook language support is displayed on the [language support page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language). Supported languages have been tested for quality with the `gemini-2.0-flash-001` and `gemini-1.5-flash-002` models.

Feature

**Conversational Agents** : New [Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/chirp3-hd) Cloud Text-to-Speech voices are now available.

Feature

**Conversational Agents playbooks** : New model `gemini-2.0-flash (Preview)` is now available. For more information and supported regions, see [Model support](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook#model).

Feature

**Conversational Agents** : You can now toggle a **Show latency** option in the [Conversational Agents Console](https://conversational-agents.cloud.google.com/projects) simulator to view latency per conversation turn for simulator conversations. To view latency breakdown, click the total latency value for the conversation turn. Latency values are also shown in the original response, Cloud logging, and BigQuery export.

Be aware that latency values are not recorded directly in the logs, but are represented as `startTime` and `completeTime` values in the `traceBlocks` field.

Feature

**Conversational Agents playbooks** : You can now enable DTMF in playbook **Settings** and as a [conditional actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions) as a Preview feature. See the [playbook settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/playbook-settings) and [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf) pages for more information.

## March 14, 2025

Feature

**Dialogflow CX (Conversational Agents)** : [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) is now a GA feature.

## March 11, 2025

Feature

**Dialogflow CX (Conversational Agents) data store handlers** : Model `gemini-2.0-flash-lite-001` is now a Preview feature available in the following regions: `global`, `us`, `us-central1`, `us-east1`, `us-west1`, `europe-west1`, `europe-west4`.

Feature

**Dialogflow CX (Conversational Agents) generators** : Model `gemini-2.0-flash-001` is now a GA feature available in the following regions: `global`, `us`, `us-central1`, `us-east1`, `us-west1`, `europe-west1`, `europe-west4`.

## March 10, 2025

Change

**Dialogflow CX (Conversational Agents)** : The Conversational Agents console has moved to a [new location](https://conversational-agents.cloud.google.com).

Feature

**Dialogflow CX (Conversational Agents)** : You can now use the console search feature to search for all resources, including playbooks, examples, and tools.

Feature

**Dialogflow CX (Conversational Agents)** : Playbooks now support the following new features:

  * [Two different playbook types](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook#types): Task playbooks and routine playbooks.
  * [Connector tools](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#connector).
  * [Conditional actions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/conditional-actions).
  * [DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/playbook-settings).



Feature

**Dialogflow CX (Conversational Agents)** : You can now use the Conversational Agents console to [manage languages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#flow-language).

Feature

**Dialogflow CX (Conversational Agents) data store handlers** : New model `gemini-2.0-flash-001` is now available to [data store handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#model-selection) as a Preview feature. This launch is limited to the following regions: `global`, `us`, `us-central1`, `us-east1`, `us-west1`, `europe-west1`, `europe-west4`.

Feature

**Dialogflow CX (Conversational Agents)** : Text-to-speech used by Dialogflow now supports new [Chirp 3 HD](https://docs.cloud.google.com/text-to-speech/docs/voice-types#chirp3_hd_voices) voices.

Feature

**Dialogflow CX (Conversational Agents)** : [Git export/restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github) now supports additional Git providers and Google Secrets for token storage.

## February 24, 2025

Feature

**Dialogflow CX (Conversational Agents)** : Text-to-speech used by Dialogflow now supports new [Chirp HD voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#chirp_hd_voices).

Feature

**Dialogflow CX (Conversational Agents) & ES**: Text-to-speech removed support for voices across European markets. Affected users were sent an [email announcement](https://docs.cloud.google.com/static/dialogflow/docs/data/euro_voices.pdf).

## February 19, 2025

Change

**Conversational Agents (CX), ES & Agent Assist**: Starting **February 24, 2025** , a [limit of _5 phone numbers per project_ will be enforced](https://docs.cloud.google.com/dialogflow/quotas#count_limits). This limit doesn't apply to the `global` region. For instructions on deleting unused phone numbers and resolving the limit issue, see the [`RESOURCE_EXHAUSTED` troubleshooting section](https://docs.cloud.google.com/dialogflow/docs/support/troubleshooting?agent=any&category=any#phone-number-limit). If you have a business requirement to increase the limit, [request to increase](https://docs.cloud.google.com/dialogflow/quotas#increase) the **Phone numbers** quota specifying the region and providing detailed justification for your request.

## January 23, 2025

Feature

The [Conversational Agents console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) has launched for preview to create agents that can use a combination of generative and deterministic features. See [how we intend on migrating to this new console](https://docs.cloud.google.com/dialogflow/cx/docs#consolidation).

## January 09, 2025

Feature

**Dialogflow CX (Conversational Agents):** Dialogflow CX has launched a new feature that allows you to auto-generate and auto-translate Intent training phrases, Entity synonyms, and Fulfillment phrases in the language of your choice. See the [documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#ai-generate-data) for details.

Feature

**Dialogflow CX (Conversational Agents):** You can now require a **full match for banned phrases** in addition to a partial match. If enabled, a full match requires the input to be matched exactly in order to trigger a ban. For more information about setting banned phrases, see the [documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-generative-banned).

Feature

**Dialogflow CX (Conversational Agents):** Service directory support is now enabled for **flexible webhooks**. See the [webhooks documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd) for details.

## December 19, 2024

Feature

**Dialogflow CX (Conversational Agents)** : You can now set either a _partial match_ or a _full match_ to banned phrases. This setting applies to playbooks, datastores, and generators. You can enable and test this feature in **Agent Settings > Generative AI > Banned phrases > Match requirements**.

## December 13, 2024

Announcement

**Dialogflow CX data stores** : The following languages are now GA. See the [language support page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) for details.

  * Arabic
  * Bengali
  * Bulgarian
  * Chinese Simplified
  * Chinese Traditional
  * Croatian
  * Czech
  * Estonian
  * Finnish
  * Hebrew
  * Hungarian
  * Japanese
  * Korean
  * Latvian
  * Lithuanian
  * Norwegian
  * Polish
  * Romanian
  * Russian
  * Serbian
  * Slovak
  * Slovenian
  * Swahili
  * Thai
  * Turkish
  * Ukrainian
  * Vietnamese



## December 12, 2024

Feature

**Dialogflow CX** : You can now configure an access token name in Dialogflow Messenger to store the end user's authentication when they sign in, and then use it as the bearer token for [tool authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/tool#openapi_tool_api_authentication). See the [Dialogflow Messenger documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger#embed) for more information about enabling this feature.

## November 14, 2024

Feature

**Dialogflow CX:** New feature **Context token limits** has been added to **Agent Settings > Generative AI**. You can use this feature to set a percentage of the token budget to be reserved for conversation history, as a maximum. See the [Agent Settings documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-generative) for details.

Feature

**Data store tools:** You can now optimize the RAG performance of data store tools used by Playbooks. See the [documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/performance#optimization_of_data_store_tools_used_by_playbooks) for details.

Change

**Generators and data store handlers:** The [model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) `gemini-1.5-flash-002` is now GA.

Change

**Data store handlers** : The default generative [model](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) has been changed to `gemini-1.5-flash-001`.

## November 07, 2024

Change

**Dialogflow CX** : As of August 2024, `us-dialogflow.*` has been re-introduced as the canonical endpoint for the US multi-region. The `usa-dialogflow.*` endpoint is still supported as an alias. See the [regionalization documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region#avail) for details.

## October 24, 2024

Change

**Dialogflow CX & ES**: In order to increase the stability of Cloud Text-to-speech, out-of-quota requests for [Journey Voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#journey_voices) will now be fulfilled with a fallback voice of the same speaker persona. To opt out, contact your Google account team.

Feature

**Dialogflow CX & ES**: Dialogflow now supports **A-law encoding** in addition to Mu-law encoding for input and output audio. A-law and Mu-law are the two available formats in [G.711](https://en.wikipedia.org/wiki/G.711).

## October 10, 2024

Feature

**Conversational Agents** : The `gemini-1.5-flash-001` [model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store/settings#model-selection) is generally available (GA) for data store handlers as of August 20, 2024. The `gemini-1.5-flash-002` model remains public Preview.

## September 26, 2024

Announcement

Starting in late 2024 and ending in early 2025, there will be changes to some Dialogflow product names, feature names, and consoles. See the [documentation](https://docs.cloud.google.com/dialogflow/cx/docs#consolidation) for complete details.

Feature

**Dialogflow CX** : You can now enable security checks to prevent prompt injection attacks. See the [documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-generative-prompt-security) for details.

Change

**Dialogflow CX** : Cloud Text-to-Speech `europe-west1` and `europe-west3` regions for Neural2 voices now use corresponding regions.

## September 19, 2024

Feature

**Dialogflow CX & ES**: Text-to-speech [Journey Voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#journey_voices) now supports MULAW output `audio_encoding` ([CX](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#outputaudioconfig), [ES](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#outputaudioconfig)) in addition to LINEAR16. Future updates to Journey Voices will appear in the [Cloud Text-to-Speech documentation](https://docs.cloud.google.com/text-to-speech/docs/voice-types#journey_voices_preview).

Deprecated

**Dialogflow CX and Vertex AI** : The `text-bison@002`, `text-bison` and `code-bison` models will be deprecated on **October 21, 2024** and automatically upgraded to the `gemini-1.5-flash-001` model. This change applies to **Vertex AI agents** and the following **[Dialogflow CX Generative Features](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative)** :

  * Vertex AI agent apps 
  * Data store agents (also known as Chat agents)
  * Generators



After the upgrade on October 21, 2024, `gemini-1.5-flash-001` will be automatically selected in the console. We recommend that you upgrade to the new model early to allow enough time for testing and to ensure that your solution works as intended.

Change

**Dialogflow CX** : Cloud Text-to-Speech `europe-west1` and `europe-west3` regions for Neural2 voices will temporarily use the `eu` multi-region instead.

## September 16, 2024

Change

**Dialogflow CX and Vertex AI Agents** : Generative features will migrate to the gemini-1.5-flash-001 model on September 30, 2024. See the [email notification](https://docs.cloud.google.com/static/dialogflow/docs/data/msa-gemini-1.5-flash-001.pdf).

## August 29, 2024

Feature

**Dialogflow CX & ES**: Text-to-Speech [Journey Voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#journey_voices) will get an update in the week of Sept 3. If you select a journey voice in your agent Text-to-Speech settings ([CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#text-to-speech), [ES](https://docs.cloud.google.com/dialogflow/es/docs/agents-settings#speech)), only LINEAR16 output audio_encoding ([CX](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#outputaudioconfig), [ES](https://docs.cloud.google.com/dialogflow/es/docs/reference/rpc/google.cloud.dialogflow.v2#outputaudioconfig)) will be supported starting from Sept 3. This model update will also include slight variations in pauses, tone, and so on of the synthesized journey voices.

## August 15, 2024

Feature

**Dialogflow CX** : You can now configure sensitivity levels of [safety filters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-generative-safety) with respect to different Responsible AI (RAI) categories.

Feature

**Vertex AI Agents** : OpenAPI [tool authentication](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi_tool_api_authentication) now supports custom client certificates for mutual TLS authentication.

## July 26, 2024

Feature

**Dialogflow CX** : You can now enable consent-based end-user content redaction. If this setting is enabled, it lets you use a special session parameter to control whether end-user input and parameters are redacted from conversation history and Cloud logging. See the [agent settings documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#logging-settings) for details.

Change

**Dialogflow CX** : Dialogflow now uses corresponding Cloud Text-to-Speech regions for [Neural2 voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#neural2_voices).

Change

The status of the Dialogflow Speech-to-Text model migrations has changed:

  * The Dialogflow speech model migration [initially announced in December 2023](https://docs.cloud.google.com/dialogflow/docs/release-notes#December_15_2023) and later [postponed to the new dates](https://docs.cloud.google.com/dialogflow/docs/release-notes#March_11_2024) has been placed on hold until further notice (no ETA). For more information, see the migration documentation for [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration) and [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration).

  * The Dialogflow `phone_call` speech model migration [announced in March 2024](https://cloud.google.com/dialogflow/docs/release-notes#March_29_2024) has been partially completed. The remaining migration parts have been placed on hold until further notice (no ETA). For more information, see the migration documentation for [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024) and [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration-q2-2024).




## July 11, 2024

Feature

**Vertex AI Agents** : Agent apps now provide [generative settings](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/agent-apps#settings-generative) for input token limit, output token limit, and temperature.

## June 27, 2024

Breaking

**Dialogflow ES** : As of May 27 2024, Twilio no longer supports integrations with Dialogflow ES. For more details and information about migrating to Dialogflow CX, see the [Twilio documentation](https://www.twilio.com/en-us/changelog/twilio-voice-google-dialogflow-es-integration-will-end-of-life-o#:%7E:text=Twilio%20Voice%20Google%20Dialogflow%20ES,on%20May%2027%202024%20%7C%20Twilio).

Feature

**Dialogflow CX** : The gemini-1.5-flash generative model is now available for the [generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) feature.

## June 13, 2024

Feature

**Vertex AI Agents** : The following new regions are supported by agent apps:

  * `europe-west1`
  * `europe-west2`
  * `europe-west3`
  * `northamerica-northeast1`
  * `us-west1`



## June 11, 2024

Feature

The following was incorrectly announced: ~~**Dialogflow CX** : The gemini-1.5-flash generative model is now available for the [generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) feature.~~

## June 07, 2024

Feature

**Data store agents** : You can now run [self-service evaluation](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store-agent-performance#evaluation) which will assess the quality of your data store agent and recommend changes.

Deprecated

**All generative features** : It was [announced previously](https://docs.cloud.google.com/dialogflow/docs/release-notes#March_25_2024) that the `text-bison@001` model will be deprecated. In addition, the `code-bison@001` model and fine-tuned `text-bison@001` options will be deprecated. This deprecation will happen mid June. The deprecated models will be updated to `gemini-1.0-pro-001`, as [previously announced](https://docs.cloud.google.com/dialogflow/docs/release-notes#May_08_2024). For more information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/docs/data/text-bison-001-to-gemini-1.0-pro-001.pdf).

Feature

**Dialogflow CX** now offers custom webhook templates for integration with Salesforce. See the [webhooks documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#predefined-template) for details.

Feature

**Data store agents** : The gemini-1.5-flash generative model is now available for selection in the console.

## May 29, 2024

Feature

**Dialogflow CX** : You can now integrate with [Soul Machines](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/soul-machines) to create 3-D avatars.

## May 21, 2024

Feature

**Vertex AI Agents** : OpenAPI tool authentication now supports [Bearer Token](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi_tool_api_authentication).

Feature

**Dialogflow CX** : [VPC Service Controls](https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls) now support Cloud Functions and Cloud Run.

Feature

**Vertex AI Agents** : OpenAPI tools now support [private network access](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#openapi_tool_private_network_access)

## May 08, 2024

Change

Dialogflow ES and Dialogflow CX: The `us-dialogflow.googleapis.com` endpoint and `locations/us` resource location, which served as aliases for global resources, will be discontinued starting May 21, 2024. We have changed the date to update resource locations and endpoints from April 16, 2024 to May 21, 2024 to provide you with additional time. For more information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/docs/data/us-deprecation.pdf).

Note

  * This change affects only the agents created in the `global` region ([ES](https://docs.cloud.google.com/dialogflow/es/docs/how/region), [CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region)) and only if you use the `us` alias in the API requests to these global-region agents. If you created agents in `us-central1`, `us-east1`, `us-west1`, and `us` (multi-region) regions, no action is required.
  * The discontinued endpoint is different than the `us` multi-region endpoint that was [announced recently](https://docs.cloud.google.com/dialogflow/docs/release-notes#April_23_2024).



Change

Dialogflow CX and Vertex AI Agents: Effective June 15, 2024, the following [generative features](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative) will be upgraded from text-bison-001 and fine-tuned text-bison@001 options to gemini-1.0-pro-001:

  * Vertex AI agent apps
  * Data store agents (aka Chat agents)
  * Generators
  * Generative fallback



For more information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/docs/data/text-bison-001-to-gemini-1.0-pro-001.pdf)

## May 06, 2024

Change

**Data store agents** : The default generative model has been changed to gemini-1.0-pro-001.

## April 30, 2024

Feature

Vertex AI Agents: Agent apps now support [all languages supported by Vertex AI generative models](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/agent-apps#language).

Change

Vertex AI Conversation has been renamed to Vertex AI Agents

Feature

Dialogflow CX: You can now access the session ID with [built-in parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#request-built-in).

Feature

Vertex AI Agents: [Agent apps](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/agent-apps) now support the `eu` multi-region.

## April 23, 2024

Feature

Dialogflow CX: The following new [region](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) is available:

  * `us`: United States multi-region accessed via `usa-dialogflow.googleapis.com` hostname



## April 18, 2024

Feature

Dialogflow CX: The [Conversation history API](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3beta1#conversationhistory) is now available for public preview.

## April 04, 2024

Feature

Vertex AI Conversation: You can now create a [data store in one language](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store#languages) that is connected to an agent that uses different languages.

## April 03, 2024

Feature

Dialogflow CX: [Language auto detect](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-multilingual#lang-detect) is now available for **chat conversations**. You can configure Dialogflow CX to detect an end-user's language and automatically respond in that same language. See the [language reference page](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) for a list of languages available for this feature.

## April 02, 2024

Feature

Vertex AI Conversation: Data stores now support [parse and chunk configuration](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store#parse-chunk).

Feature

Dialogflow CX: [Dialogflow CX phone gateway](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway) is now generally available.

Feature

Dialogflow CX: [Call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion) is now generally available with new [user interface settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion#settings).

## March 29, 2024

Change

Starting on April 17, 2024, the Dialogflow CX and Dialogflow ES traffic with audio will gradually route away from the classic `phone_call` speech model to the new conformer-based speech models for the following language tags: `en-au`, `en-gb`, `de`, `de-de`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `it-it`, `ja`, `pt-br`. For more information, see [Dialogflow ES migration documentation](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration-q2-2024) and [Dialogflow CX migration documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration-q2-2024).

Feature

Dialogflow CX: You can now enable [smart endpointing](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#smart-endpointing).

## March 25, 2024

Feature

Dialogflow CX: The **[Override request-level speech model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#stt-model-selection)** has been added to advanced speech settings. This can be used to override the speech model provided in a runtime API request.

Feature

Dialogflow CX: [DTMF for telephony integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/dtmf) is now available for preview.

Deprecated

**All generative features** : The text-bison-001 model and fine-tuned text-bison@001 options will be deprecated by Vertex AI on July 6th. Please transition as soon as possible to the default option or another model available in the settings.

Feature

Vertex AI Conversation [data stores](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/data-store): Gemini-pro 1.0 is now officially in General Availability. The model includes optimized prompting, delivering enhanced results with minimal latency impact. Please note: prompt optimization is currently focused on English, with other languages to follow.

## March 19, 2024

Feature

Dialogflow CX [request-scoped parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#request-scoped) now supports the `$request.user-utterance` parameter to reference the end-user utterance.

Feature

Dialogflow CX now provides the [offers and deals prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/offers-and-deals).

Feature

Vertex AI Conversation [data store tools](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/tools#data-store) now support `filter` and `userMetadata` example parameters.

## March 18, 2024

Feature

The following prebuilt components have been added to Dialogflow CX:

  * [Retail fraud and dispute](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/fraud-and-dispute-retail)
  * [Cancel order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/cancel-order)
  * [Return and refund](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/return-and-refund)
  * [Exchange order](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/exchange-order)



Change

The Dialogflow ES and Dialogflow CX `us-dialogflow.googleapis.com` endpoint and `locations/us` resource location, which served as aliases for global resources, will be discontinued on May 21, 2024. For more information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/docs/data/us-deprecation.pdf).

## March 11, 2024

Change

From March 18 to April 15, 2024 (new dates for the [same migration announced earlier](https://docs.cloud.google.com/dialogflow/docs/release-notes#December_15_2023)), for certain language tag and speech setting combinations, the Dialogflow CX and Dialogflow ES traffic with audio will gradually route away from the classic Speech-to-Text models behind the `command_and_search`, `default`, `phone_call`, and `video` model identifiers to the new conformer-based speech models.

If your Dialogflow agents have audio traffic and use one of the following language tags: `en`, `en-us`, `en-au`, `en-gb`, `en-in`, `de`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `ja`, `nl`, `pt-br`, read more about [Dialogflow CX speech model migration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration) and [Dialogflow ES speech model migration](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration).

## March 06, 2024

Announcement

Vertex AI Conversation now supports the [Dialogflow CX Messenger integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) for preview.

## March 05, 2024

Feature

Vertex AI Conversation [generative agent creation with playbooks](https://docs.cloud.google.com/dialogflow/vertex/docs/concept/agents) is now available for public preview. Try it by following the [quickstart](https://docs.cloud.google.com/dialogflow/vertex/docs/quick/create-application).

## February 20, 2024

Change

The [previously announced](https://docs.cloud.google.com/dialogflow/docs/release-notes#January_12_2024) migration from Standard NLU to Advanced NLU will no longer occur on March 1, 2024. For more information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/standard-nlu.pdf)

Feature

Dialogflow CX [channel-specific response messages](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific) are now available for the following integrations: Google Chat, LINE, Messenger from Meta, Workplace from Meta, Slack. See the integration documentation for details.

Feature

You can now [import and export Dialogflow CX custom entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-custom).

Change

Dialogflow CX agents now default to [advanced NLU](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#nlu-type).

## February 13, 2024

Feature

Dialogflow CX text-to-speech settings now have an option for [custom voices](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#voice-selection).

## February 12, 2024

Feature

Two new Dialogflow CX prebuilt components are available: [retail authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication-retail) and [order status](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/order-status).

## January 25, 2024

Feature

Vertex AI Conversation data stores now support [unstructured CSV](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/data-store#unstructured).

## January 24, 2024

Feature

Dialogflow CX [generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/generators) has added support for text-bison@002 and gemini-pro models.

Feature

With data store agents, you can now provide a [custom summarization prompt](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/data-store-agent#customize-summarization-prompt).

## January 23, 2024

Fixed

The Dialogflow CX [name collection prebuilt component](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection) removed use of the deprecated system entities `@sys.given-name` and `@sys.last-name`. They have been replaced with `@sys.person`.

Change

Speech model migration [announced eariler](https://docs.cloud.google.com/dialogflow/docs/release-notes#December_15_2023) will include two additional language tags: `en-in` and `nl`. The migration start date is postponed and will be announced in a new release note later. For more information, read [Dialogflow CX speech model migration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration) and [Dialogflow ES speech model migration](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration).

## January 18, 2024

Change

To temporarily opt out from the [speech model migration](https://docs.cloud.google.com/dialogflow/docs/release-notes#December_15_2023), you can now use the `opt_out_conformer_model_migration` field in the runtime Dialogflow API requests. Read more about temporary opt-out for [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration#temporary-opt-out) and [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration#temporary-opt-out).

Feature

Dialogflow CX now [allows cancellation of partial response playback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#partial-response-cancel).

## January 16, 2024

Feature

Vertex AI Conversation has launched [generative agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/playbook) in the Vertex AI Conversation console. Generative agents were previously called playbook agents in the Dialogflow CX console. This feature currently has restricted access.

## January 12, 2024

Change

Dialogflow CX Standard NLU agents ~~will be migrated to Advanced NLU starting March 1, 2024~~. For updated information, see the [email announcement](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/standard-nlu.pdf).

## January 03, 2024

Announcement

The Text-to-Speech API used by Dialogflow now supports two new experimental voices for en-us: en-US-Journey-D and en-US-Journey-F. For more details, see [Journey voices](https://docs.cloud.google.com/text-to-speech/docs/voice-types#journey_voices).

## December 21, 2023

Feature

Vertex AI Conversation: You can now [select the generative model](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/data-store-agent#model-selection) for data store agents.

## December 19, 2023

Feature

Dialogflow CX now provides a new integration for [Workplace from Meta](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/meta-workplace).

## December 15, 2023

Change

From January 23 to February 13, 2024, for certain language tag and speech setting combinations, the Dialogflow CX and Dialogflow ES traffic with audio will gradually route away from the classic Speech-to-Text models behind the `command_and_search`, `default`, `phone_call`, and `video` model identifiers to the new conformer-based speech models. 

If your Dialogflow agents have audio traffic and use one of the following language tags: `en`, `en-us`, `en-au`, `en-gb`, `de`, `es`, `es-es`, `es-us`, `fr`, `fr-ca`, `fr-fr`, `it`, `ja`, `pt-br`, read more about [Dialogflow CX speech model migration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-model-migration) and [Dialogflow ES speech model migration](https://docs.cloud.google.com/dialogflow/es/docs/speech-model-migration).

## December 14, 2023

Feature

Three new Dialogflow CX [generative prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative/prebuilt-agent) are now available. These prebuilt agents are built on [playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) and provide use cases for Department of Motor Vehicles, retail, and travel.

## December 12, 2023

Change

To restore an agent with data store handlers, you now need to associate the target agent with a Vertex AI Conversation app and create data store references in the target agent prior to the restore operation. See more at [Export and restore an agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#export).

Feature

[Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) and [data store agents](https://docs.cloud.google.com/generative-ai-app-builder/docs/cmek) now support Customer-Managed Encryption Keys (CMEK) in GA. In order to use CMEK, you must contact your Google account team to request access.

## December 04, 2023

Feature

The Speech-to-Text API used by Dialogflow now supports two new speech models for the `en` and `en-us` language tags: `telephony` and `telephony_short`. The two models are customized to recognize audio that originates from a phone call and corresponds to the most recent versions of the existing `phone_call` model. For more details, see [Dialogflow CX speech models](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-models) and [Dialogflow ES speech models](https://docs.cloud.google.com/dialogflow/es/docs/speech-models).

## November 29, 2023

Feature

Dialogflow CX [answer feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback) is now generally available (GA) and has new configurations in [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger), [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history), and [BigQuery export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq).

## November 07, 2023

Change

Dialogflow CX now has a new language code for Hebrew: `he-il`. For supported features, check the [language reference table](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language#table). 

The `iw` Hebrew language code is now deprecated, so new agents should use the `he-il` language code. Existing agents using the `iw` language code will continue working, but the list of supported features won't be expanded.

## November 01, 2023

Feature

Dialogflow CX now supports the [DIVIDE](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-divide) and [MULTIPLY](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-multiply) system functions.

Feature

[Data store agents](https://docs.cloud.google.com/generative-ai-app-builder/docs/agent-data-store) now support additional languages and regions.

## October 25, 2023

Change

On the week of October 30, 2023, auto speech adaptation ([CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#auto-adaptation), [ES](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation)) will be updated for non-English agents. No major behavior changes are expected.

If you notice speech recognition issues in Dialogflow CX, you can mitigate by enabling [manual speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#manual-adaptation) on flows and pages experiencing issues. You can tune the adaptation as follows:

  1. On the problematic flows and pages, disable auto speech adaptation by enabling manual speech adaptation without adding phrases.

  2. If your agent is unable to recognize certain words and phrases, add those phrases to the adaptation with no boost.

  3. If your agent is still unable to recognize certain words and phrases after step 2, duplicate those phrases so that you have one without boost and one with [boost](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation#boost-value).




If you notice speech recognition issues in Dialogflow ES, you can mitigate by using the [speechContexts](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryInput#inputaudioconfig) field at runtime which overrides auto speech adaptation or by updating your [agent design](https://docs.cloud.google.com/dialogflow/es/docs/speech-adaptation#agent-design).

## October 23, 2023

Feature

Dialogflow CX has added the following prebuilt components:

  * [Account balance](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-balance)

  * [Account statement](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/account-statement)

  * [Alphanumeric collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/alphanumeric-collection)

  * [Arrange appointment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/arrange-appointment)

  * [Authentication](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/authentication)

  * [Credit card enrollment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-enrollment)

  * [Credit card statement](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-statement)

  * [Disputes](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/disputes)

  * [Financial services steering](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/financial-services-steering)

  * [Lock card](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lock-card)

  * [Lost and stolen card](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/lost-stolen-card)

  * [Make a payment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/make-a-payment)

  * [Open account](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/open-account)

  * [Transaction history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/transaction-history)




## October 12, 2023

Feature

Dialogflow CX launched [generative playbooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook) with restricted access.

Change

Dialogflow CX [spelling correction](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-ml) now supports all regions, but is limited to five languages.

Feature

Dialogflow CX [generative feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback) now supports more languages.

## October 02, 2023

Feature

Dialogflow CX [speech adaptation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/speech-adaptation) can now be configured manually.

## September 29, 2023

Feature

Dialogflow CX launched two new integrations in preview:

  * [Google Chat](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/google-chat)
  * [Slack](https://cloud.google.com/dialogflow/cx/docs/concept/integration/slack)



## September 25, 2023

Feature

Dialogflow CX now provides the [call companion](https://docs.cloud.google.com/dialogflow/cx/docs/concept/call-companion) feature in preview, which provides a mobile-based user interface that supplements a phone call with an agent.

## September 19, 2023

Feature

Dialogflow CX [intent import/export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#export) and [training phrase import/export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#import-phrases) are now generally available.

## September 15, 2023

Feature

Dialogflow CX has added the [FILTER](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-filter) system function.

Change

Improvements to Prebuilt Components:

  * [Name collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/name-collection): fixed issue with names containing multiple special characters
  * [Credit card expiration date collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/credit-card-expiration-date-collection): updated SSML in agent responses
  * [Date of birth (DOB) collection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/date-of-birth-collection): fixed issue with entities for specific pronunciations of months and days



Feature

Dialogflow CX [flow export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#export) now exports flows recursively.

## August 31, 2023

Feature

[Dialogflow CX Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) has been redesigned and is now GA. This new version of the integration replaces the old version, which has been renamed [Legacy Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/legacy-dialogflow-messenger). The old version is now deprecated, and it is recommended that all users of the old version [migrate](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/legacy-dialogflow-messenger#migrate) to the new version.

Feature

Dialogflow CX [answer feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/answer-feedback) is now GA, but access is limited and must be requested.

Feature

Dialogflow CX generative features are now GA and publicly available:

  * [Generative AI agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-agent)
  * [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generators)
  * [Generative fallback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback)
  * [Generative personalization](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-personalization)



## August 16, 2023

Change

Dialogflow CX now supports past, future, and partial date and time values for ambiguous end-user inputs matched to @sys.date, @sys.date-time, and @sys.time [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities).

## August 14, 2023

Feature

Dialogflow CX [route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group) can now be flow-level or agent-level.

## August 11, 2023

Feature

Google has open sourced the following [Dialogflow CX integrations](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration#google-contributed):

  * [Azure Bot Service & Microsoft Teams](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/azure-bot-service)
  * [Discord](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/discord)
  * [Google Chat](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/google-chat)
  * [ServiceNow](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/servicenow)
  * [Slack](https://cloud.google.comhttps://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/slack)
  * [Spark](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/spark)
  * [Telegram](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/telegram)
  * [Twilio](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/twilio)
  * [Twitter](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/twitter)
  * [Viber](https://github.com/GoogleCloudPlatform/dialogflow-integrations/tree/master/cx/viber)



## August 08, 2023

Feature

Dialogflow CX [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) has added two new views: flow analysis table and flow analysis graph.

Feature

Dialogflow CX now provides [intent suggestions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#suggestions).

Feature

Dialogflow CX now provides a [split intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#split) feature.

Feature

Dialogflow CX [analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics) has been reimplemented to provide all new views and metrics. The old views have been renamed [legacy analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics-legacy).

Feature

Dialogflow CX now provides a [compare and merge intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#merge) feature.

Feature

Dialogflow CX now provides a [timeout-based end of speech sensitivity](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech) setting.

## August 01, 2023

Feature

Dialogflow CX has added a new prebuilt component for [feedback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component/feedback).

## July 18, 2023

Feature

Dialogflow CX has launched three new generative AI features. These features are generally available (GA), but access is limited and must be requested:

  * [Generative AI agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-agent)
  * [Generators](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generators)
  * [Generative fallback](https://docs.cloud.google.com/dialogflow/cx/docs/concept/generative-fallback)



Also see the [blog post](https://cloud.google.com/blog/products/ai-machine-learning/generative-ai-powered-chatbots-and-virtual-agents) announcing these features.

## July 11, 2023

Feature

Dialogflow CX now supports [speech recognition model selection](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech).

## July 06, 2023

Feature

Dialogflow CX [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) has been promoted from Preview to GA (generally available).

Change

Dialogflow CX minimum voice session duration for [pricing](https://cloud.google.com/dialogflow/pricing) has been decreased from 1 minute to 1 second.

## July 05, 2023

Feature

Dialogflow CX now provides [prebuilt components](https://docs.cloud.google.com/dialogflow/cx/docs/concept/prebuilt-component), which are prebuilt flows that handle common scenarios and accelerate agent development.

Feature

The following Dialogflow CX features have been promoted from Preview to GA (generally available):

  * [GitHub export/restore](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github)
  * [Interaction logging export to BigQuery](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq)



## June 28, 2023

Feature

Dialogflow CX now supports [flow scoped parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#flow-scoped).

## June 27, 2023

Feature

Dialogflow CX has added the following [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions):

  * IS_CREDIT_CARD_NUMBER
  * IS_DATE
  * IS_FUTURE_DATE
  * IS_PAST_DATE
  * IS_PHONE_NUMBER
  * NESTED_FIELD
  * ROUND
  * TO_OBJECT
  * TO_PHONE_NUMBER
  * UPPER



## May 24, 2023

Change

Dialogflow CX [quota](https://docs.cloud.google.com/dialogflow/quotas#table) for design time read requests has been increased to 200 per minute.

## May 03, 2023

Feature

Dialogflow CX now provides the [ADD_DATE](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-adddate) system function.

## April 26, 2023

Feature

Dialogflow CX now supports [intent import/export](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#export) and [training phrase import](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent#import-phrases).

## April 12, 2023

Feature

Dialogflow CX now supports [flexible webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#flexible), where you can define the request HTTP method, request URL parameters, and fields of the request and response messages.

## March 27, 2023

Feature

Dialogflow CX now provides the [TO_NUMBER system function](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-tonumber).

## March 21, 2023

Feature

Dialogflow CX [sentiment analysis](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment) now supports all [regions supported by Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) and over 70 new [languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language).

## March 03, 2023

Feature

Dialogflow CX now provides a setting for [choosing the voice](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-speech) for speech synthesis.

## March 02, 2023

Change

The Dialogflow CX [maximum number of flows per agent](https://docs.cloud.google.com/dialogflow/quotas#count_limits) has been increased from 20 to 50.

## February 28, 2023

Change

The Dialogflow CX [audio input duration limit](https://docs.cloud.google.com/dialogflow/quotas#duration_limits) has been increased from one minute to two minutes.

## February 14, 2023

Feature

Dialogflow CX added regional support for some [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-entities). The following system entities:

  * @sys.person
  * @sys.address
  * @sys.geo-city
  * @sys.geo-country
  * @sys.geo-state



are now available in the following [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) for English (en), French (fr), Italian (it), German (de), and Spanish (es) languages:

  * europe-west1
  * europe-west2
  * europe-west3
  * northamerica-northeast1



## February 06, 2023

Feature

Dialogflow CX now provides [flow import options](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#import) for resolving resource conflicts.

## January 30, 2023

Change

The Dialogflow CX [flow stack limit](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#flow-stack-limit) has been increased to 25.

## January 18, 2023

Feature

Dialogflow CX now provides [custom payload templates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#custom-payload-templates).

Feature

Dialogflow CX now provides [channel-specific responses](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#channel-specific).

## January 17, 2023

Announcement

Migrating from Dialogflow ES to Dialogflow CX is recommended for complex agents, and migrating can significantly improve your agent design and end-user experience. See the new [migration guide](https://cloud.google.com/dialogflow/cx/docs/how/migrate).

## December 27, 2022

Feature

Dialogflow CX now supports the [MATCH](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-match) system function.

## December 16, 2022

Feature

Dialogflow CX now supports [flow export to diagram in the draw.io XML format](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow#export).

Change

To improve security, the "dialogflow.sessions.detectIntent" and "dialogflow.sessions.streamingDetectIntent" permissions are being removed from the IAM Viewer role on January 31, 2023. 

To continue using the Dialogflow CX/ES console simulator or making detectIntent/streamingDetectIntent API calls, users and service accounts with the IAM Viewer role must update roles granted to them to include a role with these permissions. For example, the IAM Dialogflow API Client role ([ES documentation](https://docs.cloud.google.com/dialogflow/es/docs/access-control#roles), [CX documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control#iam-roles)) includes these permissions. For Dialogflow CX, you can [apply the agent-specific Client role using the Dialogflow console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control#df-console).

## December 12, 2022

Feature

Dialogflow CX added [sentiment analysis](https://docs.cloud.google.com/dialogflow/cx/docs/concept/sentiment) support in the following [regions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region) for English (en), French (fr), Italian (it), German (de), and Spanish (es) languages:

  * asia-southeast1
  * europe-west1
  * europe-west2
  * europe-west3
  * northamerica-northeast1



Feature

Dialogflow CX now supports [interaction logging export to BigQuery](https://docs.cloud.google.com/dialogflow/cx/docs/concept/export-bq).

## November 21, 2022

Feature

Dialogflow CX now [integrates with GitHub](https://docs.cloud.google.com/dialogflow/cx/docs/concept/github). This integration makes it easy to export your agent to JSON for a push to GitHub, and to pull from GitHub for an agent restore.

## November 15, 2022

Feature

Dialogflow CX agents can now be [exported to JSON](https://docs.cloud.google.com/dialogflow/cx/docs/reference/json-export).

## November 07, 2022

Feature

The following languages are now GA (generally available) for Dialogflow CX:

  * Bulgarian (bg)
  * Catalan (ca)
  * Croatian (hr)
  * Czech (cs)
  * Greek (el)
  * Hebrew (iw)
  * Hmong (hmn)
  * Hungarian (hu)
  * Serbian (sr)
  * Slovak (sk)
  * Somali (so)



## October 21, 2022

Feature

Dialogflow CX now provides a [telephony integration with Twilio](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/twilio)

## October 11, 2022

Feature

Dialogflow CX [Advanced NLU](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-ml) now supports automatic training.

## October 03, 2022

Feature

Dialogflow CX now provides a [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history) tool, which can be used to browse, filter, and analyze production conversations.

## August 18, 2022

Announcement

Dialogflow CX and ES have new tutorials that walk through the steps of deploying a Dialogflow agent on Google Cloud, integrating with Cloud Functions, Spanner, and App Engine:

  * [Deploy a Dialogflow CX agent on Google Cloud](https://docs.cloud.google.com/dialogflow/cx/docs/tutorials/deploy)
  * [Deploy a Dialogflow ES agent on Google Cloud](https://docs.cloud.google.com/dialogflow/es/docs/tutorials/deploy)



## July 06, 2022

Feature

Dialogflow ES now provides a new client library for [C++](https://docs.cloud.google.com/dialogflow/es/docs/reference/libraries/cpp).

Feature

Dialogflow CX now provides new client libraries for [C++](https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/cpp), [C#](https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/csharp), and [Go](https://docs.cloud.google.com/dialogflow/cx/docs/reference/library/go).

## June 21, 2022

Feature

The Dialogflow CX [search feature](https://docs.cloud.google.com/dialogflow/cx/docs/concept/search) is now GA (generally available).

## June 13, 2022

Deprecated

The [Dialogflow ES Google Assistant integration](https://docs.cloud.google.com/dialogflow/es/docs/integrations/aog) will be removed on June 13, 2023. This is due to the Google Assistant [Conversational Actions planned sunsetting](https://goo.gle/ca-sunset).

## May 23, 2022

Feature

Dialogflow CX now supports [version-specific webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#environment-specific).

Feature

Dialogflow CX now supports fine-grained webhook errors for [built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).

## April 28, 2022

Feature

Dialogflow ES has added preview support for the following [languages](https://docs.cloud.google.com/dialogflow/es/docs/reference/language):

Afrikaans, Albanian, Amharic, Armenian, Azerbaijani, Basque, Belarusian, Bosnian, Bulgarian, Catalan, Cebuano, Chichewa, Corsican, Croatian, Czech, Esperanto, Estonian, Frisian, Galician, Georgian, Greek, Gujarati, Haitian Creole, Hausa, Hmong, Hungarian, Icelandic, Igbo, Irish, Javanese, Kannada, Kazakh, Khmer, Kinyarwanda, Kurdish, Kyrgyz, Latin, Latvian, Lithuanian, Luxembourgish, Macedonian, Malagasy, Malayalam, Maltese, Maori, Mongolian, Nepali, Oriya/Odia, Punjabi, Samoan, Scots Gaelic, Serbian - Cyrillic, Serbian - Latin, Sesotho, Shona, Slovak, Slovenian, Somali, Sundanese, Swahili, Tajik, Tatar, Turkmen, Uzbek, Welsh, Xhosa, Yoruba, Zulu

## April 06, 2022

Feature

Dialogflow CX now supports [Access Transparency](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-transparency) logging of Google personnel access to Dialogflow data.

## April 05, 2022

Feature

Dialogflow CX now provides a setting to [lock agent editing](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-general).

Feature

Dialogflow CX [system functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions) have new list-related functions: APPEND, GET, and REMOVE.

## January 24, 2022

Feature

Dialogflow CX has a new [agent design best practices guide](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-design).

## January 19, 2022

Change

The Dialogflow CX [QueryResult.match.event](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.Match) field previously only populated custom events. It is now also populated with [no-match and no-input built-in events](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).

Feature

Dialogflow CX now provides an [IDENTITY system function](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions#func-identity), which is useful to copy a composite parameter object in a parameter preset field.

## December 15, 2021

Feature

Dialogflow CX [auto sync](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-collaboration#auto_sync) for agent collaboration is now GA (generally available).

Feature

Dialogflow CX [change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history) is now GA (generally available).

Feature

The Dialogflow CX simulator now allows you to [specify flow versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version#specify-versions) when interacting with the simulator.

## December 13, 2021

Feature

Dialogflow CX now supports the `asia-southeast1` (Jurong West, Singapore) and `europe-west3` (Frankfurt, Germany) regions.

## December 08, 2021

Feature

The Dialogflow CX simulator now provides [page lifecycle navigation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/page#visualization) to help you understand the execution steps taken for each conversational turn.

## November 17, 2021

Feature

Dialogflow CX webhooks now support [custom CA certificates](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#https_certificate_verification).

Feature

Dialogflow CX now supports [agent backup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-backup).

Feature

Dialogflow CX Phone Gateway now supports [call transfer](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#transfer).

## November 04, 2021

Feature

Preview launch of the following [languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) in Dialogflow CX:

Afrikaans, Amharic, Azerbaijani, Belarusian, Bulgarian, Bosnian, Catalan, Cebuano, Corsican, Czech, Welsh, Greek, Esperanto, Estonian, Basque, Persian, Frisian, Irish, Scots Gaelic, Galician, Gujarati, Hausa, Hebrew, Hmong, Croatian, Haitian Creole, Hungarian, Armenian, Igbo, Icelandic, Javanese, Georgian, Kazakh, Khmer, Kannada, Kurdish, Kyrgyz, Latin, Luxembourgish, Lithuanian, Latvian, Malagasy, Maori, Macedonian, Malayalam, Mongolian, Maltese, Nepali, Chichewa, Odia, Punjabi, Pashto, Kinyarwanda, Sindhi, Slovak, Slovenian, Samoan, Shona, Somali, Albanian, Serbian, Sesotho, Sundanese, Swahili, Tajik, Turkmen, Tatar, Uyghur, Urdu, Uzbek, Xhosa, Yiddish, Yoruba, Zulu

## October 20, 2021

Feature

Dialogflow ES V2 API now supports [regionalization](https://docs.cloud.google.com/dialogflow/es/docs/how/region).

## October 19, 2021

Feature

Dialogflow CX [change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history) is now available from the API.

Feature

Dialogflow CX now provides a [continuous testing and deployment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/continuous-tests) preview feature.

## October 15, 2021

Feature

Dialogflow CX has a new feature for side-by-side [flow version comparison](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version#compare).

## October 14, 2021

Feature

GA (general availability) launch of the following [languages](https://docs.cloud.google.com/dialogflow/es/docs/reference/language) in Dialogflow ES:

  * Bengali
  * Filipino
  * Finnish
  * Malay
  * Marathi
  * Romanian
  * Sinhala
  * Tamil
  * Telugu
  * Vietnamese



Feature

GA (general availability) launch of the following [languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) in Dialogflow CX:

  * Arabic
  * Bengali
  * Filipino
  * Finnish
  * Malay
  * Marathi
  * Romanian
  * Sinhala
  * Tamil
  * Telugu
  * Vietnamese



## September 01, 2021

Change

New [Dialogflow CX agent roles](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-control) are introduced for granular control of agent resources.

## August 26, 2021

Change

During the week of September 6, 2021, two new [Dialogflow IAM permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow) will become effective: `dialogflow.fulfillments.get` and `dialogflow.fulfillments.update` . If you use [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to grant access to the Dialogflow ES console and API, make sure to add these permissions to your custom roles to allow to create and update [Dialogflow ES Fulfillment](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-overview) in the Dialogflow ES console and via the API. If you don't use custom roles, no action is required.

## August 11, 2021

Feature

Dialogflow CX GA (generally available) launch of [Experiments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments) to compare the performance of flow versions to a control version while handling live traffic.

## July 22, 2021

Change

On July 26, 2021, two new [Dialogflow IAM permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/dialogflow) will become effective: `dialogflow.changelogs.get` and `dialogflow.changelogs.list`. If you use [custom roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) to grant access to the Dialogflow CX console, make sure to add these permissions to your custom roles to grant access to the [Change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history) functionality. If you don't use custom roles, no action is required.

Breaking

The root CA used for Dialogflow's client certificates for mutual TLS will change to GTS Root R1 in the week of July 26 2021. Please see the mTLS documentation for [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs/fulfillment-mtls) and [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/mtls) for details.

## July 02, 2021

Feature

In Dialogflow CX, you can now use the [Search](https://docs.cloud.google.com/dialogflow/cx/docs/concept/search) feature (Preview launch) to search, filter, and access the core resources within an agent.

Feature

In Dialogflow CX, you can now use the `sys.long-utterance` [built-in event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in) to handle user queries exceeding the [maximum length](https://docs.cloud.google.com/dialogflow/quotas#length_limits) (256 characters).

## June 30, 2021

Feature

The Dialogflow ES API now provides methods for managing [versions and environments](https://docs.cloud.google.com/dialogflow/es/docs/agents-versions).

## June 28, 2021

Feature

Dialogflow CX now supports the `asia-south1` (Mumbai) region.

## June 25, 2021

Feature

New [System functions](https://docs.cloud.google.com/dialogflow/cx/docs/reference/system-functions) are now available in Dialogflow CX.

## June 15, 2021

Deprecated

Final reminder: The [Dialogflow V1 API shutdown](https://docs.cloud.google.com/dialogflow/docs/release-notes#November_14_2019) will be finalized during the week of ~~June 21, 2021~~ July 12, 2021. All bots (except Actions on Google) using Dialogflow V1 API requests will stop responding. Consider migrating to [Dialogflow ES](https://docs.cloud.google.com/dialogflow/es/docs) or [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs).

## June 04, 2021

Change

Dialogflow CX will have new pricing on September 1, 2021. For details, see the [pricing documentation](https://cloud.google.com/dialogflow/pricing). In summary, the new pricing will be:

  * Text: $0.007/request
  * Audio: $0.06/minute



## May 14, 2021

Feature

Preview launch of the Dialogflow ES [Twilio telephony integration](https://docs.cloud.google.com/dialogflow/es/docs/integrations/twilio).

## April 26, 2021

Feature

Preview launch of the following [languages](https://docs.cloud.google.com/dialogflow/es/docs/reference/language) in Dialogflow ES:

  * Bengali
  * Filipino
  * Finnish
  * Malay
  * Marathi
  * Romanian
  * Sinhala
  * Tamil
  * Telugu
  * Vietnamese



## April 20, 2021

Feature

Preview launch of [Change history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/change-history) and [Auto sync](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-collaboration) in Dialogflow CX.

## April 19, 2021

Feature

Dialogflow CX now supports the `us-west1` (US, Oregon) [region](https://docs.cloud.google.com/dialogflow/cx/docs/concept/region).

## April 16, 2021

Feature

Preview launch of the [Dialogflow CX Phone Gateway](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway) integration.

## April 14, 2021

Change

The "Auto-preview changes" option was removed from the Dialogflow ES [Google Assistant](https://docs.cloud.google.com/dialogflow/es/docs/integrations/aog) integration.

## April 13, 2021

Feature

Preview launch of the [LINE](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/line) integration for Dialogflow CX.

Feature

Preview launch of the [Facebook Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/facebook-messenger) integration for Dialogflow CX.

Feature

Preview launch of the [Voximplant](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/voximplant) integration for Dialogflow CX.

## April 07, 2021

Feature

Preview launch of the following [languages](https://docs.cloud.google.com/dialogflow/cx/docs/reference/language) in Dialogflow CX:

  * Arabic
  * Bengali
  * Filipino
  * Finnish
  * Malay
  * Marathi
  * Romanian
  * Sinhala
  * Tamil
  * Telugu
  * Vietnamese



## April 01, 2021

Deprecated

The legacy analytics page has been removed from the Dialogflow ES console. Only the generally available [new analytics page](https://docs.cloud.google.com/dialogflow/es/docs/analytics) remains.

## March 03, 2021

Feature

Dialogflow now supports VPC Service Controls for both [CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/vpc-service-controls) and [ES](https://docs.cloud.google.com/dialogflow/es/docs/vpc-service-controls) agents.

## February 18, 2021

Feature

Dialogflow ES now supports the `europe-west1` (Belgium) [region](https://docs.cloud.google.com/dialogflow/es/docs/how/region#regions).

## February 02, 2021

Feature

Several new Dialogflow CX [prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt) have been launched. All of these prebuilt agents only support English at this time. The complete list of pre-built agents is currently:

  * Financial services agent (new)
  * Healthcare agent
  * Order and account management agent
  * Payment arrangement agent
  * Small talk agent (new)
  * Telecommunications agent (updated)
  * Travel: baggage claim agent (new)
  * Travel: car rental agent
  * Travel: flight information agent



## February 01, 2021

Feature

Dialogflow CX [conditions now support sentiment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/condition#sent).

## January 27, 2021

Feature

Dialogflow CX beta launch of [Experiments](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments) to compare the performance of flow versions to a control version while handling live traffic.

## January 21, 2021

Feature

Dialogflow CX [system entities](https://docs.cloud.google.com/dialogflow/cx/docs/concept/entity-system) can now be extended.

## December 15, 2020

Feature

GA (general availability) launch of [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs).

Feature

[CX Analytics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/analytics) for agent activity statistics.

Feature

[CX Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/dialogflow/cx/docs/concept/cmek) to manage your own Dialogflow data encryption keys.

Feature

[CX Parameter redaction](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#redact) to redact end-user parameter data from logs.

Feature

[CX Prebuilt agents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agents-prebuilt) for common agent use cases.

Feature

[CX Regionalization](https://docs.cloud.google.com/dialogflow/cx/docs/how/region) expanded to multiple regions globally.

Feature

[CX DTMF](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter#dtmf) input for telephony partner integrations.

Feature

[CX Security settings](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent#settings-security) to control data redaction and data retention.

## November 24, 2020

Feature

The Dialogflow CX [test cases](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case) feature is now launched and documented.

## November 20, 2020

Feature

The [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/dialogflow-messenger) integration is now implemented for Dialogflow CX.

Feature

[Agent Validation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/validation) is now implemented for Dialogflow CX.

## November 04, 2020

Feature

Dialogflow CX now supports the same [languages](https://docs.cloud.google.com/dialogflow/es/docs/reference/language) as Dialogflow ES.

Change

Since October 2020, Dialogflow ES no longer automatically creates service accounts upon agent creation. Some service accounts may still be [automatically created](https://docs.cloud.google.com/dialogflow/es/docs/access-control#auto-service-accounts) once you continue working with an agent.

## September 01, 2020

Feature

Beta launch of [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs). Dialogflow CX provides a new way of designing agents, taking a state machine approach to agent design. This gives you clear and explicit control over a conversation, a better end-user experience, and a better development workflow.

Change

The service previously named _Dialogflow_ is now called _Dialogflow ES_ , and the term _Dialogflow_ is now an umbrella term used to describe both the _Dialogflow ES_ and _Dialogflow CX_ services.

Change

As part of introducing Dialogflow CX, some changes have been made to [editions](https://docs.cloud.google.com/dialogflow/docs/editions):

  * _Dialogflow Enterprise Edition_ is no longer used as an umbrella term for paid editions. 
  * _Dialogflow Standard Edition_ is now called _Dialogflow Trial Edition_.
  * _Dialogflow Plus Edition_ and _Dialogflow Essentials Edition_ have been merged to one _Dialogflow Essentials (ES) Edition_.
  * _Dialogflow Customer Experience (CX) Edition_ is a new edition with a simpler pricing and quota model.



## August 10, 2020

Feature

Beta launch of [regionalization and data residency](https://docs.cloud.google.com/dialogflow/docs/how/region).

## July 30, 2020

Feature

GA (general availability) launch of [mega agents](https://docs.cloud.google.com/dialogflow/docs/agents-mega).

Feature

Beta launch of the [Facebook Workplace integration](https://docs.cloud.google.com/dialogflow/docs/integrations/workplace).

## July 27, 2020

Feature

Beta launch of [Dialogflow Messenger](https://docs.cloud.google.com/dialogflow/docs/integrations/dialogflow-messenger). This new integration provides a customizable chat dialog for your agent that can be embedded in your website.

## July 23, 2020

Deprecated

Amazon Alexa importer and exporter are no longer supported.

## July 06, 2020

Feature

The Dialogflow Console has been upgraded with an improved [Analytics page](https://docs.cloud.google.com/dialogflow/docs/analytics) (Beta) that provides new metrics and data views.

## June 29, 2020

Deprecated

The V1 API is in the process of a gradual shutdown. See the [November 14, 2019 release note](https://docs.cloud.google.com/dialogflow/docs/release-notes#November_14_2019) for details.

## June 01, 2020

Change

The shutdown of 7 integrations [announced in January](https://docs.cloud.google.com/dialogflow/docs/release-notes#January_06_2020) is now extended to July 6th, 2020.

## May 29, 2020

Change

The [Dialogflow Facebook Messenger integration](https://docs.cloud.google.com/dialogflow/docs/integrations/facebook) has been updated to to be compliant with newer Facebook Messenger API versions. If you have an agent that enabled this integration prior to today, you should have received an email from Dialogflow with upgrade instructions. If you have not received this email, please [contact Dialogflow support](https://docs.cloud.google.com/dialogflow/docs/support/getting-support).

## May 17, 2020

Change

Old Node.js client library require statements must be updated. Your require statements should look like this:

`const dialogflow = require('@google-cloud/dialogflow').v2;`

or this:

`const dialogflow = require('@google-cloud/dialogflow').v2beta1;`

Old syntax that does not include `@google-cloud` is now deprecated. The old syntax will continue to work, but you will not receive updates.

## May 08, 2020

Feature

Beta launch of a one-click integration with the [Voximplant](https://docs.cloud.google.com/dialogflow/docs/integrations/voximplant) telephony partner:

## May 05, 2020

Feature

GA (general availability) launch of [auto speech adaptation](https://docs.cloud.google.com/dialogflow/docs/speech-adaptation).

## April 30, 2020

Feature

Beta launch of a one-click integration with a new telephony partner:

  * [Avaya](https://docs.cloud.google.com/dialogflow/docs/integrations/avaya)



## April 25, 2020

Change

In May 2020, the [Facebook Messenger](https://docs.cloud.google.com/dialogflow/docs/integrations/facebook) integration will be updated, and you may notice slight changes related to fulfillment.

To make sure that your Facebook Messenger bot keeps functioning normally, observe the following recommendations:

  1. To get the Facebook `sender.id` value, use the `originalDetectIntentRequest.payload.data.sender` field from the Dialogflow `WebhookRequest` message.
  2. To get the `source` field value, use the `originalDetectIntentRequest.source` field from the Dialogflow `WebhookRequest` message.
  3. To send rich response messages from your webhook to the Facebook Messenger integration, use the `WebhookResponse.fulfillment_messages[].payload` field.
  4. In your webhook logic, don't rely on the fields that are not documented in the official [Facebook Messenger API](https://developers.facebook.com/docs/messenger-platform/reference/).



If you have any questions, reach out to your primary [support channel](https://docs.cloud.google.com/dialogflow/docs/support/getting-support#one-on-one).

## April 20, 2020

Feature

Beta launch of one-click integrations with two telephony partners:

  * [AudioCodes](https://docs.cloud.google.com/dialogflow/docs/integrations/audiocodes)
  * [SignalWire](https://docs.cloud.google.com/dialogflow/docs/integrations/signalwire)



## March 31, 2020

Change

When using fulfillment, the `WebhookResponse.payload` field can now only be used for two cases:

  * Custom data sent from your webhook service to a Dialogflow API caller.
  * Google Assistant integration custom payload rich response messages.



For all other [custom payload rich response messages](https://docs.cloud.google.com/dialogflow/docs/intents-rich-messages#custom), you should use the `WebhookResponse.fulfillment_messages[].payload` field.

## March 27, 2020

Change

The shutdown of the V1 API [announced in November](https://docs.cloud.google.com/dialogflow/docs/release-notes#November_14_2019) has been extended to May 31, 2020,

## March 13, 2020

Change

On March 16, 2020, the [Inline Editor](https://docs.cloud.google.com/dialogflow/docs/fulfillment-inline-editor) will use [Cloud Functions](https://docs.cloud.google.com/functions/docs) instead of [Cloud Functions for Firebase](https://firebase.google.com/docs/functions).

## March 10, 2020

Change

Event names are now [limited to 150 characters](https://docs.cloud.google.com/dialogflow/quotas#length_limits).

## February 19, 2020

Feature

You can now update fulfillment settings with the API. For more information, visit the [agent reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#agents) and click the link for your protocol or client library language.

Feature

GA (general availability) launch of [agent validation](https://docs.cloud.google.com/dialogflow/docs/agents-validation).

Feature

GA (general availability) launch of [versions and environments](https://docs.cloud.google.com/dialogflow/docs/agents-versions).

## January 31, 2020

Feature

Beta launch of [mega agents](https://docs.cloud.google.com/dialogflow/docs/agents-mega) to combine multiple sub-agents agents into a single mega agent.

## January 06, 2020

Deprecated

The following [integrations](https://docs.cloud.google.com/dialogflow/docs/integrations) are now deprecated and will be shut down on ~~April 6th, 2020~~ ~~May 6th, 2020~~ ~~June 6th, 2020~~ July 6th, 2020 :

  * Kik
  * Skype
  * Spark
  * Twilio IP Messaging
  * Twilio (Text Messaging)
  * Twitter
  * Viber



Your live bots that use these integrations will stop working unless you take action. The implementations of these integrations have moved to open source. To continue using these integrations, follow the instructions at the [GitHub repository](https://github.com/GoogleCloudPlatform/dialogflow-integrations).

## December 19, 2019

Change

If you use the [Telegram](https://docs.cloud.google.com/dialogflow/docs/integrations/telegram) integration, and the bot was created before August 19th, 2019, you must restart the integration in the Dialogflow console by February 28th, 2020. To restart it, perform the following steps for all your agents that use Telegram:

  1. Make sure you don't change or delete your current token on the Telegram side.
  2. Open the agent in the Dialoglow Console.
  3. In the integration settings, click the **STOP** button.
  4. Then click the **START** button.



## December 04, 2019

Feature

You can now use [Mutual TLS authentication](https://docs.cloud.google.com/dialogflow/docs/fulfillment-mtls) to ensure that webhook traffic is both secure and trusted.

Deprecated

The Cortana exporter has been removed from the console.

## November 14, 2019

Change

We are extending the V1 API shutdown deadline to ~~March 31st, 2020~~ May 31st, 2020. Migrate to the V2 API as described [here](https://dialogflow.com/docs/reference/v1-v2-migration-guide).

If you use Dialogflow exclusively for Actions on Google, you don't need to migrate your agent to the V2 API. However, note the following changes:

  * The Dialogflow simulator will show responses in the V2 format and the "Copy curl" button will generate requests in the V2 format. This should have no impact on the functionality of the Actions on Google simulator.
  * You will no longer be able to call API methods for the V1 [intents](https://dialogflow.com/docs/reference/agent/intents) and [entities](https://dialogflow.com/docs/reference/agent/entities) resources. You will still be able to modify your agent using the Dialogflow Console.



## October 17, 2019

Change

When calling the API to provide an intent priority value, the behavior has changed to the following:

  * If the supplied value is unspecified or 0, the service translates the value to 500,000, which corresponds to the `Normal` priority in the console.
  * If the supplied value is negative, the intent is ignored in runtime detect intent requests.



Prior to this change, a value of 0 was stored as-is by the service. Any agents created before this change may still have intent priority values of 0. For runtime detect intent requests, a value of 0 is treated as -1, and the intent is ignored.

## October 01, 2019

Feature

You can now [create session entities with fulfillment](https://docs.cloud.google.com/dialogflow/docs/entities-session).

Feature

You can now disable automatic agent training. See the [ML settings](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml) for details.

## September 20, 2019

Feature

Beta launch of [Agent Validation](https://docs.cloud.google.com/dialogflow/docs/agents-validation) to check your agent for quality and correctness.

## September 19, 2019

Feature

You can now use [System entity extension](https://docs.cloud.google.com/dialogflow/docs/entities-system-extension) to extend system entities with custom values.

## September 13, 2019

Feature

You can now use [Fuzzy matching](https://docs.cloud.google.com/dialogflow/docs/entities-fuzzy) to allow flexibility with word ordering for multi-word entities.

Feature

You can now use [Regexp entities](https://docs.cloud.google.com/dialogflow/docs/entities-regexp) to provide regular expressions for matching entities.

## July 23, 2019

Feature

Beta launch of [Auto speech adaptation](https://docs.cloud.google.com/dialogflow/docs/speech-adaptation) to improve the speech recognition accuracy of your agent.

## June 13, 2019

Feature

You can now create and update agents with the API. See the [Agents type reference](https://docs.cloud.google.com/dialogflow/docs/reference/common-types#agents).

## May 23, 2019

Feature

All REST command line samples in documentation now include both curl (Linux, macOS) and PowerShell (Windows) commands.

Feature

GA (general availability) launch of [Sentiment analysis](https://docs.cloud.google.com/dialogflow/docs/sentiment).

Feature

GA (general availability) launch of [Speech response](https://docs.cloud.google.com/dialogflow/docs/detect-intent-tts).

Change

[Pricing](https://cloud.google.com/dialogflow/pricing) and [Quotas](https://docs.cloud.google.com/dialogflow/quotas) have been updated for speech response and sentiment analysis.

## May 15, 2019

Feature

Integration with [Hangouts Chat](https://docs.cloud.google.com/dialogflow/docs/integrations/hangouts) is now supported.

## April 18, 2019

Feature

The new `@sys.person` [system entity](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) has been added to all languages except Portuguese and Ukrainian. It is used for given names, last names, or their combinations. You should start using `@sys.person` instead of the existing `@sys.given-name` and `@sys.last-name` system entities.

## January 15, 2019

Feature

Added support for Polish, including new [system entities](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) and [pre-defined follow-up intents](https://docs.cloud.google.com/dialogflow/docs/reference/follow-up-intent-expressions).

## December 18, 2018

Feature

Added support for Turkish, including new [system entities](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) and [pre-defined follow-up intents](https://docs.cloud.google.com/dialogflow/docs/reference/follow-up-intent-expressions).

Deprecated

You can no longer annotate training phrases with some locale-specific entities. These entities are marked as deprecated in the [system entities](https://docs.cloud.google.com/dialogflow/docs/reference/system-entities) documentation. However, if you already have training phrases annotated with these entities in your existing agents, they will continue to function properly.

## December 04, 2018

Deprecated

Template mode has been deprecated. Example mode is the only supported way to create new training phrases. If you have existing training phrases that you've created in template mode, those will continue to work. For more information, see [Example and template modes](https://docs.cloud.google.com/dialogflow/docs/intents-training-phrases#example_and_template_modes)

## September 20, 2018

Feature

Added zh-TW machine learning support.

## August 09, 2018

Feature

The Dialogflow Enterprise Edition _Plus_ pricing plan is now available. See [Editions](https://docs.cloud.google.com/dialogflow/docs/editions) for details.

## July 24, 2018

Feature

Beta launch of [Knowledge Connectors](https://docs.cloud.google.com/dialogflow/docs/knowledge-connectors)

Feature

Beta launch of [Telephony Gateway](https://docs.cloud.google.com/dialogflow/docs/telephony)

Feature

Beta launch of [Adding Sentiment Analysis to Detect Intent Requests](https://docs.cloud.google.com/dialogflow/docs/sentiment)

Feature

Beta launch of [Adding Speech Response to Detect Intent Requests](https://docs.cloud.google.com/dialogflow/docs/detect-intent-tts)

Feature

Beta launch of [Data Logging and Enhanced Speech Models](https://docs.cloud.google.com/dialogflow/docs/concepts/data-logging)

Feature

Beta launch of [Automatic Spell Correction](https://docs.cloud.google.com/dialogflow/docs/agents-settings#ml_settings_machine_learning)

## May 08, 2018

Feature

You can now enable and view [Stackdriver logs](https://docs.cloud.google.com/dialogflow/docs/history#webhook_errors_in_stackdriver_logs) for your fulfillment.

Feature

The following geography system entities have been added to pt-BR, Nl, Ko, Hi, Id, Th, No, Sv, and Da languages: @sys.geo-country, @sys.geo-city, and @sys.geo-capital.

Feature

The [Versions and Environments](https://cloudplatform.googleblog.com/2018/05/Dialogflow-adds-versioning-and-other-new-features-to-help-enterprises-build-vibrant-conversational-experiences.html) beta feature has launched.

Feature

When a phrase is matched to an intent when it shouldn't be, you can now designate it as a [negative example](https://docs.cloud.google.com/dialogflow/docs/intents-default#default_fallback_intent) and add it to the Default Fallback Intent.

## April 17, 2018

Change

The Dialogflow V2 API is now GA (general availability). See [the Google Cloud blog post](https://cloudplatform.googleblog.com/2018/04/Dialogflow-Enterprise-Edition-is-now-generally-available.html) for details. Users of the V2beta1 API are encouraged to migrate to the V2 API. See [Migrating code from Dialogflow V2beta1 to V2](https://docs.cloud.google.com/dialogflow/docs/migrating#v2beta1-to-v2) for instructions. The V2beta1 API will continue to be a beta channel for the stable V2 API. If you plan to continue using V2beta1, see the migration instructions which describe how enabling ML will become the default.

## March 29, 2018

Feature

We added additional system entities for the following languages:

  * Hindi (hi)
  * Thai (th)
  * Indonesian (id)
  * Swedish (sv)
  * Danish (da)
  * Norwegian (no)



## February 22, 2018

Feature

We added additional support for these languages:

  * Hindi (hi)
  * Thai (th)
  * Indonesian (id)
  * Swedish (sv)
  * Danish (da)
  * Norwegian (no)



We added ML support for these languages:

  * Brazilian Portuguese (br-PT)
  * Korean (ko)
  * Dutch (nl)



## December 01, 2017

Change

We updated these prebuilt agents: flights (added FAQ) and profile bot (renamed to "Job Interview").

Feature

We added new prebuilt agents: banking, easter egg, mobile account, and online shopping

## November 16, 2017

Feature

Dialogflow Beta release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
