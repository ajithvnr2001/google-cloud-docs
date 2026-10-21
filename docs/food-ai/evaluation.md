---
url: https://docs.cloud.google.com/food-ai/evaluation/
title: Evaluate ordering agents using the evaluation framework \u00a0|\u00a0 Food Ordering AI Agent \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:21:31.908907+00:00
---

# Evaluate ordering agents using the evaluation framework  |  Food Ordering AI Agent  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/food-ai/evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Food AI ](https://docs.cloud.google.com/food-ai)
  * [ Guides ](https://docs.cloud.google.com/food-ai/concepts)



Send feedback 

#  Evaluate ordering agents using the evaluation framework Stay organized with collections  Save and categorize content based on your preferences. 

This guide explains how to use the evaluation framework in Food Ordering AI Agent to test, validate, and benchmark your AI food ordering agents.

Automated evaluation lets you verify that your ordering agent takes orders accurately, handles complex modifier selections, applies menu rules correctly, and verifies agent behavior.

## Overview of the evaluation framework

The evaluation framework provides automated simulation and verification for food ordering conversations. Rather than manually testing every menu item and conversational edge case, you can define test suites that execute simulated customer sessions against your agent and verify the resulting cart state and dialogue.

During an evaluation run, the framework simulates the customer's side of the conversation using one of two types of test cases:

  * **Predefined conversation turns** : Provide a scripted sequence of customer text inputs for deterministic regression testing. Use this mode to verify that exact customer phrases produce expected agent responses, or to reproduce real customer sessions and escalations from production.
  * **Dynamic instruction-based session simulation** : Provide a high-level natural language ordering instruction (such as ordering specific items, requesting substitutions, or asking about allergens). An LLM customer simulator roleplays the conversation dynamically, testing how your agent handles realistic dialogue, clarifying questions, mid-order changes of mind, and varied customer phrasing.



## Evaluation resource model

The evaluation framework is structured around four primary resources:

  * [`EvaluationDataset`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationdataset): A named collection of evaluation cases representing a test suite, such as a core menu regression suite or breakfast combo tests.
  * [`EvaluationCase`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationcase): An individual test scenario that evaluates an ordering interaction (using either predefined turns or dynamic instructions) against an evaluation context and a set of matchers.
  * [`EvaluationContext`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationcontext): The execution environment for a test case or dataset, including the target store location, active menu, daypart, and simulated session start time.
  * [`EvaluationMatcher`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationmatcher): An assertion rule evaluated at the end of the ordering session that checks specific cart states, utterance text, or semantic criteria.



### Evaluation matchers

An [`EvaluationMatcher`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationmatcher) defines a condition that the agent must satisfy for the test case to pass. An evaluation case can reference multiple matchers, and each matcher produces a boolean pass or fail result:

  * **Order result matcher** : Compares the customer's final cart against an expected [`Order`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#order). The matcher verifies that all items, modifier groups, nested modifiers, and item quantities match after normalization.
  * **Agent utterance string matcher** : Checks whether the agent's responses contain a specific substring or match a regular expression. You can invert the match condition to verify that the agent doesn't say prohibited phrases.
  * **LLM judgement matcher** : Uses an LLM judge to evaluate natural language criteria that can't be validated with exact string matching. For example, you can assert: "The agent confirmed whether the customer wanted cheese before finalizing the order" or "The agent politely informed the customer that milkshakes are unavailable during breakfast."



### Evaluation contexts

An [`EvaluationContext`](https://docs.cloud.google.com/food-ai/reference/rpc/google.cloud.foodorderingaiagent.v1beta#evaluationcontext) configures the restaurant environment in which the evaluation session runs:

  * **Store** : The resource name of the target store (`projects/{project}/locations/{location}/brands/{brand}/stores/{store}`). The store determines the active menu, pricing, time zone, and agent customization overrides.
  * **Menu** : An optional menu resource name to test a candidate menu before associating it with a store in production.
  * **Daypart ID** : An optional daypart ID (such as `breakfast` or `dinner`) to verify menu item availability and pricing rules during specific meal periods.
  * **Test session start time** : An optional ISO timestamp to simulate orders placed at a specific time of day or day of the week.



## Evaluate in the Food Ordering AI Agent console

The [Food Ordering AI Agent console](https://foodai.cloud.google.com) provides an interactive interface for managing evaluation datasets, running tests, and analyzing results.

### 1\. Create an evaluation context

  1. In the Food Ordering AI Agent console, select your project and brand.
  2. In the navigation menu, click **Evaluation**.
  3. Click the **Contexts** tab.
  4. Click **New context**.
  5. Enter a display name and select the target **Store**.
  6. Optional: Select a specific **Menu** or **Daypart** override.
  7. Click **Create**.



### 2\. Create evaluation matchers

  1. In the **Evaluation** page, click the **Matchers** tab.
  2. Click **New matcher**.
  3. Enter a display name and choose the matcher type: 
     * **Order result** : Construct the expected order by selecting items, modifiers, and quantities.
     * **Agent utterance** : Enter the required substring or regular expression pattern.
     * **LLM judgement** : Enter the natural language criteria for the LLM judge.
  4. Click **Create**.



### 3\. Create datasets and import test cases

In the console, test cases can exist on their own or be organized into datasets. You can create datasets directly in the console, but test cases must be imported from YAML files or converted from production sessions.

#### Create a dataset

  1. In the Food Ordering AI Agent console, navigate to **Evaluation** > **Datasets & cases**.
  2. In the **Datasets** pane, click **New dataset**.
  3. Enter a display name (such as `Combo Meals Regression`) and an optional description.
  4. Click **Create**.



You can also click **Import** in the **Datasets** pane to import datasets from a YAML file.

**Warning:** When you import a dataset, the import process automatically creates any new evaluation cases defined in the file and updates existing evaluation cases that have matching resource names.

The following sample YAML file defines an evaluation dataset with inline evaluation cases:
    
    
    - name: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationDatasets/DATASET_ID
      displayName: Core Combo Regression
      description: Core combo ordering and modifier selection regression suite
      evaluationContext: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationContexts/CONTEXT_ID
      evaluationCases:
        - name: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationCases/CASE_ID_1
          displayName: double_cheeseburger_combo
          description: Tests combo meal ordering with side and drink modifier selections
          evaluationContext: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationContexts/CONTEXT_ID
          evaluationMatchers:
            - projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationMatchers/ORDER_MATCHER_ID
          staticTextTurnCase:
            textTurns:
              - userTextInput: "I'd like a double cheeseburger combo."
                exampleAgentResponse: "What drink and side would you like with your combo?"
              - userTextInput: "Onion rings and a large diet cola, please."
                exampleAgentResponse: "Got it, a double cheeseburger combo with onion rings and a large diet cola. Anything else?"
              - userTextInput: "No, that's everything."
                exampleAgentResponse: ''
    

#### Import evaluation cases

  1. In the **Cases** pane, click **Import**.
  2. Select a YAML file defining your evaluation cases.
  3. Confirm the upload. The imported cases appear in the **Cases** list.



You can also click **Export** in either the **Datasets** or **Cases** pane to download existing definitions as YAML files.

The following sample YAML file defines evaluation cases with predefined conversation turns, evaluation contexts, and matchers:
    
    
    - name: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationCases/CASE_ID_1
      displayName: Double Cheeseburger Combo
      description: Tests combo meal ordering with side and drink modifier selections
      evaluationContext: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationContexts/CONTEXT_ID
      evaluationMatchers:
        - projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationMatchers/ORDER_MATCHER_ID
        - projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationMatchers/UTTERANCE_MATCHER_ID
      staticTextTurnCase:
        textTurns:
          - userTextInput: "I'd like a double cheeseburger combo."
            exampleAgentResponse: "What drink and side would you like with your combo?"
          - userTextInput: "Onion rings and a large diet cola, please."
            exampleAgentResponse: "Got it, a double cheeseburger combo with onion rings and a large diet cola. Anything else?"
          - userTextInput: "No, that's everything."
    
    - name: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationCases/CASE_ID_2
      displayName: Breakfast Allergen Inquiry
      description: Tests agent handling of customer allergy questions during breakfast
      evaluationContext: projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationContexts/CONTEXT_ID
      evaluationMatchers:
        - projects/PROJECT_ID/locations/LOCATION/brands/BRAND_ID/evaluationMatchers/LLM_JUDGEMENT_MATCHER_ID
      staticTextTurnCase:
        textTurns:
          - userTextInput: "Are your pancakes prepared with peanut oil?"
          - userTextInput: "Okay, I'll take the oatmeal instead."
    

#### Organize cases into datasets

Evaluation cases can exist independently without belonging to a dataset. To organize cases into a dataset:

  1. In the **Cases** pane, select one or more test cases using their checkboxes.
  2. Drag the selected cases into the target dataset in the **Datasets** pane.
  3. Click the dataset in the **Datasets** pane to expand it and review its assigned cases.



### 4\. Convert customer sessions from Order history

To reproduce customer-reported issues or build test suites directly from real production traffic:

  1. In the navigation menu, click **Order history**.
  2. Click the row for the ordering session that you want to test.
  3. In the **Order details** panel, click **Convert to evaluation case**.
  4. Select or create an evaluation context and matchers.
  5. Click **Convert**. The turn-by-turn customer utterances are converted into an evaluation case automatically.



### 5\. Run evaluations and inspect results

You can run an entire dataset or execute individual selected cases:

  * **Run a dataset** : In the **Datasets** pane, click **Run dataset** next to the target dataset.
  * **Run individual cases** : In the **Cases** pane, select one or more cases using the checkboxes, then click **Run** in the selection actions bar.



To monitor runs and inspect detailed results:

  1. Click the **History** tab to track the run's progress, overall pass rate, and execution duration.
  2. Click any run in the history table to view detailed case results: 
     * **Summary** : Review the overall pass or fail percentage and total cases passed.
     * **Turn transcripts** : Inspect the turn-by-turn dialogue between the simulated customer and the agent.
     * **Matcher details** : Review which matchers passed or failed, including LLM judge explanations for failed qualitative criteria.



## What's next

  * Learn how to [configure store locations and explore menus](https://docs.cloud.google.com/food-ai/console#stores-and-menus).
  * Test ordering interactions interactively with [Agent preview](https://docs.cloud.google.com/food-ai/console#agent-preview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
