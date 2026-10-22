---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note/
title: Disposition codes and lists \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:08.992549+00:00
---

# Disposition codes and lists  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/disposition-note/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Disposition codes and lists Stay organized with collections  Save and categorize content based on your preferences. 

Disposition codes are short, predefined labels that an agent uses during wrap-up to classify the outcome of a customer session. Disposition codes can indicate the type of issue that was resolved, the status of the user's request, the end-user's satisfaction level, and much more. Examples include `Issue Resolved`, `Follow-up required`, `Escalated`, `Satisfied`, and `Unsatisfied`. Disposition codes help your organization understand the quality of customer interactions and identify any required follow-up.

You can organize disposition codes into disposition lists for different session types, such as inbound calls, outbound calls, and chats. You can then assign a disposition list as the default list for any of these session types, both at the global and queue level.

To organize a large number of disposition codes, create a hierarchy of disposition lists by adding child lists to existing lists. A child disposition list functions like a folder that you click to display its contents. A child list can contain other child lists. You can create a list hierarchy up to five levels deep including the top-level list. An organized hierarchy of disposition lists guides agents to the appropriate disposition code, simplifying the disposition process.

Disposition data is available for CRM comments, metadata files, and APIs 15 minutes after a session ends.

## Create a disposition code

Disposition codes can be used for wrap-up for inbound calls, outbound calls, and chats, both at the global and queue level.

To create a disposition code, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click **Manage Disposition Codes**. The **Disposition Codes** page appears.

  4. Click the **Codes** tab.

  5. Click **Create disposition code**. The **Create disposition code** dialog appears.

  6. In the **Name** field, enter a name for the disposition code.

  7. Optional: In the **Custom ID** field, enter a custom ID.

  8. Optional: In the **Description** field, enter a description for the disposition code. Google Cloud recommends adding a description if you're using [smart disposition](https://docs.cloud.google.com/contact-center/ccai-platform/docs/smart-disposition).

  9. Click **Add**. Your new disposition code appears.




## Create a disposition list

Disposition lists can be used for wrap-up for inbound calls, outbound calls, and chats, both at the global and queue level.

To create a disposition list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click **Manage Disposition Codes**. The **Disposition Codes** page appears.

  4. On the **Lists** tab, click **Create disposition list**. The **Add list** dialog appears.

  5. In the **Name** field, enter a name for the disposition list.

  6. Optional: In the **Custom ID** field, enter a custom ID.

  7. Click **Add**. Your new disposition list appears.

  8. To add disposition codes to your list, continue with step 4 of Add codes to a disposition list.




## Add codes to a disposition list

Disposition lists can be used for wrap-up for inbound calls, outbound calls, and chats, both at the global and queue level.

To add codes to a disposition list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click **Manage Disposition Codes**. The **Disposition Codes** page appears.

  4. On the **Lists** tab, click the list that you want add codes to.

  5. To add a disposition code, do the following:

     1. Click **Disposition Code > Add disposition code**. The **Add disposition code** dialog appears.

     2. In the **Code** list, select a disposition code that you created in Create a disposition code, and then click **Save**. The code is added to the disposition list.

     3. To add another disposition code, repeat this procedure.

  6. To create and add a disposition code, do the following:

     1. Click **Disposition Code > Create disposition code**. The **Create disposition code** dialog appears.

     2. In the **Name** field, enter a name for the disposition code.

     3. Optional: In the **Custom ID** field, enter a custom ID.

     4. Click **Add**. A code is created and added to the disposition list.

     5. To create and add another disposition code, repeat this procedure.

  7. To add a child disposition list to your list, continue with step 4 of Add a child disposition list to an existing list.




## Add a child disposition list to an existing list

Disposition lists can be used for wrap-up for inbound calls, outbound calls, and chats, both at the global and queue level.

You can add an existing list as a child list to multiple parent lists. This creates a shared child list. Any changes you make to the child list are reflected in all of its parent lists.

The system prevents you from creating loops, such as attempting to add a list into one of the list's own child lists.

To add a child disposition list to an existing list, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click **Manage Disposition Codes**. The **Disposition Codes** pane appears.

  4. On the **Lists** tab, confirm that the **Disposition Lists** pane appears. If it doesn't, click **Disposition lists** in the breadcrumb trail to go to the **Disposition Lists** pane.

  5. For **Disposition Lists** , click the list that you want to add a child list to. The list's contents appear, along with a breadcrumb trail that indicates your position in the list hierarchy. You can click the breadcrumb trail to navigate the list hierarchy.

  6. To add a child disposition list to this list, do the following:

     1. Click **Disposition List > Add disposition list**. The **Add disposition list** dialog appears.

     2. In the **List** list, select a disposition list, and then click **Save**. The child disposition list is added to the list.

     3. To add another child disposition list, repeat this procedure. You can add child lists up to five levels, including the top level.

  7. To create and add a child disposition list to this list, do the following:

     1. Click **Disposition List > Create disposition list**. The **Add list** dialog appears.

     2. In the **Name** field, enter a name for the disposition list.

     3. Optional: In the **Custom ID** field, enter a custom ID.

     4. Click **Add**. Your new disposition list appears.

     5. To create and add another child disposition list, repeat this procedure. You can add child lists up to five levels, including the top level.




## Assign a default disposition list

You can configure which disposition list appears by default in the agent adapter during wrap-up. You can assign the default list for inbound calls, outbound calls, and chats, both at the global and queue level.

To assign a default disposition list, follow these steps:

  1. Do one of the following:

     * To assign a default disposition list at the global level, do the following:

       1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

       2. Go to the **Wrap-up** pane.

     * To assign a default disposition list at the queue level, do the following:

       1. In the CCAI Platform portal, click **Settings > Queue**. If you don't see the **Settings** menu, click menu **Menu**.

       2. In the **IVR (Interactive Voice Response)** , **Mobile** , **Web** or **SMS** pane, click **Edit / View**.

       3. Click the queue that you want to edit.

       4. In the **Settings** pane, go to the **Wrap-up settings** section, and then click **Configure**. The **Wrap-up** pane appears.

  2. In the **Wrap-up** pane, do one of the following. For queue-level settings, the options that appear depend on your channel.

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. In the **Default disposition code list** , select the disposition list that you want to appear in the agent adapter during wrap-up.

  4. Click **Save Wrap-Up** or **Save** , depending whether this is a global or queue-level setting.




## View disposition list hierarchy

You can view the entire hierarchy of your nested disposition lists on a single page.

To view disposition list hierarchy, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Operation Management**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **Wrap-up** pane, do one of the following:

     * Click the **Automatic wrap-up for inbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for outbound calls** toggle to the on position.

     * Click the **Automatic wrap-up for chats** toggle to the on position.

  3. Click **Manage Disposition Codes**. The **Disposition Codes** page appears.

  4. Click the **Tree** tab.

  5. Expand lists to see their contents.




## Agent experience

During wrap-up, the agent adapter displays the **Disposition** pane. This pane contains the contents of the default disposition list that your administrator assigned in Assign a default disposition list. If you don't see the disposition code you need, do one of the following:

  * To search for the code, enter a keyword in the search field and press **Enter**.

  * To manually find the code, do the following:

    1. Click the folder for a child disposition list to display its contents.

    2. If the disposition code you need doesn't appear, click another folder for a child disposition list to display its contents.

    3. Continue until the code you need appears.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
