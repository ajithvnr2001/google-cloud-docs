---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-virtual-agent/
title: User guide: Supervisor assist for virtual agents \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:33.459066+00:00
---

# User guide: Supervisor assist for virtual agents  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-virtual-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  User guide: Supervisor assist for virtual agents Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** This feature has limited access. Contact your Google Cloud representative to access private GA features.

Supervisor assist performs the following useful actions to ensure that customer service conversations with both [Dialogflow CX playbook live agents](https://docs.cloud.google.com/dialogflow/cx/docs/quick/build-agent-playbook) and [generative agents](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps) are resolved or escalated successfully.

  * Scans all conversations for specific escalation triggers.
  * Automatically flags conversations that meet escalation trigger criteria.
  * Displays only flagged conversations to an assigned supervisor.
  * The supervisor monitors the conversations and intervenes as necessary.



## Before you begin

To use supervisor assist, you need access to the following resources.

  * A working playbook live or generative agent that uses the [bidirectional streaming API](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/bidi-stream-api) and a connected phone number.
  * A project with the `CCAI_GA` visibility label, a Pub/Sub topic, and a conversation profile.



## Step 1: Create or choose a Google Cloud project

Choose a project that will host your Dialogflow CX playbook live or generative agent, and note the project ID.

## Step 2: Enable Dialogflow API

Follow these steps to enable the Dialogflow API for your project.

  1. Navigate to Google Cloud console.

[Go to console](https://console.cloud.google.com/)

  2. Select your project.

  3. Click **APIs & Services** > **+Enable APIs & services**. 

  4. Click **Dialogflow API** > **Enable**.




## Step 3: Create or choose an agent

Supervisor assist requires a working playbook live or generative agent that uses the bidirectional streaming API. The feature scans and monitors all the agent's active conversations for escalation signals.

You can build your own [playbook live agent](https://conversational-agents.cloud.google.com/projects) or [generative agent](https://ces.cloud.google.com/), import an agent from a prior export, or choose an existing agent. Take note of your agent's name and ID.

## Step 4: Setup escalation

When you create or choose an agent, you must also setup escalation which tells the agent how to transfer a conversation to a human when the agent can't help. A supervisor can also click **Transfer to agent** to initiate an escalation.

### Setup playbook live agent escalation

Use the Conversational Agents console and Python code to set up escalation for a playbook live agent.

  1. Navigate to the Conversational Agents console and select your project.

[Conversational Agents console](https://conversational-agents.cloud.google.com)

  2. Navigate to **Conditional actions**.

  3. Click **+New logic**.

  4. For the trigger, choose **Event** and enter **escalate-to-agent**.

  5. For the action, select **Provide a response to the end user**.

  6. Add an **Agent dialogue** for the response.

  7. Add a phone number for the **Telephony transfer call**.

  8. Click **Update**.

  9. Click an action.

  10. Navigate to **Define actions with Python (advanced)**.

  11. Enter a script like the following example to define your agent's behavior.
         
         @EventHandler(event = "escalate-to-agent")
         def _supervisor_triggered_call_transfer():
           # the below message can be changed
           respond("Let me get you to a live agent who can assist you.")
           _escalate_to_agent_fn()
         
         def _escalate_to_agent_fn():
           # replace with your transfer logic
           done()
           return
         




### Setup generative agent escalation

Follow these steps to setup escalation for your generative agent.

  1. Navigate to the generative agent console and select your project and app.

[Generative agent console](https://ces.cloud.google.com/projects)

  2. Add the following prompt to your `root_agent` instruction.

     * **customer asking for a live agent** , execute the `end_session` tool with `session_escalated=true`
  3. Add the `end_session` system tool to your root agent and all sub agents.

  4. Create an `ESCALATION_MESSAGE` variable for the interactive voice response (IVR) before call transfer.

  5. Create a `PHONE_GATEWAY_TRANSFER` variable with a phone number like the following.
         
         {
           "phone_number": "+1yyy-yyy-yyyy"
         }
         




See the generative agents documentation for details about the [end session tool](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool#end_session).

## Step 5: Attach a phone number to your agent

Supervisor assist also requires a working phone number attached to the playbook live or generative agent. Follow [these instructions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway#setup) to attach a phone number to your playbook live agent. Follow [these instructions](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform) to attach a phone number to your generative agent. When you attach a phone number, the agent also creates a conversation profile. Note the conversation profile name and ID.

Follow these optional steps if you already have a phone number attached to your playbook live or generative agent.

  1. Run the following command to map your existing phone number, name, and ID to the telephony number. 
         
         curl -X GET   
         
              -H "Authorization: Bearer "$(gcloud auth print-access-token)"   
         
              -H "X-Goog-User-Project: your-project-id"   
         
              -H "Content-Type: application/json; charset=utf-8"   
         
              https://dialogflow.googleapis.com/v2beta1/projects/{your-project-id}/locations/{your-region-id}/phoneNumbers
         

  2. Update the phone number to use your conversation profile.

Example:
         
         {
         "phoneNumber": {
         "name": "projects/your-project-id/locations/global/phoneNumbers/your-phone-number",
         "conversationProfile": "projects/your-project-id/locations/your-region-id/conversationProfiles/your-conversation-profile-id"
             },
         "updateMask": "conversationProfile"
         }
         




## Step 6: Create a Pub/Sub topic

Pub/Sub is a messaging service where the senders of messages are decoupled from the receivers of messages. Pub/Sub topics are useful for providing conversation monitoring metrics and alerts. Follow the Pub/Sub instructions to [create a topic](https://docs.cloud.google.com/pubsub/docs/publish-receive-messages-console#create_a_topic) and note the topic ID.

## Step 7: Create a summarization generator

Summarization is an AI-based Agent Assist feature that automatically summarizes customer service conversations. Follow the summarization instructions to [create a generator](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/summarization-with-custom-sections#create_a_summarization_generator) and note the generator ID.

## Step 8: Configure your conversation profile

Follow these steps to verify that the conversation profile associated with your playbook live or generative agent exists.

  1. Navigate to the Agent Assist console and select your project.

[Go to Agent Assist](https://agentassist.cloud.google.com)

  2. Click the conversation profile associated with your playbook live or generative agent.

  3. Enable **Conversation summarization (generator)** and enter the name of the generator you created.

  4. Confirm that **Enable virtual agent** is enabled with your playbook live or generative agent's name.

  5. Navigate to **Telephony settings** and enable **Use Bidirectional Streaming API**.

  6. Select the following options for the **SIP configuration** :

     * **Create Conversation On The Fly**
     * **Use Multi Sdp Ports**
     * **Allow Virtual Agent Interaction**
  7. Click **Save**.




## Step 9: Gather configuration details

Gather the following details.

  * Google Cloud project ID
  * Playbook live agent ID or generative agent ID
  * Conversation profile ID
  * Pub/Sub topic name



## Step 10: Add your project to the allowlist

To add your project to the allowlist, [file an issue](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/getting-support) with the customer engagement team and include the details you gathered in the previous step.

## Step 11: Choose sentiment or AI coach

You must decide whether to use sentiment analysis, AI coach, or both to monitor your conversations. After you create an agent and a conversation profile, follow the instructions to [choose sentiment or AI coach](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-human-agent#choose-alerts) and add your decision to your conversation profile.

## Step 12: Configure rules to monitor conversations

Follow the instructions to [configure escalation rules](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/sa-human-agent#configure-rules) that determine when to alert a human supervisor during a conversation.

## Step 13: Monitor real time conversations

Follow these steps to monitor your conversations.

  1. To open the monitoring simulator, enter the following link in your browser with your project ID: 
         
         https://agentassist.cloud.google.com/projects/project-id/locations/location-id/human-supervisor
         

  2. Call the conversational agent you configured.
  3. Express negative sentiments during the conversation.
  4. Notice the conversation is listed on the dashboard.



### Monitoring desktop

Agent Assist provides a monitoring desktop for supervisors to monitor conversations. Multiple participants can launch the monitoring desktop and make themselves available to monitor calls. When a call begins, supervisor assist assigns it to one participant after another until all participants have contributed.

To access the monitoring desktop, you need the following roles:

  * `Viewer`
  * `dialogflow.virtualAgentMonitoringSupervisor`
  * `dialogflow.processor`



Follow these instructions to monitor calls with the monitoring desktop.

  1. To open the monitoring desktop, enter the following link in your browser with your project ID: 
         
         https://agentassist.cloud.google.com/human-supervisor/projects/project-id/locations/location-id/dashboard
         

  2. Click **Make me available**. 
  3. Call the agent you configured.
  4. Express negative sentiments during the conversation.
  5. Notice the conversation is listed on the dashboard when a call is routed to you.

**Note:** To ensure you receive flagged conversations, you must keep the supervisor dashboard window active. The console signals when you are online. If it detects no activity for 5 minutes, the console marks you as inactive, and the routing service stops assigning new conversations to you.

### Change the agent

Within a conversation profile, you can change which playbook live or generative agent that supervisor assist monitors. Follow these steps to change the agent.

  1. Navigate to the Agent Assist console and select your project.

[Go to Agent Assist](https://agentassist.cloud.google.com)

  2. Click **Conversation profiles**.

  3. Select the conversation profile that you added to the allowlist.

  4. Navigate to **Choose to use Dialogflow**.

  5. Enable **Enable virtual agent**.

  6. Click **close** **Close** to remove the existing playbook live or generative agent name, and enter the name of the agent you want to monitor.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
