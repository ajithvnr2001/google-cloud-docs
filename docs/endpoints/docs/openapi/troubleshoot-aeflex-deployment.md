---
url: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-aeflex-deployment/
title: Troubleshooting App Engine flexible deployment \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:49:24.249867+00:00
---

# Troubleshooting App Engine flexible deployment  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-aeflex-deployment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Troubleshooting App Engine flexible deployment Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | gRPC

This document presents troubleshooting techniques for Cloud Endpoints deployments in App Engine flexible environments. If you receive an error back from a request to your API, see [Troubleshooting response errors](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot-response-errors) for information on troubleshooting the error.

## Deployment errors

This section describes how to troubleshoot errors from `gcloud app deploy`.

**Error message** | **Troubleshooting**  
---|---  
Your deployment has failed to become healthy in the allotted time and therefore was rolled back. If you believe this was an error, try adjusting the `app_start_timeout_sec` setting in the `readiness_check` section.  |  Check that your `app.yaml` file has a `readiness_check` section with a value for `app_start_timeout_sec`. If it doesn't exist, add the section and set the value of `app_start_timeout_sec` to higher than the default of 300 seconds. For more information, see [ readiness checks](https://docs.cloud.google.com/appengine/docs/flexible/nodejs/reference/app-yaml#readiness_checks). Make sure that you enable all of the Google Cloud services that Endpoints and ESP require. See [Checking required services](https://docs.cloud.google.com/endpoints/docs/openapi/troubleshoot#required_services) for details.  Ensure that the VPC associated with your App Engine flexible app has a [local static route with the `0.0.0.0/0` destination and default internet gateway next hop](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet). If using [private internal-only services](https://docs.cloud.google.com/appengine/docs/flexible/disable-external-ip#limitations) ensure PGA is enabled on the selected subnet.   
  
### Error messages about `rollout_strategy`

When you configure `app.yaml` before deploying, you must add the `endpoints_api_service` section. The Extensible Service Proxy (ESP) needs the settings that you specify in this section to obtain the configuration for your service. You must specify either a configuration ID in the `config_id` field, or include the `rollout_strategy: managed` option, but not both. This option configures ESP to use the latest deployed service configuration. When you specify this option, up to 5 minutes after you deploy a new service configuration, ESP detects the change and automatically begins using it. We recommend that you specify this option instead of a specific configuration ID for ESP to use. For example:
    
    
    endpoints_api_service:
      name: example-project-12345.appspot.com
      rollout_strategy: managed
    

If the `endpoints_api_service` section doesn't include the information that ESP needs to obtain a service configuration, one of the following messages is displayed:

**Error message** | **Troubleshooting**  
---|---  
`config_id` is forbidden when `rollout_strategy` is set to `"managed"` |  You cannot specify both a configuration ID and `rollout_strategy: managed`. Unless you have a reason for using a specific configuration ID, we recommend that you remove the `config_id: [YOUR_CONFIG_ID]` from `app.yaml` and rerun `gcloud app deploy`.   
`config_id` must be specified when `rollout_strategy` is unspecified or set to `"fixed"` |  This error message is displayed when either `app.yaml` doesn't include the `rollout_strategy: managed` or `rollout_strategy` is set to `fixed` and you haven't specified a configuration ID. Unless you have a reason for using a specific configuration ID, we recommend that you add `rollout_strategy: managed` to the `endpoints_api_service` section of `app.yaml` and rerun `gcloud app deploy`.   
  
## Viewing logs on an instance

App Engine crash and system logs provide information on why the application failed to launch or perform as intended. You can find further debugging information in the Endpoints log.

  1. In the Google Cloud console, SSH into your virtual machine. See [connecting to an instance](https://docs.cloud.google.com/appengine/docs/flexible/python/debugging-an-instance#connecting_to_the_instance) for more information.

  2. Use a text viewer such as `tail`:
         
         tail -f /var/log/nginx/error.log
         




## What's next

  * [App Engine flexible environment logs](https://cloud.google.com/logging/docs/view/service/appengine-logs#appengine-vms)
  * [Viewing Logs](https://cloud.google.com/logging/docs/view/logs-explorer-interface)
  * [Using Cloud Logging in App Engine apps](https://cloud.google.com/appengine/articles/logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
