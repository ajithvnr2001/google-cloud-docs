---
url: https://docs.cloud.google.com/monitoring/api/v3/filters/
title: Monitoring filters \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:29.578852+00:00
---

# Monitoring filters  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/v3/filters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  Monitoring filters Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to configure filters when you use the [Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest). You use filters to specify monitored resources, metric types, group definitions, and time series. You can also use a filter to configure an alerting policy that monitors processes running on your systems. For information about those filters, see [Process-health filters](https://docs.cloud.google.com/monitoring/api/v3/process-health-filters).

## Before you begin

If you aren't familiar with metrics, time series, and monitored resources, see [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics).

If you aren't familiar with labels, see [Labels](https://docs.cloud.google.com/monitoring/api/v3/metric-model#generic-label-info) for an introduction.

## Using filters

You can use filters in the [Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest) to do the following:

  * Select the specific [time series data](https://docs.cloud.google.com/monitoring/api/v3/metric-model#time-series) that is returned from a `list` API request. The filter can select time series based on the data's project, group, monitored resource properties, and metric properties. For more information and examples, see Retrieving time series data.


  * Assign resources to a [`Group`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group) based on the resources' properties and the project to which they belong. For more information and examples, see Defining group membership.

  * Select resources within a group based on the resources' properties. For more information and examples, see Listing group members.



  * List particular metric types. For more information and examples, see Listing metric descriptors.

  * List particular monitored resource types. For more information and examples, see Listing monitored resource descriptors.




### Filter selectors

A filter consists of at least one _selector_ , which is a filter keyword. The following examples illustrate the different selectors:

  * `project`: Matches when the metrics of the specified projects are visible to the scoping project of a metrics scope mentioned in the `name` parameter.

Use the `project` selector when a Google Cloud project can view the metrics of multiple Google Cloud projects or AWS accounts and you only want metrics for a subset of those projects. For example, if the [metrics scope](https://docs.cloud.google.com/monitoring/settings#concept-scope) for `Project-A` includes `Project-B`, then a match occurs when `name` has a value of `Project-A` and you use the following filter:
        
        project = "Project-B"

The following filter matches any project ID that starts with `Project-`:
        
        project = monitoring.regex.full_match("Project-.*")

  * `group`: Matches resources belonging to one [ `Group`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group).

The following filter matches the group with the identifier `group-id`:
        
        group.id = "group-id"
            

  * `resource`: Matches [ monitored resources](https://docs.cloud.google.com/monitoring/api/resources) of a particular type or having particular label values.

    * The following filter matches all monitored resources that are Compute Engine virtual machine (VM) instances:
          
          resource.type = "gce_instance"

    * The following filter matches all resources whose zone begins with `europe-`:
          
          resource.labels.zone = starts_with("europe-")

  * `metric`: Matches a particular [ metric type](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor) or [time series](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries) with with a particular label that matches a specific value.

    * The following filter matches a specific metric type:
          
          metric.type = "compute.googleapis.com/instance/cpu/usage_time"

    * The following filter matches time series with a label named `instance_name`, whose value starts with `gke-hipster` or `gke-nginx`:
          
          metric.labels.instance_name = monitoring.regex.full_match("gke-(hipster|nginx).*")




The following table shows which selectors are permitted in filters based on the [Monitoring API](https://docs.cloud.google.com/monitoring/api/ref_v3/rest) call:

Filter purpose | `project` selector | `group` selector | `resource` selector | `metric` selector  
---|---|---|---|---  
Define groups | yes |  | yes* |   
List group members | yes |  | yes |   
List time series | yes | yes | yes | yes †  
List metric descriptors | yes |  |  | yes  
List monitored resource descriptors |  |  | yes |   
* The resource selector has additional options when used for defining group membership.  
† When listing time series, you must specify exactly one metric type. 

The following sections show examples of typical uses of monitoring filters. See Filter syntax for a complete discussion of the available filter objects and operators.

**Note:**

We recommend filtering on the labels defined on [monitored-resource types](https://docs.cloud.google.com/monitoring/api/resources) instead of labels defined on [metric types](https://docs.cloud.google.com/monitoring/api/metrics) when possible, particularly if you are querying high-cardinality metrics. If you have a resource label and a metric label that capture similar information, then use the resource label in your queries.

For example, if your monitored resource includes a `cluster` label and your metric includes a `kubernetes_cluster_name` label that captures similar information, then filter on the resource `cluster` label.

### Retrieving time series data

**Method** : [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list)  
**Filter objects** : `project`, `group.id`, `resource.type`, `resource.labels.[KEY]`, `metric.type`, `metric.labels.[KEY]`

A time series is a list of time-stamped data points of a metric type from a specific monitored resource. For details, see [The metric model](https://docs.cloud.google.com/monitoring/api/v3/metric-model). The metric type is specified by a [metric descriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors#MetricDescriptor), and the monitored resource is specified by a [monitored-resource descriptor](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors#MonitoredResourceDescriptor).

The filter specified to the `timeSeries.list` method must include a `metric` selector, and that selector must specify exactly one metric type:

  * To return all time series for a particular metric type: 
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time"
        

  * To return all time series for a specific group. The `group` selector only works with aligned time series data; see Group selector for more information:
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        group.id = "2468013579"
        

  * To return all time series from a specific Compute Engine instance, use the following filter: 
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = "my-instance-name"
        

  * Return all time series from Compute Engine instances whose names start with `frontend-`, use the following filter: 
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = starts_with("frontend-")
        

  * Return all time series from Compute Engine instances whose names start with `gke-hipster` or `gke-nginx`, use the following filter: 
        
        metric.type = "compute.googleapis.com/instance/cpu/usage_time" AND
        metric.labels.instance_name = monitoring.regex.full_match("^gke-(hipster|nginx).*")
        




### Defining group membership

**Method** : [`projects.groups.create`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups/create)  
**Filter objects** : `project`, `resource.type`, `resource.labels.key`, `metadata.system_labels.[KEY]`, `metadata.user_labels.[KEY]`

A group can contain any number of resources, as specified by a filter. Group membership is dynamic; more or fewer resources might match the filter every time the filter is evaluated. The `name` parameter in the [`Group`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group) object specifies the group and the [scoping project of a metrics scope](https://docs.cloud.google.com/monitoring/settings#data-model). If the `project` selector is used in the filter, then it must specify a project whose metrics are visible to the scoping project.

For example, to create a group that includes only Compute Engine virtual machine (VM) instances in Europe, use the following filter: 
    
    
    resource.type = "gce_instance" AND resource.labels.zone = starts_with("europe-")
    

For information about API methods that you can use to delete, update, or list groups, see [`projects.groups`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups#Group) API reference page.

### Listing group members

**Method** : [`projects.groups.members.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.groups.members/list)  
**Filter objects** : `project`, `resource.type`, `resource.labels.[KEY]`

The `name` parameter specifies a [scoping project of a metrics scope](https://docs.cloud.google.com/monitoring/settings#data-model) and a group defined in that project. If you don't specify a filter, then `projects.groups.members.list` returns a list of the membership of the group.

You can use a filter to limit which group members you retrieve. If the filter includes a `project` selector, then the selectors value must specify a project whose metrics are visible to the scoping project. If an invalid value is specified, then the `project` selector is ignored.

For example, suppose that you create a group that includes all resources whose name contains `test`. To list only the group members that are Pub/Sub topics, use the following filter:
    
    
    resource.type = "pubsub_topic"
    

### Listing metric descriptors

**Method** : [`projects.metricDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.metricDescriptors/list)  
**Filter objects** : `project`, `metric.type`

Use a filter to limit which metric descriptors you retrieve.

For example, to return only the Compute Engine metric descriptors, use the following filter: 
    
    
    metric.type = starts_with("compute.googleapis.com")
    

See [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics) for a complete list of the available metric types. For an overview of how metrics are named, see [Metric naming conventions](https://docs.cloud.google.com/monitoring/api/v3/naming-conventions).

### Listing monitored resource descriptors

**Method** : [`projects.monitoredResourceDescriptors.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.monitoredResourceDescriptors/list)  
**Filter objects** : `resource.type`

Use a filter to limit which monitored resource descriptors you retrieve.

For example, to retrieve only the Pub/Sub monitored resource descriptors, use the following filter: 
    
    
    resource.type = starts_with("pubsub")
    

See [Monitored resource list](https://docs.cloud.google.com/monitoring/api/resources) for a complete list of the monitored resource types defined by Monitoring.

## Examples

In the filtering examples, we use the following metric descriptor, monitored resource descriptor, and virtual machine instance, simplified for illustration:
    
    
        # Metric descriptor:
        { "name": "projects/my-project-id/metricDescriptors/compute.googleapis.com%2Finstance%2Fdisk%2Fread_bytes_count"
          "type": "compute.googleapis.com/instance/disk/read_bytes_count",
          "labels": [ { "key": "device_name",
                        "description": "The name of the disk device." } ] }
    
        # Monitored resource descriptor:
        {  "name": "monitoredResourceDescriptors/gce_instance"
           "type": "gce_instance",
           "labels": [
             { "key": "instance_id",
               "description": "The instance ID provide by Google Compute Engine." },
             { "key": "zone",
               "description": "The Google Cloud Platform zone hosting the instance."
             } ] }
    
        # Resource descriptor for a virtual machine instance.
        { "type": "gce_instance",
          "instance_id": "1472038649266883453",
          "zone": "us-east-1b",
          "disks": [ "log_partition" ],
          "machine_type": "n1-standard-2",
          "tags": { "environment": "bleeding-edge",
                    "role": "frobulator" },
          "project_id": "my-project-id" }
    

**Note:** The filtering syntax doesn't support comments. The examples in this section use a commenting convention, `# comment`, to provide explanatory text, but these comments can't be included in filters.

### Metric retrieval examples

To request the disk-read bandwidth usage for all instances and all devices, define a filter as follows. This filter returns, for each instance, a separate time series reporting the read bandwidth for each device:
    
    
    metric.type = "compute.googleapis.com/instance/disk/read_bytes_count"
    

To refine the request to query for the read bandwidth for only the disk device known as "log_partition" on each instance, define the filter as follows. This filter returns, for each instance, at most one time series, depending on whether a device of that name exists on that instance:
    
    
    metric.type = "compute.googleapis.com/instance/disk/read_bytes_count" AND
    metric.labels.device_name = "log_partition"
    

To restrict the request to a single instance, specify that instance:
    
    
    resource.type = "gce_instance" AND
    resource.labels.instance_id = "1472038649266883453" AND
    metric.type = "compute.googleapis.com/instance/disk/read_bytes_count" AND
    metric.labels.device_name = "log_partition"
    

### Filtering with groups

The following examples illustrate the use of the group selector in filters to restrict monitored resources to those in a specific group. See Resource selector for group definitions for information on the selectors used to define group membership.
    
    
    { "name": "projects/my-test-project/groups/024681012",
      "display_name": "My Redis Cluster",
      "filter": "metadata.user_labels.role=redis" }
    

In a call to the [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method, the following filter requests the disk-read bandwidth usage for all Compute Engine instances in a particular group. The group must be defined in the [scoping project of a metrics scope](https://docs.cloud.google.com/monitoring/settings#data-model) specified in the method's `name` parameter:
    
    
    resource.type = "gce_instance" AND
    group.id = "024681012" AND
    metric.type = "compute.googleapis.com/instance/disk/read_bytes_count"
    

## Reference: filter syntax

For an overview of filters with examples, see Using filters.

A monitoring filter is a string consisting of up to four types of selectors:
    
    
        <monitoring_filter> ::=  <project_selector> AND
                                 <group_selector> AND
                                 <resource_selector> AND
                                 <metric_selector>
    

The filter matches an item if all of the included selectors match the item. As described in the following sections, some selectors can have multiple comparisons joined by `AND` or `OR`. The order of the selectors in the filter doesn't matter, but comparisons for different selectors must not be intermingled.

Depending on the filter's purpose, certain selectors might be required, optional, or prohibited. For example, the filter used to list time series must contain a metric selector. However, the filter that defines the resources in a group can't contain a metric selector, because groups don't contain metric types or time series. 

### Comparisons

Filters and their selectors are built from comparisons. Each **comparison** has the following form:

  * **[OBJECT]** : selects a value to be tested; one of the following:
        
        project
        group.id
        metric.type
        metric.labels.[KEY]
        resource.type
        resource.labels.[KEY]
        metadata.system_labels.[KEY]
        metadata.user_labels.[KEYSTRING]
            

[KEY] is a name, such as `zone` or `instance_id`.

[KEYSTRING] can be name, but if it contains special characters, then it must be quoted with quotation marks (`"`).

  * **[OPERATOR]** : a comparison operator; one of the following:
        
        =            # equality (case-sensitive)
        > < >= <=    # numeric ordering
        !=           # not equal
        :            # "has" substring match and test for key (case-sensitive)
            

  * **[VALUE]** : a literal value or a built-in function call; one of the following:
        
        <string>     # "a Unicode string". Don't use apostrophes (`'`) to quote strings.
        <bool>       # true or false
        <number>     # 0, -2, 123456, 3.14156
        <function>   # operators on the right side of '=' or '!=':
                     #   starts_with(<string>)
                     #   ends_with(<string>)
                     #   has_substring(<string> [, ignore_case=false])
                     #   one_of(<string>,...,<string>) for up to 100 strings
                     #   monitoring.regex.full_match(<RE2-string>)
            

Except when used in the `timeSeries.list` method, the `has_substring` filter takes an optional second argument, which specifies whether the match ignores case or not. The default value is `false`, so the default match is case-sensitive: 

    * Case-sensitive: `display_name=has_substring("Demo")`
    * Case-sensitive: `display_name=has_substring("Demo", false)`
    * Case-insensitive: `display_name=has_substring("Demo", true)`

When used in the `timeSeries.list` method, only the `has_substring(<string>)` form is supported.

The `monitoring.regex.full_match` filter takes a regular-expression string in [RE2](https://github.com/google/re2/wiki/Syntax) syntax.




You can use the following operators to group or modify comparisons. `OR` has higher precedence than `AND`. The operators must be written in upper case:
    
    
    (...)        # grouping comparisons
    AND          # conjunction (optional but recommended)
    OR           # disjunction
    

The `AND` operator can be omitted between operators, but it is clearer and less error-prone to include it.

The comparison `x = one_of("a", "b", "c")` is equivalent to the following:
    
    
    (x = "a" OR x = "b" OR x = "c")
    

Only in group definitions, you can use the unary negation operator, `NOT`, before a comparison, but not with an exists operator (`:`) or before a parenthesized expression: 
    
    
    NOT          # negates the following comparison
    

### Filter selectors

Use selectors to limit the filter selections to certain items. In the following sections, braces are used to show repetition. For example, the notation `<x> {OR <y>}` means that you can write any of the following:
    
    
    <x>
    <x> OR <y>
    <x> OR <y> OR <y>
    <x> OR <y> OR <y> OR <y>
    ...
    

#### Project selector

A project selector limits the filter selection to items belonging to a single project or to any one of a set of projects. Each project can be specified by its ID, its number, or by using a regular expression:
    
    
    <project_selector> ::= project '=' (<number> | <string> | monitoring.regex.full_match '(' <RE2-string> ')') {OR project '=' (<number> | <string> | monitoring.regex.full_match '(' <RE2-string> ')')}
    

If your project selector has more than a single comparison, enclose the entire selector in parentheses for better readability. For example:
    
    
    (project=12345 OR project="my-project-id" OR monitoring.regex.full_match("^6789.*") OR monitoring.regex.full_match("some-project-id.*" )) AND resource.type="gce_instance"
    

#### Group selector

A group selector limits the filter selection to items belonging to a single group:
    
    
    <group_selector> ::= group.id '=' <string>
    

For example, the following filter can be used to retrieve a time seriess from each of the VM instances in a group:
    
    
    group.id = 12345 AND
    resource.type = "gce_instance" AND
    metric.type = "compute.googleapis.com/instance/disk/read_bytes_count"
    

The group selector is permitted only in filters passed to the [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method. In addition, group selection requires **aligned data** ; that is, the `projects.timeSeries.list` call must include values for the fields `perSeriesAligner` and `alignmentPeriod`. This is because group membership is itself a kind of time series that must be joined with the metric data, and supplying alignment parameters gives you control over how that join happens. For more information on alignment parameters, see [Aggregating data](https://docs.cloud.google.com/monitoring/custom-metrics/reading-metrics#aggregating). 

#### Resource selector

A resource selector limits the filter selection to resources—or items associated with resources—that have a specific resource type or label values:
    
    
    <resource_selector> ::= <resource_type_expression>
                          | <resource_label_expression>
                          | <resource_type_expression> AND <resource_label_expression>
    
    <resource_type_expression> ::= resource.type '=' <string>
                                 | resource.type ':' <string>
                                 | resource.type '=' starts_with '(' <string>')'
                                 | resource.type '=' ends_with '(' <string> ')'
    
    <r_label_comparison> ::= resource.labels.[KEY] '=' (<string> | <bool>)
                           | resource.labels.[KEY] ':' <string>
                           | resource.labels.[KEY] '=' (starts_with | ends_with) '(' <string> ')'
                           | resource.labels.[KEY] ('=' | '>' | '<' | '>=' | '<=') <number>
    
    <resource_label_expression> ::= <r_label_comparison> {AND <r_label_comparison>}
                                  | <r_label_comparison> {OR <r_label_comparison>}
    

If you use more than one `<r_label_comparison>` in your selector, then enclose them all in parentheses for better readability. For example, the following filter could be used to define a group that includes all Compute Engine VM instances in the USA and Europe.
    
    
    resource.type = "gce_instance" AND
    (resource.labels.zone = starts_with("us-") OR resource.labels.zone = starts_with("europe-"))
    

#### Resource selector for group definitions

Resource selectors used to define group membership use extensions to the `<resource_selector>` syntax:

  * You include filters based on the value of metadata system labels, `metadata.system_labels.[KEY]`, and metadata user labels, `metadata.user_labels.[KEYSTRING]`. We recommend quoting the keys for `metadata.user_labels` because they can contain special characters such as hyphens.

When a selector contains a metadata filter and a resource filter, you must combine them with `AND`; you can't use `OR`. For example, a chart with the following selector displays the CPU utilization for all VM instances with a machine type of `e2-medium` or `e2-micro`:
        
        metric.type="compute.googleapis.com/instance/cpu/utilization"
        resource.type="gce_instance" AND
        (metadata.system_labels."machine_type"="e2-medium" OR
        metadata.system_labels."machine_type"="e2-micro")
        

  * You can use the not-equals operator (`!=`) to compare resource types, resource labels, and metadata. The operator can be used when comparing strings, numbers, Booleans, or the substring functions. For example, `resource.type!=starts_with("gce")` is true if the resource type does not start with `"gce"`.

  * You can use a single `NOT` operator before a resource comparison. For example, `NOT resource.labels.zone="europe"` is true if the resource's zone doesn't include `"europe"`. You can't use `NOT` before an exists operator (`:`) or a parenthesized expression.

  * You can use the "exists" operator (`:`) to test for the existence of keys. For example, the comparison `resource.labels:zone` is true if the label key `zone` is present in the resource.




For example, one of the platform resource metadata keys for VM instances is `spot_instance`. The following filter selector chooses instances that are spot instances:
    
    
    resource.type = "gce_instance" AND metadata.system_labels.spot_instance = true
    

#### Metric selector

A metric selector specifies certain metrics or metric descriptors by limiting the metric type and metric labels. When used with the [`projects.timeSeries.list`](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method, the metric selector must specify a single metric type:
    
    
    <metric_selector> ::= <metric_name_expression> [AND <metric_label_expression>]
    
    <metric_name_expression> ::= metric.type '=' <string>
                               | metric.type ':' <string>
                               | metric.type '=' starts_with '(' <string> ')'
                               | metric.type '=' ends_with '(' <string> ')'
    
    <metric_label_comparison> ::= metric.labels.[KEY] '=' <string> | <bool>
                                | metric.labels.[KEY] ':' <string>
                                | metric.labels.[KEY] '=' starts_with '(' <string> ')'
                                | metric.labels.[KEY] '=' ends_with '(' <string> ')'
                                | metric.labels.[KEY] ('=' | '>' | '<' | '>=' | '<=') <number>
    
    <metric_label_expression> ::= <metric_label_comparison> {[AND] <metric_label_comparison>}
                                | <metric_label_comparison> {OR <metric_label_comparison>}
    

For example, the following filter could be used to retrieve a time series for a specific database instance:
    
    
    metric.type = "cloudsql.googleapis.com/database/state" AND
    (metric.labels.resource_type = "instance" AND
     metric.labels.resource_id = "abc-123456")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
