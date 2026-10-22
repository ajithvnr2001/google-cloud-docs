---
url: https://docs.cloud.google.com/api-gateway/docs/troubleshoot/
title: Troubleshooting overview \u00a0|\u00a0 API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:22.573950+00:00
---

# Troubleshooting overview  |  API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshooting overview

This page provides general troubleshooting information for API Gateway.

## Cannot run "gcloud api-gateway" commands

To run the `gcloud api-gateway ...` commands, you must have updated the [Google Cloud CLI](https://cloud.google.com/sdk/docs) and enabled the necessary Google services. See [Configuring your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env) for more.

## Command "gcloud api-gateway api-configs create" says service account does not exist

If you run the `gcloud api-gateway api-configs create ...` command and receive an error in the form:
    
    
    ERROR: (gcloud.api-gateway.api-configs.create) FAILED_PRECONDITION:
    Service Account "projects/-/serviceAccounts/service_account_email" does not exist

Rerun the command but this time include the `--backend-auth-service-account` option to explicitly specify the email address of the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to use:
    
    
    gcloud api-gateway api-configs create CONFIG_ID \
      --api=API_ID --openapi-spec=API_DEFINITION \
      --backend-auth-service-account=SERVICE_ACCOUNT_EMAIL

Ensure that you have already assigned the necessary permissions to the service account as described in [Configuring your development environment](https://docs.cloud.google.com/api-gateway/docs/configure-dev-env).

## Determining the source of API error responses

If requests to your deployed API result in an error (HTTP status codes `400` through `599`), it may not be clear from the response itself if the error originates from the Gateway or from your backend. To determine this:

  1. Go to the Logs Explorer page and select your project.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Filter to the relevant gateway resource using the following Log query:
         
         resource.type="apigateway.googleapis.com/Gateway"
         resource.labels.gateway_id="GATEWAY_ID"
         resource.labels.location="GCP_REGION"

Where:

     * GATEWAY_ID specifies the name of the gateway.
     * GCP_REGION is the Google Cloud region for the deployed gateway.
  3. Find the log entry matching the HTTP error response you want to investigate. For example, filter by `httpRequest.status`.

  4. Inspect the contents of the field `jsonPayload.responseDetails`.




If the value of the `jsonPayload.responseDetails` field is `"via_upstream"`, then the error response originates from your backend and you will need to troubleshoot your backend directly. If it is any other value, then the error response originates from the Gateway; see the following sections of this document for further troubleshooting tips.

## API request returns an HTTP 403 error

If a request to a deployed API returns an HTTP `403` error to the API client, it means the requested URL is valid but access is forbidden for some reason.

A deployed API has the permissions associated with roles granted to the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) that you used when you created the API config. Typically, the reason for the HTTP `403` error is that the service account does not have the necessary permissions to access the backend service.

If you defined the API and the backend service in the same Google Cloud Project, ensure that the service account has the `Editor` role assigned to it, or the role necessary to access the backend service. For example, if the backend service is implemented using [Cloud Run functions](https://docs.cloud.google.com/functions/docs), ensure that the service account has the `Cloud Function Invoker` role assigned to it.

## API request returns an HTTP `401` or `500` error

If a request to a deployed API returns an HTTP `401` or `500` error to the API client, there may be a problem using the service account used when you created the API config to call your backend service.

A deployed API has the permissions associated with roles granted to the [service account](https://docs.cloud.google.com/iam/docs/service-accounts) that you used when you created the API config. The service account is checked to make sure that it both exists, and can be used by the API gateway when the API is deployed.

If the service account is deleted or disabled after the gateway is deployed, the following sequence of events may occur:

  1. Immediately after the service account is deleted or disabled, you may see 401 HTTP responses in your gateway logs. If the `jsonPayload.responseDetails` field is set to `"via_upstream"` in the log entry's `jsonPayload`, this indicates that deleting or disabling the service account is the cause of the error.

  2. You may also see an HTTP `500` error without any corresponding log entry in the API Gateway's logs. If there are no requests to your gateway immediately after the service account is deleted or disabled, you may not see the HTTP 401 responses, but the HTTP `500` errors without corresponding API gateway logs are an indication that the gateway's service account may no longer be active.




If the backend for the failing request is another Google Cloud API (such as `bigquery.googleapis.com`), you will see 401 HTTP responses in your gateway logs with the `jsonPayload.responseDetails` field set to `"via_upstream"`. This is because API Gateway authenticates to backends with an [ID Token](https://docs.cloud.google.com/authentication/token-types#id) while other Google Cloud APIs require an [Access Token](https://docs.cloud.google.com/authentication/token-types#access).

## API request returns an HTTP 500 error for a quota-enforced method

If you receive the following error, the gateway couldn't allocate quota for your request:
    
    
    HTTP/2 500
    {"code":500,"message":"Failed to call Service Control Quota."}

This error commonly occurs when you call a method that has a [quota](https://docs.cloud.google.com/api-gateway/docs/quotas-overview) configured, but the quota metrics no longer exist for the API. On a gRPC gateway, the same failure is returned as the gRPC status code `Internal`.

### Confirm the cause in your gateway logs

  1. Go to the Logs Explorer page and select your project.

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Run the following log query:
         
         resource.type="apigateway.googleapis.com/Gateway"
         resource.labels.gateway_id="GATEWAY_ID"
         jsonPayload.responseDetails="service_control_quota_error"
         httpRequest.status=500

Where GATEWAY_ID specifies the name of the gateway.

The query filters on the status code as well as on `jsonPayload.responseDetails` because API Gateway uses the same `responseDetails` value for every quota rejection. A request that legitimately exceeded its quota produces the same value with an `httpRequest.status` of `429`.

  3. Inspect the `jsonPayload.apiConfig` and `jsonPayload.apiMethod` fields of any matching entry. They identify the API config and the method whose quota configuration is invalid.




### Why an API config can have an invalid quota configuration

You define quota metrics and limits in an API config, but API Gateway applies them to the entire API. Each time you create an API config, the metrics and limits it declares _replace_ the ones declared by the API's previous API configs. Only the values from the most recently created API config are enforced.

In contrast, the metrics consumed by each method are defined in the API config that the gateway serves. If a gateway runs an older API config, it asks Service Control to allocate quota against a metric that exists in its own config, but might not exist in the API. If the metric doesn't exist, the allocation call fails, and the gateway rejects the request.

For example, the following sequence leaves the first gateway broken:

  1. You create API config `config-v1`, which declares the metric `quota-metric-v1`, and deploy it to `gateway-1`.
  2. You create API config `config-v2` for the same API, which declares the metric `quota-metric-v2`, and deploy it to `gateway-2`.



`gateway-2` works, but requests to the quota-enforced methods of `gateway-1` start failing, because `quota-metric-v1` is no longer defined for the API.

The following changes can cause errors for any gateway that's still deployed with an earlier API config:

  * Renaming or removing a metric.
  * Changing which metric a quota limit applies to.
  * Changing the metric named in the per-method quota costs (`x-google-quota` for OpenAPI documents, or `quota.metric_rules` for gRPC service configs).



Changing only the _value_ of a limit doesn't cause errors. However, because limits are also applied at the API level, the new value is enforced on every gateway of that API, including gateways deployed with an earlier API config.

### Compare the deployed quota configurations

  1. List your gateways and the API config that each one serves:
         
         gcloud api-gateway gateways list \
          --format="table(name.basename(),apiConfig)"

  2. List the API configs of the affected API, most recently created first:
         
         gcloud api-gateway api-configs list --api=API_ID \
          --format="table(name.basename(),createTime:sort=1:reverse)"

The first entry is the API config whose quota metrics and limits are enforced for the whole API. Sort with the `--format` flag as shown: this command doesn't support the `--sort-by` flag, and it doesn't return API configs in a predictable order.

  3. Display the API definition that an API config was created from:
         
         gcloud api-gateway api-configs describe CONFIG_ID --api=API_ID \
          --view=FULL --format="value(openapiDocuments[0].document.contents)" \
          | tr '_-' '/+' | base64 --decode

The `tr` command is required because the `contents` field is base64url encoded, which `base64 --decode` can't read directly.

For a gRPC API, the quota configuration is in the service config rather than in an OpenAPI document, so replace `openapiDocuments[0].document.contents` with `managedServiceConfigs[0].contents`.

  4. Run the command in step 3 for the API config at the top of the list from step 2, and then for each of the other API configs that step 1 shows as still deployed to a gateway.

  5. Compare the results. Every metric that an older API config charges its methods against must also be defined in the most recently created API config. If a metric is missing from that config, the gateways that serve the older API config fail.




### Restore a valid quota configuration

Audit your quota metrics and limits to ensure that they are consistent across all active configurations. To do this, take one of the following actions:

  * Update every gateway of the API to use the most recently created API config, as described in [Update a gateway](https://docs.cloud.google.com/api-gateway/docs/deploying-api#update_a_gateway).
  * Create a new API config that declares every metric used by the API configs that are still deployed, and keep the existing gateways on their current API configs.



To avoid allocation errors, keep metric names consistent across the API configs of an API. When you change a quota, change the value of the limit rather than the name of the metric.

## High latency API requests

Like Cloud Run and Cloud Run functions, API Gateway is subject to "cold start" latency. If your gateway has not received traffic for 15 to 20 minutes, requests made to your gateway within the first 10 to 15 seconds of the cold start will experience 3 to 5 seconds of latency.

If the issue persists after the initial "warm up" period, check the request logs of the backend service(s) you configured in your API Config. For example, if the backend service is implemented using [Cloud Run functions](https://docs.cloud.google.com/functions/docs), check the Cloud Logging entries of the associated Cloud Function request log.

## Cannot view log information

If your API is responding correctly, but the logs contain no data, it typically means that you have not enabled all of the Google services required by API Gateway.

API Gateway requires that you enable the following Google Cloud services:

Name | Service name  
---|---  
API Gateway API | `apigateway.googleapis.com`  
Service Management API | `servicemanagement.googleapis.com`  
Service Control API | `servicecontrol.googleapis.com`  
  
To enable required services:

###  Google Cloud console

  1. In the Google Cloud console, go to the **APIs & Services > API Library** page.

[Go to API Library](https://console.cloud.google.com/apis/library)

  2. On the **API Library** page, enter the required API name into the search bar.
  3. In the search results, select the API page.
  4. On the API page, click **Enable**.
  5. Repeat these steps for each of the services listed in the preceding table.



### Google Cloud CLI

Use the following commands to enable the services:
    
    
    gcloud services enable apigateway.googleapis.com
    gcloud services enable servicemanagement.googleapis.com
    gcloud services enable servicecontrol.googleapis.com

For more information about the `gcloud` services, see [`gcloud` services](https://docs.cloud.google.com/sdk/gcloud/reference/services).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
