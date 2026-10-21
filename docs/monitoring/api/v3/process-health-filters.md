---
url: https://docs.cloud.google.com/monitoring/api/v3/process-health-filters/
title: Process-health filters \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:59.236508+00:00
---

# Process-health filters  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/process-health-filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Process-health filters Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to count the number of processes running on your virtual machines (VMs) that meet the filter conditions you specify. You can create alerting policies and charts that count processes by using the Cloud Monitoring API or by using the Google Cloud console.

If you are interested in information about running processes, for example, you want to know the CPU utilization for specific processes, then see [Process metrics](https://docs.cloud.google.com/monitoring/agent/process-metrics).

The structure of the Monitoring filter when it's used to count processes is similar to the structure used when you use these filters to specify monitored resources or metric types. For general information, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).

## Before you begin

If you aren't familiar with metrics, time series, and monitored resources, see [Metrics, Time Series, and Resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

## Processes that are counted

Monitoring counts processes by applying a regular expression to the command line that invoked the process. If a process doesn't have a command-line field available, then that process isn't counted.

One way to determine whether a process can be counted is to view the output of the Linux `ps` command:
    
    
        ps aux | grep nfs
        USER      PID  %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
        root      1598  0.0  0.0      0     0 ?        S<   Oct25   0:00 [nfsd4]
        root      1639  0.0  0.0      0     0 ?        S    Oct25   2:33 [nfsd]
        root      1640  0.0  0.0      0     0 ?        S    Oct25   2:36 [nfsd]
    

When the entry in the `COMMAND` column is wrapped with square brackets, for example `[nfsd]`, the command-line information for the process isn't available and therefore the process isn't counted.

## Process-health filter structure

A process-health filter identifies which processes to count and one or more resources whose processes are to be counted. For example, the following JSON describes an alerting policy that sends a notification if the number of processes is less than 30 on any Compute Engine VM instance:
    
    
         {
            "displayName": "Count all processes",
            "conditionThreshold": {
              "aggregations": [],
              "comparison": "COMPARISON_LT",
              "duration": "0s",
              "filter": "select_process_count(\"*\") resource.type=\"gce_instance\"",
              "thresholdValue": 30,
              "trigger": {
                "count": 1
              }
            }
         }
    

In this example, the value of the `filter` statement is a string with two clauses. The first clause, `select_process_count(\"*\")`, specifies that all processes are counted. The second clause, `resource.type=\"gce_instance\"`, identifies that Compute Engine VMs are to be monitored.

If you use the Google Cloud console, then use direct filter mode to enter the value of a Monitoring filter. However, be sure to remove any escapes that protect a substring. For example, to count all processes for Compute Engine VMs, enter the following:
    
    
        select_process_count("*") resource.type="gce_instance"
    

For information about how to access direct filter mode when using Metrics Explorer, or when creating alerting policies or charts on dashboards, see the following documents:

  * Alerting: [Direct filter mode](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#not-listed)
  * Charts: [Direct filter mode](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics#direct-filter)
  * Metrics Explorer: [Direct filter mode](https://docs.cloud.google.com/monitoring/charts/metrics-selector#direct-filter)



## Resource identifier

A process-health filter must set the `resource.type` field to specify the VMs whose processes are counted. The value of this filter must be one of the following:

  * `gce_instance`
  * `aws_ec2_instance`



If you only specify the `resource.type` field, then processes on all VMs are counted:

  * To select a single VM instance, add a `metric.labels.instance_name` filter object.
  * To select a group of VMs, add a `group.id` filter object.



For more information on the `resource.type` field, see [Monitoring filters](https://docs.cloud.google.com/monitoring/api/v3/filters).

## Process identifier

A process-health filter must call the function `select_process_count`. The arguments of this function identify the processes to be counted.

There are three filter objects that you can specify in a call to `select_process_count`:

  * `command_line` (or `metric.labels.command_line`): This filter applies to the command line used to start the process. Command lines are truncated after 1024 characters, so text in a command line beyond that limit can't be matched against.

  * `command` (or `metric.labels.command`): This filter applies to the command line used to start the process. Commands are truncated after 1024 characters, so text in a command beyond that limit can't be matched against.

  * `user` (or `metric.labels.user`): This filter applies to the user that started the process.




You can either use positional arguments or named arguments in the call to `select_process_count`. If you use named arguments, then you must specify the filter object, an equals statement, `=`, and a value. If you use positional arguments, then you only specify the value. A case-sensitive string test determines whether a process is a match to the filter.

The value of a filter object can be any of the following:

  * string (exact match)
  * `*` (wildcard)
  * `has_substring(string)`
  * `starts_with(string)`
  * `ends_with(string)`
  * `monitoring.regex.full_match(string)`



If you specify multiple filters, then the following rules apply:

  * `command_line` is joined to `command` by a logical-OR. A process is counted when it matches either filter.
  * `user` is joined to `command_line` (`command`) by a logical-AND. A process is a match only when it matches the `user` filter and the `command_line` (`command`) filter.
  * If you apply all filters, then a process is counted when it matches the `user` filter and when it matches the `command_line` or `command` filter.



### Named arguments

To use named arguments, specify the filter name, an equals statement, `=`, and then the filter value. You can specify named arguments in any order.

For example, the following matches all processes started by root when the command line included the string `nginx`:
    
    
         select_process_count("command_line=has_substring(\"nginx\")","user=root")
    

This example uses a regular expression match on the command line:
    
    
         select_process_count("command_line=monitoring.regex.full_match(\".*nginx.*\")","user=starts_with(\"root\")")
    

This example counts all processes whose command line was `/bin/bash`:
    
    
         select_process_count("command=/bin/bash")
    

This example counts all processes started by the user `www` whose command line starts with `/bin/bash`:
    
    
         select_process_count("user=www", "command_line=starts_with(\"/bin/bash \")")
    

### Positional arguments

To use positional arguments, you supply only the filter value. The following rules apply to positional arguments:

  * If a single argument is provided, then that argument is interpreted as a command-line filter object:


    
    
            select_process_count("*")
            select_process_count("/sbin/init")
            select_process_count("starts_with(\"/bin/bash -c\")")
            select_process_count("ends_with(\"--alsologtostderr\")")
            select_process_count("monitoring.regex.full_match(\".*nginx.*\")")
    

  * If two arguments are provided, then the first argument is interpreted as a command-line filter and the second is a user filter. A process is counted when it matches both filter objects:


    
    
            select_process_count("/sbin/init", "root")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
