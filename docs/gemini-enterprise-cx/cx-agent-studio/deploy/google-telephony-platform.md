---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/google-telephony-platform/
title: Google Telephony Platform \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:16.695138+00:00
---

# Google Telephony Platform  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/deploy/google-telephony-platform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Google Telephony Platform Stay organized with collections  Save and categorize content based on your preferences. 

This guide walks you through the process of creating and configuring a new Google Telephony Platform (GTP) phone number for your agent application. This out-of-the-box feature lets you attach a new phone number to your agent that can handle incoming traffic in only a few minutes.

If you want to use a pre-existing phone number, you can configure your Session Border Control (SBC) system to automatically redirect the existing number to the new GTP number or to a virtual phone number over a SIP trunk. For detailed instructions on SBC integration and setup, see the Dialogflow CX [telephony documentation](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/overview).

## Before you begin

  1. Follow the steps on the [setup and cleanup](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/setup) page to create or configure the project you'd like to use for the deployment.
  2. [Create and configure](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/quick/create-agent) an agent application to use in the deployment.
  3. Enable the [Dialogflow API](https://docs.cloud.google.com/dialogflow/cx/docs/quick/setup#api) in the project.



## Limitations

The following limitations apply:

  * Standard PSTN (Public Switched Telephone Network) phone numbers are supported for the `us` multi-region. For `eu` multi-region, you can use virtual phone numbers.
  * Virtual phone numbers can't be dialed directly from standard PSTN phones, but you can route calls to them from your SBC over a SIP trunk or test them in the WebRTC widget.



## Connect an agent application to a GTP phone number

  1. Open the [CX Agent Studio console](https://ces.cloud.google.com) and select your agent application.
  2. At the top of the console, click the **Deploy** tab followed by **Connect to a platform**. If you already have deployed channels, click **+New channel**.
  3. Enter a **Name** for the channel and select **Google Telephony Platform (GTP)** from the **Platform** menu.
  4. The default option is to provision a virtual phone number for testing your agent application in the browser or routing inbound calls from an SBC over a SIP trunk. To provision a standard PSTN (Public Switched Telephone Network) phone number, select that option from the `Connection type` drop-down.
  5. Select a **Version** for deployment. If you don't have pre-existing versions, create a new one.
  6. (Optional) Click the **Channel-specific behavior** toggle to configure additional options. You can change the agent response length, enable DTMF input, and allow users to interrupt the agent mid-response. For more information about these settings, see the [agent application settings documentation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings).
  7. Click **Create channel**. You can now see the phone number and deployment ID for the channel.
  8. If you provisioned a PSTN phone number, call it to test that it connects to your agent application, then click **Done**. The new channel appears on the agent application's **Deployed channels** page. You can now use this number to have customers call your agent. If you provisioned a virtual phone number, you can test it in the WebRTC widget or connect it to an SBC over a SIP trunk.

**Note:** Virtual phone numbers can't be dialed directly from standard PSTN phones. To route PSTN calls to a virtual phone number, forward the calls from your SBC over a SIP trunk.



## Test agent application in WebRTC widget

Whether you provisioned a standard PSTN or a virtual phone number, you can test your agent application in the WebRTC widget by using audio, video, or text.

  1. At the top of the console, click the **Deploy** tab.
  2. Click the phone_forwarded icon next to the deployed channel name. A WebRTC widget will open on the right.
  3. If prompted by the WebRTC widget, grant the browser permission to access your microphone and camera.
  4. Interact with your agent through audio, video, or text. When using video, you can also switch to screen sharing by using the drop-down menu next to the camera icon.



## Connect a virtual phone number to an SBC over a SIP trunk

You can route inbound PSTN or VoIP calls from your own Session Border Controller (SBC) or carrier to a CX Agent Studio virtual phone number over a secure SIP trunk. Virtual phone numbers are country-agnostic identifiers (prefixed with `+0` followed by 32 hexadecimal characters) that let you keep your existing carrier phone numbers in any country and forward inbound calls to your agent.

### Prerequisites for SIP trunk connectivity

Before sending SIP traffic from your SBC to a virtual phone number, complete the standard Dialogflow CX [SIP trunk setup](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/cloud-setup) and [SBC configuration](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/sip-trunk/sbc-config).

### Format the SIP URI for a virtual phone number

Because virtual phone numbers (`+0...`) are not PSTN E.164 numbers, Google Telephony Platform routes them based on the **SIP domain** in the `INVITE` Request-URI and `To` header.

Format the destination SIP URI in **both** the `INVITE` Request-URI and the `To` header as follows:
    
    
    sip:VIRTUAL_NUMBER@ccai.prod-LOCATION.telephony.goog:5672;transport=tls
    

Replace the following:

  * VIRTUAL_NUMBER: The full 34-character virtual phone number copied from the console, starting with `+0` followed by 32 uppercase hexadecimal characters and **no spaces** (for example, `+01BCE14D51A354F8E84E142E7E1E3B4E5`).
  * LOCATION: The Google Cloud location ID where the GTP deployment channel and virtual phone number were created (for example, `us`, `eu`).

Channel Google Cloud Location | SIP Domain (`ccai.prod-LOCATION.telephony.goog`) | Example SIP URI  
---|---|---  
`global` | `ccai.prod-global.telephony.goog` | `sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-global.telephony.goog`  
`us` | `ccai.prod-us.telephony.goog` | `sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-us.telephony.goog`  
`eu` | `ccai.prod-eu.telephony.goog` | `sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-eu.telephony.goog`  
Other supported region (REGION) | `ccai.prod-REGION.telephony.goog` | `sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-REGION.telephony.goog`  
  
### Sample SIP `INVITE` for a virtual phone number

The following example shows a valid `SIP INVITE` sent over mTLS to `us.telephony.goog:5672` (`74.125.88.132:5672`) targeting the virtual phone number `+01BCE14D51A354F8E84E142E7E1E3B4E5` in the `us` location:
    
    
    INVITE sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-us.telephony.goog:5672;transport=tls SIP/2.0
    Via: SIP/2.0/TLS sbc.example.com:5672;branch=z9hG4bK74bf9;rport
    Max-Forwards: 70
    From: "Caller" <sip:+16502530000@sbc.example.com>;tag=9fxced76sl
    To: <sip:+01BCE14D51A354F8E84E142E7E1E3B4E5@ccai.prod-us.telephony.goog:5672;transport=tls>
    Call-ID: 3848276298220188511@sbc.example.com
    CSeq: 1 INVITE
    Contact: <sip:+16502530000@sbc.example.com:5672;transport=tls>
    Content-Type: application/sdp
    Content-Length: ...
    

## Configure agent application behavior

You can customize your agent's behavior around ending and transferring calls.

**Note:** Since August 1st, 2026 the following parameters were switched from ALL_CAPS to camelCase (both are supported for backwards compatibility):

  * `PHONE_GATEWAY_TRANSFER` is now `telephonyTransferCall` (and its nested keys: `phone_number` -> `phoneNumber`, `use_originating_trunk` -> `useOriginatingTrunk`)
  * `LIVE_AGENT_HANDOFF` is now `liveAgentHandoff` (and its nested keys: `sip-refer` -> `sipRefer`, `uui-headers` -> `uuiHeaders`, `x-headers` -> `xHeaders`)
  * `TELEPHONY_PAYLOAD` is now `telephonyPayload`
  * `ESCALATION_MESSAGE` is now `escalationMessage`



### Configure agent call termination

To allow the agent to terminate a call:

  1. Click the plus symbol at the top right of the agent and click **Add tools**.
  2. Add the `end_session` tool to the agent (and all sub-agents, if present). This [system tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool#system_tools) is automatically available to every agent by default.
  3. Add a description of call termination behavior to the [instructions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/instruction). For example: `End the call by executing the end_session tool with arguments reason="customer_query_ended".`



### Transfer a call to a human agent

To configure the agent to transfer the call to a human agent and end the virtual agent leg of the call:

  * Add the `end_session` system tool to the agent (and all sub-agents, if present).
  * Create the following variables: 
    * `escalationMessage`: Optionally, add text to the **Default value** field if you would like the agent to say a message before transferring the call.
    * `telephonyTransferCall`: Set the **Type** to **Custom schema**. Enter the following JSON object in the **Schema** input box with the phone number you want the agent to transfer calls to (E.164 format required).


    
    
    {
      "phoneNumber": "+PHONE_NUMBER"
    }

  * Add a description of this behavior to your instructions. For example: `Escalate the call to a human agent by executing the end_session tool with session_escalated=true`



### Partner-supported human agent transfer

If your system incorporates a [non-Google partner](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration) there are two available options for human agent transfer: A `liveAgentHandoff` variable or a `telephonyPayload` variable. In both cases, the JSON payload might vary depending on the partner's instructions.

**Live agent handoff human agent transfer:**

  * Add the `end_session` system tool to the agent (and all sub-agents, if present).
  * Create the following variable: 
    * `liveAgentHandoff`: Set the **Type** to **Custom schema** and add the partner-required JSON schema, for example:


    
    
    {
      "PARTNER_NAME": {
        "type": "action",
        "action": "deflection",
        "deflection_type": "sip",
        "sip_uri": "SIP_URI",
        "sip_refer": true,
        "sip_parameters": {
          "x-header": "value"
        }
      }
    }

  * Add a description of this behavior to your instructions. For example: `Escalate the call to a human agent by executing the end_session tool with session_escalated=true`



**Custom payload human agent transfer:**

  * Add the `end_session` system tool to the agent (and all sub-agents, if present).
  * Create the following variable: 
    * `telephonyPayload`: Set the **Type** to **Custom schema** and add the partner-required JSON schema, for example:


    
    
    {
      "PARTNER_NAME": {
        "type": "action",
        "action": "deflection",
        "deflection_type": "sip",
        "sip_uri": "SIP_URI",
        "sip_refer": true,
        "sip_parameters": {
          "x-header": "value"
        }
      }
    }

  * Add a description of this behavior to your instructions. For example: `Escalate the call to a human agent by executing the end_session tool with session_escalated=true`



## Use SIP signaling to pass data to and from the agent

If you have done an SBC integration, you can use SIP signaling to pass data to the agent using SIP headers. You can also pass data out when a BYE, REFER or INVITE is triggered by the agent.

All data passed into the agent is accessible using variables. _You must first create the variables in order to access the data._

The caller's phone number (ANI) is stored in the variable `telephony-caller-id` of type `Text`.

If the agent should say a message before doing an escalation, the message should be stored in the variable `escalationMessage` of type `Text`.

To do a SIP REFER or SIP INVITE, the variable `telephonyTransferCall` of type `Custom schema (advanced)` should exist with variables `phoneNumber` and `useOriginatingTrunk` specified.

Any data that needs to be passed out should be present in the variable `liveAgentHandoff` of type `Custom schema (advanced)`.

### UUI SIP header

You can pass in a semicolon-separated list of key value pairs that is hex encoded, followed by `;encoding=hex;purpose=Goog-Session-Param`. To access this within the agent, create a variable with the name `uui-headers` and type `List`.

For example, if the string `key1=value1;key2=value2` needs to be passed in, the following UUI header should be sent, where the payload is the hex-encoded value `key1=value1;key2=value2`.
    
    
    User-to-User: 6B6579313D76616C7565313B6B6579323D76616C756532;encoding=hex;purpose=Goog-Session-Param
    

The variable `uui-headers` will contain the following object:
    
    
    "uui-headers": ["key1=value1;key2=value2"]
    

To pass `uuiHeaders` out when calling the `end_session` tool, specify `params={"liveAgentHandoff": {"uuiHeaders": [ {uui-headers}[0] ]}}`

For example, if the UUI headers passed in had to be passed out upon a SIP BYE, you would have an instruction similar to the following:

`If the user says that they would like to speak to an agent, escalate the call to the agent by executing the end_session tool with session_escalated=true and params={"escalationMessage": "I am transferring you to an agent", "liveAgentHandoff":{"uuiHeaders": [ {uui-headers}[0] ]}}.`

### SIP x-headers

SIP headers starting with `x-` can be passed to the agent and saved as a variable `x-headers` and type `Custom schema (advanced)`. The `x-` prefix is removed from the header name in the variable.

For example, if the SIP INVITE contains the following header:
    
    
    x-billing-id: 12345
    

The variable `x-headers` will contain the following object:
    
    
    {
      "x-headers": {
        "billing-id": "12345"
      }
    }
    

To pass `xHeaders` out, when calling the `end_session` tool, specify `params={"liveAgentHandoff": {"xHeaders": {x-headers} }}`

For example, if the x-headers passed in had to be passed out upon a SIP BYE, you would have an instruction similar to the following:

`If the user says that they would like to speak to an agent, escalate the call to the agent by executing the end_session tool with session_escalated=true and params={"escalationMessage": "I am transferring you to an agent", "liveAgentHandoff":{"xHeaders": {x-headers} }}.`

**Note:** The receiving telephony platform should expect a lowercase `x-`, not an uppercase `X-`.

### Send a SIP BYE

When the agent ends the call, a SIP BYE is sent. To send `uuiHeaders` and `xHeaders` in the SIP BYE, use an instruction similar to the following example:

`If the user says that they would like to speak to an agent, escalate the call to the agent by executing the end_session tool with session_escalated=true and params={"escalationMessage": "I am transferring you to an agent", "liveAgentHandoff":{"xHeaders": {x-headers}, "uuiHeaders": [{uui-headers[0]}] }}.`

### Send a SIP REFER

If the agent needs to escalate the call to a human agent and drop off the call, a SIP REFER should be used. A SIP REFER is triggered by specifying `"sipRefer": true` in the `liveAgentHandoff` variable and the `refer-to` number should be provided in the `telephonyTransferCall` variable. An example instruction to do a SIP REFER and pass out the `uuiHeaders` and `xHeaders`:

`If the user says that they would like to speak to an agent, escalate the call to the agent by executing the end_session tool with session_escalated=true and params={"escalationMessage": "I am transferring you to an agent", "telephonyTransferCall": {"phoneNumber": "+19496855555", "useOriginatingTrunk": true}, "liveAgentHandoff":{"sipRefer": true, "xHeaders": {x-headers}, "uuiHeaders": [{uui-headers[0]}] }}.`

### Send a SIP INVITE

If the agent needs to escalate the call to a human agent and stay on the call so that Agent Assist features can be used, a SIP INVITE should be used. A SIP INVITE is triggered by the `phoneNumber` in the `telephonyTransferCall` variable. An example instruction to do a SIP INVITE and pass out the `uuiHeaders` and `xHeaders`:

`If the user says that they would like to speak to an agent, escalate the call to the agent by executing the end_session tool with session_escalated=true and params={"escalationMessage": "I am transferring you to an agent", "telephonyTransferCall": {"phoneNumber": "+19496855555", "useOriginatingTrunk": true}, "liveAgentHandoff":{"xHeaders": {x-headers}, "uuiHeaders": [{uui-headers[0]}] }}.`

## Create a handler for remote call disconnects

When a customer hangs up the call, it triggers a specific event, `sys.remote-call-disconnected`, that can be used to trigger a tool call within CX Agent Studio. In the following example, the tool `sum` is called when the customer hangs up the call.

The tool `sum` is defined as a Python code tool and contains the code:
    
    
    def sum(x: int, y: int) -> int:
      """
      Computes the sum of two numbers.
    
      Args:
        x: The first number.
        y: The second number.
    
      Returns:
        The sum of the two numbers.
      """
      return x+y
    

In the root agent, create a `Before LLM` callback with the logic to watch for the call disconnect event. In the `LlmResponse` make the `sum` tool call and then call the `end_session` tool.
    
    
    def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
    
      for part in callback_context.get_last_user_input():
        if part.text == "<event>sys.remote-call-disconnected</event>":
          return LlmResponse.from_parts(
            [Part.from_function_call('sum', {'x': 1, 'y': 2}),
             Part.from_end_session(reason='sum tool called after caller disconnected')]
          )
      return None
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
