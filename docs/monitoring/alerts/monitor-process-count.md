---
url: https://docs.cloud.google.com/monitoring/alerts/monitor-process-count/
title: Monitor count of processess on a VM \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:10.076353+00:00
---

# Monitor count of processess on a VM  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/alerts/monitor-process-count/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Monitor count of processess on a VM Stay organized with collections  Save and categorize content based on your preferences. 

A _process-health_ alerting policy in Cloud Monitoring lets you monitor the number of processes running on your virtual machines (VMs) that meet conditions that you specify. For example, you can use the Google Cloud console to count processes started by the root user or processes whose invocation command contains a specific string. The alerting policy sends notifications when the process count crosses a threshold you define. For information about which processes you can monitor, see Processes that are monitored.

This content does not apply to log-based alerting policies. For information about log-based alerting policies, which notify you when a particular message appears in your logs, see [Monitoring your logs](https://docs.cloud.google.com/logging/docs/alerting/monitoring-logs). 

## Before you begin

  1. To get the permissions that you need to create and modify alerting policies by using the Google Cloud console, ask your administrator to grant you the [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about Cloud Monitoring roles, see [Control access with Identity and Access Management](https://docs.cloud.google.com/monitoring/access-control).

  2. Ensure that you're familiar with the general concepts of alerting policies. For information about these topics, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts).

  3. Configure the notification channels that you want to use to receive any alerts. For redundancy purposes, we also recommend that you create multiple types of notification channels. For information about these steps, see [Create and manage notification channels](https://docs.cloud.google.com/monitoring/support/notification-options).

  4. Ensure that you've installed the Ops Agent on the VMs that you want to monitor. For more information, see [Google Cloud Observability agents](https://docs.cloud.google.com/monitoring/agent).




## Create alerting policy

To create an alerting policy that monitors the count of processes running on a VM by using the Cloud Monitoring API, the filter expression must specify a time series selector. For an example of a JSON file that specifies this selector, see [Process-health policy](https://docs.cloud.google.com/monitoring/alerts/policies-in-json#json-process-health).

To create an alerting policy that monitors the count of processes running on a VM, do the following:

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select **Create policy**.
  3. Select **?** on the **Select metric** section header and then select **Direct filter mode** in the tooltip.

  4. Enter a Monitoring filter.

For example, to count the number of processes that are running on Compute Engine VM instances whose name includes `nginx`, enter the following:
         
         select_process_count("monitoring.regex.full_match(\".*nginx.*\")")
         resource.type="gce_instance"
         

For syntax information see the following resources:

     * For filters used to count processes running on virtual machines, see [Process-health filters](https://docs.cloud.google.com/monitoring/api/v3/process-health-filters).
     * For general syntax, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).
  5. Complete the alerting policy. You must configure the condition trigger, notifications, documentation, and policy name, and then click **Create policy**.

For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).




## Processes that are monitored

Not all processes running in your system can be monitored by a process-health condition. This condition selects processes to be monitored by using a regular expression that is applied to the command line that invoked the process. When the command line field isn't available, the process can't be monitored.

One way to determine if a process can be monitored by a process-health condition is to look at the active processes. For example, on a Linux system, you can use the `ps` command:
    
    
        ps aux | grep nfs
        USER      PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
        root      1598  0.0  0.0      0     0 ?        S<   Oct25   0:00 [nfsd4]
        root      1639  0.0  0.0      0     0 ?        S    Oct25   2:33 [nfsd]
        root      1640  0.0  0.0      0     0 ?        S    Oct25   2:36 [nfsd]
    

When a `COMMAND` entry is wrapped with square brackets, for example `[nfsd]`, the command-line information for the process isn't available. In this situation, you can't use Cloud Monitoring to monitor the process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
