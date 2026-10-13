---
url: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-agent-health-metrics/
title: Configure agent health metrics collection \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:07.596166+00:00
---

# Configure agent health metrics collection  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-agent-health-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Configure agent health metrics collection Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows you how to configure Google Cloud's Agent for SAP to collect the health metrics from the agent's daemon process on your Compute Engine instance or Bare Metal Solution server.

For information about this feature, see [Agent health metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#agent_health_metrics).

**Note:** The collection of the agent health metrics is supported only on Linux. It is not supported on Windows.

## Before you begin

  * Validate your installation of Google Cloud's Agent for SAP. For instructions, see the [installation guide for your scenario](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config).
  * If you have installed the agent on a Bare Metal Solution server, then make sure that you have completed the required prerequisites and set up a service account. For instructions, see [Configure Google Cloud's Agent for SAP on Linux](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-bms#configure_agent4sap).



### Required roles

To ensure that the service account has the necessary permissions to let Google Cloud's Agent for SAP collect Agent Health metrics, ask your administrator to grant the following IAM roles to the service account on your project: 

**Important:** You must grant these roles to the service account, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * Write the collected metrics to Cloud Monitoring: [Monitoring Metric Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter) (`roles/monitoring.metricWriter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to let Google Cloud's Agent for SAP collect Agent Health metrics. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to let Google Cloud's Agent for SAP collect Agent Health metrics:

  * Collect the Agent Health metrics from the host Compute Engine instance and write them to Cloud Monitoring: `monitoring.timeSeries.create`



Your administrator might also be able to give the service account these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable agent health metrics collection

To enable Google Cloud's Agent for SAP to collect the health metrics for its daemon process on your host, follow these steps:

  1. Establish an SSH connection with your host Compute Engine instance or Bare Metal Solution server.

  2. Enable the collection of the agent health metrics:

###  Run command 

     1. To enable the collection of the agent health metrics, run the following command:
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -enable

     2. Optionally, you can modify the frequency at which the agent collects the CPU and memory usage of its daemon process and sends them to Cloud Monitoring. The default frequency is 60 seconds.

To modify this frequency, run the following command:
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -agent_metrics_frequency=FREQUENCY

Replace `FREQUENCY` with the required value, in seconds. The frequency must not be less than 5 seconds.

     3. Optionally, you can modify the frequency at which the agent checks its operational health and sends that information to Cloud Monitoring. The default frequency is 60 seconds.

To modify this frequency, run the following command. The frequency must not be less than 5 seconds.
            
            sudo /usr/bin/google_cloud_sap_agent configure -feature=agent_metrics -agent_health_frequency=FREQUENCY

###  Edit configuration file 

As an alternative to running the agent's command, you can manually modify the agent's configuration as follows:

     1. Open the Backint configuration file:
            
            /etc/google-cloud-sap-agent/configuration.json

     2. In the `collection_configuration` section, include the following:
            
            "collect_agent_metrics": true

     3. Optionally, you can modify the frequency at which the agent collects the CPU and memory usage of its daemon process and sends them to Cloud Monitoring. The default frequency is 60 seconds.

To modify this frequency, include the following in the `collection_configuration` section.
            
            "agent_metrics_frequency": FREQUENCY

Replace `FREQUENCY` with the required value, in seconds. The frequency must not be less than 5 seconds.

     4. Optionally, you can modify the frequency at which the agent checks its operational health and sends that information to Cloud Monitoring. The default frequency is 60 seconds.

To modify this frequency, include the following in the `collection_configuration` section. The frequency must not be less than 5 seconds.
            
            "agent_health_frequency": FREQUENCY

     5. Save the configuration file.

     6. Restart the agent for the new settings to take effect:

**Note:** From version 3.7, you need not restart the agent because any changes to the agent's configuration are automatically applied within the next 30 seconds.
            
            sudo systemctl restart google-cloud-sap-agent




### Example configuration files

### Compute Engine instance

The following example is a completed configuration file of Google Cloud's Agent for SAP running on a Compute Engine instance, where the collection of the agent health metrics is enabled: 
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": false,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false,
        **"collect_agent_metrics" : true,
        "agent_metrics_frequency": 60,
        "agent_health_frequency": 60**
      },
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": false
      }
    }

### Bare Metal Solution server

The following example is a completed configuration file of Google Cloud's Agent for SAP running on a Bare Metal Solution server, where the collection of the agent health metrics is enabled: 
    
    
    {
      "provide_sap_host_agent_metrics": true,
      "bare_metal": true,
      "log_level": "INFO",
      "log_to_cloud": true,
      "collection_configuration": {
        "collect_workload_validation_metrics": true,
        "collect_process_metrics": false,
        **"collect_agent_metrics" : true,
        "agent_metrics_frequency": 60,
        "agent_health_frequency": 60**
      },
      "cloud_properties": {
        "project_id": "my-project",
        "instance_name": "bms-machine-1",
        "region": "us-central1",
        "image": "rhel-8"
      },  
      "discovery_configuration": {
        "enable_discovery": true,
        "enable_workload_discovery": true
      },
      "hana_monitoring_configuration": {
        "enabled": false
      }
    }

### Configuration parameters

The following table explains the configuration parameters of Google Cloud's Agent for SAP that are specific to the collection of the agent health metrics:

Parameters  
---  
`collection_configuration.collect_agent_metrics` |  `Boolean` Optional. Specify `true` to let the agent collect the following information and send them to Cloud Monitoring:

  * CPU and memory usage by the agent's daemon process on your host.
  * The operational health of the agent's daemon process on your host.

The default value is `false`.  
`collection_configuration.agent_metrics_frequency` |  `Int` Optional. Specify the frequency at which the agent collects the CPU and memory usage of its daemon process on the host and sends them to Cloud Monitoring. This information is captured by the `sap/agent/cpu/utilization` and `sap/agent/memory/utilization` metrics. The default value is `60` seconds. The frequency must not be less than 5 seconds.   
`collection_configuration.agent_health_frequency` |  `Int` Optional. Specify the frequency at which the agent which the agent checks its operational health and sends that information to Cloud Monitoring. This information is captured by the `sap/agent/health` metric. The default value is `60` seconds. The frequency must not be less than 5 seconds.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
