---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/gmail/
title: Integrate Gmail with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:09:55.405125+00:00
---

# Integrate Gmail with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/gmail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Gmail with Google SecOps

This document explains how to integrate Gmail with Google Security Operations.

## Use cases

The **Gmail** integration uses Google SecOps capabilities to support the following use cases:

  * **Automated phishing containment** : Search for and delete malicious emails across the entire organization to prevent user interaction with threat actors.

  * **Forensic email analysis** : Retrieve message headers, attachments, and body content for analysis during an active investigation.

  * **Incident notification** : Automate communication by sending security alerts, investigation updates, or remediation instructions to stakeholders directly from a playbook.

  * **Mailbox management** : List user messages or audit labels to identify patterns in targeted phishing campaigns.




## Before you begin

Before you configure the **Gmail** integration in Google SecOps, complete the following prerequisite steps:

  1. Enable the Gmail API.

  2. Create a service account.

  3. Delegate domain-wide authority to your service account.

  4. Choose and configure one of the following authentication methods:

     * **Option 1:Workload Identity (recommended)**: This method uses short-lived, temporary access tokens through service account impersonation, so you don't need to store secrets.

     * **Option 2:Service account JSON key**: This method relies on a static, long-lived secret key file. Use this method only if Workload Identity authentication isn't available in your environment.




### Enable the Gmail API

You must enable the Gmail API in your Google Cloud organization for the integration to communicate with Google Workspace.

  1. In the Google Cloud console, go to **Library**.

[Go to Library](https://console.cloud.google.com/apis/library)

  2. Search for and enable the **Gmail API**.




### Create a service account

To create a service account for the integration, complete the following steps:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Click **add Create service account**.

  3. Provide a name (such as "SecOps IAM Integration") and description.

  4. Click **Create and continue**. 

  5. Skip the optional role assignment steps and click **Done**.

  6. Locate the service account in the list and copy its client ID (also called the **Unique ID**) and email address. You need these for domain-wide delegation.




### Delegate domain-wide authority

Service accounts don't have their own mailboxes. You must delegate domain-wide authority to the service account so it can impersonate users within your organization.

  1. From your domain's Google Admin console, go to **Main menu > Security > Access and data control > API controls**.

  2. In the **Domain wide delegation** pane, select **Manage Domain Wide Delegation**.

  3. Click **Add new**.

  4. In the **Client ID** field, enter the **Unique ID** (client ID) of the service account you created.

  5. In the **OAuth Scopes** field, enter the following comma-delimited list of scopes:
         
         https://mail.google.com/,
         https://www.googleapis.com/auth/cloud-platform,
         https://www.googleapis.com/auth/admin.directory.user,
         https://www.googleapis.com/auth/admin.directory.group.member,
         https://www.googleapis.com/auth/admin.directory.customer.readonly,
         https://www.googleapis.com/auth/admin.directory.domain.readonly,
         https://www.googleapis.com/auth/admin.directory.group,
         https://www.googleapis.com/auth/admin.directory.orgunit,
         https://www.googleapis.com/auth/admin.directory.user.alias,
         https://www.googleapis.com/auth/admin.directory.rolemanagement.readonly,
         https://www.googleapis.com/auth/apps.groups.settings
         

  6. Click **Authorize**.




### Configure Workload Identity credentials

Choose this method or the JSON key method to authenticate the integration. Using a Workload Identity is the recommended approach because it uses short-lived, temporary access tokens through service account impersonation.

#### Identify the unique instance identity

To authenticate using a Workload Identity, you must grant your Google SecOps instance permission to impersonate your service account. This lets the instance securely access Google Cloud resources.

  1. In Google SecOps, go to **Content Hub > Response Integrations**.

  2. Select the **Gmail** integration, and enter your service account email in `Workload Identity Email`.

  3. Click **Save > Test**. The test is expected to fail. 

  4. Click close_small to the right of **Test** and search the error message for the identity email beginning with `gke-init-python@...` or `soar-python@...`.

  5. Copy this unique email address.




#### Authorize the instance identity in Google Cloud

Once you have retrieved the unique identity for your Google SecOps instance, you must authorize it to access your Google Cloud resources. This step lets the platform impersonate the service account, generate short-lived tokens, and act on your behalf without static keys.

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts**.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select the target service account and go to **Permissions > Grant Access**.

  3. Paste the unique email address into the **New principals** field and assign the **Service Account Token Creator** role (`roles/iam.serviceAccountTokenCreator`).




### Configure a JSON key

Choose this method or the Workload Identity method to authenticate the integration. Use the JSON key method only if Workload Identity isn't available in your environment. Workload Identity is the recommended and more secure approach. This method relies on a static, long-lived secret key file that requires manual management and rotation.

Use the following procedure to generate the JSON key file required to authenticate the integration:

  1. In the Google Cloud console, go to **IAM & Admin > Service Accounts** and select the service account you created.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Go to the **Keys** tab.

  3. Click **Add key > Create new key**.

  4. Select **JSON** as the key type and click **Create**. The browser downloads the JSON file to your computer.

  5. Copy the entire content of this file and paste it into **Service Account JSON File Content** during integration configuration.




## Integration parameters

The **Gmail** integration requires the following parameters:

Parameter | Description  
---|---  
`Default Mailbox` | Required. The primary user email address the integration uses to send or receive messages when no specific mailbox is provided in an action.  
`Service Account JSON File Content` | Optional. The full content of the service account key JSON file. Only use this parameter if you're authenticating using a JSON key.  
`Workload Identity Email` | Optional. The client email address of your service account. Only use this parameter if you're authenticating using a Workload Identity.  
`Verify SSL` | Required. If selected, the integration validates the SSL certificate when connecting to the Gmail server. Enabled by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add Email Label

Use the **Add Email Label** action to add a label to the specified email.

This action is asynchronous. Adjust the action timeout in the Google SecOps integrated development environment (IDE) accordingly.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Add Email Label** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration. This parameter accepts multiple values as a comma-separated list.  
`Internet Message ID` | _Optional_ The internet message ID of an email to search for. This parameter accepts multiple values as a comma-separated string. If you provide the internet message ID, the action ignores the `Subject Filter`, `Sender Filter`, and `Time Frame (minutes)` parameters.  
`Labels Filter` | _Optional_ A filter condition that specifies the email labels to search for.This parameter accepts multiple values as a comma-separated string.The default value is `Inbox`. You can search for emails with specific labels, such as `label1, label2`. To search for emails that don't have the specific label, use the following format: `-label1`. You can configure this parameter to search for emails with and without specific labels in one string, such as `label1, -label2, label3`.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for. This filter uses the `contains` logic and requires you to specify search items in full words. This filter doesn't support partial matches.  
`Sender Filter` | _Optional_ A filter condition that specifies the email sender to search for. This filter uses the `equals` logic.  
`Time Frame (minutes)` | _Optional_ A filter condition that specifies the timeframe in minutes to search for emails.The default value is 60 minutes.  
`Email Status` | _Optional_ A status of the email to search. The possible values are as follows:

  * `Only Unread Messages`
  * `Only Read Messages`
  * `Both Read & Unread Messages`

The default value is `Both Read & Unread Messages`.  
`Label` | _Required_ A label to update the email with.This parameter accepts multiple values as a comma-separated list. If the label doesn't exist in a mailbox, the action creates the label.   
  
#### Action outputs

The **Add Email Label** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Add Email Label** action:
    
    
    [
       {
           "Entity": "email@example.com",
           "EntityResult": [
               {
                   "id": "ID",
                   "thread_id": "THREAD_ID",
                   "label_ids": [
                       "CATEGORY_PERSONAL",
                       "INBOX"
                   ],
                   "snippet": "SNIPPET",
                   "history_id": "10576",
                   "internal_date": 1728217410000,
                   "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
                   "subject": "SUBJECT",
                   "from": "example@example.com",
                   "headers": {
                       "delivered-to": "email@example.com",
                       "received": [
                           "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
                       ],
                       "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
                       "x-received": [
                           "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
                       ],
                       "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
                       "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
                       "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
                   },
                   "mimetype": "text/plain",
                   "text_bodies": [
                       "text\r\n"
                   ],
                   "html_bodies": [],
                   "file_attachments": [],
                   "date": "Sun, 6 Oct 2024 12:23:30 +0000",
                   "to": "email@example.com",
                   "cc": null,
                   "bcc": null,
                   "in-reply-to": null,
                   "reply-to": null
               }
           ]
       }
    ]
    

##### Output messages

The **Add Email Label** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated labels for emails in the following mailboxes: MAILBOX_LIST` `No emails were found based on the provided search criteria in the following mailboxes: MAILBOX_LIST ` `The following mailboxes were not found: MAILBOX_LIST. Check the spelling. ` `Update is pending for emails in the following mailboxes: MAILBOX_LIST` | The action succeeded.  
`Error executing action "Add Email Label". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Add Email Label** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Delete Email

Use the **Delete Email** action to delete one or multiple emails from the mailbox based on the provided search criteria. By default, this action moves emails to Trash. You can configure the action to delete emails forever instead of moving them to Trash.

The **Delete Email** action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Email** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration. This parameter accepts multiple values as a comma-separated string.  
`Labels Filter` | _Optional_ A filter condition that specifies the email labels to search for.This parameter accepts multiple values as a comma-separated string.The default value is `Inbox`. You can search for emails with specific labels, such as `label1, label2`. To search for emails that don't have the specific label, use the following format: `-label1`. You can configure this parameter to search for emails with and without specific labels in one string, such as `label1, -label2, label3`.  
`Internet Message ID` | _Optional_ The internet message ID of an email to search for. This parameter accepts multiple values as a comma-separated string. If you provide the internet message ID, the action ignores the `Subject Filter`, `Sender Filter`, `Labels Filter`, and `Time Frame (minutes)` parameters.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for. This filter uses the `contains` logic and requires you to specify search items in full words. This filter doesn't support partial matches.  
`Sender Filter` | _Optional_ A filter condition that specifies the email sender to search for. This filter uses the `equals` logic.  
`Time Frame (minutes)` | _Optional_ A filter condition that specifies the timeframe in minutes to search for emails.The default value is 60 minutes.  
`Email Status` | _Optional_ A status of the email to search. The possible values are as follows:

  * `Only Unread Messages`
  * `Only Read Messages`
  * `Both Read & Unread Messages`

The default value is `Both Read & Unread Messages`.  
`Move to Trash` | _Optional_ If selected, the action moves emails to **Trash** and doesn't search through emails with the **Trash** label unless you configure the `Labels Filter` parameter to include the following label: `Trash`. If not selected, the action executes a search across the whole mailbox and deletes emails forever. Selected by default.  
  
#### Action outputs

The **Delete Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Delete Email** action:
    
    
    {
    "mailbox1": [DELETED_MESSAGE_ID_LIST],
    "mailbox2": [DELETED_MESSAGE_ID_LIST]
    }
    

##### Output messages

The **Delete Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully deleted emails in the following mailboxes: MAILBOX_LIST` `No emails to delete based on the provided search criteria in the following mailboxes: MAILBOX_LIST ` `The following mailboxes were not found: MAILBOX_LIST. Check the spelling.` `The action didn't find any emails based on the specified search criteria.` `Pending deletion of emails in the following mailboxes: MAILBOX_LIST` | The action succeeded.  
`Error executing action "Delete Email". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Delete Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Forward Email

Use the **Forward Email** action to forward emails, including emails with previous threads.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Forward Email** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to send an email from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration.  
`Internet Message ID` | _Required_ The internet message ID of an email to search for.  
`Send To` | _Required_ A comma-separated string of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.   
`CC` | _Optional_ A comma-separated string of email addresses for the carbon copy (CC) email recipients, such as `user1@example.com, user2@example.com`.  
`BCC` | _Optional_ A comma-separated string of email addresses for the blind carbon copy (BCC) email recipients, such as `user1@example.com, user2@example.com`.  
`Subject` | _Required_ The new subject for an email to forward.  
`Attachments Paths` | _Optional_ A comma-separated string of paths for file attachments that are stored on the Google SecOps server.  
`Mail Content` | _Required_ The body of the email.  
  
#### Action outputs

The **Forward Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Forward Email** action:
    
    
    {
       "id": "ID",
       "thread_id": "THREAD_ID",
       "label_ids": [
           "CATEGORY_PERSONAL",
           "INBOX"
       ],
       "snippet": "SNIPPET",
       "history_id": "10576",
       "internal_date": 1728217410000,
       "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
       "subject": "SUBJECT",
       "from": "example@example.com",
       "headers": {
           "delivered-to": "email@example.com",
           "received": [
               "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
           ],
           "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
           "x-received": [
               "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
           ],
           "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
           "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
           "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
       },
       "mimetype": "text/plain",
       "text_bodies": [
           "text\r\n"
       ],
       "html_bodies": [],
       "file_attachments": [],
       "date": "Sun, 6 Oct 2024 12:23:30 +0000",
       "to": "email@example.com",
       "cc": null,
       "bcc": null,
       "in-reply-to": null,
       "reply-to": null
    }
    

##### Output messages

The **Forward Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully forwarded the  MESSAGE_ID email.` | The action succeeded.  
`Error executing action "Forward Email". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Forward Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test connectivity to Gmail.

This action doesn't run on Google SecOps entities. 

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully connected to the Google Gmail service with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the Google Gmail service! Error is ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove Email Label

Use the **Remove Email Label** action to remove a label from the specified email.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Remove Email Label** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration. This parameter accepts multiple values as a comma-separated list.  
`Internet Message ID` | _Optional_ The internet message ID of an email to search for. This parameter accepts multiple values as a comma-separated string. If you provide the internet message ID, the action ignores the `Subject Filter`, `Sender Filter`, and `Time Frame (minutes)` parameters.  
`Labels Filter` | _Optional_ A filter condition that specifies the email labels to search for.This parameter accepts multiple values as a comma-separated string.The default value is `Inbox`. You can search for emails with specific labels, such as `label1, label2`. To search for emails that don't have the specific label, use the following format: `-label1`. You can configure this parameter to search for emails with and without specific labels in one string, such as `label1, -label2, label3`.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for. This filter uses the `contains` logic and requires you to specify search items in full words. This filter doesn't support partial matches.  
`Sender Filter` | _Optional_ A filter condition that specifies the email sender to search for. This filter uses the `equals` logic.  
`Time Frame (minutes)` | _Optional_ A filter condition that specifies the timeframe in minutes to search for emails.The default value is 60 minutes.  
`Email Status` | _Optional_ A status of the email to search. The possible values are as follows:

  * `Only Unread Messages`
  * `Only Read Messages`
  * `Both Read & Unread Messages`

The default value is `Both Read & Unread Messages`.  
`Label` | _Required_ A label to remove from an email.This parameter accepts multiple values as a comma-separated list. To remove all labels from the email, configure the parameter value as `All`.  
  
#### Action outputs

The **Remove Email Label** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Remove Email Label** action:
    
    
    [
       {
           "Entity": "email@example.com",
           "EntityResult": [
               {
                   "id": "ID",
                   "thread_id": "THREAD_ID",
                   "label_ids": [
                       "CATEGORY_PERSONAL",
                       "INBOX"
                   ],
                   "snippet": "SNIPPET",
                   "history_id": "10576",
                   "internal_date": 1728217410000,
                   "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@mail.gmail.com>",
                   "subject": "SUBJECT",
                   "from": "example@example.com",
                   "headers": {
                       "delivered-to": "email@example.com",
                       "received": [
                           "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
                       ],
                       "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
                       "x-received": [
                           "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
                       ],
                       "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
                       "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
                       "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
                   },
                   "mimetype": "text/plain",
                   "text_bodies": [
                       "text\r\n"
                   ],
                   "html_bodies": [],
                   "file_attachments": [],
                   "date": "Sun, 6 Oct 2024 12:23:30 +0000",
                   "to": "email@example.com",
                   "cc": null,
                   "bcc": null,
                   "in-reply-to": null,
                   "reply-to": null
               }
           ]
       }
    ]
    

##### Output messages

The **Remove Email Label** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully updated labels for EMAIL_NUMBER emails in the MAILBOX_NAME mailbox.` `The following labels don't exist in the MAILBOX_NAME mailbox: LABEL_LIST ` `None of the provided labels exists in the MAILBOX_NAME mailbox.` | The action succeeded.  
`Error executing action "Remove Email Label". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Remove Email Label** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Save Email To The Case

Use the **Save Email To The Case** action to save email or email attachments to the action Case Wall in Google SecOps.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Save Email To The Case** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration.  
`Internet Message ID` | _Required_ The internet message ID of an email to search.  
`Save Only Email Attachments` | _Optional_ If selected, the action saves only attachments from the specified email.Not selected by default.  
`Attachment To Save` | _Optional_ If you selected the `Save Only Email Attachments` parameter, the action only saves attachments that you specify in this parameter.This parameter accepts multiple values as a comma-separated string.  
`Base64 Encode` | _Optional_ If selected, the action encodes the email file into a base64 format.Not selected by default.  
  
#### Action outputs

The **Save Email To The Case** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall attachment

The **Save Email To The Case** action saves emails and attachments as case evidences in Google SecOps.

The following table describes the files that the action saves:

Saved file | Name and format  
---|---  
Email | `EMAIL_SUBJECT.eml`  
`Email attachment` | `ATTACHMENT_NAME. ATTACHMENT_EXTENSION`  
  
##### JSON result

The following example describes the JSON result output received when using the **Save Email To The Case** action:
    
    
    {
       "id": "ID",
       "thread_id": "THREAD_ID",
       "label_ids": [
           "CATEGORY_PERSONAL",
           "INBOX"
       ],
       "snippet": "SNIPPET",
       "history_id": "10576",
       "internal_date": 1728217410000,
       "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
       "subject": "SUBJECT",
       "from": "example@example.com",
       "headers": {
           "delivered-to": "email@example.com",
           "received": [
               "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
           ],
           "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
           "x-received": [
               "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
           ],
           "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
           "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
           "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
       },
       "mimetype": "text/plain",
       "text_bodies": [
           "example\r\n"
       ],
       "html_bodies": [],
       "file_attachments": [],
       "date": "Sun, 6 Oct 2024 12:23:30 +0000",
       "to": "email@example.com",
       "cc": null,
       "bcc": null,
       "in-reply-to": null,
       "reply-to": null
    }
    

##### Output messages

The **Save Email To The Case** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully saved the  INTERNET_MESSAGE_ID email.` `Successfully saved the following attachments from the INTERNET_MESSAGE_ID email: ATTACHMENT_NAMES` `The following attachments were not found in the INTERNET_MESSAGE_ID email: ATTACHMENT_NAMES` | The action succeeded.  
`Error executing action "Save Email To The Case". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Save Email To The Case** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search For Emails

Use the **Search for Emails** action to execute email search in a specified mailbox using the provided search criteria.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search For Emails** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration. This parameter accepts multiple values as a comma-separated list.  
`Labels Filter` | _Optional_ A filter condition that specifies the email labels to search for.This parameter accepts multiple values as a comma-separated string.The default value is `Inbox`. You can search for emails with specific labels, such as `label1, label2`. To search for emails that don't have the specific label, use the following format: `-label1`. You can configure this parameter to search for emails with and without specific labels in one string, such as `label1, -label2, label3`.  
`Internet Message ID` | _Optional_ The internet message ID of an email to search for. This parameter accepts multiple values as a comma-separated string. If you provide the internet message ID, the action ignores the `Subject Filter`, `Sender Filter`, `Labels Filter`, `Recipient Filter`, `Time Frame (minutes)`, and `Email Status` parameters.  
`Subject Filter` | _Optional_ A filter condition that specifies the email subject to search for.  
`Sender Filter` | _Optional_ A filter condition that specifies the email sender to search for.  
`Recipient Filter` | _Optional_ A filter condition that specifies the email recipient to search for.  
`Time Frame (minutes)` | _Optional_ A filter condition that specifies the timeframe in minutes to search for emails.The default value is 60 minutes.  
`Email Status` | _Optional_ A status of the email to search. The possible values are as follows:

  * `Only Unread Messages`
  * `Only Read Messages`
  * `Both Read & Unread Messages`

The default value is `Both Read & Unread Messages`.  
`Headers To Return` | _Optional_ A comma-separated list of headers to return in the action output. The action always returns the following headers: `date`, `from`, `to`, `cc`, `bcc`, `in-reply-to`, `reply-to`, `message-id`, and `subject`.If you don't provide any value, the action returns all headers.This parameter is case-insensitive.  
`Return Email Body` | _Optional_ If selected, the action returns the full body content of an email in the action output. If not selected, the information about the attachment names in the email is unavailable. Not selected by default.  
`Max Emails To Return` | _Optional_ The maximum number of emails for the action to return. The default value is 50.  
  
#### Action outputs

The **Search For Emails** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Search For Emails** action provides the following table:

Table title: **Found Mails**

Columns:

  * **Message_id**
  * **Received Date**
  * **Sender**
  * **Recipients**
  * **Subject**
  * **Email body snippet**
  * **Attachment names**
  * Optional: **Found in mailbox**



##### JSON result

The following example describes the JSON result output received when using the **Search For Emails** action:
    
    
    [
       {
           "Entity": "email@example.com",
           "EntityResult": [
               {
                   "id": "ID",
                   "thread_id": "THREAD_ID",
                   "label_ids": [
                       "CATEGORY_PERSONAL",
                       "INBOX"
                   ],
                   "snippet": "SNIPPET",
                   "history_id": "10576",
                   "internal_date": 1728217410000,
                   "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
                   "subject": "SUBJECT",
                   "from": "example@example.com",
                   "headers": {
                       "delivered-to": "email@example.com",
                       "received": [
                           "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
                       ],
                       "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
                       "x-received": [
                           "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
                       ],
                       "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
                       "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
                       "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
                   },
                   "mimetype": "text/plain",
                   "text_bodies": [
                       "text\r\n"
                   ],
                   "html_bodies": [],
                   "file_attachments": [],
                   "date": "Sun, 6 Oct 2024 12:23:30 +0000",
                   "to": "email@example.com",
                   "cc": null,
                   "bcc": null,
                   "in-reply-to": null,
                   "reply-to": null
               }
           ]
       }
    ]
    

##### Output messages

The **Search For Emails** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully found emails in the following mailboxes: MAILBOX_LIST` `No emails found in the following mailboxes: MAILBOX_LIST` `Pending search for emails in the following mailboxes: MAILBOX_LIST` `The following mailboxes were not found: MAILBOX_LIST. Please check the spelling.` `The action was not able to find any emails based on the specified search criteria.` | The action succeeded.  
`Error executing action "Search For Emails". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Search For Emails** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Email

Use the **Send Email** action to send an email based on the provided parameters.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Send Email** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to send an email from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration.  
`Subject` | _Required_ The subject for an email to send.  
`Send To` | _Required_ A comma-separated string of email addresses for the email recipients, such as `user1@example.com, user2@example.com`.   
`CC` | _Optional_ A comma-separated string of email addresses for the carbon copy (CC) email recipients, such as `user1@example.com, user2@example.com`.  
`BCC` | _Optional_ A comma-separated string of email addresses for the blind carbon copy (BCC) email recipients, such as `user1@example.com, user2@example.com`  
`Attachments Paths` | _Optional_ A comma-separated string of paths for file attachments that are stored on the Google SecOps server.  
`Mail Content` | _Required_ The body of the email.  
`Reply-To Recipients` | _Optional_ A comma-separated list of recipients to use in the **Reply-To** header.Use the **Reply-To** header to redirect reply emails to the specific email address instead of the sender address that is stated in the **From** field.  
  
#### Action outputs

The **Send Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Send Email** action:
    
    
    {
       "id": "ID",
       "thread_id": "THREAD_ID",
       "label_ids": [
           "CATEGORY_PERSONAL",
           "INBOX"
       ],
       "snippet": "SNIPPET",
       "history_id": "10576",
       "internal_date": 1728217410000,
       "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
       "subject": "SUBJECT",
       "from": "example@example.com",
       "headers": {
           "delivered-to": "email@example.com",
           "received": [
               "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
           ],
           "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
           "x-received": [
               "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
           ],
           "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
           "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
           "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
       },
       "mimetype": "text/plain",
       "text_bodies": [
           "example\r\n"
       ],
       "html_bodies": [],
       "file_attachments": [],
       "date": "Sun, 6 Oct 2024 12:23:30 +0000",
       "to": "email@example.com",
       "cc": null,
       "bcc": null,
       "in-reply-to": null,
       "reply-to": null
    }
    

##### Output messages

The **Send Email** action provides the following output messages:

Output message | Message description  
---|---  
`Email was sent successfully.` | The action succeeded.  
`Error executing action "Send Email". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Send Email** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Send Thread Reply

Use the **Send Thread Reply** action to send a message as a reply to the email thread.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Send Thread Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration.  
`Internet Message ID` | _Required_ The internet message ID of an email to search for.  
`Reply To` | _Optional_ A comma-separated list of emails to send the reply to.If you don't provide any value and the `Reply All` checkbox is clear, the action only sends a reply to the original email sender. If you select the `Reply All` parameter, the action ignores this parameter.  
`Reply All` | _Optional_ If selected, the action sends a reply to all recipients related to the original email.This parameter has priority over the `Reply To` parameter.Not selected by default.  
`Attachments Paths` | _Optional_ A comma-separated string of paths for file attachments that are stored on the Google SecOps server.  
`Mail Content` | _Required_ The body of the email.  
  
#### Action outputs

The **Send Thread Reply** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Send Thread Reply** action:
    
    
    {
       "id": "ID",
       "thread_id": "THREAD_ID",
       "label_ids": [
           "CATEGORY_PERSONAL",
           "INBOX"
       ],
       "snippet": "SNIPPET",
       "history_id": "10576",
       "internal_date": 1728217410000,
       "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
       "subject": "SUBJECT",
       "from": "example@example.com",
       "headers": {
           "delivered-to": "email@example.com",
           "received": [
               "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
           ],
           "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
           "x-received": [
               "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
           ],
           "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
           "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
           "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
       },
       "mimetype": "text/plain",
       "text_bodies": [
           "text\r\n"
       ],
       "html_bodies": [],
       "file_attachments": [],
       "date": "Sun, 6 Oct 2024 12:23:30 +0000",
       "to": "email@example.com",
       "cc": null,
       "bcc": null,
       "in-reply-to": null,
       "reply-to": null
    }
    

##### Output messages

The **Send Thread Reply** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully sent a thread reply to the INTERNET_MESSAGE_ID email.` | The action succeeded.  
`Error executing action "Sent Thread Reply". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Send Thread Reply** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Wait For Thread Reply

Use the **Wait For Thread Reply** action to wait for the user reply based on an email sent using the **Send Email** action.

This action is asynchronous. Adjust the action timeout in the Google SecOps IDE accordingly.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Wait For Thread Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Mailbox` | _Required_ A mailbox to wait for a reply from, such as `user@example.com`.By default, the action uses the default mailbox that you configured for the integration. This parameter accepts multiple values as a comma-separated list.  
`Internet Message ID` | _Required_ The internet message ID of an email for the action to wait for. If the message was sent using the **Send Email** action, configure this parameter using the `SendEmail.JSONResult|message_id` placeholder. To retrieve an internet message ID, use the **Search for Emails** action.  
`Wait for All Recipients to Reply` | _Optional_ If selected, the action waits for responses from all recipients until reaching timeout.Not selected by default.  
`Fetch Response Attachments` | _Optional_ If selected and the recipient reply contains attachments, the action retrieves email attachments and adds them as an attachment to the Case Wall in Google SecOps.Not selected by default.  
  
#### Action outputs

The **Wait For Thread Reply** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example describes the JSON result output received when using the **Wait For Thread Reply** action:
    
    
    [
       {
           "Entity": "reply@example.com",
           "EntityResult": [
               {
                   "id": "ID",
                   "thread_id": "THREAD_ID",
                   "label_ids": [
                       "CATEGORY_PERSONAL",
                       "INBOX"
                   ],
                   "snippet": "SNIPPET",
                   "history_id": "10576",
                   "internal_date": 1728217410000,
                   "message_id": "<CAAfJ0RiApRCW7jbTMQdjia+cnzrsWR4UNbB4x94srTZHaEG+Vw@example.com>",
                   "subject": "SUBJECT",
                   "from": "example@example.com",
                   "headers": {
                       "delivered-to": "reply@example.com",
                       "received": [
                           "by 2002:a096512 named unknown by gmailapi.google.com with HTTPREST; Sun, 6 Oct 2024 12:23:30 +0000"
                       ],
                       "x-google-smtp-source": "AGHT+IEq/FCBnUtDRgoabTbX8/z1dIKeKteo3Ic5+sbufKyI22pP1gK1soG9jSmV7dMEQXlIVdRf",
                       "x-received": [
                           "by 2002:a05:620a:0:b0:374:ce15:9995 with SMTP id ffacd0b85a97d-37d0e78253cmr6681102f8f.34.1728217410309; Sun, 06 Oct 2024 05:23:30 -0700 (PDT)"
                       ],
                       "arc-seal": "i=1; aLC/Hhaf3TqCPqGGiSfvDT7bxtQp1lz         c9xg==",
                       "arc-message-signature": "i=1; a=rsa-sha256; c=relaxed/relaxed; d=google.com; s=arc-20240605;        h=to:subject:message-id:datG+AhKivQ7tcf2K8m9B/lexnQw/puC+acDzdYkIqU6         o4ne1qpcJKc32l6V0+ggtGSuHFvp6ySOZkhLJqei9RXBd6HPV3Yj5nVexbhlFuH29w3E         KpGg==;        dara=google.com",
                       "arc-authentication-results": "i=1; mx.google.com;       dkim=pass header.i=@labilfrom=example@example.com;       dara=pass header.i=@example.com",
                   },
                   "mimetype": "text/plain",
                   "text_bodies": [
                       "text\r\n"
                   ],
                   "html_bodies": [],
                   "file_attachments": [],
                   "date": "Sun, 6 Oct 2024 12:23:30 +0000",
                   "to": "reply@example.com",
                   "cc": null,
                   "bcc": null,
                   "in-reply-to": null,
                   "reply-to": null
               }
           ]
       }
    ]
    

##### Output messages

The **Wait For Thread Reply** action provides the following output messages:

Output message | Message description  
---|---  
`Found replies from the following users: USERS` `Waiting for replies from the following users: USERS` | The action succeeded.  
`Error executing action "Wait For Thread Reply". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table describes the values for the script result output when using the **Wait For Thread Reply** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Gmail Connector

Use the **Gmail Connector** to retrieve Gmail emails from a specified mailbox.

The **Gmail Connector** does not ingest emails with a **Scheduled** label for the following reasons:

  * The connector ingests only sent emails. The **Scheduled** label means that emails are only scheduled, not sent.
  * The connector requires timestamps to retrieve emails. Scheduled emails have no timestamps.



#### Connector inputs

The **Gmail Connector** requires the following parameters:

Parameter | Description  
---|---  
`Product Field Name` | _Required_ The name of the field where the product name is stored.The default value is `device_product`.  
`Event Field Name` | _Required_ The field name used to determine the event name (subtype).The default value is `event_name`.  
`Environment Field Name` | _Optional_ The name of the field where the environment name is stored.If the environment field isn't found, the environment is set to `""`.   
`Environment Regex Pattern` | _Optional_ A regular expression pattern to run on the value found in the `Environment Field Name` field. This parameter lets you manipulate the environment field using the regular expression logic. Use the default value `.*` to retrieve the required raw `Environment Field Name` value. If the regular expression pattern is null or empty, or the environment value is null, the final environment result is `""`.  
`Email Exclude Pattern` | _Optional_ A regular expression to exclude specific emails from ingestion, such as spam or news.This parameter works with both the subject and the body of an email. For example, to exclude the auto-reply emails from ingestion, you can configure the following regular expression: `(?i)(auto|no)(\s|-)?re(ply|sponse|sponder)`.  
`Script Timeout (Seconds)` | _Required_ The timeout limit (in seconds) for the Python process running the current script.The default value is 300 seconds.  
`Service Account JSON File Content` | _Optional_ The content of the service account key JSON file. You can configure this parameter or the `Workload Identity Email` parameter.To configure this parameter, provide the full content of the service account key JSON file that you have downloaded when creating a service account.  
`Workload Identity Email` | _Optional_ The client email address of your service account. You can configure this parameter or the `Service Account JSON File Content` parameter.To impersonate service accounts with workloads, grant the `Service Account Token Creator` role to your Google SecOps service account.  
`Disable Overflow` | _Optional_ If selected, the connector ignores the Google SecOps overflow mechanism during alert creation. Not selected by default.  
`Default Mailbox` | _Required_ An email address to use as a default mailbox for the integration, such as `user@example.com`.  
`Labels Filter` | _Optional_ The labels of emails to ingest into Google SecOps.The connector supports nested labels. Provide the labels in a format that is acceptable for Gmail, such as `Inbox-label1-label2`.  
`Email Status` | _Optional_ A status of the email to search.The possible values are as follows:

  * `Both`
  * `Read`
  * `Unread`

The default value is `Both`.  
`Extract Headers` | _Optional_ Header values to filter from the `internetMessageHeaders` list and add to a Google SecOps event.By default, the connector adds all headers to the event. To add only specific headers, enter them as a comma-separated list, such as `DKIM-Siganture, Received, From`. To prevent the connector from adding any header, enter the `None` value.This parameter is case-insensitive.  
`Attached Mail File Prefix` | _Optional_ A prefix to add to the extracted event keys (for example, `to`, `from`, or `subject`) from the attached email file received in the monitored mailbox. The default value is `attach`.  
`Original Received Mail Prefix` | _Optional_ A prefix to add to the extracted event keys (for example, `to`, `from`, or `subject`) from the original email received in the monitored mailbox. The default value is `orig`.  
`Attach Original EML` | _Optional_ If selected, the connector attaches the original email to the case information as an Elements Markup Language (EML) file.Not selected by default.   
`Create Alert Per Attachment File` | _Optional_ If selected, the connector creates multiple alerts, with one alert for every attached email file.This behavior is useful when you process emails with multiple email files attached and set the Google SecOps event mapping to create entities from attached email files.Not selected by default.  
`Max Emails Per Cycle` | _Optional_ The maximum number of emails to retrieve for every connector iteration.The maximum number is 100. The default value is 10.  
`Max Hours Backwards` | _Optional_ A number of hours before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time or the fallback value for an expired connector timestamp.The default value is 24.  
`Case Name Template` | _Optional_ A custom case name.When you configure this parameter, the connector adds a new key called `custom_case_name` to the Google SecOps event. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps event. The connector only handles keys containing the string value. To configure this parameter, specify event fields without prefixes.  
`Alert Name Template` | _Optional_ A custom alert name. You can provide placeholders in the following format: `[name of the field]`. Example: `Phishing - [event_mailbox]`. For placeholders, the connector uses the first Google SecOps SOAR event. The connector only handles keys containing the string value. If you provide no value or an invalid template, the connector uses the default alert name. To configure this parameter, specify event fields without prefixes.  
`Verify SSL` | _Required_ If selected, the integration verifies that the SSL certificate for connecting to Gmail is valid. Selected by default.  
`Proxy Server Address` | _Optional_ The address of the proxy server to use.  
`Proxy Username` | _Optional_ The proxy username to authenticate with.  
`Proxy Password` | _Optional_ The proxy password to authenticate with.  
  
#### Connector rules

The **Gmail Connector** supports the dynamic list.

To filter specific values from the email body and subject, use the dynamic list regular expressions in the following format: `key: regex`, such as `subject: (?<=Subject: ).*`. For example, after finding a match for the `subject: (?<=Subject: ).*` regular expression, the connector creates a Google SecOps alert event and adds a new key with the `subject` name to it. The new key value matches the regular expression.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
