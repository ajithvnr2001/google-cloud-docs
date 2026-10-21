---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands/
title: Configuration commands for Google Cloud's Agent for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:51.056036+00:00
---

# Configuration commands for Google Cloud's Agent for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/config-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configuration commands for Google Cloud's Agent for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you the commands that you can use to modify the configuration of Google Cloud's Agent for SAP. These commands are supported from version 3.2 of the agent.

The configuration commands are an alternative to editing the agent's configuration file: `/etc/google-cloud-sap-agent/configuration.json`. Up to version 3.6 of the agent, running any configuration command also restarts the agent to make sure that the change takes effect. From version 3.7 of the agent, the updated configuration is automatically applied within 30 seconds of the change.

## Agent restart limit

You can restart Google Cloud's Agent for SAP up to 3 times in 60 seconds. During this timeframe, while you can continue configuring the agent by running the configuration commands, all auto-restart operations beyond this limit fail with the output: `Could not restart the agent`.

If you see this output, then after running all the required configuration commands, you need to manually restart the agent for the changes to take effect. For instructions, see [Restart the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-restart).

## Help commands

  * To print a summary help for the `google_cloud_sap_agent configure` command of the agent and exit: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -help

  * To print the status of the features of your agent instance: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -showall

  * To print the version of your agent instance: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -version




For information about the arguments supported by the `google_cloud_sap_agent configure` command, see Supported arguments.

## For top-level settings

  * To configure the agent for a Bare Metal Solution server: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -setting=bare_metal -enable

To configure the agent for a Compute Engine instance: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -setting=bare_metal -disable

  * To set the logging level of the agent: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -loglevel=LOG_LEVEL

Replace `LOG_LEVEL` with one of the supported log levels: `debug`, `info`, `warn`, or `error`.




## For SAP system discovery

  * To let the agent collect the names and versions of the SAP products used by your SAP system: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_discovery -enable

To stop the agent from collecting the names and versions of the SAP products used by your SAP system:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_discovery -disable

  * To let the agent send the discovered SAP system information to Cloud Logging, and to Workload Manager if [Workload Manager API](https://console.cloud.google.com/apis/library/workloadmanager.googleapis.com) is enabled in your Google Cloud project: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=sap_discovery -enable

To stop the agent from sending the discovered information to Cloud Logging and Workload Manager:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=sap_discovery -disable




## For SAP Host Agent metrics collection

  * To allow the agent to collect the [SAP Host Agent metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_host_agent_metrics): 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=host_metrics -enable

To stop the collection of the SAP Host Agent metrics:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=host_metrics -disable




## For Agent health metrics collection

  * To enable the collection of the agent health metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -enable

To disable the collection of the agent health metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -disable

  * To modify the frequency at which the agent collects the CPU and memory usage of its daemon process and sends them to Cloud Monitoring: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -agent_metrics_frequency=FREQUENCY

Replace `FREQUENCY` with the required value, in seconds. The frequency must not be less than 5 seconds.

  * To modify the frequency at which the agent checks its operational health and sends that information to Cloud Monitoring: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -agent_health_frequency=FREQUENCY




## For Process monitoring metrics collection

  * To allow the agent to collect the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring): 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -enable

To stop the collection of the Process Monitoring metrics:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -disable

  * To modify the frequency at which agent must collect the fast-changing Process Monitoring metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -process_metrics_frequency=FREQUENCY

To modify the frequency at which agent must collect the slow-changing Process Monitoring metrics:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -slow_process_metrics_frequency=FREQUENCY

Replace `FREQUENCY` with the frequency, in seconds, at which the agent must collect the metrics.

  * To stop the collection of any Process Monitoring metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -process_metrics_to_skip="LIST_OF_METRICS" -add

To resume the collection of any Process Monitoring metrics that you had the agent stop:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -process_metrics_to_skip="LIST_OF_METRICS" -remove

Replace `LIST_OF_METRICS` with the names of the Process Monitoring metrics that you want the agent to resume collecting. Use a comma to separate the metric names.




## For Workload Manager evaluation metrics collection

  * To let the agent collect the [Workload Manager evaluation metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#wlm_evaluation_metrics): 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -enable

  * To stop the collection of the Workload Manager evaluation metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -disable

  * To modify the frequency at which agent must collect the Workload Manager evaluation metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -workload_evaluation_metrics_frequency=FREQUENCY

Replace `FREQUENCY` with the frequency, in seconds, at which the agent must collect the Workload Manager evaluation metrics.

  * To modify the frequency at which agent must collect the SAP HANA database metrics, for Workload Manager evaluation: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_evaluation -workload_evaluation_db_metrics_frequency=FREQUENCY

Replace `FREQUENCY` with the frequency, in seconds, at which the agent must collect the SAP HANA database metrics for Workload Manager evaluation.




## For SAP HANA monitoring metrics collection

  * To allow the agent to collect the [SAP HANA monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana): 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -enable

To stop the collection of the SAP HANA monitoring metrics:
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -disable

  * To modify the sample interval at which the agent must collect the SAP HANA Monitoring metrics: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -sample_interval_sec=SAMPLE_INTERNAL

Replace `SAMPLE_INTERNAL` with the interval, in seconds. The interval must be 5 seconds or longer.

  * To modify the timeout value for a query made to your SAP HANA instance: 
        
        sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -query_timeout_sec=QUERY_TIMEOUT

Replace `QUERY_TIMEOUT` with a value, in seconds.




## Supported arguments

The following table describes the arguments that you can use with the `google_cloud_sap_agent configure` command:

Argument | Description  
---|---  
`-add` |  This argument makes the agent stop collecting the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring) that you specify for the `-process_metrics_to_skip` argument.  
`-disable` |  Disables the specified feature or parameter of the agent.  
`-enable` |  Enables the specified feature or parameter of the agent.  
`-f`=`FEATURE_NAME`   
or  
`-feature`=`FEATURE_NAME` |  `STRING` Sets the agent feature that you want to configure. The following are the supported values:

  * `host_metrics`
  * `process_metrics`
  * `agent_metrics`
  * `hana_monitoring`
  * `workload_evaluation`
  * `sap_discovery`

  
`-h` or `-help` |  Displays help information for the command.  
`-loglevel`=`LOG_LEVEL` |  `STRING` Sets the logging level for the agent. The supported values are: `debug`, `info`, `warn`, and `error`.  
`-path`=`PATH` |  `STRING` Sets the path for the agent's configuration file: `/etc/google-cloud-sap-agent/configuration.json`.  
`-process_metrics_to_skip`="`LIST_OF_METRICS`" |  `STRING` Specifies the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring) that the agent must stop collecting. Use a comma to separate the metric names. Use the `-add` and `-remove` arguments with `-process_metrics_to_skip`.  
`-process_metrics_frequency`=`FREQUENCY` |  `INT` Sets the frequency at which the agent collects fast-changing [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#pm_metric_types). The default value is `30` seconds.  
`-slow_process_metrics_frequency`=`FREQUENCY` |  `INT` Sets the frequency at which the agent collects slow-changing [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring#pm_metric_types). The default value is `120` seconds.  
`-query_timeout_sec`=`TIMEOUT` |  `INT` Sets the query timeout, in seconds, for the collection of the SAP HANA monitoring metrics.  
`-remove` |  This argument makes the agent resume the collection of the [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring) that you stopped using the `-process_metrics_to_skip` argument.  
`-sample_interval_sec`=`INTERVAL` |  `INT` Sets the frequency, in seconds, at which the agent queries your SAP HANA instance and collects the [SAP HANA monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/monitoring-sap-hana).  
`-setting`=`SETTING` |  `STRING` Specifies the agent setting that you want configure.  
`-showall` |  Prints the status of the features of your agent instance.  
`-slow_process_metrics_frequency`=`FREQUENCY` |  `INT` Sets the collection frequency of the slow-changing [Process Monitoring metrics](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/process-monitoring), in seconds.  
`-v` or `-version` |  Prints the version of the agent.  
`-workload_evaluation_metrics_frequency`=`FREQUENCY` |  `INT` Sets the frequency at which the agent collects the Workload Manager evaluation metrics.  
`-workload_evaluation_db_metrics_frequency`=`FREQUENCY` |  `INT` Sets the frequency at which the agent collects the SAP HANA database metrics for Workload Manager evaluation.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
