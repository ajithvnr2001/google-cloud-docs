---
url: https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design/
title: Voice agent design best practices \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:39:25.222937+00:00
---

# Voice agent design best practices  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/voice-agent-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)



Send feedback 

#  Voice agent design best practices Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides best practices specifically for designing voice agents. When you design a voice agent, the goal is to help users (end-users) achieve a task without escalating to a human agent. Users should feel like they are having a natural, interactive, and cooperative conversation with the voice agent.

You should also see the general [general agent design](https://docs.cloud.google.com/dialogflow/es/docs/agents-design) guide for all agent types, and the [best practices](https://docs.cloud.google.com/dialogflow/es/docs/best-practices) guide for using the Dialogflow service.

## Measure agent quality

To measure the quality of your agent's user experience, consider tracking the following metrics:

  * **Misroute** : how many callers ended up in the wrong place.

  * **First call resolution** : number of calls that are resolved on the first call or contact.

  * **Average handling time** : how long it takes to resolve the user's issue.

  * **Customer satisfaction** : how high your voice agent scores on a user survey.

  * **Number of turns** : how many exchanges it takes to accomplish the user's task.

  * **User churn** : how often users disengage from the conversation.




## Speech recognition

The following tips can help your agent recognize end-user speech:

  * Your agent should encourage the end-user to use long phrases or complete sentences. This improves recognition quality.
  * Consider using a webhook to verify end-user input that may not be accurately recognized or needs to be validated.
  * Use [fallback intents](https://docs.cloud.google.com/dialogflow/es/docs/intents-default#fallback) to ask the end-user to enunciate more slowly and clearly.



## Conversation structure

A conversation with a voice agent is generally organized in the following sequence:

Activity | Example | Notes  
---|---|---  
Opening activity | User logs in or calls your contact center.**Voice agent** : Hello, this is Travel Inc. How can I help you today? | The voice agent starts the conversation with a welcome message.  
Main sequence | **User** : I want to book a plane ticket.**Voice agent** : Ok, where do you want to go?**User** : Guatemala on May 19th, 9PM.**Voice agent** : Ok, we have booked you a ticket for Guatemala on May 19th, 9PM. | The task is defined by the user, and the task is completed by the voice agent. The task may take several turns for the voice agent to collect all the necessary information.  
Closing activity | **Voice agent** : Is there anything else I can help you with?**User** : No**Voice agent** : Ok, thanks for chatting with me! | User is ready to finish the conversation when their request is fulfilled.  
  
### Welcome message

When designing your opening message to the user, think about how to get to the first topic as soon as possible. The welcome message should be short and straight to the point. Some suggestions include the following:

  1. Answer the call with phrases like "Hello."
  2. Identify the voice agent with phrases like "This is XYZ Company's voice agent/assistant."
  3. Show availability with phrases like "How can I help you today?"



Any extra information may frustrate users and cause them to escalate to a human agent. However, you may need to extend the welcome message for legal reasons, such as informing the user that the conversation may be recorded.

Avoid information that makes the conversation sound unnatural or unbalanced. For example:

Do | Don't  
---|---  
Do model the language you want your users to use. For example, if you want the user to explain things in one or two sentences, limit your voice agent to one or two sentences per turn. | Don't instruct users how to speak with phrases such as "in one or two sentences, tell me…" or "you can say things like…"  
Do focus on the task the user wants to accomplish, and design error handling strategies in case the conversation fails. | Don't tell users what the voice agent can do with phrases like "I can help you solve complex issues."  
  
### Conversation turn pairs

A typical conversation consists of _turn pairs_ such as the following types of exchanges:

  * question-answer, which is most common for a voice agent
  * invitation-acceptance/rejection
  * greetings-greetings



Sometimes, a turn pair can include extra verbiage, such as an explanation about why we need to ask a question, background information related to the question we want to ask, or a reaction to the user's answer. For example, consider the following question-answer turn pair:

**Voice Agent** : This will cost you $10/day. _(background information/explanation)_ Would you like to continue adding this perk? _(question)_

**User** : Yes. _(answer)_

**Voice Agent** : Awesome! _(reaction)_

### Conversation repair

_Conversation repair_ is the practice of fixing misunderstandings, mishearings, and misarticulations to resume a conversation. Repairing a conversation can help build a user's trust by showing that the voice agent is listening to their request.

Some best practices include:

  * Be specific and use context the user already offered in previous turns. Avoid asking obvious and redundant questions such as "I didn't catch that," "I don't understand," or "I'm having trouble."

  * Give the user the opportunity for self-repair, which means allowing the user to repair their turn in the way they think is best to ensure that they have agency in the conversation. Avoid phrases such as "try rephrasing" or "you can say x, y, or z."

  * Use the "You mean x?" structure to check for understanding.




The following table describes several examples of dos and don'ts:

Do | Don't  
---|---  
**User** : I'm traveling to Italy.**Voice agent** : Sorry, which country? | **User** : I'm traveling to Italy.**Voice agent** : Sorry, I'm having trouble. Can you rephrase? Where are you going?  
**User** : I want to pay $80.**Voice agent** : You mean $80? (Repeats only the information that needs confirmation) | **User** : I want to pay $80.**Voice agent** : Do you want to pay $80? (Repeats the redundant "want to pay" information)  
  
## Conversation techniques

This section describes techniques to help the voice agent build trust with users and make conversations run more smoothly.

### Designing actionable questions

Design explicit and actionable questions for your voice agent to ask the user. For example, consider the following do's and don'ts:

Do | Don't  
---|---  
Do ask open-ended questions like "When are you traveling?" which prompts the user to provide dates if they know them, or say "I don't know" otherwise. | Don't ask "Do you know your travel dates?" which only prompts a yes or no answer and is less actionable.  
Do ask "Would you like to check the order status of another package?" | Don't ask "Would you like to continue with the order status of another package?"  
  
You should also prepare your voice agent for situations where the user may answer a question implicitly, as people often do in natural conversations. For example, consider the following interaction:

**Voice agent** : Go to **Account** , then click on **Usage** , then on **Usage by line**. Let me know when you get there.

**User** : It says I can't see data from 3 months ago or older.

The user's response implies that they successfully arrived at the target screen, but that they still needed more help. Your voice agent should anticipate such implications, instead of expecting the user to only say "I got there," or "I didn't get there."

### Gaining user trust

Voice agents can show users that they are listening through the use of acknowledgements and specific details. If the voice agent provides generic answers, users may feel that the voice agent sounds unnatural.

  * Use _acknowledgements_. For example, consider the following exchange, where "No problem" is used as an acknowledgement:

**User** : I want to set a payment arrangement for Monday.

**Voice Agent** : No problem. How much would you like to pay on Monday?

  * Add specific details to show that the voice agent is actively listening to the user. For example, in the above exchange, the phrase "on Monday" is a specific detail that indicates the voice agent has heard what the user said.

  * Address the user's request as quickly as possible and exclude any unnecessary steps. In the following example, the extraneous information may cause user frustration:

**User** : Is there an outage in my area?

**Voice Agent** : We know how important it is for you to stay connected. Let's find out what's causing this issue. Please tell us the last 4 digits of the line that you're experiencing issues on. If the issue is on multiple lines, just provide one for now.

**User** : 1234

**Voice Agent** : Thanks. Let me look into next steps for this line. Now, let's get started. Temporarily disabling and then re-enabling HD Voice can do the trick... Did that work?"

  * Make sure the conversation between the user and voice agent is balanced. Users may feel an uncomfortable lack of agency in the conversation if the voice agent dominates the conversation. Prioritize Who/Where/What/When/How questions over Yes/No questions.

  * Ensure that the user's conversation transitions smoothly when they want to escalate to human agents.




## Additional information

  * See the [conversation design guide](https://developers.google.com/assistant/conversation-design/welcome) provided by the Actions on Google team.

  * See the [Voice Playbook](https://blog.google/technology/next-billion-users/voice-users-playbook/) for the Next Billion Users.

  * See the [Cloud Text-to-Speech SSML guide](https://docs.cloud.google.com/text-to-speech/docs/ssml).

  * Read about [speech acts](https://en.wikipedia.org/wiki/Speech_act) for more information about designing actionable questions.




[ Previous arrow_back  General agent design best practices  ](https://docs.cloud.google.com/dialogflow/es/docs/agents-design)

[ Next Cloud logging  arrow_forward  ](https://docs.cloud.google.com/dialogflow/es/docs/logging)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
