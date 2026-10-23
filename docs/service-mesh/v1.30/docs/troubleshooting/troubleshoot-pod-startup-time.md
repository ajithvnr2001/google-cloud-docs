---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-pod-startup-time/
title: Pod startup time \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:35.749137+00:00
---

# Pod startup time  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-pod-startup-time/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Pod startup time

This section explains common Cloud Service Mesh problems with pod startup time and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

## Pod startup and Envoy configuration synchronization

A common issue observed during pod startup in some Cloud Service Mesh and Istio environments involves the synchronization between application readiness and Envoy proxy configuration. The problem arises from the concurrent startup of the application container and the Envoy sidecar. The application may signal readiness before the Envoy proxy has completed its initialization and received its configuration from the control plane. This creates a race condition where incoming requests are directed to an unconfigured Envoy proxy that is not ready to receive any traffic. This can lead to requests being dropped, misrouted, or handled incorrectly during the initial phase of application startup, since there is no sidecar to forward any traffic.

## Mitigation strategies

The following sections describe methods that can mitigate this issue.

### Global mesh configuration: `holdApplicationUntilProxyStarts`

The first option is to set `holdApplicationUntilProxyStarts: true` in the Istio mesh configuration. Note that it is off by default. The flag adds hooks to delay application startup until the pod's proxy is ready to accept traffic.

Adding the configuration eliminates this race but may introduce a delay to application readiness times for new pods if it was not previously enabled.

### Readiness probes

Another solution is to implement [readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/) that incorporate both application and Envoy health checks. Readiness probes inform Kubernetes when a pod is ready to accept traffic. Critically, the readiness probe logic should verify not only the application's readiness but also the Envoy proxy's status. This can be achieved by querying Envoy's administrator port for its health status. By combining both checks, Kubernetes prevents traffic from being directed to the pod until both the application and Envoy are fully initialized and configured.

This approach is more flexible and allows for more complicated startup and readiness logic, but it comes at the cost of more complexity.

Create the file `healthcheck.sh` from the following code:
    
    
    #!/bin/sh
    APP_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" \
      http://localhost:8080/health)
    ENVOY_HEALTH=$(curl -s -o /dev/null -w "%{http_code}" \
      http://localhost:9901/ready)
    
    if [[ "$APP_HEALTH" -eq 200 && "$ENVOY_HEALTH" -eq 200 ]]; then
      exit 0
    else
      exit 1
    fi
    

Replace the IP/ports with your application container and Envoy's.

The following YAML file defines a readiness probe that uses the script you previously create:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: my-app-with-envoy
    spec:
      containers:
      - name: application
        <…>
        readinessProbe:
          initialDelaySeconds: 15
          periodSeconds: 10
          failureThreshold: 3
          exec:
            command:
            - /healthcheck.sh # using the script
      - name: envoy
        <…>
    

## What's next

  * [Learn more about `holdApplicationUntilProxyStarts`](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#ProxyConfig-hold_application_until_proxy_starts)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
