---
url: https://docs.cloud.google.com/monitoring/agent/plugins/statsd/
title: StatsD plugin \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:33.396138+00:00
---

# StatsD plugin  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/agent/plugins/statsd/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  StatsD plugin Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** As of September 28, 2026, the legacy Monitoring agent has reached its end of support. Standard maintenance and bug fixes are no longer provided. We strongly recommend migrating to one of the [supported alternatives](https://docs.cloud.google.com/monitoring/agent/). For more information about this deprecation, see [Legacy Monitoring and Logging agents end of support](https://docs.cloud.google.com/stackdriver/docs/deprecations/legacy-agents). 

[StatsD](https://github.com/etsy/statsd/wiki) is a protocol for submitting metrics and a daemon for metric data aggregation. By configuring the Monitoring agent's StatsD plugin, you make the agent function as a StatsD daemon that writes metrics to Monitoring.

Using the StatsD plugin with its default configuration is the easiest way to get your user-defined metrics into Monitoring. The StatsD plugin is only available in the Linux Stackdriver Monitoring agent.

The Monitoring agent can also export other collectd metrics as user-defined metrics, but there is no simple default configuration. See [User-defined metrics from the agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent) for details.

This functionality is only available for agents running on Linux. It is not available on Windows.

## Discovery

Monitoring doesn't automatically detect StatsD. To use StatsD metrics, configure the StatsD plugin as described in the next section.

## Configuring the StatsD plugin

### Prerequisites

The StatsD plugin requires version 5.5.2-356 or later of the Monitoring agent. To update the agent, see [Updating the agent](https://docs.cloud.google.com/monitoring/agent/monitoring/installation#agent-version).

### Enabling the plugin

Do the following on your supported VM instance running Linux:

  1. Download [statsd.conf](https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/statsd.conf) and place it in `/etc/stackdriver/collectd.d/`, using the following command:
         
         (cd /etc/stackdriver/collectd.d/ && sudo curl -O https://raw.githubusercontent.com/Stackdriver/stackdriver-agent-service-configs/master/etc/collectd.d/statsd.conf)
         

  2. The default configuration file instructs the agent to accept StatsD metrics on the default StatsD port, **8125**.

If you want to send some metrics to your own StatsD daemon and other metrics to the agent's StatsD daemon, then change the port settings in the configuration file.

  3. Restart the Monitoring agent to pick up the StatsD configuration by running the following command:
         
         sudo service stackdriver-agent restart
         




For more information on the `collectd` `statsd` plugin, see [Plugin:StatsD](https://collectd.org/wiki/index.php/Plugin:StatsD).

## Default mapping to user-defined metrics

To get you started quickly, the agent's StatsD plugin comes with a default collectd configuration that maps from StatsD metrics to Stackdriver user-defined metrics:

  * All metrics from the StatsD plugin have `statsd` in the collectd `plugin` component.

  * Each StatsD **metric type** —held in the collectd `type` component—has a corresponding user-defined metric type name.

  * The StatsD **metric name** —held in the collectd `type_instance` component—is stored as the value of a label named `metric`.

The value of the `metric` label is different for the metric type `Timer`: it includes both the metric name and a counter name: average, upper, lower, sum, percentile-50, and percentile-95.




For example, the following table shows how the supported StatsD metric types and the metric's name are mapped to Monitoring user-defined metrics:

StatsD type | StatsD name | Stackdriver metric type | Metric kind | Value type | Metric label(s)  
---|---|---|---|---|---  
Counter | my.counter | custom.googleapis.com/statsd/derive | Cumulative | Int64 | metric:my.counter  
Gauge | my.gauge | custom.googleapis.com/statsd/gauge | Gauge | Double | metric:my.gauge  
Set | my.set | custom.googleapis.com/statsd/objects | Gauge | Double | metric:my.set  
Timer1 | my.timer | custom.googleapis.com/statsd/latency | Gauge | Double | metric:my.timer-average  
|  | (same) | (same) | (same) | metric:my.timer-upper  
|  | (same) | (same) | (same) | metric:my.timer-lower  
|  | (same) | (same) | (same) | metric:my.timer-sum  
|  | (same) | (same) | (same) | metric:my.timer-percentile-50  
|  | (same) | (same) | (same) | metric:my.timer-percentile-95  
|  | custom.googleapis.com/statsd/gauge | Gauge | (same) | metric:my.timer-count  
  
**Notes:**  
1 There is an incoming sequence of statsd timer metrics with the same name. The agent aggregates StatsD timer metrics and exports summary data to 7 different time series.

For more information on StatsD types, see the [StatsD specification](https://github.com/etsy/statsd/blob/master/docs/metric_types.md).

## Customizing exported metrics

The default StatsD configuration is designed to get you started quickly. This section helps you customize the configuration to suit more complex needs.

You should be familiar with user-defined metrics. For an introduction to metrics, see [Metrics, Time Series, and Resources](https://docs.cloud.google.com/monitoring/api/v3/metrics). For more information, see [User-defined metrics overview](https://docs.cloud.google.com/monitoring/custom-metrics).

You can customize the following things:

  * You can change the values assigned to the default `metric` label. Using more label values results in more time series in your user-defined metric. Using fewer label values results in fewer time series.

  * You can change the user-defined metric types. You don't have to use the predefined types provided in the default configuration. For example, you could identify metrics with a certain name and use a different user-defined metric type for them.

  * If you change the user-defined metric types, then you can can also change the labels associated with each type. The default configuration has a single label, but you can add more labels or change the label key.




If you change the metric types, you should define your new user-defined metric types in the Monitoring API. For details, see the following section, Designing a metric type.

### Example

Assume that you are using StatsD to monitor an application consisting of two services, `my_service_a` and `my_service_b`. For each service, you want to export to Monitoring a counter metric that represents the number of failed requests. You don't want to use the default StatsD metric types.

### Incoming collectd metrics

Before defining your own metric types, it is important to understand the structure of a collectd metric and how a StatsD metric by default maps into user-defined metrics.

Collectd metrics, including StatsD metrics, include the following components:
    
    
        Host, Plugin, Plugin-instance, Type, Type-instance
    

In this example, the StatsD metrics that you want to export have the following identifiers in collectd:

Component | Expected value(s)  
---|---  
**Host** | _any_  
**Plugin** | `statsd`  
**Plugin instance** | _unset_ 1  
**Type** | `derive`2  
**Type instance** | `[SERVICE_NAME].GET.[CODE]`3  
`[VALUE]` | _any value_ 4  
  
**Notes** :  
1 The StatsD plugin currently leaves this component empty.  
2 A StatsD Counter metric is mapped to the collectd `derive` type. 3 For example, a type instance might be `my_service_a.GET.500`. 4 [VALUE] is typically a timestamp and a double-precision number.

The following table shows how this metric would be mapped by default:

StatsD type | StatsD name | Stackdriver metric type | Metric kind | Value type | Metric labels  
---|---|---|---|---|---  
Counter | my_service_a.GET.500 | custom.googleapis.com/statsd/derive | Cumulative | Int64 | metric:my_servce_a.GET.500  
Counter | my_service_b.GET.403 | custom.googleapis.com/statsd/derive | Cumulative | Int64 | metric:my_servce_b.GET.403  
  
The default mapping might present some difficulties for you:

  * This particular counter metric (`[SERVICE_NAME].GET.[CODE]`) is in the same user-defined metric type as all other counter metrics. You can't easily get just this metric's data, because Stackdriver doesn't presently support regular expression searches on labels.

  * You can't easily get data for individual services or individual response codes in your data. For example, you can't easily get the total number of errors (of all kinds) that occurred in `my_service_a`.

  * The default configuration exports all StatsD metrics to Stackdriver, which could be costly if you are only interested in certain metrics.




### Designing a metric type

For a full discussion of creating metric types, see [Create a user-defined metric type](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#md-create).

The following user-defined metric type is a reasonable choice for the data in this example, because it holds only the StatsD metric you are interested in and because its choice of labels helps to better organize the data:

  * Type: `custom.googleapis.com/http/request_errors`
  * Labels: 
    * `service_name` (STRING): The name of the service.
    * `response_code` (INT64): The HTTP response code.
  * Kind: CUMULATIVE
  * Value type: INT64



The following table shows the desired mapping from StatsD to Stackdriver:

StatsD type | StatsD name | Stackdriver metric type | Metric kind | Value type | Metric labels  
---|---|---|---|---|---  
Counter | my_service_a.GET.500 | custom.googleapis.com/http/request_errors | Cumulative | Int64 | service_name:my_service_a, response_code:500  
Counter | my_service_b.GET.403 | custom.googleapis.com/http/request_errors | Cumulative | Int64 | service_name:my_service_b, response_code:403  
  
Once you've designed the metric type, create it using [metricDescriptors.create](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/create). For information about letting Monitoring create the metric type for you, see [Auto-creation of metric descriptors](https://docs.cloud.google.com/monitoring/custom-metrics/creating-metrics#auto-creation).

### Mapping configuration

To export the StatsD metric to the new user-defined metric type, replace the contents of the default StatsD plugin configuration, `/etc/stackdriver/collectd.d/statsd.conf`, with the following code:
    
    
    <Plugin statsd>
      Host "127.0.0.1"
      Port "8125"
      DeleteSets true
      TimerPercentile 50.0
      TimerPercentile 95.0
      TimerLower true
      TimerUpper true
      TimerSum true
      TimerCount true
    </Plugin>
    
    LoadPlugin match_regex
    LoadPlugin target_set
    LoadPlugin target_replace
    
    # Insert a new rule in the default "PreCache" chain, to divert your metrics.
    PreCacheChain "PreCache"
    <Chain "PreCache">
      # The following rule does all the work for your metric:
      <Rule "rewrite_request_errors">
        # Do a careful match for just your metrics; if it fails, drop down
        # to the next rule:
        <Match regex>
          Plugin "^statsd$"
          TypeInstance "^.*\\.GET\\..*$"    # Match on type instance.
        </Match>
    
        <Target "set">
          # Specify the metric descriptor type:
          MetaData "stackdriver_metric_type" "custom.googleapis.com/http/request_errors"
          # Initialize the labels from the "type_instance" label; clean the values up in the next Target below.
          MetaData "label:service_name" "%{type_instance}"
          MetaData "label:response_code" "%{type_instance}"
        </Target>
    
        <Target "replace">
          # Remove ".GET.[code]" to get the real service name.
          MetaData "label:service_name" "\\.GET\\.[0-9]*$" ""
          # Remove "[service].GET." to get the real response code.
          MetaData "label:response_code" "^[^\\.]*\\.GET\\." ""
        </Target>
      </Rule>
    </Chain>
    

**Note:** Installing this configuration file removes the default StatsD mapping. If you want to retain the default mapping for other StatsD metrics, you must add the `Rule` from the default StatsD configuration after the new `rewrite_request_errors` rule.

### Restart the agent

Restart your agent to pick up the new configuration by executing the following command on your VM instance:
    
    
    sudo service stackdriver-agent restart
    

Your user-defined metric information begins to flow into Monitoring immediately.

## Next steps

Customizing the StatsD plugin is the same as customization of collectd metrics for Monitoring. For more information, see the Reference and Troubleshooting sections of [User-defined metrics from the agent](https://docs.cloud.google.com/monitoring/agent/custom-metrics-agent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
