---
url: https://docs.cloud.google.com/monitoring/agent/plugins/nginx/
title: Nginx plugin \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.558885+00:00
---

# Nginx plugin  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/nginx/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Nginx plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

Nginx is a free, open-source, high-performance HTTP server and reverse proxy, as well as an IMAP/POP3 proxy server. For more information visit [nginx.org](http://nginx.org/).

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your Nginx instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for nginx](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/nginx).

## Discovery

Even if the Nginx plugin is not configured, Cloud Monitoring will discover Nginx services running in your Cloud Platform project by:

  * Searching instance names for **nginx**
  * Checking for ports opened to **80** or **443** via firewall rules



To see the metrics for Nginx, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Nginx** dashboard from the list.



## Configuring Monitoring to monitor Nginx

After you [install the monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), use the following instructions to configure the Nginx plugin on your instances.

### Prerequisites

The Nginx plugin requires that you enable the status information handler in Nginx. This can be done by downloading [status.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/nginx/conf.d/status.conf) from the [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs) and placing it in the Nginx configuration directory (normally `/etc/nginx/conf.d/`):
    
    
    (cd /etc/nginx/conf.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/nginx/conf.d/status.conf)
    

Alternatively, you can append the contents of [status.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/nginx/conf.d/status.conf) to your `nginx.conf` file, normally located in one of the following directories on your VM instance: `/etc/nginx`, `/usr/local/nginx/conf`, or `/usr/local/etc/nginx`.

**Caution:** You should only expose the agent's endpoint to `localhost` through HTTP.

Reload the Nginx configuration by running:
    
    
    sudo service nginx reload
    

### Enabling the Nginx monitoring plugin

On your VM instance, download [nginx.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/nginx.conf) from the [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs) and place it in the directory `/etc/stackdriver/collectd.d/`:
    
    
    (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/nginx.conf)
    

After adding the configuration file, restart the monitoring agent by running the following command:
    
    
    sudo service stackdriver-agent restart
    

For more information on the `collectd` `nginx` plugin, see [Plugin:nginx](https://collectd.org/wiki/index.php/Plugin:nginx).

## What is monitored

The full list of metrics the Nginx plugin monitors is at [Agent metrics: nginx](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-nginx).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
