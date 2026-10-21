---
url: https://docs.cloud.google.com/logging/docs/agent/default-logs/
title: Default Logging agent logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:34:18.821463+00:00
---

# Default Logging agent logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/agent/default-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Reference ](https://docs.cloud.google.com/logging/docs/apis)



Send feedback 

#  Default Logging agent logs Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent and Logging agent have reached theis end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/logging/docs/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

The [Logging agent](https://docs.cloud.google.com/logging/docs/agent) is pre-configured to send logs from VM instances to Cloud Logging. This page lists the logs that the Logging agent sends to Cloud Logging with the default configuration.

You can add your own [`fluentd` configuration files](https://docs.fluentd.org/configuration/config-file) to the Logging agent. For more information, see [Configure the Logging agent](https://docs.cloud.google.com/logging/docs/agent/configuration).

**Note:** The next major version of the Logging agent (2.0.0) drops support for several plugins. For more information about this deprecation, refer to the [deprecation guide for third-party integrations](https://docs.cloud.google.com/stackdriver/docs/deprecations/third-party-apps).

### Linux instances

The following logs are pre-configured in the Logging agent running on Linux VM instances.

Log ID | Source and configuration files  
---|---  
`syslog` | Linux `syslog`  
`apache-access`, `apache-error` | [Apache logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`cassandra`, `cassandra-output` | [Cassandra logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`chef-*` | [Chef logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`gitlab-*` | [gitlab logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`jenkins` | [Jenkins logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`jetty-*` | [Jetty logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`joomla` | [Joomla logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`magento-*` | [Magento logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`mediawiki` | [MediaWiki logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`memcached` | [memcached logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`mongodb` | [Mongodb logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`mysql`, `mysql-slow` | [MySQL logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`nginx-access`, `nginx-error` | [Nginx logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`postgresql` | [PostgreSQL logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`puppet-*` | [Puppet Enterprise logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`rabbitmq-*` | [RabbitMQ logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`redis` | [Redis logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`redmine` | [Redmine logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`salt-*` | [Salt logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`solr` | [Solr logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`sugarcrm` | [SugarCRM logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`tomcat`, `tomcat-localhost_access_log` | [Tomcat logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
`zookeeper`, `zookeeper-trace` | [Zookeeper logs](https://github.com/GoogleCloudPlatform/fluentd-catch-all-config/)  
  
### Windows instances

The following logs are pre-configured in the Logging agent running on Windows VM instances.

Log ID | Description  
---|---  
`fluent.info` | Logging agent messages  
`winevt.raw` | Windows Event Log  
  
The logs from the agent are named `projects/[PROJECT_ID]/logs/[LOG_ID]`.

`[LOG_ID]` is a simple name such as `syslog` or `redis`. There is no service name prefix.

The asterisk (`*`) following some of the log names means that there can be several logs whose names begin with the same prefix.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
