---
url: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent/
title: Schedule chat agent executions \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:59.045053+00:00
---

# Schedule chat agent executions  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/schedule-chat-agent/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Schedule chat agent executions Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your chat agent to execute tasks automatically on a recurring basis. A schedule serves as an automated trigger for the agent's predefined instructions or prompts.

**Note:** Execution schedules are only supported for non-workflow chat agents. **Note:** Scheduled chat agents run automatically for personal tasks, such as creating your own calendar invites or emailing yourself. However, scheduling agents is not supported for actions involving other people.

## Add an execution schedule

### App

To add an execution schedule for your chat agent, do the following:

  1. [Open your agent in edit mode](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent#open-edit-mode).
  2. In the chat agent builder canvas, click the **Schedule** tab.
  3. Click **\+ Add schedule** and configure the recurrence and execution time:

     1. **Repeat frequency:** select how often the agent should run to execute the provided prompt. The following options are available:

        * **Hourly:** runs the task every specified number of hours and at a specific minute within that hour.
        * **Daily:** runs the task once per day at the specified time.
        * **Weekly:** runs the task once per week on the specified day and time.
        * **Monthly:** runs the task once per month on the specified day of the month and time. If a month doesn't have this day, the agent won't trigger. For example, if you enter `30` here, the agent won't trigger in February.
        * **Annually:** runs the task once per year on the specified month, day, and time.
     2. **Execution time and timezone:** define the specific interval settings based on your selected frequency and select the execution timezone.

     3. **Execution time and time zone:** define the specific interval settings based on your selected frequency and select the execution time zone.

     4. **Prompt:** enter the specific prompt (or instruction) the agent will receive at the scheduled time. This defines the task the chat agent will execute.

  4. Click **Save** to create the schedule and add it to your agent in a **Draft** state.

  5. Optional: Test your schedule to verify if it functions as expected.

  6. To activate your schedule and relaunch your chat agent with the updated changes, click **Update**.




## Test the execution schedule

After configuring a schedule, you can immediately test the chat agent's execution to ensure it performs the task as expected without waiting for the next scheduled interval.

### App

To test the execution schedule, do the following:

  1. In the chat agent builder canvas, click the **Schedule** tab.
  2. Find the schedule card that you want to test and click **Run in preview**.

This triggers the chat agent using the saved prompt and configuration.




## Edit an execution schedule

Edit an execution schedule to make changes to the frequency, time, time zone, or prompt.

### App

To edit an existing execution schedule, do the following:

  1. In the chat agent builder canvas, click the **Schedule** tab.
  2. Find the schedule card that you want to test and click **Edit**.
  3. Modify the **Repeat Frequency** , **Run Time** , **Time Zone** , and the **Prompt** as selected.
  4. Click **Save**.
  5. Click **Update** to ensure all changes, including the new schedule, are saved and applied to the chat agent.



## Delete an execution schedule

If a recurring task is no longer needed, you can delete and remove it from the **Agent Schedules** list.

### App

To delete an execution schedule, do the following:

  1. In the chat agent builder canvas, click the **Schedule** tab.
  2. Find the schedule card that you want to test and click **Delete**.
  3. Confirm the deletion to permanently remove the execution schedule for your chat agent.



## Refresh chat agent schedules

Chat agent schedules operate using your user credentials. To ensure data privacy and security, these credentials expire every **14 days**. You must manually refresh your chat agent schedules to ensure they continue to run automatically without interruption.

### App

To refresh schedules for all your chat agents, do the following:

  1. Open your Gemini Enterprise web app and go to the **Agent Gallery** page.
  2. Perform one of the following actions to refresh your schedules:

     * Go to the **Your agents** section and click event_repeat (**Refresh the existing schedules**).
     * [Open the chat agent in edit mode](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent#open-edit-mode) and do the following:

       1. In the chat agent builder canvas, click the **Schedule** tab.
       2. Click **Refresh schedules**.



Your user credentials are refreshed, and all scheduled chat agents will continue to run for another 14-day period.

## View and approve scheduled runs

All scheduled runs, including those waiting for approval, are listed in your chat history.

### App

To view and approve scheduled runs, do the following:

  1. Open your Gemini Enterprise web app and go to the **Chats** section in the navigation menu.
  2. Find and open the conversation thread corresponding to your scheduled chat agent.
  3. If the scheduled run is paused, review the proposed action and click **Approve** to complete the task.



## Limitations

  * You must manually refresh your schedules every 14 days to prevent your scheduled chat agents from failing.
  * A maximum delay of 5 minutes is expected when executing a chat agent schedule.
  * Schedules are only supported in multi-region locations.



## What's next

  * Learn how to [use a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/use-chat-agent).
  * Learn how to [edit a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/edit-chat-agent).
  * Learn how to [share a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/share-chat-agent).
  * Learn how to [delete a chat agent](https://docs.cloud.google.com/gemini/enterprise/docs/workflow-builder/delete-chat-agent).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
