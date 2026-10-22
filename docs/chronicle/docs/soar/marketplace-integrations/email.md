---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email/
title: Email \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:39.308304+00:00
---

# Email  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Email

**Deprecated:** This integration is deprecated and no longer supported. We recommend that you use the [Email V2](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/email-v2) integration instead.

This integration uses one or more open source components. You can download a copy of the full source code of this integration from the [storage bucket](https://storage.googleapis.com/csoar_public_integrations/Email.zip).

## Prerequisites

The example provided in this document is based on Gmail, as the most popular email server. Gmail provides several options to access the mailbox data from third-party applications:

  1. **More secure app access** , enabled by default, where one could sign into a Google Account without exposing the password, and see what data the third party app will have access to and more.

[How more secure apps help protect your account](https://support.google.com/accounts/answer/6010255#more-secure-apps-how)

  2. **App password.** An App password is a 16-digit passcode that gives the third-party app access to Gmail mailbox. App passwords can only be used with accounts that have 2-Step Verification turned on.

[Sign in with app passwords](https://support.google.com/accounts/answer/185833)

  3. **Less secure apps** usually is for third party apps that don't follow the Google security standards for some reason. If this option is not enabled, third-party app access attempt that don't follow Google security standards to Gmail mailbox will be blocked. Enablement of this option makes Gmail account less secure, so this option should be used with caution.

[Less secure apps & your Google Account](https://support.google.com/accounts/answer/6010255)


**Note:** For example, for Gmail, decisions should be made at the development stage about what option for permission to use.

### Network Access to IMAP/SMTP

To use a configured account to access mail with IMAP and send mail with SMTP, go to **Configuration details > Account > Turn on access for less secure apps**.

Function | Default Port | Direction | Protocol  
---|---|---|---  
API | Multivalues | Outbound | IMAP/SMTP  
  
## Integrate Email with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

## Actions

### Download Email Attachments

Download Email Attachments.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Download Path | String | N/A | Yes | Save message attachment to the given download path.  
Message ID | String | N/A | No | Download attachments from specific email using its ID. For example, `example@mail.gmail.com`.  
Subject filter | String | N/A | No | Filter condition to search emails by specific subject.  
Email UID | String | N/A | No | UUID to filter by.  
Only Unread | Checkbox | N/A | No | If checked, fetch from mailbox only the unread emails.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Example**  
---|---  
attachments_local_paths | Script result returns String of comma separated full paths to the saved attachments.  
  
### Get Mail EML File

Fetch mail message EML information.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Message ID | String | N/A | No | Download attachments from specific email using its ID. For example, `example@mail.gmail.com`.  
Base64 Encode | String | true | No | Filter condition to search emails by specific subject.  
  
#### Run On

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Example**  
---|---  
eml_base64 | N/A  
  
### Ping

Test connectivity to the email server with parameters provided at the integration configuration page.

#### Parameters

N/A

#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_succeed | True/False | is_succeed:False  
  
### Send Email

You may send emails from a single mailbox to a number of random recipients with this action. Users may be alerted of the outcome of such alerts by the respective alerts generated by Google SecOps or users. The action can return the email message ID so that you will be able to use the message ID to monitor username response of this email in your "Wait for User E-mail" action. It is used to ask the user a playbook question and to operate on the playbook according to the user's answer.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Recipients | String | N/A | Yes | Recipient email address. Multiple addresses can be separated by commas.  
CC | String | N/A | No | CC email address. Multiple addresses can be separated by commas.  
Bcc | String | N/A | No | Bcc email address. Multiple addresses can be separated by commas.  
Subject | String | N/A | Yes | The subject of the email.  
Content | String | N/A | Yes | The body of the email.  
  
#### Run On

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
### Send Email and Wait

This action periodically searches the specified mailbox for a user's unique email. The function can be used with the "Submit Email" feature, and the "Check Message ID" option for the "submit email" parameter, which helps you to have a preference in the playbooks to submit a request to the receiver and wait until the recipient has answered the question. Google SecOps workflow of the playbook can use branching based on feedback from the user.

#### Parameters

**Parameter** | **Type** | **Default Value** | **Is Mandatory** | **Description**  
---|---|---|---|---  
Recipients | String | N/A | Yes | Recipient email address. Multiple addresses can be separated by commas.  
CC | String | N/A | No | CC email address. Multiple addresses can be separated by commas.  
Bcc | String | N/A | No | Bcc email address. Multiple addresses can be separated by commas.  
Subject | String | N/A | Yes | The subject of the email.  
Content | String | N/A | Yes | The body of the email.  
Exclusion Subject Regex | String | N/A | No | Exclude received mails by (subject) inserted regular expression and wait for the next mail.  
Exclusion Body Regex | String | N/A | No | Exclude received mails by (body) inserted regular expression and wait for the next mail.  
  
#### Run on

This action runs on all entities.

#### Action results

##### Script result

**Script Result Name** | **Value Options** | **Example**  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON result
    
    
    {
        "body": "Mail Body",
        "receivers": "set(['user1@example.com'])",
        "cc": [],
        "timestamp": 1565012780,
        "raw": "Raw Content",
        "names": {
            "user1@example.com": null,
            "user2@example.com": "Tester Testor"
        },
        "content_type": "multipart/alternative",
        "date": "2019-08-05 16:46:20",
        "subject": "Re: Subject",
        "answer": " ",
        "sender": "user2@example.com",
        "received_timestamp": null,
        "charset": null,
        "bcc": [],
        "to": ["user1@example.com"],
        "email_uid": "173180",
        "received_date": null,
        "reply_to": null,
        "html_body": "HTML Body",
        "message_id": "<id@example-domain>",
        "plaintext_body": "Plain Text Body",
        "in_replay_to": "<id@example-domain>"
    }
    

## Connectors

For detailed instructions on how to configure a connector in Google SecOps, see [Configuring the connector](https://docs.cloud.google.com/chronicle/docs/soar/ingest/connectors/ingest-your-data-connectors).

### Email Connector

The connector connects to the mail server periodically to check for new emails in a particular mailbox. If a new connector is present, an email will be sent out and a new alert will be created, which will be added with information from this email by Google SecOps.

This topic illustrates the mechanism and configuration by which Google SecOps connects and integrates to the IMAP/SMTP email along with supported working flows and actions taken within the platform. This topic refers to communicating with servers that support IMAP such as Gmail, Outlook.com and Yahoo! Mail.

#### Email Case Forwarding to Google SecOps

Google SecOps communicates with an email server for searching emails in near real-time, and forward them to be translated and contextualized as alerts for cases.

#### Connector parameters

Parameter | Type | Default Value | Description  
---|---|---|---  
Product Field Name | String | device_product | Framework parameter, must be set for every connector. Describes the name of the field where the product name is stored.  
Event Field Name | String | event_name | The field name used to determine the event name (sub-type).  
Script Timeout (Seconds) | Integer | 60 | The timeout limit (in seconds) for the Python process running current script.   
Email | Email | N/A | Email address for the mailbox to be monitored.  
IMAP Server Address | IP_OR_HOST | N/A | IMAP Server Address to connect to.  
IMAP Port | Integer | N/A | IMAP Port to connect to.  
Username | String | N/A | Username for the mailbox to pull emails from, for example, `user@example.com`.  
Password | Password | N/A | Password for the email mailbox to pull emails from.  
Folder to check for emails | String | Inbox | Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive.  
Server Time Zone | String | UTC | The timezone configured in the server, examples (1. UTC, 2. Asia/Jerusalem).   
Environment Regex Pattern | String | N/A | If defined, the connector extracts the environment from the specified event field. You can manipulate the field data using the regular expression pattern field to extract a specific string.  
IMAP USE SSL | Checkbox | Checked | Indicates whether to use SSL on connection or not.  
Unread Emails Only | Checkbox | Checked | If checked, pull only unread mails.  
Mark Emails as Read | Checkbox | Checked | If checked, mark mails as read after pulling them.  
Attach Original EML | Checkbox | Unchecked | If checked, attach the original message as eml file.  
Regex expressions to handle forwarded emails | String | N | Parameter could be used to specify a JSON one liner string to handle forwarded emails - to search for subject, from and to fields of original email in forwarded email.  
Offset Time In Days | Integer | 5 | Max number of days to fetch mails since. Example: 3.  
Max Emails Per Cycle | Integer | 10 | Max count of mails to pull in one cycle.  
Proxy Server Address | IP_OR_HOST | N/A | The address of the proxy server to use.  
Proxy Username | String | N/A | The proxy username to authenticate with.  
Proxy Password | Password | N/A | The proxy password to authenticate with.  
  
In the dynamic list area, add the following rule in order to extract specific values from the email using the regular expression in the following format: `Display name: matching regular expression`.

For example, to extract URLs from the email, enter the following rule:
    
    
    urls: http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%0-9a-fA-F))+
    

#### Use cases

Monitor a specific mailbox for new emails for ingestion to the Google SecOps server as alerts.

#### Connector rules

  * The connector supports encrypted communications for email server communications (SSL/TLS).

  * The connector supports connection to the mail server using proxy for both IMAP and IMAPS traffic.

  * The connector has a parameter to specify the mailbox email folder to search for the emails. The parameter accepts a comma-separated list of folders to check the user response in multiple folders. The parameter is case-sensitive.

  * The connector supports Unicode encoding for the emails processed as end user communications, which could be in a language other than English.




**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
