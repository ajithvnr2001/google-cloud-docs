---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics/
title: Quality AI basics \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:45:50.230057+00:00
---

# Quality AI basics  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Quality AI basics Stay organized with collections  Save and categorize content based on your preferences. 

Quality AI uses an AI model to automatically analyze customer service conversations, or interactions between contact center agents and users. The AI model analyzes chat or voice transcripts.

## Conversation details

Conversations contain the following details. These details include identifiers and metrics for analysis.

  * **Agent ID** : A unique number assigned to each agent that identifies the conversations they have handled.
  * **Agent total score** : The average score of an agent's performance across that agent's conversations.
  * **AHT** : Average Handling Time, the average duration of an agent's conversations in a specified period.
  * **Average agent score** : The average across all your agents' total scores. (See **Agent total score**.)
  * **Average agent quality score** : Average of the quality scores produced by a single agent's conversations over a specified period. (See **Quality score**.)
  * **Average conversation score** : Average score across all conversations.
  * **Average quality score** : Average of the quality score over a specified period. (See **Quality score**.)
  * **Channel** : The medium of conversation between a customer and an agent. Channel has one of two values: voice or chat.
  * **Conversation ID** : A unique number assigned to identify each customer service conversation.
  * **Conversation total score** : Sum of question scores in a single conversation.
  * **CSAT** : Customer satisfaction rating from your conversation metadata, generally ranging from 1-5.
  * **Duration** : Time the conversation spans, beginning to end.
  * **Primary topic** : The concern discussed during a conversation, determined by topic modeling. Quality AI displays a primary topic only if you have used topic modeling on that conversation.
  * **Quality score** : The overall score assigned for a scorecard.
  * **Question** : Used to evaluate an agent's performance in a conversation. You enter your questions into Quality AI, and the agent is then rated on whether they satisfied the criteria for each question.
  * **Sentiment** : The main emotional state conveyed by the conversation. Sentiment has one of three values: positive, neutral, or negative. Quality AI displays a sentiment only if you have used [sentiment analysis](https://docs.cloud.google.com/gemini-enterprise-cx/insights/sentiment-analysis) on the conversation.
  * **Silence** : Time during which neither the customer nor the agent spoke or typed.
  * **Start date** : The date on which the conversation began, based on your agent's region.
  * **Start time** : The time at which the conversation began, based on your agent's region.
  * **Total volume** : The total number of conversations that a single agent handled in a specified period.



## Scorecards

The scorecard is a structured framework used to assess conversation quality and the performance of contact center agents during conversations. Each contact center has its own scorecards.

Each scorecard consists of the following information:

  * Question (Example: Did the agent provide an appropriate product compliment?).
  * Optional: Tag to group the questions into categories.
  * Instructions for interpreting the question and defining each answer choice.
  * Tracing to include system events and metadata.
  * Answer type (can be text, numbers, or yes/no).
  * Answer choices that define the possible answers based on answer type (For example, yes and no, a list of numbers, or some text responses).
  * Score to set the points earned for each answer choice. The maximum score for a single question is determined by the highest score among all the answer choices.



You can create multiple scorecards in a single Google Cloud project. If each scorecard contains different questions, you can see multiple quality scores for the same conversations. Each score is then based on different criteria.

### Predefined questions

You can use predefined questions in your scorecard with questions and answer choices that you cannot edit. Customer Experience Insights (CX Insights) defines the instructions and answer choices. These questions have an ID indicating their version. You can add predefined questions to any scorecard to use for Quality AI analysis.

Predefined questions identify the following metrics:

  * Conversation outcome
  * Escalation initiator
  * AI aversion



#### Conversation outcome

Conversation outcomes identify the outcome of the conversation in the context of the user's task.

  * **Abandoned** : The user stopped responding or dropped off the conversation before any of the user's tasks were completed and without being escalated to a human agent.
  * **Partially resolved** : The agent understood the user's intent and completed some, but not all of the user's tasks. The conversation ended before all the user's tasks were fully completed.
  * **Escalated** : Conversation transferred to a human agent, initiated by the user's request.
  * **Redirected** : Conversation transferred to a human agent, initiated by the agent.
  * **Successfully resolved** : The agent understood the user's intent, completed the user's tasks, and received an explicit acknowledgement from the user at the end of the conversation.
  * **Unknown** : The conversation's outcome could not be identified.



#### Escalation initiator

The escalation initiator identifies if there is an escalation to a human agent and who initiated that process.

  * **User** : The user initiated an escalation to a human agent.
  * **Agent** : The agent initiated an escalation to a human agent.
  * **No transfer** : The conversation was not escalated to a human agent. This includes cases where the agent redirected the user to a different resource to resolve their request, but did not escalate to a human agent.



#### AI aversion

The AI aversion metric highlights situations where customers express reluctance, attempt to bypass the system, or show frustration when interacting with virtual agents early in a conversation. This distinction helps separate initial customer preference for a human representative from standard escalations caused by virtual agent errors later in the session.

Quality AI automatically categorizes each customer turn into one of the following levels:

  * **High aversion** : The user refuses to engage with the agent from the start and doesn't state any intent or issue, includes messages with direct demands for a human. Or, the user expresses explicit hostility toward AI automation, such as _I hate talking to robots_.
  * **Moderate aversion** : The user shows reluctance to engage with the virtual agent by providing only a vague or overly generic intent (for example, _help_ or _problem_) such that the virtual agent lacks enough information to assist, and immediately demands a human transfer. Alternatively, the user states an intent but refuses to answer basic clarifying questions from the virtual agent, insisting on reaching an agent instead.
  * **No aversion** : The user treats the virtual agent as a valid support channel by engaging naturally and providing actionable issue details. One example of a normal escalation due to virtual agent failure, and not AI aversion, is when the user provides a specific intent (for example, _My internet is down_) and later escalates because the virtual agent provided an inaccurate or unhelpful answer.



CX Insights and Customer Experience Agent Studio dashboards display the following AI aversion metrics to track early escalation trends:

  * **AI Aversion Rate (Summary Card):** Shows the percentage of overall conversations where customers demonstrate AI aversion within the first two message exchanges. Click the card to open detailed metrics.
  * **AI Aversion Breakdown (Chart):** Visual breakdown of the distribution between high, moderate, and no aversion levels.



Select the summary card or click any section of the breakdown chart to view session details, filtered for conversations with early AI aversion.

### Custom tags

Use tags to group questions into categories on a given scorecard. Each project includes default BUSINESS, COMPLIANCE, and CUSTOMER tags. In addition to these three tags, you can use CX Insights to create your own custom tags. The custom tags are limited to 10 per Google Cloud project. If you need more than 10 tags, contact your CX Insights point of contact.

Custom tags are _independent_ of questions or scorecards containing those questions. You can create custom tags from the tag management page or from the question creation dialog. After you create a custom tag, you can apply it to any question in any scorecard in a CX Insights project.

You can perform the following operations on custom tags when you edit a scorecard.

  * Add tags to existing questions.
  * Remove tags from existing questions.



## Conversation scores

Quality AI automatically evaluates conversations against the scorecards you supply. For each question, do the following:

  * Define the answer type.
  * List the possible answer choices.
  * Set the score for each answer choice.



### One scorecard

A conversation score consists of the total received score divided by the maximum possible score for that conversation. The total received score is the sum of all the points obtained from the assigned answer choices for each question. The maximum possible score is the sum of the maximum scores for each question. Any question assigned an N/A response is removed from this conversation score calculation. The conversation score is displayed as a percentage.

### Multiple scorecards

A conversation can receive multiple conversation scores. Each conversation score reflects the agent's performance during that conversation according to the questions on a single scorecard. When each scorecard contains a different group of questions, you can evaluate a single conversation against multiple types of questions.

### Manual updates

After analyzing a conversation, you can manually update the answer to any question. When you manually update an answer, Quality AI automatically adjusts the score for that question and the corresponding conversation score. In addition, the Quality AI console marks that question and conversation with a visual icon to indicate that the answer was manually updated. Lastly, Quality AI automatically adds any manually updated answer as an example conversation to improve the AI model.

### Source menu

In the CX Insights console, each page in the Quality AI section includes a **Source** menu. This menu lists your scorecards so that you can choose which information to display.

For example, on the **Conversations** page, you can view the scores for each conversation. Those scores depend on which scorecard Quality AI evaluated the conversations against. So, if you select a different scorecard from the **Source** menu the scores for the same conversations might change.

### Examples

The following examples illustrate how a conversation score is calculated.

_Example 1_

If the following is true:

  * A scorecard has 10 questions
  * Each question is a yes or no question
  * Yes receives a score of 1 and No gets 0
  * A conversation has received all "Yes" answers



Then the conversation score is 100%.

_Example 2_

If the following is true:

  * A scorecard has 10 questions
  * Each question is a yes or no question
  * Yes receives a score of 1 and No gets 0
  * A conversation received 7 "Yes" responses, 2 "No", and 1 "N/A"



Then the "N/A" question is removed so there are 9 total possible points. The conversation received 7 out of 9 possible points. The conversation score is rounded and displayed as 78%.

## What's next?

  * [Get started with Quality AI](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-setup-guide)
  * [Quality AI best practices](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
