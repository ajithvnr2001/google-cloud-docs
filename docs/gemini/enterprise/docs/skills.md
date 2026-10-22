---
url: https://docs.cloud.google.com/gemini/enterprise/docs/skills/
title: Create and manage skills \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:43.284959+00:00
---

# Create and manage skills  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/skills/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Create and manage skills Stay organized with collections  Save and categorize content based on your preferences. 

Skills are reusable custom instructions that help the Gemini Enterprise assistant perform specific tasks, such as reviewing legal contracts or writing in your brand voice.

**Note:** To create skills, your administrator must turn on the skills feature. Similarly, to share skills, your administrator must also enable skill sharing, which they can configure to require administrator review or allow immediate sharing. For more information, see [Manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills).

Each skill is a package containing a `SKILL.md` prompt file. A skill package can also include scripts, files, or background context that the assistant uses to complete a task. By default, Gemini Enterprise turns on skills that you create.

## Supported editions

The ability to create, upload, or use skills depends on the Gemini Enterprise [edition](https://docs.cloud.google.com/gemini/enterprise/docs/editions) that you subscribe to:

  * **Standard, Plus, and Pay-as-you-go** : You can create and upload custom skills, and use Google-managed skills and user-created skills shared with you.
  * **Frontline** : You can browse, install, and use Google-managed skills and user-created skills shared with you. You can't create or upload custom skills.



## Overview

Key aspects of skills include:

  * **Open Standard** : Built on the open skills standard, each skill is defined by a core `SKILL.md` file and can be extended with additional files or scripts.
  * **Modular extension:** Skills let you teach an agent domain-specific tasks using custom instructions and context.
  * **Dynamic access:** Gemini Enterprise accesses these specialized instructions automatically when they are relevant to your question or task.



## Create a skill

**Note:** You can't create skills with the Gemini Enterprise Frontline edition. For more information, see Supported editions.

To create a new skill in the Gemini Enterprise web app, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the add icon and click **Create skill with Gemini**.
  4. Enter a name for your skill.
  5. Enter a description. Gemini Enterprise uses the description to determine whether the skill can help with a prompt or task. You can also add trigger instructions to the description to help guide Gemini Enterprise.
  6. Provide the skill instructions using natural language in the chat box or the **Instructions** field. To create a skill using an existing `SKILL.md` file with custom Markdown or YAML front matter, see Upload a skill.
  7. Click **Save**. Gemini Enterprise turns on the new skill by default.



## Upload a skill

**Note:** You can't upload skills with the Gemini Enterprise Frontline edition. For more information, see Supported editions.

To add existing skills, upload them as Markdown or ZIP files. Gemini Enterprise automatically extracts the skill name and description from the `SKILL.md` file. In the `SKILL.md` file, make sure the description explains when to use the skill.

If you upload a ZIP file containing multiple folders or files, you must include the `SKILL.md` file in the root directory. The ZIP archive can also include optional directories, such as a `scripts/` directory containing Python or Bash code.

To upload a skill, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the add icon and click **Upload skill**.
  4. Drag or browse for the Markdown or ZIP file, and click **Import**. Gemini Enterprise turns on the skill by default.



## Browse skills

You can browse and install skills by using the following sections to filter the list:

Section | Description  
---|---  
**All** | Both Google-managed skills and user-created skills.  
**Google** | Built-in skills provided by Google.  
**Shared with me** | Read-only, user-created skills that other users have shared with you.  
  
To browse and install a skill, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the add icon and click **Browse skills**.
  4. Find the skill you want to use and click **\+ Install**.



## Update a skill

To update an existing skill, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the name of the skill that you want to update.
  4. Click the _more_vert_ icon next to the skill and click **Edit**.
  5. Make the necessary updates to the instructions, name, or description.
  6. Click **Save**.



To return to the Skills page, click _arrow_back_ **Skills**.

## Share a skill

If your Gemini Enterprise administrator enables skill sharing, you can share skills that you create with other users.

**Note:** Sharing a skill doesn't send an email notification. To find the skill, recipients must go to the **Shared with me** section in Browse skills.

To share a skill, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Find the skill you created and want to share.
  4. Click the _more_vert_ icon next to the skill and click **Share**.
  5. In the **Share skill** dialog, enter the comma-separated email addresses of the users you want to share the skill with.
  6. Click **Done**.

**Note:** If your Gemini Enterprise administrator requires approval for share requests, other users can't access the skill until your administrator approves the request.

## Use a skill

You can use skills directly within your chat conversations in the Gemini Enterprise web app.

### Test a skill from the Skills page

You can test a skill directly from the **Skills** page by starting a new chat session with that skill:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the _more_vert_ icon next to the skill and click **New chat**. Gemini Enterprise opens a new chat referencing the selected skill.



### Invoke a skill in a conversation

You can invoke skills dynamically during a conversation to tailor the assistant's responses.

**Note:** You can use skills and agents dynamically, but you cannot invoke both an agent and a skill in the same prompt.

When chatting with the Gemini Enterprise assistant, you can use skills in the following ways:

  * **Manual mentions:** You can explicitly invoke a skill using the `@` or `/` mention feature in the chat box (for example, `@Brand Voice` or `/Brand Voice`). Typing `/` opens a menu displaying only your available skills, while typing `@` opens the general mentions menu.
  * **Direct requests:** If you need Gemini Enterprise to use a specific skill, you can ask for it directly in your prompt. For example, `Use the brand voice skill to review this`.
  * **Automatic selection:** Gemini Enterprise automatically uses a skill when it is relevant to your task based on the skill's description and trigger instructions.



## Turn off a skill

To prevent Gemini Enterprise from using a specific skill, turn it off. When you turn off a skill, Gemini Enterprise doesn't invoke it in conversations.

To turn off a skill, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. On the **Skills** page, find the skill that you want to turn off.
  4. Click the toggle next to the skill to the **Off** position.



## Uninstall a skill

To remove an installed skill from your **Skills** page, follow these steps:

  1. Sign in to the Gemini Enterprise web app.
  2. In the navigation menu, click **Skills**.
  3. Click the _more_vert_ icon next to the skill and click **Uninstall**.

**Note:** **Turning off** a skill pauses automatic triggering but keeps it on your **Skills** page. **Uninstalling** a skill removes it from your **Skills** page, but the skill remains available in **Browse skills** for you to reinstall.

## Skill states

In addition to turning skills on or off yourself, your administrator can change the state of a skill, which affects its availability:

  * **Suspended:** Your administrator temporarily deactivates the skill. It remains visible on the **Skills** page with a suspended status, but other users cannot invoke it in conversations until the administrator re-enables it. Skill owners can update and test the skill.
  * **Disabled:** Your administrator temporarily hides the skill from other users, removing it from their **Skills** page. The skill remains visible to the skill owner, who can update and test it until the administrator re-enables it.
  * **Deleted:** Your administrator permanently removes the skill from the Gemini Enterprise web app, so you can no longer use it.



## Limitations

This section lists the limitations for skills in Gemini Enterprise:

  * Skills are not available for use with agents.
  * Skills support Python and Bash execution only.
  * The web app editor lets you create skills by entering instructions in the form fields or by chatting with the assistant, which automatically generates a single`SKILL.md` file. You must upload more complex skills that require additional scripts or files as a ZIP file.
  * Natural language skill creation does not use your conversation context or connectors as inputs to create a skill.
  * Skills work best with Canvas when a skill has only one `SKILL.md` file.



## What's next

  * Learn how administrators [manage skills](https://docs.cloud.google.com/gemini/enterprise/docs/manage-skills).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
