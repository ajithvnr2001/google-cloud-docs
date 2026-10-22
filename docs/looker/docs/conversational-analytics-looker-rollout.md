---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout/
title: Recommended setup and rollout strategy for Conversational Analytics in Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:32.166912+00:00
---

# Recommended setup and rollout strategy for Conversational Analytics in Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-rollout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Recommended setup and rollout strategy for Conversational Analytics in Looker Stay organized with collections  Save and categorize content based on your preferences. 

This guide is intended to help plan the rollout of Conversational Analytics to users of a Looker instance. It recommends the following phased approach for implementing Conversational Analytics in Looker:

  * Phase 1: Curate data and define the initial scope
  * Phase 2: Configure agents and validate internally
  * Phase 3: Expand Conversational Analytics adoption to more users



This approach lets you start with a small, controlled scope, validate your setup, and then expand to more users and data.

## Phase 1: Curate data and define the initial scope

In this phase, prepare your data for users to query with Conversational Analytics and define the scope of the initial deployment. Follow these recommendations for starting with a small and controlled scope:

  * **Initial setup** : Follow the setup steps in [Set up Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup) for your instance.
  * **Limit initial user access** : To enable internal testing and validation, use Looker's permission system to grant the [required permissions to use Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) to a small set of users who are familiar with the data. To start, consider limiting access to one or two models that you have curated for Conversational Analytics.
  * **Select curated Explores** : Start with one or two well-structured Explores that are based on relatively clean data and that provide clear business value. Optimize these Explores for Conversational Analytics in Looker by following the detailed instructions in [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices#lookml-best-practices-for-conversational-analytics).



## Phase 2: Configure agents and validate internally

In this phase, [build and refine your Conversational Analytics agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents), and then thoroughly test them with internal users to confirm accuracy and effectiveness. This phase involves the following steps:

  1. **Create curated agents** : Create Conversational Analytics agents that are based only on the curated Explores that you prepared during the curation and initial setup phase.
  2. **Refine with agent instructions** : Use [agent instructions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#write-agent-instructions) to provide additional context and further guidance. For example:

     * Use the [`synonym`](https://docs.cloud.google.com/looker/docs/reference/param-field-synonyms) LookML parameter to define synonyms for field names or values.
     * Provide specific context or rules for how certain fields should be used.
**Note:** Agent instructions can diverge from your LookML. Be mindful of potential discrepancies.
  3. **Validate internally and iterate** : Thoroughly test the agents with users who are familiar with the data. Ask various questions, test edge cases, and identify weaknesses. Make the following changes based on feedback from testing:

     1. Refine the LookML. For example, adjust the values for the [`label`](https://docs.cloud.google.com/looker/docs/reference/param-field-label), [`description`](https://docs.cloud.google.com/looker/docs/reference/param-field-description), or [`hidden`](https://docs.cloud.google.com/looker/docs/reference/param-field-hidden) LookML parameters.
     2. Adjust agent instructions.
     3. Continue flagging issues with data quality.



## Phase 3: Expand Conversational Analytics adoption to more users

In this phase, expand Conversational Analytics adoption to more users by granting access, collecting feedback, and iterating on your agents. This phase involves the following steps:

  1. **Grant targeted access** : [Grant Conversational Analytics access](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) to additional users, and encourage those users to use the specific, vetted agents that you have created.
  2. **Launch and collect feedback** : Actively solicit feedback on the following topics:

     * Accuracy of responses
     * Ease of use
     * Missing information or confusing results
  3. **Iterate continuously** : Use feedback to make further refinements to LookML and agent instructions, and prioritize data cleanup efforts.

  4. **Expand access** : Once the agents prove stable and valuable, expand access to other relevant user groups and introduce new curated agents by granting these users the [appropriate permissions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions). You can also introduce new curated agents and expand access to the models that are available to the Gemini role, following the same processes that were used in the previous phases.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
