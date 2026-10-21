---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments/
title: Experiments \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:37:55.235033+00:00
---

# Experiments  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Experiments Stay organized with collections  Save and categorize content based on your preferences. 

Experiments are used to compare the performance of multiple flow versions (_variant_ versions) to a _control_ version (normally a production version) while handling live traffic. You can allocate a portion of live traffic to each flow version and monitor the following metrics:

  * **Contained** : Count of sessions that reached [END_SESSION](https://cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic) without triggering other metrics below. Only available to agents using a telephony integration.
  * **Live agent handoff rate** : Count of sessions [handed off to a live agent](https://docs.cloud.google.com/dialogflow/cx/docs/concept/fulfillment#handoff).
  * **Callback rate** : Count of sessions that were restarted by an end-user. Only available to agents using a telephony integration.
  * **Abandoned rate** : Count of sessions that were abandoned by an end-user. Only available to agents using a telephony integration.
  * **Session end rate** : Count of sessions that reached [END_SESSION](https://cloud.google.com/dialogflow/cx/docs/concept/handler#symbolic).
  * **Total no-match count** : Total count of occurrences of a [no-match event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event-built-in).
  * **Total turn count** : Total number of conversational turns (one end-user input and one agent response is considered a turn).
  * **Average turn count** : Average number of turns.



## Preparation

To prepare for an experiment:

  1. Decide which flow will be used for the experiment. You cannot run multiple experiments on a single flow, so ensure that you have partitioned your agent into multiple flows.
  2. Create multiple [versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) for your flow. The differences between each version could be small or large, depending on what you want to compare.
  3. Decide on the amount of traffic that will be allocated to your experiment. If you are testing minor changes, you might start with a higher amount of traffic. For large changes that may be disruptive, consider allocating a small amount of traffic to your experiment.



## Create an experiment

To create an experiment:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project to open the agent selector.
  3. Select your agent to open the agent builder.
  4. Select the **Manage** tab.
  5. Click **Experiments** to open the Experiments panel.
  6. Select the **Status** tab.
  7. Click **Create**.
  8. Enter a description.
  9. Select the [environment](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) that you want to run the experiment from.
  10. Select the flow for the experiment.
  11. Optionally enter the number of days in which the experiment will automatically stop.
  12. Enter the control flow version and the percentage of traffic that will go to the control version.
  13. Enter one to four variant flow versions, and the percentage of traffic that will go to the variant version.
  14. Optionally, click **Enable auto rollout and steps** for a gradual rollout of traffic to the variant flow. An automated experiment is based on _steps_ , which are time durations in which a percentage of traffic is increased to the variant flow. Auto rollout only supports one variant flow. 
     1. Under **Rollout rules** , you can set one or more conditional rules to determine how the experiment should proceed through the steps. 
        1. If you select **Match at least one rule** , the experiment proceeds to the next step if at least one rule and the time duration for the current step are met.
        2. If you select **Match all rules** , the experiment proceeds to the next step if all rules and the time duration for the current step are met.
        3. If you select **Steps only** , the experiment proceeds according to the time durations for each step.
     2. Under **Increase steps** , define a percentage of traffic to allocate to the variant flow and a time duration for each step. The default time duration for each step is 6 hours.
     3. Select **Stop conditions** to set one or more conditions under which to stop sending traffic to the variant flow. Note that you cannot restart a stopped experiment.
  15. Click **Save**.



## Start and stop an experiment

You can start a saved experiment or manually stop a running experiment at any time. Stopping an experiment will cancel the traffic allocation and will revert traffic to its original state.

**Note:** If you stop an experiment while it is pending, results will not be available. If you stop an experiment while it is running, results might be inconclusive or missing.

To start or stop an experiment:

  1. Open the Experiments panel.
  2. Select the **Status** tab.
  3. Click **Start** or **Stop** for an experiment in the list.



## Manage experiments

**Note:** You can change variant traffic allocation while an experiment is running.

You can edit or delete experiments at any time:

  1. Open the Experiments panel.
  2. Select the **Status** tab.
  3. Click the option _more_vert_ menu for an experiment in the list.
  4. Click **Edit** or **Delete**.



## Monitor status of experiments

All experiments, regardless of their status, can be found on the experiments panel. Experiments can have four different statuses:

  * **Draft** : Experiment has been created, but it has never run.
  * **Pending** : Experiment has started recently, but results are not available yet.
  * **Running** : Experiment is running and interim results are available.
  * **Completed** : Experiment has been completed due to automatically or manually being stopped.



## Viewing experiment results

To see experiment results:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Select your project to open the agent selector.
  3. Select your agent to open the agent builder.
  4. Select the **Manage** tab.
  5. Click **Experiments** to open the Experiments panel.
  6. Select the **Results** tab.
  7. Select an environment and experiment to see the results.



Green colored results suggest a favorable outcome, while red suggests a less favorable result. Notice that in some cases, higher/lower numbers are not necessarily better (high abandonment rate / low abandonment rate).

**Note:** You will see "no experiment result" if not enough conversations have been through each variant of the experiment.

## Limitations

The following limitations apply:

  * The [Enable conversation history](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent-settings#settings-general) agent setting must be enabled.



[ Previous arrow_back  Test cases  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case)

[ Next Continuous tests and deployment  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/continuous-tests)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
