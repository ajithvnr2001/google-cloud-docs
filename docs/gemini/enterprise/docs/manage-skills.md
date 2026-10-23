---
url: https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills/
title: Manage skills \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:44.109625+00:00
---

# Manage skills  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Manage skills Stay organized with collections  Save and categorize content based on your preferences. 

User-created skills are reusable instructions that help the Gemini Enterprise assistant perform specific tasks.

By default, Gemini Enterprise turns off the skills feature. As a Gemini Enterprise administrator, you can turn on skills, manage skill sharing, and require administrator approval for shared skills.

**Note:** Skills don't have specific location restrictions. Their availability depends on the model selected in the chat conversation. For more information, see [Gemini Enterprise limitations](https://docs.cloud.google.com/gemini/enterprise/docs/locations#product-limitations).

## Supported editions

Whether users can create, upload, or use skills depends on their Gemini Enterprise [edition](https://docs.cloud.google.com/gemini/enterprise/docs/editions):

  * **Standard, Plus, and Pay-as-you-go** : Users can create and upload custom skills, and use Google-managed skills and user-created skills shared with them.
  * **Frontline** : Users can browse, install, and use Google-managed skills and user-created skills shared with them. They can't create or upload custom skills.



## Before you begin

  * To perform administrative tasks related to skills, you must have the [Gemini Enterprise Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/discoveryengine#discoveryengine.agentspaceAdmin) IAM role (`roles/discoveryengine.agentspaceAdmin`).



## Turn on skills and configure sharing

To allow users to create, use, and share skills, you must turn on the feature in the **Feature Management** settings.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to configure.

  3. Click **Configurations** and then click the **Feature Management** tab.

  4. Turn on the following toggles based on your use case:

Toggle | Description  
---|---  
**Enable skills** | Allow users to create and use skills. Users with a Frontline license can use Google-managed skills and user-created skills shared with them, but can't create or upload skills.   
**Enable skill sharing** | Allow users to share skills with other users. To enable this setting, you must turn on **Enable skills**. If you don't also turn on the **Enable skill sharing without admin approval** , administrators must review and approve pending skill share requests.   
**Enable skill sharing without admin approval** | Allow users to share and use skills immediately without requiring administrator review. To enable this setting, you must turn on **Enable skills** and **Enable skill sharing**.  



For more information about feature management, see [Manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).

## View skills

To view the skills created by users, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**. The **Skills** page appears, listing all skills created by users.




## Review share requests

If you have configured skill sharing to require administrator approval, you can review pending share requests on the **Skills** page. Follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, look for skills with a pending sharing status.

  5. Click **Review share request**.

  6. Select the users you want to share the skill with.

  7. Click **Approve** to allow the skill to be shared, or **Deny** to deny the request.




## Suspend a skill

To temporarily suspend a skill created by a user and make it unavailable for use, follow these steps:

**Note:** You can't use administrator controls to suspend Google-managed skills for all end users. But, end users can turn off Google-managed skills they installed if they don't want to use them.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, click _more_vert_ next to the skill you want to suspend.

  5. Enter the reason for suspending the skill.

  6. Click **Suspend**.




The skill status changes to **Suspended**. The skill remains visible in the end-user skill gallery with a **Suspended** label next to its name, but users can no longer invoke it in conversations. The skill owner can update and test the skill.

## Disable a skill

To hide a skill that is shared with users and prevent its use, follow these steps:

**Note:** You can't use administrator controls to disable Google-managed skills for all users. End users can turn off Google-managed skills they installed if they don't want to use them.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, click _more_vert_ next to the skill you want to disable.

  5. Click **Disable**.




Gemini Enterprise hides the skill from the end-user skill gallery.

## Enable a skill

To re-enable a suspended or disabled skill, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, click _more_vert_ next to the suspended or disabled skill.

  5. Click **Enable**. The skill becomes available for use.




## Reject a skill

When you reject a skill that is in the **Disabled** state, Gemini Enterprise returns it to the **Private** state and makes it available only to the skill owner. You must enter a reason for the rejection.

To reject a skill, follow these steps:

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, click _more_vert_ next to the disabled skill you want to reject.

  5. Click **Reject**.

  6. Enter a reason for the rejection.

  7. Click **Confirm**.




## Delete a skill

To permanently delete a user-created skill, follow these steps:

**Note:** You can't delete Google-managed skills.

  1. In the Google Cloud console, go to the Gemini Enterprise page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that has the skill.

  3. Click **Skills**.

  4. On the **Skills** page, click _more_vert_ next to the skill you want to delete.

  5. Click **Delete**.




## Skill states

The following table describes each state that a skill might be in:

State | Description  
---|---  
**Private** | The skill isn't shared with other users and is only available to the skill owner.  
**Suspended** | The skill is temporarily deactivated. The skill remains visible in the end-user gallery with a **Suspended** label next to its name, but users can no longer invoke it in conversations. Skill owners can update and test the skill.  
**Enabled** | The skill is active and available for use on the web app.  
**Disabled** | The skill is inactive and hidden completely from the end user's Skills page. Users can't interact with the skill until you re-enable it. Skill owners can update and test the skill.  
  
## What's next

  * Learn how users [create and manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/skills).
  * Learn more about how to [manage web app features](https://docs.cloud.google.com/gemini/enterprise/docs/manage-web-app-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
