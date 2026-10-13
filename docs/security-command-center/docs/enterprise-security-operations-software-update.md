---
url: https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update/
title: Update the Enterprise use case \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:47.335288+00:00
---

# Update the Enterprise use case  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/enterprise-security-operations-software-update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Update the Enterprise use case Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The December 18, 2024 update of the **SCC Enterprise – Cloud Orchestration and Remediation** use case is now available. Update the use case at your earliest convenience.

This use case provides updates to the security operations features of the Enterprise tier of Security Command Center. To apply the updates, follow the procedures on this page.

The update procedure includes the following high-level steps:

  1. Prepare the system for update by disabling a connector and deleting certain existing playbooks.
  2. Install the latest version of the **SCC Enterprise – Cloud Orchestration and Remediation** use case.
  3. Validate the installation and run the updated playbooks.



These steps are performed using the **Settings > SOAR settings** Security Operations console page.

## Confirm that you have the required roles

To complete this procedure, you must be granted any of the following SOC roles in the Security Operations console:

  * Administrator
  * Vulnerability Manager
  * Threat Manager



For more details about SOC roles and permissions required for users to access Security Operations console pages, see [Control access to features in Security Operations console pages](https://docs.cloud.google.com/security-command-center/docs/configure-secops-users).

## Prepare the system for the update

Before updating the use case, you need to disable the **SCC Enterprise – Urgent Posture Findings Connector** and delete the playbooks provided by the current use case version.

### Disable the connector

To avoid having alerts with no playbooks attached, disable the **SCC Enterprise – Urgent Posture Findings Connector** connector before deleting playbooks. Security Command Center ingests findings collected while the connector is disabled when you update and enable the connector.

To disable the connector, complete the following steps:

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Ingestion > Connectors**.
  2. Under the **SCCEnterprise** , select **SCC Enterprise – Urgent Posture Findings Connector**.
  3. Switch the toggle to disable the connector.
  4. Click **Save**.



### Delete playbooks

To avoid playbook duplication, delete default playbooks that you use in the current version of your use case. Deleting playbooks before upgrading the use case has no impact on the case management.

To delete default playbooks, complete the following steps:

  1. In the Security Operations console navigation, go to **Response > Playbooks**. The drop-down filter is set to **Show All** by default.

  2. Select the **Siemplify Use Cases** folder. This folder contains the following default playbooks:

     * **AWS Threat Response Playbook**
     * **GCP Threat Response Playbook**
     * **IAM Recommender Response**
     * **Posture Findings – Generic**
     * **Posture Findings – Generic – VM Manager**
     * **Posture Findings With Jira**
     * **Posture Findings With ServiceNow**
     * **Google Cloud – Execution – Cryptomining**
     * **Google Cloud – Execution – Binary or Library Loaded Executed**
     * **Google Cloud – Execution – Malicious URL Script or Shell Process**
     * **Google Cloud – Persistence – Suspicious Behaviour**
     * **Google Cloud – Persistence – IAM Anomalous Grant**
     * **Posture – Toxic Combination Playbook**
     * **Preview – Azure Threat Response Playbook**
  3. In the **Playbooks** page navigation, click ![](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/multiple-selection.svg)**Edit** to select multiple items.

  4. Next to **Siemplify Use Cases** , click **done_all Select all** to select all playbooks and blocks in the folder.

  5. In the **Playbooks** page navigation, click **list Menu > Delete**. A window appears that requires you to confirm or cancel the deletion of selected playbooks.

  6. Click **Confirm**.

Now you can update your use case version.




## Install the Security Command Center Enterprise use case

To install the latest version SCC Enterprise use case to the latest version and check that all integrations provided in the use case are up to date.

### Install the latest use case

To install the latest version of the **SCC Enterprise – Cloud Orchestration and Remediation** use case, complete the following steps:

  1. In the Security Operations console navigation, go to **Marketplace > Use Cases**.
  2. Open the **Filter by categories** dialog by clicking the filter icon, ![](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/filter.svg).
  3. In the **Filter by categories** dialog, type `SCC Enterprise`. The use case appears in the **Use Cases** section.
  4. In the description of the **SCC Enterprise – Cloud Orchestration and Remediation** use case, check for a date.

     * If the date is earlier than July 10, 2024, or there is no date in the description, delete the use case. The latest use case appears in place of the deleted use case automatically.
     * If the date in the **SCC Enterprise – Cloud Orchestration and Remediation** use case is July 10, 2024 or later, confirm that the playbooks in the latest use case are installed by completing the following steps:

       1. Click the use case to open the installation wizard.
       2. Expand the playbooks category and take note of any new or updated playbooks.
       3. On the **Response > Playbooks** page in the Security Operations console, search for the new or updated playbook. If you find the new or updated playbook, the use case installation is already complete.
  5. To complete the installation of the use case, click the **SCC Enterprise – Cloud Orchestration and Remediation** use case and follow the instructions in the installation wizard.




## Apply and validate configurations from the new use case

You need to validate that the various features that are included in the latest use case are updated correctly. For certain features, you need to apply the updates from new use case manually.

### Validate integration versions in the use case

The new versions of integrations included in the use case are available every week. Update the integrations to their latest versions at your earliest convenience.

The new versions of integrations introduce updates including, but not limited to, fixes, new widgets and actions, changes to existing widgets and actions, enhancements to alert handling, and improvements to detection processing logic and workflow mapping.

To apply the updates for integrations, complete the following steps:

  1. In the Security Operations console navigation, go to **Marketplace > Integrations**.
  2. In the **Type** field, select **All Integrations**.
  3. In the **Status** field, select **Available Upgrade**. All of the integrations that require an upgrade are displayed.
  4. To upgrade an integration, click ![](https://docs.cloud.google.com/static/security-command-center/images/icons-uno/updates.svg)**Upgrade to version VERSION** in the integration card.
  5. If the **Updating INTEGRATION** dialog appears, click **Confirm**.
  6. If the **Confirmation** dialog appears, click **Approve**.
  7. In the **Confirm Overwrite Mapping** dialog, select the following option: **Install the new ontology configuration and override the existing one** , and then click **Confirm**.



Upgrading the **SCC Enterprise** integration and installing the new ontology configuration for all upgraded integrations is required.

#### Configure the Cloud Storage integration

To remediate the public bucket ACL findings, the **SCC Enterprise – Cloud Orchestration and Remediation** use case includes an additional integration, the Cloud Storage integration.

To let the playbooks enrich and remediate the `PUBLIC BUCKET ACL` finding type, configure the Cloud Storage integration by completing the following steps:

  1. Configure the integration parameters.
  2. Enable the public bucket remediation for playbooks.



##### Configure the integration parameters

To configure the Cloud Storage integration parameters, complete the following steps:

  1. In the Security Operations console navigation, go to **Marketplace > Integrations**.
  2. In the **Search** field, enter `Storage`. The Cloud Storage integration card appears.
  3. On the integration card, click **Configure**. The configuration dialog opens.
  4. Configure the **Workload Identity Email** , **Project ID** , and **Quota Project ID** parameters. You can copy the parameter values from any other Google Cloud integration, such as the Cloud Asset Inventory integration.
  5. Click **Save**.
  6. Click **Test** to test the configuration.



##### Enable the public bucket remediation for playbooks

To enable the public bucket remediation for the posture findings playbooks, see [Enable public bucket remediation](https://docs.cloud.google.com/security-command-center/docs/playbooks-public-bucket-acl).

### Update case view widgets

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Case Data > Views**.
  2. Select **Default Case View**.
  3. Select the **Predefined** tab.
  4. Drag the widgets from the **Predefined** tab into the **Default Case View** in the following recommended order:

     1. Case Summary
     2. Toxic combination attack path
     3. Findings
     4. AI Investigation/Gemini Summary
     5. Finding Summary
     6. SCC – Finding State
     7. Impacted Assets
     8. Ticket Information
     9. Pending Actions
     10. Entities Graph
     11. Entities Highlights
  5. Click **Save View**.




#### Validate widgets

To ensure that you get the correct information, validate that the following widgets contain the correct condition:

  * **Toxic combination attack path**
  * **Finding**
  * **Entities Graph**
  * **AI Investigation/Gemini Summary**
  * **Finding Summary**
  * **Impacted Resources**
  * **SCC – Finding State**
  * **Impacted Assets**
  * **Impacted AWS Assets**



To validate the widgets, complete the following steps:

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Case Data > Views**.

  2. Select **Default Case View**.

  3. For both the **Toxic combination attack path** and **Finding** widgets, click **settings Configuration**.

Under **Advanced Settings** , in the **Conditions** section, the condition should be as follows: `[Case.Tags] () Toxic Combination`. If not, update the condition, and then click **Save**.

  4. For both the **Entities Graph** and **AI Investigation/Gemini Summary** widgets, click **settings Configuration**.

Under **Advanced Settings** , in the **Conditions** section, the condition should be as follows: `[Case.Tags] !() Toxic Combination`. If not, update the condition, and then click **Save**.

  5. For the **Finding Summary** widget, click **settings Configuration**.

Under **Advanced Settings** , in the **Conditions** section, the conditions should be as follows:

     * `[Case.Tags] () SCC-TICKET-INFO`
     * `[Case.Tags] !() Toxic Combination`
     * `[Case.Tags] !() CIEM`
     * `[Event.parentDisplayName] !() VM Manager`

If not, update the conditions, and then click **Save**.

  6. For the **Impacted Resources** widget, click **settings Configuration**.

Under **Advanced Settings** , in the **Conditions** section, the condition should be as follows: `[Case.Tags] () Toxic Combination`. If not, update the condition, and then click **Save**.

  7. For the **SCC – Finding State** widget, click **Delete**. When the confirmation dialog opens, click **Yes**.

To install the **SCC – Finding State** widget configured for the latest use case version, drag the **SCC – Finding State** widget from the **Predefined** tab into the **Default Case View**.

  8. For the **Impacted Assets** widget, click **Delete**. When the confirmation dialog opens, click **Yes**.

To install the **Impacted Assets** widget configured for the latest use case version, drag the **Impacted Assets** widget from the **Predefined** tab into the **Default Case View**.

  9. For the **Impacted AWS Assets** widget, click **Delete**. When the confirmation dialog opens, click **Yes**.

  10. Click **Save View**.




### Enable playbooks

To enable playbooks for processing vulnerabilities and misconfigurations, complete the following steps:

  1. In the Security Operations console navigation, go to **Response > Playbooks**.
  2. Select the **Siemplify Use Cases** folder.

If you didn't integrate with ticketing systems, ensure that the **Posture Findings – Generic** is enabled. Enabling the **Posture Findings – Generic – VM Manager** playbook is optional.

If you integrated with ticketing systems, complete the following steps:

     1. Select the **Posture Findings – Generic** playbook.
     2. Switch the toggle to disable it.
     3. Click **Save**.
     4. Select the **Posture Findings – Generic – VM Manager** playbook.
     5. Switch the toggle to disable it.
     6. Click **Save**.
     7. If you integrated with Jira, select the **Posture Findings With Jira** playbook. 
        1. Switch the toggle to enable the playbook.
        2. Click **Save**.
     8. If you integrated with ServiceNow, select the **Posture Findings with SNOW** playbook. 
        1. Switch the toggle to enable the playbook.
        2. Click **Save**.



### Update connectors

Updating the use case doesn't update existing connectors automatically. To ensure that data ingestion works as expected after the use case update, update the **SCC Enterprise – Urgent Posture Findings Connector** and **Google Chronicle – Chronicle Alerts Connector** connectors.

To update the **SCC Enterprise – Urgent Posture Findings Connector** connector, complete the following steps:

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Ingestion > Connectors**.
  2. Under **SCCEnterprise** , select **SCC Enterprise – Urgent Posture Findings Connector**. The connector parameters configuration page opens.
  3. Click cached **Update**.
  4. Set the **Run Every** parameter to 1 minute.
  5. Switch the toggle to enable the connector.
  6. Click **Save**.



To update the **Google Chronicle – Chronicle Alerts Connector** connector, complete the following steps:

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Ingestion > Connectors**.
  2. Under **GoogleChronicle** , select **Google Chronicle – Chronicle Alerts Connector**. The connector parameters configuration page opens.
  3. Click cached **Update**.
  4. Set the **Run Every** parameter to 1 minute.
  5. In the **Product Field Name** parameter field, enter `SCCE`.
  6. Switch the toggle to enable the connector.
  7. Click **Save**.



## Verify the update configuration

To ensure that all use case components are updated successfully, test the connector and job.

### Test the connector

  1. In the Security Operations console navigation, go to **Settings > SOAR Settings > Ingestion > Connectors**.
  2. Under the **SCCEnterprise** , select **SCC Enterprise – Urgent Posture Findings Connector**.
  3. Go to the **Testing** tab.
  4. Click **Run connector once**. If the connector configuration is correct, the checkmark appears.



### Test the job

  1. In the Security Operations console navigation, go to **Response > Job Scheduler**.
  2. Under **GoogleSecurityCommandCenter** , select **Sync SCC Data**.
  3. Click **Run Now**. If the job works as expected, the job status is `Success`.



## Troubleshooting

  * The **Sync SCC Data** job displays the following error:
        
        TIPCommon.exceptions.JobSetupError: Resource already exists in the project (resource={identifier}_topic)
        

Wait for ten minutes and click **Run Now**. If the error persists, complete the following steps:

    1. In the job **Parameters** section, delete the **Organization ID** parameter value.
    2. Enter the **Organization ID** parameter value.
    3. Click **Save**.
    4. Click **Run Now**.
  * The **Sync SCC Data** job displays an authentication error when it failed to update automatically during the use case update. To fix the synchronization job issue, manually enter the values for the **Project ID** and **Quota Project ID** parameters.

To specify the correct parameter values, complete the following steps:

    1. Go to **Settings > SOAR Settings > Ingestion > Connectors**.
    2. Under **SCCEnterprise** , select **SCC Enterprise – Urgent Posture Findings Connector**.
    3. In the **Parameters** section, copy the value of the **Quota Project ID** parameter.
    4. Go to **Response > Job Scheduler**.
    5. Under **SCCEnterprise** , select **Sync SCC Data**.
    6. In the **Parameters** section of the **Sync SCC Data** job, enter the copied value in the **Project ID** and **Quota Project ID** fields.
    7. Click **Save**.
  * After the use case update, new playbooks don't apply to existing alerts.

To apply the new playbooks to existing alerts and rerender the **Alert** widget, close a case and wait until the connector ingests alerts again with the new playbooks attached.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
