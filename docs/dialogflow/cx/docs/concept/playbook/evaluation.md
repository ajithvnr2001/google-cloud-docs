---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation/
title: Playbook evaluations \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:44:16.212426+00:00
---

# Playbook evaluations  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Playbook evaluations Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use the built-in evaluations feature in the Dialogflow CX console to verify your agent's functionality and prevent any regressions after updates. Dialogflow CX provides [out-of-the-box metrics](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation#test_results) to help evaluate your agent's performance.

All metrics except for latency require at least one **test case** , a "golden response" that Dialogflow CX compares the agent's performance against to calculate its performance. Each test case can be measured in the context of an **environment** , which lets you specify different versions of playbooks, flows, and tools to use in the agent's performance evaluation.

## (Optional) Create an environment

Creating an environment is optional. If you don't create one, the default value is **Draft**.

  1. To create an environment, click **Environments** in the left-hand menu and select **\+ Create**.
  2. Choose the versions of the playbooks, flows, and tools that you'd like to use to measure the agent's performance.
  3. Click **Save** to save the environment.



## Create a test case

You have the option of either creating a test case from an existing conversation in your conversation history, creating a new conversation to save as a test case, or importing test cases into Dialogflow CX.

### Create a test case in the console

  1. Navigate to **Conversation history** in the left-hand menu.
  2. To create a new conversation, activate your agent (for example, by calling the agent's phone number) to create a conversation in conversation history. When you have a conversation you'd like to use as a test case, select it.
  3. View the conversation and verify the agent responses, tools invoked, and how each response sounds. When you're satisfied, click **Create test case** in the top right corner of the window.
  4. Provide a display name for the test case and specify your expectations of events that should happen at the conversation-level. This can include tools, playbooks, and flows you expect to be called within the conversation. Click **+Add expectation** to add more expectations. To have the expectations evaluated in sequential order as listed (from top to bottom), toggle **Sequential validation**.
  5. Click **Save** to save your test case.



### Upload test cases

  1. Test cases must be in [the following CSV format](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/evaluation#batch_import_test_cases_formatting). 
  2. To upload test cases to the system, click **Import** at the top of the text cases menu.
  3. In the menu that pops up, either select the locally-stored file or input the path to its Cloud Storage bucket.
  4. Your test cases should now appear in the test cases menu.



## Run a test case

  1. Click **Test cases** in the left-hand menu and select the test case(s) that you want to compare your agent against. This can be a single test case or multiple.
  2. Click **Run selected test cases**. 



## Test results

  1. **Access results** : The latest test run execution results are shown for each test case in _Test Case_ view after completion: 
     1. **Semantic similarity** : Measures how similar the agent's conversations were against the "golden response" (responses in the Test Case). Golden responses are required to receive this metric. Values can be one of 0 (inconsistent), 0.5 (somewhat consistent), or 1 (very consistent). 
     2. **Tool call accuracy** : A value that reflects how faithfully the conversation includes the tools that are expected to be invoked during the conversation. Values range from 0-1. If no tools are used in the conversation, the accuracy will be displayed as `--` (N/A).
     3. **Latency** : The total time that the agent takes to process an end user request and respond to the user (the difference between the end of user utterance and beginning of the agent response). Units are in seconds. 
  2. **Update golden test case** : If the latest run reflects expected changes due to an agent update, you can click "Save as golden" to overwrite the original Test Case.
  3. **Filter and sort results** : You can filter and sort evaluation results by any of the generated metrics or by a specific Environment. This is useful for tracking changes in performance after each update.



## Batch import test cases formatting

This section describes how to format a CSV file for importing batch test cases for your agent. The system reads this file to create a structured set of test cases, each containing one or more conversational turns.

A single test case can span multiple rows in the CSV file. The first row of a test case defines its overall properties (like its name and language). Each subsequent row for that test case defines a single back-and-forth turn in the conversation (user says something, agent is expected to reply).

### Header

The CSV file _must_ have a header row as the very first line. This header defines the data in each column.

#### Required headers

The two required headers must be in the order shown. Both are required for the first row of a new test case. You can start a new test case by providing new `DisplayName` and `LanguageCode` values.

  * `DisplayName`: The name of your test case. This is only filled in for the first row of a new test case.
  * `LanguageCode`: The language code for the test (for example, `en`, `en-US`, `es`).



#### Optional headers

You can include any of the following optional headers to provide more detail for your test cases. They can be in any order after the first two required columns.

**Test case metadata**

  * Tags: Space-separated tags for organizing tests (for example, "payments onboarding").
  * Notes: Free-text notes or a description of the test case purpose.
  * `TestCaseConfigV2.StartResource`: Specify the flow or playbook to start the test with.



**User input**

  * `UserInput.Input.Text`: The text the user "types" for a given turn.
  * `UserInput.InjectedParameters`: Parameters to inject into the conversation at the start of a turn, formatted as a JSON string.



**Agent output**

  * `AgentOutput.QueryResult.ResponseMessages.Text`: The exact text you assert the agent replied with.
  * `AgentOutput.QueryResult.Parameters`: The parameters you assert were extracted by the agent, formatted as a JSON string.



**Expectations**

  * `OrderedExpectations.ExpectedFlow`: The flow you expect to be active after the turn.
  * `OrderedExpectations.ExpectedIntent`: The intent you expect to be matched for the turn.
  * `OrderedExpectations.ExpectedAgentReply`: The text you expect the agent to reply with. Can be a substring of the full reply.
  * `OrderedExpectations.ExpectedOutputParameter`: The parameters you expect to be set at the end of the turn, formatted as a JSON string.



**Audio metadata**

  * `AudioTurnMetadata` Metadata for audio-based tests, formatted as a JSON string.



### Build a test case

Test cases are organized by data rows.

  1. To start a new test case, fill out its metadata row. 
     * **Rule** : This row must have a value in the `DisplayName` column.
     * **Action** : Input values for `DisplayName` and `LanguageCode`. You can also add tags, notes, or a `TestCaseConfigV2.StartResource` in this row. Conversation-turn columns (like `UserInput.Input.Text`) should be left empty in this row. if using tags, separate each tag with a space. Example: `tag1 tag2 tag3`. If using `TestCaseConfigV2.StartResource`, prefix the resource name with `start_flow:` or `start_playbook:`. Example: `start_flow:projects/p/locations/l/agents/a/flows/f`.
  2. Add a conversational turn to the test case you just started by adding a new row immediately below it. 
     * **Rule** : The `DisplayName` column must be empty. This tells the parser that it's a turn belonging to the previous test case.
     * **Action** : Fill in the columns that describe the user's action and the expected agent response for this turn, such as `UserInput.Input.Text` and `OrderedExpectations.ExpectedAgentReply`. For columns requiring JSON, you must provide a valid JSON object as a string. Example: `{"param_name": "param_value", "number_param": 123}`.



[ Previous arrow_back  Playbook best practices  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/playbook/best-practices)

[ Next Data stores  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/data-store)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
