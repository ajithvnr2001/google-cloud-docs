---
url: https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems/
title: Integrate Security Command Center Enterprise with ticketing systems \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:49.607531+00:00
---

# Integrate Security Command Center Enterprise with ticketing systems  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/integrate-ticketing-systems/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Integrate Security Command Center Enterprise with ticketing systems Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document explains how to integrate the Enterprise tier of Security Command Center with ticketing systems after configuring security orchestration, automation, and response (SOAR).

Integrating with ticketing systems is optional and requires manual configuration. If you use the default Security Command Center Enterprise configuration, you don't need to perform this procedure. You can integrate with a ticketing system later at any time.

## Overview

You can track findings using the console and APIs with the default Security Command Center Enterprise configuration. If your organization uses ticketing systems to track issues, integrate with Jira or ServiceNow after you have configured your Google Security Operations instance.

Upon receiving findings for resources, the **SCC Enterprise – Urgent Posture Findings Connector** analyzes and groups them into new or existing cases, depending on the finding type.

If you integrate with a ticketing system, Security Command Center creates a new ticket every time it creates a new case for findings. Security Command Center automatically updates the related ticket whenever a case is updated.

A single case can contain multiple findings. Security Command Center creates one ticket for each case and synchronizes the case content and information with the corresponding ticket to let ticket assignees know what to remediate.

The synchronization between a case and its ticket works both ways:

  * Changes within a case, such as a status update or new comment, are automatically reflected in the associated ticket.

  * Similarly, ticket details synchronize back to the case, enriching it with information from the ticketing system.




## Before you begin

Before configuring Jira or ServiceNow, provide a valid email address for the **Fallback Owner** parameter in the **SCC Enterprise – Urgent Posture Findings Connector** , and make sure that this email is assignable in your ticketing system.

## Integrate with Jira

Make sure to complete all integration steps to synchronize the case updates with Jira issues and ensure the correct playbook flow.

A _case priority_ is reflected in the Jira _issue severity_.

### Create a new project in Jira

To create a new project in Jira for the Security Command Center Enterprise issues called **SCC Enterprise Project (SCCE)** , run a manual action in the case. You can use any existing case or simulate one. For more information about simulating cases, refer to the [Simulate cases](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/simulate-cases) page in the Google SecOps documentation.

Creating a new Jira project requires Jira admin-level credentials.

**Note:** To create a new Jira project and configure the custom issue layout, use your Jira admin credentials.

To create a new Jira project, complete the following steps:

  1. In the Google Cloud console, go to **Risk > Cases**.
  2. Select an existing case or the one that you've simulated.
  3. In the **Case Overview** tab, click **Manual Action**.
  4. In the manual action **Search** field, enter `Create SCC Enterprise`.
  5. In search results under the **SCCEnterprise** integration, select the **Create SCC Enterprise Cloud Posture Ticket Type Jira** action. The dialog window opens.
  6. To configure the **API Root** parameter, enter the API root of your Jira instance, such as `https://YOUR_DOMAIN_NAME.atlassian.net`

  7. To configure the **Username** parameter, enter the username that you use to sign in to Jira as an administrator.

  8. To configure the **Password** parameter, enter the password that you use to sign in to Jira as an administrator.

  9. To configure the **API Token** parameter, enter the API token of your Atlassian admin account that was generated in the Jira console.

  10. Click **Execute**. Wait until the action is completed.




#### Optional: Configure custom Jira issue layout

  1. Sign in to Jira as an administrator.
  2. Go to **Projects > SCC Enterprise Project (SCCE)**.
  3. Adjust and reorder issue fields. For more details about managing issue fields, see [Configuring issue field layout](https://support.atlassian.com/jira-software-cloud/docs/configure-field-layout-in-the-issue-view/) in Jira documentation.



### Configure Jira integration

**Note:** To configure the Jira integration, use credentials for a regular Jira user with permissions to create and update issues in the newly created project.

  1. In the Google Cloud console, go to **Response > Playbooks** to open the Security Operations console navigation.
  2. In the Security Operations console navigation, go to **Response > Integrations Setup**.
  3. Select the **Default Environment**.
  4. In the integration **Search** field, enter `Jira`. The **Jira** integration returns as a search result.
  5. Click settings **Configure Instance**. The dialog window opens.
  6. To configure the **API Root** parameter, enter the API root of your Jira instance, such as `https://YOUR_DOMAIN_NAME.atlassian.net`

  7. To configure the **Username** parameter, enter the username that you use to sign in to Jira. Don't use your admin credentials.

  8. To configure the **API Token** parameter, enter the API token of your _non-admin_ Atlassian account that was generated in the Jira console.

  9. Click **Save**.

  10. To test your configuration, click **Test**.




### Enable the Posture Findings With Jira playbook

  1. In the Google Cloud console, go to **Response > Playbooks** to open the Security Operations console **Playbooks** page.
  2. In the Playbook **Search** bar, enter `Generic`.
  3. Select the **Posture Findings - Generic** playbook. This playbook is enabled by default.
  4. Switch the toggle to **disable the playbook**.
  5. Click **Save**.
  6. In the Playbook **Search** bar, enter `Jira`.
  7. Select the **Posture Findings With Jira** playbook. This playbook is disabled by default.
  8. Switch the toggle to **enable the playbook**.
  9. Click **Save**.



## Integrate with ServiceNow

Make sure to complete all integration steps to synchronize the updates of Google SecOps cases with ServiceNow tickets and ensure the correct playbook flow.

### Create and configure ServiceNow custom ticket type

Make sure to create and configure the ServiceNow custom ticket type enable the Activities tab in the ServiceNow UI and avoid using the erroneous ticket layout.

#### Create ServiceNow custom ticket type

Creating a custom ServiceNow ticket type requires ServiceNow admin-level credentials.

To create a custom ticket type, complete the following steps:

  1. In the Google Cloud console, go to **Risk > Cases**.
  2. Select an existing case or the one you've simulated.
  3. In the **Case Overview** tab, click **Manual Action**.
  4. In the manual action **Search** field, enter `Create SCC Enterprise`.
  5. In search results under the **SCCEnterprise** integration, select the **Create SCC Enterprise Cloud Posture Ticket Type SNOW** action. The dialog window opens.
  6. To configure the **API Root** parameter, enter the API root of your ServiceNow instance, such as `https://INSTANCE_NAME.service-now.com/api/now/v1/`

  7. To configure the **Username** parameter, enter the username that you use to sign in to ServiceNow as an administrator.

  8. To configure the **Password** parameter, enter the password that you use to sign in to ServiceNow as an administrator.

  9. To configure the **Table Role** parameter, leave the field empty or provide a value if you have one. This parameter only accepts one role value.

By default, the **Table Role** field is empty. You must create a new custom role in ServiceNow to specifically manage the Security Command Center Enterprise tickets. Only ServiceNow users granted this new custom role have access to the Security Command Center Enterprise tickets.

If you already have a dedicated role for users who manage incidents in ServiceNow and you'd like to use this role for managing the Security Command Center Enterprise findings, enter the existing ServiceNow role name in the **Table Role** field. For example, if you provide the existing `incident_handler_role` value, all of the users who are granted the `incident_handler_role` role in ServiceNow can access the Security Command Center Enterprise tickets.

  10. Click **Execute**. Wait until the action is completed.




#### Configure ServiceNow custom ticket layout

To ensure that the ServiceNow web interface accurately displays the updates related to cases and case comments, complete the following steps:

  1. In your ServiceNow administrator account, go to the **All** tab.
  2. In the **Search** field, enter `SCC Enterprise`.
  3. In the drop-down list, select the **SCC Enterprise Cloud Posture Ticket** and run a search.
  4. Select the **Posture Test Ticket**. The ServiceNow ticket layout page opens.
  5. At the ServiceNow ticket layout page, go to **Additional actions > Configure > Form Layout**.
  6. Go to the **Form view and section** section.
  7. In the **Section** field, select **u_scc_enterprise_cloud_posture_ticket**.
  8. Click **Save**. After the page updates, the ticket template has fields that are distributed into two columns.
  9. Go to **Additional actions > Configure > Form Layout**.
  10. Go to the **Form view and section** section.
  11. In the **Section** field, select **Summary**.
  12. Click **Save**. After the page updates, the ticket template displays the new Summary structure.



### Configure ServiceNow integration

  1. In the Google Cloud console, go to **Response > Playbooks** to open the Security Operations console navigation.
  2. In the Security Operations console navigation, go to **Response > Integrations Setup**.
  3. Select the **Default Environment**.
  4. In the integration **Search** field, enter `ServiceNow`. The **ServiceNow** integration returns as a search result.
  5. Click settings **Configure Instance**. The dialog window opens.
  6. To configure the **API Root** parameter, enter the API root of your ServiceNow instance, such as `https://INSTANCE_NAME.service-now.com/api/now/v1/`

  7. To configure the **Username** parameter, enter the username that you use to sign in to ServiceNow. Don't use your admin credentials.

  8. To configure the **Password** parameter, enter the password that you use to sign in to ServiceNow. Don't use your admin credentials.

  9. Click **Save**.

  10. To test your configuration, click **Test**.




### Enable the Posture Findings With SNOW playbook

  1. In the Google Cloud console, go to **Response > Playbooks**.
  2. In the Playbook **Search** bar, enter `Generic`.
  3. Select the **Posture Findings - Generic** playbook. This playbook is enabled by default.
  4. Switch the toggle to **disable the playbook**.
  5. Click **Save**.
  6. In the Playbook **Search** bar, enter `SNOW`.
  7. Select the **Posture Findings With SNOW** playbook. This playbook is disabled by default.
  8. Switch the toggle to **enable the playbook**.
  9. Click **Save**.



## Enable case data synchronization

Security Command Center automatically synchronizes the information between a case and its corresponding ticket, ensuring matching priority, status, comments, and other relevant data between a case and its ticket.

To synchronize case data, Security Command Center uses internal automatic processes called synchronization jobs. The **Sync SCC-Jira Tickets** and **Sync SCC-ServiceNow Tickets** jobs synchronize case data between Security Command Center and integrated ticketing systems. Both jobs are initially disabled and require you to enable them to initiate automatic case data synchronization.

Closing a case automatically resolves the corresponding ticket. Resolving a ticket in Jira or ServiceNow triggers the synchronization jobs to close the case too.

### Before you begin

To enable case synchronization, you must be granted any of the following SOC roles on the **SOAR settings** page:

  * Administrator
  * Vulnerability Manager
  * Threat Manager



For more details about SOC roles and permissions required for users, see [Control access to features in Security Operations console pages](https://docs.cloud.google.com/security-command-center/docs/configure-secops-users).

### Enable synchronization for ticketing systems

To ensure that the information in cases and tickets is automatically synchronized, enable the synchronization job that is relevant to the ticketing system that you integrated with.

To enable the synchronization job, complete the following steps:

  1. In the Google Cloud console, go to Security Command Center.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/overview)

  2. In the navigation menu, click **Response > Playbooks**. The **Playbooks** page opens in the Security Operations console.

  3. Click **Response > JobScheduler**.

  4. Choose the correct synchronization job:

     * If you integrated with Jira, select **Sync SCC-Jira Tickets** job.

     * If you integrated with ServiceNow, select **Sync SCC-ServiceNow Tickets** job.

  5. Switch the toggle to enable the selected job.

  6. Click **Save** to enable Security Command Center automatically synchronize case data with a ticketing system.




## Create tickets for existing cases

Security Command Center automatically creates tickets only for cases opened after you have integrated with a ticketing system and does not retroactively attach new playbooks to existing alerts. To create tickets for cases opened before integrating with a ticketing system, use one of the following approaches:

  * Close a case that has no ticket and wait until SCC reingests findings and assigns a new playbook to the case alerts.

  * Manually add a playbook to any alert in a case that was opened before you integrated with a ticketing system.




### Close a case with no ticket

To close a case that has no ticket, complete the following steps:

  1. In the Google Cloud console, go to Security Command Center.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/overview)

  2. In the navigation, click **Risk > Cases**. The **Cases** page opens in the Security Operations console.

  3. Click ![](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Open Filter**. The **Case queue filter** panel opens.

  4. In the **Case queue filter** , specify the following:

     1. In the **Time Frame** field, specify time period for open cases.
     2. Set **Logical operator** to **AND**.
     3. For the first value under **Logical operator** , select **Tags**.
     4. Set the condition to **IS**.
     5. For the second value, select **Internal-SCC-Ticket-Info**.
     6. Click **Apply** to update cases in the case queue and show only the cases that match the filter you specified.
  5. From the case queue, select the case.

  6. In the **Case view** , select ![](https://docs.cloud.google.com/static/security-command-center/images/close-case.svg)**Close Case**. The **Close Case** window opens.

  7. In the **Close Case** window, specify the following:

     1. Select a value for the **Reason** field to state the reason for closing the case.

     2. Select a value for the **Root Cause** field to state the cause for closing the case.

     3. Optional: Add a comment.

     4. Click **Close** to close the case. Security Command Center then reingests findings into a new case and automatically attaches a correct playbook to them.




### Manually add a playbook to an alert

To manually attach a playbook to an alert in an existing case, complete the following steps:

  1. In the Google Cloud console, go to Security Command Center.

[Go to Security Command Center](https://console.cloud.google.com/security/command-center/overview)

  2. Click **Risk > Cases**. The **Cases** page opens in the Security Operations console.

  3. Click ![](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg)**Open Filter**. The **Case queue filter** panel opens.

  4. In the **Case queue filter** , specify the following:

     1. In the **Time Frame** field, specify time period for open cases.
     2. Set **Logical operator** to **AND**.
     3. For the first value under **Logical operator** , select **Tags**.
     4. Set the condition to **IS**.
     5. For the second value, select **Internal-SCC-Ticket-Info**.
     6. Click **Apply** to update cases in the case queue and show only the cases that match the filter you specified.
  5. From the case queue, select the case.

  6. Select any alert contained in a case.

  7. In an alert view, go to the **Playbooks** tab.

  8. Click **add Add Playbook**. The **Add a Playbook** window with a list of available playbooks appears.

  9. In the search field of the **Add a Playbook** window, enter `Posture Findings`.

     * If you integrated with Jira, select the **Posture Findings With Jira** playbook.
     * If you integrated with ServiceNow, select the **Posture Findings With SNOW** playbook.
  10. Click **Add** to add a playbook to an alert.




Upon completion, the playbook creates a ticket for a case and automatically populates the ticket with information from the case.

Adding a playbook to a single alert within a case is sufficient to create a ticket and trigger data synchronization.

## What's next

  * Learn how to [determine ownership for posture findings](https://docs.cloud.google.com/security-command-center/docs/determine-ownership-posture-findings).

  * Learn how to [group findings in cases](https://docs.cloud.google.com/security-command-center/docs/group-findings-in-cases).

  * Learn how to [assign tickets based on posture cases](https://docs.cloud.google.com/security-command-center/docs/assign-itsm-tickets).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
