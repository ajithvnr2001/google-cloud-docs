---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter/
title: Email adapter \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:50.521365+00:00
---

# Email adapter  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-adapter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Email adapter Stay organized with collections  Save and categorize content based on your preferences. 

The email adapter lets you manage your email communications with end-users. It can be integrated with Contact Center AI Platform (CCAI Platform), your CRM, custom third-party applications, and hybrid mobile applications. Your administrator must [configure the email channel](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config) before you can use the email adapter.

## Email navigation view

When you open the email adapter, the email navigation view appears. This view consists of a navigation menu and an email list.

To see the email navigation view, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears in the email navigation view. The **Assigned** mailbox is selected, and the emails assigned to you appear in the email list.

  2. Optional: To view the queues that you're assigned to, do the following:

     1. Click chevron_right**Expand** next to ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The queues that you are assigned to appear.

     2. Click a queue. A list of email sessions that are assigned to the queue appears. For more information, see Email lists.




### Navigation menu

The navigation menu contains the **Assigned** , **Closed** , **Drafts** mailboxes. The **Assigned** and **Closed** mailboxes contain the queues that you're assigned to. Click a mailbox or a queue to display its contents. The following list shows the contents of the mailboxes and queues:

  * ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned** : the emails assigned to you

  * ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned >** folder **QUEUE_NAME** : the queues that you're assigned to

  * ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/closed-email.png)**Closed** : the emails that you've closed in the last 60 days

  * ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/closed-email.png)**Closed >** folder **QUEUE_NAME** : the closed emails in queues that you're assigned to

  * ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/draft-email.png)**Drafts** : your draft emails




### Email lists

An email list displays the emails in the mailbox or queue that you select in the navigation menu. Emails older than 36 months don't appear.

Emails in an email list display the following:

  * **The sender** : Draft emails don't have a sender. Instead, they show **(No name)**.

  * **The email subject** : Hold the pointer over the email subject to see more information about the queue.

  * **An assigned agent tag** : A round tag with an agent's initials that indicates the assigned agent. Hold the pointer over the tag to view the agent's full name. Unassigned emails and drafts have no assigned agent tag.

  * **A last-updated date** : The date that the email session was last updated. Emails in the **Closed** mailbox don't contain this date.




To sort an email list by date, do one of the following:

  * To sort oldest to newest, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-oldest-to-newest.png)**Oldest to newest**.

  * To sort newest to oldest, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-newest-to-oldest.png)**Newest to oldest**.




To filter an email list by date, follow these steps:

  1. Click the **Filter by Date** list. A list of filters appears.

  2. Click one of the following filters:

     * **Today**. Shows only emails received today.

     * **Yesterday**. Shows only emails received yesterday.

     * **This Week**. Shows only emails received this week.

     * **Last Week**. Shows only emails received last week.

     * **Custom Range**. The **Custom range** dialog appears. Set a beginning and end date, and then click **Apply**. Shows only emails received within the date range, inclusive.




## Start a new email session

You can start a new email session with an end-user in the email adapter.

To start a new email session, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Click **Compose**. The **New email** pane appears.

  3. To specify the email recipients, do the following:

     1. In the **To** field, enter an email address, and then press **Enter**. The email address appears in the field.

     2. Optional: Repeat this step to add more email addresses.

     3. Optional: Click **Cc** , **Bcc** , or both, to add these fields to the email.

  4. In the **Subject** field, enter the email subject.

  5. Click the **Queue** field. One or more queues appear.

  6. Click the queue that you want to assign this email to. If the queue you select is [configured for an email signature](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-email-signature-for-queue), the ink_pen **Insert signature** button appears in the formatting toolbar.

  7. In the editing field, write your email. Use the formatting bar to format your email.

  8. To attach a file, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-attach-file.png)**Attach file** and navigate to a file to attach to the email. You can attach up to 10 files. The combined size of all attached files can't exceed 25 MB. For information about the file types that you can attach, see Allowed file types.

  9. To insert an image, click  image  **Insert image** and navigate to an image that you want to insert into the message. You can insert up to 10 images. The combined size of all inserted images can't exceed 25 MB. To resize an image, click it and drag a corner. For information about the image file types that you can insert, see Allowed file types.

  10. To insert a signature, click ink_pen **Insert signature**. This button appears only if the queue you selected in step 6 is [configured for an email signature](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#configure-email-signature-for-queue).

  11. To assign this email session to a user, do the following:

     1. Click the **Assign to** field. A list appears that contains the users from the queue that you assigned this email session to.

     2. Click the user that you want to assign this email session to.

  12. Click **Send**.


**Note:** If you click close **Close** before sending your email, a draft is saved. If you click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/discard-email.png)**Discard** before sending your email, you're given the option to permanently delete this draft.

## Reply in an email session

You can reply in an email session using the email adapter.

To reply in an email session, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Do one of the following:

     * To select an email session that you are assigned to, do the following:

       1. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. A list of emails that are assigned to you appears. For more information, see Email lists.

       2. Click the email that you want to respond to. The email session appears.

     * To select an email session from a queue, do the following:

       1. Click chevron_right**Expand** next to ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The queues that you are assigned to appear.

       2. Click a queue. A list of email sessions that are assigned to the queue appears. For more information, see Email lists.

       3. Click the email session that you want to respond to. The email session appears.

  3. Click **Reply** or **Reply all** to respond to the latest message. To respond to a different message in the session, click that message.

  4. In the editing field that appears, write your email response. Use the formatting bar to format your email.

  5. Optional: Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-attach-file.png)**Attach file** and navigate to a file that you want to attach to the email. You can attach up to 10 files. The combined size of all attached files can't exceed 25 MB. For information about the file types that you can attach, see Allowed file types.

  6. Optional: Click  image  **Insert image** and navigate to an image that you want to insert into the message. You can insert up to 10 images. The combined size of all inserted images can't exceed 25 MB. To resize an image, click it and drag a corner. For information about the image file types that you can insert, see Allowed file types.

  7. Click **Send**. If your administrator configured the email channel to [append the session ID to email subject lines](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#append-session-id-to-email-subject-lines), the session ID is appended to the subject line.




## Edit the subject line in an email

You can edit the subject line when replying to an email. This lets you add important information to the subject line, such as the ticket numbers or case IDs, for improved tracking and organization. For more information, see [Let agents edit the subject lines in emails](https://docs.cloud.google.com/contact-center/ccai-platform/docs/email-channel-config#let-agents-edit-subject-lines).

To edit the subject line in an email, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Click an email to open it.

  3. Click **Reply** or **Reply all**.

  4. Click edit **Edit Subject**. The subject line becomes editable.

  5. Edit the subject line, and then click away from it to save your edit.




## Finish a draft email

You can finish an email that you left in a draft state using the email adapter.

To finish a draft email, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/draft-email.png)**Drafts**. A list of your draft emails appears. For more information, see Email lists.

  3. Click the draft email that you want to finish. The draft email appears.

  4. Finish your email and send it.




## Transfer an email session from one queue to another

If configured by your administrator, you can transfer an email session from one queue to another. For more information, see [Transfer email sessions to a queue](https://docs.cloud.google.com/contact-center/ccai-platform/docs/let-agents-transfer-email-sessions-to-a-queue).

To transfer an email session to a different queue, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Click chevron_right**Expand** next to ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The queues that you are assigned to appear.

  3. Click a queue. A list of email sessions that are assigned to the queue appears. For more information, see Email lists.

  4. Click an email to transfer to a different queue.

  5. Click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/icon-transfer.png)**Transfer**. A list of queues appears.

  6. Click the queue that you want to transfer your session to. The **Transfer email** dialog appears.

  7. Click **Transfer**.




If the transfer is successful, the following happens:

  * The session is removed from the source queue and added to the destination queue

  * In the destination queue, the transferred session appears as an incoming email and has a **Transferred** tag.

  * The session ID and linked CRM ticket for the session remain unchanged.

  * The session metadata and linked CRM ticket are updated with information about the session transfer.

  * The system sends an email to the end-user indicating that their email session was transferred.




If the transfer fails, the following happens:

  * An error message displays in the email adapter.

  * The email remains in the source queue.

  * A **Transfer failed** tag is added to the email. This tag remains until one of the following happens:

    * You attempt to transfer the email again.

    * You reply to the email.

    * You assign the email to another agent.

    * You resolve the email.




## Forward an email

To forward an email, follow these steps:

  1. In the email adapter, open the email that you want to forward.

  2. Click **Forward**. A forwarding pane appears. If the original email contains attachments, the forwarded email includes those attachments. You can optionally delete the attachments before forwarding the email.

  3. To specify the email recipients, do the following:

     1. In the **To** field, enter an email address, and then press **Enter**. The email address resolves in the field.

     2. Optional: Repeat this step to add more email addresses.

     3. Optional: Click **Cc** , **Bcc** , or both, to add these fields to the email.

  4. Click **Send**.




## Assign emails to another agent

You can assign one or more emails to another agent.

To assign emails to another agent, follow these steps:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter appears.

  2. Do one of the following:

     * To assign emails that you are assigned to, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The emails that are assigned to you appear.

     * To assign emails from a queue, do the following:

       1. Click chevron_right**Expand** next to ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The queues that you are assigned to appear.

       2. Click a queue. A list of email sessions that are assigned to the queue appears. For more information, see Email lists.

  3. Select one or more emails to assign.

  4. Click the **Assign to** field. A list of agents appears.

  5. Select the agent that you want to assign the emails to.




## Close an email session

You can close an email session that requires no further action. The closed status is visible in reports.

To close an email session:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter opens.

  2. Do one of the following:

     * To close an email session that you are assigned to, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. The emails that are assigned to you appear.

     * To close an email session from a queue:

       1. Click chevron_right![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned**. Your assigned queues appear.

       2. Click a queue. A list of email sessions that are assigned to the queue appears. For more information, see Email lists.

  3. Select an email session to close.

  4. Click **Active**. The **Paused** and **Resolved** buttons become visible.

  5. Click **Resolved**. The email session changes to the resolved state.

  6. Click **Resolved**. The **Closed** button becomes visible.

  7. Click **Closed**. The email session changes to the closed state. The email session is visible in the ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/closed-email.png)**Closed** folder, and remains there for 60 days.




## Search for emails

You can search for emails across all search categories, or you can configure your search to target specific categories.

### Search categories

The email search categories are:

  * **Session ID** : the email session ID

  * **Subject** : the email subject

  * **Email Address** : the end-user's email address. This is available only if you retain end-users' email addresses and names.

  * **Name** : the end-user's name. This is available only if you retain end-users' email addresses and names.




### Retain end-users' email addresses and names

To search for emails by email address and name, your instance must be configured to retain end-users' email addresses and names. Contact Google Support to configure your instance to retain this data.

### Search for emails across all search categories

To search for emails across all search categories:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter opens.

  2. To narrow your search, do one of the following:

     * To search for assigned emails, click chevron_right![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned** , and then click a queue.

     * To search for closed emails, click chevron_right![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/closed-email.png)**Closed** , and then click a queue.

     * To search for draft emails, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/draft-email.png)**Drafts**.

  3. In the **Search** field, enter one or more keywords (or keyword phrases in quotation marks) separated by spaces. Keywords and keyword phrases must contain at least three characters.

  4. Press the `Return` key. Emails that match the search criteria appear, with the matched text highlighted. You can open emails or assign them to other agents.




### Search for emails by targeting search categories

To search for emails by targeting specific search categories:

  1. In the CCAI Platform portal, click mail **Email**. The email adapter opens.

  2. To narrow your search, do one of the following:

     * To search for assigned emails, click chevron_right![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/assigned-email.png)**Assigned** , and then click a queue.

     * To search for closed emails, click chevron_right![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/closed-email.png)**Closed** , and then click a queue.

     * To search for draft emails, click ![](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/draft-email.png)**Drafts**.

  3. In the **Search** field, click expand_more **Advanced Search**. The **Keyword** , **Session ID** , and **Subject** fields become visible. If your instance is configured to retain end-users' email addresses and names, the **Email Address** and **Name** fields also become visible.

  4. Do one or more of the following actions:

     * In the **Session ID** field, enter the session ID for an email that you want to search for, and then press the `Tab` key. The session ID becomes a keyword. Repeat to add more keywords. Multiple keywords in this field use OR logic, returning results for any keyword matches.

     * In the **Email Address** field, enter an end-user's email address, and then press the `Tab` key. The email address becomes a keyword. Repeat to add more keywords. Multiple keywords in this field use OR logic, returning results for any keyword matches. Emails that have email addresses in the **From** , **To** , **Cc** , or **Bcc** fields that match a keyword are returned. This field is visible only if your instance is configured to retain end-users' email addresses and names.

     * In the **Subject** field, enter an email subject, and then press the `Tab` key. The email subject becomes a keyword. Repeat to add more keywords. Multiple keywords in this field use OR logic, returning results for any keyword matches. Emails with subjects that match a keyword are returned.

     * In the **Name** field, enter a name, and then press the `Tab` key. The name becomes a keyword. Repeat to add more keywords. Multiple keywords in this field use OR logic, returning results for any keyword matches. Emails that have names in the **From** , **To** , **Cc** , or **Bcc** fields that match a keyword are returned. This field is visible only if your instance is configured to retain end-users' email addresses and names.

**Note:** Searching with multiple search categories uses AND logic, only returning results that match all search categories.
  5. Optional: To search for emails across all search categories, do the following. This procedure is similar to Search for emails across all search categories.

     1. Click **Clear Search**.

     2. In the **Keyword** field, enter a word or a phrase, and then press the `Tab` key. The word or phrase becomes a keyword. Repeat to add more keywords. Multiple keywords in this field use OR logic, returning results for any keyword matches.

  6. Click **Search**. Emails that match the search criteria appear, with the matched text highlighted. You can open emails or assign them to other agents.




## Allowed file types

The following table shows the file types that you can attach to an outbound email.

Image | Video | Audio | Document  
---|---|---|---  
JPEG, JPG, PNG, GIF, TIFF, RAW, WebP | MP4, MOV, AVI, WMV, WebM | MP3, WAV | PDF, DOC, XLS, PPT, CSV, TXT  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
