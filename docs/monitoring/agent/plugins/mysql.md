---
url: https://docs.cloud.google.com/monitoring/agent/plugins/mysql/
title: MySQL plugin \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.184241+00:00
---

# MySQL plugin  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  MySQL plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

MySQL is a relational database management system that runs as a server providing multi-user access to a number of databases. For more information visit [mysql.com](http://www.mysql.com/).

This functionality is only available for agents running on Linux. It is not available on Windows.

**Note:** You can now collect metrics from your MySQL instance using the [Ops Agent](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent), the primary and preferred agent for collecting telemetry from your Compute Engine instances. For details, see [configuring the Ops Agent for MySQL](https://docs.cloud.google.com/stackdriver/docs/solutions/agents/ops-agent/third-party/mysql).

## Discovery

Even if the MySQL plugin is not configured, Monitoring will discover MySQL services running in your Cloud Platform project by:

  * Searching instance names for **mysql**
  * Checking for ports opened to **3306** via firewall rules



To see the metrics for MySQL, do the following:

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Select the **MySQL** dashboard from the list.



## Configuring MySQL monitoring

The Monitoring agent uses the [Connector/C API](http://dev.mysql.com/doc/c-api/8.0/en/) to monitor MySQL. For Linux distributions that don't include the Connector/C library with MySQL, run the appropriate command to install it:

### Ubuntu 16.04 LTS and Ubuntu 18.04 LTS
    
    
        sudo apt-get install libmysqlclient20
    

### Ubuntu 19.10
    
    
        sudo apt-get install libmysqlclient21
    

### Debian 9
    
    
        sudo apt-get install libmariadbclient18
    

### Amazon AMI 2016.03 or later
    
    
        sudo yum install mysql-libs
    

### SLES 12
    
    
        sudo zypper install libmysqlclient18
    

### SLES 15
    
    
        sudo zypper install libmariadb3
    

## Configuring Monitoring to monitor MySQL

After you [install the monitoring agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation), use the following instructions to configure the MySQL plugin on your instances.

### Prerequisites

For MySQL collection, you must add a user with a password to MySQL that can run the **SHOW STATUS** command. This user and password are referred to as `STATS_USER` and `STATS_PASS` in the following config file.

### Enabling the MySQL monitoring plugin

MySQL is configured per database on your system. At the moment, no drop-in configuration is available. The following configuration file shows how to configure one database, named `DATABASE_NAME`. You would need to use that configuration as a template for your databases.

On your VM instance, download [mysql.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/mysql.conf) from the [GitHub configuration repository](https://github.com/Stackdriver/stackdriver-agent-service-configs) and place it in the directory `/etc/stackdriver/collectd.d/`:
    
    
    (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/mysql.conf)
    

As **root** , edit the downloaded configuration file and add information about your databases. Inline comments point out where you need to add configuration for additional databases. Wherever you see `DATABASE_NAME`, substitute the name of your database.

After editing the configuration file, restart the monitoring agent by running the following command:
    
    
    sudo service stackdriver-agent restart
    

For more information on the `collectd` `mysql` plugin, see [Plugin:MySQL](https://collectd.org/wiki/index.php/Plugin:MySQL).

## What is monitored

The full list of metrics the MySQL plugin monitors is at [Agent metrics: mysql](https://docs.cloud.google.com/monitoring/api/metrics_agent#agent-mysql).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
