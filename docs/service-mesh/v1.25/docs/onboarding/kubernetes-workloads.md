---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/kubernetes-workloads/
title: Onboard Kubernetes workloads \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:26.411256+00:00
---

# Onboard Kubernetes workloads  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/kubernetes-workloads/

You are viewing archived v1.25 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Onboard Kubernetes workloads

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

This page shows you how to onboard Kubernetes workloads with Cloud Service Mesh.

## Deploy Kubernetes services

To deploy Kubernetes services to clusters with Cloud Service Mesh, you must do the following:

  * Create [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#services) for all containers. All [Deployments](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) should have a Kubernetes service attached.

  * Name your service ports. Although GKE lets you define unnamed service ports, Cloud Service Mesh requires that you provide a name for a port that matches the port's protocol.

  * Label your deployments. This lets you use Cloud Service Mesh traffic management features such as splitting traffic between versions of the same service.




The following example deployment and service illustrate these requirements:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: helloserver
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: helloserver
      template:
        metadata:
          labels:
            app: helloserver
        spec:
          containers:
          - image: gcr.io/google-samples/istio/helloserver:v0.0.1
            imagePullPolicy: Always
            name: main
          restartPolicy: Always
          terminationGracePeriodSeconds: 5
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: hellosvc
    spec:
      ports:
      - name: http
        port: 80
        targetPort: 8080
      selector:
        app: helloserver
      type: LoadBalancer

After deploying your services on a cluster with Cloud Service Mesh, be sure to [inject sidecar proxies](https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/kubernetes-workloads#inject_sidecar_proxies).

### Example: Deploy the Online Boutique sample

The Online Boutique sample application in the [`anthos-service-mesh-packages`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages) repository is modified from the original set of manifests in the [`microservices-demo`](https://github.com/GoogleCloudPlatform/microservices-demo) repository. Following best practices, each service is deployed in a separate namespace with a unique service account.

  1. Create the namespaces for the application:
         
         kubectl apply -f \
           DIR_PATH/samples/online-boutique/kubernetes-manifests/namespaces
         

Expected output:
         
         namespace/ad created
         namespace/cart created
         namespace/checkout created
         namespace/currency created
         namespace/email created
         namespace/frontend created
         namespace/loadgenerator created
         namespace/payment created
         namespace/product-catalog created
         namespace/recommendation created
         namespace/shipping created
         

  2. Enable the namespaces for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.25/docs/check-control-plane-implementation).

### Managed (TD)

Apply the default injection label to the namespace:
         
         for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
           kubectl label namespace $ns \
               istio.io/rev- istio-injection=enabled --overwrite
         done;
         

### Managed (Istiod)

**Recommended:** Run the following command to apply the default injection label to the namespace:
         
         for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
             kubectl label namespace $ns \
                 istio.io/rev- istio-injection=enabled --overwrite
           done;
         

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

**Note:** If two control plane revisions appear in the earlier list, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/v1.25/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
              kubectl label namespace $ns \
                  istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            done;
            

### In-cluster

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
        kubectl label namespace $ns \
            istio.io/rev- istio-injection=enabled --overwrite
      done;
    

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
               jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            for ns in ad cart checkout currency email frontend loadgenerator payment product-catalog recommendation shipping; do
              kubectl label namespace $ns \
                  istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            done;
            

  3. Deploy the sample application to the cluster.

     1. Create the service accounts and deployments:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/kubernetes-manifests/deployments
            

Expected output:
            
            serviceaccount/ad created
            deployment.apps/adservice created
            serviceaccount/cart created
            deployment.apps/cartservice created
            serviceaccount/checkout created
            deployment.apps/checkoutservice created
            serviceaccount/currency created
            deployment.apps/currencyservice created
            serviceaccount/email created
            deployment.apps/emailservice created
            serviceaccount/frontend created
            deployment.apps/frontend created
            serviceaccount/loadgenerator created
            deployment.apps/loadgenerator created
            serviceaccount/payment created
            deployment.apps/paymentservice created
            serviceaccount/product-catalog created
            deployment.apps/productcatalogservice created
            serviceaccount/recommendation created
            deployment.apps/recommendationservice created
            serviceaccount/shipping created
            deployment.apps/shippingservice created
            

     2. Create the services:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/kubernetes-manifests/services
            

Expected output:
            
            service/adservice created
            service/cartservice created
            service/checkoutservice created
            service/currencyservice created
            service/emailservice created
            service/frontend created
            service/frontend-external created
            service/paymentservice created
            service/productcatalogservice created
            service/recommendationservice created
            service/shippingservice created
            

     3. Create the service entries:
            
            kubectl apply -f \
             DIR_PATH/samples/online-boutique/istio-manifests/allow-egress-googleapis.yaml
            

Expected output:
            
            serviceentry.networking.istio.io/allow-egress-googleapis created
            serviceentry.networking.istio.io/allow-egress-google-metadata created
            




## Name service ports

To be included in Cloud Service Mesh, service ports must be named, and the name must include the port's protocol, for example:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: ratings
      labels:
        app: ratings
        service: ratings
    spec:
      ports:
      - port: 9080
        **name: http**

The service port name can include a suffix in the following syntax: `name: protocol[-suffix]` where the square brackets indicate an optional suffix that must start with a dash, for example:
    
    
    kind: Service
    metadata:
      name: myservice
    spec:
      ports:
      - number: 3306
        name: mysql
      - number: 80
        **name: http-web**

For metrics to be displayed in the Google Cloud console, the service ports must be named with one of the following protocols: `http`, `http2`, or `grpc`. Service ports named with the `https` protocol are treated as`tcp`, and metrics aren't displayed for those services.

## Inject sidecar proxies

This section covers how to configure sidecar proxy injection with Cloud Service Mesh to enhance network security, reliability, and observability. These functions are abstracted away from the application's primary container and implemented in a common out-of-process proxy (the sidecar), delivered as a separate container in the same Pod. You can use [Cloud Service Mesh's features](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview) without redesigning your production applications to participate in a service mesh.

Automatic sidecar proxy injection (auto-injection) occurs when Cloud Service Mesh detects a namespace label you configure for the workload's Pod. The proxy intercepts all inbound and outbound traffic to the workloads and communicates with Cloud Service Mesh.

#### Permissions required for these tasks

To perform the tasks on this page, you must have the `roles/container.clusterAdmin` or a higher role. See [ Google Kubernetes Engine roles](https://docs.cloud.google.com/iam/docs/understanding-roles#container) for details on the permissions included in this role. 

### Enabling automatic sidecar injection

  1. Enable the namespace for injection. The steps depend on your [control plane implementation](https://docs.cloud.google.com/service-mesh/v1.25/docs/check-control-plane-implementation).

### Managed (TD)

     1. Apply the default injection label to the namespace:
    
    kubectl label namespace NAMESPACE
        istio.io/rev- istio-injection=enabled --overwrite
    

### Managed (Istiod)

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**If you are an existing user with the Managed Istiod control plane:** We recommend that you use default injection, but revision-based injection is supported. Use the following instructions:

     1. Run the following command to locate the available release channels:
            
            kubectl -n istio-system get controlplanerevision
            

The output is similar to the following:
            
            NAME                AGE
            asm-managed-rapid   6d7h
            

NOTE: If two control plane revisions appear in the list above, remove one. Having multiple control plane channels in the cluster is not supported.

In the output, the value under the `NAME` column is the revision label that corresponds to the available [release channel](https://docs.cloud.google.com/service-mesh/v1.25/docs/managed/select-a-release-channel#anthos_service_mesh_versions_per_channel) for the Cloud Service Mesh version.

     2. Apply the revision label to the namespace:
            
            kubectl label namespace NAMESPACE \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

### In-cluster

**Recommended:** Run the following command to apply the default injection label to the namespace:
    
    kubectl label namespace NAMESPACE \
          istio.io/rev- istio-injection=enabled --overwrite
    

**We recommend that you use default injection, but revision-based injection is supported:** Use the following instructions:

     1. Use the following command to locate the revision label on `istiod`:
            
            kubectl get deploy -n istio-system -l app=istiod -o \
               jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
            

     2. Apply the revision label to the namespace. In the following command, `REVISION_LABEL` is the value of the `istiod` revision label that you noted in the previous step.
            
            kubectl label namespace NAMESPACE \
                istio-injection- istio.io/rev=REVISION_LABEL --overwrite
            

  2. Restart the affected pods, using the steps in the next section.

  3. Annotate the `demo` namespace as follows:
         
         kubectl annotate --overwrite namespace NAMESPACE \
         mesh.cloud.google.com/proxy='{"managed":"true"}'
         




#### Restart Pods to update sidecar proxies

**Warning:** Unless you have a load balancer or router setup for [blue-green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html), make sure you test restarting Pods in a staging environment to verify that your services can handle any potential traffic interruption.

With automatic sidecar injection, you can update the sidecars for existing Pods with a Pod restart:

How you restart Pods depends on whether they were created as part of a [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/).

  1. If you used a Deployment, restart the Deployment, which restarts all Pods with sidecars:
         
         kubectl rollout restart deployment -n NAMESPACE

If you didn't use a Deployment, delete the Pods, and they are automatically recreated with sidecars:
         
         kubectl delete pod -n NAMESPACE --all

  2. Check that all the Pods in the namespace have sidecars injected:
         
         kubectl get pod -n NAMESPACE

In the following example output from the previous command, notice that the `READY` column indicates there are two containers for each of your workloads: the primary container and the container for the sidecar proxy.
         
         NAME                    READY   STATUS    RESTARTS   AGE
         WORKLOAD           2/2     Running   0          20s
         ...
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
