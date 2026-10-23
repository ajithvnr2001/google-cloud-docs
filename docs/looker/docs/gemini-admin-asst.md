---
url: https://docs.cloud.google.com/looker/docs/gemini-admin-asst/
title: Manage Looker roles with the Admin Assistant \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:51.666397+00:00
---

# Manage Looker roles with the Admin Assistant  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/gemini-admin-asst/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Manage Looker roles with the Admin Assistant Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** The Admin Assistant is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, [use this form](https://docs.google.com/forms/d/16LvBDB-ZZ63RjVlo6rmgrt4HsjbUF-yt2KevG8mCeSk/edit) and provide the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



This documentation page describes how to use the Admin Assistant to manage Looker [roles](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles).

The Admin Assistant lets you use natural language and can help you with the following tasks:

  * Learn about your existing configuration with tasks like the following:

    * Searching for roles by name, permission set, or model set
    * Searching for permission sets by name or the permissions that they contain
    * Searching for model sets by name or the models that they contain
    * Listing all available permissions in Looker
    * Listing all available LookML models
  * Create new configurations like these examples:

    * Creating new roles by combining a permission set and a model set
    * Creating new permission sets with a specified list of permissions
    * Creating new model sets with a specified list of models
  * Provide insights and best practices by helping you analyze existing configurations and guide you on best practices for role structuring and permissions management.




[Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker) provides generative AI-powered assistance to help you work with your data.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

To use the Admin Assistant to manage roles, note the following requirements:

  * Gemini in Looker must be enabled for your Looker instance:

    * For Looker (original), the instance must be running Looker 26.14 or later, the instance must be enabled for Gemini in Looker in the **Admin** settings, and the **Trusted Tester features** option must be enabled. For detailed enablement instructions, see the [**Admin** settings — Gemini in Looker](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil) documentation page.
    * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview), the instance must be enabled for Gemini in Looker in the Google Cloud console and the **Trusted Tester features** option must be enabled. For detailed enablement instructions, see the [Administer Gemini on your Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini) documentation page.
  * If you are using Looker (Google Cloud core), you must be using an instance that is not configured for [private connections only](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private_ip_connections).

  * The **Admin Assistant** must be enabled on the [**Gemini in Looker** page](https://docs.cloud.google.com/looker/docs/admin-panel-platform-gil#enable-and-disable-gil-original) in the **Admin** panel.

  * You must be assigned a Looker Admin role.




## Use the Admin Assistant to manage roles

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

Once enabled, the Admin Assistant is available from the **Roles** page in the **Users** section of Looker's **Admin** panel. If the **Admin Assistant** panel is not visible, click the  assistant **Admin Assistant** button to open the **Admin Assistant** panel. The Admin Assistant is also available from the **New Role** and **Edit Role** pages, **New Permission Set** and **Edit Permission Set** pages, and **New Model Set** and **Edit Model Set** pages.

To use the Admin Assistant, enter your questions or instructions into the **Ask a question** field.

## Tips for using the Admin Assistant

Here are some tips for using the Admin Assistant to manage Looker roles:

  * For best results, write your prompts in American English. See the [Gemini for Google Cloud limitations](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai#gemini-limitations) documentation for more information.
  * When creating or editing a role, permission set, or model set that was suggested by the Admin Assistant, always verify the Admin Assistant's suggestions.



## Sample prompts

Here are some examples of tasks that the Admin Assistant can help with.

You can ask the Admin Assistant for information about roles and permissions:

![The Admin Assistant displays a list of permissions required by a LookML developer.](https://docs.cloud.google.com/static/looker/docs/images/admin-asst-list-permissions-2612.png)

You can also get help with creating a new role. The Admin Assistant will prompt you to name the role, whether you want to use existing permission and model sets, or whether you want to create new permission or model sets:

![The Admin Assistant helps create a new Looker role](https://docs.cloud.google.com/static/looker/docs/images/admin-asst-new-role-2612.png)

## Limitations

The Admin assistant is in preview, and the following limitations apply:

  * The number of responses is limited to 100: 
    * In instances where queries yield over 100 records, the preview scope will be restricted to exactly 100 responses.
    * To optimize the user experience, the initial result set will be limited to 25 items; users will then be prompted to load more results if chosen, up to the maximum preview limit of 100.
  * There are limits for both the user interface and the context window: 
    * Only the six most recent conversations will be displayed in the **Admin Assistant** panel.
    * The model will summarize conversation threads after every sixth interaction for storing context.
    * This summarized context must be cleared when a new conversation is initiated.
    * The user query size is limited to 1,000 words.



## Provide feedback

You can provide feedback for the Admin Assistant in the **Admin Assistant** panel. If the Admin Assistant response looks correct, click the thumb_up thumbs-up icon. If the Admin Assistant response looks incorrect or isn't what you expected, click the thumb_down thumbs-down icon.

**Note:** Gemini in Looker is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) and be sure to include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



## Related resources

  * [Learn more about Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview)
  * [Learn more about Gemini in Looker](https://docs.cloud.google.com/looker/docs/gemini-overview-looker)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
