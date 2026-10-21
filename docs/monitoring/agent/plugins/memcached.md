---
url: https://docs.cloud.google.com/monitoring/agent/plugins/memcached/
title: Memcached plugin \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.235364+00:00
---

# Memcached plugin  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/memcached/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Memcached plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering. For more information visit [memcached.org](http://www.memcached.org/).

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your Memcached instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for Memcached](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/memcached).

## Discovery

Even if the memcached plugin is not configured, Cloud Monitoring will discover memcached services running in your Cloud Platform project by:

  * Searching instance names for **memcached**
  * Checking for ports opened to **11211** via firewall rules



To see the metrics for Memcached, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Memcached** dashboard from the list.



## Configuring Monitoring to monitor memcached

After you [install the monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), use the following instructions to configure the memcached plugin on your instances.

### Enabling the memcached monitoring plugin

On your VM instance, download [memcached.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/memcached.conf) from the [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs) and place it in the directory `/etc/stackdriver/collectd.d/`:
    
    
    (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/memcached.conf)
    

After adding the configuration file, restart the monitoring agent by running the following command:
    
    
    sudo service stackdriver-agent restart
    

For more information on the `collectd` `memcached` plugin, see [Plugin:memcached](https://collectd.org/wiki/index.php/Plugin:memcached).

## What is monitored

The full list of metrics the Memcached plugin monitors is at [Agent metrics: memcached](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-memcached).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
