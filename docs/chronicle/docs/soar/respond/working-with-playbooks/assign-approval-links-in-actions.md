---
url: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-approval-links-in-actions/
title: Assign approval links in actions \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:55.134190+00:00
---

# Assign approval links in actions  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-approval-links-in-actions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Assign approval links in actions

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

Use _Approval links_ to send manual actions waiting for user input (pending actions) to users _outside_ of the platform. For example, if you're working with an end user that doesn't have access to Google Security Operations, you could email them the approval link and (similarly to the **Pending actions** widget or the **Pending Actions** tab in **Your Workdesk**), they can approve or decline the action from wherever they are. 

As a Managed Security Service Provider (MSSP), you want to quarantine an infected computer on your end customer's site but you want the IT manager in the end customer's company to approve this action first. To send out this request to approve or decline the action to the IT Manager in an email, you'll need to assign an approval link in the action.

## Assign an approval link in an action

This use case describes how an MSSP can build a playbook based on a suspicious phishing alert.

  1. In the playbook you're building, select the **Carbon Black Quarantine Device** action. This action is the one you want the end user to approve. 
  2. Change the **Action Type** to **Manual**. The **Approval link** toggle appears. 
  3. Click the **Approval link** toggle to on. This automatically creates placeholders (with links to approve or decline the Quarantine Device) which can then be used in any action _preceding_ this one in the playbook.  
You can assign the manual action to a specific user or SOC role, or leave it blank.
  4. Optionally, you can enable the **Time to respond** toggle in conjunction with the **Approval link** toggle. This will specify a specific time by which the end user must respond to the email by clicking one of the links. 
  5. Drag a **Send Email** action to directly _before_ the **Carbon Black Quarantine Device** action in the playbook.
  6. In the **Send Email** action, fill out the recipient email address.
  7. While in the email body, click  data_array  **Placeholder** and click individual **Approve** and **Decline** links to place them in the message. 
  8. Make sure you've written an email first before you add the placeholders.  
**Pro Tip** : Wrap the sentence in HTML links so that the approval link appears as a hypertext link. 
  9. Save your playbook.



After you save your playbook, an incoming alert that matches the trigger starts the execution. When the flow reaches the **Send Email** step, an email is sent to the recipient containing the **Approve** and **Decline** action links.

These approval links are fully portable; you can use them in various places, such as an **HTML** widget in a custom playbook view, a **Send to Slack** action, or a **Send SMS with Twilio** action.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
