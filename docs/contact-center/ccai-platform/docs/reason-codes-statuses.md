---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/reason-codes-statuses/
title: Reason codes and statuses \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:40.128619+00:00
---

# Reason codes and statuses  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/reason-codes-statuses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Reason codes and statuses Stay organized with collections  Save and categorize content based on your preferences. 

This document describes call and chat reason codes and statuses used in CCAI Platform.

## Occupancy statuses

|   
---|---  
**Available Time** | The sum of time that agents were idle and ready to handle an interaction.  
**Login Time** | The sum of time that agents were logged in.  
**Wrap-up time** | The sum of time that agents were in the wrap-up state after ending an interaction.  
**Break Time** | The sum of time that agents were in the Break status.  
**Idle Time** | The sum of time that agents were in the Idle status.  
**In-call Time** | The sum of time that agents were handling calls.  
**In-chat Time** | The sum of time that agents were handling chats.  
**Meal Time** | The sum of time that agents were in the Meal status.  
**Missed Call Time** | The sum of time that agents were in the Missed Call status.  
**Missed Chat Time** | The sum of time that agents were in the Missed Chat status.  
**Offline Time** | The sum of time that agents were logged out.  
**Special Task Time** | The sum of time that agents were in the Special Task status.  
**Unavailable Time** | The sum of time that agents were in the Unavailable status.  
**Unresponsive Time** | The sum of time that agents were in the Unresponsive status.  
  
## View and identify failed reason codes

This page can help you identify:

Call fail reasons

Chat fail reasons

The following Failed Reason codes can be viewed:

  * In the **Individual Call History** standard report.

  * On the Dashboards for [Calls](https://docs.cloud.google.com/contact-center/ccai-platform/docs/calls-connected-queued-completed) and [Chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/chats-connected-queued-and-completed) completed.

  * Using the [API.](https://docs.cloud.google.com/contact-center/ccai-platform/docs/reporting-api)




### Call fail reasons

**Code** | **Metric Name** | **Description**  
---|---|---  
nothing: 0 | No Error - Call | The sum of calls that did not fail.  
unknown: 10001 | Unknown - Call | The sum of calls that failed for unknown reasons.  
expired: 11001 | Expired - Call | The sum of calls that failed due to the connection timing out.  
transfer_expired: 11002 | Transfer Expired | The sum of calls that failed due to the transfer connection timing out.  
eu_canceled: 20001 | Cancelled | The sum of calls where the end-user hung up while being connected to an agent.  
eu_rejected: 20002 | Rejected | The sum of outbound calls that were declined by the end-user.  
eu_abandoned: 20003 | Abandoned | The sum of calls that were abandoned by the end-user while waiting in queue.  
eu_in_menu_abandoned: 20004 | In-Menu Abandoned | The sum of calls that were abandoned by the end-user while in the IVR menu.  
eu_repeated_voicemail: 20005 | Repeated Voicemail | The sum of calls that failed because the end-user already had left a voicemail waiting to be answered. For more information on voicemail settings see [After hour deflection for calls and chats](https://docs.cloud.google.com/contact-center/ccai-platform/docs/after-hour-deflection).  
eu_repeated_callback: 20006 | Repeated Callback | The sum of calls that failed because the end-user had already requested a callback.  
eu_busy: 21001 | Busy | The sum of outbound calls that reached the end-user in a busy state.  
eu_wrong_number: 21002 | Wrong Number | The sum of outbound calls that were made to an invalid phone number.  
eu_no_answer: 21003 | No Answer | The sum of outbound calls where the end-user did not pick up.  
eu_noti_failed: 22001 | Notification Failed | The sum of calls that were not connected to the agent due to the agent not having browser notifications enabled.  
ag_canceled: 30001 | Agent Cancelled | The sum of calls that failed while being connected to the agent. Possible reasons include the agent closing their browser or a network error.  
ag_ignored: 30002 | Agent Ignored | The sum of calls that were not picked up by the agent.  
ag_mic_no_device: 31001 | Agent No Mic | The sum of calls that failed due to the agent not having a microphone.  
ag_mic_denied: 31002 | Agent mic denied | The sum of calls that failed due to the agent not having microphone access enabled.  
ag_called_blocked_num 32002 | Agent called blocked number | The consumer is blocking the call.  
Unable to connect call to the dialed phone number 32003 | Agent connection timeout | The sum of calls that failed to connect because the agent's device lost network connectivity or failed to register with the server.  
voip_twilio_error: 41001 | VOIP Error | The sum of calls that failed due to a voice provider issue.  
voip_tokbox_error: 42001 | VOIP Error | The sum of calls that failed due to an issue with the Tokbox voice provider.  
voip_invalid_token: 43001 | VOIP Invalid Token | The sum of calls that failed due to the voice provider providing an invalid token.  
voip_conn_general: 44001 | VOIP General | The sum of calls that failed due to a general voice provider issue.  
voip_conn_timeout: 44002 | VOIP Timeout | The sum of calls that failed due to the voice provider connection timing out.  
voip_conn_signal: 44003 | VOIP Signal | The sum of calls that failed due to a poor connection to the voice provider.  
voip_nexmo_error: 45001 | VOIP Error | The sum of calls that failed due to an issue with the Nexmo voice provider.  
stuck_due_to_api_error: 50001 | Stuck due to API | The sum of calls that failed due to an API issue.  
group_deleted_no_substitute: 50002 | Group Deleted - Call | The sum of calls that failed due to a cascade group being deleted without any alternative available.  
menu_deleted: 50003 | Menu Deleted | The sum of calls that failed due to the queue being deleted after the end-user had already entered the queue.  
direct_pstn_call_to_ fallback_number: 60001 | Directed to Fallback | The sum of calls that were directed to a fallback number.  
  
### Chat fail reasons

|  |   
---|---|---  
**Code** | **Metric Name** | **Description**  
nothing: 0 | No Error - Chat | The sum of chats that did not fail.  
unknown: 1 | Unknown - Chat | The sum of chats that failed for unknown reasons.  
no_response: 2 | No Response | The sum of chats that ended due to the end-user not responding.  
expired: 3 | Expired - Chat | The sum of chats that failed due to the connection timing out.  
after_hours: 4 | After Hours | The sum of chats that reached a queue outside of operating hours.  
expired_menu_selection: 31 | Expired Menu | The sum of chats where end-users selected a queue that no longer existed.  
end_user_opt_out: 41 | Opted Out | The sum of chats where end-users opted not to be recorded.  
over_cap_email: 50001 | Overcapacity Email | The sum of chats where end-users sent an email due to the queue being in an overcapacity state.  
group_deleted_no_substitute: 60001 | Group Deleted - Chat | The sum of chats that failed due to a cascade group being deleted without any alternative available.  
  
## Data dictionary - Sample API and calculation scripts

The following are sample API and calculation scripts.

### Sample API and calculation scripts

This is a sample script that can be run to try out a couple of the CCAI Platform metrics that exist in the administrator portal dashboard. It exemplifies how any of the metrics can be retrieved and calculated.

The example walks through the definition of variables, functions and calculation scripts for how to calculate **total volume** and **service level.**

#### Variables

  * **Array of calls** : add an array of calls set to the variable callsArray.

  * **Call types** : is an array of all call types that exist in CCAI Platform.

//You can remove elements from this array to test metrics of only a certain type of calls; for example:

  * **Total hours** : is a total hours variable. Calculate the difference in hours based on the parameters in your request.

  * **SLA** : is calculated using a configured threshold in the administrator portal. Change the variable with the configured amount. This example shows a 60 second SLA; for example:




#### Functions

  * **Call record function** : //checkCallRecord is designed to validate if a call record is the proper status, did not fail a certain way, and in some cases whether connected is null;

  * **Total volume of calls function** : getTotalVolumeOfCalls is designed to return a total volume of calls; e.g.:

  * **Service level function** : getServiceLevel is designed to return the Service Level of a call type; e.g.:




#### Calculation scripts

Example calculation scripts.

For total volume:
    
    
    // TOTAL VOLUME SECTION
    
    for(var i = 0; i\<call_type.length;i++){
    
    var vol = getTotalVolumeOfCalls(callsArray,call_type\[i\]);
    
    if(vol \> 0){
    
    var volPerHour = Math.round(vol/total_hours\*10)/10
    
    var stringToPrint = \"the per hour volume of \"+call_type\[i\]+\" is \"+
    volPerHour.toString()
    
    console.log(stringToPrint);
    
    };
    
    }
    

For SLA:
    
    
    // SLA SECTION
    
    for(var i = 0;i\<call_type.length;i++){
    
    var SLACalc =
    (getServiceLevel(callsArray,call_type\[i\])/getTotalVolumeOfCalls(callsArray,call_type\[i\],false,\['eu_in_menu_abandoned'\]));
    
    if (isNaN(SLACalc) == false){
    
    var stringToPrint = \"the SLA of \"+call_type\[i\]+\" is \"+
    SLACalc.toString();
    
    console.log(stringToPrint);
    
    } else {
    
    var stringToPrint = \"the SLA of \"+call_type\[i\]+\" cannot be
    calculated due to lack of volume\";
    
    console.log(stringToPrint);
    
    }
    
    };
    

## Chat status definitions

  * Common chat statuses

  * Chat finished statuses

  * Chat failed reasons




### Common chat statuses

|   
---|---  
**Chat statuses** | **Description**  
Queued | Chat is in queue and is waiting for an Agent  
Assigned | Chat is assigned to an agent  
Ongoing | Chat is active with an Agent and End User  
Finished | Chat finished successfully _(finished reasons listed below)_  
Abandoned | Chat canceled by the end user before assigned to an agent  
Deflected | Chat was cancelled and deflected to Over Capacity Email  
Failed | Chat failed (_failure reasons listed_)  
  
### Chat finished statuses

Finished chat statuses | Description  
---|---  
Finished | Chat finished successfully with no additional information  
Finished: Disconnected By Agent | Chat was finished, agent disconnected  
Finished: Disconnected By End User | Chat was finished, disconnected by end user  
Finished: No Messages | Chat was finished, there was no response  
Finished: No Messages Disconnected By Agent | Chat was finished, there was no response and the agent disconnected  
Finished: No Messages Disconnected By End User | Chat was finished, there was no response and the end user disconnected  
Timeout: Timeout By Agent With No Messages | The chat timed out and the agent never sent a message while handling the chat. For chats escalated from a virtual agent, only the human agent's messages are counted.  
Timeout: Timeout By End User With No Messages | The chat timed out and the end user never sent a message at any point during the chat, including to the virtual agent before an escalation. If the end user sent at least one message earlier in the chat and then went silent, the chat is recorded as 'Timeout: end user stopped responding' instead.  
Timeout: agent stopped responding | The chat timed out while the most recent unanswered message was from the end user; the agent had responded earlier but stopped.  
Timeout: end user stopped responding | The chat timed out after the end user stopped responding. The end user sent at least one message earlier in the chat, to the virtual agent or to the agent, and then went silent.  
  
### Chat finish reason values (BigQuery chat export)

Value | Definition  
---|---  
0 | No specific finish reason. The displayed status ("Finished" / "Finished: Disconnected By Agent" / "Finished: Disconnected By End User") is determined by the disconnected_by column (0 = unknown, 1 = agent, 2 = end user).  
1 | No response. Corresponds to the "Finished: No Messages" statuses, combined with disconnected_by as previously described.  
2 | Timeout: Timeout By Agent With No Messages  
3 | Timeout: agent stopped responding  
4 | Timeout: agent stopped responding  
5 | Timeout: end user stopped responding  
6 | End user opted out (for example, replied STOP on SMS)  
7 | Consumer check-in timed out  
8 | Chat ended by API orchestration (direct access point end_chat outcome)  
  
### Chat failed reasons

Failed Reason | Definition  
---|---  
Failed | Chat session Failed for an Unknown reason  
Expired | Chat expired within a queue and was not picked up by an Agent  
  
## Call status definitions

The following call statuses can appear in the call performance history report.

Call status  | Description   
---|---  
Abandoned  | A call is waiting in the queue and is disconnected by the caller before it is accepted by an agent. Excludes In-menu and Short Abandons.   
Busy  | End-user was busy   
Canceled  | End-user canceled the call   
Completed  | A call is successfully completed without any errors   
Error  | Call has an error   
Failed  | A call ends because of an error. Includes a failed reason for more context.   
No Answer  | The end-user didn't answer   
Recovered  | A failed call is called back. The new call is a child of the original call. Includes whether the call back finishes without error.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
