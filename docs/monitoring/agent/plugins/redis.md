---
url: https://docs.cloud.google.com/monitoring/agent/plugins/redis/
title: Monitoring Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.446919+00:00
---

# Monitoring Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/redis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitoring Redis Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

This guide helps you configure Monitoring to monitor Redis.

Redis is an open source advanced key-value store. It is often referred to as a data structure server since values can contain strings, hashes, lists, sets and sorted sets. For more information, visit [redis.io](http://redis.io/).

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your Redis instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for Redis](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/redis).

## Discovery

Monitoring discovers Redis services running in your Cloud Platform project if you have the following:

  * VM instances with **redis** in their names.
  * Firewall rules that open port **6379**.



To see the metrics for Redis, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Redis** dashboard from the list.



## Configuring Redis monitoring

The Monitoring agent uses the [**hiredis** client library](https://github.com/redis/hiredis) to monitor Redis. After installing Redis, install `hiredis` by running the following commands:

  * RHEL and CentOS
        
        sudo yum install epel-release
            sudo yum install hiredis
        

  * Ubuntu 18.04 LTS, 16.04 LTS, and Debian 9
        
        sudo apt-get install libhiredis0.13
        

  * SLES
        
        sudo zypper install libhiredis0_13
        




## Configuring Monitoring

To monitor Redis, perform the following actions on your VM instance after [installing the monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation):

  1. **Install the Redis configuration file** , [redis.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/redis.conf), by running the following command:
         
         (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/redis.conf)
         

  2. If your Redis instance is password-protected, or if you are using a nonstandard host or port for Redis, as **root** , edit `redis.conf` by following the instructions at the top of the file.

  3. **Restart the monitoring agent** by running the following command:
         
         sudo service stackdriver-agent restart
         




For more information on the `collectd` `redis` plugin, see [Plugin:Redis](https://collectd.org/wiki/index.php/Plugin:Redis).

## Redis metrics

The full list of metrics the Redis plugin monitors is at [Agent metrics: redis](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-redis). The actual metrics collected, and the metrics available in the Monitoring menus, can vary.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
