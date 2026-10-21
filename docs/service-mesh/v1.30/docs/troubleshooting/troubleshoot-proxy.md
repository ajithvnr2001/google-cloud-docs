---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-proxy/
title: Resolving workload startup issues in Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:31:41.972956+00:00
---

# Resolving workload startup issues in Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-proxy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Resolving workload startup issues in Cloud Service Mesh

This document explains common Cloud Service Mesh problems and how to resolve them. If you need additional assistance, see [Getting support](https://docs.cloud.google.com/service-mesh/v1.30/docs/getting-support).

## Gateway fails to start with distroless proxy when a privileged port is exposed

By default distroless proxy starts with non-root permissions which in some cases might cause bind failures on privileged ports. If you see errors similar to the following during the proxy startup, then additional securityContext needs to be applied for a gateway deployment.
    
    
      Error adding/updating listener(s) 0.0.0.0_80: cannot bind '0.0.0.0:80': Permission denied
    

The following example is the yaml for an egress gateway deployment:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: istio-egressgateway
    spec:
      selector:
        matchLabels:
          app: istio-egressgateway
          istio: egressgateway
      template:
        metadata:
          annotations:
            # This is required to tell Anthos Service Mesh to inject the gateway with the
            # required configuration.
            inject.istio.io/templates: gateway
          labels:
            app: istio-egressgateway
            istio: egressgateway
        spec:
          containers:
          - name: istio-proxy
            image: auto # The image will automatically update each time the pod starts.
            resources:
              limits:
                cpu: 2000m
                memory: 1024Mi
              requests:
                cpu: 100m
                memory: 128Mi
          **# Allow binding to all ports (such as 80 and 443)
          securityContext:
            sysctls:
            - name: net.ipv4.ip_unprivileged_port_start
              value: "0"
          serviceAccountName: istio-egressgateway **
    

## Connection Refused when reaching a Cloud Service Mesh endpoint

You might intermittently experience connection refused (`ECONNREFUSED`) errors with communication from your clusters to your endpoints, for example Memorystore Redis, Cloud SQL, or any external service your application workload needs to reach.

This can occur when your application workload initiates faster than the istio-proxy (`Envoy`) container and tries to reach an external endpoint. Because at this stage istio-init (`initContainer`) has already executed, there are iptables rules in place redirecting all outgoing traffic to `Envoy`. Since istio-proxy is not ready yet, the iptables rules will redirect traffic to a sidecar proxy that is not yet started and therefore, the application gets the `ECONNREFUSED` error.

The following steps detail how to check if this is the error you are experiencing:

  1. Check the stackdriver logs with the following Filter to identify which pods had the problem.

The following example shows a typical error message:
         
         Error: failed to create connection to feature-store redis, err=dial tcp   192.168.9.16:19209: connect: connection refused
         [ioredis] Unhandled error event: Error: connect ECONNREFUSED
         

  2. Search for an occurrence of the problem. If you are using legacy Stackdriver, then use `resource.type="container"`.
         
         resource.type="k8s_container"
         textPayload:"$ERROR_MESSAGE$"
         

  3. Expand the latest occurrence to obtain the name of the pod and then make note of the `pod_name` under `resource.labels`.

  4. Obtain the first occurrence of the issue for that pod:
         
         resource.type="k8s_container"
         resource.labels.pod_name="$POD_NAME$"
         

Example output:
         
         E 2020-03-31T10:41:15.552128897Z
         post-feature-service post-feature-service-v1-67d56cdd-g7fvb failed to create
         connection to feature-store redis, err=dial tcp 192.168.9.16:19209: connect:
         connection refused post-feature-service post-feature-service-v1-67d56cdd-g7fvb
         

  5. Make note of the timestamp of the first error for this pod.

  6. Use the following filter to see the pod startup events.
         
         resource.type="k8s_container"
         resource.labels.pod_name="$POD_NAME$"
         

Example output:
         
         I 2020-03-31T10:41:15Z spec.containers{istio-proxy} Container image "docker.io/istio/proxyv2:1.3.3" already present on machine  spec.containers{istio-proxy}
         I 2020-03-31T10:41:15Z spec.containers{istio-proxy} Created container  spec.containers{istio-proxy}
         I 2020-03-31T10:41:15Z spec.containers{istio-proxy} Started container  spec.containers{istio-proxy}
         I 2020-03-31T10:41:15Z spec.containers{APP-CONTAINER-NAME} Created container  spec.containers{APP-CONTAINER-NAME}
         W 2020-03-31T10:41:17Z spec.containers{istio-proxy} Readiness probe failed: HTTP probe failed with statuscode: 503  spec.containers{istio-proxy}
         W 2020-03-31T10:41:26Z spec.containers{istio-proxy} Readiness probe failed: HTTP probe failed with statuscode: 503  spec.containers{istio-proxy}
         W 2020-03-31T10:41:28Z spec.containers{istio-proxy} Readiness probe failed: HTTP probe failed with statuscode: 503  spec.containers{istio-proxy}
         W 2020-03-31T10:41:31Z spec.containers{istio-proxy} Readiness probe failed: HTTP probe failed with statuscode: 503  spec.containers{istio-proxy}
         W 2020-03-31T10:41:58Z spec.containers{istio-proxy} Readiness probe failed: HTTP probe failed with statuscode: 503  spec.containers{istio-proxy}
         

  7. Use the timestamps of errors and istio-proxy startup events to confirm the errors are happening when `Envoy` is not ready.

If the errors occur while the istio-proxy container is not ready yet, it is normal to obtain connection refused errors. In the preceding example, the pod was trying to connect to Redis as soon as `2020-03-31T10:41:15.552128897Z` but by `2020-03-31T10:41:58Z` istio-proxy was still failing readiness probes.

Even though the istio-proxy container started first, it is possible that it did not become ready fast enough before the app was already trying to connect to the external endpoint.

If this is the problem you are experiencing, then continue through the following troubleshooting steps.

  8. Annotate the config at the pod level. This is _only_ available at the pod level and not at a global level.
         
         annotations:
         proxy.istio.io/config: '{ "holdApplicationUntilProxyStarts": true }'
         

  9. Modify the application code so that it checks if `Envoy` is ready before it tries to make any other requests to external services. For example, on application start, initiate a loop that makes requests to the istio-proxy health endpoint and only continues once a 200 is obtained. The istio-proxy health endpoint is as follows:
         
         http://localhost:15020/healthz/ready
         




## Race condition during sidecar injection between Vault and Cloud Service Mesh

When using `vault` for secrets management, sometimes `vault` injects sidecar before `istio`, causing that Pods get stuck in `Init` status. When this happens, the Pods created get stuck in Init status after restarting any deployment or deploying a new one. For example:
    
    
    E 2020-03-31T10:41:15.552128897Z
    post-feature-service post-feature-service-v1-67d56cdd-g7fvb failed to create
    connection to feature-store redis, err=dial tcp 192.168.9.16:19209: connect:
    connection refused post-feature-service post-feature-service-v1-67d56cdd-g7fvb
    

This issue is caused by a race condition, both Istio and `vault` inject the sidecar and Istio must be the last doing this, the `istio` proxy is not running during init containers. The `istio` init container sets up iptables rules to redirect all traffic to the proxy. Since it is not running yet, those rules redirect to nothing, blocking all traffic. This is why the init container must be last, so the proxy is up and running immediately after the iptables rules are set up. Unfortunately, the order is not deterministic, so if Istio is injected first it breaks.

To troubleshoot this condition, allow the IP address of `vault` so the traffic going to the Vault IP is not redirected to the Envoy Proxy which is not ready yet and therefore blocking the communication. To achieve this, a new annotation named `excludeOutboundIPRanges` should be added.

For managed Cloud Service Mesh, this is only possible at Deployment or Pod level under `spec.template.metadata.annotations`, for example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    ...
    ...
    ...
    spec:
      template:
        metadata:
          annotations:
            traffic.sidecar.istio.io/excludeOutboundIPRanges:
    

For in-cluster Cloud Service Mesh, there is an option to set it as a global one with an IstioOperator under `spec.values.global.proxy.excludeIPRanges`, for example:
    
    
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    spec:
      values:
        global:
          proxy:
            excludeIPRanges: ""
    

After adding the annotation, restart your workloads.

## Identify the proxy image type used in the cluster

To identify which proxy image type (`default` or `distroless`) a specific pod uses, you can inspect the pod specification.

Run the following command to check the image used by the `istio-proxy` container:
    
    
    kubectl get pod POD_NAME -n NAMESPACE -o jsonpath='{.spec.containers[?(@.name=="istio-proxy")].image}'
    

  * If the image path does not contain `-distroless` in the tag or suffix, it uses the **`default`** image.
  * If the image path contains `-distroless` in the tag or suffix, it uses the **`distroless`** image.



### Verify Configuration Intent

The image type can be configured in two ways (Annotation takes precedence over MeshConfig):

  1. **Pod Annotation** : Check if the pod has the `sidecar.istio.io/proxyImageType` annotation.
         
         kubectl get pod POD_NAME -n NAMESPACE -o jsonpath='{.metadata.annotations["sidecar.istio.io/proxyImageType"]}'
         

  2. **MeshConfig** : Check the `defaultConfig.image.imageType` setting in your `istio-RELEASE_CHANNEL` ConfigMap in the `istio-system` namespace.




**Note** : For clusters with the managed `TRAFFIC_DIRECTOR` control plane:

  * For clusters provisioned directly with a managed `TRAFFIC_DIRECTOR` control plane, only `distroless` images are supported. Overrides to other image types are ignored.
  * For clusters migrated to the `TRAFFIC_DIRECTOR` control plane (such as those migrated from CSM-ISTIOD), the image type defaults to the `default` image but you can opt-in to `distroless` using `MeshConfig` or pod annotation. Overrides to other image types (such as `debug`) are unsupported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
