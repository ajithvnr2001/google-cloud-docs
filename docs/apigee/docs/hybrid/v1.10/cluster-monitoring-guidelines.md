---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-monitoring-guidelines/
title: Cluster monitoring guidelines \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:11:29.043794+00:00
---

# Cluster monitoring guidelines  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-monitoring-guidelines/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Cluster monitoring guidelines Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cluster-monitoring-guidelines.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/cluster-monitoring-guidelines.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/cluster-monitoring-guidelines.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/cluster-monitoring-guidelines.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/cluster-monitoring-guidelines.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/cluster-monitoring-guidelines.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/cluster-monitoring-guidelines.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/cluster-monitoring-guidelines.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cluster-monitoring-guidelines.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/cluster-monitoring-guidelines.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/cluster-monitoring-guidelines.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/cluster-monitoring-guidelines.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/cluster-monitoring-guidelines.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/cluster-monitoring-guidelines.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/cluster-monitoring-guidelines.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/cluster-monitoring-guidelines.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/cluster-monitoring-guidelines.html)



## Overview

This guide provides guidelines on what to monitor and how to monitor an Apigee Hybrid deployment. It is intended for hybrid cluster administrators and Org admins. 

If you are new to Google Cloud monitoring, please refer to Google Cloud Monitoring documentation for: [Create charts with Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer#configuration-tab) and [How alerting works](https://docs.cloud.google.com/monitoring/alerts). 

Apigee Hybrid clusters provide SLI (Service Level Indicator) metrics to help you understand how application and system services are performing at any given time. You can view a complete list of [Available metrics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/metrics-view#available_metrics). 

Google Cloud Monitoring uses [Resource Type](https://docs.cloud.google.com/monitoring/api/v3/metrics) to identify every SLI metric. There are three common Resource Types used for all Apigee Hybrid metrics. 

  * [`k8s_container`](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) for system level metrics.
  * [`ProxyV2`](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2) for Apigee API Proxy metrics.
  * [`TargetV2`](https://cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2) for Apigee API Target metrics



The Resource Types have common labels that apply to all their associated metrics. For example, all the metrics with `k8s_container` resource type have `cluster_name`, `pod_name`, and `container_name` labels available to use, in addition to the metrics labels. A combination of Resource Type labels and metrics labels should be used to effectively monitor cluster health and performance. 

Alert threshold: In a perfect world, alerting thresholds would be obvious and the provided documentation would list the values that should trigger alerts. In reality, it is less obvious for the Apigee to define - what is acceptable performance and what is a dangerous resource utilization of services and infrastructures. The alert threshold values will vary greatly depending on particular traffic patterns and SLO/SLA agreements. 

An Alert threshold optimization and determination is an on-going process as it can change with the service and infrastructure usage. Use Warning and Critical threshold for notifications and alerting. 

  * **Healthy** : Value is less than the _warning threshold_.
  * **Concerning** : Value greater than the _warning threshold_ , but value is less than the _Critical threshold_.
  * **Critical** : Value > _Critical threshold_.



Customers should use the tools provided to determine the optimal threshold, whether it's the Cloud Monitoring dashboards that customers can create with the MQL provided below or the Apigee's analytics, to identify what "normal" looks like and then tune the alerts thresholds accordingly. 

Hybrid cluster monitoring can be categorized into four different general groups, for example **Traffic** , **Database** , **Apigee control plane** , and **infrastructure** monitoring. The following sections describe these groups in detail: 

**Note:** API Traffic monitoring is the same for Apigee-X and Hybrid clusters. Apigee-X users have access to API traffic SLI metrics such as Proxy, Target, and Policy in the Org's Google Cloud project and can use these SLI metrics for monitoring and alerts. **Tip:** Generally, the "Request Rate" dashboards are useful by themselves for visualization of the traffic pattern. Adding an alert threshold just for request rate SLI metrics could be challenging - unless the traffic pattern/volume is predetermined. However, a request rate chart can provide useful information about any unusual abnormal traffic spikes or dips during debugging any issue related to traffic (read, write, response code, etc).

## Traffic

The Apigee Proxy and Target SLI metrics provide request/response counts and latencies for API Proxy and Targets. The Apigee Policy latency SLI metric provides policy response latencies. These SLI metrics provide coverage for monitoring the Apigee API traffic. 

###  Request Rate 

**Proxy request count**

**Use case** : Use the _proxyv2/request_count_ to monitor the proxy request count. The _proxyv2/request_count_ chart displays the request rate for proxies. This chart is useful to identify which Proxy is receiving a higher request rate, request rate patterns and any abnormal spike in request calls for a particular proxy. Any unexpected abnormal spike in API traffic could be a security concern around a bot or attack on API proxies. Similarly, a large drop in overall traffic cloud indicates issues with clients or connectivity from Apigee upstream components. 

**Resource types** | _ProxyV2_  
---|---  
**Metric** | _proxyv2/request_count_  
**Group By** | _method_ and all [ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | Events like abnormal _request_count spike/drop_ alerts  
**Alert threshold** | _None_  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/ProxyV2
    | metric 'apigee.googleapis.com/proxyv2/request_count'
    | align rate(1m)
    | every 1m
    | group_by [metric.method],
      [value_request_count_aggregate: aggregate(value.request_count)]
      
  
**Target request count**

**Use case** : Use the _targetv2/request_count_ to monitor the Apigee runtime target request count. The targetv2/request_count chart displays the request rate received by the Apigee target. This chart may be useful to see which target is getting a higher request rate, request rate pattern and any abnormal spike in request calls for a particular target. 

**Resource types** | _TargetV2_  
---|---  
**Metric** | _targetv2/request_count_  
**Group By** | _method_ and all [TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | Events like abnormal _request_count spike/drop_ alerts  
**Alert threshold** | _None_  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/TargetV2
    | metric 'apigee.googleapis.com/targetv2/request_count'
    | align rate(1m)
    | every 1m
    | group_by [metric.method, metric.type, metric.endpoint],
      [value_request_count_aggregate: aggregate(value.request_count)]
      
  
### Error Rate

**Proxy error response count**

**Use case** : Use the _proxyv2/response_count_ to monitor the proxy error response rate. The proxyv2/response_count chart displays the request rate for API Proxy. This chart is useful to understand which proxy is getting a higher request error rate or any abnormal error spike in request calls for a particular proxy. 

**Resource types** | _ProxyV2_  
---|---  
**Metric** | _proxyv2/response_count_  
**Filter By** | `response_code != 200` Use a regex to exclude all of 2xx and 3xx `response_code`s, for example:
    
    
    "response_code !=~ 1.*| 2.*|3.*"  
  
**Group By** | _method_ , `response_code`, `fault_code`, `fault_source`, `apigee_fault`, and all [ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | The Proxy response error ratio: _Total response errors / Total response count._

  * Total response errors = Sum of _proxyv2/response_count with filter response_code != 200_
  * Total response count = Sum of _proxyv2/response_count_

  
**Alert threshold** | Depends on the SLO for the installation. Production and non-prodroduction installations may have different thresholds. For example: For production, trigger an event notification if the proxy response 500 error ratio is 5% for 5 mins.  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/ProxyV2
    | metric 'apigee.googleapis.com/proxyv2/response_count'
    | filter (metric.response_code != '200')
    | align rate(1m)
    | every 1m
    | group_by
      [metric.method, metric.response_code, metric.fault_code,
       metric.fault_source, metric.apigee_fault],
      [value_response_count_aggregate: aggregate(value.response_count)]
      
  
**Example Google Cloud operation Alert policy MQL** : 
    
    
    fetch apigee.googleapis.com/ProxyV2::apigee.googleapis.com/proxyv2/response_count
    | {
       filter (metric.response_code == '500')
       ;
       ident
    }
    | group_by drop[metric.response_code ], sliding(5m), .sum
    | ratio
    | scale '%'
    | every (30s)
    | condition val() > 5'%'
      
  
**Target error response count**

**Use case** : Use the _targetv2/response_count_ to monitor the API Target error response rate. The targetv2/response_count chart displays the request rate from API Target. This chart may be useful to identify which target is getting a higher request rate or any abnormal errors spike in request calls. 

**Resource types** | _TargetV2_  
---|---  
**Metric** | _targetv2/response_count_  
**Filter By** | `response_code != 200` Use a regex to exclude all of 2xx and 3xx `response_code`s, for example:
    
    
    "response_code !=~ 1.*| 2.*|3.*"  
  
**Group By** | _method_ and all [TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | The Proxy response error ratio, for example: _Total response errors / Total response count._

  * Total response errors = Sum of _targetv2/response_count with filter response_code != 200_
  * Total response count = Sum of _targetv2/response_count_

  
**Alert threshold** | _Depends on the SLO for the installation. For example: For production, trigger an event notification, If the target response error ratio is 5% for 3 mins._  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/TargetV2
    | metric 'apigee.googleapis.com/targetv2/response_count'
    | filter (metric.response_code != '200')
    | align rate(1m)
    | every 1m
    | group_by
      [metric.method, metric.type, metric.endpoint,
       metric.response_code],
      [value_response_count_aggregate: aggregate(value.response_count)]
      
  
### Latencies

**Proxy latencies percentile**

**Use case** : Use the _proxyv2/latencies_percentile_ to monitor the latency percentile (p50, p90, p95, and p99) of all API proxy responses to a request. The proxyv2/latencies_percentile chart may be useful to identify the latency in Apigee API proxy to your overall API proxy request latency. 

**Resource types** | _ProxyV2_  
---|---  
**Metric** | _proxyv2/latencies_percentile_  
**Filter By** | `percentile = p99`  
**Group By** | _method_ , percentile, and all [ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2) resource type labels  
**Aggregator** | _p99 (99th percentile)_  
**Alert consideration** | _High value of p99 latencies_percentile._  
**Alert threshold** | _Depends on the SLO for the installation. For example: For production, trigger an event notification, If the value of proxy p99 latencies_percentile is 5 seconds for 5 mins._  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/ProxyV2
    | metric 'apigee.googleapis.com/proxyv2/latencies_percentile'
    | filter (metric.percentile == 'p99')
    | group_by 1m,
      [value_latencies_percentile_mean: mean(value.latencies_percentile)]
    | every 1m
    | group_by [metric.method, metric.percentile],
      [value_latencies_percentile_mean_percentile:
         percentile(value_latencies_percentile_mean, 99)]
      
  
**Target latencies percentile**

**Use case** : Use the _targetv2/latencies_percentile_ to monitor the latency percentile (p50, p90, p95, and p99) of all API proxy target responses to a request. The targetv2/latencies_percentile chart identifies the total amount of time for the Apigee API proxy target to respond to a request. This value does not include the Apigee API proxy overhead. 

**Resource types** | _TargetV2_  
---|---  
**Metric** | _targetv2/latencies_percentile_  
**Filter By** | `percentile = p99`  
**Group By** | _method_ , percentile, and all [TargetV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/TargetV2) resource type labels  
**Aggregator** | _p99 (99th percentile)_  
**Alert consideration** | _High value of p99 latencies_percentile._  
**Alert threshold** | _Depends on the SLO for the installation. For example: For production, trigger an event notification, If the value of target p99 latencies_percentile is 5 seconds for 5 mins._  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/ProxyV2
    | metric 'apigee.googleapis.com/proxyv2/latencies_percentile'
    | filter (metric.percentile == 'p99')
    | group_by 1m,
      [value_latencies_percentile_mean: mean(value.latencies_percentile)]
    | every 1m
    | group_by [metric.method, metric.percentile],
      [value_latencies_percentile_mean_percentile:
         percentile(value_latencies_percentile_mean, 99)]
      
  
**Policy latencies percentile**

**Use case** : Use the _policyv2/latencies_percentile_ monitor the processing latency percentile (p50, p90, p95, and p99) of all Apigee policies. The _policyv2/latencies_percentile_ chart may be useful to identify the latency in Apigee API policy to the customer overall API proxy request latency. 

**Resource types** | _ProxyV2_  
---|---  
**Metric** | _proxyv2/latencies_percentile_  
**Filter By** | `percentile = p99`  
**Group By** | _method_ , percentile, and all [ProxyV2](https://docs.cloud.google.com/monitoring/api/resources#tag_apigee.googleapis.com/ProxyV2) resource type labels  
**Aggregator** | _p99 (99th percentile)_  
**Alert consideration** | _High value of p99 latencies_percentile._  
**Alert threshold** | _Depends on the SLO for the installation. For example: For production, trigger an event notification, If the value of proxy p99 latencies_percentile is 5 seconds for 5 mins._  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch apigee.googleapis.com/ProxyV2
    | metric 'apigee.googleapis.com/policyv2/latencies_percentile'
    | filter (metric.percentile == 'p99')
    | group_by 1m,
      [value_latencies_percentile_mean: mean(value.latencies_percentile)]
    | every 1m
    | group_by [metric.policy_name, metric.percentile],
      [value_latencies_percentile_mean_aggregate:
         aggregate(value_latencies_percentile_mean)]
      
  
### Database

#### Cassandra

Apigee Cassandra database service has multiple [Cassandra SLI metrics](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/metrics-view). These SLI metrics can provide comprehensive monitoring for the Apigee Cassandra service. At a minimum, along with Cassandra resource usage (CPU, Mem, and disk volume), the client's read and write request latency should be monitored for Cassandra service health. 

**Cassandra read request rate**

**Use case** : The _cassandra/clientrequest_rate_ (with scope=**Read**) SLI metric provides insight into Cassandra services read request average rate at any given time. This metric helps with the understanding of clients' read request activity level trends. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _cassandra/clientrequest_rate_  
**Filter By** | `scope = Read` and `unit = OneMinuteRate`  
**Group By** | _scope_ , _unit_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | For any potential problems or significant change in clients query patterns; for example a sudden, unexpected spike or drop in read request rate.  
**Alert threshold** | None  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/cassandra/clientrequest_latency'
    | filter (metric.scope == 'Read' && metric.unit == 'OneMinuteRate')
    | group_by 1m,
      [value_clientrequest_latency_mean: mean(value.clientrequest_latency)]
    | every 1m
    | group_by [metric.scope, metric.unit],
      [value_clientrequest_latency_mean_aggregate:
         aggregate(value_clientrequest_latency_mean)]
      
  
**Cassandra write request rate**

**Use case** : The _cassandra/clientrequest_rate_ (with scope=Write) SLI metric provides insight into Cassandra services write request average rate at any given time. This metric helps with the understanding of clients' write request activity level trends. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _cassandra/clientrequest_rate_  
**Filter By** | `scope = Read` and `unit = OneMinuteRate`  
**Group By** | _scope_ , _unit_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | _For any potential problems or significant change in clients query patterns; for example a sudden, unexpected spike or drop in write requests that warrant further investigation._  
**Alert threshold** | _None_  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/cassandra/clientrequest_latency'
    | filter (metric.scope == 'Write' && metric.unit == 'OneMinuteRate')
    | group_by 1m,
      [value_clientrequest_latency_mean: mean(value.clientrequest_latency)]
    | every 1m
    | group_by [metric.scope, metric.unit],
      [value_clientrequest_latency_mean_aggregate:
         aggregate(value_clientrequest_latency_mean)]
      
  
**Cassandra read request latency**

**Use case** : The _cassandra/clientrequest_latency_ (with scope=Read) SLI metric provides Cassandra services read request latency (at 99th percentile, 95th percentile, or 75th percentile). These metrics help with the overall view of Cassandra performance and can indicate any changes in usage patterns or a problem manifesting itself over time. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _cassandra/clientrequest_latency_  
**Filter By** | `scope = Read` and `unit = 99thPercentile`  
**Group By** | _scope_ , _unit_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | If read requests latency SLI consistently shows 99th percentile latency trending upwards continuously.  
**Alert threshold** | Depends on your SLO for Cassandra services. For example: In production, trigger an event notification if the read _clientrequest_latency_ value of 99thPercentile is 5 seconds for 3 minutes  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/cassandra/clientrequest_latency'
    | filter (metric.scope == 'Read' && metric.unit == '99thPercentile')
    | group_by 1m,
      [value_clientrequest_latency_mean: mean(value.clientrequest_latency)]
    | every 1m
    | group_by [metric.scope, metric.unit],
      [value_clientrequest_latency_mean_aggregate:
         aggregate(value_clientrequest_latency_mean)]
      
  
**Cassandra write request latency**

**Use case** : The _cassandra/clientrequest_latency_ (with scope=Write) SLI metric provides Cassandra services write request latency (at 99th percentile, 95th percentile, or 75th percentile). These metrics help with the overall view of Cassandra performance and can indicate any changes in usage patterns or a problem manifesting itself over time. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _cassandra/clientrequest_latency_  
**Filter By** | `scope = Write` and `unit = 99thPercentile`  
**Group By** | _scope_ , _unit_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** |  If write requests latency SLI consistently shows 99th percentile latency trending upwards continuously.  
**Alert threshold** | Depends on your SLO for Cassandra services. For example: in production, trigger an event notification if the write _clientrequest_latency_ value of 99thPercentile is 5 seconds for 3 minutes  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/cassandra/clientrequest_latency'
    | filter (metric.scope == 'Write' && metric.unit == '99thPercentile')
    | group_by 1m,
      [value_clientrequest_latency_mean: mean(value.clientrequest_latency)]
    | every 1m
    | group_by [metric.scope, metric.unit],
      [value_clientrequest_latency_mean_aggregate:
         aggregate(value_clientrequest_latency_mean)]
      
  
## Apigee Control plane

Apigee Synchronizer service SLI metrics provide request and response counts and latencies between the Apigee control plane and the Hybrid runtime plane. Synchronizer instances running in the runtime plane are expected to poll the control plane regularly, download the contracts and make the same available to local runtime instances. 

###  Request rate 

**Upstream request count**

**Use case** : The _upstream/request_count_ metrics indicate the number of requests made by the Synchronizer service to the Apigee control plane. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _upstream/request_count_  
**Filter By** | `container_name = apigee-synchronizer` and `type = CONTRACT`  
**Group By** | _method_ , _type_ , _container_name_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | _Use this for traffic abnormalities, such as an abnormal _request_count_ spike or drop alert._  
**Alert threshold** | _None_  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/upstream/request_count'
    | filter
      (resource.container_name == 'apigee-synchronizer')
      && (metric.type == 'CONTRACT')
    | align rate(1m)
    | every 1m
    | group_by [metric.method, metric.type, resource.container_name],
      [value_request_count_aggregate: aggregate(value.request_count)]
      
  
###  Error rate 

**Upstream response count**

**Use case** : The _upstream/response_count_ SLI metric provides the number of responses the Synchronizer services received from the Apigee control plane. This chart may be useful to identify any connectivity or configuration issue between the Apigee Hybrid Runtime plane and Control plane. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _upstream/request_count_  
**Filter By** | _method_ , _response_type_ , _container_name_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Group By** | __  
**Aggregator** | _sum_  
**Alert consideration** | If there are errors in upstream/response_count metrics with non-200 response codes returned from Apigee Control plane, then its required further investigation into those errors.  
**Alert threshold** | Depends on your SLO for Cassandra services. For example: in production, trigger an event notification if Synchronizer experiences greater than one _response_code_ error every three min.  
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'apigee.googleapis.com/upstream/response_count'
    | filter
      (resource.container_name == 'apigee-synchronizer')
      && (metric.response_code != '200' && metric.type == 'CONTRACT')
    | align rate(1m)
    | every 1m
    | group_by
      [metric.method, metric.response_code, metric.type, resource.container_name],
      [value_response_count_aggregate: aggregate(value.response_count)]
      
  
## Infrastructure

[GKE](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes#kubernetes) and other Kubernetes platforms provide system-level SLI metrics. The SLI metrics labels can be filtered and grouped to monitor a specific container and its resource usage. To monitor the Apigee Runtime cluster infrastructure health and availability, a cluster admin can monitor the container and pod common resource use such as CPU, Mem, disk, and container restart counts. Please follow [GKE documentation](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) for more details on available metrics and labels. 

The following table lists some of the services and the containers you can monitor for each service.

**Service Name** | **Container Name**  
---|---  
**Cassandra** | `apigee-cassandra`  
**Message Processor(MP)** | `apigee-runtime`  
**Synchronizer** | `apigee-synchronizer`  
**Telemetry** | `apigee-prometheus-app`  
`apigee-prometheus-proxy`  
`apigee-prometheus-agg`  
`apigee-stackdriver-exporter`  
  
  
### Containers / Pods

**Restart count**

**Use case** : The _kubernetes.io/container/restart_count_ system SLI metric provides the number of times a container has restarted. This chart may be useful to identify if a container is crashing/restarting frequently. The specific service container can be filtered out by metrics labels for a specific service's container monitoring. 

The following shows using the _kubernetes.io/container/restart_count_ metric for the Cassandra container. You can use this metric for any of the containers in the table above. 

**Resource types** | _k8s_container_  
---|---  
**Metric** | _kubernetes.io/container/restart_count_  
**Filter By** | `namespace_name = apigee` and `container_name =~ .*cassandra.*`  
**Group By** | _cluster_name_ , _namespace_name_ , _pod_name_ , _container_name_ , and all [k8s_container](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_container) resource type labels  
**Aggregator** | _sum_  
**Alert consideration** | If a container is restarting frequently, further investigation is needed for the root cause. There are multiple reasons a container can restart, such as `OOMKilled`, data disk full, and configuration issues, to name a few.  
**Alert threshold** | Depends on the SLO for the installation. For example: For production, trigger an event notification, If a container restarts more often than 5 times within 30 minutes.   
**Cloud Monitoring dashboard MQL query** : 
    
    
    fetch k8s_container
    | metric 'kubernetes.io/container/restart_count'
    | filter
      (resource.container_name =~ '.*cassandra.*'
       && resource.namespace_name == 'apigee')
    | align rate(1m)
    | every 1m
    | group_by
      [resource.cluster_name, resource.namespace_name, resource.pod_name,
       resource.container_name],
      [value_restart_count_aggregate: aggregate(value.restart_count)]
      
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v9ce9cb5b22b62a465ff52c45061a0a6a2d86a80b685e9aa8a182b203fdfbf420/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


