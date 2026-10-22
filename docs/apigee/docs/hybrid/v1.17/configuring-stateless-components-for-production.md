---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configuring-stateless-components-for-production/
title: Configuring stateless Apigee hybrid components for production \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:09.697405+00:00
---

# Configuring stateless Apigee hybrid components for production  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configuring-stateless-components-for-production/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring stateless Apigee hybrid components for production Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configuring-stateless-components-for-production.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/configuring-stateless-components-for-production.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/configuring-stateless-components-for-production.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/configuring-stateless-components-for-production.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/configuring-stateless-components-for-production.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/configuring-stateless-components-for-production.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/configuring-stateless-components-for-production.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/configuring-stateless-components-for-production.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/configuring-stateless-components-for-production.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/configuring-stateless-components-for-production.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/configuring-stateless-components-for-production.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/configuring-stateless-components-for-production.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/configuring-stateless-components-for-production.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/configuring-stateless-components-for-production.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/configuring-stateless-components-for-production.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/configuring-stateless-components-for-production.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/configuring-stateless-components-for-production.html)



For production environments, Apigee hybrid stateless components like MART, Runtime, and Synchronizer require specific resource configurations to ensure stability and performance. This topic provides recommended minimum configurations for these stateless Apigee hybrid components in a production installation. Stateless components run in the `apigee-runtime` node pool, as described in [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-dedicated-nodes). 

These recommendations are based on Apigee's default provisioning for paid organizations and should be considered minimum requirements for a production deployment. You may need to adjust these values based on your specific traffic patterns and load testing results. 

## Production resource recommendations

The following table lists the recommended resource requests and limits for Apigee hybrid components in a production environment. 

Component | CPU Request | Memory Request | CPU Limit | Memory Limit  
---|---|---|---|---  
**MART** | `500m` | `2Gi` | `2000m` | `5Gi`  
**Watcher** | `1` | `4Gi` | `4` | `16Gi`  
**Runtime** | `2` | `6Gi` | 4 | `12Gi`  
**Synchronizer** | `1` | `3Gi` | `2000m` | `5Gi`  
**Metrics Aggregator** | `1` | `10Gi` | `4` | `32Gi`  
**Metrics App** | `500m` | `10Gi` | `2` | `32Gi`  
**Metrics Proxy** | `500m` | `1Gi` | `2` | `32Gi`  
**Metrics Exporters**  
(App/Proxy) | `500m` | `3Gi` | `1` | `10Gi`  
**Logger** | `100m` | `200Mi` | `200m` | `200Mi`  
**Connect Agent** | `500m` | `1Gi` | `500m` | `512Mi`  
**Mint Task Scheduler**  
(If using Monetization) | `100m` | `100Mi` | `2000m` | `4Gi`  
  
## Example overrides

Add the following configurations to your `overrides.yaml` file to configure your Apigee hybrid installation for production. 
    
    
    # Production resource requests for MART
    mart:
      resources:
        requests:
          cpu: 500m
          memory: 2Gi
        limits:
          cpu: 2000m
          memory: 5Gi
    
    # Production resource requests for Watcher
    watcher:
      resources:
        requests:
          cpu: 1
          memory: 4Gi
        limits:
          cpu: 4
          memory: 16Gi
    
    # Production resource requests for environment-scoped components
    envs:
      - name: your-env-name
        runtime:
          resources:
            requests:
              cpu: 2
              memory: 6Gi
            limits:
              memory: 12Gi
        synchronizer:
          resources:
            requests:
              cpu: 1
              memory: 3Gi
            limits:
              cpu: 2000m
              memory: 5Gi
      - name: your-other-env-name
        runtime:
          resources:
            requests:
              cpu: 2
              memory: 6Gi
            limits:
              memory: 12Gi
        synchronizer:
          resources:
            requests:
              cpu: 1
              memory: 3Gi
            limits:
              cpu: 2000m
              memory: 5Gi
    
    # Production resource requests for Metrics
    metrics:
      aggregator:
        resources:
          requests:
            cpu: 1
            memory: 10Gi
          limits:
            cpu: 4
            memory: 32Gi
      app:
        resources:
          requests:
            cpu: 500m
            memory: 10Gi
          limits:
            cpu: 2
            memory: 32Gi
      proxy:
        resources:
          requests:
            cpu: 500m
            memory: 1Gi
          limits:
            cpu: 2
            memory: 32Gi
      appStackdriverExporter:
        resources:
          requests:
            cpu: 500m
            memory: 3Gi
          limits:
            cpu: 1
            memory: 10Gi
      proxyStackdriverExporter:
        resources:
          requests:
            cpu: 500m
            memory: 3Gi
          limits:
            cpu: 1
            memory: 10Gi
    
    # Production resource requests for Logger
    logger:
      resources:
        requests:
          cpu: 100m
          memory: 200Mi
        limits:
          cpu: 200m
          memory: 200Mi
    
    # Production resource requests for Connect Agent
    connectAgent:
      resources:
        requests:
          cpu: 500m
            memory: 1Gi
        limits:
          cpu: 500m
          memory: 512Mi
    
    # Production resource requests for Mint Task Scheduler (if using Monetization)
    mintTaskScheduler:
      resources:
        requests:
          cpu: 100m
          memory: 100Mi
        limits:
          cpu: 2000m
          memory: 4Gi

**Note:** If you are using large message payloads (above 10MB), follow the instructions in [Configure large payload support](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-large-payload-support).

## Applying the configuration

After updating your `overrides.yaml` file, apply the changes to your cluster using `helm upgrade` for each component.

For Helm, apply the changes in order:

Update `apigee-operator`:
    
    
    helm upgrade operator apigee-operator/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

Apply changes for **Logger** and **Metrics** components:
    
    
    helm upgrade telemetry apigee-telemetry/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

Apply changes for **MART** , **Watcher** , **Connect Agent** , and **Mint Task Scheduler** components:
    
    
    helm upgrade ORG_NAME apigee-org/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      -f OVERRIDES_FILE.yaml
    

Apply changes for **Runtime** and **Synchronizer** components for each environment in your installation:
    
    
    helm upgrade ENV_RELEASE_NAME apigee-env/ \
      --namespace APIGEE_NAMESPACE \
      --atomic \
      --set env=ENV_NAME \
      -f OVERRIDES_FILE.yaml
    

## See also

  * [Configuring dedicated node pools](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/configure-dedicated-nodes)
  * [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-production)
  * Configuration properties: 
    * [`connectAgent`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#connectagent)
    * [`envs`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#envs)
    * [`logger`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#logger)
    * [`mart`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#mart)
    * [`metrics`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#metrics)
    * [`mintTaskScheduler`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#minttaskscheduler)
    * [`runtime`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#runtime)
    * [`synchronizer`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#synchronizer)
    * [`watcher`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#watcher)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
