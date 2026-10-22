---
url: https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case/
title: Test cases \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:04.442715+00:00
---

# Test cases  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/concept/test-case/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)



Send feedback 

#  Test cases Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This documentation describes the newest version of this feature as provided by the Conversational Agents console. The documentation for the legacy version of this feature as provided by the Dialogflow CX console is provided below.

You can use the built-in test feature to uncover bugs and prevent regressions. To test your agent, you can use the simulator to interact with your agent and save the conversation as a test case.

When you save a test case, intent matches, playbook actions, activated flows, and activated pages that occurred during the conversation are saved as test case expectations. When you run the test case later after making updates to your agent, these expectations are verified. You can also edit these expectations when creating or editing test cases.

## Create a test case

To create a test case using the simulator:

  1. Open the simulator.
  2. Have a conversation with the agent.
  3. Click the **Create test case** button above the simulator.
  4. The test case editor panel opens. Provide the test case display name and edit any of the expectations as desired.
  5. Click the **Save test case** button above the simulator.



## Run test cases

To run a single test case:

  1. Click **Test Cases** in the left navigation.
  2. Select the test case that you want to run.
  3. Click the **Run** button.
  4. Test case history results are shown.



To run multiple test cases:

  1. Click **Test Cases** in the left navigation.
  2. Selected the test cases that you want to run using the check boxes on the left.
  3. Click **Run selected**.
  4. Latest test run execution results are shown for each test case.



## Edit a test case

When editing a test case, you cannot edit the end-user message or agent response, but you can change the following:

  * Add expectations
  * Delete expectations
  * Update expectations



To edit a test case:

  1. Click **Test Cases** in the left navigation.
  2. Select the test case that you want to edit.
  3. Click the **Edit** button above the test case summary.
  4. You can expand the **Conversation-level expectations** section to edit expectations that apply to the entire conversation.
  5. Each conversational turn shows the end-user message, the agent response, and expectations for the turn. You cannot edit the messages, but you can edit turn-level expectations.



## Delete test cases

To delete test cases:

  1. Click **Test Cases** in the left navigation.
  2. Selected the test cases that you want to delete using the check boxes on the left.
  3. Click **Delete selected test cases**.



## Expectations

When providing expectations for a test case, you can provide _conversation-level expectations_ or _turn-level expectations_.

Conversation-level expectations apply to the entire conversation, and you can provide the following expectation types:

  * Tool use
  * Flow invocation
  * Playbook invocation



Turn-level expectations apply only to a specific conversational turn, and you can provide the following expectation types:

  * Agent response
  * Current flow
  * Current intent
  * Current page
  * Tool use
  * Flow invocation
  * Playbook invocation



## Legacy test cases

You can use the built-in test feature to uncover bugs and prevent regressions. To test your agent, you create test cases using the [simulator](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console#simulator) to define _golden test cases_ , then you execute test cases as needed. A test execution verifies that agent responses have not changed for end-user inputs defined in the test case.

The instructions below show you how to use the console, but you can also find the same functionality in the API.

### Simulator settings

When you first open the simulator, you need to select an [agent environment or flow versions](https://docs.cloud.google.com/dialogflow/cx/docs/concept/version) and an active [flow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/flow). In most cases, you should use the draft environment and default start flow.

You can also enable or disable webhook calls at any time with the webhook toggle button. Disabling webhooks is useful when defining test cases.

### Simulator input

When interacting with the simulator, you provide end-user input as text, then press enter or click the send sendbutton. In addition to plain text, you can choose alternate input types with the input input selector:

  * **Parameter** : Inject a [parameter](https://docs.cloud.google.com/dialogflow/cx/docs/concept/parameter) value. You can provide new parameters or provide preset values for existing parameters.
  * **Event** : Invoke an [event](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#event).
  * **DTMF** : Send dual-tone multi-frequency signaling (Touch-Tone) input for telephony interactions.



### Create a test case

To create a conversation:

  1. Open the [Dialogflow CX console](https://dialogflow.cloud.google.com/cx/projects).
  2. Choose your project.
  3. Select your agent.
  4. Click **Test Agent** to open the simulator.
  5. Chat with the agent to create a conversation that covers the functionality you want to test. For each turn, verify correct values for the triggered intent, the agent response, the active page, and the session parameters.



![Simulator screenshot.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/simulator-test-case.png)

To save a conversation as a test case:

  1. Click the save system_update_altbutton.
  2. Enter a test case display name. Every test case must have a unique display name.
  3. Optionally provide a tag name. Tags help you organize your test cases. All tags must start with a "#".
  4. Optionally provide a note that describes the purpose of the test case.
  5. Optionally select parameters you want to track in the test case. A list of suggested parameters are provided. You can also input other parameters to track. If you select tracking parameters, the parameter assertion is checked when running the test case. See more details on the parameter assertion in the Run test cases section.
  6. Click **Save** to save the test case.



### Run test cases

To view all test cases for an agent, click **Test Cases** in the **Manage** tab. The test cases table shows the test name, the tags, the latest test time and environment, and the latest test result.

To run test cases:

  1. Select the test cases you want to run, and click **Run**. Alternatively, you can click **Run all test cases**.
  2. Select the environment you want to run the test cases against.
  3. The tests start running and you can view the status in the task queue. The test result will be updated when it is completed.



To view the test detail result, click the test case. The **golden test case** and the **latest run** conversations are shown side-by-side.

![Simulator screenshot.](https://docs.cloud.google.com/static/dialogflow/cx/docs/images/simulator-test-case-run-detail.png)

You can click on any agent's conversational turn to see the details for that turn. The test engine checks the following types of data turn by turn to evaluate the test result:

  * **Agent dialogue** :

For each conversational turn, the agent dialogue is compared from golden to latest run. If there is any difference, a warning is displayed. These differences do not prevent a test from passing, because agent dialogue often varies for the same agent state.

  * **Matched intent** :

The matched intent must be the same for each turn for a test to pass.

  * **Current page** :

The active page must be the same for each turn for a test to pass.

  * **Session parameters** :

If you added tracking parameters when you created the test case, the test engine will check the corresponding session parameters and fail the test if there are missing/unexpected parameters or parameter value mismatches.




In some situations, a test case may have an expected failure due to an updated agent. If the conversation in the latest run reflects the expected changes, you can click **Save as golden** to overwrite the _golden test case_.

### Edit test cases

To edit a test case, select the test case from the **Test cases** table, then click the edit edit icon next to the name of the test case. The **Update Test Cases** dialog appears.

To edit the metadata and settings for the test case, click the **Settings** tab.

  1. You can edit the **Test case name** , **Tags** , and **Note** fields, or add new tracking parameters.

  2. Click **Save**.




To edit the user input for the test case, click the **User Input** tab.

  1. Add, remove, or edit the user inputs in JSON format.

  2. Click **Confirm**. An automatic test run begins, and the updated conversation displays after the test run completes.

  3. Click **Save** to overwrite the original golden test case, or click **Save as** to create a new test case with the changes.




### View test coverage

To view a test coverage report for all test cases, click **Coverage**.

The **Coverage** page includes the following tabs:

  * **Transitions** coverage is determined for all [state handlers](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler) (not including route groups) with a transition target exercised by the test case. The source flow/page and transition target flow/page are listed in the table.

  * **Intents** coverage is determined for all [intents](https://docs.cloud.google.com/dialogflow/cx/docs/concept/intent) that are matched by the test case.

  * **Route groups** coverage is determined for all [route groups](https://docs.cloud.google.com/dialogflow/cx/docs/concept/handler#route-group) matched by the test case.




### Import and export test cases

To export test cases:

  1. Select test cases and click **Export** or click **Export all test cases**.
  2. Click **Download to local file** , or provide a Cloud Storage bucket URI and click **Export to Google Cloud Storage**.



When importing test cases, Dialogflow CX always creates new test cases for the target agent and does not overwrite any existing test cases. To import test cases:

  1. Click **Import**.
  2. Choose a local file or provide a Cloud Storage bucket URI.

**Note:** There are references to the agent resources (intents, pages, transitions, etc.) in test cases. Test cases are validated one by one when being imported. Partial success from importing is supported, and any test case with a mismatched resource will fail.

[ Previous arrow_back  Access Transparency  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/access-transparency)

[ Next Experiments  arrow_forward  ](https://docs.cloud.google.com/dialogflow/cx/docs/concept/experiments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
