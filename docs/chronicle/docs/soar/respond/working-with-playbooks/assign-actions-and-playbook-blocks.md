---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks/
title: Assign actions and playbook blocks \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:48:34.084121+00:00
---

# Assign actions and playbook blocks  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assign actions and playbook blocks

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

You can assign actions or playbook blocks to a specific user or SOC role in the playbook designer. The assignee decides the outcome of the manual action or playbook block for the playbook run. You can include a message about the action that needs to be taken by the assignee. You can also enable **Time to respond** and add the time they have to complete the action. The timer starts the countdown from when the playbook reaches that part of the flow. 

If they don't respond in the time allotted to complete the action, the action will fail. When you build your playbook, make sure to use **If Step fails** to decide whether to stop the playbook entirely at this stage or skip this step. You can also use the conditional step **If previous Step failed** to push the playbook flow in a different direction. 

For more information on assigning actions to end users, refer to [Assign Approval Links in Actions](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-approval-links-in-actions). 

## Assign an action in a playbook

  1. Double-click the required action in the playbook. 
  2. Select **Manual** from the **Action Type** list. 
  3. Select the user or SOC role from the **Assign To** list. 
  4. Add a message explaining what needs to be done. You have the option to insert a placeholder in your message. This message is displayed to the user in the **Pending Actions** widget in the case overview and in **Your Workdesk**. 
  5. Optionally, enable **Time to respond** and enter the time that the action needs to be completed by.  
If the user doesn't respond in the time selected, you can choose to use the **If Step fails** together with **If previous action fails** in the next playbook conditional step to control the flow. 
  6. Click **Save**. 



After a playbook is triggered, usually following an alert being ingested into the platform, it runs until it gets to the manual action. This action appears in the **Pending Actions** widget in the case overview and in **Your Workdesk**. The user needs to execute or skip the action. 

## Assign playbook blocks

  1. Open the required playbook with an existing block. 
  2. Double-click the playbook block. Note that the block is displayed in green. 
  3. Select **Manual Action** from the **Action Type** list. 
  4. Select the user or SOC role from the **Assign To** list. 
  5. Add a message explaining what needs to be done. You have the option to insert a placeholder in your message. The user will receive a message when their input is required. 
  6. If required, enable the **Time to Save** field and enter the time for the assignee to approve or decline the playbook block. 
  7. Click **Save**. 



After a case has been ingested into the platform and an alert triggers the playbook, it runs until it gets to the manual action. The manual action appears in the **Pending Actions** widget in the case overview and alert overview or on **Your Workdesk**. If the **Time to respond** field has been filled out, then a ticker will appear with the time the user has left to respond to this action. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
