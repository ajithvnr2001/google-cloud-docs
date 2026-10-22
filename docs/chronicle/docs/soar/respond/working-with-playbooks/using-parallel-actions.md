---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-parallel-actions/
title: Configure parallel actions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:13.119123+00:00
---

# Configure parallel actions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/using-parallel-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure parallel actions 

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

When you use parallel actions, it speeds up playbook execution by querying multiple products or running long actions at the same time. This reduces the wait time for enrichment information, letting analysts start an investigation sooner. Additionally, grouping parallel actions logically helps organize the playbook. 

Before you begin, consider these guidelines: 

  * You can't put a condition or a block in a parallel action.
  * You can't use actions that have been set to **manual**.
  * The parallel actions in each group run randomly in any order. This means you can't use placeholders of actions in the same group of parallel actions. 
  * You can choose to have individual Skip actions if a step failed for an individual action, within a group of parallel actions. 
  * Double-click the top of a group of parallel actions to change the name to help logically arrange the parallel action boxes in your playbook. 



## Increase the playbook's speed

To speed up the playbook, you can choose to run up to five actions at once. 

### Create a parallel action (option 1)

  1. Drag an action from the **Step** selection on top of another existing action in the playbook. 
  2. Drop it on top of the action. It automatically displays one on top of the other in a Parallel Action container.  




### Create a parallel action (option 2)

  1. Press and hold the **Shift** key to highlight an action. You can highlight up to five actions at a time using **Shift** \+ **click**. Alternatively, you can simultaneously highlight several actions by pressing and holding **Shift** \+ mouse to draw a rectangle around them. 
  2. Right-click any of the actions and choose **Run in Parallel**.  




### Create a parallel action (option 3)

  1. Group two parallel actions together in a box, as you created in the previous two options. 
  2. Right-click a separate action and click **Cut**.
  3. Place your cursor in the **Parallel Action** box and click **Paste** to add the action to the other parallel actions. 



### Delete one or more parallel actions (option 4)

  1. Highlight one of the parallel actions in the box.
  2. Right-click and select **Delete step** to delete the highlighted parallel action, or select **Delete all steps** to delete the entire group of parallel actions. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
