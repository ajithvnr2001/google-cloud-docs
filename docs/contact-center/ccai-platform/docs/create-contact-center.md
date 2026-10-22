---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-contact-center/
title: Configure a sample contact center \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:05.275178+00:00
---

# Configure a sample contact center  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/create-contact-center/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Configure a sample contact center Stay organized with collections  Save and categorize content based on your preferences. 

Follow this quickstart to create a voice-channel contact center using Contact Center AI Platform (CCAI Platform). After completing the quickstart, you'll have a working contact center that can route live calls to billing and support agents. The agents can answer the calls in the CCAI Platform UI.

## Before you begin

  1. Ask your account manager for a demo CCAI Platform instance and provide your project name and ID.

Your account manager will assist you in provisioning a CCAI Platform contact center environment.

  2. After provisioning your environment, verify that you can sign in using the credentials provided.




## Create users and teams

The following procedure shows you how to create user accounts and teams, and add users to those teams.

You can create user accounts for real employees in your organization. Alternatively, you can create test users accounts, as long as you provide valid email addresses for these accounts.

  1. Sign in to the URL for your CCAI Platform contact center as an administrator. For more information, see Before you begin.

  2. Click **Settings > Users & teams**.

If you don't see the Settings menu, click menu **Menu** and click **Settings > Users & Teams**.

  3. Click **\+ Add Users**.

  4. Complete the following fields:

     * **Email** : a valid email address that can receive email

     * **First name** : the user's first name or given name

     * **Last name** : the user's last name or family name

     * **Role:** select **Agent**

  5. Click **Add**.

An invitation to access the environment and set the initial password is emailed to the user by CCAI Platform. If the users don't receive their invitations, ask them to check their email spam folders.

  6. Repeat the preceding step three times to create four users.

  7. Create two teams, one called `Billing Team` and one called `Support Team`. To create a team, follow these steps:

     1. Click **\+ Add a Team**.
     2. Enter the team name, and then click **Add**.
  8. In the **Add Team** display, enter `Support Team`.




You now have two teams, a billing team and a support team.

## Add users to teams

To add users to teams, follow these steps:

  1. In the CCAI Platform portal, go to the **Teams** list, and then click **Billing Team**.

  2. In the right panel, click **\+ Add Agents**.

  3. Select two agents and click **Add**.

  4. In the **Teams** list, click **Support Team**.

  5. In the right panel, click **\+ Add Agents**.

  6. Select two agents, and then click **Add**.




You now have two agents in each of your teams.

## Set up the menu structure for your IVR

To create an Interactive Voice Response (IVR) system, follow these steps:

  1. In the CCAI Platform portal, go to **Settings > Queue**.

  2. Under **IVR (Interactive Voice Response)** , click **Edit/View**.

  3. Next to the **Menu Structure** heading, click the pencil icon.

**Note:** If menu items exist already, you can create a new menu item by clicking an existing menu item and pressing the `Enter` key.
  4. Click **New Item** , enter `Support`, and then press the `Enter` key.

  5. Click **New Item** , enter `Billing`, and then click **Done**.




You now have a menu structure with two items.

## Add agents to menu items for your IVR

To add the two teams to the **Support** and **Billing** menu items so that the agents can receive calls, follow these steps:

  1. Select the **Support** item.

  2. For **Channel Settings** , select **Human Agents**.

  3. Click **Assign Human Agents**.

  4. In the **Cascade Group 1** box, enter `Support Team`.

  5. Click **Save**.

  6. Repeat steps 1-5 for **Billing** , adding the Billing Team as human agents to the **Billing** menu item.

  7. Refresh the page and confirm that the IVR menu items have numbers in the blue boxes. These are the numbered options presented to callers.




You now have teams of agents assigned to receive calls for menu items 1 and 2.

## Test your IVR

To test out your contact center, follow these steps:

  1. Go to **Settings > Call** and record the **Global Outbound Phone Number**.

  2. Sign in to the CCAI Platform portal as one of the support agents that you created in Create users and teams. Follow the instructions sent in the invitation email.

  3. In the call adapter, set the status to **Available**. If prompted, allow microphone access and browser notifications.

  4. On a separate phone line, dial the global outbound number recorded in step 1.

  5. When prompted, press `1` for Support.

  6. As the agent on the Support team, answer the call using the call adapter.

  7. Optional: Repeat steps 2-6 for Billing.




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, you can delete the project.

**Note:** Deleting a project will trigger the deletion of a CCAI Platform instance.**Caution:** Deleting a project has the following effects:

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, when you delete it, you also delete any other work you've done in the project.

  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an **appspot.com** URL, delete selected resources inside the project instead of deleting the whole project.




To delete a project, follow these steps.

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the project list, select the project that you want to delete, and then click **Delete**.

  3. In the dialog, type the project ID, and then click **Shut down** to delete the project.




## What's next

  * To learn about users, see [Add, view, and edit users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user).

  * To learn about queues and menus, see [Queue and menu setup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup).

  * [Getting started for agents](https://docs.cloud.google.com/contact-center/ccai-platform/docs/getting-started-for-agents).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
