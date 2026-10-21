---
url: https://docs.cloud.google.com/service-mesh/docs/gateways/
title: Installing and upgrading gateways with Istio APIs \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:51:04.557423+00:00
---

# Installing and upgrading gateways with Istio APIs  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/gateways/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Installing and upgrading gateways with Istio APIs

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh gives you the option to deploy and manage _gateways_ as part of your service mesh. A gateway describes a load balancer that operates at the edge of the mesh and receives incoming or outgoing HTTP/TCP connections. Gateways are primarily used to manage ingress traffic, but you can also configure gateways to manage other types of traffic.

  * Egress gateways: An egress gateway lets you configure a dedicated exit node for traffic leaving the mesh, letting you limit which services can or should access external networks, or to enable secure control of egress traffic to add security to your mesh, for example.

  * Ingress gateways: An ingress gateway lets you configure a dedicated entrance node to receive incoming HTTP/TCP connections.

  * East-west gateways: A proxy for [east-west](https://en.wikipedia.org/wiki/East-west_traffic) traffic to allow service workloads to communicate across cluster boundaries in a multi-primary mesh on different networks. By default, this gateway will be public on the Internet.




This page describes best practices for deploying and upgrading the gateway proxies as well as examples of configuring your own `istio-ingressgateway` and `istio-egressgateway` gateway proxies.

You can deploy gateways in different ways and you can use more than one topology within the same cluster. Refer to [Gateway deployment topologies](https://istio.io/v1.31/docs/setup/additional-setup/gateway/#gateway-deployment-topologies) in the Istio documentation to learn more about these topologies.

## Best practices for deploying gateways

The best practices for deploying gateways depend on whether you are using the managed data plane or the unmanaged data plane.

### Best practices for managed data plane

  * Enable the [managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#managed-data-plane).
  * Add a [managed revision label](https://docs.cloud.google.com/service-mesh/docs/revisions-overview) to a namespace.
  * Deploy and manage the control plane and gateways separately.
  * As a security best practice, deploy gateways in a different namespace from the control plane.
  * Use [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/anthos-service-mesh-proxy-injection) (auto-injection) to inject the proxy configuration for the gateways similar to how you would inject the sidecar proxies for your services.



These best practices:

  * Ensure your managed gateways are automatically kept up-to-date with the latest enhancements and security updates.
  * Offloads management and maintenance of gateway instances to Cloud Service Mesh managed data plane.



### Best practices for unmanaged data plane

  * Deploy and manage the control plane and gateways separately.
  * As a security best practice, deploy gateways in a different namespace from the control plane.
  * Use [automatic sidecar injection](https://docs.cloud.google.com/service-mesh/docs/anthos-service-mesh-proxy-injection) (auto-injection) to inject the proxy configuration for the gateways similar to how you would inject the sidecar proxies for your services.



These best practices:

  * Let your namespace administrators manage gateways without needing elevated privileges to your entire cluster.
  * Let your administrators use the same deployment tooling or mechanism that they use to manage Kubernetes applications to deploy and manage gateways.
  * Give administrators full control over the gateway Deployment, and also simplify operations. When a new upgrade is available or a configuration has changed, administrators update gateway Pods by restarting them. This makes the experience of operating a gateway Deployment the same as operating sidecar proxies for your services.



## Deploy sample gateway

To support users with existing deployment tools, Cloud Service Mesh supports the same ways to deploy a gateway as [Istio](https://istio.io/v1.31/docs/setup/additional-setup/gateway/#deploying-a-gateway): `IstioOperator`, Helm, and Kubernetes YAML. Each method produces the same result. Although you can choose the method you are most familiar with, we recommend that you use the Kubernetes YAML method because it is easier to modify and you can store hydrated manifests in source control.

The following steps show how to deploy a sample gateway.

  1. Create a namespace for the gateway if you don't already have one. Replace `GATEWAY_NAMESPACE` with the name of your namespace.
         
         kubectl create namespace GATEWAY_NAMESPACE
         

  2. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation).

### Managed (TD)

     1. Apply the default injection label to the namespace:
    
    kubectl label namespace GATEWAY_NAMESPACE \
        istio.io/rev- istio-injection=enabled --overwrite
    

### Managed (Istiod)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace GATEWAY_NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

NOTE: If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            kubectl label namespace GATEWAY_NAMESPACE \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

### In-cluster

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace GATEWAY_NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
               jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace GATEWAY_NAMESPACE \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  3. Copy the configuration files for the sample gateways from the [`anthos-service-mesh` repository](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/tree/main/samples/gateways).

  4. Change your directory to the `samples` directory. To ensure you are in the correct directory, run the `ls` command to list the directory contents and then confirm there is a `gateways` directory (which you will access in the next step) and an `online-boutique` directory.

  5. Deploy an ingress or egress gateway. These are located in the `samples/gateways/` directory as is, or modify it as needed.

### Ingress
         
         kubectl apply -n GATEWAY_NAMESPACE -f samples/gateways/istio-ingressgateway
         

### Egress
         
         kubectl apply -n GATEWAY_NAMESPACE -f samples/gateways/istio-egressgateway
         

  6. After you create the deployment, verify that the new services are working correctly:
         
         kubectl get pod,service -n GATEWAY_NAMESPACE
         

Verify that the output is similar to the following:
         
         NAME                                      READY   STATUS    RESTARTS   AGE
         pod/istio-ingressgateway-856b7c77-bdb77   1/1     Running   0          3s
         
         NAME                           TYPE           CLUSTER-IP     EXTERNAL-IP      PORT(S)        AGE
         service/istio-ingressgateway   LoadBalancer   10.24.5.129    34.82.157.6      80:31904/TCP   3s




Manage gateway resources like any other Kubernetes application. The samples in the `anthos-service-mesh-packages` repository are meant for guidance and a quickstart. Customize them according to your needs.

### Gateway selectors

You apply a [Gateway](https://istio.io/v1.31/docs/reference/config/networking/gateway/#Gateway) configuration to the `istio-ingressgateway` and `istio-egressgateway` proxies to manage inbound and outbound traffic for your mesh, letting you specify which traffic you want to enter or leave the mesh. The labels on a gateway deployment's Pods are used by Gateway configuration resources, so it's important that your Gateway selector matches these labels.

For example, in the preceding deployments, the `istio=ingressgateway` label is set on the gateway Pods. To apply a Gateway configuration to these deployments, you need to select the same label:
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: Gateway
    metadata:
      name: gateway
    spec:
      selector:
        istio: ingressgateway
    ...
    

For an example of a Gateway configuration and Virtual Service, see [frontend.yaml](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages/blob/master/samples/online-boutique/istio-manifests/frontend-gateway.yaml) in the Online Boutique sample application.

## Upgrade gateways

### In-place upgrades

For most use cases, you should upgrade your gateways following the in-place upgrade pattern. Because gateways utilize Pod injection, new gateway Pods that are created will automatically be injected with the latest configuration, which includes the version.

If you would like to change the control plane revision in use by the gateway, you can set the `istio.io/rev` label on the gateway Deployment, which will also trigger a rolling restart.

#### Managed control plane

Since Google manages the control plane upgrades for the managed control plane, you can simply restart the gateway Deployment and the new pods will automatically be injected with the latest configuration and version.
    
    
    kubectl rollout restart deployment istio-ingressgateway \
      -n GATEWAY_NAMESPACE
    

#### In-cluster control plane

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

To apply the same pattern to your gateways when you have the in-cluster control plane, you will need to change the control plane revision in use by the gateway. Set the `istio.io/rev` label on the gateway Deployment which will trigger a rolling restart. The steps required depend on whether you need to update the revision label on namespace and/or the gateway pod.

  * If you labeled the namespace for injection, set the `istio.io/rev` label on the namespace to the new revision value:
        
        kubectl label namespace GATEWAY_NAMESPACE \
            istio-injection- istio.io/rev=REVISION \
            --overwrite
        

  * If you enabled injection only for the gateway pod, set the `istio.io/rev` label on the Deployment to the new revision value like the following Kubernetes YAML file:
        
        cat <<EOF > gateway-deployment.yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: istio-ingressgateway
          namespace: GATEWAY_NAMESPACE
        spec:
          selector:
            matchLabels:
              istio: ingressgateway
          template:
            metadata:
              annotations:
                # This is required to tell Cloud Service Mesh to inject the gateway with the
                # required configuration.
                inject.istio.io/templates: gateway
              labels:
                istio: ingressgateway
                istio.io/rev: REVISION
            spec:
              containers:
              - name: istio-proxy
                image: auto # The image will automatically update each time the pod starts.
        EOF
        
        kubectl apply -f gateway-deployment.yaml
        

**Note:** If the `image` does not automatically update with the actual Cloud Service Mesh proxy image, then the container will not be found and an error will occur. See Troubleshoot gateways for next steps.



### Canary upgrades (advanced)

If you are using the in-cluster control plane and would like to more slowly control the rollout of a new control plane revision, you can follow the canary upgrade pattern. You can run multiple versions of a gateway Deployment and ensure everything works as expected with a subset of your traffic. For example, if you want to roll out a new revision, canary, create a copy of your gateway Deployment with the `istio.io/rev=REVISION` label set to the new revision and a new name, for example `istio-ingressgateway-canary`:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: istio-ingressgateway-canary
      namespace: GATEWAY_NAMESPACE
    spec:
      selector:
        matchLabels:
          istio: ingressgateway
      template:
        metadata:
          annotations:
            inject.istio.io/templates: gateway
          labels:
            istio: ingressgateway
            istio.io/rev: REVISION # Set to the control plane revision you want to deploy
        spec:
          containers:
          - name: istio-proxy
            image: auto
    
    

**Note:** If the `image` does not automatically update with the actual Cloud Service Mesh proxy image, then the container will not be found and an error will occur. See Troubleshoot gateways for next steps.

When this Deployment is created, you will then have two versions of the gateway, both selected by the same Service:

`kubectl get endpoints -o "custom-columns=NAME:.metadata.name,PODS:.subsets[*].addresses[*].targetRef.name"`
    
    
    NAME                   PODS
    istio-ingressgateway   istio-ingressgateway-788854c955-8gv96,istio-ingressgateway-canary-b78944cbd-mq2qf
    

**Note:** Unlike application services deployed inside the mesh, you cannot use Istio traffic shifting to distribute the traffic between the gateway versions because their traffic is coming directly from external clients that Istio does not control. Instead, you can control the distribution of traffic by the number of replicas of each Deployment. If you use another load balancer in front of Istio, you may also use that to control the traffic distribution.

If you are satisfied that your applications are working as expected, run this command to transition to the new version by deleting the Deployment with the old istio.io/rev label set:
    
    
    kubectl delete deploy/istio-ingressgateway -n GATEWAY_NAMESPACE
    

If you encountered an issue when testing your application with the new version of the gateway, run this command to transition back to the old version by deleting the Deployment with the new istio.io/rev label set:
    
    
    kubectl delete deploy/istio-ingressgateway-canary -n GATEWAY_NAMESPACE
    

## Advanced configuration

### Deploying Gateways that terminate TLS traffic

Refer to [Set up TLS termination in ingress gateway](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/gateway-tls-termination) document for more details.

### Configure gateway minimum TLS version

For Cloud Service Mesh, the default minimum TLS version for gateway servers is 1.2. You can configure the minimum TLS version using the `minProtocolVersion` field. For more information, see [ServerTLSSettings](https://istio.io/latest/docs/reference/config/networking/gateway/#ServerTLSSettings).

### Unsupported features

If you have `TRAFFIC_DIRECTOR` [control plane implementation](https://docs.cloud.google.com/service-mesh/docs/check-control-plane-implementation) then the following fields or values in Gateway are not supported:

  * ServerTLSSettings.TLSmode with `AUTO_PASSTHROUGH` value
  * ServerTLSSettings.verifyCertificateSpki
  * ServerTLSSettings.verifyCertificateHash



## Troubleshoot gateways

### Failed to update gateway image from `auto`

When you deploy or upgrade a gateway, Cloud Service Mesh inserts `auto` as a placeholder in the `image` field. After the call to a mutating webhook, Cloud Service Mesh automatically replaces this placeholder with the actual Cloud Service Mesh proxy image. If the call to the mutating webhook fails, the `auto` placeholder remains, and the container is not found. This is typically caused by an incorrect namespace label. Ensure that you configured the correct namespace and then deploy or upgrade the gateway again.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
