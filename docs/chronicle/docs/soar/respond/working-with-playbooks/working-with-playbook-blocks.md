---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-blocks/
title: Work with playbook blocks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:00.136272+00:00
---

# Work with playbook blocks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/working-with-playbook-blocks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Work with playbook blocks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

_Blocks_ are essentially reusable mini-playbooks that let you implement common workflows and logical decisions across multiple playbooks. This reusability makes maintenance and improvements efficient because any edit or change to a block automatically affects all playbooks that incorporate it.

You can configure input parameter fields in blocks to adjust their internal flow of actions when you use them in other playbooks. Blocks can also return output values to the parent playbook, which supports dynamic interaction and conditional logic within your larger workflows.

## Before you begin

Before you create playbook blocks, we recommend that you take time to map out specific processes you anticipate reusing in parent playbooks. Also, consider the input fields you'll need to configure to make those blocks flexible and adaptable. 

## Add a new block

This example creates a block that manages communication between the SOC and its clients.

To add a new block, do the following:

  1. On the **Playbooks** page, click  add  **Add** , choose the folder and environment, and then click **Create**. We recommend that administrator users click **All Environments**. 
  2. Enter the name of the new playbook block. 
  3. Add input:
     1. Select **Input**.
     2. Click  add  **Add** and enter the input name and value fields. You can add as many fields as you need.
  4. You'll use the following inputs to condition the flow of this block:
     1. **Communication Type** : **Require Approval** (This is one of two defined types; the other is **Investigate**).
     2. **Communication Method** : **Email**.
     3. **Additional Message** : Leave blank.
  5. If you add values to these fields, they'll serve as default settings. While these defaults are established when you configure the block, you can modify them for each individual block instance once it's inserted into a parent playbook. This method supports adaptable and dynamic workflows.



## Configure the flow step for input type

Add a flow step to your block. This step creates different branches, letting the playbook follow a specific path based on the **Input Type** you enter. You'll use placeholders to pick up the **Investigate** and **Requires Approval** input types.

#### Branch 1: Require Approval (default)

This branch handles the **Require Approval** input type and is your default branch.

  1. Configure the **Require Approval** condition to start this branch.
  2. In the **Actions** column, select **Email > Send Email**, and enter the required parameters to send an email. This email typically requests user approval for a security analyst to remediate their machine.
  3. Select **Flow > Condition** and enter the required parameters to confirm whether the customer has approved the request.
  4. Output (Approved Path): In the output step for the _approved_ path of this condition, add **Approved**. This value will be returned to the parent block.
  5. Output (Else Branch - Not Approved): In the output step of the Else branch (where the customer responded negatively to the approval request), add **Not Approved** in the **Output** box.



#### Branch 2: Investigate

This branch defines the actions for the **Investigate** input type.

  1. In the **Actions** column, select **Email > Send Email** and fill in the required parameters. A placeholder is added for the additional message. If you change the **Type** to **Investigate** in the parent playbook, enter a message in the **Input Additional Message** field.  

  2. Select **Siemplify > Assign Case** to assign the case to the customer. This action directs their Tier 1 analyst to review the incident, shifting the initial investigation responsibility to them.  

  3. Select **Siemplify > Change Case Stage**. This step assumes confirmation that the customer is actively investigating, so the case stage is changed to **Investigation**.  

  4. Select **Siemplify > Assign case**. This step assumes that the customer has completed their investigation and has requested the SOC to reclaim ownership of the case.  

  5. Select **Siemplify > Change Case Stage**. This step now changes the case stage from **Investigation** to **Assessment** , letting the SOC resume handling the case.  

  6. In the Output step, add the words **Investigation Completed** to return to the parent playbook. 



This block is now configured with conditional logic and you can insert it into various parent playbooks, adapting its behavior based on the **Communication Type** input. 

### Insert an existing block

To insert an existing block, do the following: 

  1. On the **Playbooks** page, click **Add Step**.  

  2. In the **Step Selection** box, select the **Blocks** section.  

  3. Drag the required block into the center of the playbook. 



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
