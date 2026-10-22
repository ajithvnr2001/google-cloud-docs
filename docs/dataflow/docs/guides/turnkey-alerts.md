---
url: https://docs.cloud.google.com/dataflow/docs/guides/turnkey-alerts/
title: Turnkey alerts for Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:11.430178+00:00
---

# Turnkey alerts for Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/turnkey-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Turnkey alerts for Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Cloud Monitoring Alerting is scheduled to become a [billable service in 2026](https://docs.cloud.google.com/stackdriver/pricing).

To monitor streaming pipeline health and resource consumption without manually configuring policies in Cloud Monitoring, you can enable turnkey alerts in Dataflow. Turnkey alerts provide a preconfigured suite of recommended alert policies that you can enable during job startup.

This feature lets you:

  * **Get instant visibility:** Automatically track critical streaming metrics, such as backlog processing time and vCPU growth, without manual setup.
  * **Standardize monitoring:** Quickly apply baseline alerting policies across new and existing production workloads.
  * **Customize alerts:** Adjust default alert thresholds, disable individual policies, or add your own custom alert policies to the suite.



You can customize these default policies at any time in Cloud Monitoring or integrate your own custom alert policies with the turnkey alerts suite.

## Prerequisites

To use turnkey alerts, your project must meet the following requirements:

  1. **Notification channels** : You must have at least one notification channel configured (for example, email, Slack, or PagerDuty). We recommend configuring Essential Contacts to ensure alerts reach the correct stakeholders. This requirement isn't enforced by the Dataflow service. For more information, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  2. **Permissions** : The Dataflow Service Account (P4SA) requires specific [IAM permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#cloud-monitoring-permissions) to create and manage these policies on your behalf:

     * `monitoring.alertPolicies.get`
     * `monitoring.alertPolicies.list`
     * `monitoring.alertPolicies.create`
     * `monitoring.alertPolicies.update`
     * `monitoring.alertPolicies.delete`

For new projects, these permissions are added automatically. For existing projects, you might need to manually set these permissions on the P4SA account.




## Update P4SA permissions

The Dataflow Service Agent (often referred to as the P4SA, or Per Product, Per Project Service Account) is an automatically managed service account created when you enable the Dataflow API. Its email address uses the following format:
    
    
    service-PROJECT_NUMBER@dataflow-service-producer-prod.iam.gserviceaccount.com
    

To update the P4SA, you need the `resourcemanager.projects.setIamPolicy` permission or a role that includes this permission, such as Project IAM Admin (`roles/resourcemanager.projectIamAdmin`).

To grant the required roles by using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select your project.

  3. Select the **Include Google-provided role grants** checkbox.

  4. In the list of principals, locate the row for the Dataflow Service Agent (`service-PROJECT_NUMBER@dataflow-service-producer-prod.iam.gserviceaccount.com` or with the **Cloud Dataflow Service Agent** role).

  5. In that row, click edit **Edit principal**.

  6. In the **Edit permissions** pane, click add **Add another role**.

  7. In the **Select a role** list, select **Monitoring Editor** (`roles/monitoring.editor`).

  8. Click **Save**. It might take several minutes for the permission update to propagate.


**Note:** Alternatively, you can grant a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) containing the specific `monitoring.alertPolicies.*` permissions listed in Prerequisites.

## Enable turnkey alerts

You can enroll a job in turnkey alerts using the gcloud CLI.

### Enable alerts using the gcloud CLI

Add one of the following flags during job submission to enable or disable the feature:

  * `--enable-turnkey-alerts`
  * `--no-enable-turnkey-alerts`



If your service account lacks the required permissions, the CLI rejects the request and displays the missing permissions. For more information, see Prerequisites.

Turnkey alert settings are preserved across job updates. When you update a job, the previous turnkey alerts setting is retained, so you don't need to specify the `--enable-turnkey-alerts` or `--no-enable-turnkey-alerts` flag again unless you want to change the setting.

## Default policy suite

Turnkey alerts include two primary policies designed for typical streaming workloads, which focus on real-time KPIs such as processing times and resource utilization. Google-provided policies are prefixed with `Default Policy:` for identification, although the service uses labels as the primary identifier.

Customers are automatically enrolled in all policies in the default policy suite. If needed, you can disable specific default policies in Cloud Monitoring Alerting.

Policy name | Base metric | Default threshold | Rationale  
---|---|---|---  
**Default Policy: Estimated Backlog** | `job/estimated_backlog_processing_time` | 30 minutes | Estimates the time needed to clear the current backlog. A backlog greater than 30 minutes indicates the job is struggling to make progress.  
**Default Policy: vCPU Growth Policy** | `job/current_num_vcpus` | Greater than 5x increase in 1-hour average vCPU usage compared to a 7-day average | Monitors relative changes in vCPU counts to help gauge unexpected job costs.  
  
### Policy lifecycle

  * **Beta policies:** These policies have a `BETA` prefix in their name and are subject to change or deletion as thresholds are refined.
  * **GA policies:** Once a policy is deemed stable, the `BETA` prefix is removed.



## Customize and manage alerts

Turnkey alerts serve as a starting point. We recommend customizing them to fit your specific business requirements.

  1. In the Google Cloud console, go to **Cloud Monitoring > Alerting**.
  2. Find the policy (for example, **Default Policy: Estimated Backlog**).
  3. Edit the threshold to your preferred value.

**Note:** You can rename default policies as needed. The Dataflow service identifies turnkey alert policies using the `goog-turnkey-alerts` label, meaning an exact string match of the name is not required.

### Create custom policies

You can add any Cloud Monitoring alert policy to your turnkey alerts suite by adding the `goog-turnkey-alerts` label to it. This lets you manage custom business-specific rules alongside the default suite.

### Disable or delete alert policies

You can disable or delete specific default policies by using Monitoring. When you disable a policy, Monitoring stops evaluating the policy condition and no new incidents are created, but the policy configuration is preserved. If you delete a policy, it's permanently removed from your project. For more information about managing policy lifecycles, see [Manage alerting policies](https://docs.cloud.google.com/monitoring/alerts/manage-alerts) and [Disabled alerting policies](https://docs.cloud.google.com/monitoring/alerts/concepts-indepth#disabled-policies).

## Troubleshooting

Issue | Resolution  
---|---  
**PERMISSION_DENIED** | Ensure that the Dataflow P4SA has the required `monitoring.alertPolicies.*` permissions listed in Prerequisites. If the P4SA is missing these roles, your pipeline still launches successfully, but a `PERMISSION_DENIED` error appears in your command line output and in job logs indicating that default alerts couldn't be created.  
**No alerts received** | Determine if the alert condition was met by checking for incidents. You can view alert firings and incident timelines in Monitoring (see [View incidents and events](https://docs.cloud.google.com/monitoring/alerts/incidents-events)).  
**Duplicate policies** | This typically happens if multiple policies share the `goog-turnkey-alerts` label and the same metric configuration. Dataflow checks for overlapping labels and metrics rather than exact name matches. Review your policies and remove the label from redundant configurations.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
