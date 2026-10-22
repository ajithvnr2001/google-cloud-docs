---
url: https://docs.cloud.google.com/chronicle/docs/detection/security-validation/
title: Validate security controls and configurations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:38.864183+00:00
---

# Validate security controls and configurations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/detection/security-validation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Validate security controls and configurations

**Note:** This feature is covered by [Pre-GA Offerings Terms](https://chronicle.security/legal/service-terms/) of the Google Security Operations Service Specific Terms. Pre-GA features might have limited support, and changes to pre-GA features might not be compatible with other pre-GA versions. For more information, see the [Google SecOps Technical Support Service guidelines](https://chronicle.security/legal/technical-support-services-guidelines/) and the [Google SecOps Service Specific Terms](https://chronicle.security/legal/service-terms/).  
If this feature isn't visible in your environment, see [Manage preview features](https://docs.cloud.google.com/chronicle/docs/secops/preview-features-manage) or contact your system administrator.

**Note:** This feature may not be available to all customers in all regions. Private preview features are not manageable in the Public Preview Manager page in the Google SecOps platform. 

This guide is for security engineers who want to proactively test their security by simulating attacks in their Google Cloud environment. It explains how to implement a continuous Security Validation journey.

Security Validation uses actions and scripts that mimic attacker techniques to trigger detection alerts in your Google Cloud projects. Continuous operation identifies vulnerabilities and security teams can reduce risk by ensuring that configurations and controls respond to the latest threats as expected.

Successful completion of this journey provides measurable proof of improved security posture and ensures that newly implemented detection rules or integrations operate correctly without manual intervention.

## Common use cases

This section lists common use cases of Security Validation.

### Detect security posture regression

**Objective** : Identify when a previously blocked attacker behavior is successfully executed in the environment.

**Value** : Alerts security and operations teams to unintended configuration drift, allowing them to remediate vulnerabilities before they are exploited.

### Validate security control tuning

**Objective** : Confirm that newly implemented detection rules or product integrations operate as expected.

**Value** : Provides measurable proof that rule updates or environment changes have successfully improved the security posture, allowing teams to confidently establish a new baseline.

## Key terminology

  * **Security Validation context** : A security validation context sets up the environment for your security tests. It specifies which project to use, which account to run the test with, and any other details that your actions need.

  * **Security Validation action** : A script designed to mimic real-world attacker techniques, used to trigger detection rules to verify your security posture.

  * **Baseline execution** : A specific, completed Security Validation run used as the standard reference for comparing future executions.

  * **Monitor** : A scheduled job (`SecurityValidationJob` in the API) that executes a Security Validation action and evaluates the results against a defined baseline.

  * **Drift status** : The health indicator of a Monitor based on whether recent executions match the baseline (healthy) or show deviation (drift detected).

  * **Correlation window** : The 12-hour period after an execution during which the system searches for and associates related events and detections, based on the event filter template in the metadata of the action executed.

  * **Monitor timeout** : The maximum duration the system waits after an execution for events and detections to correlate before evaluating the final drift status. This timeout operates within the larger 12-hour correlation window. Expected outcomes must be observed before this monitor timeout is reached for the monitor to be considered successful. If checks do not pass before this timeout, the system marks the monitor as `failed`. This duration defaults to 8 hours but can be configured between 15 minutes and 10 hours.




## Before you begin

Ensure the following setup and permissions are in place.

### Required setup

Make sure you have the following setup:

  * Your tenant must have Security Validation enabled.

  * Security Validation only works with self-managed projects.

  * You need one or two Google Cloud projects. While you can use the same project for both executing and targeting, we recommend using separate projects for better security, keeping your tests clean, and making it easier to manage your setup.

    * **Execution project** : Security Validation runs your security tests in the execution project. It uses Cloud Run and Cloud Storage to do this. These jobs and buckets are only intended to be used by the validation service. Other users should not be granted access to them.

The Cloud Run API, Resource Manager API, and IAM API must be enabled in this project and you must have the `resourcemanager.projects.SetIamPolicy`, `storage.buckets.SetIamPolicy`, `storage.buckets.create`, and `storage.buckets.delete` permissions in order to create a Security Validation context for it. See [IAM permissions reference](https://docs.cloud.google.com/iam/docs/permissions-reference) for the list of roles that provide this permission.

    * **Target project** : where the API calls made by the security validation action script operate. The success of actions depends on whether the required APIs used by the actions are enabled in this project and whether the service accounts in the Security Validation context have the necessary permissions on them.

  * **Service accounts** : requires one or more service accounts in the execution project. These accounts execute the action scripts. Any user who needs to run an action with a specific context, must have the `iam.serviceAccounts.actAs` permission on the service account(s) in that context.




### Required permissions

Assign one of the following predefined roles in your SecOps instance project.

  * `chronicle.viewer`: Read-only access to Security Validation actions, contexts, jobs, and execution resources.

  * `chronicle.editor`: Includes all `viewer` permissions, and the ability to create, update, run, and delete Security Validation contexts and jobs.

  * `chronicle.admin`: Includes all `editor` permissions, and the ability to create, update, and delete custom Security Validation actions (API only).




If you're not using the predefined roles listed above, you can grant equivalent permissions using a custom role or by assigning the `chronicle.securityValidationAdmin` role, which includes the same permissions as `chronicle.admin`.

**Note:** the `chronicle.securityValidationAdmin` role must be assigned using the `gcloud` CLI.

For more information, see [Required roles](https://docs.cloud.google.com/chronicle/docs/onboard#required-roles).

## Implement continuous security validation

Validating your security posture involves a structured progression:

  * Defining your environment

  * Executing simulations to establish a baseline

  * Automating the simulations to detect drift.




This workflow ensures that your security controls remain effective as your environment evolves.

### Create a Security Validation context

A Security Validation context sets up the environment for your security tests. It specifies which project to use, which account to run the test with, and any other details that your actions need. You can reuse the same context for different actions.

To create a Security Validation context, do the following:

  1. [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Navigate to **Security Validation** and go to the **Execution Contexts** tab.

  3. Click **Add Execution Context**.

  4. In the **Add Execution Context** dialog, do the following:

     1. In **Basic Properties** , enter the context name and description, and click **Next**.

     2. In **Environment Settings** , enter the Google Cloud project ID, the execution service account, and the cleanup service account. Click **Next**.

We recommend using separate service accounts for `action profile` (to execute action scripts) and for `setup/cleanup profile` (to execute the setup and cleanup scripts that are part of some actions). These service accounts can be given different permissions in the target project.

     3. In **Runtime Variables** , add one or multiple variables to dynamically override default parameters. Add key-value pairs where the `key` is the parameter name and the `value` is its override value.

**Tip:** All actions require the `TARGET_PROJECT_ID` variable to specify the Google Cloud project that you want to target.
     4. Click **Create**.


**Note:** Creating a context allows Google SecOps to create Cloud Run jobs and Cloud Storage buckets in the specified project. Resource and service charges related to these workloads are charged according to the project billing settings.

### Run Security Validation action

To run a Security Validation action for a Security Validation context, do the following:

  1. [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Navigate to **Security Validation** and go to the **Content Library** tab.

  3. Select an action and click **Run**.

  4. On the dialog, select the execution context that you created and click **Run Now**.




A new execution is created and appears on the **Execution History** tab.

## Manage Security Validation Monitors

You can automatically re-run successful actions on a recurring basis using the monitor feature. It enables continuous security posture monitoring without manual intervention.

### Create a Monitor

You can create a Monitor only from a successfully completed execution. To create a Monitor from an execution, do the following:

  1. [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Navigate to **Security Validation** and go to the **Execution history** tab.

  3. Click the **Execution ID** of an execution and click **Create Monitor**.

  4. Optional: In the **Create Monitor** window, give the Monitor a name.

If you don't enter a Monitor name, the Monitor is referenced by a Monitor ID.

Review the baseline execution details displayed in this window.

  5. Click **Next**.

  6. Configure the Monitor settings.

You can either run a Monitor at specific times or run it every hour.

**To run the Monitor at specific times** , do the following:

     1. In the **Time** dropdown, select **Run at specific time**.

     2. Specify the time of day in the adjacent text box.

     3. In the **Days** option, select one of the following:

        * **Daily** : Runs every day at the specified time.

        * **Days of the week** : Runs only on selected days (for example, Mon, Wed, Fri) at the specified time.

        * **Day of the month** : Runs once a month on the specified day (for example, the 15th) at the specified time.

     4. In the **Months** dropdown, select either **Monthly** (to run every month) or **Specific Months** to specify the exact months when the Monitor should run (for example, January, April, July).

     5. In the **Time zone** dropdown, select the required time zone. This field defaults to the time zone set in your **User Preferences** (which may differ from your browser settings). To find or change this default setting, navigate to **Profile > User Preferences > Localization > Time Zone**.

     6. Click **Next**.

**To run the Monitor at hourly intervals** , do the following:

     1. In the **Time** dropdown, select **Repeat hourly**.

     2. Set the Monitor cycle repeat frequency in the **hour(s)** field and the specific minute mark in the **minute(s)** field. For example, setting 1 hour and 30 minutes means the monitor runs every hour at 30 minutes past the hour (it does NOT run every 90 minutes).

     3. In the **Hours** option, select one of the following:

        * **All hours of the day:** The Monitor will run around the clock, every hour of the day, based on the specified frequency.

        * **Start and end hour:** The Monitor will run only within the specified starting and ending hour range (for example, between 8:00 AM and 5:00 PM).

     4. In the **Days** option, select one of the following:

        * **Daily** : Runs every day at the specified time.

        * **Days of the week** : Runs only on selected days (for example, Mon, Wed, Fri) at the specified time.

        * **Day of the month** : Runs once a month on the specified day (for example, the 15th) at the specified time.

     5. In the **Months** dropdown, select either **Monthly** (to run every month) or **Specific Months** to specify the exact months when the Monitor should run (for example, January, April, July).

     6. In the **Time zone** dropdown, select the required time zone. This field defaults to the time zone set in your **User Preferences** (which may differ from your browser settings). To find or change this default setting, navigate to **Profile > User Preferences > Localization > Time Zone**.

     7. Click **Next**.

  7. In **Expected Outcomes** , check or uncheck the conditions as required. You need to select at least one condition.

     * **Action outcome matches baseline:** Evaluates whether the execution state, outcome, and the reason for the outcome match the baseline. All three parameters must match for the check to evaluate to true.

     * **Correlated events products match baseline:**

       * Groups correlated events by product.

       * Verifies that the current execution has at least one event for every product listed in the baseline.

       * The check ignores events from products that don't have any events in the baseline.

       * It evaluates to `false` if events matching the baseline don't arrive before the timeout.

     * **Correlated detection rules alerting match baseline:**

       * Groups detections by rule and alerting state.

       * Verifies that the current execution has at least one detection from a rule that has detections in the baseline execution.

       * Ignores detections from rules that have no detections in the baseline execution.

       * Evaluates to `false` if detections matching the baseline don't arrive before the timeout.

  8. Click **Create** to create the Monitor.




### View and run a Monitor

To view a created Monitor, do the following:

  1. Navigate to **Security Validation** and go to the **Monitors** tab. Some columns are hidden by default; click view_column **Column manager** to manage column visibility.

  2. Locate your specific Monitor within the list.

  3. Click the link for the Monitor to open the Monitor details page.

  4. Click **Run now** to run the Monitor.




The Monitor details page provides a centralized, high-level overview of the Monitor. It helps you assess a Monitor's overall status and health at a glance. It provides the following important information about the Monitor:

**Health Summary**

The following metric cards provide a high-level overview of the Monitor's stability:

  * **Monitor Health Status** : Displays the current state based on the last execution with a finalized monitor result (for example, `Healthy`) and how long it has maintained that state.

  * **Latest Healthy or Unhealthy Result** : Provides a pointer to the most recent execution that deviated from the baseline.

  * **Result Freshness** : Shows the time elapsed since the last execution with a finalized monitor status.




**Expected Outcomes**

This section defines the success criteria derived from the baseline execution.

  * **Action Outcome and Reason** : The action outcome and reason that match the baseline execution (for example, `NOT_BLOCKED` with an accompanying reason).

  * **Products that generated events** : The list of products for correlated events that match the baseline execution.

  * **Alerting Detection Rules** : The list of alerting correlated detection rules that match the baseline execution.




The **Monitor Results** table displays all executions for the Monitor. The table supports text Search, filtering, and column configuration.

### Enable or disable a Monitor

To enable or disable a Monitor, do the following:

  1. Navigate to **Security Validation** and go to the **Monitors** tab.

  2. Click the **Status** toggle to enable or disable a Monitor. Alternatively, you can click **Pause Monitor** or **Restart Monitor** on the **Monitor details** page to change its status.




### Modify or delete a Monitor

To modify or delete a Monitor, do the following:

  1. Navigate to **Security Validation** and go to the **Monitors** tab.

  2. Click the more_vert menu from the Monitor that you want to modify.

  3. Click **Edit Monitor** to modify the monitor or **Delete Monitor** to delete the monitor. You can also click **Edit Monitor** on the **Monitor details** page to modify it.

  4. Click **Update** or **Confirm** to apply the changes.




### Review Monitor results

To view all executions of a Monitor, do the following:

  1. Navigate to **Security Validation** and go to the **Monitors** tab.

  2. Click the more_vert menu from the Monitor.

  3. Click **View all results**. The **Execution history** page appears.




The executions are filtered to display all executions associated with that specific Monitor.

### View last run results

To view the last run results of a Monitor, do the following:

  1. Navigate to **Security Validation** and go to the **Monitors** tab.

  2. Click the more_vert menu from the Monitor.

  3. Click **View last run results** to open the **Execution details**.




The system displays the details of the most recent execution that ran for that Monitor.

## Review execution results

You can view the Security Validation action you execute in the **Execution History** tab. To review the execution results, do the following:

  1. [Sign in to Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Navigate to **Security Validation** and go to the **Execution History** tab to monitor the execution status.

The **Run status** column indicates whether the execution was successful or encountered an error. If successful, you can view the generated events and detections triggered by the Security Validation action in Google SecOps.

  3. Click the **execution ID** to view the execution details.




The **Action Execution Details** page provides the status, outcome, and in-depth analysis of a validation action. Use this page to validate your security posture by understanding which detection rules the action's activity triggered.

**Correlation progress** shows the real-time correlation workflow progress for an execution. While correlation runs, the total event count might increase until the task finishes.

**Note:** Click  refresh  **Refresh** to reload the table data or reload the page to update the total event count.

### Analyze the Correlated Rules table

The **Correlated Rules** table lists detection rules triggered during the action's execution, including both custom and curated rules.

The table displays both custom and curated rules. It includes two groups: * Rules explicitly defined in the action's metadata * Additional rules triggered by correlated events

This helps you identify which rules performed as expected and which rules might require further investigation.

The table includes the following columns:

  * **Rule name:** name of the detection rule. Click the rule name to view the rule definition and its detection history.

  * **Detection count:** number of detections triggered by the rule. A value of `0` indicates no matching events were found.

  * **Detections:** link to the **Detections** page that displays triggered detections from this run.

  * **Associated with Action:** indicates whether the rule was part of the action's metadata:

    * **Yes:** the action's metadata includes the rule. The system _expects_ it to trigger when the action executes.

    * **No:** this action's metadata does not include the rule, but its logic matched the generated events and triggered it.




This table helps you identify the outcomes:

Associated to Action column  | Detection count column  | What it means   
---|---|---  
`YES` | `1` or more  | Success: An expected rule successfully triggered one or more detections.   
`NO` | `1` or more  | An unexpected rule was triggered by the activity.   
`YES` | `0` | An expected rule failed to trigger any detections.   
  
### Analyze correlated events

After you run a Security Validation action, use the correlated events to assess how your environment and security controls responded to the simulated threat.

Your analysis includes two components: a real-time status of the correlation workflow and a detailed table of all the generated events.

The **Event Correlation Status** shows the current workflow state as one of the following:

  * **Running:** the system is actively searching for correlated events.

  * **Completed:** all event correlation activities have completed successfully.

  * **Errored:** the correlation workflow encountered an error and could not complete.




The **Correlation workflow complete at** indicates a time estimation of when the correlation is expected to or has completed.

The **Events table** lists all all events generated by the action. Use this data to analyze individual responses in your environment and security controls.

The table includes the following columns:

  * **Event** : event ID. Click to view event details in **UDM Search**.

  * **Event timestamp:** time the event occurred on the source system (for example, the server or the firewall).

  * **Observed timestamp:** time the Security Validation service found and correlated the event with the execution.

  * **Product:** product that generated the event.

  * **Security result action:** outcome of the event (`Blocked` or `Not blocked`), based on the `security_result.action` field of the UDM event.




Actions may target regions outside of the Google SecOps instance where they're run. Execution results display logs retrieved from the execution project.

## Access advanced assets and references

Review the following assets for configuration examples and reference data mapping.

### Sample implementation: Generate access token using signJWT

Consider an example of the Generate access token using signJWT permission action. This example assumes that you have already set up a Security Validation context and are running the action within that context. The action is expected to generate Cloud Audit Logs and trigger the Access token generation with signJWT threat detection rule.

The following setup is required:

  * **Enabled APIs:** the Identity and Access Management (IAM) service account credentials API must be enabled in both the target and execution projects.

  * **Service account permissions:** the service account specified in the `profile` field of the Security Validation context must have the `iam.serviceAccounts.signJwt` permission in the target project. This can be granted through the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`). This role can be granted either on the project or the target service account (which, for this action, is the default compute engine service account of the target project).

  * **IAM audit logging:** IAM [audit logging](https://docs.cloud.google.com/iam/docs/audit-logging/audit-logging-iamcreds#SignJwt) (`ADMIN_READ`) must be enabled in the target project to capture the events generated by this action.

  * **Custom export filter:** to ingest the events generated by this action through [SecOps Google Cloud ingestion](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/ingest-gcp-logs), a custom export filter must be set that includes `log_id("cloudaudit.googleapis.com/data_access")`.

  * **Rule set:** the Cloud Threats -> [Google Cloud] IAM Abuse rule set must be enabled and set to alerting to see detections in the search and investigation view.




### Monitor scheduling examples

Use these examples as a reference when configuring recurring schedules for continuous monitoring.

Configuration  | When it runs  | **Time** : Run at specific time (10:00 PM)  
**Days** : Days of the week (Monday)  
**Months** : Monthly  
**Timezone** : EST  | Runs every Monday at 22:00 Eastern Standard Time.   
---|---  
**Time** : Run at specific time (01:00)  
**Days** : Day of the month (1)  
**Months** : Specify (Jan, Apr, Jul, Oct)  
**Timezone** : PST  | Runs at 1:00 AM Pacific Standard Time on the first day of January, April, July, and October.   
**Time** : Run at specific time (14:00)  
**Days** : Daily  
**Months** : Monthly   
**Timezone** : UTC  | Runs every day at 02:00 PM Coordinated Universal Time.   
**Time** : Run at specific time (09:30)   
**Days** : Day of the month (15)   
**Months** : Specify (Feb, Apr, Jun, Aug, Oct, Dec)   
**Timezone** : EST  | Runs at 9:30 AM Eastern Standard Time on the 15th of every second month (February, April, June, August, October, December).   
**Time** : Repeat hourly   
**Interval** : Every 1 hour  
**Hours** : All hours  |  Runs non-stop. Executes precisely at the start of every hour, 24 hours a day (for example, 1:00, 2:00, 3:00, and so on).   
**Time** : Repeat hourly   
**Interval** : Every 4 hours   
**Hours** : Start and end hour (22:00 PM to 6:00)  |  Runs overnight only. Executes at 10:00 PM, 2:00 AM, and 6:00 AM to capture server status during low-traffic periods.   
  
## Troubleshooting

### Latency and limits

Results for newly triggered monitors runs do not immediately populate with detection and event data due to the correlation window.

### Error remediation

Error  | Issue Description  | Fix  | IAM Permission Error  | Permission `iam.serviceaccounts.actAs` denied on service account.  | If you created or updated the context just before running the action, wait a few minutes and try again. IAM changes are consistent, however, it can take time for role assignments to propagate across the system.  
  
Verify that the identity running the action has the `iam.serviceaccounts.actAs` permission on the specified service account.   
---|---|---  
  
### Validation and testing

To verify your Monitor is configured correctly without waiting for the next scheduled interval, use the **Run now** button on the Monitor details page. Refresh the page after the correlation window has passed to verify the **Run status**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
