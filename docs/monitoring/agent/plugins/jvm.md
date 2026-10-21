---
url: https://docs.cloud.google.com/monitoring/agent/plugins/jvm/
title: Standalone JVM Monitoring plugin \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:02.109281+00:00
---

# Standalone JVM Monitoring plugin  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/jvm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Standalone JVM Monitoring plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

Cloud Monitoring can monitor Java Virtual Machine processes for common Java metrics.

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your Java Virtual Machine instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for JVM](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/jvm).

## Discovery

To see the metrics for Java Virtual Machine, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Java Virtual Machine** dashboard from the list.



## Configuring Monitoring to monitor Java VMs

**Note:** You do not have to install this plugin if you install one of the Java-based plugins listed in the Discovery section.

After you [install the monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), use the following instructions to configure the JVM plugin on your instances.

### Prerequisites

The JVM plugin requires version 5.5.0-257 or later of the monitoring agent. To update the agent, see [Upgrading the agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#upgrade).

### Enabling the JVM monitoring plugin

Java Virtual Machines are monitored via [JMX](http://www.oracle.com/technetwork/articles/java/javamanagement-140525.html).

On your VM instance, download [jvm-sun-hotspot.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/jvm-sun-hotspot.conf) from the [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs) and place it in the directory `/etc/stackdriver/collectd.d/`:
    
    
    (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/jvm-sun-hotspot.conf)
    

As **root** , edit the downloaded configuration file and replace `JMX_PORT` by the port on which your JVM is configured to allow JMX connections.

After adding the configuration file, restart the monitoring agent by running the following command:
    
    
    sudo service stackdriver-agent restart
    

For more information on the `collectd` `GenericJMX` plugin used to monitor the JVM, see [Plugin:GenericJMX](https://collectd.org/wiki/index.php/Plugin:GenericJMX).

## What is monitored

The full list of metrics the JVM plugin monitors is at [Agent metrics: jvm](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-jvm).

Any additional JMX metrics (MBean attributes) _must_ be sent to Cloud Monitoring as user-defined metrics. For more information, see [User-defined metrics from the agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent). Any user-supplied MBeans added to the configuration that are not redirected to user-defined metrics are rejected by the API.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
