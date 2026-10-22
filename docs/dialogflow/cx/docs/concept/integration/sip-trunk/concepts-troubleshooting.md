---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting/
title: Concepts and troubleshooting \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:04.961404+00:00
---

# Concepts and troubleshooting  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Concepts and troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This page details specific configurations required for integration as well as troubleshooting for common issues.

## Telephony network requirements

If your network filters outbound traffic, it must allow outbound traffic for SIP signaling and media streaming.

For SIP signaling, the whole IP range 74.125.88.128/25 (TCP) over port 5672 should be allowed. For a more restrictive firewall rule set, you may restrict SIP signaling to just one or more regionalized GTP SIP servers:

  * US region: `us.telephony.goog` (74.125.88.132)
  * EU region: `eu.telephony.goog` (74.125.88.133)
  * APAC region: `ap.telephony.goog` (74.125.88.134)
  * South America region: `sa.telephony.goog` (74.125.88.135)



For RTP media, you must configure firewall rules to allow traffic destined to the CIDR IP range 74.125.39.0/24. Typically the ports required for media are only 16384-32767 (TCP+UDP), however, this port range may be expanded in the future.

## Supported SBC vendors or models

The following table lists the supported SBC vendors or models and firmware versions. Detailed integration instructions for each vendor are linked in the firmware version.

Vendors and models | Firmware versions  
---|---  
AudioCodes VE SBC | v7.60A.100.022 ([SIPREC](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/audiocodes_siprec.pdf), [SIP](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/audiocodes_sip_agent_handoff.pdf))  
Avaya Session Border Controller for Enterprise | v10.2.1.1-104-25336 ([SIPREC](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/avaya_siprec.pdf), [SIP](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/avaya_sip_agent_handoff.pdf))  
Oracle E-SBC Acme Packet 4600 | SCZ9.3.0 GA (Build 46) ([SIPREC](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/oracle_siprec.pdf), [SIP](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/oracle_sip_agent_handoff.pdf))  
Ribbon Swe Core SBC | v12.01.07R000 ([SIPREC](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/ribbon_siprec.pdf), [SIP](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/ribbon_sip_agent_handoff.pdf))  
Cisco Unified Border Element (CUBE) | v17.15.4 ([SIPREC](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/cisco_siprec.pdf), [SIP](https://docs.cloud.google.com/static/dialogflow/cx/docs/data/cisco_sip_agent_handoff.pdf))  
**Note:** This table represents the minimum supported firmware versions that have been certified to work with SIP integration. Newer firmware versions that are a part of the same major firmware patch series are also certified.

## Supported SBC signaling and media protocols

|   
---|---  
Signaling Protocol | SIP over TLS  
Media | SRTP  
Media Encryption | SDES  
Media Cipher Suite Supported | AES_CM_128_HMAC_SHA1_80, AEAD_AES_256_GCM  
Media Codecs Supported | G.711 µ-law (PCMU), G.711 A-law (PCMA), Opus  
  
## SIP headers

When you [set up a conversation profile and phone number](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup#configure-profile), you created a CCAI conversation profile with the `sipConfig.createConversationOnTheFly` set to `true`. The conversation ID should be dynamically generated during the SIP INVITE by using the SIP header value of `Call-Info` or `UUI`.

The SIP header value points to the Dialogflow endpoint by defining the Google Cloud project ID and conversation ID:

  1. The Google Cloud project ID is the project you used when you [set up a Google Cloud project](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup).
  2. The [conversation ID](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v2beta1/projects.conversations/create#query-parameters) should be dynamically generated by the SBC. The conversation ID must be compliant with the regular expression formula `[a-zA-Z][a-zA-Z0-9_-]*` with the characters length in range of `[3,64]`. To dynamically generate the conversation ID, a common pattern is to use the Call-ID value in the SIP INVITE and prefix it with letters to make it compliant with the regular expression as specified previously. For example, if the Call-ID value is `297363723_79131759_799783510`, prefixing the Call-ID value with `"CID-"` would make it compliant with the regular expression `[a-zA-Z][a-zA-Z0-9_-]*`.



### `Call-Info` SIP header

Insert a custom SIP header called `Call-Info` in the SIP INVITE to uniquely set the conversation ID:
    
    
    Call-Info: <http://dialogflow.googleapis.com/v2beta1/projects/$PROJECT_ID/conversations/$CONVERSATION_ID>;purpose=Goog-ContactCenter-Conversation
    

Example:
    
    
    Call-Info: <http://dialogflow.googleapis.com/v2beta1/projects/gcp-project-id-12345/conversations/CID-297363723_79131759_799783510>;purpose=Goog-ContactCenter-Conversation
    

### `UUI` SIP header

If setting the custom SIP header `Call-Info` is not supported, you can configure the `UUI` (User-to-User) SIP header in the SIP INVITE to pass in the conversation ID.

Use the same data requested in `Call-Info` with the URL encoded in hex and the purpose set to `Goog-ContactCenter-Conversation`. The following is an example header, where the hex string when decoded is `http://dialogflow.googleapis.com/v2beta1/projects/gcp-project-id-12345/conversations/CID-297363723_79131759_799783510`:
    
    
    User-to-User: 687474703a2f2f6469616c6f67666c6f772e676f6f676c65617069732e636f6d2f763262657461312f70726f6a656374732f6763702d70726f6a6563742d69642d31323334352f636f6e766572736174696f6e732f4349442d3239373336333732335f37393133313735395f373939373833353130;encoding=hex;purpose=Goog-ContactCenter-Conversation
    

If additional data needs to be passed into the agent and set as a session parameter, you can do so by passing in a semicolon separated list of key value pairs that is hex encoded, followed by `;encoding=hex;purpose=Goog-Session-Param`. This will result in a session parameter created with the name `uui-headers` containing a list of decoded payload strings.

For example, if the string `key1=value1;key2=value2` needed to be passed in, the following UUI header would be sent, where the payload is the hex encoded value of `key1=value1;key2=value2`.
    
    
    User-to-User: 6B6579313D76616C7565313B6B6579323D76616C756532;encoding=hex;purpose=Goog-Session-Param
    

which would result in the following session parameter being created.
    
    
    {
        "uui-headers": ["key1=value1;key2=value2"]
    }
    

If your SBC supports sending multiple UUI headers, you can send individual key value strings per UUI header and they would be available as individual values in the `uui-headers` session parameter.

The following snippet takes the parameter value and then splits the parameter multiple times to access the appropriate value for the `key2` variable in the string.
    
    
    $sys.func.GET($sys.func.SPLIT($sys.func.GET($sys.func.SPLIT($session.params.uui-headers,";"),1),"="),1)
    

The following example shows a function that is called from a trigger in the Playbook's code blocks, eg. @PlaybookStartHandler, which is called on entering the Playbook. Other functions call this function to get values from the `uui-headers` parameter.
    
    
    def _get_fromuui(attribute):
        try:
            uui_headers_src = history.playbook_input.action_parameters['uui-headers']
            # If uui_headers_src is a string, split by ';'
            if isinstance(uui_headers_src, str):
                headers = uui_headers_src.split(';')
            else:
                # If it's a list, join and split
                headers = ';'.join(uui_headers_src).split(';')
            for header in headers:
                header = header.strip()
                if header.lower().startswith(f"{attribute.lower()}="):
                    return header[len(attribute) + 1:]
            return ""
        except Exception:
            return ""
    

Additional data can be sent using separate `UUI` headers having different "purpose" values. These values are added to the [`Conversation.telephonyConnectionInfo`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v2beta1/projects.conversations#resource:-conversation) object. Note that this data is not available to the Dialogflow CX agent at runtime.

### SIP x-headers

SIP headers starting with `x-` can be passed to the agent and set as a session parameter. The SIP headers are available in the `x-headers` session parameter. The `x-` prefix is removed from the header name in the session parameter.

For example, if the SIP INVITE contains the following header:
    
    
    x-billing-id: 12345
    

The session parameter `x-headers` will contain:
    
    
    {
        "x-headers": {
            "billing-id": "12345"
        }
    }
    

To access the value:
    
    
    $session.params.x-headers.billing-id
    

### Pass in human-agent information

If you need to pass information specific to human agents, you can set the Session Description Protocol (SDP) media label attribute, for the human-agent, Real-time Transport Protocol (RTP) stream to the required data value. Example: `none a=label:7382373482` This data will be populated in the [`sip_recording_media_label`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.v2beta1#google.cloud.dialogflow.v2beta1.Participant) field and available in the `New message notification` pubsub topic containing the transcripts. Look for the `sip_recording_media_label` field in the pubsub [`Message.attributes`](https://docs.cloud.google.com/python/docs/reference/pubsub/latest/google.cloud.pubsub_v1.subscriber.message.Message) message.

**Warning:** For compliance reasons, don't pass any PII user data in SIP headers. They should be used to pass non-PII key and value pairs only.

## Configure participant roles and media stream order

By default, the first media stream is associated with the `END_USER` participant role and subsequent media streams are associated with the `HUMAN_AGENT` participant role.

If you require different behavior (for example, in an outbound calling system), then the URL passed in the header should have the roles parameter appended.

Example: `none http://dialogflow.googleapis.com/v2beta1/projects/gcp-project-id-12345/conversations/CID-297363723_79131759_799783510?roles=HUMAN_AGENT,END_USER`

The URL specifies that the first media stream should have the `HUMAN_AGENT` role and the second media stream should have the `END_USER` role. You can apply the roles parameter with the [`Call-Info` or `UUI` SIP header](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#sip_headers).

## Set additional parameters on a given conversation

To set additional parameters on a given conversation, use the [`MatchIntentRequest`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#google.cloud.dialogflow.cx.v3.MatchIntentRequest) RPC call. You can set `query_params.parameters` to the required key value pairs and `query_input.text` to something like 'Setting parameters'.

Make the API call after the 200 OK response for the initial SIP INVITE, at which point the conversation has been created. The session ID for the `MatchIntentRequest` is the same conversation ID provided in the `Call-Info` header in the INVITE.

## Use `SIP REFER` to transfer a call to a SIP endpoint

To transfer a call from a virtual agent to a SIP endpoint, use the SIP REFER method. Include a payload in the `Live agent handoff` field and set the `Telephony transfer call` field to the number that's set in the outbound `SIP REFER` `Refer-To` field. Your `Live agent handoff` payload should look similar to the following code sample.
    
    
    {
        "sip-refer": true
    }
    

If data needs to be passed out of Dialogflow CX, UUI headers and x-headers can be used to pass out strings of data. If you wanted to do a `SIP REFER` and pass out 2 key value pairs in a UUI header and 2 x-headers, you could use a `Live agent handoff` payload similar to the following code sample.
    
    
    {
        "sip-refer": true,
        "uui-headers": [
            "key1=value1;key2=value2"
        ],
        "x-headers": {
            "header1": "value1",
            "header2": "value2"
        }
    }
    

This would generate a SIP REFER with the following UUI and x-headers.
    
    
    User-to-User: <hex encoded "key1=value1;key2=value2">;encoding=hex;purpose=Goog-Session-Param
    x-header1: value1
    x-header2: value2
    

## Use `SIP INVITE` to conference a call with another SIP endpoint

To conference a call from an end customer to a human agent accessible using a SIP endpoint, use the SIP INVITE method. This keeps Google in the media path and allows use of Agent Assist features. Set the `Telephony transfer call` field to the number that's set in the outbound `SIP INVITE` `To` field.

If data needs to be passed out of Dialogflow CX, UUI headers and x-headers can be used to pass out strings of data. If you wanted to do a `SIP INVITE` and pass out 2 key value pairs in a UUI header and 2 x-headers, you could use a `Live agent handoff` payload similar to the following code sample.
    
    
    {
        "uui-headers": [
            "key1=value1;key2=value2"
        ],
        "x-headers": {
            "header1": "value1",
            "header2": "value2"
        }
    }
    

This would generate a SIP INVITE with the following UUI and x-headers.
    
    
    User-to-User: <hex encoded "key1=value1;key2=value2">;encoding=hex;purpose=Goog-Session-Param
    x-header1: value1
    x-header2: value2
    

## Pass data out in a SIP BYE

Navigating to `End Session` will trigger a SIP BYE. If you want to pass data out of Dialogflow CX, UUI headers or x-headers can be used to pass out strings of data. You would route the call to a page that defined the `Live agent handoff` payload similar to the following code sample before transitioning to `End Session`.
    
    
    {
        "uui-headers": [
            "key1=value1;key2=value2"
        ],
        "x-headers": {
            "header1": "value1",
            "header2": "value2"
        }
    }
    

This would generate a SIP BYE with the following UUI and x-headers.
    
    
    User-to-User: <hex encoded "key1=value1;key2=value2">;encoding=hex;purpose=Goog-Session-Param
    x-header1: value1
    x-header2: value2
    

## Trigger an action when the remote caller hangs up

The new BiDi API (`use_bidi_streaming=True` in the ConversationProfile) supports triggering a tool call within a playbook or a webhook call within a flow when the remote caller hangs up.

When the remote caller hangs up and Dialogflow CX receives a SIP BYE message, the custom event `sys.remote-call-disconnected` is triggered. If you create a handler with this specific event name, you can then use it to trigger a tool call with a playbook or a webhook call within a flow.

## Allow calls from SBC only

To decline calls from the PSTN and only connect calls originating from your SBC, update the [`PhoneNumber`](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2beta1/projects.locations.phoneNumbers) object to specify the `allowedSipTrunks` message. If the integration uses a SIP trunk, you can specify a list of specific SIP trunk IDs. If the message is created with an empty list, then any SIP trunk is allowed. If a private interconnect is established, provide the carrier ID provisioned by the Google Telephony team.

## Troubleshooting

The Google team might ask you to provide the following artifacts to aid in troubleshooting of the SIP OPTIONS ping and the test calls conducted:

  1. Network packet capture
  2. SIP debug trace showing full header and SIP SDP: 
     * Call-ID value
     * `Call-Info` value (if exist)



### Network packet capture

The network packet capture should show the following:

  1. A complete 3-way TCP handshake (SYN, SYN-ACK, ACK) between the your SBC to GTP SIP servers communicated over TCP port 5672. If TCP connection failed to be established, possible issues are:

     * Your network is blocking outbound traffic.
     * Communication is not being sent to one of the regionalized GTP SIP server. See [Telephony connectivity network requirement](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/concepts-troubleshooting#telephony_network_requirements).
     * Communication is not being sent over TCP port 5672.
  2. A complete TLS connection handshake with the following:

     * TLS v1.2 or later initiated by your SBC.
     * Your SBC initiating a "Client Hello" and GTP responding with "Server Hello".
     * Mutual TLS authentication process. 
       * GTP responds with its own server TLS certificate which is authenticated by your SBC.
       * The SBC sends its own client TLS certificate which is authenticated by GTP.
     * Encrypted channel established as evident by "Encrypted Handshake Message".
     * Evidence of "Application Data" being transmitted over TLS channel.

If TLS connection failed to be established, possible issues are:

     * SIP trunk has not been created on the GTP side.
     * The SIP trunk configured FQDN does not match the FQDN presented in the TLS certificate (CN or SAN attribute) from the SBC.
     * TLS version not supported, only TLS version 1.2 or later are supported.
     * Requested cipher suite not supported, see [SBC's TLS Configuration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config#sbc_tls_configuration).
     * Untrusted TLS certificate providers, see [SBC's TLS Configuration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config#sbc_tls_configuration).
  3. The SIP debug trace should show the following:

     * Customer `Call-Info` SIP header inserted in this format: `none Call-Info: <http://dialogflow.googleapis.com/v2beta1/projects/$PROJECT_ID/conversations/$CONVERSATION_ID>;purpose=Goog-ContactCenter-Conversation`

Example: `none Call-Info: <http://dialogflow.googleapis.com/v2beta1/projects/gcp-project-id-12345/conversations/CID-297363723_79131759_799783510>;purpose=Goog-ContactCenter-Conversation`

     * SIP headers show the phone number in E.164 format (+16501234567).

     * SIP headers show public IP addresses being used in the request URI and other SIP header fields (for example To, From, Via). Private IP addresses would be rejected.

     * SIP SDP connection information (c= ... ) is specified with a public IP address. Private IP addresses would be rejected.

     * Ensure the media prioritization sends the end users stream first followed by the human agent's media stream second because GTP treats the first media stream as the end users by default.

If you receive a SIP error response code:

     * SIP 400's error (for example, 488 Not Acceptable Here) response code likely indicates that GTP rejected a SIP header or SIP media SDP configuration.
     * A SIP 600's error (SIP 603 Declined Error) response code likely indicates a quota-related issue. See the [Quotas & limits page](https://docs.cloud.google.com/dialogflow/quotas#increase) for details about how to request an increase.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
