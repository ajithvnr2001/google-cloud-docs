---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-collaborator-user/
title: Create a collaborator user \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:25:42.363372+00:00
---

# Create a collaborator user  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/user-soar-only/create-a-collaborator-user/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a collaborator user

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This page only applies to customers who haven't migrated to Google Cloud. After completing Stage 1 of the migration, see [Feature RBAC using Cloud IAM](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role) to manage roles and permissions for Google SecOps including SOAR.

This document outlines the procedure for an administrator to add Collaborator users to the Google Security Operations platform. This user type is essential when you need to grant controlled access and assign specific, scoped tasks to an internal stakeholder or an external partner, such as a Managed Security Service Provider (MSSP) customer.

The high-level steps to add these users are the same as adding regular users:

  1. Purchase the license for the required number of Collaborator users with your Account Managers.
  2. Create a new **Collaborator** permissions group or use the predefined **Collaborator** group.
  3. Create a new user.



## Benefits of adding a Collaborator user

The Collaborator user in the Google Security Operations platform is designed for external partners (like a Managed Security Service Provider [MSSP]) or internal stakeholders who need specific, controlled access to investigations. It blends the permissions of a basic user and a view-only role. 

This model facilitates joint investigations and real-time case collaboration with customers or end users by granting granular, module-specific permissions (either `view-only` or `edit`).

## Key permissions and features

The SOC Manager can assign `view-only` or `edit` access to the Collaborator user across the following platform modules:

  * **Case management** : Access to specific cases with an Alert view customized for the Collaborator's role. 
  * **Playbook Execution** : Direct participation in automated workflows:
    * Manual actions (or entire Playbook blocks) can be assigned to the Collaborator.
    * Assigned tasks appear in the Collaborator's **Workdesk** and the **Pending Actions** widget.
    * The Playbook action supports direct, targeted messaging to the Collaborator.
  * **Data visibility** : Access to platform-wide operational and security data: 
    * **Dashboards** : Collaborators can view metrics, trends, and key performance indicators (KPIs) related to security operations. This information lets them monitor the overall health of the environment without the ability to modify the underlying data or settings. 
    * **Search** : Collaborators can execute queries to investigate security events, review logs, and identify Indicators of Compromise (IoCs). This tool supports threat hunting and gathering data for active incidents.
    * **Cases:** Collaborators with case access view an alert screen specifically tailored to their role. For information about how to define customized alerts, see [Define customized alert views from the playbook designer](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/define-customized-alert-views-from-playbook-designer).
  * **Entity Explorer** : Collaborators can view detailed entity information (users, endpoints, IP addresses, files), including the entity's timeline, associated alerts, and relationships to other objects. This information is critical for scoping an incident and identifying lateral movement.
  * **Reports** : Collaborators can view pre-generated reports on vulnerability scans, compliance audits, and incident summaries.
  * **Command Center** : Access shows a consolidated, real-time overview of all security operations. This overview includes a live feed of alerts, a summary of active cases, and key metric dashboards.
  * **SLA** : The Service Level Agreement (SLA) view lets Collaborators track the security team's performance against defined response and resolution targets. This information provides visibility into operational efficiency and confirms timely handling of security events per established agreements.
  * **Workdesk:** SOC managers can assign a manual action or an entire Playbook block to a Collaborator, along with a targeted message in the action. The Collaborator views the assigned task and message in their **Workdesk** and the **Pending Actions** widget.For more information on how to assign an action to a collaborator, see [Assign actions and playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks).  
For more information on how to assign an action to a collaborator, see [Assign actions and playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks).
  * **Workdesk: My Requests** : Collaborators access **My Requests** to submit predefined service requests.  
For details on how to define requests for collaborator users, see [Define requests for users](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/define-requests-for-users-admin).  
For details on how to choose a specific request as a collaborator user, see [Fill out a request](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/filling-out-request-from-workdesk).  




## View license details

To view license details, follow these steps:

  1. Arrange a license for the required number of collaborator users.
  2. Go to **Settings > Organizations > License Management** to view the details.



## Set up a permission group

To configure a permissions group to define the platform modules a collaborator user can access, follow these steps:

  1. Go to **Settings > Organization > Permissions**.
  2. Click the predefined **Collaborators** permissions group, or create a new one.
  3. Select the **Landing Page** type from the list. **Note:** The default landing page for Collaborators is **Homepage > Pending Actions**. The administrator can define any other permitted module as the Collaborator's landing page.
  4. Select the required modules the group needs access to.
  5. Click **Save**.



## Create a collaborator user (SOAR standalone customers only)

To create a collaborator user, follow these steps:

  1. Go to **Settings > Organization > User Management**.
  2. Click add **Add**.
  3. In the **Add User dialog** , select the following:
     1. In the **License Type** field, select the **Collaborator**.
     2. In the **Permission Group** list, select **Collaborator** or any new group that you created which is for collaborator users.
  4. Click **Add**.



An invitation to join Google SecOps SOAR is sent automatically to the collaborator user. Their status remains **Pending** until they accept the invitation and create a password.

## What's next

  * To assign tasks, see [Assign actions and playbook blocks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/assign-actions-and-playbook-blocks).
  * To configure the requests form, see [Create user requests](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/define-requests-for-users-admin).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
