---
url: https://docs.cloud.google.com/appengine/docs/flexible/migrating-to-split-health-checks/
title: Migrate from legacy to split health checks \u00a0|\u00a0 App Engine flexible environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:40:09.436006+00:00
---

# Migrate from legacy to split health checks  |  App Engine flexible environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/flexible/migrating-to-split-health-checks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Flexible environment ](https://docs.cloud.google.com/appengine/docs/flexible)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Migrate from legacy to split health checks Stay organized with collections  Save and categorize content based on your preferences. 

As of September 15, 2019, if you're using the legacy health checks, your application will continue to run and receive health checks but you won't be able to deploy new versions of your application.

This page explains upgrading from the legacy health checks to [split health checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#updated_health_checks).

## Verifying your health check type

To verify the type of health checks your application is using, run the following command:
    
    
    gcloud app describe
    

If your application is using split health checks, the description should include the following information:
    
    
    featureSettings:
        splitHealthChecks: true
    

## Understanding key differences

Before upgrading to split health checks, consider the following important differences between legacy and split health checks:

  * **HTTP requests for split health checks are not forwarded by default.** By contrast, legacy health checks forward to the `/_ah/health` path in your application by default.

  * **Forwarded split health checks must return`200 OK` when healthy and ready.** Legacy health checks consider the following HTTP codes as healthy: `200`, `301`, `302`, `303`, `307`, `401`, `402`, `403`, `404`, `405`.




If you do not specify a [liveness check path](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_path) or a [readiness check path](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_path), by default split health checks only confirm that the VM instance and the Docker container are running. As long as these conditions hold, the VM will continue to receive traffic and remain alive regardless of the app's internal state.

By contrast, when legacy health checks are enabled, if your app's `/_ah/health` path starts returning unhealthy HTTP error codes (e.g. `5XX`) then legacy health checks will start failing and the VM will stop receiving traffic and be restarted.

If your app depends on the default legacy health check behavior, set the [liveness check path](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_path) and the [readiness check path](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_path) accordingly.

## Converting legacy health check options

Each legacy health check option can be rewritten using split health checks as follows:

Option | Maintaining same behavior in split health checks  
---|---  
`enable_health_check` | If `True` or unset, configure [`liveness_check.path`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_path) and [`readiness_check.path`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_path) to a path on the app that returns `200 OK` when the app is healthy.  
`check_interval_sec` | Configure [`liveness_check.check_interval_sec`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_interval) and [`readiness_check.check_interval_sec`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_interval) to the same value.  
`timeout_sec` | Configure [`liveness_check.timeout_sec`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_timeout) and [`readiness_check.timeout_sec`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_timeout) to the same value.  
`unhealthy_threshold` | Configure [`readiness_check.failure_threshold`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_failure) to the same value.  
`healthy_threshold` | Configure [`liveness_check.success_threshold`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_success) and [`readiness_check.success_threshold`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_success) to the same value.  
`restart_threshold` | Configure [`liveness_check.failure_threshold`](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_failure) to the same value. Note the value of your `check_interval_sec` option multiplied by the `failure_threshold` option is the time it'll take for an unhealthy VM to be taken down.  
  
## Enabling split health checks

To migrate from legacy health checks to split health checks and avoid seeing elevated `5xx` status codes, complete the following steps:

  1. Understand the important differences between legacy and split health checks.

  2. Convert legacy health check options for each version in your application.

Alternatively, you can customize the `liveness_check` or `readiness_check` section in the `app.yaml` file for each version. For examples, see [Liveness checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#liveness_checks) and [Readiness checks](https://docs.cloud.google.com/appengine/docs/flexible/reference/app-yaml#readiness_checks).

  3. Run the following command:
         
         gcloud app update --split-health-checks --project [YOUR_PROJECT_ID]

  4. If you used customized settings for legacy health checks, you must remove the `health_check` section from your `app.yaml` file.

  5. Deploy a new major version of your app to start using liveness and readiness health checks.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
