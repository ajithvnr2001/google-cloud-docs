---
url: https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics/
title: Custom metrics for Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:37.216359+00:00
---

# Custom metrics for Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Custom metrics for Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use custom metrics with your Application Load Balancers. Custom metrics let you configure your load balancer's traffic distribution behavior to be based on metrics specific to your application or infrastructure requirements, rather than Google Cloud's standard utilization or rate-based metrics. Defining custom metrics for your load balancer gives you the flexibility to route application requests to the backend instances and endpoints that are most optimal for your workload.

For GKE, you can also use custom metrics that come from the service or application that you are running. For details, see [Expose custom metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics).

The load balancer uses the custom metrics values to make the following decisions:

  1. Select which backend virtual machine (VM) instance group or network endpoint group is to receive traffic.
  2. Select which VM instance or endpoint is to receive traffic.

[ ![Load balancing with custom metrics.](https://docs.cloud.google.com/static/load-balancing/images/lb-decisions-custom-metrics.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-decisions-custom-metrics.svg) Load balancing with custom metrics (click to enlarge).

Here are some example use-cases for custom metrics:

  * **Maximize the use of your global compute capacity** by making load balancing decisions based on custom metrics that are most relevant to your application, instead of the default criteria such as regional affinity or network latency.

In case your applications often have backend processing latencies in the order of seconds, you can use your global compute capacity more efficiently by load balancing requests based on custom metrics rather than network latency.

  * **Maximize compute efficiency** by making load balancing decisions based on combinations of metrics unique to your deployment. For example, consider a scenario where your requests have highly variable processing times and compute requirements. In such a scenario, load balancing based solely on the rate of requests per second results in an uneven load distribution. In such a case you might want to define a custom metric that balances load based on a combination of both the rate of requests as well as CPU or GPU utilization to most efficiently use your compute fleet.

  * **Autoscale backends based on custom metrics** that are most relevant to your application requirements. For example, you can define an autoscaling policy to autoscale your backend instances when your configured custom metric exceeds 80%. This is achieved by using traffic-based autoscaling metrics (`autoscaling.googleapis.com|gclb-capacity-fullness`). For more information, see [Autoscaling based on load balancer traffic](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#autoscale-traffic).




## Supported load balancers and backends

Custom metrics are supported for the following Application Load Balancers:

  * Global external Application Load Balancer
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer



Custom metrics are supported with the following backend types:

  * Managed instance groups
  * Zonal NEGs (with `GCE_VM_IP_PORT` endpoints)
  * Hybrid connectivity NEGs



## How custom metrics work

To enable your load balancer to make traffic distribution decisions based on custom metrics, you must first determine what the most relevant metrics are for your specific application. When you know which metrics you want to use, you then configure your backends to start reporting a steady stream of these metrics to your load balancer. Google Cloud lets you report metrics as part of the header of each HTTP response sent from the backends to your load balancer. These metrics are encapsulated in a custom HTTP response header and must follow the [Open Request Cost Aggregation (ORCA)](https://github.com/envoyproxy/envoy/issues/6614) standard.

Metrics can be configured at two levels:

  * At the backend service level, to influence backend (MIG or NEG) selection
  * At the backend level, to influence VM instance or endpoint selection



The following sections describe how custom metrics work.

### Determine which custom metrics influence load balancing decisions

Determining which custom metrics influence load balancing decisions is highly subjective and based on the needs of your applications. For example, if your applications have backend processing latencies in the order of seconds, then you might want to load balance requests based on other custom metrics rather than standard network latencies.

After you have determined which metrics you want to use, you must also determine the maximum utilization threshold for each metric. For example, if you want to use memory utilization as a metric, you must also determine the maximum memory utilization threshold for each backend.

For example, if you configure a metric called `example-custom-metric`, with its maximum utilization threshold set to 0.8, the load balancer dynamically adjusts traffic distribution across backends to keep the `example-custom-metric` metric reported by the backend less than 0.8, as much as possible.

There are two types of custom metrics you can use:

  * **Reserved metrics**. There are five reserved metric names; these names are reserved because they correspond to top-level predefined fields in the ORCA API.

    * `orca.cpu_utilization`
    * `orca.mem_utilization`
    * `orca.application_utilization`
    * `orca.eps`
    * `orca.rps_fractional`

The `mem_utilization`, `cpu_utilization`, and `application_utilization` metrics expect values in the range of `0.0 - 1.00` but can exceed `1.00` for scenarios where resource utilization goes over budget.

  * **Named metrics**. These are metrics that are unique to your application that you specify by using the ORCA `named_metrics` field in the following format:
        
        orca.named_metrics.METRIC_NAME
        

All user-defined custom metrics are specified using this `named_metrics` map in the format of name, value pairs.

Named metrics defined for the `CUSTOM_METRICS` balancing mode must include values in the `0 - 100` range. Named metrics defined for the `WEIGHTED_ROUND_ROBIN` load balancing locality policy have no expected range.




#### Required metrics

To enable your load balancer to use custom metrics for backend VM instance group or network endpoint group selection, you must specify _one or more_ of the following utilization metrics in the ORCA load report sent to the load balancer. `orca.named_metrics` is a map of user-defined metrics in the form of name, value pairs.

  * `orca.cpu_utilization`
  * `orca.application_utilization`
  * `orca.mem_utilization`
  * `orca.named_metrics`



Additionally, to enable your load balancer to use custom metrics to further influence the selection of the backend VM instance or endpoint, you must provide _all_ of the following metrics in the ORCA load report sent to the load balancer. The load balancer uses weights computed from these reported metrics to assign load to individual backends.

  * `orca.rps_fractional` (requests per second)
  * `orca.eps` (errors per second)
  * a utilization metric with the following order of precedence: 
    1. `orca.application_utilization`
    2. `orca.cpu_utilization`
    3. user-defined metrics in the `orca.named_metrics` map



#### Limits and requirements

  * There is a limit of two custom metrics per backend. However, you can perform `dryRun` tests with a maximum of three custom metrics.

If two metrics are provided, the load balancer treats them independently. For example, if you define two dimensions: `custom-metric-util1` and `custom-metric-util2`, the load balancer treats them independently. If a backend is running at a high utilization level in terms of `custom-metric-util1`, the load balancer avoids sending traffic to this backend. Generally, the load balancer tries to keep all backends running with roughly the same _fullness_. Fullness is computed as `currentUtilization` / `maxUtilization`. In this case, the load balancer uses the higher of the two fullness values reported by the two metrics to make load balancing decisions.

  * There is a limit of two custom metrics per backend service. However, you can perform `dryRun` tests with a maximum of three custom metrics. This limit doesn't include the required `orca.eps` and `orca.rps_fractional` metrics. This limit is also independent of metrics configured at the backend level.

  * Both reserved metrics and named metrics can be used together. For example, both `orca.cpu_utilization = 0.5` and a custom metric such as `orca.named_metrics.queue_depth_util = 0.2` can be provided in a single load report.

  * Custom metric names must not contain regulated, sensitive, identifiable, or other confidential information that anyone external to your organization must not see.




#### Available encodings for custom metric specification

  * **JSON**

Sample JSON encoding of a load report:
        
        endpoint-load-metrics-json: JSON {"cpu_utilization": 0.3, "mem_utilization": 0.8, "rps_fractional": 10.0, "eps": 1, "named_metrics": {"custom-metric-util": 0.4}}.
        

  * **Binary Protobuf**

For Protocol Buffers-aware code, this is a binary serialized base64 encoded OrcaLoadReport protobuf in either `endpoint-load-metrics-bin` or in `endpoint-load-metrics: BIN`.

  * **Native HTTP**

Comma separated key-value pairs in `endpoint-load-metrics`. This is a flattened text representation of the OrcaLoadReport:
        
        endpoint-load-metrics: TEXT cpu_utilization=0.3, mem_utilization=0.8, rps_fractional=10.0, eps=1, named_metrics.custom_metric_util=0.4
        

  * **gRPC**

gRPC specification requires the metrics to be provided by using trailing metadata using the `endpoint-load-metrics-bin` key.




### Backend configuration to report custom metrics

After you determine the metrics you want the load balancer to use, you configure your backends to compile the required custom metrics in an ORCA load report and report their values in each HTTP response header sent to the load balancer.

For example, if you chose `orca.cpu_utilization` as a custom metric for a backend, that backend must report the current CPU utilization to the load balancer in each response sent to the load balancer. For instructions, see the report metrics to the load balancer section on this page.

### Load balancer configuration to support custom metrics

To enable the load balancer to use the custom metrics values reported by the backends to make traffic distribution decisions, you must set each backend's balancing mode to `CUSTOM_METRICS` and set the backend service load balancing locality policy to `WEIGHTED_ROUND_ROBIN`.

[ ![How custom metrics work with Application Load Balancers.](https://docs.cloud.google.com/static/load-balancing/images/applb-custom-metrics.svg)](https://docs.cloud.google.com/static/load-balancing/images/applb-custom-metrics.svg) How custom metrics work with Application Load Balancers (click to enlarge).

  * **`CUSTOM_METRICS` balancing mode**. Each of your backends in a backend service must be configured to use the `CUSTOM_METRICS` balancing mode. When a backend is configured with `CUSTOM_METRICS` balancing mode, the load balancer directs traffic to the backends according to the maximum utilization threshold configured for each custom metric.

Each backend can specify a different set of metrics to report. If multiple custom metrics are configured per backend, the load balancer tries to distribute traffic such that all the metrics remain below the configured maximum utilization limits.

Traffic is load balanced across backends based on the load balancing algorithm you choose; for example, the [default `WATERFALL_BY_REGION` algorithm](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy#waterfall-by-region) tries to keep all backends running with the same fullness.

  * **`WEIGHTED_ROUND_ROBIN` load balancing locality policy**. The backend service's load balancing locality policy must be set to `WEIGHTED_ROUND_ROBIN`. With this configuration, the load balancer also uses the custom metrics to select the optimal instance or endpoint within the backend to serve the request.




## Configure custom metrics

To enable your Application Load Balancers to use custom metrics, do the following:

  1. Determine the custom metrics you want to use.
  2. Configure the backends to report custom metrics to the load balancer. You must establish a stream of data that can be sent to the load balancer to be used for load balancing. These metrics must be compiled and encoded in an ORCA load report and then reported to the load balancer by using HTTP response headers.
  3. Configure the load balancer to use the custom metric values being reported by the backends.



### Determine the custom metrics

This step is highly subjective based on the needs of your applications. After you have determined which metrics you want to use, you must also determine the maximum utilization threshold for each metric. For example, if you want to use memory utilization as a metric, you must also determine the maximum memory utilization threshold for each backend.

Before you proceed to configuring the load balancer, make sure you have reviewed the types of custom metrics available to you (reserved and named) and the requirements for metric selection, which are described in the How custom metrics work section on this page.

### Configure backends to report metrics to the load balancer

Custom metrics are reported to load balancers as part of each HTTP response from your application backends by using the ORCA standard.

When using Google Kubernetes Engine, you also have the option to use [custom metrics for load balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/expose-custom-metrics).

This section shows you how to compile the custom metrics in an ORCA load report and report these metrics in _each HTTP response header_ sent to the load balancer.

For example, if you're using HTTP text encoding, the header must report the metrics in the following format.
    
    
    endpoint-load-metrics: TEXT BACKEND_METRIC_NAME_1=BACKEND_METRIC_VALUE_1,BACKEND_METRIC_NAME_2=BACKEND_METRIC_VALUE_2
    

Regardless of the encoding format used, make sure that you remove the `orca.` prefix from the metric name when you build the load report.

Here is a code snippet that shows how to append two custom metrics (`customUtilA` and `customUtilB`) to your HTTP headers. This code snippet shows both native HTTP text encoding and base64 encoding. Note that this example hardcodes the values for `customUtilA` and `customUtilB` only for simplicity. Your load balancer receives the values for the metrics that you determined are to influence load balancing.
    
    
    ...
    type OrcaReportType int
    
    const (
            OrcaText OrcaReportType = iota
            OrcaBin
    )
    
    type HttpHeader struct {
            key   string
            value string
    }
    
    const (
            customUtilA = 0.2
            customUtilB = 0.4
    )
    
    func GetBinOrcaReport() HttpHeader {
            report := &pb.OrcaLoadReport{
                    NamedMetrics: map[string]float64{"customUtilA": customUtilA, "customUtilB": customUtilB}}
            out, err := proto.Marshal(report)
            if err != nil {
                    log.Fatalf("failed to serialize the ORCA proto: %v", err)
            }
            return HttpHeader{"endpoint-load-metrics-bin", base64.StdEncoding.EncodeToString(out)}
    }
    
    func GetHttpOrcaReport() HttpHeader {
            return HttpHeader{
                    "endpoint-load-metrics",
                    fmt.Sprintf("TEXT named_metrics.customUtilA=%.2f,named_metrics.customUtilB=%.2f",
                            customUtilA, customUtilB)}
    }
    
    func GetOrcaReport(t OrcaReportType) HttpHeader {
            switch t {
            case OrcaText:
                    return GetHttpOrcaReport()
            case OrcaBin:
                    return GetBinOrcaReport()
            default:
                    return HttpHeader{"", ""}
            }
    }
    ...
    

### Configure the load balancer to use custom metrics

For the load balancer to use these custom metrics when selecting a backend, you need to set the balancing mode for each backend to `CUSTOM_METRICS`. Additionally, if you want the custom metrics to also influence endpoint selection, you set the load balancing locality policy to `WEIGHTED_ROUND_ROBIN`.

The steps described in this section assume you have already deployed a load balancer with zonal NEG backends. However, you can use the same `--custom-metrics` flags demonstrated here to update any existing backend by using the `gcloud compute backend-services update` command.

  1. You can set a backend's balancing mode to `CUSTOM_METRICS` when you add the backend to the backend service. You use the `--custom-metrics` flag to specify your custom metric and the threshold to be used for load balancing decisions.
         
         gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
             --network-endpoint-group=NEG_NAME \
             --network-endpoint-group-zone=NEG_ZONE \
             [--global | region=REGION] \
             --balancing-mode=CUSTOM_METRICS \
             --custom-metrics='name="BACKEND_METRIC_NAME_1",maxUtilization=MAX_UTILIZATION_FOR_METRIC_1' \
             --custom-metrics='name="BACKEND_METRIC_NAME_2",maxUtilization=MAX_UTILIZATION_FOR_METRIC_2'
         

Replace the following:

     * `BACKEND_SERVICE_NAME`: the name of the backend service
     * `NEG_NAME`: the name of the zonal or hybrid NEG
     * `NEG_ZONE`: the zone where the NEG was created
     * `REGION`: for regional load balancers, the region where the load balancer was created
     * `BACKEND_METRIC_NAME`: the custom metric names used here must match the custom metric names being reported by the backend's ORCA report
     * `MAX_UTILIZATION_FOR_METRIC`: the maximum utilization that the load balancing algorithms must target for each metric

For example, if your backends are reporting two custom metrics, `customUtilA` and `customUtilB` (as demonstrated in the Configure backends to report metrics to the load balancer section), you use the following command to configure your load balancer to use these metrics:
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        [--global | region=REGION] \
        --balancing-mode=CUSTOM_METRICS \
        --custom-metrics='name="customUtilA",maxUtilization=0.8' \
        --custom-metrics='name="customUtilB",maxUtilization=0.9'
    

Alternatively, you can provide a list of custom metrics in a structured JSON file:
    
    {
    "name": "METRIC_NAME_1",
    "maxUtilization": MAX_UTILIZATION_FOR_METRIC_1,
    "dryRun": true
    }
    {
    "name": "METRIC_NAME_2",
    "maxUtilization": MAX_UTILIZATION_FOR_METRIC_2,
    "dryRun": false
    }

Then attach the metrics file in JSON format to the backend as follows:
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        [--global | region=REGION] \
        --balancing-mode=CUSTOM_METRICS \
        --custom-metrics-file='BACKEND_METRIC_FILE_NAME'
    

If you want to test whether the metrics are being reported without actually affecting the load balancer, you can set the `dryRun` flag to `true` when configuring the metric as follows:
    
    gcloud compute backend-services add-backend BACKEND_SERVICE_NAME \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        [--global | region=REGION] \
        --balancing-mode=CUSTOM_METRICS \
        --custom-metrics 'name="BACKEND_METRIC_NAME",maxUtilization=MAX_UTILIZATION_FOR_METRIC,**dryRun=true** '
    

When a metric is configured with `dryRun` set to `true`, the metric is reported to Monitoring but isn't actually used by the load balancer.

To reverse this, update the backend service with the `dryRun` flag set to `false`.
    
    gcloud compute backend-services update-backend BACKEND_SERVICE_NAME \
        --network-endpoint-group=NEG_NAME \
        --network-endpoint-group-zone=NEG_ZONE \
        [--global | region=REGION] \
        --balancing-mode=CUSTOM_METRICS \
        --custom-metrics 'name="BACKEND_METRIC_NAME",maxUtilization=MAX_UTILIZATION_FOR_METRIC_,**dryRun=false** '
    

If all your custom metrics are configured with `dryRun` set to `true`, setting the balancing mode to `CUSTOM_METRICS` or the load balancing locality policy to `WEIGHTED_ROUND_ROBIN` has no effect on the load balancer.

**Note:** To see other flags supported by the `gcloud compute backend-services update-backend` command, such as `--clear-custom-metrics`, see the [gcloud compute backend-services update-backend reference page](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update-backend).
  2. To configure the load balancer to use the custom metrics to influence endpoint selection, you set the backend service load balancing locality policy to `WEIGHTED_ROUND_ROBIN`.

For example, if you have a backend service that is already configured with the appropriate backends, you configure the load balancing locality policy as follows:
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             [--global | region=REGION] \
             --custom-metrics='name=BACKEND_SERVICE_METRIC_NAME,dryRun=false' \
             --locality-lb-policy=WEIGHTED_ROUND_ROBIN
         

As demonstrated previously for the backend level metrics, you can also provide a list of custom metrics in a structured JSON file at the backend service level. Use the `--custom-metrics-file` field to attach the metrics file to the backend service.




## What's next

  * [Troubleshoot issues with external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs)
  * [Troubleshoot issues with internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/troubleshooting-l7-ilb)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
