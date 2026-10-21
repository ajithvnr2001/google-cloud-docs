---
url: https://docs.cloud.google.com/contact-center/insights/docs/agent-engagement/
title: Agent engagement platform \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:20:43.085770+00:00
---

# Agent engagement platform  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/insights/docs/agent-engagement/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Agent engagement platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The agent engagement platform is a feature within Quality AI for managing the performance of contact center agents. The platform provides a succinct summary of an agent's performance to reduce information overload for contact center owners and managers, and help human agents understand their own performance.

In the agent engagement platform, you can view historical agent performance data, and conversation assessments. Displaying this information also significantly reduces the time it takes for contact center managers to prepare for agent coaching sessions.

## View platform

Follow these steps to view the agent engagement platform.

  1. Go to the Customer Experience Insights console, sign in with your Google Account, and select your project.

[CX Insights console](https://ccai.cloud.google.com/insights)

  2. Click **Quality AI** > **Agents** > **Human agent**.

  3. Select an agent.




## Agent identification

The agent engagement platform identifies an agent within their individual profile, which includes the following details.

  * **Display name** : Displays the name of an agent.
  * **Agent ID** : Identifies an agent.
  * **Team** : Names the team that the agent belongs to.



## Agent performance

The agent engagement platform provides a summary and detailed data about an agent's performance.

### Overall summary

Quality AI uses a large language model (LLM) to provide an AI-generated summary of agent performance based on the agent's overall scorecard scores and category scores for the business, customer, and compliance categories. The summary focuses on the following comparisons:

  * **Self-Comparison (Current vs. Previous)** : The summary compares the current and previous time periods by subtracting the current from the previous scores for each metric. If the current score is higher than the previous score, it indicates improvement. A lower current score indicates a decline.
  * **Category-Level Performance (Current Period)** : The summary analyzes the scores for each category in the current time period you specify. Comparing the scores across categories identifies areas of strength and areas where an agent could improve.



The agent performance summary also provides actionable insights to improve an agent's performance in specific areas.

### Individual metrics

The agent engagement platform displays agent performance data across all scorecards for a time period you choose. Quality AI uses its own [metrics](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics#conversation_details) to measure performance data. Agent performance data is separated into the following two categories:

  * Scorecard (quality-related) metrics
  * Operational metrics



#### Scorecard (quality-related) metrics

For each question on each scorecard, the agent engagement platform displays the following data about agent performance:

  * Average quality score
  * Comparison of average quality scores between the selected agent and other agents in the selected authorized view
  * Comparison of average quality score between the current and previous time period



#### Operational metrics

The agent engagement platform also displays a separate graph of the changes for each of the following metrics over the time period you choose. Each graph also displays the following metrics averaged over all agents in the selected authorized view. You can use this average to compare the performances of the selected agent with other agents.

  * Call volume
  * Average CSAT
  * Average handle time 
  * Average silence percentage (applicable to voice agents) 



### Expertise and coaching opportunities

The agent engagement platform helps identify areas where agents are performing well compared to their peers, and where they need improvement. The platform determines both expertise and coaching opportunities in terms of topics identified with [topic modeling](https://docs.cloud.google.com/gemini-enterprise-cx/insights/topic-modeling-overview) or [scorecard questions](https://docs.cloud.google.com/gemini-enterprise-cx/insights/qai-basics). The platform uses Quality AI scores to evaluate an agent's performance, and compares them with the scores of other agents in the same authorized view.

  * **Expertise** : Topics or scorecard questions for which the agent's average quality score or average question score, respectively, was in the top 30th percentile of those scores among all agents listed in the same authorized view.
  * **Coaching opportunities** : Topics or scorecard questions for which the agent's average quality score or average question score, respectively, was in the bottom 30th percentile among all agents listed in the same authorized view.



For example, to determine expertise or coaching opportunities in terms of topics, the platform does the following:

  1. Calculates the average quality score over all scorecard questions for conversations assigned to that topic.
  2. Ranks agents in an authorized view based on their scores.
  3. Checks if the agent whose page you are viewing is in the top or bottom 30th percentile of the agent list. \- If not, no entries are displayed. \- If so, the topic and the agent's score for that topic appears as an expertise or coaching opportunity.



The agent engagement platform uses the same process to calculate expertise and coaching opportunities for scorecard questions.

#### Example

Suppose an authorized view has data on five agents, each with an average quality score for two topics.

Agent | Topic 1: Billing issues | Topic 2: Customer returns  
---|---|---  
Alice | 80% | 30%  
Bob | 70% | 40%  
Charlie | 60% | 50%  
Dan | 50% | 60%  
Eve | 40% | 70%  
  
Viewing the agent engagement platform page for Alice, who's in the top 30th percentile for **Billing issues** , reveals billing issues as her expertise. Because she's in the bottom 30th percentile for **Customer returns** , that topic is listed as her coaching opportunity.

## Assessments

Lastly, the agent engagement platform displays a list of the agent's [conversation assessments](https://docs.cloud.google.com/gemini-enterprise-cx/insights/conversation-assessments).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
