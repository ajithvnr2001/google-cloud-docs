---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation/
title: Evaluation \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T22:59:00.168495+00:00
---

# Evaluation  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Evaluation Stay organized with collections  Save and categorize content based on your preferences. 

Evaluation is a critical tool for testing your agent's performance and ensuring it behaves as expected in specific situations. It lets you automate testing, catch regressions after making changes, and measure the quality of your agent's responses to improve your agent quality.

To get started, click the **Evaluate** button at the top of the agent builder.

## Evaluation concepts

**Test case** : Each test case is a specific, self-contained test scenario or prompt designed to assess the agent's performance. You can create two different types of test case:

  * **Scenario** : An AI-powered feature to bootstrap your testing and ensure comprehensive test coverage. You describe a user's goal, and the system automatically simulates the user and generates conversations to test the agent's ability to handle the scenario in a robust way. Scenarios are a useful way to experiment and help define golden conversations.
  * **Golden** : Ideal for regression testing. You provide a specific, "ideal" conversation path, and the evaluation checks if the agent's behavior matches this ideal path, including tool calls.



**Run** : An evaluation _run_ represents a complete, single execution of a set of golden and scenario test cases against the performance of the agent you're testing. Each run can include one or more test cases.

**Result** : A test case _result_ refers to a single execution of a specific test case in a single run. If a test case is run multiple times during a single evaluation run (for example, to check for consistency, flakiness, and so on), each individual execution is an individual result. Results are displayed as rectangular icons in columns in each test case row, showing a red X if the run failed and a green check-mark if it passed.

**Tags** : Test cases can be grouped with _tags_ for easier management.

## Create test cases

To create and access test cases for your agent, click the **Evaluate** button at the top of the agent builder. You can create and manage either golden or scenario based test cases.

## Scenario

Scenario-based test case uses AI to automatically generate a variety of conversations based on a high-level user goal you define. With these test cases, rather than providing specific golden conversations, you select generated scenarios or describe specific scenarios that must be tested. This is a powerful tool to help you explore edge cases and testing your agent's robustness without having to manually write every possible conversational path.

Once these scenarios are working well, you can save them as golden conversations.

To create a scenario:

  1. Click **Create scenario**. Multiple scenarios are suggested for you.
  2. You can either generate scenarios based on the selections or you can create a new scenario from scratch.



When you are viewing the list of scenarios, you can list the details and conversation list for each scenario by clicking the scenario.

To save a scenario as a golden conversation:

  1. Select the scenario.
  2. Click the menu button in the top right corner.
  3. Select **Save as golden conversation**.



### Scenario user goal

Each scenario has a user goal, which describes the goals of the end-user when using the agent application. For example:
    
    
    Securely book a specific room at a chosen hotel and receive a confirmation.
    

Based on your user goal, CX Agent Studio automatically generates conversations used for evaluation.

### Scenario variables

When defining a scenario, you can provide [variables](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio) that should be used for the scenario.

### Scenario expectations

In order to perform an evaluation, you define expectations for the test case.

Expectations can be one of two types:

  * **Message** : An expected agent response.
  * **Tool call** : A tool call with expected inputs and outputs.



Expectations can have the following conditions:

  * Must have
  * Must not have
  * After tool call
  * Variable value



To create an expectation:

  * Click a particular scenario to open its details.
  * In the **Expectations** section, click **View all**.
  * Follow the interface instructions to create expectations for the scenario.



## Golden

These test cases are used to define ideal conversation paths for regression testing so that core, critical conversational paths don't break as you update the agent. There are multiple options for creating a golden conversation:

To import a conversation from the simulator:

  1. Start a conversation using the simulator.
  2. Click the three vertical dots at the top right corner of the simulator to bring up the simulator menu.
  3. Click **Save as golden**.
  4. Enter a name for the golden test case and click **Save**. It will now appear in the **Evaluation** tab.



To create a test case from conversation history:

  1. Navigate to the **Evaluation** tab.
  2. Click **\+ Add test case**.
  3. Select **Golden**.
  4. Click **Next**.
  5. Click **select from conversation history**.
  6. In the window that appears, select the conversation you'd like to save as a golden test case. You have the option of searching by conversation ID.
  7. If you have enabled redaction, check agent responses and variables for redaction before proceeding with missing information.
  8. Click **Add**.



To create a Test Case from scratch:

  1. Navigate to the **Evaluation** tab.
  2. Click **\+ Add test case**.
  3. Select **Golden**.
  4. Click **Next**.
  5. Click **Create from scratch**.
  6. In the window that appears, add a **Display name** for the test case.
  7. Add text for user input and agent expectation as required. Click **\+ Add user input** and **\+ Add agent expectation** to add responses. Click **\+ Add turn** to add a new conversation turn to the test case.
  8. Click **Create** to add the golden test case to your list of test cases.



To create a test case from a simulated conversation in a scenario test case:

  1. Navigate to the evaluation run results page.
  2. Click the **menu icon** (three vertical dots) to the right of your selected conversation and click **Save as golden conversation**.



To batch upload test cases from a file:

For details on file format and a CSV template, see the [Golden test cases CSV format](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation-batch-upload) page.

### Golden expectations

In order to perform an evaluation, you define expectations for the golden test case. An expectation is a specific outcome that you anticipate from the agent at a particular point in the conversation. During evaluation, the actual agent behavior is compared against these expectations.

Expectations can be one of the following types:

  * **Message** : An expected text response from the agent to the end-user. The evaluation checks if the agent's response semantically matches this expectation.
  * **Tool call** : An expectation that the agent calls a specific tool and response. You can also specify expected input arguments for the tool call.
  * **Agent Handoff** : An expectation that the agent transfers the conversation to a human agent or another bot.

**Note:** In stable replay mode, expected variables and tool responses are used to inject context into the conversation. In naive replay mode, these values have no effect on the result.

To create an expectation:

  1. Click a particular golden test case to open its details.
  2. In the **Details** section, Click **View golden**.
  3. Follow the interface instructions to add or modify expectations.



## Evaluation settings

In the heading row of the test cases list, you can configure evaluation settings:

  * **Goldens** : 
    * **Golden pass/fail criteria** : Set the logic for whether a simulated conversation passes or fails.
    * **Turn level** : These rules judge each individual turn. If any of these thresholds are not met, then the specific metric will be color-coded red as a failure. 
      * **Semantic similarity** : Threshold value for semantic similarity.
      * **Tool correctness** : Threshold value for tool correctness.
      * **Hallucinations** : If disabled, hallucinations are excluded from pass/fail.
    * **Expectation level** : These rules judge the expectations within a turn. If any of these thresholds are not met, then the specific metric will be color-coded red as a failure. 
      * **Tool correctness** : Threshold value for tool correctness.
    * **Golden run method** : Choose between naive or stable replay validation.
    * **Tool fake** : Use mocked data instead of real production API calls.
  * **Scenarios** : 
    * **Scenario pass/fail criteria** : Set the logic for whether a simulated conversation passes or fails.
    * **Conversation initiator** : Set who starts the conversation, user or model.
    * **Tool fake** : Use mocked data instead of real production API calls.
  * **Audio evaluation**
    * **Audio evaluation recordings**



## Run evaluations

To run an evaluation, you can either click the run button on the test case row, or you can select multiple test cases and run them.

If you have saved multiple [versions](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/version), you can select which agent version to use, or automatically save your draft agent as a new version for the run.

After an evaluation run, the metrics will be updated and the results will be presented.

If you click a particular run evaluation, you can see the detailed results for a run. In addition to the standard metrics, the following are displayed:

  * Failed turns
  * Paginated list of all turn details, which includes both actual and expected agent responses.



For golden test cases, you may see the term "stable replay" which is clarifying that the test ran in a consistent environment (i.e. without shifting context / input).

### Use AI to improve test cases (PREVIEW)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** Presently, AI improvements only support agent applications with a single agent.

You can optionally use AI to help troubleshoot a run and suggest ways to improve agent quality. AI suggestions are optimal when the number of runs (run count) is 3 or more. To enable AI, select the test case(s) you'd like to evaluate and click **Run selected**. In the window that pops up, check the box next to **Find issues with AI**.

After the run completes, you will see AI-based suggestions on the results page. Gemini automatically generates a downloadable `loss_report` that summarizes aspects of the agent's performance and highlights areas that can be improved.

Any user can view AI-suggested fixes, but only the person who initiated the run can take actions based on the results.

Click **Ask Gemini** to interact with the helper agent. You will first see the **loss report** that explains high level problems with the model or agent. You can ask the helper agent to explain the report, which will summarize the report and may suggest fixes. After fixes are applied, you can ask the helper agent run evaluation again.

## Import and export

You can import and export evaluation test cases, runs, and results in either YAML or JSON format. When you import, be sure that the receiving agent contains all of the resources (tools, variables, and sub-agents) defined in the exported data.

To export test cases:

  1. Select one or more test cases.
  2. Click **Export test cases**.
  3. Select a format.
  4. A zip file will be downloaded.



To import test cases:

  1. Click **\+ Add test case**.
  2. Select **Golden**.
  3. Click **Next**.
  4. Upload the zip file.
  5. If there are any conflicts with the import, you will be guided for how to handle them.
  6. Click **Create**.



To export evaluation runs and results:

  1. Select one or more evaluation runs.
  2. Click **Export run**.
  3. Select a format.
  4. A zip file will be downloaded.



## Metrics

Each test case result includes a set of metrics that measure the agent's performance against your selected test cases. Metrics are calculated either at the turn level or expectation (conversation) level as indicated in the console.

In all cases, you can customize the values required to for the run pass in the **Settings** menu in the **Evaluate** tab.

### Tool correctness

Calculated for _golden and scenario_ test cases. This metric reflects the percentage of expected parameters that were matched given an expected tool call and its expected parameter values. Missed tool calls are scored as 0, tool calls with no input parameters are scored as 1 if present. If an unexpected tool call is made during a _golden evaluation_ , the result will be considered a failure, but this has no impact on the tool correctness value.

### User goal satisfaction

Calculated for _scenarios_. User goal satisfaction is a binary metric designed for user-simulation evaluations. It measures whether the simulated user believes their goals were achieved (0=no, 1=yes). Inputs are the `user_goal` as defined by the simulated user configuration and a conversation transcript. If the `user_goal` provided doesn't specify an explicit or implied goal, the output score is -1.

### Hallucinations

Available for _golden and scenario_ test cases. Hallucination scores are calculated for each generated turn. This metric reflects whether or not the agent made claims that are not justified by the agent's context (0=no, 1=yes). Context is made up of any preceding turns in the conversation, session variables, tool calls, and agent instructions. This metric is only computed for turns containing tool calls. It does not detect hallucinations within tool calls; tool calls provided as context are presumed to be correct. In order to minimize false positives, the metric might return a score of N/A if a response contains no factual claims or only common knowledge that's already been established.

You can enable and disable hallucinations in the evaluation settings.

### Semantic match

Calculated for _golden_ test cases. This metric measures the extent to which an observed agent utterance matches with an expected agent utterance. **Semantic match is computed at the turn level**. Returned values range from 0 (completely inconsistent or contradictory) to 4 (fully consistent).

### Scenario expectations

Calculated for _scenarios_. This metric is a measure of whether or not the behavior of the agent as expected by the simulated users was satisfactory or not (0=no, 1=yes). Two types of simulated user expectations are supported:

  * Tool call expectations: Calculated similarly to [tool call correctness](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/evaluation#tool_correctness) with the following exceptions: 
    * Results are either 0 (no) or 1 (yes).
    * Unexpected tool calls aren't penalized. Expectations are meant to specify the set of tool calls that are essential for a conversation to meet the simulated user's expectations.
    * When a tool call input expectation is met, the call is intercepted and replaced with a mock return value at runtime.
  * Agent response expectations: Checks if any agent response in the conversation contains an expected string.



### Task completion

Calculated for _scenarios_. Task completion is a measure of conversation quality. It jointly measures whether or not the user's goals were achieved AND that the agent behavior was correct. It is defined as:

`User_Goal_Satisfied AND no_hallucinations_detected AND Expectations Satisfied`

## Personas

Personas are simulated user personas that you can customize and use for agent testing with _scenario_ test cases. This feature is useful for ensuring that the agent appropriately interacts with the types of human users they are likely to encounter at runtime.

If you do not select a persona, a random persona will be selected for each scenario result.

This feature is available for use with both text and audio inputs.

### Create a persona

  1. To create a persona, navigate to the **Evaluate** tab and click **Persona management** (next to the Settings icon).
  2. Click **\+ Add persona**.
  3. In the menu that pops up, enter a **Name** , **User personality** , and any additional **User context** (such as age, location, why they are calling, and so on).
  4. Click **\+ Add**.



To run an evaluation using a persona:

  1. Navigate back to the main **Evaluate** page and select one or more scenario test cases. Click **Run selected**.
  2. In the window that pops up, select the persona you just created from the **Personas** drop-down menu and click **Run**.



## Evaluations and hillclimbing best practices

When building a new agent using [modular components](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/modular-components), create dedicated test cases for each agent variant you have, for example:

  * Voice and chat
  * SMS and chat SDK
  * Brand A, B and C, and so on



Create additional cases to check for cross-variant instruction leakage. For example, chat-specific instructions should not show up for cases run in voice mode, and vice versa.

Ensure that cases are run against the right agent:

  * For modality (chat vs voice) or channels, running the case against the _right deployment_ automatically ensures alignment.
  * Each deployment encapsulates the modality, model used and channel.
  * For builder-defined variable conditionals, inject the variable value when running the case. For example: `brand_name == "Cymbal Retail"` or `brand_name == "Acme Corp"`.



Ask your favorite coding agent to iteratively improve the CX Agent Studio agent until all test cases meet their target metrics or any other quality goal.

  * Ask your coding agent to reconcile suggested changes from different test cases that impact the same agent instructions. Instruct it to flag tricky conflicts for human review, so that you can provide nuanced input if needed.
  * Ask your coding agent to create side-by-side diffs of all agent variants for the changes made. This helps understand and validate the fixes it chose.
  * Iterate as needed. The specific nature of these iterations will depend on your CX Agent Studio agent design, coding agent design, model used, and conversation framing.
  * Make sure that the coding agent results are accurate by manually validating actual transcript and result samples.
  * Instruct your coding agent to find missing scenarios from the hillclimbing exercise and suggest new cases if applicable. Continue iterations as needed.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
