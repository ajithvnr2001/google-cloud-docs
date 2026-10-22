---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/system/
title: System tools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:55:23.069332+00:00
---

# System tools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/tool/system/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  System tools Stay organized with collections  Save and categorize content based on your preferences. 

System tools are built-in tools that can be used by the agent to perform common tasks. They are not editable.

Similar to other tools, when using system tools, provide agent instructions for when to use the tool and provide tool arguments.

## customize_response

**Note:** This system tool only applies to voice agents.

Generates an agent voice response with granular control over parameters including disabled barge-in and DTMF parameters.

Arguments:

Argument | Required/Optional | Description | Default  
---|---|---|---  
content | Required | The text content of the agent response. |   
enable_dtmf | Optional | Whether to enable keyboard input (DTMF). | Determined by [agent application settings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/agent#agent-application-settings)  
dtmf_endpointing_timeout_modes | Optional | The wait time for users' typing response, choosing from "short", "mid" and "long". | "mid"  
dtmf_finish_digit | Optional | The DTMF digit that finishes DTMF collection. For example, "#". | Empty string  
disable_barge_in | Optional | Disallow user barge-in when agent is speaking. | False  
  
Example instruction for collecting a phone number with DTMF, where DTMF is explicitly enabled, possibly overriding the agent application setting:
    
    
    make the tool call customize_response(content="Please type your phone number",
    enable_dtmf=True,
    dtmf_endpointing_timeout_modes='short')
    

Alternatively, you can set `enable_dtmf` explicitly to `False`, or you can omit this argument and rely on agent application settings.

Example instruction for collecting a credit card number with DTMF:
    
    
    make the tool call customize_response(
    content="Using your keypad, please enter your 16-digit credit card number, then press the pound key when you are finished.",
    enable_dtmf=True,
    dtmf_finish_digit='#',
    dtmf_endpointing_timeout_modes='mid')
    

Example instruction for reading terms while not allowing barge-in:
    
    
    make the tool call customize_response(
    content="By proceeding, you agree to the terms and condition...",
    disable_barge_in=True)
    

## end_session

Ends the session. This tool is used to end the conversation to either escalate to a human agent or end the session if the user does not have any more requests.

If the session is ended because of a problem, and the user had to be escalated, supply a value of `True` to the `session_escalated` parameter. Use the `params` argument to forward data to the end session metadata of the final response.

Arguments:

Argument | Required/Optional | Description | Default  
---|---|---|---  
reason | Required | The reason for ending the session. |   
session_escalated | Optional | Whether the session is escalated to a human agent. | False  
params | Optional | Other parameters to pass to the end session handler. | None  
  
Example instruction for finishing the conversation:
    
    
    If the user has no more questions execute the tool end_session(reason="success")
    

Example instruction for escalating when the user wants a live agent:
    
    
    If the user wants to talk to a human, execute the tool
    end_session(reason="escalate_to_human", session_escalated=True)
    

Example instruction for checking the user input language:
    
    
    If the user speaks a language that is not English or Spanish, escalate by
    calling: end_session(
    reason='Encountered an unsupported language, escalating to a human agent.',
    session_escalated=true).
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
