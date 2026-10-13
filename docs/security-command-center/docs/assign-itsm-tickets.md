---
url: https://docs.cloud.google.com/security-command-center/docs/assign-itsm-tickets/
title: Assign tickets based on posture cases \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:14:16.523309+00:00
---

# Assign tickets based on posture cases  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/assign-itsm-tickets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Assign tickets based on posture cases Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This page documents the mechanism of an automatic ticket assignment in Security Command Center Enterprise and explains how to manually assign or reassign tickets using the Security Operations console.

## Overview

A ticket assignee is a person responsible for addressing and remediating the vulnerabilities. The ticket is assigned to the respective assignee automatically based on either the resource owner value inherited by the finding through the Google Cloud [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) or the value configured in the connector's **Fallback Owner** parameter.

## Assign tickets automatically

The default automatic flow for assigning a ticket consists of the following steps:

  1. Determining the resource owner of a finding.

  2. Creating cases and grouping related findings into them.

  3. Creating and assigning tickets based on cases.




### Determining the resource owner

While ingesting and grouping findings into cases, the **SCC Enterprise - Urgent Posture Findings Connector** analyzes every finding for the resource owner and fallback owner values. The fallback owner value configured in the **Fallback Owner** connector parameter is the final option to ensure that a custom finding is assigned to a correct person for remediation when all other prioritized options failed.

For more information about defining the resource owner in Security Command Center Enterprise, refer to [Determine ownership for posture findings](https://docs.cloud.google.com/security-command-center/docs/determine-ownership-posture-findings).

### Creating cases and grouping findings

After the connector has ingested a finding, Security Command Center forwards the finding to a new case if the finding is first of a kind, or an existing case if the finding parameters comply with a grouping mechanism. In a case, the finding becomes an _event_ which the _alert_ is based on. Essentially, an alert is a finding container that includes all information about a finding.

To learn more about how findings are grouped into cases, see [Group findings in cases](https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases).

### Creating and assigning tickets

Creating a case automatically creates a ticket in an integrated ticketing system. All information contained in a case is bidirectionally synchronized with a corresponding ticket, meaning that every time there is an update in a case like a new finding, a new comment, or a status change, the same update appears in the ticket and the other way around.

Security Command Center Enterprise automatically assigns the created ticket to the resource owner of findings grouped in a case. All findings in a case have the same resource owner.

**Important:** When using a ticketing system like Jira or ServiceNow to manage tickets, make sure to provide the assignable email (ldap) of the resource owner in your ticketing system, not the username.

## Assign tickets manually

Assigning tickets manually in requires you to run manual actions on cases.

### Assign Jira issues in cases

To manually assign a Jira issue in a case, complete the following steps:

  1. In the Google Cloud console, go to **Risk > Cases**.
  2. Select a case related to the ITSM ticket.
  3. In the **Case Overview** tab, click **Manual Action**.
  4. In the manual action **Search** field, enter `Jira`.
  5. In the search results under the **Jira** integration, select the **Assign Issue** action. The action dialog window opens.
  6. To configure the **Issue Key** parameter, enter the following placeholder: `[Case.Ticket_ID]`

The placeholder dynamically retrieves the Jira issue ID corresponding to the selected case.

     1. To configure the **Issue Key** parameter for a specific issue, enter the **Jira issue ID** in the following format: `SCCE-NUMBER`

You can find the issue ID in the Jira issue URL:
    
    https://YOUR_INSTANCE_NAME.atlassian.net/browse/ISSUE_ID
    

  7. To configure the **Assignee** parameter, enter the email address of the Jira ticket assignee.

Alternatively, you can enter the name of the ticket assignee as it is displayed in Jira. The action supports using usernames or displayed names.

  8. Click **Execute**.




### Assign ServiceNow tickets in cases

To manually assign a ServiceNow ticket in a case, complete the following steps:

  1. Retrieve the `sys_id` value to obtain the ServiceNow assignee ID.
  2. Assign the ServiceNow ticket.



#### Retrieve the `sys_id` value

  1. In the Google Cloud console, go to **Risk > Cases**.
  2. Select a case related to the ServiceNow ticket.
  3. In the **Case Overview** tab, click **Manual Action**.
  4. In the manual action **Search** field, enter `ServiceNow`.
  5. In the search results, select the **Get User Details** action. The action dialog window opens.
  6. To configure the **Emails** parameter field, enter the email address of the ServiceNow ticket assignee.
  7. Click **Execute**. Wait until the action is executed.
  8. Go to the **Case Wall** , and then click **Refresh Case**.
  9. In the **ServiceNow_Get User Details** data record, click **View more**.
  10. In the **JSON Result** section, find the **`sys_id`** key and save its value to use it in the following section.



#### Assign the ServiceNow ticket

  1. Go to the **Case Overview** tab, and then click **Manual Action**.
  2. In the manual action **Search** field, enter `ServiceNow`.
  3. In the search results under the **ServiceNow** integration, select the **Update Record** action. The action dialog window opens.
  4. To configure the **Table Name** parameter, enter the following value: `u_scc_enterprise_cloud_posture_ticket`
  5. To configure the **Object Json Data** parameter, enter the following code:
         
         {
           "u_assigned_to": "SYS_ID_VALUE"
         }
         

In the code, use the **`sys_id`** value that you retrieved in the previous section.

  6. To configure the **Record Sys ID** parameter, enter the following placeholder: `[Case.Ticket_ID]`

The placeholder dynamically retrieves the ServiceNow ticket ID corresponding to the selected case.

Alternatively, for the **Record Sys ID** parameter, you can provide a **Ticket ID** (**Case Overview** > **Ticket Information** widget > **Ticket ID**).

  7. Click **Execute**.




## What's next?

Learn how you can [group findings in cases](https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases).

Learn how you can [mute findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-mute-findings).

Learn how you can [mute findings in cases](https://docs.cloud.google.com/security-command-center/docs/mute-findings-in-cases).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
