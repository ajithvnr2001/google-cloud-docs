---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances/
title: Configure guest OS on bare metal instances for SAP HANA \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:42.759257+00:00
---

# Configure guest OS on bare metal instances for SAP HANA  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure guest OS on bare metal instances for SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure the guest operating system (OS) on Compute Engine bare metal instances for the optimal performance of SAP HANA workloads.

To seamlessly configure the guest OS on bare metal instances such as X4, you run the `configureinstance` command of Google Cloud's Agent for SAP.

This guide is meant for SAP Basis and SAP system administrators who run and manage SAP HANA workloads on Google Cloud.

**Caution:** If you've used an Infrastructure as code (IaC) tool such as Terraform or Ansible to deploy your SAP HANA workload on Google Cloud, then you're responsible for ensuring that the state management feature of these tools doesn't modify the configuration updates performed by the `configureinstance` command.

## Before you begin

  * Deploy a Compute Engine instance based on a bare metal machine type.

For information about the bare metal machine types that you can use to run SAP HANA on Google Cloud, the supported OS versions, and the supported block storage configuration, see [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#x4-machines-for-hana).

For information about how to deploy a bare metal instance, see [Create a bare metal instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#baremetal).

  * Verify that version 3.15 (latest) of Google Cloud's Agent for SAP is installed on your bare metal instance.

For information about how to install the agent on a compute instance, see [Install and configure Google Cloud's Agent for SAP on a Compute Engine instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm).

For information about how to update an agent instance to the latest version, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).




## Configure the guest OS on your bare metal instance

  1. Connect to your bare metal instance by using SSH or your preferred method.

  2. To capture information about OS configuration checks and updates that the agent performs on your X4 instance, set the agent's log level to `info`:
         
         sudo /usr/bin/google_cloud_sap_agent configure -loglevel=info
         

  3. Check whether the OS on your bare metal instance is optimally configured to run an SAP HANA workload:
         
         sudo /usr/bin/google_cloud_sap_agent configureinstance -check
         

The command output informs if any OS configurations are needed. From version 3.11, the agent also writes a summary of this output to the `/var/log/google-cloud-sap-agent.log` file.

For information about the OS packages that X4 instances need to run SAP HANA, see the following file in the agent's read-only repository on GitHub: [GoogleCloudPlatform/sapagent/internal/onetime/configureinstance/configurex4.go](https://github.com/GoogleCloudPlatform/sapagent/blob/main/internal/onetime/configureinstance/configurex4.go).

  4. If the preceding command output mentions that OS configurations are required, then apply them:
         
         sudo /usr/bin/google_cloud_sap_agent configureinstance -apply
         

  5. For the configuration to take effect, restart the guest OS that's running on your bare metal instance or restart the bare metal instance.




To view information about the OS configuration checks and updates that the agent performed on your bare metal instance, see View OS configuration logs.

## View guest OS configuration logs

From version 3.11, the agent writes the output of the `configureinstance -check` and `configureinstance -apply` commands to the `/var/log/google-cloud-sap-agent.log` file.

To view these logs, complete the following steps:

  1. Connect to your bare metal instance by using SSH or your preferred method.

  2. Verify that the agent's log level is `info` or higher:
         
         sudo /usr/bin/google_cloud_sap_agent configure -loglevel=info
         

For information about supported logging values, see [For top-level settings](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands#for_top-level_settings).

  3. View log entries in the `/var/log/google-cloud-sap-agent.log` file.

The following are examples of OS configuration related logs:

     * **Success scenario** : If the OS configuration passes all checks, then the output includes `"result": "pass"` and is similar to the following example:
           
           {"level":"info","timestamp":"2026-01-20T22:06:54.501Z","caller":"workloadmanager/systemmetrics.go:202","msg":"Completed check of system configuration settings via ConfigureInstance.",**"result":"pass"** ,"pid":3365118,"context":"WorkloadManagerMetrics"}

     * **Failure scenario** : If the OS configuration fails any check, then the output includes `"result": "fail"` and is similar to the following example:
           
           {"level":"info","timestamp":"2026-02-03T21:52:38.184Z","caller":"workloadmanager/systemmetrics.go:202","msg":"Completed check of system configuration settings via ConfigureInstance.","pid":43310,"context":"WorkloadManagerMetrics",**"result":"fail"**}




## Set up alerts to detect deviations in OS configuration

Guest OS configuration on a compute instance can be modified by several tools or agents. Any misconfiguration can jeopardize the stability of the compute instance, which in turn can jeopardize the stability of the SAP HANA workload running on that instance.

You can monitor the deviations in the guest OS configuration for your bare metal instances by using the following options:

  * Monitor guest OS deviations by using log-based alerts.
  * Monitor guest OS deviations by using Workload Manager evaluation.



### Monitor guest OS deviations by using log-based alerts

On X4 instances, Google Cloud's Agent for SAP checks the guest OS configuration every 5 minutes and writes the output in the `/var/log/google-cloud-sap-agent.log` file. You can send these logs to Cloud Logging and set up alerts for whenever the guest OS configuration check fails.

To monitor guest OS deviations by using log-based alerts, complete the following steps:

  1. To create and manage log-based alerting policies, verify that your administrator grants you the required IAM roles, as described in [Roles required to create and use log-based alerting policies](https://docs.cloud.google.com/logging/docs/access-control#lba-permissions).

  2. Verify that you've satisfied the prerequisites mentioned in the "Before you begin" section of [Configure log-based alerting policies](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts).

  3. Connect to your bare metal instance by using SSH or your preferred method.

  4. Verify that the agent is configured to send logs to Cloud Logging:

     1. Open the agent's configuration file:
            
            /etc/google-cloud-sap-agent/configuration.json
            

     2. For the parameter `log_to_cloud`, verify that the value is set to `true`.

  5. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  6. Use the **Query** pane to build a query that matches the OS configuration related logs that you want to filter. For example:

     * The following query helps you filter log entries related to the agent's OS configuration checks:
           
           LOG_ID("google-cloud-sap-agent")
           resource.type="gce_instance"
           jsonPayload.message="Completed check of system configuration settings via ConfigureInstance."

     * The following query helps you filter log entries related to scenarios where your bare metal instances don't pass the agent's OS configuration checks:
           
           LOG_ID("google-cloud-sap-agent")
           resource.type="gce_instance"
           jsonPayload.message="Completed check of system configuration settings via ConfigureInstance."
           **jsonPayload.result="fail"**

The following are examples of how OS configuration check related logs appear in Logging:
    
    Configuration Passed:
    {
      "caller": "third_party/sapagent/internal/workloadmanager/systemmetrics.go:202",
      "message": "Completed check of system configuration settings via ConfigureInstance.",
      "result": "pass",
      "stack": ""
    }
    ...
    Configuration Failed:
    {
      "caller": "third_party/sapagent/internal/workloadmanager/systemmetrics.go:202",
      "message": "Completed check of system configuration settings via ConfigureInstance.",
      "result": "fail",
      "stack": ""
    }
    

  7. Click **Run query** to validate the query.

  8. Create a log alert.

To learn how to create this alert, see step three in the procedure that's described in [Create a log-based alerting policy by using the Logs Explorer](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts#lba-definition).




### Monitor guest OS deviations by using Workload Manager evaluation

Workload Manager evaluation is a rule-based service that you can use to scan your SAP workload for deviations, including those related to the guest OS configuration on X4 instances. You can create evaluations that automatically run at a specific frequency and set up alerts based on the evaluation results.

To monitor guest OS deviations by using Workload Manager evaluation, complete the following steps:

  * Create and run an evaluation for your SAP workload as follows:

    * While selecting the best practices for which you want to evaluate your SAP workload, include **SAP General: Configure OS settings for X4 instances**.

    * In the **Frequency & notification** pane, perform the following:

      * In the **Scheduling** section, set the frequency at which you want to run the evaluation. 

If you deployed your SAP system by using an IaC tool, then we recommend that you run this evaluation more than once a week. This is because such tools periodically enforce configurations, which can include guest OS settings.

      * In the **Notification** section, select the values **When an issue is found** and **> When an issue is fixed**. 

For more information about how to create and run a Workload Manager evaluation, see [Create and run an evaluation](https://docs.cloud.google.com/workload-manager/docs/evaluate/create-evaluation).




## Disable hyperthreading for an X4 instance

In some scenarios, you can improve the performance of OLTP based SAP HANA workloads by disabling hyperthreading on the underlying X4 instances. For more information, see [Hyperthreading](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperthreading).

To disable hyperthreading for your X4 instance by using Google Cloud's Agent for SAP, complete the following steps:

  1. Connect to your X4 instance by using SSH or your preferred method.

  2. Disable hyperthreading for your X4 instance:
         
         sudo /usr/bin/google_cloud_sap_agent configureinstance -apply -hyperThreading="off"
         

  3. Restart your X4 instance.




## Best practices

To ensure that the guest OS on your Compute Engine bare metal instance is configured to enable optimal performance of your SAP workload, we recommend the following best practices:

  * Use the latest version of Google Cloud's Agent for SAP.
  * Run the agent's `configureinstance` command after activities such as patching or upgrading the OS, updating Google Cloud's Agent for SAP.
  * If you're using X4 instances to run your SAP workload, then set up log based alerts.

From version 3.11, the agent runs the `configureinstance -check` command on X4 instances every 5 minutes and writes a summary of the output to the `/var/log/google-cloud-sap-agent.log` file. For more information, see the following:

    * View guest OS configuration logs
    * Set up alerts to detect deviations in OS configuration



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
