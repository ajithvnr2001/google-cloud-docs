---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-gke-options/
title: Options for Google Kubernetes Engine Pod setup using automatic Envoy injection \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:58:09.896425+00:00
---

# Options for Google Kubernetes Engine Pod setup using automatic Envoy injection  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-gke-options/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Options for Google Kubernetes Engine Pod setup using automatic Envoy injection

This guide provides you with information on additional options and tasks for the automatic Envoy sidecar injector.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## Adding sidecar proxies to existing workloads

After you've installed the sidecar injector to your clusters, sidecar proxies are automatically injected to newly created pods in enabled namespaces. If you have workloads already running prior to enabling the sidecar injector, you must restart them for injection to take place.

For pods managed by Deployment, DaemonSet or StatefulSet controllers, you can run the following:
    
    
    # Deployment
    kubectl rollout restart deployment/DEPLOYMENT_NAME --namespace NAMESPACE
    
    # DaemonSet
    kubectl rollout restart daemonset/DAEMONSET_NAME --namespace NAMESPACE
    
    # StatefulSet
    kubectl rollout restart statefulset/STATEFULSET_NAME --namespace NAMESPACE
    

If you didn't use any of the above controllers to deploy your pod(s), you must delete the pod(s) individually. Afterwards, they are automatically recreated with new sidecar proxies.
    
    
    kubectl delete pod POD_NAME -n NAMESPACE
    

Verify that a sidecar proxy container has been injected in each of your pods:
    
    
    kubectl get pods -n NAMESPACE
    

For example, with the busybox client created above, you should see 2/2 pods running, one for the busybox application itself and one for the injected Envoy sidecar proxy:
    
    
    NAME                      READY   STATUS    RESTARTS   AGE
    busybox-c54f578c9-c9fk4   2/2     Running   183        7d15h
    

## Injection overrides

By default, enabling a namespace enables sidecar proxy injection for all resident pods. Injection can also be selectively configured for different scopes to suit specific needs. For instance, overrides should be used to prevent sidecar proxy injection for proxyless gRPC services.

Note that the injection overrides only apply when the namespace is enabled, and take effect with the following priority: **Pod Annotations > NeverInjectSelector > AlwaysInjectSelector > Default Policy**

### Enabling or disabling injection for specific individual pods

Use the following pod annotation to turn injection on or off for a specific pod in an enabled namespace:
    
    
    ...
    metadata:
      annotations:
        td-injection: "true" / "false"
    

## Customizing traffic interception behavior

By default, all outbound traffic from your application is intercepted and redirected to the Envoy sidecar proxy. The Envoy proxy can then handle the traffic according to the instructions received from Cloud Service Mesh. In some cases, you might want to modify this behavior to bypass the sidecar proxy.

Use the following Pod annotations to exclude traffic from interception and redirection.

### Exclude from interception by outbound IP address range

You can exclude traffic from interception by IP address range.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/excludeOutboundCIDRs: "10.0.0.1/32,169.254.169.254/32"
    

The `cloud.google.com/excludeOutboundCIDRs` Pod annotation is a comma-separated list of outbound IP address ranges in CIDR format. Egress traffic destined to these IP address ranges is not redirected to the Envoy sidecar.

Note that you need to list `169.254.169.254/32` in the Pod annotation to ensure that applications can communicate with the metadata server. If you don't specify the `cloud.google.com/excludeOutboundCIDRs` Pod annotation, traffic interception is configured to exclude the "169.254.169.254/32" outbound CIDR range.

### Include in interception by outbound IP address range

You can include traffic in interception by IP address range.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/includeOutboundCIDRs: "10.0.0.1/32,169.254.169.254/32"
    

The `cloud.google.com/includeOutboundCIDRs` Pod annotation is a comma-separated list of outbound IP address ranges in CIDR format. Egress traffic destined to these IP address ranges is redirected to the Envoy sidecar.

The wildcard character `*` can be used to redirect all outbound traffic. An empty list disables all outbound traffic. The annotation defaults to `*`.

### Exclude from interception by outbound port number

You can exclude traffic from interception and redirection by outbound port number.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/excludeOutboundPorts: "10001, 10002"
    

The `cloud.google.com/excludeOutboundPorts` Pod annotation is a comma-separated list of outbound ports. Egress traffic destined to these ports is excluded from interception and redirection to the Envoy sidecar.

If you don't specify the `cloud.google.com/excludeOutboundPorts` annotation, outbound traffic destined for any port is intercepted and redirected to the Envoy sidecar. This is equivalent to passing the `cloud.google.com/excludeOutboundPorts` annotation with an empty ("") list.

### Include in interception by inbound port number

You can include traffic in interception by inbound port number.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/includeInboundPorts: "10001, 10002"
    

The `cloud.google.com/includeInboundPorts` Pod annotation is a comma-separated list of inbound ports for which traffic is to be redirected to the Envoy sidecar. The wildcard character `*` can be used to configure redirection for all ports. An empty value disables all inbound redirection. The value defaults to an empty string ("").

### Exclude from interception by inbound port number

You can exclude traffic from interception by inbound port number.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/excludeInboundPorts: "10001, 10002"
    

The `cloud.google.com/excludeInboundPorts` Pod annotation is a comma separated list of inbound ports to be excluded from redirection to the Envoy sidecar. The annotation only applies when all inbound traffic (`*`) is being redirected. The value defaults to an empty string ("").

### Enable managed certificates

You can enable managed workload certificates.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/enableManagedCerts: "true"
    

When the Pod annotation `cloud.google.com/enableManagedCerts` is set to `true`, GKE managed workload certificates signed by Certificate Authority Service are inserted and mounted on the sidecar container. The value of the annotation defaults to `false`.

## Configuring sidecar proxy metadata

To support additional Cloud Service Mesh features, sidecar proxies can inherit specific metadata from their encapsulating Pods. There are two ways to accomplish this. Both options append metadata and share the metadata with Cloud Service Mesh when the sidecar proxy connects to Cloud Service Mesh. The options are mutually exclusive.

The first option allows you to specify individual metadata key/value pairs. For example, include the following annotation in your Pod template specification to apply the `"version": "dev"` label to its injected sidecar proxies.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/proxyMetadata: '{"version": "dev"}'
    

The second option appends all of the Pod's labels to the Pod's injected sidecar proxy.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/forwardPodLabels: "true"
    

If you don't specify the `cloud.google.com/forwardPodLabels` annotation, Pod labels will not be appended to the sidecar proxy. Note that the `cloud.google.com/proxyMetadata` and `cloud.google.com/forwardPodLabels` annotations are mutually exclusive. If you set both, `cloud.google.com/forwardPodLabels` takes priority and `cloud.google.com/proxyMetadata` is ignored.

[Config filtering](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management#config-filtering-metadata) then allows Cloud Service Mesh to share a subset of configuration only with the specific proxies that match on this `"version": "dev"` label.

Existing deployments must be restarted for this configuration to take effect.

## Supported pod annotations

Cloud Service Mesh supports the following Pod annotations for sidecar injection. Though additional sidecar injector annotations might work, the following list represents annotations that Cloud Service Mesh supports. To avoid breakage or instability, do not create a dependency on other annotations in your production deployment.

Annotation Name | Value | Description  
---|---|---  
td-injection | Boolean, represented as a string. For example: "`true`" | Specifies whether or not an Envoy sidecar should be automatically injected into the workload.   
cloud.google.com/proxyMetadata | JSON map of key-value pairs. For example: "`'{"version": "dev"}'`"  | Specifies the key/value pairs in a JSON map that should be appended to Envoy metadata.   
cloud.google.com/forwardPodLabels | "true" or "false" | When set to "true", all Pod labels are appended to Envoy metadata, and the "cloud.google.com/proxyMetadata" annotation is ignored. Defaults to "false".   
cloud.google.com/excludeOutboundPorts  | Comma-separated list of outbound ports | Egress traffic that indicates any of these destination ports are excluded from interception/redirection to the Envoy sidecar. This traffic will bypass the Envoy proxy and will not be handled according to Cloud Service Mesh configuration. Defaults to an empty string (i.e. "").   
cloud.google.com/includeInboundPorts  | Comma-separated list of inbound ports | A comma-separated list of inbound ports for which traffic is redirected to the Envoy sidecar. Use the wildcard character `*` to configure redirection for all ports. An empty value disables all inbound redirection. The value defaults to an empty string ("").   
cloud.google.com/excludeInboundPorts  | Comma-separated list of inbound ports | A comma-separated list of inbound ports for which traffic is not redirected to the Envoy sidecar. The annotation applies only when all inbound traffic (*) is being redirected. The value defaults to an empty string ("").   
cloud.google.com/excludeOutboundCIDRs | Comma-separated list of outbound IP ranges in CIDR form. | Egress traffic that indicates any of these destination IPs are excluded from interception/redirection to the Envoy sidecar. This traffic will bypass the Envoy proxy and will not be handled according to Cloud Service Mesh configuration. Defaults to "169.254.169.254/32", which is the range required to communicate with the metadata server. Note that this range is required so if you specify the `excludeOutboundCIDRs` annotation, ensure that you also include "169.254.169.254/32" in addition to any other CIDRs. Ensure that there are no spaces in the comma-separated list.   
cloud.google.com/includeOutboundCIDRs | Comma-separated list of outbound IP ranges in CIDR form. | Egress traffic that indicates any of these destination IPs are included in interception/redirection to the Envoy sidecar. This traffic is directed to the Envoy proxy and is handled according to Cloud Service Mesh configuration. Defaults to "169.254.169.254/32", which is the range required to communicate with the metadata server. Note that this range is required so if you specify the `includeOutboundCIDRs` annotation, ensure that you also include "169.254.169.254/32" in addition to any other CIDRs. Ensure that there are no spaces in the comma-separated list.   
cloud.google.com/enableManagedCerts | Boolean, represented as a string. For example: "`true`" | When set to "`true`", GKE managed workload certificates signed by Certificate Authority Service are inserted and mounted on the sidecar container. The default value is "`false`".   
  
## Uninstalling the sidecar injector

Uninstall the sidecar injector with the following commands:
    
    
    kubectl delete MutatingWebhookConfiguration td-mutating-webhook
    kubectl label namespace default td-injection-
    

**Note:** the commands above uninstall the sidecar injector, but injected sidecar proxies persist until the next rolling restart or manual pod deletion.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
