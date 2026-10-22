---
url: https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs/
title: Collect SOAR platform logs \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:47.642906+00:00
---

# Collect SOAR platform logs  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/secops/collect-secops-soar-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Collect SOAR platform logs

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

You can manage and monitor Google Security Operations SOAR logs in the [Google Cloud Logs Explorer](https://docs.cloud.google.com/logging/docs). You can also use Google Cloud tools to set up special metrics and alerts that are triggered by specific events in your SOAR operation logs.

The logs capture essential data from SOAR's Extract, Transform, Load (_ETL_), _playbook_ , and _Python_ functions. The logs capture data types including the running of Python scripts, alert ingestion, and playbook performance.

## Enable SOAR log collection

Google SecOps provides operational logs for SOAR activities, including playbook executions, connector runs, and Python script outputs.

  * **Google SecOps (SIEM + SOAR Unified):** By default, the system enables collection of SOAR logs. The platform automatically configures log sinks to route these logs to Cloud Logging in your Google Cloud project. You don't need to perform any manual configuration.

  * **SOAR Standalone:** You must manually configure a service account and provide the credentials to Google SecOps Support to enable log export. See the following section for instructions.


**Note:** To view these logs, you must have the Logs Viewer (`roles/logging.viewer`) IAM role on your Google Cloud project.

The system automatically routes SOAR logs to the `_Default` cloud logging bucket. Because this incurs costs, Google recommends setting up exclusion filters to drop low-value logs or to adjust retention periods. For more information on collecting logs and setting up filters, see [Logging overview](https://docs.cloud.google.com/logging/docs/routing/overview).

### Set up SOAR logs for SOAR Standalone

To set up SOAR log collection for SOAR Standalone, follow these steps:

  1. Create a Service Account in the Google Cloud project where you plan to view the logs. For details, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

  2. In the Google Cloud console, go to **IAM & Admin > IAM**. 

[Go to IAM](https://console.cloud.google.com/iam-admin/iam)

  3. Locate the Service Account you created and click edit **Edit principal**.

  4. In the **Assign Roles** section, add the **Logs Writer** role. For more information, see the [predefined Logs Writer role](https://docs.cloud.google.com/logging/docs/access-control#logging.logWriter).

  5. Click **Save**.

  6. Go to **IAM & Admin > Service Accounts**.

  7. Select the service account you created.

  8. Click more_vert **More** and select **Manage Permissions**.

  9. In the **Permissions** section, click **Grant Access**.

![Grant access in Permissions section.](https://docs.cloud.google.com/static/chronicle/images/soar/logsgrantaccess.png)

  10. In the **New principals** field, add the following principal: `gke-init-backgroundservices@{SOAR-GCP-Project-Id}.iam.gserviceaccount.com`

Replace `{SOAR-GCP-Project-Id}` with your SOAR Google Cloud Project ID. If you don't know the `SOAR-GCP-Project-Id`, submit a ticket through [Google Support](https://console.cloud.google.com/support).

**Note:** Organization policies might restrict access to external service accounts due to Domain Restriction Sharing. If this occurs, you must add an allowlist exception for the mentioned principal. For more information, see [Restricting Domains: Configure Exceptions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains#configure-exceptions).
  11. In **Assign Roles** , select **Service Account Token Creator**. For more information, see [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role).

  12. Click **Save**.

  13. Provide the name of the configured Service Account to the Google SecOps support team.




## Access Google SecOps SOAR logs

Google SecOps writes SOAR logs in a separate namespace called `chronicle-soar` and categorizes them by the service that generated the log.

To access Google SecOps SOAR logs, do the following:

  1. In the Google Cloud console, go to **Logging** > **Logs Explorer**. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select the Google SecOps Google Cloud project.

  3. Enter the following filter in the query field and click **Run Query** :
         
         resource.labels.namespace_name="chronicle-soar"
         

![Logs Explorer showing a filter for the chronicle-soar namespace.](https://docs.cloud.google.com/static/chronicle/images/soar-logs-filter.png)

  4. To filter logs from a specific service, enter the following filters in the query field and click **Run Query** :
         
         resource.labels.namespace_name="chronicle-soar"
         resource.labels.container_name="<CONTAINER_NAME>"
         

Replace `<CONTAINER_NAME>` with the relevant service container: `playbook`, `python`, or `etl`.




## Playbook step debugging

You can view execution logs for an individual playbook step directly from the **Playbook** tab in the **Cases** page. This lets you inspect the logic and outcome of every step, regardless of its execution status.

To view logs for a specific step:

  1. In the **Case View** , open the **Playbook** tab.
  2. Select a step to view its results.
  3. Click **View Logs Explorer**.

**Note:** You must have the Logs Viewer (`roles/logging.viewer`) IAM role on your Google Cloud project to view the logs.

The link opens the **Logs Explorer** in the Google Cloud console with a pre-configured filter for the specific execution ID of that step.

**Note:** It can take up to 5 minutes for logs to synchronize and appear in the Logs Explorer.



## Filter logs using labels

Log labels provide an efficient and convenient way to refine a query scope. You can find all labels in the `labels` section of each log message.

![Log labels shown within a log message in Logs Explorer.](https://docs.cloud.google.com/static/chronicle/images/soar-labels.png)

To narrow the log scope, expand the log message, right-click each label, and hide or show specific logs:

![Filtering options available when right-clicking a label in Logs Explorer.](https://docs.cloud.google.com/static/chronicle/images/soar-labels-filtering.png)

### Playbook log labels

The following labels are available for the playbooks:

  * `playbook_definition`
  * `playbook_name`
  * `block_name`
  * `block_definition`
  * `case_id`
  * `correlation_id`
  * `integration_name`
  * `action_name`

**Note:** Use the `correlation_id` label to retrieve all logs from both the playbook and associated Python services. This provides complete tracing and analysis of an entire playbook execution.

### Python log labels

The following labels are available for the Python service, filtered by `resource.labels.container_name="python"`:

**Integration and Connector labels**

  * `integration_name`
  * `integration_version`
  * `connector_name`
  * `connector_instance`



**Job labels**

  * `integration_name`
  * `integration_version`
  * `job_name`



**Action labels**

  * `integration_name`
  * `integration_version`
  * `integration_instance`
  * `correlation_id`
  * `action_name`



### ETL log labels

The following labels are available for the ETL service, filtered by `resource.labels.container_name="etl"`:

  * `correlation_id`



For example, to trace the ingestion flow for an alert, filter by `correlation_id`:

![Example filter in Logs Explorer using correlation_id for ETL logs.](https://docs.cloud.google.com/static/chronicle/images/soar-etl-filter.png)

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
