---
url: https://docs.cloud.google.com/endpoints/docs/openapi/quotas-configure/
title: Configuring quotas \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:30.427060+00:00
---

# Configuring quotas  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/quotas-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Configuring quotas Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/quotas-configure "View this page for the Cloud Endpoints gRPC docs")

**Beta**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to configure quotas for your API. At a high level, the steps are:

  1. Add the information about the quota to your OpenAPI configuration file.
  2. Deploy your OpenAPI configuration file.
  3. Deploy the Extensible Service Proxy (ESP).



For an overview of the functionality provided by quotas, see [About quotas](https://docs.cloud.google.com/endpoints/docs/openapi/quotas-overview).

## Prerequisites

As a starting point, this page assumes that you have:

  * [Configured Cloud Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/configure-endpoints)
  * [Deployed the Endpoints configuration](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-endpoints-config).
  * [Deployed the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).
  * Configured your API to use an API key. This is needed for Endpoints to identify the Google Cloud project that the calling application is associated with. See [Sharing APIs protected by API key](https://docs.cloud.google.com/endpoints/docs/openapi/restricting-api-access-with-api-keys#sharing_apis_protected_by_api_key) for more information.



## Adding a quota to your OpenAPI document

The following procedure describes adding the required extensions to your OpenAPI document to set up quotas. For simplicity, this page refers to the OpenAPI document as the `openapi.yaml` file and provides the OpenAPI extensions only in YAML format.

You add the following three sections to the `openapi.yaml` file:

  * `x-google-management.metrics`: A named metric that counts requests to your API. You provide a name that describes the counter. The name can be a category, such as `read-requests` or `write-requests`. Alternatively, if you are defining a quota for a specific method, you might want to include the method name, for example, `echo-api/echo_requests`

  * `x-google-management.quota.limits`: Represents a single enforceable limit on a named metric. This is where you configure the allowed number of requests for a metric that you have defined. Currently, only per-minute, per-project limits are supported.

  * `x-google-quota.metricCosts`: The `metricCosts` maps methods to metrics (many-to-many). A request to a method allocates a counter for each of the mapped metrics. When you associate a method with a metric, you always specify a cost for the request. You can configure the cost of each method independently. This allows different methods to consume at different rates from the same named metric. If you don't have a complex quota requirement, you can configure the cost of every metric to 1.




To configure quotas on your API:

  1. Open your project's `openapi.yaml` file in a text editor.
  2. If you don't already have it, add the `x-google-management` extension at the root of the file (not indented or nested) before the section that defines the paths.
  3. Add the `metrics` definition indented under `x-google-management`.
         
         x-google-management:
           metrics:
             - name: "YOUR_METRIC_NAME"
               displayName: "YOUR_METRIC-DISPLAY_NAME"
               valueType: INT64
               metricKind: DELTA
         

     * Replace `YOUR_METRIC_NAME` with a name that describes the API requests counter.
     * Replace `YOUR_METRIC_DISPLAY_NAME` with the text that is displayed on the **Endpoints** > **Services** > **Quotas** page to identify the metric.
     * The `valueType` field must be `INT64`.
     * The `metricKind` field must be `DELTA`.
  4. Add a `quota` field at the same level as `metrics`, and add a `limits` field nested within the `quota` section.
         
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
  5. Optionally, define additional metrics and limits for each metric.

  6. In the `paths` section of the `openapi.yaml` file, add the `x-google-quota` extension indented under each method that you want to apply a quota to.
         
         x-google-quota:
           metricCosts:
             YOUR_METRIC_NAME: YOUR_METRIC_COST
         

     * Replace `YOUR_METRIC_NAME` with a previously defined `metric.name`.
     * Replace `YOUR_METRIC_COST` with an integer. For each request, the request counter for the metric is incremented by the number you specify for the cost.
  7. Save the `openapi.yaml` file.




### Quota configuration examples

The following three examples show how to configure quotas on your API.

The following example shows how to configure the `metric` field:
    
    
    x-google-management:
      metrics:
        # Define a metric for read requests.
        - name: "read-requests"
          displayName: "Read requests"
          valueType: INT64
          metricKind: DELTA

The following example shows how to configure the `quota` and `limits` fields within the `quota` section:
    
    
    x-google-management:
      metrics:
        # Define a metric for read requests.
        - name: "read-requests"
          displayName: "Read requests"
          valueType: INT64
          metricKind: DELTA
      quota:
        limits:
          # Define the limit or the read-requests metric.
          - name: "read-limit"
            metric: "read-requests"
            unit: "1/min/{project}"
            values:
              STANDARD: 1000

The following example shows how to configure the `x-google-quota` extension in the `paths` section:
    
    
    x-google-management:
      metrics:
        # Define a metric for read requests.
        - name: "read-requests"
          displayName: "Read requests"
          valueType: INT64
          metricKind: DELTA
      quota:
        limits:
          # Define the limit or the read-requests metric.
          - name: "read-limit"
            metric: "read-requests"
            unit: "1/min/{project}"
            values:
              STANDARD: 1000
    paths:
      "/echo":
        post:
          description: "Echo back a given message."
          operationId: "echo"
          produces:
          - "application/json"
          responses:
            200:
              description: "Echo"
              schema:
                $ref: "#/definitions/echoMessage"
          parameters:
          - description: "Message to echo"
            in: body
            name: message
            required: true
            schema:
              $ref: "#/definitions/echoMessage"
          x-google-quota:
            metricCosts:
              "read-requests": 1
          security:
          - api_key: []

See [OpenAPI extensions](https://docs.cloud.google.com/endpoints/docs/openapi/openapi-extensions) for more examples and detailed descriptions of the `x-google-management` and `x-google-quota` extensions.

## Deploying the `openapi.yaml` file and the ESP

For the quota to take effect, you must:

  1. Deploy the `openapi.yaml` file to Service Management, which updates the configuration in Endpoints.
  2. Deploy the ESP. The steps for deploying the ESP vary by the backend that your API is deployed on.



For detailed steps, see [Deploying the API backend](https://docs.cloud.google.com/endpoints/docs/openapi/deploy-api-backend).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
