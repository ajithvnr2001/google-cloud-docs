---
url: https://docs.cloud.google.com/monitoring/settings/disable/
title: Disable collection of metrics \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:18:22.517133+00:00
---

# Disable collection of metrics  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/settings/disable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Disable collection of metrics Stay organized with collections  Save and categorize content based on your preferences. 

You can prevent the ingestion of chargeable metrics into a Google Cloud project by disabling the Cloud Monitoring API. You can also configure the Ops Agent to stop collecting process metrics.

## Disable collection of all metrics

**Caution:** We don't recommend that you disable the Cloud Monitoring API. When you disable the Cloud Monitoring API for a Google Cloud project, you lose the ability to monitor the resources and services in that Google Cloud project.

To prevent the collection of all metrics, disable the Cloud Monitoring API:

###  Console 

  1. In the Google Cloud console, select the Google Cloud project, and then go to the **APIs & Services** page:

[Go to APIs & Services](https://console.cloud.google.com/apis)

  2. Select **Cloud Monitoring API**.

  3. Click **Disable API**.




###  gcloud 

Run the following command to disable the Cloud Monitoring API in your current project:
    
    
    gcloud services disable monitoring.googleapis.com
    

For information about disabling an API by using Google Cloud CLI, see [Enabling and Disabling Services](https://docs.cloud.google.com/service-usage/docs/enable-disable#gcloud).

## Disable collection of process metrics

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

There are multiple ways you can disable the collection of these metrics by the Ops Agent (versions 2.0.0 and higher) and by the legacy Monitoring agent on Linux.

The agents run only on Compute Engine VMs; these procedures apply only to that platform.

You can't disable collection by the Ops Agent if you are running versions less than 2.0.0 or the legacy Monitoring agent on Windows. If you want to disable collection of these metrics on Windows, we recommend that you upgrade to the Ops Agent version 2.0.0 or higher. For more information, see [Installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index).

The general procedure looks like this:

  1. Connect to the VM.

  2. Make a copy of the existing configuration file as a backup. Store the backup copy outside the agent's configuration directory so that the agent doesn't attempt to load both files. For example, the following command makes a copy of the configuration file for the Monitoring agent on Linux:
         
         cp /etc/stackdriver/collectd.conf BACKUP_DIR/collectd.conf.bak
         

  3. Change the configuration by using one of the options described in the following sections:

     * Ops Agent on Linux or Windows
     * Legacy Monitoring agent on Linux
  4. Restart the agent to pick up the new configuration:

     * Legacy Monitoring agent: `sudo service stackdriver-agent restart`
     * Ops Agent: `sudo service google-cloud-ops-agent restart`
  5. Verify that the process metrics are no longer being collected for this VM:

     1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

     2. In the toolbar of the query-builder pane, select the button whose name is _code_ **PromQL**.

     3. For a `gce_instance` resource, enter the following query, replacing VM_NAME with the name of this VM:
            
            rate({"agent.googleapis.com/processes/cpu_time", monitored_resource="gce_instance", metadata_system_name="VM_NAME"}[1m])
            

     4. Click **Run Query**.




### Ops Agent on Linux or Windows

**Note:** This procedure applies only to Ops Agent versions 2.0.0 and higher; you can't disable process metrics on earlier versions.

The location of the configuration file for the Ops Agent depends on the operating system:

  * For Linux: `/etc/google-cloud-ops-agent/config.yaml`
  * For Windows: `C:\Program Files\Google\Cloud Operations\Ops Agent\config\config.yaml`



To disable the collection of all process metrics by the Ops Agent, add the following to your `config.yaml` file:
    
    
    metrics:
      processors:
        metrics_filter:
          type: exclude_metrics
          metrics_pattern:
          - agent.googleapis.com/processes/*
    

This excludes process metrics from collection in the `metrics_filter` processor that applies to the default pipeline in the `metrics` service.

For more information about configuration options for the Ops Agent, see [Configuring the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/configuration).

### Legacy Monitoring agent on Linux

You have the following options for disabling the collection of process metrics with the legacy Monitoring agent:

  * Modify the agent's configuration file.
  * Replace the agent's configuration file.



The following sections describe each option and list the benefits and risks associated with that option.

#### Modify the agent's configuration file

With this option, you directly edit the agent's main configuration file, `/etc/stackdriver/collectd.conf`, to remove the sections that enable the collection of the process metrics.

##### Procedure

There are three groups of deletions you need to make to the `collectd.conf` file:

  1. Delete the following `LoadPlugin` directive and plugin configuration:
         
         LoadPlugin processes
         
         <Plugin "processes">
           ProcessMatch "all" ".*"
           Detail "ps_cputime"
           Detail "ps_disk_octets"
           Detail "ps_rss"
           Detail "ps_vm"
         </Plugin>
         

  2. Delete the following `PostCacheChain` directive and the configuration of the `PostCache` chain:
         
         PostCacheChain "PostCache"
         
         <Chain "PostCache">
           <Rule "processes">
             <Match "regex">
               Plugin "^processes$"
               Type "^(ps_cputime|disk_octets|ps_rss|ps_vm)$"
             </Match>
             <Target "jump">
               Chain "MaybeThrottleProcesses"
             </Target>
             Target "stop"
           </Rule>
         
           <Rule "otherwise">
             <Match "throttle_metadata_keys">
               OKToThrottle false
               HighWaterMark 5700000000  # 950M * 6
               LowWaterMark 4800000000  # 800M * 6
             </Match>
             <Target "write">
                Plugin "write_gcm"
             </Target>
           </Rule>
         </Chain>
         

  3. Delete the `MaybeThrottleProcesses` chain used by the `PostCache` chain:
         
         <Chain "MaybeThrottleProcesses">
           <Rule "default">
             <Match "throttle_metadata_keys">
               OKToThrottle true
               TrackedMetadata "processes:pid"
               TrackedMetadata "processes:command"
               TrackedMetadata "processes:command_line"
               TrackedMetadata "processes:owner"
             </Match>
             <Target "write">
                Plugin "write_gcm"
             </Target>
           </Rule>
         </Chain>
         




##### Benefits and risks

  * Benefits 
    * You reduce the resources consumed by the agent because the metrics are never collected.
    * If you have made other changes to your `collectd.conf` file, you might be able to preserve those changes.
  * Risks 
    * You must use the `root` account to edit this configuration file.
    * You risk introducing typographical errors into the file.



#### Replace the agent's configuration file

With this option, you replace the agent's main configuration file with a pre-edited version that has the relevant sections removed for you.

##### Procedure

  1. Download the pre-edited file, `collectd-no-process-metrics.conf`, from the GitHub repository to the `/tmp` directory:
         
         cd /tmp && curl -sSO https://raw.githubusercontent.com/Stackdriver/agent-packaging/master/collectd-no-process-metrics.conf
         

  2. Replace the existing `collectd.conf` file with the pre-edited file:
         
         cp /tmp/collectd-no-process-metrics.conf /etc/stackdriver/collectd.conf
         




##### Benefits and risks

  * Benefits 
    * You reduce resources consumed by the agent because the metrics are never collected.
    * You don't have to manually edit the file as `root`.
    * Configuration-management tools can replace a file.
  * Risks 
    * If you have made other changes to the `collectd.conf` file, you have to merge those changes into the replacement file.



#### Troubleshooting

The procedures described in this document are changes to the configuration of the agent, so the following problems are most likely:

  * Insufficient privilege to edit the configuration files. Configuration files must be edited from the `root` account.
  * Introduction of typographical errors into the configuration file if you edit it directly.



For information on resolving other problems, see [Troubleshooting the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/troubleshooting).

### Legacy Monitoring agent on Windows

You can't disable the collection of process metrics by the legacy Monitoring agent running on Windows VMs. This agent is not configurable. If you want to disable collection of these metrics on Windows, we recommend that you upgrade to the Ops Agent version 2.0.0 or higher. For more information, see [Installing the Ops Agent](https://docs.cloud.google.com/monitoring/agent/ops-agent/install-index).

If you are running the Ops Agent, see Ops Agent on Linux or Windows.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
