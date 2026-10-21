---
url: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks/
title: Share notebooks \u00a0|\u00a0 Gemini Notebook Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:39:14.574738+00:00
---

# Share notebooks  |  Gemini Notebook Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/share-notebooks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Gemini Notebook Enterprise ](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)



Send feedback 

#  Share notebooks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to share notebooks between users and also how to revoke notebook sharing.

Sharing notebooks is one of the few user features that differs between Gemini Notebook Enterprise and the other Gemini Notebook products.

**Note:** You can't share notebooks between Gemini Notebook Enterprise and personal Gemini Notebook or Gemini Notebook Plus accounts.

## Who can you share notebooks with?

You can share your notebooks with others if they fulfill the following criteria:

  * They're users in the same project.

  * They've been granted the Cloud NotebookLM User role. For more information, see [Grant Gemini Notebook Enterprise roles to users](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm#grant-roles).

  * They're in the same workforce pool.

  * They have a Gemini Notebook Enterprise or Gemini Enterprise license.




## Sharing permissions

There are two levels of sharing permissions:

  * **Viewer** : Viewers can interact with the notebook but otherwise have limited access. For example, viewers can't upload sources or add notes.

  * **Editor** : Editors have the same permissions as the [notebook owner](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview#user_roles) with the following exceptions. Editors can't:

    * Delete notebooks
    * Share notebooks
    * Revoke access to notebooks



If a user is assigned both the permissions, the highest permission is granted. For example, if a person belongs to one group with editor permissions and another group with view permissions, that person can edit the notebook.

## Autocomplete for user emails and group names

The autocomplete feature for the **Add people and groups** field is a convenience that makes entering email addresses and group names less error prone.

![Add people and groups field in the share notebook dialog.](https://docs.cloud.google.com/static/gemini/enterprise/notebooklm-enterprise/images/share-notebooks-add-people-groups.png)

If you have set up Gemini Notebook Enterprise with the Cloud Identity authentication, then autocomplete is available automatically. (Cloud Identity corresponds to the [**Google identity provider** in the **Identity settings** dropdown](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm#set-id-provider).)

However, if you're using Workforce Identity Federation for authentication, then you must configure Workforce Identity Federation to use extended attributes with System for Cross-domain Identity Management (SCIM). Most likely, you did this when you set up Gemini Notebook Enterprise, see [Set up Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/set-up-notebooklm).

## Limitations related to sharing notebooks

Be aware of the following limitations related to sharing notebooks in Gemini Notebook Enterprise:

  * If your notebook is integrated with Gemini Enterprise and you added sources from Gemini Enterprise search results, then you can't share those notebooks.

  * If a notebook is already shared, you can't add sources to it from Gemini Enterprise.




## Share a notebook with individuals

To share a notebook with people using their email addresses, follow these steps:

  1. Click group **Share**.

  2. Enter comma-separated email addresses and click person_add.

  3. Optional. Clear the **Notify people** checkbox if you don't want the people you add to receive an email telling them that you've shared the notebook.

  4. Set the permissions to **Viewer** or **Editor**.

  5. Click **Send**.

After you've shared the notebook with someone, they'll find the shared notebook at the top of the notebook list on their **My Notebooks** page.




## Share a notebook with a group

You can share a notebook with others using an email distribution group such as a Google group or a Microsoft Entra ID group.

To share a notebook with a group, follow these steps:

  1. Click group **Share**.

  2. In the **Add people and groups** field, type the name of the group that you want to share the notebook with (for example, `my-google-group@example.com`), and click person_add.

**Note:** If you use Microsoft Entra ID as your external identity provider and you have not set up SCIM, you might have to type the group's Object ID (the UUID)— _not_ the Group name in the **Add people and groups** field.
  3. Set the permission to **Viewer** or **Editor**.

  4. Click **Share**.

After you've shared the notebook with a group, each member of the group receives an email with a message saying that you've invited them to edit or view the notebook. A link to the notebook is included in the message. The group member doesn't see the notebook in their **My Notebooks** page until after they've clicked the notebook link in the email.

**Note:** If you've shared using the Object ID (as required with Microsoft Entra ID), an email is not sent. Click **Copy link** in the Share dialog and manually send the link another way.



## Revoke access to a notebook

If you've shared a notebook with someone and you decide that you no longer want that person to have access to the notebook, then you can revoke sharing.

To revoke access to a notebook, follow these steps:

  1. Click group **Share**.

  2. Select **Revoke access** next to the email address of the person.

  3. Click **Send**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
