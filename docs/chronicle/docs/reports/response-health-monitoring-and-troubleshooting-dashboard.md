---
url: https://docs.cloud.google.com/chronicle/docs/reports/response-health-monitoring-and-troubleshooting-dashboard/
title: Monitor response and playbook health \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:35:28.665556+00:00
---

# Monitor response and playbook health  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/response-health-monitoring-and-troubleshooting-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor response and playbook health

Supported in:

Google SecOps 

This guide is for security engineers, SOAR engineers, and Security Operations Center (SOC) managers who want to monitor the health, performance, and automation efficiency of their playbooks and integrations within Google Security Operations. It explains how to use the Response Health Hub to identify, diagnose, and remediate issues affecting playbook execution, action latency, and third-party integrations.

The Response Health Hub is the central location in Google SecOps for monitoring the operational status and effectiveness of your automated response workflows across environments. It provides comprehensive visibility into playbook execution volumes, queue backlogs, attachment and rerun rates, action-level latency, and failure diagnostics.

The Response Health Hub includes the following information:

  * Playbook execution volumes, queue backlogs, and completion success rates
  * Playbook attachment and re-execution (rerun) rates across cases and alerts
  * End-to-end playbook and action execution latency metrics, including the slowest individual playbook and action runs
  * Playbook and integration health metrics, including failed playbook summaries, terminated playbooks, failure trends over time, and action failure reasons
  * Integration and action utilization rankings, automated versus manual closure rates, and Mean Time to Resolve (MTTR) comparisons



## Key terminology

  * **Response Health Hub** : The central interface within Google SecOps for monitoring the status, execution latency, automation effectiveness, and health of playbooks and integrations.
  * **Playbook execution time** : The total end-to-end elapsed duration of a playbook run, measured from when the playbook is first triggered and attached to an alert or case until all steps finish. This duration includes action executions, step transitions, queue delays, and waiting time for manual user actions.
  * **Action execution time** : The active execution duration of an individual action within a playbook, measured from when the action starts running until its result is saved.
  * **Attached playbook** : A playbook that is triggered and linked to a case or alert when the alert is ingested or created.
  * **Rerun playbook** : A playbook execution that is re-triggered on a case or alert where that playbook was already attached.
  * **Faulted** : Describes a playbook action that encountered an error or timeout during execution (such as `FAULTED`, `FAULTED_AND_SKIPPED`, `UNHANDLED_TIMEDOUT`, or `PENDING_ACTION_TIMEOUT`).
  * **Terminated** : Describes a playbook run (`TERMINATED`) that was manually stopped by an analyst or whose associated alert or case was closed before the playbook finished executing.
  * **Mean Time to Resolve (MTTR)** : The average elapsed time, in minutes, from when a case is created until it is closed. The Response Health Hub compares MTTR for cases closed automatically by playbooks (`AUTOMATIC`) against cases closed manually by analysts.



## Before you begin

Before you use the Response Health Hub, confirm that you are assigned a role that includes the necessary Identity and Access Management (IAM) and SOAR permissions for viewing dashboards and playbook data. If you can't access the Response Health Hub, contact your administrator.

### Standard predefined roles

Access to Response Health Hub features is included in the following [predefined IAM roles](https://docs.cloud.google.com/chronicle/docs/onboard/configure-feature-access#overview-perm-role):

  * **Chronicle API Admin** (`roles/chronicle.admin`)
  * **Chronicle API Editor** (`roles/chronicle.editor`)
  * **Chronicle API Viewer** (`roles/chronicle.viewer`)



### Specific permissions and SOAR roles

Viewing the Response Health Hub requires the following IAM permissions and SOAR role access:

  * **Required IAM permissions** : 
    * `chronicle.nativeDashboards.get` and `chronicle.nativeDashboards.list` to view curated dashboards
    * `chronicle.playbooks.read` to view playbook execution and health metrics
    * `chronicle.nativeDashboards.create` and `chronicle.nativeDashboards.duplicate` to duplicate and customize the dashboard
  * **SOAR roles** : Users also need a SOAR role with permissions to view playbooks and dashboards, such as **ChronicleSOAR Admin** , **ChronicleSOAR Threat Manager** , **ChronicleSOAR Vulnerability Manager** , or **ChronicleSOAR Observer**. For more information, see [Manage playbook permissions](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/playbook-permissions).



## Access the Response Health Hub

  * In the navigation menu, click **Dashboards & Reports** > **Dashboards** , and then select **Response Health Hub** under the predefined curated dashboards list.



The Response Health Hub is a read-only [curated dashboard](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards) and can't be modified directly. To customize the charts or queries, duplicate the Response Health Hub and modify the copied dashboard for your specific use case.

### Filter the Response Health Hub

You can refine the data displayed across the Response Health Hub using the following dashboard-level filters at the top of the page:

  * **Global Time Filter** : Filters dashboard widgets by the selected time range (default: `Past 7 days`).

**Note:** The **Playbooks Pending in Queue** widget displays the current queue count over a fixed 7-day lookback window and isn't affected by the **Global Time Filter**.
  * **Playbook Simulated** : Filters playbook metrics by whether the runs were executed in the playbook simulator (`playbook.simulated`). By default, this filter is set to `false` so that the dashboard displays only live playbook executions. Set this filter to `true` to inspect simulated test runs.

  * **Execution Scope Filter** : Filters metrics by the playbook execution scope (`playbook.metadata.execution_scope`).

  * **Environments Filter** : Filters dashboard widgets by one or more Google SecOps environments (`playbook.metadata.environments` and `case.environment`). By default, this filter is set to `Default Environment` and supports selecting multiple environments simultaneously.




## Understand and use the Response Health Hub interface

This section describes the sections and widgets in the Response Health Hub so that you can monitor playbook performance and diagnose issues across your SOAR workflows.

The Response Health Hub is organized into the following sections:

  * **Volume & Adoption**
  * **Playbook Attachment Rates**
  * **Response Execution Time**
  * **Playbook Health**
  * **Integrations Utilization** and **Automation Effectiveness**



### Volume and adoption

The **Volume & Adoption** section provides high-level metrics on playbook execution volume, queue depth, and overall completion rates:

  * **Total Playbook Executions** : A big number widget showing the total number of playbook runs executed within the selected timeframe.
  * **Top 30 Most Executed Playbooks** : A horizontal bar chart ranking the top 30 playbooks by total execution count in the selected timeframe.
  * **Playbooks Pending in Queue** : A big number widget showing the current number of playbook runs with a status of `PENDING_IN_QUEUE` that are queued and awaiting execution.
  * **Playbook Execution Success Rate** : A pie chart showing the breakdown of finished playbook executions categorized by status (`COMPLETED` versus `FAILED`).
  * **Daily Playbook Execution Volume** : A line chart displaying the daily trend of total playbook runs over time, grouped by playbook display name.



### Playbook attachment rates

The **Playbook Attachment Rates** section tracks how frequently playbooks are attached to cases or alerts and how often they are re-executed:

  * **Avg Playbooks Attached per Case / Alert** : A big number widget showing the average number of playbook runs attached per distinct case or alert.
  * **Max Playbooks Attached per Case / Alert** : A big number widget showing the maximum number of unique playbooks attached to any single case or alert.
  * **Top Playbook Attachments / Reruns** : Ranks playbooks by attachment count and rerun frequency.



### Response execution time

The **Response Execution Time** section measures playbook and action latency to help you distinguish between active integration execution time and overall workflow wait time:

  * **Avg Playbook Execution Time** : A big number widget showing the average end-to-end duration (`Xh Ym Zs`) of completed playbook runs, from initial trigger and attachment until all steps finish. This includes action execution time, step transitions, queue delays, and manual user waiting time.
  * **Avg Execution Time by Playbook** : A bar chart displaying the average execution duration, in seconds, for each playbook.
  * **Avg Action Execution Time** : A big number widget showing the average active execution duration (`Xh Ym Zs`) across individual playbook actions, measured from when an action starts executing until its result is saved.
  * **Avg Execution Time by Action** : A bar chart displaying the average execution duration, in seconds, for each action (excluding internal loop markers `ForEachStartLoop` and `ForEachEndLoop`).
  * **Top 30 Slowest Playbook Executions** : Lists the 30 longest individual playbook runs.
  * **Top 30 Slowest Action Executions** : Lists the 30 longest individual action runs.



### Playbook health

The **Playbook Health** section provides diagnostics and trend charts for failed playbooks, terminated runs, and integration action errors:

  * **Latest 30 Failed Playbook Summary** : Lists the 30 most recent failed playbook runs (`FAILED`) along with the specific faulted action (`FAULTED`) and error message.
  * **Top 30 Failure Rate Playbooks** : Ranks the top 30 playbooks with the highest number of failed runs and their failure percentages.
  * **Top 30 Playbooks Terminated** : Tracks playbooks with the highest percentage of `TERMINATED` runs.
  * **Failed Playbooks % Over Time** : A line chart showing the daily trend of playbook failure percentages, grouped by playbook name.
  * **Failed Integrations % Over Time** : A line chart showing the daily trend of action failure percentages (`FAULTED` actions), grouped by integration.
  * **Actions Failure Rate** : Details action failure counts, failure rates, failure statuses, and the latest error messages for each integration and action.



### Integrations utilization and automation effectiveness

The **Integrations Utilization** and **Automation Effectiveness** sections highlight which tools your playbooks rely on most heavily and quantify the operational impact of automation on case closure and resolution times:

  * **Top 30 Most Frequently Used Integrations** : A bar chart ranking the top 30 integrations by total action executions across all playbooks (excluding internal `Loop` steps).
  * **Top 30 Most Frequently Used Actions** : A bar chart ranking the top 30 individual actions by execution count across all playbooks (excluding `ForEachStartLoop` and `ForEachEndLoop`).
  * **Case / Alert Closure Method (Auto vs. Manual)** : A donut chart showing the proportion of closed cases (`CLOSED`) that were resolved automatically by playbooks (`AUTOMATIC`) versus manually by SOC analysts.
  * **Case MTTR: Automated vs. Manual Closure** : A bar chart comparing the Mean Time to Resolve (MTTR, in minutes on a logarithmic scale) for cases closed automatically by playbooks versus cases closed manually.



## Identify and investigate playbook and integration issues

This section describes how to use the Response Health Hub to identify, investigate, and troubleshoot common playbook and integration issues.

**Note:** This section refers to Response Health Hub components and filters described in the interface section.

### Investigate failed playbook runs and faulted actions

When the **Playbook Execution Success Rate** or **Failed Playbooks % Over Time** chart indicates an increase in playbook failures, do the following:

  1. Go to the **Top 30 Failure Rate Playbooks** to identify which playbooks have the highest failure counts and failure percentages.
  2. View the **Failed Playbooks % Over Time** line chart to determine whether the failures started suddenly (for example, after a playbook edit or credential expiration) or represent a persistent issue.
  3. In the **Latest 30 Failed Playbook Summary** , locate recent runs for the failing playbook and review the **Action** , **Action Status** , and **Action Message** fields to see the exact step and error message that caused the playbook to fail.
  4. Click the **Case ID** link in the **Latest 30 Failed Playbook Summary** to open the affected case in a new tab.
  5. On the **Cases** page, select the alert, open the **Playbooks** tab, and click the playbook name to open the [playbook summary side drawer](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/understanding-playbook-monitoring#playbook-summary). From the **Errors** section of the drawer, you can inspect the full step logs and rerun the failed action or the entire playbook after addressing the root cause.



### Diagnose integration and action failures or timeouts

If multiple playbooks fail simultaneously, the root cause is often a shared third-party integration issue (such as expired API credentials, network connectivity problems, or rate limiting). To isolate integration-level issues, do the following:

  1. Review the **Failed Integrations % Over Time** chart to see if failure spikes correlate with a specific integration across your playbooks.
  2. In the **Actions Failure Rate** view, locate the affected integration and review the **Failure %** , **Failure Statuses** , and **Latest Failure Reasons** : 
     * `FAULTED` or `FAULTED_AND_SKIPPED`: Indicates that the action returned an execution error. Review **Latest Failure Reasons** for details such as `401 Unauthorized`, `403 Forbidden`, or invalid input parameters.
     * `UNHANDLED_TIMEDOUT`: Indicates that the action or remote agent timed out before completing execution.
     * `PENDING_ACTION_TIMEOUT`: Indicates that an asynchronous or manual pending action exceeded its configured waiting timeout before receiving a response.
  3. Navigate to **Response** > **IDE** or **Settings** > **SOAR Settings** > **Environments** to verify and test the integration instance configuration and credentials for the affected environment.



### Investigate playbook execution delays and queue backlogs

Slow response times can stem from either slow third-party integration actions or playbook waiting states and queue backlogs. To isolate the source of execution delays, do the following:

  1. **Check for queue backlogs** : View the **Playbooks Pending in Queue** widget in the **Volume & Adoption** section. A high number of queued playbooks indicates that incoming alerts are triggering playbooks faster than they can finish executing.
  2. **Compare playbook execution time with action execution time** : 
     * In the **Response Execution Time** section, compare **Avg Playbook Execution Time** with **Avg Action Execution Time**.
     * **Slow integration actions** : If **Avg Action Execution Time** is high, review the **Avg Execution Time by Action** chart and the **Top 30 Slowest Action Executions** to identify which specific integration actions are taking the longest to run. Click the **Case ID** link to inspect the specific case and alert where the slow action ran.
     * **Workflow waiting times or polling delays** : If **Avg Playbook Execution Time** is high while **Avg Action Execution Time** remains low, the delay is occurring between active action executions—most commonly because playbooks are waiting on manual analyst confirmation steps, pending asynchronous actions, or queue delays. Review **Avg Execution Time by Playbook** and **Top 30 Slowest Playbook Executions** to pinpoint the affected playbook runs.



### Optimize playbook triggers, reruns, and terminated runs

Inefficient trigger conditions or overly broad playbook designs can cause unnecessary executions, frequent reruns, or prematurely terminated playbooks. To optimize your playbook workflows, do the following:

  1. **Audit attachment and rerun counts** : 
     * View the **Avg Playbooks Attached per Case / Alert** and **Max Playbooks Attached per Case / Alert** widgets in the **Playbook Attachment Rates** section.
     * Review **Top Playbook Attachments / Reruns**. A high value in **Times Rerun** relative to **Times Attached** can indicate that analysts are repeatedly re-triggering a playbook due to transient action failures or incomplete enrichment data.
  2. **Investigate terminated playbooks** : 
     * Review **Top 30 Playbooks Terminated** in the **Playbook Health** section.
     * Playbooks are marked as `TERMINATED` when an analyst manually stops the playbook or when the underlying alert or case is closed before the playbook finishes running. If a playbook has a high **Percentage Terminated** , verify whether an automated closure rule or another playbook is closing the alert before long-running enrichment or containment steps complete.



### Evaluate SOC automation effectiveness and MTTR

To measure how effectively your playbooks reduce analyst workload and accelerate incident response, do the following:

  1. In the **Automation Effectiveness** section, review the **Case / Alert Closure Method (Auto vs. Manual)** donut chart to track the proportion of closed cases resolved automatically (`AUTOMATIC`) versus manually.
  2. Review the **Case MTTR: Automated vs. Manual Closure** bar chart to compare the average resolution time, in minutes, between automated closures and manual closures.
  3. Use the **Environments Filter** to compare automation closure rates and MTTR across different environments or tenants, and identify environments where additional auto-triage or auto-closure playbooks can reduce manual analyst handling time.



## Self-remediate playbook and integration health issues

To remediate common playbook and integration issues identified in the Response Health Hub, review the following symptoms, causes, and suggested remediations:

  * **Action status is`FAULTED` or `FAULTED_AND_SKIPPED` with authentication errors (`401` / `403`)**: 
    * **Cause** : The API key, token, or service account configured for the integration instance has expired or lacks required permissions.
    * **Suggested remediation** : Review **Latest Failure Reasons** in the **Actions Failure Rate** widget to identify the integration, update the credentials in your integration configuration for the affected environment, and test connectivity.
  * **Action status is`UNHANDLED_TIMEDOUT`**: 
    * **Cause** : The third-party endpoint took too long to respond, or the remote agent executing the action experienced connectivity or resource issues.
    * **Suggested remediation** : Check the health of the target service and [troubleshoot remote agents](https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/troubleshooting2) if the integration runs remotely. Consider increasing the action timeout or reducing the query scope passed to the action.
  * **Action status is`PENDING_ACTION_TIMEOUT`**: 
    * **Cause** : A playbook step waiting for user input or an external asynchronous callback did not complete before the step's timeout expired.
    * **Suggested remediation** : Click **Case ID** in the **Latest 30 Failed Playbook Summary** widget to inspect the pending step. Adjust the step's timeout settings in the playbook designer or configure fallback branches for timed-out pending actions.
  * **High Percentage Terminated (`TERMINATED`) in Top 30 Playbooks Terminated**: 
    * **Cause** : Cases or alerts are being closed (manually or by another automation rule) while the playbook is still running, or analysts are manually stopping the playbook.
    * **Suggested remediation** : Review the playbook's execution duration in **Avg Execution Time by Playbook** and ensure case auto-closure steps occur only after all required enrichment and response actions finish.
  * **High Playbooks Pending in Queue (`PENDING_IN_QUEUE`)**: 
    * **Cause** : A surge in alerts or overly broad playbook triggers is queuing more playbook runs than the execution pipeline can process concurrently.
    * **Suggested remediation** : Refine playbook trigger conditions to be more selective, consolidate redundant playbooks using reusable blocks, and review [bulk actions and filters in playbooks](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/bulk-actions-and-filters-in-playbooks).
  * **Avg Playbook Execution Time is much higher than Avg Action Execution Time** : 
    * **Cause** : Playbooks spend most of their lifecycle waiting for manual user actions or external callbacks rather than actively executing integration actions.
    * **Suggested remediation** : Inspect the **Top 30 Slowest Playbook Executions** to identify which playbooks are waiting on manual intervention, and automate routine approval or triage decisions where appropriate.



After making changes to your playbooks or integration configurations, monitor the **Failed Playbooks % Over Time** and **Failed Integrations % Over Time** charts in the Response Health Hub to verify that failure rates return to expected levels.

## Troubleshooting

The following items explain interface behaviors of the Response Health Hub that you might encounter when analyzing your data:

  * **Playbooks Pending in Queue doesn't change when adjusting the Global Time Filter** : The **Playbooks Pending in Queue** widget measures the current active backlog (`PENDING_IN_QUEUE`) over a fixed 7-day window and intentionally ignores the **Global Time Filter** so that you always see the live queue status.
  * **Simulated playbook runs aren't displayed by default** : The **Playbook Simulated** filter defaults to `false` so that test runs from the playbook simulator don't skew production health metrics. To troubleshoot simulated runs, change **Playbook Simulated** to `true`.
  * **Loop actions and the`Loop` integration don't appear in top action or integration charts**: Internal loop control steps (`ForEachStartLoop`, `ForEachEndLoop`, and the `Loop` integration) are automatically excluded from **Avg Execution Time by Action** , **Top 30 Most Frequently Used Integrations** , and **Top 30 Most Frequently Used Actions** so that your rankings reflect actual security integrations and actions.
  * **Difference between Avg Playbook Execution Time and Avg Action Execution Time** : **Avg Playbook Execution Time** measures the entire wall-clock duration of a playbook from start to finish (`playbook.end_time` minus `playbook.start_time`), whereas **Avg Action Execution Time** averages only the active runtime (`playbook.action.execution_time_ms`) of individual actions. A playbook that waits several hours for an analyst to approve a pending action will have a high playbook execution time even if its automated actions finish in a few seconds.



## What's next

  * [Monitor playbook performance](https://docs.cloud.google.com/chronicle/docs/soar/respond/working-with-playbooks/understanding-playbook-monitoring)
  * [Monitor health of data sources](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard)
  * [Query SOAR playbooks](https://docs.cloud.google.com/chronicle/docs/reports/curated-dashboards/dashboard-queries-soar-playbooks)
  * [Manage and configure dashboards](https://docs.cloud.google.com/chronicle/docs/reports/manage-native-dashboards)



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
