---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email-v2/
title: Integrate EmailV2 with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:14.168282+00:00
---

# Integrate EmailV2 with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Integrate EmailV2 with Google SecOps 

This document explains how to integrate EmailV2 with Google Security Operations (Google SecOps).

**Note:** This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/EmailV2.zip).

## Use cases

The **EmailV2** integration uses the Google SecOps capabilities to support the following use cases:

  * **Phishing triage and notification** : Automate the process of sending notification emails to recipients, including external users, and setting up asynchronous playbooks to wait for user responses (such as confirmation of a phishing attempt).

  * **Incident data enrichment and retention** : Search a mailbox for related messages based on criteria (like sender or subject) and save all file attachments from suspicious emails directly to the case wall for forensic analysis and data retention.

  * **Mailbox management and containment** : Automatically move malicious or triaged emails from the inbox to quarantine or archive folders, or permanently delete emails that match specific filters (such as deleting all copies of a known malware email across multiple folders).

  * **Threaded response and collaboration** : Send an immediate reply or a structured response within an existing email thread using the Send Thread Reply action, ensuring all necessary parties are kept in the loop with relevant security updates.




## Before you begin

To enable the **EmailV2** integration to successfully connect to your mail server, you must ensure the configured mailbox grants access to third-party applications using IMAP/SMTP.

If you are using a Gmail or Google Workspace account, you must use an App password to authenticate. Standard account passwords don't work for IMAP/SMTP connections to Google servers.

To use an app password, ensure the following requirements are met:

  1. **Enable 2-Step Verification** : App passwords can only be generated if 2-Step Verification is enabled on your Google Account. For more details, see [Turn on 2-Step Verification](https://support.google.com/accounts/answer/185839).

  2. **Generate a 16-digit App password** : Create a unique passcode for the integration. For more details, see [Sign in with app passwords](https://support.google.com/accounts/answer/185833).


**Note:** For non-Google mail servers, ensure that IMAP and SMTP access are enabled in your mail provider's settings.

### Network access to IMAP/SMTP

Accessing and processing received email using IMAP and sending outgoing email using SMTP requires network access using the configured account credentials.

#### Network requirements

Function | Default Port | Direction | Protocol  
---|---|---|---  
Mail Server Communication | Multivalues | Outbound | IMAP/SMTP  
  
## Integration parameters

The **EmailV2** integration requires the following parameters:

Parameter | Description  
---|---  
`IMAP - Use SSL` | Optional. If selected, the action enables secure communication (SSL/TLS) when connecting to the IMAP server. Enabled by default.  
`SMTP - Use Authentication` | Optional. If selected, the action enables authentication for the SMTP connection. This is required when the SMTP server isn't in an "open relay" configuration and requires credentials to send outgoing emails. Enabled by default.  
`Sender's Address` | Required. The email address of the mailbox used by the integration for both sending and receiving messages.  
`Sender's Display Name` | Required. The name that appears as the sender when the integration sends emails.  
`SMTP Server Address` | Optional. The DNS hostname or IP address of the SMTP server used for sending emails, such as `smtp.gmail.com`.  
`SMTP Port` | Optional. The port number used to connect to the SMTP server, such as `587` or `465`.  
`IMAP Server Address` | Optional. The DNS hostname or IP address of the IMAP server required to retrieve received emails, such as `imap.gmail.com`.  
`IMAP Port` | Optional. The port number used to connect to the IMAP server, such as `993`.  
`Username` | Required. The username required for authenticating with the mail server (usually the full email address).  
`Password` | Required. The password required for authenticating with the mail server. For Gmail or Google Workspace accounts, you must enter the 16-digit App password generated in your Google account security settings.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Delete Email

Use the **Delete Email** action to remove emails from the mailbox that match specified search criteria. You can utilize this action to either delete the first matching email found or delete all matching emails.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Email** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | Required. A comma-separated list of the mailbox folders where the action searches for emails.  
`Message IDs` | Optional. A comma-separated list of specific Message IDs to search for and delete. If provided, this list overrides the `Subject Filter`, `Sender Filter`, and `Recipient Filter`.  
`Subject Filter` | Optional. A subject line used to narrow the search for matching emails.  
`Sender Filter` | Optional. A sender's address used to search for matching emails.  
`Recipient Filter` | Optional. A recipient's address used to search for matching emails.  
`Days Back` | Optional. The time window (in days) the action searches for emails to delete. The timeframe is calculated with day granularity. Using a value of `0` restricts the search to emails received only within the current day. The default value is `0`.  
`Delete all matching emails` | Optional. If selected, the action deletes all emails that match the specified criteria; otherwise, it only deletes the first match. Disabled by default.  
  
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

The following example shows the JSON result outputs received when using the **Delete Email** action:
    
    
    {
        "deleted_emails": {
            "email_1_deleted": {
                "message_id": "<a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0@mail.example.com>",
                "deleted_from_folder": "Inbox",
                "subject": "Suspicious Login Alert - Deleted",
                "sender": "noreply@system.com",
                "timestamp": "2025-11-20T14:30:00Z"
            },
            "email_2_deleted": {
                "message_id": "<u1v2w3x4y5z6a7b8c9d0e1f2g3h4i5j6k7l8m9n0@mail.example.com>",
                "deleted_from_folder": "Spam",
                "subject": "Phishing Offer",
                "sender": "scam@badsite.net",
                "timestamp": "2025-11-15T09:15:00Z"
            }
        }
    }
    

##### Output messages

The **Delete Email** action can return the following output messages:

Output message | Message description  
---|---  
`NUMBER_OF_DELETED_EMAILS email(s) were deleted successfully` `Failed to find emails for deletion!` | The action succeeded.  
`Error deleting emails ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### DownloadEmailAttachments

Use the **Download Email Attachments** action to retrieve attachments from specific emails and save them to a designated path on the Google SecOps server.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Download Email Attachments** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | Required. A comma-separated list of the mailbox folders where the action searches for the email. The default value is `Inbox`.  
`Download Path` | Required. The path on the Google SecOps server where the downloaded attachments are saved.  
`Message IDs` | Optional. A comma-separated list of message IDs from which to download attachments.  
`Subject filter` | Optional. A subject line used to narrow the search for the email.  
  
#### Action outputs

The **Download Email Attachments** action provides the following outputs:

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

The **Download Email Attachments** action can return the following output messages:

Output message | Message description  
---|---  
`Downloaded NUMBER_OF_ATTACHMENTS attachments. ATTACHMENT_PATHS` | The action succeeded.  
`failed to download email attachments, the error is: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Download Email Attachments** action:

Script result name | Value  
---|---  
`attachments_local_paths` | A string of comma-separated full paths to the saved attachments.  
  
### Forward Email

Use the **Forward Email** action to send an existing email, including its previous thread content, to new recipients by providing the original email's unique Message ID.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Forward Email** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | Required. The mailbox folders where the original email is located.

  * Provide a comma-separated list if checking multiple folders.
  * The folder name must match the IMAP folder exactly.
  * If the folder name contains spaces, it must be wrapped in double quotes.

The default value is `Inbox`.  
`Message ID of the email to forward` | Required. The unique `message_id` of the existing email that the action forwards.  
`Recipients` | Required. A comma-separated list of the primary email addresses for the new recipients.  
`CC` | Optional. A comma-separated list of email addresses to include in the CC field.  
`BCC` | Optional. A comma-separated list of email addresses to include in the BCC field.  
`Subject` | Required. The subject line for the forwarded email.  
`Content` | Optional. Additional body content to include in the forwarded email.  
`Return message id for the forwarded email` | Optional. If selected, the action returns the unique Message ID of the newly forwarded email in the JSON result. Disabled by default.  
`Attachment Paths` | Optional. A comma-separated list of file paths on the server for additional attachments.  
  
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

The following example shows the JSON result outputs received when using the **Forward Email** action:
    
    
    {
       "Date"
       "message_id"
       "Recipient"
    }
    

##### Output messages

The **Forward Email** action can return the following output messages:

Output message | Message description  
---|---  
`Email was forwarded successfully.` `Mail was forwarded successfully. Mail message ID is: MESSAGE_ID` | The action succeeded.  
`Failed to forward the email! The Error is ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Forward Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Move Email to Folder

Use the **Move Email to Folder** action to transfer emails from a specified source folder to a different destination folder within the mailbox.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Move Email to Folder** action requires the following parameters:

Parameter | Description  
---|---  
`Source Folder Name` | Required. The name of the source folder from which the emails are moved.  
`Destination Folder Name` | Required. The name of the destination folder where the emails are moved.  
`Message IDs` | Optional. A comma-separated list of specific Message IDs to search for and move. If provided, this list overrides `Subject Filter`.  
`Subject Filter` | Optional. A subject line used to narrow the search for matching emails.  
`Only Unread` | Optional. If selected, the search restricts results to only unread emails. Disabled by default.  
  
#### Action outputs

The **Move Email to Folder** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Move Email to Folder** action:
    
    
    {
        "emails": {
            "email_1": {
                "message_id": "<4f1e50e8f4027d187a2385a39b83cde46e5b53c1@mail.example.com>",
                "received": "Mon, 24 Nov 2025 10:00:00 +0000",
                "sender": "security-alert@example.com",
                "recipients": "user@example.com",
                "subject": "Phishing Alert: Urgent Action Required",
                "plaintext_body": "Original alert content...",
                "moved_from_folder": "Inbox",
                "moved_to_folder": "Quarantine"
            },
            "email_2": {
                "message_id": "<a5b6c7d8e9f01g2h3i4j5k6l7m8n9o0p1q2r3s4t@mail.example.com>",
                "received": "Sun, 23 Nov 2025 14:30:00 +0000",
                "sender": "noreply@system.com",
                "recipients": "user@example.com",
                "subject": "System Update Notification",
                "plaintext_body": "System update successful...",
                "moved_from_folder": "Inbox",
                "moved_to_folder": "Archive"
            }
        }
    }
    

##### Output messages

The **Move Email to Folder** action can return the following output messages:

Output message | Message description  
---|---  
`NUMBER_OF_MOVED_EMAILS mails were successfully moved from` SOURCE_FOLDER to DESTINATION_FOLDER `No mails were found matching the search criteria!` | The action succeeded.  
`Error search emails: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Move Email to Folder** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Ping

Use the **Ping** action to test the connectivity to Email V2.

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

The **Ping** action can return the following output messages:

**Note:** This action performs separate connectivity checks for IMAP and SMTP. 

The action returns an overall success if at least one server is configured and passes the check, while noting any skipped or unconfigured parts.

It returns an overall failure if all configured checks fail, printing all associated errors.

If both IMAP and SMTP aren't configured, it returns an error.

Output message | Message description  
---|---  
`Successfully connected to the email server server with the provided connection parameters!` | The action succeeded.  
`Failed to connect to the IMAP server! Error is ERROR_REASON` `Failed to connect to the SMTP server! Error is ERROR_REASON` `SMTP (or IMAP) configuration is needed to execute action. Please configure STMP (or IMAP) on integration configuration page in Content Hub. ` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Save Email Attachments to Case

Use the **Save Email Attachments to Case** action to retrieve and automatically save attachments from specific emails in the mailbox directly onto the current case's Case Wall.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Save Email Attachments to Case** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | Required. A comma-separated list of the mailbox folders where the action searches for the email.  
`Message ID` | Optional. The unique Message ID of the email from which to download attachments.  
`Attachment To Save` | Optional. The specific name of the attachment being saved. If no value is provided, the action saves all attachments from the email to the Case Wall.  
  
#### Action outputs

The **Save Email Attachments to Case** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Save Email Attachments to Case** action:
    
    
    {
        "saved_attachments_from_email": {
            "message_id": "<a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0@mail.example.com>",
            "subject": "Email with Malicious Attachment",
            "sender": "external@suspicious.com",
            "attachments_saved": [
                {
                    "file_name": "Invoice_Q3_2025.pdf",
                    "file_hash_md5": "3bd4a36cc0ed0bfc12ae5e2ece929e82",
                    "saved_to_case_wall": "True"
                },
                {
                    "file_name": "Report_Data.docx",
                    "file_hash_md5": "b3e0c1a9f8d7c6b5a4e3d2c1b0a9f8e7",
                    "saved_to_case_wall": "True"
                }
            ]
        }
    }
    

##### Output messages

The **Save Email Attachments to Case** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully saved the following attachments from the email MESSAGE_ID: MESSAGE_INFO` | The action succeeded.  
`Failed to save the email attachments to the case, the error is: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Save Email Attachments to Case** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Search Email

Use the **Search Email** action to find specific emails within the configured mailbox using various filtering criteria.

The action retrieves details about the matching messages in a JSON file, which can be used for subsequent automated or manual analysis.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Email** action requires the following parameters:

Parameter | Description  
---|---  
`Folder Name` | Required. A comma-separated list of the mailbox folders where the action searches for emails. The default value is `Inbox`.  
`Subject Filter` | Optional. A subject line used to narrow the search for matching emails.  
`Sender Filter` | Optional. A sender's address used to search for matching emails.  
`Recipient Filter` | Optional. A recipient's address used to search for matching emails.  
`Time frame (minutes)` | Required. The time window (in minutes) the search looks back for emails. The default value is `60`.  
`Only Unread` | Optional. If selected, the search retrieves only unread emails. Disabled by default  
`Max Emails To Return` | Required. The maximum number of emails the action returns as a result. The default value is `100`.  
  
#### Action outputs

The **Search Email** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Search Email** action:
    
    
    {
        "emails": {
            "email_1": {
                "message id": "<CAJP=A_uGkttoWc1eahvP43rWVEsdk77nMu1FomhgRjRSmySLLg@mail.example.com>",
                "received": "Mon, 26 Aug 2019 03:20:13 -0700 (PDT)",
                "sender": "user@test.example",
                "recipients": "user1@example.com,user2@example.com",
                "subject": "Cool offer",
                "plaintext_body": "Hi, ...",
                "attachmment_1": "pdfdocument.pdf",
                "attachment_1_file_hash_md5": "3bd4a36cc0ed0bfc12ae5e2ece929e82"
            },
            "email_2": {
                "message id": "<WEAA=D_uGkttoWc1eahvP43rWVEsdk77nMu1FomhgRjRSmySLLg@mail.example.com>",
                "received": "Wen, 21 Aug 2019 03:20:13 -0700 (PDT)",
                "sender": "user@test.example",
                "recipients": "user3@example.com",
                "subject": "Cool offer",
                "plaintext_body": "Hi, ...",
                "attachmment_1": "photo.jpg",        "attachment_1_file_hash_md5": "3bd4a36cc0ed0bfc12ae5e2ece929e82",
                "attachmment_2": "word_document.docx",
                "attachment_2_file_hash_md5": "3bd4a36cc0ed0bfc12ae5e2ece929e82"
            }
        }
    }
    

##### Output messages

The **Search Email** action can return the following output messages:

Output message | Message description  
---|---  
`Search found NUMBER_OF_FOUND_EMAILS emails based on the provided search criteria` `Search didn't found any matching emails` | The action succeeded.  
`Search didn't completed successfully due to error: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Send Email

Use the **Send Email** action to send emails from the configured mailbox to multiple recipients.

This action optionally returns the Message ID, which can then be used by the **Wait for Email From User** action to track user responses and control playbook execution.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Send Email** action requires the following parameters:

Parameter | Description  
---|---  
`Recipients` | Required. The primary recipient email addresses. Multiple addresses must be separated by commas.  
`CC` | Optional. The email addresses to include in the Carbon Copy (CC) field. Multiple addresses must be separated by commas.  
`Bcc` | Optional. The email addresses to include in the Blind Carbon Copy (Bcc) field. Multiple addresses must be separated by commas.  
`Subject` | Required. The subject line of the email message.  
`Content` | Required. The body content of the email message.  
`Return message id for the sent email` | Optional. If selected, the action returns the unique Message ID in the JSON result. This ID can be used by the Wait for Email From User action to track responses. Disabled by default.  
`Attachments Paths` | Optional. A comma-separated list of absolute file paths on the server for attachments.  
  
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

The following example shows the JSON result outputs received when using the **Send Email** action:

**Note:** Enabling `Return message id for the sent email` is required to retrieve the unique `message_id` in the JSON result, which is required for dependent actions.
    
    
    {
        "message_id": "<4f1e50e8f4027d187a2385a39b83cde46e5b53c1-10013525-100078757@example.com>"
    }
    

##### Output messages

The **Send Email** action can return the following output messages:

**Note:** This action performs separate connectivity checks for IMAP and SMTP. 

The action returns an overall success if at least one server is configured and passes the check, while noting any skipped or unconfigured parts.

It returns an overall failure if all configured checks fail, printing all associated errors.

If neither IMAP nor SMTP are configured, it returns an error.

Output message | Message description  
---|---  
`Mail sent successfully.` `Mail sent successfully. Mail message ID is: MESSAGE_ID` | The action succeeded.  
`Execution Failed: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Send Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Send Thread Reply

Use the **Send Thread Reply** action to send a new message as a response within an existing email thread using the original message ID.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Send Thread Reply** action requires the following parameters:

Parameter | Description  
---|---  
`Message ID` | Required. The unique ID of the message to which the reply is sent.  
`Folder Name` | Required. A comma-separated list of the mailbox folders where the action searches for the original email. The folder name must match the IMAP folder exactly. If the name contains spaces, it must be wrapped in double quotes (such as "[Gmail]/All Mail"). The default value is `Inbox`.  
`Content` | Required. The body content of the reply message.  
`Attachment Paths` | Optional. A comma-separated list of file paths on the server for attachments to include in the reply.  
`Reply All` | Optional. If selected, the reply is sent to all recipients of the original email thread. This parameter takes priority over `Reply To`. Enabled by default.  
`Reply To` | Optional. A comma-separated list of specific email addresses to receive the reply. If `Reply All` is disabled and no value is provided, the reply is sent only to the sender of the original email.  
  
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

The following example shows the JSON result outputs received when using the **Send Thread Reply** action:
    
    
    {
        "message_id": "<162556278608.14165.480701790user@example>",
        "recipients": "test@example.com"
    }
    

##### Output messages

The **Send Thread Reply** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully sent reply to the message with ID MESSAGE_ID in Exchange.` | The action succeeded.  
`Error executing action "Send Thread Reply". Reason: ERROR_REASON` | The action failed. Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Send Thread Reply** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Wait for Email From User

Use the **Wait for Email From User** action to pause the playbook's execution and monitor a mailbox for a reply to a message previously sent by the **Send Email** action.

This action doesn't run on Google SecOps entities. 

**Note:** This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE as needed.

#### Action inputs

The **Wait for Email From User** action requires the following parameters:

Parameter | Description  
---|---  
`Email Message_id` | Required. The unique Message ID of the sent email for which the action tracks replies. If the message has been sent using the Send Email action, please select `SendEmail.JSONResult.message_id` as a placeholder.  
`Email Date` | Required. The timestamp indicating when the original email was sent. The action uses this value to calculate the reply window. If the message was sent using the Send Email action, use the placeholder `SendEmail.JSONResult.email_date`.  
`Email Recipients` | Required. A comma-separated list of recipient email addresses from which the action waits for a reply. If the message was sent using the Send Email action, use the placeholder `SendEmail.JSONResult.email_date`.  
`Wait stage timeout (minutes)` | Optional. The duration (in minutes) the action waits for a reply before marking the wait stage as timed out. The default value is `1440`.  
`Wait for all recipients to reply?` | Optional. If selected, the playbook waits for responses from all recipients to proceed; otherwise, it proceeds after receiving the first reply. Enabled by default.  
`Wait stage exclude pattern` | Optional. A regular expression pattern used to exclude specific replies (such as automated Out-of-Office messages) from being considered valid responses.  
`Folder to check for reply` | Optional. A comma-separated list of the mailbox folders where the action searches for the user's reply. This parameter is case-sensitive. The default value is `Inbox`.  
`Fetch Response Attachments` | Optional. If selected, any attachments included in the recipient's reply are saved as attachments for the action result. Disabled by default.  
  
#### Action outputs

The **Wait for Email From User** action provides the following outputs:

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

The following example shows the JSON result outputs received when using the **Wait for Email From User** action:
    
    
    {
        "Responses":
        {[
         "user1@example.com": "Approved",
         "user2@example.com": "",
         "user3@example.com": ""
         ]}
    }
    

##### Script result

The following table lists the value for the script result output when using the **Wait for Email From User** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
## Connectors

To learn more about configuring connectors in Google SecOps, see [Ingest your data (connectors)](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors). **Note:** To prevent data loss, connectors utilize **Event Flattening**. If a raw alert contains a list of entities (such as multiple email addresses, hostnames, or IP addresses), connectors automatically flatten them into separate, unique events. 

For example, a single raw alert containing three different email addresses is ingested as three separate events, each containing one distinct email address.

This process ensures that every entity is correctly indexed as a unique asset, making it fully searchable and actionable in playbooks.

### Generic IMAP Email Connector

Use the **Generic IMAP Email Connector** to periodically connect to an IMAP mail to check a specified mailbox for new emails. The connector processes new emails in near real-time, translating them into contextualized alerts and cases within the Google SecOps platform.

#### Known Issues and Limitations

  1. **Outlook Attachments (.eml)** : The connector may not process attachments converted to the .eml format by Microsoft Outlook if critical headers are missing. Google SecOps still creates an alert for the email, but without an event based on the attachment. The following log indicates this issue:
         
         Error Code 1: Encountered an email object with missing headers. Please
         visit documentation portal for more details.
         

  2. **Missing Filenames** : When processing attached mail files that lack a filename in the email headers, the connector assigns a unique placeholder filename: `Undefined_{UUID}.eml`, allowing the attachment to appear as an event in Google SecOps.




#### Email Case Forwarding

Google SecOps communicates with the email server to search for and ingest emails, forwarding them to the platform for near real-time translation and contextualization as security alerts.

#### Connector Rules

  * The connector uses SSL/TLS to ensure encrypted communication with the email server.
  * The connector supports connecting to the mail server using a proxy for both IMAP and IMAPS traffic.
  * The connector allows searching for emails across multiple mailbox folders. The `Folder` parameter accepts a comma-separated, case-sensitive list of folder names.
  * The connector supports Unicode encoding, enabling it to process emails sent in languages other than English.



#### Connector inputs

The **Generic IMAP Email Connector** requires the following parameters:

Parameter | Description  
---|---  
`Default Environment` | Optional. The name of the environment to which ingested alerts are assigned.  
`Run Every` | Optional. The frequency at which the connector runs to check for new emails. The default value is `00:00:10:00` (10 minutes).  
`Product Field Name` | Required. The name of the field where the product name is stored. The product name primarily impacts mapping. To streamline and improve the mapping process for the connector, the default value resolves to a fallback value that is referenced from the code. Any invalid input for this parameter resolves to a fallback value by default. The default value is `Product Name`.  
`Event Field Name` | Required. The name of the field that determines the event name (subtype). The default value is `event_name_mail_type`.  
`Additional headers to extract from emails` | Optional. A comma-separated list of custom header fields to be extracted from the email message during connector processing.  
`Script Timeout (Seconds)` | Required. The timeout limit, in seconds, for the Python process that runs the current script. The default value is `60`.  
`IMAP Server Address` | Required. The IP address or DNS hostname of the IMAP server to connect to. The default value is `imap.gmail.com`.  
`IMAP Port` | Required. The port number used to connect to the IMAP server. The default value is `993`.  
`Username` | Required. The username for the mailbox from which the connector pulls emails. The default value is `username`.  
`Password` | Required. The password for the mailbox used to pull emails. The default value is `1`.  
`Folder to check for emails` | Required. A comma-separated list of mailbox folders where the connector searches for emails. This parameter is case-sensitive. The default value is `Inbox`.  
`Server Time Zone` | Optional. The timezone configured in the mail server. The default value is `UTC`.  
`Environment Regex Pattern` | Optional. A regular expression pattern used to manipulate the event field data and extract the environment name.  
`IMAP USE SSL` | Optional. If selected, the connector uses SSL/TLS to establish a secure IMAP connection to the mail server. Enabled by default.  
`Unread Emails Only` | Optional. If selected, the connector pulls only unread emails. Enabled by default.  
`Mark Emails as Read` | Optional. If selected, emails are marked as read after being successfully pulled by the connector. Enabled by default.  
`Attach Original EML` | Optional. If selected, the original message is attached to the created alert as an .eml file. Disabled by default.  
`Regex expressions to handle forwarded emails` | Optional. A JSON one-liner string containing regular expression patterns to extract original subject, sender, and recipient fields from forwarded emails.  
`Exclusion Body Regex` | Optional. A regular expression pattern used to exclude emails from ingestion if the body content matches the pattern, such as `([N|n]ewsletter)|([O|o]ut of office)`.  
`Exclusion Subject Regex` | Optional. A regular expression pattern used to exclude emails from ingestion if the subject line matches the pattern, such as `([N|n]ewsletter)|([O|o]ut of office)`.  
`Offset Time In Days` | Required. The maximum number of days backwards the connector fetches mail from (max time window). This value also serves as a fallback for the initial run or if the connector timestamp expires, ensuring alerts are ingested for the disabled period. The default value is `5`.  
`Max Emails Per Cycle` | Required. The maximum number of emails the connector processes in a single polling cycle. The default value is `10`.  
`Proxy Server Address` | Optional. The address of the proxy server to use.  
`Proxy Username` | Optional. The username for proxy server authentication.  
`Proxy Password` | Optional. The password for proxy server authentication.  
`Create a Separate Siemplify Alert per Attached Mail File?` | Optional. If selected, the connector creates a separate alert for every attached email file found within a message. This is useful when event mapping is set to create entities from attached email files. Disabled by default.  
`Original Received Mail Prefix` | Optional. A prefix (such as `orig`) added to extracted keys (to, from, subject, etc.) from the original email received in the monitored mailbox. The default value is `orig`.  
`Attached Mail File Prefix` | Optional. A prefix (such as `attach`) added to extracted keys (to, from, subject, etc.) from attached mail files found within the email. The default value is `attach`.  
**Note:** The connector supports extracting specific values from emails using Regular Expressions defined in the **Dynamic List** area (often labeled "Extraction Rules"). To extract a value, use the format: `Desired Display Name: matching regex`. 

To extract URLs from the email body for creation as entities, insert:

`none urls: http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%0-9a-fA-F))+`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
