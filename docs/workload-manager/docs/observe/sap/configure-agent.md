---
url: https://docs.cloud.google.com/workload-manager/docs/observe/sap/configure-agent/
title: Configure Agent for SAP to set up observability \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:24.055939+00:00
---

# Configure Agent for SAP to set up observability  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/observe/sap/configure-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/workload-manager/docs/overview)



Send feedback 

#  Configure Agent for SAP to set up observability Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to configure Google Cloud's Agent for SAP to set up observability for your SAP workload by using Workload Manager.

The Workload Manager observability service needs the agent to collect metrics from your SAP workload and the underlying infrastructure. For more information, see [SAP observability overview](https://docs.cloud.google.com/workload-manager/docs/observe/sap/overview).

## Before you begin

  * Validate your installation of Google Cloud's Agent for SAP on all the Compute Engine instances running the SAP workload for which you want to set up observability.

For information about how to validate agent installation, see [Validate your installation of the agent](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#validate-agent4sap-installation).

  * Verify that you've completed the [Prerequisites for SAP observability](https://docs.cloud.google.com/workload-manager/docs/observe/sap/prerequisites#configure-vm).




## Configure the agent for a single-zone workload

###  VM Extension Manager 

To configure and manage the agent on a fleet of Compute Engine instances, you must create a VM Extension Manager policy for it.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

To configure the agent to set up observability for an SAP workload that is running in a single [zone](https://docs.cloud.google.com/compute/docs/regions-zones), complete the following steps:

  1. Set up VM Extension Manager:

     * In the VM Extension Manager documentation, review the [Before you begin](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#byb) section.
     * Set up the IAM roles needed to create and manage VM Extension Manager policies. For more information, see the following:

       * [Create VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#create-permissions)
       * [Update VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-iam-permissions)
       * [Delete VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#delete-iam-permissions)
       * [List and describe VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-iam-permissions)
  2. Create a VM extension policy that installs and manages Google Cloud's Agent for SAP on the compute instances that run your SAP workload:

     * Create the VM extension policy in the zone where your SAP workload is running. For information about how to create such a VM extension policy, see [Create a zonal VM extension policy](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#create-vm-ext-policy).
     * To view examples of agent configurations for observability, see Example agent configurations.



###  Package manager 

If you manage the agent lifecycle manually instead of using VM Extension Manager, then you can configure Google Cloud's Agent for SAP by using a package manager:

  1. Establish an SSH connection with the compute instance that runs your SAP workload.

  2. Verify that you're running the latest version of the Agent for SAP.

For information about how to update the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

  3. To let the agent lookup details about SAP workload and send them to Workload Manager:
         
         sudo /usr/bin/google_cloud_sap_agent configure -feature=sap_discovery -enable
         sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_discovery -enable
         

  4. Enable the agent to collect metrics from the processes running in your SAP workload:

     1. Enable the process monitoring feature of the agent:
    
    sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -enable
    

     1. To let the agent collect process metrics related to your SAP HANA database instances, you need to configure additional parameters in the `hana_metrics_config` section.

For more information, see [Configure process monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring).

  5. Enable the agent to collect metrics from the SAP HANA instances running in your SAP workload:

     1. Enable the SAP HANA monitoring feature of the agent:
    
    sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -enable
    

     1. To let the agent connect with the SAP HANA instances and collect metrics, you need to configure additional parameters.

For more information, see [Configure SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring).

  6. Save the configuration file.




To view examples of agent configurations for observability, see Example agent configurations.

## Configure the agent for a multi-zone workload

###  VM Extension Manager 

To configure and manage the agent on a fleet of Compute Engine instances, you must create a VM Extension Manager policy for it.

**Caution** : If you apply a VM Extension Manager policy to VMs on which the Agent for SAP is already running, then the policy overrides the existing agent's version and configuration with what you've set in the policy. 

The existing configuration of the agent is written to a BAK file in the `/etc/google-cloud-sap-agent/`directory on the respective VMs.

To configure the agent to set up observability for an SAP workload that is running in two or more [zones](https://docs.cloud.google.com/compute/docs/regions-zones), complete the following steps:

  1. Set up VM Extension Manager:

     * In the VM Extension Manager documentation, review the [Before you begin](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#byb) section.
     * Set up the IAM roles needed to create and manage VM Extension Manager policies. For more information, see the following:

       * [Create VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#create-permissions)
       * [Update VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#update-iam-permissions)
       * [Delete VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#delete-iam-permissions)
       * [List and describe VM extension policies](https://docs.cloud.google.com/compute/docs/vm-extensions/manage-vm-extensions#view-iam-permissions)
  2. Create a VM extension policy that installs and manages Google Cloud's Agent for SAP on the compute instances that run the primary site of your SAP workload:

     * Create the VM extension policy in the zone where your SAP workload's primary site is running. For information about how to create such a VM extension policy, see [Create a zonal VM extension policy](https://docs.cloud.google.com/compute/docs/vm-extensions/create-extension-policy#create-vm-ext-policy).
     * To view examples of agent configurations for observability, see Example agent configurations.
  3. If you're running a high-availability SAP workload, or have a disaster recovery (DR) site for your SAP workload, then create a VM extension policy that installs and manages Google Cloud's Agent for SAP on the compute instances that run the secondary or DR site of your SAP workload.




###  Package manager 

If you manage the agent lifecycle manually instead of using VM Extension Manager, then you can configure Google Cloud's Agent for SAP by using a package manager:

  1. Establish an SSH connection with the compute instance that runs your SAP workload.

  2. Verify that you're running the latest version of the Agent for SAP.

For information about how to update the agent, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).

  3. To let the agent collect details about SAP workload and send them to Workload Manager:
         
         sudo /usr/bin/google_cloud_sap_agent configure -feature=sap_discovery -enable
         sudo /usr/bin/google_cloud_sap_agent configure -feature=workload_discovery -enable
         

  4. Enable the agent to collect metrics from the processes running in your SAP workload:

     1. Enable the process monitoring feature of the agent:
    
    sudo /usr/bin/google_cloud_sap_agent configure -feature=process_metrics -enable
    

     1. To let the agent collect process metrics related to your SAP HANA database instances, you need to configure additional parameters in the `hana_metrics_config` section.

For more information, see [Configure process monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-process-monitoring).

  5. Enable the agent to collect metrics from the SAP HANA instances running in your SAP workload:

     1. Enable the SAP HANA monitoring feature of the agent:
    
    sudo /usr/bin/google_cloud_sap_agent configure -feature=hana_monitoring -enable
    

     1. To let the agent connect with the SAP HANA instances and collect metrics, you need to configure additional parameters.

For more information, see [Configure SAP HANA monitoring metrics collection](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-sap-hana-monitoring).

  6. Save the configuration file.

  7. If you're running a high-availability SAP workload, or have a disaster recovery (DR) site for your SAP workload, then repeat this procedure for all the other compute instances that are running your SAP workload.




To view examples of agent configurations for observability, see Example agent configurations.

## Validate the setup for Workload Manager observability

You can validate if you have the correct Google Cloud setup for using the Workload Manager observability service by running the agent's `status` command.

To validate the Google Cloud setup, complete the following steps:

  1. Establish an SSH connection with the Compute Engine instance that is running your SAP workload.
  2. Check the Google Cloud setup for observability:
         
         sudo /usr/bin/google_cloud_sap_agent status
         

If your Google Cloud setup for using the Workload Manager observability service is correct, then the output includes the following. Your configuration might have values other than the **`default`** ones.
         
         Agent Status:
             Installed version: 3.15-....
             ...
             Systemd Service Enabled: True
             Systemd Service Running: True
             Cloud API Full Scopes: True
             Configuration File: /etc/google-cloud-sap-agent/configuration.json
             Configuration Valid: True
         ...
         ----------------------------------------------------------------------------
         Process Metrics: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 collect_process_metrics:        true (configuration file)
                 process_metrics_frequency:      30    (default)
                 process_metrics_to_skip:        []   (default)
                 slow_process_metrics_frequency: 120   (default)
         ...
         ----------------------------------------------------------------------------
         HANA Monitoring Metrics: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 connection_timeout:       120   (default)
                 enabled:                  true  (configuration file)
                 execution_threads:        10    (default)
                 max_connect_retries:      1     (default)
                 query_timeout_sec:        300   (default)
                 sample_interval_sec:      300   (default)
                 send_query_response_time: false (default)
         ...
         ----------------------------------------------------------------------------
         System Discovery: Enabled
             Status: Fully Functional
             IAM Permissions: All granted
             Configuration:
                 enable_discovery:                  true  (default)
                 enable_workload_discovery:         true  (default)
                 sap_instances_update_frequency:    60    (default)
                 system_discovery_update_frequency: 14400 (default)
         ...
         

  3. If your output conveys that some setup is missing, then review the information provided in the preceding sections, perform the required actions, and then re-run the `status` command to re-validate the setup.

  4. If you're using more than one compute instance to run your workload, then repeat this procedure for all the other compute instances running your workload.




## Example agent configurations

The following examples are completed configuration files of Google Cloud's Agent for SAP that is configured to support observability for an SAP HANA workload:

The following example uses a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key for SAP HANA authentication:
    
    
      {
        "provide_sap_host_agent_metrics": true,
        "bare_metal": false,
        "log_level": "INFO",
        "log_to_cloud": true,
        "collection_configuration": {
          "collect_workload_validation_metrics": true,
          "collect_process_metrics": true,
          "hana_metrics_config": {
            "hana_db_user": "db_user_name",
            "sid": "DEH",
            "hdbuserstore_key": "user_store_key"
          }
        },
        "discovery_configuration": {
          "enable_workload_discovery": true,
          "enable_discovery": true
        },
        "hana_monitoring_configuration": {
          "enabled": true,
          "hana_instances": [
            {
              "name": "local",
              "sid": "DEH",
              "user": "system",
              "hdbuserstore_key": "user_store_key"
            },
            {
              "name": "remote",
              "sid": "DEH",
              "user": "system",
              "hdbuserstore_key": "user_store_key"
            }
          ]
        }
      }

The following example uses a username and Secret Manager secret for SAP HANA authentication:
    
    
      {
        "provide_sap_host_agent_metrics": true,
        "bare_metal": false,
        "log_level": "INFO",
        "log_to_cloud": true,
        "collection_configuration": {
          "collect_workload_validation_metrics": true,
          "collect_process_metrics": true,
          "hana_metrics_config": {
            "hana_db_user": "db_user_name",
            "sid": "DEH",
            "hana_db_password_secret_name": "db_pwd_secret_name"
          }
        },
        "discovery_configuration": {
          "enable_workload_discovery": true,
          "enable_discovery": true
        },
        "hana_monitoring_configuration": {
          "enabled": true,
          "hana_instances": [
            {
              "name": "local",
              "sid": "DEH",
              "host": "localhost",
              "port": "30015",
              "user": "db_user_name",
              "hdbuserstore_key": "user_store_key"
            },
            {
              "name": "remote",
              "sid": "DEH",
              "host": "10.123.0.12",
              "port": "30015",
              "user": "db_user_name",
              "secret_name": "db_pwd_secret_name"
            }
          ]
        }
      }

The following example uses a username and password for SAP HANA authentication. We recommend that you instead use a [Secure user store (`hdbuserstore`)](https://help.sap.com/docs/HANA_SERVICE_CF/18956b5b1b004347b7c350f9378bd2e3/dd95ac9dbb571014a7d7f0234d762fdb.html) key or Secret Manager secret for SAP HANA authentication.
    
    
      {
        "provide_sap_host_agent_metrics": true,
        "bare_metal": false,
        "log_level": "INFO",
        "log_to_cloud": true,
        "collection_configuration": {
          "collect_workload_validation_metrics": true,
          "collect_process_metrics": true,
          "hana_metrics_config": {
            "hana_db_user": "db_user_name",
            "sid": "DEH",
            "hana_db_password": "TempPa55word"
          }
        },
        "discovery_configuration": {
          "enable_workload_discovery": true,
          "enable_discovery": true
        },
        "hana_monitoring_configuration": {
          "enabled": true,
          "hana_instances": [
            {
              "name": "local",
              "sid": "DEH",
              "host": "localhost",
              "port": "30015",
              "user": "db_user_name",
              "password": "TempPa55word"
            },
            {
              "name": "remote",
              "sid": "DEH",
              "host": "10.123.0.12",
              "port": "30015",
              "user": "db_user_name",
              "password": "TempPa55word"
            }
          ]
        }
      }

For information about the configuration parameters supported by the agent, see [Configuration parameters](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm#configuration_parameters).

## What's next

  * Once you've successfully completed the observability setup for an SAP workload, it can take up to 15 minutes for that workload to appear in the Workload Manager **Observability** page in the Google Cloud console.

For information about how to observe your SAP workload, see [View observability metrics for SAP](https://docs.cloud.google.com/workload-manager/docs/observe/sap/view-dashboards).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
