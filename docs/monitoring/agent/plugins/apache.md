---
url: https://docs.cloud.google.com/monitoring/agent/plugins/apache/
title: Apache plugin \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.124286+00:00
---

# Apache plugin  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/apache/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Apache plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

Apache is a widely-used web server for a variety of operating systems. For more information, visit <http://httpd.apache.org/>.

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your Apache instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for Apache](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/apache).

## Discovery

Even if the Apache plugin is not configured, Cloud Monitoring discovers Apache services running in your Cloud Platform project by:

  * Searching instance names for **apache**

  * Checking for ports opened to **80** or **443** via firewall rules




To see the metrics for Apache, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **Apache HTTP Server** dashboard from the list.



## Configuring Monitoring to monitor Apache

After you [install the Monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), use the following instructions to configure the Apache plugin on your instances.

### Prerequisite

The Apache plugin requires that you enable the `mod_status` plugin in Apache. Many Apache installations enable this plugin by default. To see if the plugin is enabled on your VM instance, run the following request:
    
    
    curl http://local-stackdriver-agent.stackdriver.com:80/server-status?auto
    

If the plugin is enabled, then the output includes lines similar to the following:
    
    
     Total Accesses: 2
     Total kBytes: 1
     BusyWorkers: 1
     IdleWorkers: 4
    

If instead you get a `404 Not Found` page, then `mod_status` is not enabled.

Here are several options to enable the `mod_status` plugin:

  * Download [status.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/httpd/conf.d/status.conf) and place it in the Apache configuration directory on your VM instance, typically in `/etc/httpd/conf.d/` or `/etc/apache2/conf.d`. For more information about enabling the `mod_status` plugin, refer to the [Apache 2.4](https://httpd.apache.org/docs/2.4/mod/mod_status.html#enable) or [Apache 2.2](https://httpd.apache.org/docs/2.2/mod/mod_status.html#enable) documentation:
        
        (cd /etc/httpd/conf.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/httpd/conf.d/status.conf)
        

  * Append the contents of [status.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/httpd/conf.d/status.conf) to your main Apache configuration file, normally located at either `/etc/httpd/conf/httpd.conf` or `/etc/apache2/apache2.conf` on your VM instance.

**Caution:** You should only expose the agent's endpoint to `localhost` through HTTP.



Reload the Apache configuration by running:

  * For Debian, Ubuntu, and SLES:
        
        sudo a2enmod mod_status
        sudo a2enmod mod_access_compat
        sudo service apache2 reload
        

  * Other Linux distributions:
        
        sudo service httpd reload
        




### Enabling the Apache monitoring plugin

To enable the Apache monitoring plugin, complete the following steps:

  1. On your VM instance, download [apache.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/apache.conf) and place it in the directory `/etc/stackdriver/collectd.d/`:
         
         (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/apache.conf)
         

If you're not using the default or Google Cloud Observability-provided Apache `mod_status` configuration, as **root** , edit `apache.conf` by following the instructions at the top of the file.

  2. Restart the monitoring agent:
         
         sudo service stackdriver-agent restart
         




For more information on the `collectd` `apache` plugin, see [Plugin:Apache](https://collectd.org/wiki/index.php/Plugin:Apache).

## What is monitored

The full list of metrics the Apache plugin monitors is at [Agent metrics: apache](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-apache).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
