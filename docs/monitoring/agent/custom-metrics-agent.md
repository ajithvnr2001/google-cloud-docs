---
url: https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent/
title: User-defined metrics from the agent \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.682176+00:00
---

# User-defined metrics from the agent  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  User-defined metrics from the agent Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

**Beta**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This guide explains how you can configure the Monitoring agent to recognize and export your application metrics to Cloud Monitoring.

The Monitoring agent is a [collectd](https://collectd.org/wiki/index.php/Main_Page) daemon. In addition to exporting many predefined system and third-party metrics to Cloud Monitoring, the agent can export your own collectd application metrics to Monitoring as [user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics). Your collectd plugins can also export to Monitoring.

An alternative way to export application metrics to Monitoring is to use [StatsD](https://github.com/etsy/statsd/wiki). Cloud Monitoring provides a default configuration that maps StatsD metrics to user-defined metrics. If you are satisfied with that mapping, then you don't need the customization steps described below. For more information, see the [StatsD plugin](https://docs.cloud.google.com/monitoring/agent/plugins/statsd).

For more information about metrics, see the following documents:

  * [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).
  * [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details).
  * [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics).



This functionality is only available for agents running on Linux. It is not available on Windows.

## Before you begin

  * Install the most recent Monitoring agent on a VM instance and verify it is working. To update your agent, see [Updating the agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#upgrade).

  * Configure [collectd](https://collectd.org/wiki/index.php/Main_Page) to get monitoring data from your application. Collectd supports many application frameworks and standard monitoring endpoints through its [read plugins](https://collectd.org/wiki/index.php/List_of_Plugins). Find a read plugin that works for you.

  * (Optional) As a convenience, add the agent's collectd reference documentation to your system's `man` pages by updating the `MANPATH` variable and then running `mandb`:
        
        export MANPATH="$MANPATH:/opt/stackdriver/collectd/share/man"
        sudo mandb
        

The man pages are for `stackdriver-collectd`.




### Important files and directories

The following files and directories, created by installing the agent, are relevant to using the Monitoring agent (collectd):

`/etc/stackdriver/collectd.conf`
    

The collectd configuration file used by the agent. Edit this file to change general configuration.

**Note:** The system-default collectd configuration, `/etc/collectd.conf`, isn't used by the Monitoring agent.
`/etc/stackdriver/collectd.d/`
    

The directory for user-added configuration files. To send user-defined metrics from the agent, you place the required configuration files, discussed below, in this directory. For backward compatibility, the agent also looks for files in `/opt/stackdriver/collectd/etc/collectd.d/`.

`/opt/stackdriver/collectd/share/man/*`
    

The documentation for the agent's version of collectd. You can add these pages to your system's set of `man` pages; see [Before you begin](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent#before-begin) for details.

`/etc/init.d/stackdriver-agent`
    

The init script for the agent.

## How Monitoring handles collectd metrics

As background, the Monitoring agent processes collectd metrics and sends them to Monitoring, which treats each metric as a member of one of the following categories:

  * **User-defined metrics**. Collectd metrics that have the metadata key `stackdriver_metric_type` and a single [data source](https://collectd.org/wiki/index.php/Data_source) are handled as [user-defined metrics](https://docs.cloud.google.com/monitoring/custom-metrics) and sent to Monitoring using the [`projects.timeSeries.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/create) method in the Monitoring API.

  * **Curated metrics**. All other collectd metrics are sent to Monitoring using an internal API. Only the metrics in [the list of curated metrics](https://docs.cloud.google.com/monitoring/api/metrics_agent) are accepted and processed.

  * **Discarded metrics**. Collectd metrics that aren't in the curated metrics list and aren't user-defined metrics are silently discarded by Monitoring. The agent itself isn't aware of which metrics are accepted or discarded.




## Write user-defined metrics with the agent

You configure the agent to send metric data points to Monitoring. Each point must be associated with a user-defined metric, which you define with a _metric descriptor_. These concepts are introduced in [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics) and described in detail at [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details) and [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics).

You can have a collectd metric treated as a user-defined metric by adding the proper metadata to the metric:

  * `stackdriver_metric_type` : (required) the name of the exported metric. Example: `custom.googleapis.com/my_custom_metric`.

  * `label:[LABEL]` : (optional) additional labels for the exported metric. For example, if you want a Monitoring STRING label named `color`, then your metadata key would be `label:color` and the value of the key could be `"blue"`. You can have up to 10 labels per metric type.




You can use a [collectd filter chain](https://www.collectd.org/documentation/manpages/collectd.conf.html#filter-configuration) to modify the metadata for your metrics. Because filter chains can't modify the list of data sources and user-defined metrics only support a single data source, any collectd metrics that you want to use with this facility must have a single data source.

## Example

In this example we will monitor active Nginx connections from two Nginx services, `my_service_a` and `my_service_b`. We will send these to Monitoring using a user-defined metric. We will take the following steps:

  1. Identify the collectd metrics for each Nginx service.

  2. Define a Monitoring metric descriptor.

  3. Configure a [collectd filter chain](https://www.collectd.org/documentation/manpages/collectd.conf.html#filter-configuration) to add metadata to the collectd metrics, to meet the expectations of the Monitoring agent.




### Incoming collectd metrics

Collectd expects metrics to consist of the following components. The first five components make up the collectd **identifier** for the metric:
    
    
        Host, Plugin, Plugin-instance, Type, Type-instance, [value]
    

In this example, the metrics you want to send as a user-defined metric have the following values:

Component | Expected value(s)  
---|---  
**Host** | _any_  
**Plugin** | `curl_json`  
**Plugin instance** | `nginx_my_service_a` or  
`nginx_my_service_b`1  
**Type** | `gauge`  
**Type instance** | `active-connections`  
`[value]` | _any value_ 2  
  
**Notes** :  
1 In the example, this value encodes both the application (Nginx) and the connected service name.  
2 The value is typically a timestamp and double-precision number. Monitoring handles the details of interpreting the various kinds of values. Compound values aren't supported by the Monitoring agent.

### Monitoring metric descriptor and time series

On the Monitoring side, design a metric descriptor for your user-defined metric. The following descriptor is a reasonable choice for the data in this example:

  * Name: `custom.googleapis.com/nginx/active_connections`
  * Labels: 
    * `service_name` (STRING): The name of the service connected to Nginx.
  * Kind: GAUGE
  * Type: DOUBLE



After you've designed the metric descriptor, you can create it by using [`projects.metricDescriptors.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create), or you can let it be created for you from the time series metadata, discussed below. For more information, see [Creating metric descriptors](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent#creating_metric_descriptors) on this page.

The time series data for this metric descriptor must contain the following information, because of the way the metric descriptor is defined:

  * Metric type: `custom.googleapis.com/nginx/active_connections`
  * Metric label values: 
    * `service_name`: either `"my_service_a"` or `"my_service_b"`



Other time series information, including the associated [monitored resource](https://docs.cloud.google.com/monitoring/api/resources)—the VM instance sending the data—and the metric's data point, is automatically obtained by the agent for all metrics. You don't have to do anything special.

### Your filter chain

**Note:** You must hook your new filter chain into the `PreCache` filter chain.

Create a file, `/opt/stackdriver/collectd/etc/collectd.d/nginx_curl_json.conf`, containing the following code:
    
    
    LoadPlugin match_regex
    LoadPlugin target_set
    LoadPlugin target_replace
    
    # Insert a new rule in the default "PreCache" chain, to divert your metrics.
    PreCacheChain "PreCache"
    <Chain "PreCache">
      <Rule "jump_to_custom_metrics_from_curl_json">
        # If the plugin name and instance match, this is PROBABLY a metric we're looking for:
        <Match regex>
          Plugin "^curl_json$"
          PluginInstance "^nginx_"
        </Match>
        <Target "jump">
          # Go execute the following chain; then come back.
          Chain "PreCache_curl_json"
        </Target>
      </Rule>
      # Continue processing metrics in the default "PreCache" chain.
    </Chain>
    
    # Following is a NEW filter chain, just for your metric.
    # It is only executed if the default chain "jumps" here.
    <Chain "PreCache_curl_json">
    
      # The following rule does all the work for your metric:
      <Rule "rewrite_curl_json_my_special_metric">
        # Do a careful match for just your metrics; if it fails, drop down
        # to the next rule:
        <Match regex>
          Plugin "^curl_json$"                   # Match on plugin.
          PluginInstance "^nginx_my_service_.*$" # Match on plugin instance.
          Type "^gauge$"                         # Match on type.
          TypeInstance "^active-connections$"    # Match on type instance.
        </Match>
    
        <Target "set">
          # Specify the metric descriptor type:
          MetaData "stackdriver_metric_type" "custom.googleapis.com/nginx/active_connections"
          # Specify a value for the "service_name" label; clean it up in the next Target:
          MetaData "label:service_name" "%{plugin_instance}"
        </Target>
    
        <Target "replace">
          # Remove the "nginx_" prefix in the service_name to get the real service name:
          MetaData "label:service_name" "nginx_" ""
        </Target>
      </Rule>
    
      # The following rule is run after rewriting your metric, or
      # if the metric wasn't one of your user-defined metrics. The rule returns
      # to the default "PreCache" chain. The default processing
      # will write all metrics to Cloud Monitoring,
      # which will drop any unrecognized metrics: ones that aren't
      # in the list of curated metrics and don't have
      # the user-defined metric metadata.
      <Rule "go_back">
        Target "return"
      </Rule>
    </Chain>
    

### Load the new configuration

Restart your agent to pick up the new configuration by executing the following command on your VM instance:
    
    
    sudo service stackdriver-agent restart
    

Your user-defined metric information begins to flow into Monitoring.

## Reference and best practices

### Metric descriptors and time series

For an introduction to Cloud Monitoring metrics, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). More details are available in [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics) and [Structure of time series](https://docs.cloud.google.com/monitoring/api/v3/metrics-details).

**Metric descriptors**. A metric descriptor has the following significant pieces:

  * A **type** of the form `custom.googleapis.com/[NAME1]/.../[NAME0]`. For example:
        
        custom.googleapis.com/my_measurement
        custom.googleapis.com/instance/network/received_packets_count
        custom.googleapis.com/instance/network/sent_packets_count
        

The recommended naming is hierarchical to make the metrics easier for people to keep track of. Metric types can't contain hyphens; for the exact naming rules, see [Naming metric types and labels](https://docs.cloud.google.com/monitoring/api/v3/naming-conventions#naming-types-and-labels).

  * Up to 10 labels to annotate the metric data, such as `device_name`, `fault_type`, or `response_code`. The values of the labels aren't specified in the metric descriptor.

  * The kind and value type of the data points, such as "a gauge value of type double". For more information, see [`MetricKind`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricKind) and [`ValueType`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#ValueType).




**Time series**. A metric data point has the following significant pieces:

  * The type of the associated metric descriptor.

  * Values for all of the metric descriptor's labels.

  * A timestamped value consistent with the metric descriptor's value type and kind.

  * The [monitored resource](https://docs.cloud.google.com/monitoring/api/resources) the data came from, typically a VM instance. Space for the resource is built in, so the descriptor doesn't need a separate label for it.




### Creating metric descriptors

You don't have to create a metric descriptor ahead of time. When a data point arrives in Monitoring, the point's metric type, labels, and the point's value can be used to automatically create a gauge or cumulative metric descriptor. For more information, see [Auto-creation of metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#auto-creation).

However, there are advantages to creating your own metric descriptor:

  * You can include some thoughtful documentation for the metric and its labels.

  * You can specify additional kinds and types of metrics. The only (kind, type) combinations supported by the agent are (GAUGE, DOUBLE) and (CUMULATIVE, INT64). For more information, see [Metric kinds and value types](https://docs.cloud.google.com/monitoring/api/v3/kinds-and-types#metric-kinds).

  * You can specify label types other than STRING.




If you write a data point to Monitoring that uses a metric type that isn't defined, then a new metric descriptor is created for the data point. This behavior can be a problem when you are debugging the code that writes metric data—misspelling the metric type results in spurious metric descriptors.

After you create a metric descriptor, or after it is created for you, it cannot be changed. For example, you can't add or remove labels. You can only delete the metric descriptor—which deletes all its data—and then recreate the descriptor the way you want.

For more details about creating metric descriptors, see [Creating your metric](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#md-create).

## Pricing

To learn about pricing for Cloud Monitoring, see the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

## Limits

Cloud Monitoring has limits on the number of metric time series and the number of user-defined metric descriptors in each project. For details, see [Quotas and limits](https://docs.cloud.google.com/monitoring/quotas).

If you discover that you have created metric descriptors you no longer want, you can find and delete the descriptors using the Monitoring API. For more information, see [`projects.metricDescriptors`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor).

## Troubleshooting

This section explains how to configure the Monitoring agent's `write_log` plugin to dump out the full set of metric points, including metadata. This can be used to determine what points need to be transformed, as well as to ensure your transformations behave as expected.

**Note:** This will produce a lot output in the system logs. We recommend turning this feature off at the end of your troubleshooting session. If you have configured the Cloud Logging agent, then you can view the system log entries in Cloud Logging.

### Enabling write_log

The `write_log` plugin is included in the `stackdriver-agent` package. To enable the plugin:

  1. As **root** , edit the following configuration file:
         
         /etc/stackdriver/collectd.conf
         

  2. Right after `LoadPlugin write_gcm`, add:
         
         LoadPlugin write_log
         

  3. Right after `<Plugin "write_gcm">…</Plugin>`, add:
         
         <Plugin "write_log">
           Format JSON
         </Plugin>
         

  4. Search for `<Target "write">…</Target>` and after every `Plugin "write_gcm"`, add:
         
         Plugin "write_log"
         

  5. Save your changes and restart the agent:
         
         sudo service stackdriver-agent restart
         




These changes will print one log line per metric value reported, including the full collectd identifier, the metadata entries, and the value.

### Output of write_log

If you were successful in the previous step, you should see the output of `write_log` in the system logs:

  * **Debian-based Linux** : `/var/log/syslog`
  * **Red Hat-based Linux** : `/var/log/messages`



The sample lines below have been formatted to make them easier to read in this document.
    
    
    Dec  8 15:13:45 test-write-log collectd[1061]: write_log values:#012[{
        "values":[1933524992], "dstypes":["gauge"], "dsnames":["value"],
        "time":1481210025.252, "interval":60.000,
        "host":"test-write-log.c.test-write-log.internal",
        "plugin":"df", "plugin_instance":"udev", "type":"df_complex", "type_instance":"free"}]
    
    Dec  8 15:13:45 test-write-log collectd[1061]: write_log values:#012[{
        "values":[0], "dstypes":["gauge"], "dsnames":["value"],
        "time":1481210025.252, "interval":60.000,
        "host":"test-write-log.c.test-write-log.internal",
        "plugin":"df", "plugin_instance":"udev", "type":"df_complex", "type_instance":"reserved"}]
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
