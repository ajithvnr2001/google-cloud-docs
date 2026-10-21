---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks/
title: Manage playbook flows \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:13:34.910686+00:00
---

# Manage playbook flows  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-flows-in-playbooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage playbook flows

Supported in: 

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how the **Flow** component directs the next steps of a playbook by using a branching system to make decisions.

Condition flows are essential for allowing a playbook to make decisions—routing a case down different paths based on incoming alert data, previous action results, or user input.

The following flow options are available:

  * **Condition** : Complex conditions based on placeholders, existing case data, and the **Previous Actions** flow.
  * **Multi-Choice Question** : Questions that analysts must answer manually.



## Add Condition flows

This section describes how to use Condition flows to create dynamic, branching logic within your playbooks.

### Add a single Condition flow

To add a single Condition flow, follow these steps:

  1. On the **Response > Playbooks** page, click **Open Step Selection**.
  2. In **Step Selection** , select the **Flow** section.
  3. Drag the condition to the step or between two actions, depending on how you're building your playbook.
  4. Double-click the condition to open the dialog.
  5. Select the required entities. If you are using placeholders, they are scoped to this group of entities.
  6. Decide how many branches you want to create. Each branch has an _OR_ between them.
  7. Select and add parameters for each branch, as follows: 
     1. Select the relevant placeholder you would like to evaluate from the list of existing placeholders. For new users, this is empty if you've not yet ingested any alerts.
     2. Select the required operator: (for example, **Equals to** , **Does not contain**)
     3. Choose a value. 
  8. Define a "fallback branch" to avoid failed conditions. If a condition is based on previous actions, and one of those actions failed (and skipped), the condition continues to the fallback branch, instead of stopping. To select a fallback branch, see Define a fallback branch.
  9. Click **Save**. The playbook creates the branches you defined (up to 19) plus an Else branch (marked as _E_).
  10. Set the outcome for (at least) one branch to mark the playbook as complete.



### Add a multi-choice question flow

  1. Drag the **MultiChoiceQuestion** flow to the required playbook step.
  2. Double-click the box to open the side-drawer.
  3. In the **Parameters** tab, add a question with as many answers as required.
  4. To configure a timeout for the analyst's response: 
     1. Click the **Settings** tab in the side-drawer.
     2. Toggle the **Time to respond** option to `ON`.
     3. Specify the appropriate duration in days, hours, and minutes.
     4. Under the **If Time to Respond exceeded** section, select one of the following actions: 
        * **Stop Playbook:** The playbook execution halts if the user doesn't respond within the defined time.
        * **Select existing branch:** Select one of the already defined answer branches from the menu. The playbook follows this chosen branch if the response time is exceeded.
        * **Create new branch:** This option generates a dedicated branch in the playbook designer to handle the timeout. This lets you define specific actions (for example, send an email to a manager) that are different from the flow's standard answer options. This new branch will appear in the playbook designer, labeled as **Time to respond exceeded**.
  5. Optional: **Approval link:** If this MultiChoiceQuestion is being used to gather approvals from an external source such as email, toggle **Approval link** to `ON`. For more information about setting up and using Approval links, see [Assign an approval link in an action](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-approval-links-in-actions#assign-approval). 
  6. Click **Save**. The playbook opens a branch for each answer provided (up to 20), plus an additional **Time to respond exceeded** branch if configured.
  7. Set the outcome for at least one of the answer branches to mark it as complete.



### Add a Conditions flow

To add a Conditions flow, follow these steps:

  1. Drag the **Conditions** to the **Final Step** box.
  2. Click **Conditions** to open the dialog.
  3. Decide how many branches to create. Each branch has an **OR** between them.
  4. Add a parameter: Select the required parameter. The list shows only the action script results from this playbook.
  5. Select the required operator: **Equals to/Does not equal to** , **Contains/Does not contain** , **Starts with** , or **Greater than/Smaller than**.
  6. Choose the value (the action result).
  7. You can add more parameters to each branch and choose a logical operator: **AND** or **OR**.
  8. Click **Save**. The playbook opens the branches you defined (up to 19) plus an **Else** branch.
  9. Set the outcome for at least one branch to complete the playbook.



### Define a fallback branch

  1. In one of the flows (Condition), select the branch to use as a fallback branch. This example uses **Branch – not risky**. You're not required to add a fallback branch.
  2. When the playbook runs, and the previous actions fail, the playbook chooses the fallback branch and continues.



## Manage step failures

Playbook steps can fail during execution. By default, a playbook is designed to stop if a step fails, which is a crucial safety mechanism to prevent continuing with incomplete or incorrect data. However, there are cases where you want a playbook to continue even if a step doesn't return the expected results. This is especially true for enrichment actions where the data you're looking for might not exist in every case. You can decide whether to stop the playbook or skip to the next step. If the failed step was crucial for decision-making, you can then check if the previous step failed in the next step and decide how to proceed accordingly (for example, if a step fails, go to a fallback branch).

### Skip on failure

For any action, you can configure it to skip the step if it fails. When you enable this setting, the playbook will continue to the next step, even if the action fails to run or returns an error.

To enable this setting, follow these steps:

  1. Double-click the action block to open its settings drawer.
  2. In the **Settings** tab, go to the **If step fails** section.
  3. Select **Skip step**.



### Use a condition for advanced error handling

The "skip if failed" option works well for basic cases, but a more robust method is to use a **Condition** flow to create a dedicated error-handling path. This lets the playbook take a different set of actions when a step fails, such as notifying an analyst or logging the error.

To create an error-handling path, follow these steps:

  1. After an action that might fail, and for which you want to define a specific failure path, add a **Condition** flow block.
  2. Double-click the **Condition** block to open its dialog.
  3. Go to the **Settings** tab, and in the **If previous action fails** section, select which branch to direct the flow to. Important: The **If previous action fails** condition doesn't simply check for any previous failure; it checks if a previous action whose results are being used in the current condition's evaluation has failed. If that dependent action failed, the condition can't be decided, and the flow is directed to the selected branch. This lets you handle cases where a dependency failed, preventing the condition from being resolved.
  4. In this failure branch, you can add actions like sending a notification email, creating a task, or logging the failure.



For example, consider a playbook that attempts to resolve a user's owner. If the **Resolve User Owner** action fails (for example, the user doesn't exist in Active Directory), the playbook won't stop. Instead, the condition block will detect the failure and direct the flow to a separate branch, where it can send an email to the security team about the missing data, ensuring the playbook continues running without interruption. <

### Remove a flow

When removing a flow from within a playbook, the system prompts you to remove the entire branch or just one aspect of it.

### Merge branches

You can merge different branches of the playbook into one branch. To do so, drag an action from one of the branches and drop it to the **Final Step** box of another branch. The playbook can continue after this or end here.

## How logical operators work in a condition

This section clarifies how **Conditional Operators** in playbooks evaluate fields with single or multiple items (for example, Entities or Events in an Alert). Understanding if a field is a **string** or a **list** is crucial for playbook logic.

### The role of data types in Condition evaluation

Operator behavior (`Equals`, `Contains`) varies with data type:

  * **Single-Item Context:** fields like `[Entity.Identifier]` from an alert with one entity are treated as a **single string**.
  * **Multi-Item Context:** the same field from an alert with multiple entities is a **list of strings**.

**Note:** A single item is not always returned; in some cases there may be multiple values.

### Operator behavior of `equals` and `contains`

The following sections discuss how these operators work. 

### `Equals` operator

The `Equals` operator directly compares two values.

  * **Single-item field (string)** checks for an exact match. 
    * _Assuming that`[Entity.Identifier]`_ is `"Tom"`.
    * Then the condition `if [Entity.Identifier] equals "Tom"` is **True**.
  * **Multi-item field (list)** checks if the entire list equals the specified string. A list will **never** equal a single string. 
    * _Assuming that`[Entity.Identifier]`_ is a list `(Tom, Kai)`
    * Then the condition `if [Entity.Identifier] equals "Tom, Kai"` is always **False**. This is because `[Entity.Identifier]` is a list and "Tom, Kai" is a string. 



### `Contains` operator

The `Contains` operator also changes by data type:

  * **Single-item field (string)** performs a **substring search**. Returns `True` if the string contains the value. 
    * _Assuming that`[Entity.Identifier]`_ is `"user-1234"`.
    * Then the condition, `if [Entity.Identifier] contains "user"` is **True**.
  * **Multi-item field (list)** checks for an **exact match** of an item in the list. **No substring search** is performed. 
    * _Assuming that`[Entity.Identifier]`_ is a list (`"UserA@corp.com", "UserB@corp.com"`).
    * Then the condition, `if [Entity.Identifier] contains "corp"` is **False**.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
