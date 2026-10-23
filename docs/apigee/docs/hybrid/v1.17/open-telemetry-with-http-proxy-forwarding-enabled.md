---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/open-telemetry-with-http-proxy-forwarding-enabled/
title: OpenTelemetry collector with HTTP proxy forwarding enabled \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:50.745342+00:00
---

# OpenTelemetry collector with HTTP proxy forwarding enabled  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/open-telemetry-with-http-proxy-forwarding-enabled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  OpenTelemetry collector with HTTP proxy forwarding enabled Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/open-telemetry-with-http-proxy-forwarding-enabled.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/open-telemetry-with-http-proxy-forwarding-enabled.html)



When you enable HTTP proxy forwarding, you create a single point through which multiple machines send requests to an external server. If you are behind a corporate proxy or firewall, Apigee may not be able to send metrics to Cloud Monitoring with its default settings. You can set and modify settings directly in the OpenTelemetry collector to have its requests pass through the proxy server.

This topic describes how to configure the OpenTelemetry collector settings using one of the three available environment variables: 

  * `NO_PROXY`: Accepts a list of hostnames or IP addresses whose traffic should not flow through the HTTP proxy.
  * `HTTP_PROXY`: Accepts the URL of the proxy whose server is used for HTTP connections.
  * `HTTPS_PROXY`: Accepts the URL of the proxy whose server is used for HTTPS connections.



## Configure OpenTelemetry collector settings

You can configure the OpenTelemetry collector settings to work with HTTP proxy forwarding by using the `metrics.collector.envVars` property in `overrides.yaml`. The `metrics.collector.envVars` property allows you to pass in the environment variables supported by OpenTelemetry. See [ Proxy support](https://opentelemetry.io/docs/collector/configuration/#proxy-support)in the OpenTelemetry documentation for more details.

You can use the following values for the `metrics.collector.envVars` property: 

  * For an `http` proxy: 
        
        metrics:
        ...
        collector:
          envVars:
            HTTP_PROXY: '_< proxy-address>_'

for example: 
        
        envVars:
            HTTP_PROXY: 'http://1.1.1.1:80'

  * For an `https` proxy: 
        
        metrics:
        ...
        collector:
          envVars:
            HTTPS_PROXY: '_< proxy-address>_'

for example: 
        
        envVars:
            HTTPS_PROXY: 'https://1.1.1.1:80'

  * For addresses that must not use the proxy: 
        
        metrics:
        ...
        collector:
          envVars:
            NO_PROXY: '_< comma-separated-values>_'

for example: 
        
        envVars:
            NO_PROXY: 'http://1.1.1.1:80, http://1.1.1.1:81'




## Apply the changes

Use the following command to apply the changes with the `apigee-telemetry` chart: 
    
    
    helm upgrade telemetry apigee-telemetry/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE
    

**Note:** If you see an error saying `Error: UPGRADE FAILED: "telemetry" has no deployed releases`, replace `upgrade` with `install` and try the command again.

## What's next

  * See [`metrics.collector.envVars`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#logger-envVars) in the Configuration properties reference.
  * Learn how to [Configure forward proxying for API proxies](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/forward-proxy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
