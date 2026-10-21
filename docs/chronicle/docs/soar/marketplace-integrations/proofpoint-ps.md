---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-ps/
title: Proofpoint Email Protection \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:29:16.509290+00:00
---

# Proofpoint Email Protection  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/proofpoint-ps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Proofpoint Email Protection

This document provides guidance on how to integrate Proofpoint Email Protection with Google SecOps.

## Integrate Proofpoint Email Protection with Google Security Operations

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration inputs

To configure the integration, use the following parameters:

Parameters  
---  
`API Root` | _Required_ API root of your Proofpoint Email Protection instance.  
`Username` | _Required_ Username of your Proofpoint Email Protection instance.  
`Password` | _Required_ Password of your Proofpoint Email Protection instance.  
`Verify SSL` | _Optional_ If checked, verifies that the SSL connection certificate to the Proofpoint server is valid.  
  
## Actions

Before running actions, make sure to configure their respective parameters, if any.

### Enrich Entities

Enrich entities with Proofpoint Email Protection.

#### Entities

This action runs on the following entities:

  * Hostname
  * User



#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | Available  
JSON result | N/A  
Script result | Available  
  
##### Entity enrichment

Enrichment field | Logic  
---|---  
`dlpviolation` | N/A  
`messagestatus` | N/A  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
### Ping

Test the Proofpoint Protection Server connectivity.

#### Entities

This action runs on all entities.

#### Action inputs

N/A

#### Action outputs

Action output type  
---  
Case wall attachment | N/A  
Case wall link | N/A  
Case wall table | N/A  
Enrichment table | N/A  
JSON result | N/A  
Script result | Available  
  
##### Script result

Script result name | Value  
---|---  
is_success | True/False  
  
### Search Quarantined Emails

Use the **Search Quarantined Emails** action to trace and analyze information about quarantined messages in Proofpoint Email Protection.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Search Quarantined Emails** action requires the following parameters:

Parameters  
---  
`Message GUID` | _Optional_ The unique message GUID to search for.  
`Message ID` | _Optional_ The unique Internet Message ID to search for.  
`Sender` | _Optional_ The email address of the sender.  
`Recipient` | _Optional_ The email address of the recipient.  
`Subject` | _Optional_ The subject of the quarantined email.  
`Time Frame` | _Optional_ Specify a time frame for the results. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | _Optional_ Specify the start time for the results in ISO 8601 format. This parameter is required if `Custom` is selected for the `Time Frame` parameter.  
`End Time` | _Optional_ Specify the end time for the results in ISO 8601 format. If left blank and `Custom` is selected for the `Time Frame` parameter, the current time is used.  
`Folder Name` | _Optional_ The name of the quarantine folder. The default value is `Quarantine`.  
`Query ID` | _Optional_ An ID used for the REST client to track the search results.  
`Fetch DLP Violation` | _Optional_ Select the level of DLP violation data to fetch. The possible values are as follows:

  * `No`
  * `Basic`
  * `Detailed`

The default value is `No`.  
`Fetch Message Status` | _Optional_ If selected, fetches the message status and comments. Not selected by default.  
`Max Results To Return` | _Optional_ The maximum number of results to return. The default value is `100`. The maximum value is `1000`.  
  
#### Action outputs

The **Search Quarantined Emails** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Search Quarantined Emails** action:
    
    
    [
      {
        "processingserver": "mta1",
        "date": "2026-05-25 09:30:00",
        "subject": "Test Subject",
        "messageid": "message-id-2",
        "folder": "PCI",
        "size": 1200,
        "rcpts": [
          "recipient@example.com"
        ],
        "from": "sender@example.com",
        "spamscore": 99,
        "guid": "message-guid-1",
        "host_ip": "10.10.10.10",
        "localguid": "14:14:7"
      }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Search Quarantined Emails** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Forward Quarantined Email

Use the **Forward Quarantined Email** action to forward quarantined messages to another recipient. Note: This action works on messages that were created in the last 30 days. This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Forward Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ Comma-separated list of quarantined message GUIDs.  
`Folder Name` | _Required_ Name of the folder where the message is stored.  
`Deleted Folder Name` | _Optional_ Folder to move the message to after forwarding.  
`New Subject` | _Optional_ Overwrites the original subject.  
`Append Old Subject` | _Optional_ If selected, appends the original subject to the forwarded subject. Disabled by default.  
`From Address` | _Optional_ Overwrites the envelope sender.  
`Header From` | _Optional_ Overwrites the Header From.  
`To Address` | _Required_ Recipient email address(es) to forward to.  
`New Body Comment` | _Optional_ New message body comment.  
  
#### Action outputs

The **Forward Quarantined Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Forward Quarantined Email** action:
    
    
    {
      "success": [
        {
          "processingserver": "m0409394.ppops.net",
          "date": "2026-06-10 12:27:51",
          "subject": "JS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X",
          "messageid": "AM6PR05MB5064A15BF3842D5A4A09AE70BE1A2@AM6PR05MB5064.eurprd05.prod.outlook.com",
          "folder": "Outbound Spam",
          "size": 12174,
          "rcpts": [
            "user@example.com"
          ],
          "from": "james.bond@siemplifycyarx.onmicrosoft.com",
          "spamscore": 0,
          "guid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq",
          "host_ip": "mail-norwayeastazhn15013062.outbound.protection.outlook.com [52.102.179.62]",
          "localguid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq"
        }
      ]
    }
    

##### Script result

The following table lists the value for the script result output when using the **Forward Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Forward Quarantined Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully forwarded quarantined email(s) in Proofpoint Email Protection.` | Action succeeded.  
`Error executing action "Forward Quarantined Email". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Release Quarantined Email

Use the **Release Quarantined Email** action to release specified quarantined messages.

**Note:** This action works on messages that were created in the last 30 days.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Release Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ Comma-separated list of quarantined message GUIDs.  
`Folder Name` | _Required_ Name of the folder where the message is stored.  
`Deleted Folder Name` | _Optional_ Folder to move the message to after release.  
`Rescan Message` | _Optional_ If selected, rescans the released message by DLP and Attachment Defense. Disabled by default.  
`Branding Template` | _Optional_ Branding template to use when released.  
`Security Policy` | _Optional_ Secure Reader response profile.  
  
#### Action outputs

The **Release Quarantined Email** action provides the following outputs: 

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Release Quarantined Email** action:
    
    
    {
      "success": [
        {
          "processingserver": "m0409394.ppops.net",
          "date": "2026-06-10 12:27:51",
          "subject": "JS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X",
          "messageid": "AM6PR05MB5064A15BF3842D5A4A09AE70BE1A2@AM6PR05MB5064.eurprd05.prod.outlook.com",
          "quarantinefolder": "Outbound Spam",
          "size": 12174,
          "rcpts": [
            "user@example.com"
          ],
          "from": "james.bond@siemplifycyarx.onmicrosoft.com",
          "spamscore": 0,
          "guid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq",
          "host_ip": "mail-norwayeastazhn15013062.outbound.protection.outlook.com [52.102.179.62]",
          "localguid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq"
        }
      ]
    }
    

##### Script result

The following table lists the value for the script result output when using the **Release Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Release Quarantined Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully released quarantined email(s) in Proofpoint Email Protection.` | Action succeeded.  
`Error executing action "Release Quarantined Email". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
### Delete Quarantined Email

Use the **Delete Quarantined Email** action to permanently delete quarantined messages from the Proofpoint quarantine folder.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Delete Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ The unique message GUID(s) to delete. Supports a comma-separated list for multiple GUIDs.  
`Folder Name` | _Required_ The folder name where the message is stored (for example, `Quarantine` or `PCI`).  
`Time Frame` | _Optional_ Specify a time frame for the results. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | _Optional_ Specify the start time for the results in ISO 8601 format. This parameter is required if `Custom` is selected for the `Time Frame` parameter.  
`End Time` | _Optional_ Specify the end time for the results in ISO 8601 format. If left blank and `Custom` is selected for the `Time Frame` parameter, the current time is used.  
`Deleted Folder Name` | _Optional_ The folder name to move the deleted messages to.  
  
#### Action outputs

The **Delete Quarantined Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Delete Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Move Quarantined Email

Use the **Move Quarantined Email** action to move quarantined messages to a specified target folder or rule queue.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Move Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ The unique message GUID(s) to move. Supports a comma-separated list for multiple GUIDs.  
`Folder Name` | _Required_ The folder name where the message is stored (for example, `Quarantine` or `PCI`).  
`Time Frame` | _Optional_ Specify a time frame for the results. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | _Optional_ Specify the start time for the results in ISO 8601 format. This parameter is required if `Custom` is selected for the `Time Frame` parameter.  
`End Time` | _Optional_ Specify the end time for the results in ISO 8601 format. If left blank and `Custom` is selected for the `Time Frame` parameter, the current time is used.  
`Target Folder Name` | _Required_ The target folder name to move the quarantined emails to.  
  
#### Action outputs

The **Move Quarantined Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Move Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Resubmit Quarantined Email

Use the **Resubmit Quarantined Email** action to resubmit specified quarantined messages back into the main filtering process queue for re-evaluation.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Resubmit Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ The unique message GUID(s) to resubmit. Supports a comma-separated list for multiple GUIDs.  
`Folder Name` | _Required_ The folder name where the message is stored (for example, `Quarantine` or `PCI`).  
`Time Frame` | _Optional_ Specify a time frame for the results. The possible values are as follows:

  * `Last Hour`
  * `Last 6 Hours`
  * `Last 24 Hours`
  * `Last Week`
  * `Custom`

The default value is `Last Hour`.  
`Start Time` | _Optional_ Specify the start time for the results in ISO 8601 format. This parameter is required if `Custom` is selected for the `Time Frame` parameter.  
`End Time` | _Optional_ Specify the end time for the results in ISO 8601 format. If left blank and `Custom` is selected for the `Time Frame` parameter, the current time is used.  
  
#### Action outputs

The **Resubmit Quarantined Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Resubmit Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
### Download Quarantined Email

Use the **Download Quarantined Email** action to download raw message data for quarantined emails created within the last 30 days.

This action doesn't run on Google SecOps entities. 

#### Action inputs

The **Download Quarantined Email** action requires the following parameters:

Parameters  
---  
`Message GUIDs` | _Required_ The unique message GUID(s) of the email(s) to download.  
`Folder Name` | _Optional_ The name of the folder where the message is stored. If not specified, defaults to `Quarantine`.  
`Download Folder Path` | _Required_ The folder path where the file needs to be stored. The default value is `/tmp`.  
`Overwrite` | _Required_ If selected, overwrites any existing file with the same name. Enabled by default.  
`Save To Case Wall` | _Optional_ If selected, saves the downloaded file as an attachment on the case wall. Disabled by default.  
  
#### Action outputs

The **Download Quarantined Email** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Download Quarantined Email** action:
    
    
    {
      "success": [
        {
          "downloaded_file_path": "/tmp/filename",
          "processingserver": "m0409394.ppops.net",
          "date": "2026-06-10 12:27:51",
          "subject": "JS*C4JDBQADN1.NSBN3*2IDNEN*GTUBE-STANDARD-ANTI-UBE-TEST-EMAIL*C.34X",
          "messageid": "AM6PR05MB5064A15BF3842D5A4A09AE70BE1A2@AM6PR05MB5064.eurprd05.prod.outlook.com",
          "folder": "Outbound Spam",
          "size": 12174,
          "rcpts": [
            "user@example.com"
          ],
          "from": "data",
          "spamscore": 0,
          "guid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq",
          "host_ip": "mail-norwayeastazhn15013062.outbound.protection.outlook.com [52.102.179.62]",
          "localguid": "VSumNsz7vyHqnWhaZkUwElagll3ZCYZq"
        }
      ]
    }
    

##### Script result

The following table lists the value for the script result output when using the **Download Quarantined Email** action:

Script result name | Value  
---|---  
`is_success` | `true` or `false`  
  
##### Action output messages

The **Download Quarantined Email** action provides the following output messages:

Output message | Message description  
---|---  
`Successfully downloaded quarantined email(s) in Proofpoint Email Protection.` | Action succeeded.  
`Error executing action "Download Quarantined Email". Reason: ERROR_REASON` | Action failed. Check connection to the server, input parameters, or credentials.  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
