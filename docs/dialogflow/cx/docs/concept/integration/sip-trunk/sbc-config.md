---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config/
title: SBC configuration and validation \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:42:44.874692+00:00
---

# SBC configuration and validation  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  SBC configuration and validation Stay organized with collections  Save and categorize content based on your preferences. 

This document helps you configure and validate the SBC.

## Supported vendors and firmware

Before you begin the configuration, review the table of [supported SBC vendors or models and firmware versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_vendors_or_models).

## Supported SBC signaling and media protocols

You can find the supported signaling and media protocols in the [SBC signaling and media protocols documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_signaling_and_media_protocols).

## SBC's TLS configuration

Request a TLS certificate for the SBC from an approved certificate authority vendor. Wildcard certificates aren't supported.

Within the TLS certificate, you must present the fully qualified domain name (FQDN) of the SBC either in the common name (CN) attribute or in the subject alternative name (SAN) attribute. If you request one TLS certificate for multiple SBCs, the SAN of the certificate must include all SBC FQDNs.

Approved certificate authority vendors:

  * DigiCert
  * Entrust DataCard
  * GlobalSign
  * GoDaddy
  * Sectigo (previously known as Comodo)



### Configure SBC TLS

  1. Install the requested TLS certificate along with the associated root CA certificate to your SBC's trust chain.
  2. Install Google's trusted root CA into your SBC's trust chain. To get the Google root certificate, complete the following steps: 
     1. Download Google's [trusted root CAs](https://pki.goog/roots.pem).
     2. Extract the root certificates.
     3. Upload the full root bundle to your SBC keystore.
     4. If required, enable certificate revocation lists (CRLs).
     5. Enable mutual authentication for the SBC.
  3. Configure supported TLS versions and cipher suites. Versions 1.2 or later are supported, along with the following cipher suites: 
     * `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
     * `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`
     * `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
     * `TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
     * `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
     * `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
     * `TLS_AES_256_GCM_SHA384`
     * `TLS_CHACHA20_POLY1305_SHA256`
     * `TLS_AES_128_GCM_SHA256`



## Create a SIP trunk on GTP

  1. Go to the [Unified Console](https://ccai.cloud.google.com/projects) {:.button .button-primary} and select your project.
  2. Go to the **SIP Trunks** tab, and then click **Add a SIP Trunk**.
  3. Fill in all required fields.
  4. Click **Create**.



## Review telephony connectivity network requirements

See the [concepts and troubleshooting page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#telephony_network_requirements) for a table of network and connectivity requirements.

## Configure SBC for SIP connection to GTP

If your SBC is configured using one of the supported and certified SBC vendors, see the [SBC signaling and media protocols documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_signaling_and_media_protocols) for detailed instructions specific to that vendor.

Configure the SIP profile to use TLS over TCP port 5672 targeting specific regionalized GTP SIP servers (for example, `us.telephony.goog`).

Configure SIP and SIPREC integration as follows:

  * For the use case of connecting to Dialogflow virtual agents, configure SIP integration on the SBC.
  * For the use case of Conversational AI Agent Assist or Insights, configure SIPREC integration on the SBC so copies of the media stream are forked to GTP. Note that using SIPREC with certain SBC vendors can be a separate licensed feature that you must purchase and activate.



## SIP connectivity test with SIP OPTIONS ping

Perform a SIP OPTIONS ping test from the customer SBC to GTP to help ensure that your SBC receives a `SIP 200 OK` from GTP. If `SIP 200 OK` isn't received, see the SIP [troubleshooting section](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#troubleshooting).

## SIP header configuration for Conversational AI conversations

  1. Set the Conversational AI conversation ID by configuring the SIP header (`Call-Info` or UUI) during SIP INVITE.
  2. Use the `Call-Info` SIP header. If that isn't supported, you can use the User-to-User-Info (UUI) SIP header. For more information about SIP headers, see [SIP headers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#sip_headers).
  3. Optional: Configure participant roles (`END_USER` and `HUMAN_AGENT`) and media stream order. For more information about participant roles, see [participant roles](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#configure_participant_roles_and_media_stream_order).
  4. Optional: Configure additional parameters for a given conversation by calling the `MatchIntentRequest` API. For more information about additional parameters, see [additional parameters](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#set_additional_parameters_on_a_given_conversation).



## Perform test calls

Conduct a test call and verify that SIP and media traverse to GTP SIP servers (`74.125.88.128/25`) and RTP media servers (`74.125.39.0/24`). You can expect a `SIP 200 OK` response message.

If you receive a `SIP 400` error response code, it's likely that GTP rejected either the SIP header or SIP media SDP configuration. Refer to the [troubleshooting section](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#troubleshooting) for details. If you receive a `SIP 600` error response code, it's likely that you have a quota-related issue.

## Review Dialogflow conversation history

This section applies only if you deploy a Dialogflow virtual agent.

If the previous test call resulted in a `SIP 200 OK` response, check the Conversational AI Google Cloud project's Dialogflow [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history#browser) to help ensure that new conversations are logged and include the conversation ID specified in the call info header.

## (Optional) Review Google Cloud Logs Explorer

Check Dialogflow activity in the Conversational AI Google Cloud project's Logs Explorer "incoming_call" log:

  1. Use the following query to review Dialogflow's incoming call activities, and then click **Run query** :
         
         logName="projects/PROJECT_ID/logs/dialogflow.googleapis.com%2Fincoming_call"
         

     * `PROJECT_ID`: the Google Cloud project ID that you used to configure the telephony integration.
  2. Alternatively, go to the Logs Explorer's **All log names** list and search for log name `incoming_call`. Select it and click **Apply**.

  3. If audit logging is [enabled for the Dialogflow API](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#audit-logging), then verify that Dialogflow created a conversation successfully in the Conversational AI Google Cloud project's Logs Explorer. Use the following query to review Dialogflow's conversation creation events from a specific Google Cloud project and conversation profile, and then click **Run query**.
         
         protoPayload.serviceName=~"dialogflow"
         protoPayload.methodName=~"google.cloud.dialogflow.*.Conversations.CreateConversation"
         protoPayload.request.conversation.conversationProfile="projects/PROJECT_ID/locations/global/conversationProfiles/CONVERSATION_PROFILE_ID"
         

     * `PROJECT_ID`: the Google Cloud project ID defined when you [configured the integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#select-project).
     * `CONVERSATION_PROFILE_ID`: the conversation profile ID you created when you [configured the integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#configure-profile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
