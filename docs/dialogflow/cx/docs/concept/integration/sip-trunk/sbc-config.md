---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config/
title: SBC configuration and validation \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:48.603058+00:00
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

This page walks you through the process of configuring and validating the SBC.

## Supported vendors and firmware

Before you begin the configuration, review the table of [supported SBC vendors or models and firmware versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_vendors_or_models).

## Supported SBC signaling and media protocols

The supported signaling and media protocols are specified in the [SBC signaling and media protocols documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_signaling_and_media_protocols).

## SBC's TLS configuration

Request a TLS certificate for the SBC from an approved certificate authority vendor. Wildcard certificates are not supported.

Within the TLS certificate, you must present the SBC's fully qualified domain name (FQDN) either in the common name (CN) attribute or in the subject alternative name (SAN) attribute. If you request one TLS certificate for multiple SBCs, the certificate's SAN should include all SBC FQDNs.

Approved certificate authority vendors

  * DigiCert
  * Entrust DataCard
  * GlobalSign
  * GoDaddy
  * Sectigo (Formerly known as Comodo)



### Configure SBC TLS

  1. Install the requested TLS certificate along with the associated root CA certificate to the SBC's trust chain.
  2. Install Google's trusted root CA into SBC's trust chain. To get the Google Root certificate:

     1. Download Google's [trusted root CAs](https://pki.goog/roots.pem).
     2. Extract the Root certificates.
     3. Upload the full root bundle to your SBC keystore.
     4. If required, enable Certificate Revocation Lists (CRLs)
     5. Enable mutual authentication for the SBC.
  3. Configure supported TLS versions and cipher suites. TLS versions 1.2 or later are supported. Supported cipher suites:

     * `TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256`
     * `TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256`
     * `TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256`
     * `HTLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256`
     * `TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384`
     * `TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`
     * `TLS_AES_256_GCM_SHA384`
     * `TLS_CHACHA20_POLY1305_SHA256`
     * `TLS_AES_128_GCM_SHA256`



## Create a SIP trunk on GTP

  1. Navigate to the [Unified Console](https://ccai.cloud.google.com/projects) and select your project.
  2. Navigate to the **SIP Trunks** tab, then click **Add a SIP Trunk**.
  3. Fill in all required fields.
  4. Click **Create**.



## Review telephony connectivity network requirements

See the [concepts and troubleshooting page](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#telephony_network_requirements) for a table of network and connectivity requirements.

## Configure SBC for SIP connection to GTP

If your SBC is deployed with one of the supported and certified SBC vendors, see the [SBC signaling and media protocols documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#supported_sbc_signaling_and_media_protocols) for detailed instructions specific to that vendor.

Ensure that the SIP profile is configured to use TLS over TCP port 5672 targeting specific regionalized GTP's SIP servers (for example, `us.telephony.goog`). SIP and SIPREC integration configuration:

  * For the use case of connecting to Dialogflow virtual agents, configure SIP integration on the SBC.
  * For the use case of Conversational AI Agent Assist or Insights, configure SIPREC integration on the SBC so copies of the media stream are forked to GTP. Note that using SIPREC with certain SBC vendors might be a separate licensed feature that you must purchase and activate.



## SIP connectivity test with SIP OPTIONS ping

Perform a SIP OPTIONS ping test from customer SBC to GTP to ensure that your SBC receives a `SIP 200 OK` from GTP. If `SIP 200 OK` is not received, refer to the SIP [troubleshooting section](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#troubleshooting) for more details.

## SIP header configuration for Conversational AI conversations

  1. Set Conversational AI's Conversation ID by configuring the SIP header (`Call-Info` or UUI) during SIP INVITE.
  2. Use the `Call-Info` SIP header. If that is not supported, you can use the User-to-User-Info (UUI) SIP header. Refer to [SIP headers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#sip_headers) for more details.
  3. (Optional) Configure participant roles (`END_USER` and `HUMAN_AGENT`) and media stream order. Refer to the [participant roles](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#configure_participant_roles_and_media_stream_order) section for details.
  4. (Optional) To set additional parameters for a given conversation, call the `MatchIntentRequest` API. Refer to the [additional parameters section](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#set_additional_parameters_on_a_given_conversation) for details.



## Perform test calls

Conduct a test call and check to ensure SIP and media are traversing to GTP SIP servers (`74.125.88.128/25`) and RTP media servers (`74.125.39.0/24`). You should get a `SIP 200 OK` response message.

If you receive a `SIP 400's` error response code it likely indicates that GTP rejected either the SIP header or SIP media SDP configuration. Refer to the [troubleshooting section](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#troubleshooting) for details. If you receive a `SIP 600's` error response code, it likely indicates a quota-related issue.

## Review Dialogflow conversation history

This section applies only if you deploy a Dialogflow virtual agent.

If the previous test call resulted in a `SIP 200 OK` response, check the Conversational AI Google Cloud project's Dialogflow [conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/conversation-history#browser) to make sure new conversations are being logged and include the conversation ID specified in the call info header.

## (Optional) Review Google Cloud Logs Explorer

Check Dialogflow activity in the Conversational AI Google Cloud project's Logs Explorer "incoming_call" log.

  1. Use the following query to review Dialogflow's incoming call activities, then click "Run query":

`logName="projects/$PROJECT_ID/logs/dialogflow.googleapis.com%2Fincoming_call`

`$PROJECT_ID` = The Google Cloud project ID that you used to configure the telephony integration.

  2. Alternatively, you can navigate to the Logs Explorer's **All log names** drop down box and search for log name `incoming_call`. Select it and click **Apply**.

  3. Verify that Dialogflow created a conversation successfully in the Google Cloud project's Logs Explorer (this step only applies if audit logging is [enabled for the Dialogflow API](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#audit-logging)). Use the following query to review Dialogflow's conversation creation events from a specific Google Cloud project and conversation profile, then click **Run query**.
         
         protoPayload.serviceName=~"dialogflow"
         protoPayload.methodName=~"google.cloud.dialogflow.*.Conversations.CreateConversation"
         protoPayload.request.conversation.conversationProfile="projects/$PROJECT_ID/locations/global/conversationProfiles/$CONVERSATION_PROFILE_ID"
         

     * `$PROJECT_ID` = The Google Cloud project ID defined when you [configured the integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#select-project).
     * `$CONVERSATION_PROFILE_ID` = The conversation profile ID you created when you [configured the integration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#configure-profile).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
