---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/logging-with-http-proxy-forwarding-enabled/
title: Logging with HTTP proxy forwarding enabled \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:45:31.116295+00:00
---

# Logging with HTTP proxy forwarding enabled  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/logging-with-http-proxy-forwarding-enabled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Logging with HTTP proxy forwarding enabled Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/logging-with-http-proxy-forwarding-enabled.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/logging-with-http-proxy-forwarding-enabled.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/logging-with-http-proxy-forwarding-enabled.html)



## Logging when HTTP proxy forwarding is enabled

When you enable HTTP proxy forwarding, you create a single point through which multiple machines send requests to an external server. For logging, you may not want to have all traffic forwarded through the proxy. 

This procedure explains how to disable HTTP proxy forwarding for specific hosts in your overrides file. 

### Procedure

  1. Disable proxy forwarding for logging for specific hosts by setting the [`logger.envVars`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#logger-envvars) property in `overrides.yaml`: 
         
         logger:
         ...
           envVars:
             NO_PROXY: '_< comma-separated-values>_'

for example: 
         
         envVars:
             NO_PROXY: 'kubernetes.default.svc,oauth2.googleapis.com,logging.googleapis.com'

The `logger.envVars` property allows you to pass in environment variables supported by Fluent Bit. See [NO_PROXY](https://docs.fluentbit.io/manual/administration/http-proxy#no_proxy) in the Fluent Bit documentation. 

  2. Apply the changes with the `apigee-telemetry` chart: 
         
         helm upgrade telemetry apigee-telemetry/ \
           --namespace apigee \
           --atomic \
           -f OVERRIDES_FILE
         

**Note:** If you see an error saying `Error: UPGRADE FAILED: "telemetry" has no deployed releases`, replace `upgrade` with `install` and try the command again.



### See also

  * [`logger.envVars`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/config-prop-ref#logger-envvars) in the Configuration properties reference.
  * [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/forward-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
