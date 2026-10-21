---
url: https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces/
title: Trace outbound traffic with Cloud Trace \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:08:20.947590+00:00
---

# Trace outbound traffic with Cloud Trace  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Trace outbound traffic with Cloud Trace Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document explains how to configure distributed request tracing for Secure Web Proxy by using [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview).

For information about the concepts, key benefits, and architecture details, see [Distributed tracing overview](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview).

## Before you begin

  1. Complete the [initial setup steps](https://docs.cloud.google.com/secure-web-proxy/docs/initial-setup-steps).
  2. Enable the Compute Engine API, Network Services API, and Cloud Trace API in your project.
         
         gcloud services enable \
             compute.googleapis.com \
             networkservices.googleapis.com \
             cloudtrace.googleapis.com
         

  3. Make sure that you have an active Secure Web Proxy gateway instance deployed. For more information, see [Deploy a Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart).

  4. To generate HTTP-level distributed trace spans and propagate [W3C trace context headers](https://docs.cloud.google.com/trace/docs/trace-context#http-requests) for HTTPS requests, you must [enable TLS inspection](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection) on your Secure Web Proxy gateway.




### Roles and permissions

To obtain the permissions that are required to configure telemetry policies and view traces, request your administrator to grant you the following Identity and Access Management (IAM) roles:

  * To create, update, or delete telemetry policies: [Network Services Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/networkservices#networkservices.admin) (`roles/networkservices.admin`) or [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * To view and analyze trace spans in the Google Cloud console: [Cloud Trace User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.user) (`roles/cloudtrace.user`)
  * To export trace spans to Trace, make sure that the following service accounts have the [Cloud Trace Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudtrace#cloudtrace.agent) (`roles/cloudtrace.agent`):

    * Compute Engine service agent: `service-PROJECT_NUMBER@compute-system.iam.gserviceaccount.com`
    * Network Security service agent: `service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com`
    * Client virtual machine (VM) service accounts, if client applications generate or propagate spans



## Telemetry policy configuration schema

To define a telemetry policy in a YAML file, use the following schema:
    
    
        name: projects/PROJECT_ID/locations/REGION/telemetryPolicies/POLICY_NAME
        telemetryTarget:
          resources:
          - "//networkservices.googleapis.com/projects/PROJECT_ID/locations/REGION/gateways/GATEWAY_NAME"
        description: "OPTIONAL_DESCRIPTION"
        tracingConfiguration:
          samplingRate: SAMPLING_RATE
          parentBasedSampling:
            enabled: true
      

The following table describes the fields in a telemetry policy:

Field | Type | Description  
---|---|---  
`name` | String | Unique identifier of the telemetry policy.  
`telemetryTarget.resources` | List of strings | Resource URLs of the Secure Web Proxy gateways to which this policy applies. Your gateways must reside in the same region as the policy. Format: `//networkservices.googleapis.com/projects/PROJECT_ID/locations/REGION/gateways/GATEWAY_NAME` Alternatively, use the short name format: `projects/PROJECT_ID/locations/REGION/gateways/GATEWAY_NAME`.   
`description` | String | Optional. This field provides a human-readable description of the telemetry policy.  
`tracingConfiguration.samplingRate` | Float | Proportion of requests to trace, specified as a decimal between `0.0` (0%) and `1.0` (100%). For example, `0.01` samples 1% of requests.  
`tracingConfiguration.parentBasedSampling.enabled` | Boolean | Indicates whether you want to enable upstream trace sampling decisions (`true` or `false`).  
  
## Configure distributed tracing

To apply a tracing policy to your Secure Web Proxy gateway by using the Google Cloud CLI, do the following:

  1. Create a YAML policy file named `swp-tracing-policy.yaml`.
         
         cat <<EOF > swp-tracing-policy.yaml
         name: projects/PROJECT_ID/locations/REGION/telemetryPolicies/my-swp-tracing-policy
         telemetryTarget:
           resources:
             - "//networkservices.googleapis.com/projects/PROJECT_ID/locations/REGION/gateways/GATEWAY_NAME"
         description: "Distributed tracing policy for the Secure Web Proxy gateway"
         tracingConfiguration:
           samplingRate: 0.01
           parentBasedSampling:
             enabled: true
         EOF
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `REGION`: region where your Secure Web Proxy gateway is deployed, such as `us-central1`
     * `GATEWAY_NAME`: name of your Secure Web Proxy gateway instance
  2. Import the telemetry policy by using the [`gcloud beta network-services telemetry-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/import):
         
         gcloud beta network-services telemetry-policies import my-swp-tracing-policy \
             --source=swp-tracing-policy.yaml \
             --location=REGION
         

  3. Verify that the policy is applied by using the [`gcloud beta network-services telemetry-policies describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/describe):
         
         gcloud beta network-services telemetry-policies describe my-swp-tracing-policy \
             --location=REGION
         




### Attach or detach target gateways

To update the policy definition or attach multiple regional gateways, do the following:

  1. Update the `telemetryTarget.resources` list in the `swp-tracing-policy.yaml` file to include all target gateway resource URIs.
         
         telemetryTarget:
           resources:
             - "//networkservices.googleapis.com/projects/PROJECT_ID/locations/us-central1/gateways/prod-swp-uc1"
             - "//networkservices.googleapis.com/projects/PROJECT_ID/locations/us-central1/gateways/staging-swp-uc1"
         

  2. Import the updated telemetry policy by using the [`gcloud beta network-services telemetry-policies import` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-services/telemetry-policies/import):
         
         gcloud beta network-services telemetry-policies import my-swp-tracing-policy \
             --source=swp-tracing-policy.yaml \
             --location=REGION
         

Replace the following:

     * `PROJECT_ID`: ID of your Google Cloud project
     * `REGION`: region where your Secure Web Proxy gateway is deployed, such as `us-central1`



## View and analyze traces in Trace

  1. In the Google Cloud console, go to the **Trace Explorer** page.

[Go to Trace Explorer](https://console.cloud.google.com/traces/explorer)

  2. Select your Google Cloud project.

  3. In the **Filter** field, search for traces by using various attributes.

  4. Click any trace in the scatter plot or timeline view to inspect span details, such as total duration, proxy processing latency, and external server IP details.




## Correlate traces with logs and metrics

Secure Web Proxy provides correlation between traces, logs, and metrics:

  * **Log-trace correlation** : every proxy transaction log entry written to Cloud Logging contains a `trace` field with the format: `projects/PROJECT_ID/traces/TRACE_ID`.

    * In the **Logs Explorer** , click the log entry and then select **View trace details** to navigate directly to the corresponding span in Trace.
    * In Trace, click **Show logs** on the **Trace Details** pane to view all transaction logs that are associated with that request.
  * **Metric correlation** : compare latency spikes observed in Cloud Monitoring metrics, such as `networkservices.googleapis.com/https/total_latencies`, with trace span breakdowns to identify whether a latency spike occurred within the proxy or at the external origin server.




## What's next

  * [Distributed tracing overview](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview)
  * [Troubleshoot distributed tracing errors](https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-distributed-tracing-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
