---
url: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-configure/
title: Configuring quotas \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:18.982014+00:00
---

# Configuring quotas  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/quotas-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Configuring quotas Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-configure "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure quotas for your API. At a high level, the steps are:

  1. Add the information about the quota to your gRPC API configuration file.
  2. Deploy your gRPC API configuration file.
  3. Deploy the Extensible Service Proxy (ESP).



For an overview of the functionality provided by quotas, see [About quotas](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-overview).

## Prerequisites

As a starting point, this page assumes that you have:

  * [Configured Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints).
  * [Deployed the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config).
  * [Deployed the API backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend).
  * Configured your API to use an API key. This is needed for Endpoints to identify the Google Cloud project that the calling application is associated with. See [Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/grpc/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key) for more information.



## Adding a quota to your gRPC API configuration file

The following procedure describes adding the required settings to your gRPC API configuration file to set up quotas. For simplicity, this page refers to the gRPC API configuration file as the `api_config.yaml` file.

You add the following three sections to the `api_config.yaml` file:

  * `metrics`: A named metric that counts requests to your API. You provide a name that describes the counter. The name could be a category, such as `read-requests` or `write-requests`. Alternatively, if you are defining a quota for a specific method, you might want to include the method name, for example,`echo-api/echo_requests`.

  * `quota.limits`: Represents a single enforceable limit on a named metric. This is where you configure the allowed number of requests for a metric that you have defined. Currently, only per-minute, per-project limits are supported.

  * `quota.metric_rules`: A `metric_rule` maps methods to metrics (many-to-many). A request to a method allocates a counter for each of the mapped metrics. When you associate a method with a metric, you always specify a cost for the request. You can configure the cost of each method independently. This allows different methods to consume at different rates from the same named metric. If you don't have a complex quota requirement, you can configure the cost of every metric to 1.




To configure quotas on your API:

  1. Open your project's `api_config.yaml` file in a text editor.
  2. Add the `metrics` field at the top level of the file (not indented or nested), after the `apis` field.`
         
         metrics:
           - name: "YOUR_METRIC_NAME"
             display_name: "YOUR_METRIC_DISPLAY_NAME"
                 value_type: INT64
             metric_kind: DELTA`
         

     * Replace `YOUR_METRIC_NAME` with a name that describes the API requests counter.
     * Replace `YOUR_METRIC_DISPLAY_NAME` with the text that is displayed on the **Endpoints** > **Services** > **Quotas** page to identify the metric.
     * The `value_type` field must be `INT64`.
     * The `metric_kind` field must be `DELTA`.
  3. Add a `quota` field at the same level as `metrics`, and add a `limits` field nested within the `quota` section.
         
         quota:
           limits:
             - name: "YOUR_LIMIT_NAME"
               metric: "YOUR_METRIC_NAME"
               unit: "1/min/{project}"
               values:
                 STANDARD: VALUE_FOR_THE_LIMIT
         

     * Replace `YOUR_LIMIT_NAME` with a name that describes the limit.
     * Replace `YOUR_METRIC_NAME` with a previously defined `metric.name`.
     * The `unit` field must be `"1/min/{project}"`. This is the identifier for the per-minute per-project limit.
     * The `values` field must contain `STANDARD`.
     * Replace `VALUE_FOR_THE_LIMIT` with an integer value. This is the number of requests that an application associated with a consumer's Google Cloud project can make in a minute.
  4. Optionally, define additional metrics and limits for each metric.

  5. Add a `metric_rules` line indented under `quota`, after the `limits` section. Within the `metric_rules` section, associate a previously defined metric with a method, as follows:
         
         metric_rules:
           - metric_costs:
               YOUR_METRIC_NAME: YOUR_METRIC_COST
             selector: [METHODS]
         

     * Replace `YOUR_METRIC_NAME` with a previously defined `metric.name`.
     * Replace `YOUR_METRIC_COST` with an integer. For each request, the request counter for the metric is incremented by the number you specify for the cost.
     * For the `selector` field, you can specify one of the following:

       * To associate all methods in all APIs with the `metric_cost` use `selector: "*"`
       * To associate all methods within an API with the `metric_cost` use `selector: YOUR_API_NAME.*`
       * To associate a specific method within an API with the `metric_cost` use `selector: YOUR_API_NAME.YOUR_METHOD_NAME`
  6. Save the `api_config.yaml` file.




### Quota configuration examples

The following three examples show how to configure quotas on your API.

The following example shows how configure the `metric` field:
    
    
    metrics:
      # Define a metric for read requests.
      - name: "read-requests"
        display_name: "Read requests"
        value_type: INT64
        metric_kind: DELTA`

The following example shows how to configure the `quota` and `limits` fields within the `quota` section:
    
    
    metrics:
      # Define a metric for read requests.
      - name: "read-requests"
        display_name: "Read requests"
        value_type: INT64
        metric_kind: DELTA
    quota:
      limits:
        # Define the limit or the read-requests metric.
        - name: "read-limit"
          metric: "read-requests"
          unit: "1/min/{project}"
          values:
            STANDARD: 1000

The following example shows how to configure the `metrics` line after the `limits` section:
    
    
      metrics:
        # Define a metric for read requests.
        - name: "read-requests"
          display_name: "Read requests"
          value_type: INT64
          metric_kind: DELTA
      quota:
        limits:
          # Define the limit or the read-requests metric.
          - name: "read-limit"
            metric: "read-requests"
            unit: "1/min/{project}"
            values:
              STANDARD: 1000
        metric_rules:
          - metric_costs:
              "read-requests": 1
            selector: *
    

## Deploying the `api_config.yaml` file and the ESP

For the quota to take effect, you must:

  1. Deploy the `api_config.yaml` file to Service Management, which updates the configuration in Endpoints. For detailed steps, see [Deploying the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-endpoints-config).
  2. Deploy the ESP. For detailed steps, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/grpc/deploy-api-backend).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
