---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/onlineboutique-install-kpt/
title: Deploying the Online Boutique sample application \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:00.508293+00:00
---

# Deploying the Online Boutique sample application  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/onlineboutique-install-kpt/

You are viewing archived v1.19 Service Mesh documentation.

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
  * [ v1.19 ](https://docs.cloud.google.com/service-mesh/v1.19/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.19/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Deploying the Online Boutique sample application

This guide explains how to install the Online Boutique sample application to demonstrate Cloud Service Mesh. If you haven't installed Cloud Service Mesh, see the [installation guide](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh).

## Downloading and deploying the sample

To deploy the application, you first need to download the Online Boutique manifests from the [`anthos-service-mesh-packages`](https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages) repo using `kpt`. The Online Boutique sample application in the `anthos-service-mesh-packages` repo is modified from the original set of manifests in the [`microservices-demo`](https://github.com/GoogleCloudPlatform/microservices-demo) repo. Following best practices, each service is deployed in a separate namespace with a unique service account.

  1. Install `kpt` if you haven't already:
         
         gcloud components install kpt
         

  2. Download the sample using `kpt`:
         
         kpt pkg get \
           https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages.git/samples/online-boutique \
           online-boutique
         

Expected output
         
         Package "online-boutique":
         Fetching https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages@main
         From https://github.com/GoogleCloudPlatform/anthos-service-mesh-packages
         * branch            main       -> FETCH_HEAD
         Adding package "samples/online-boutique".
         Fetched 1 package(s).
         

  3. Navigate to the `online-boutique` directory:
         
         cd online-boutique
         

  4. Create the namespaces for the application:
         
         kubectl apply -f kubernetes-manifests/namespaces
         

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
         

  5. Deploy the sample to the cluster.

     1. Create the service accounts and deployments:
            
            kubectl apply -f kubernetes-manifests/deployments
            

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
            
            kubectl apply -f kubernetes-manifests/services
            

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
            
            kubectl apply -f istio-manifests/allow-egress-googleapis.yaml
            

Expected output:
            
            serviceentry.networking.istio.io/allow-egress-googleapis created
            serviceentry.networking.istio.io/allow-egress-google-metadata created
            




## Enabling sidecar auto-injection

To enable auto-injection, you label your namespaces with the _[default injection labels](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag)_ if the default tag is set up, or with the [revision label](https://docs.cloud.google.com/service-mesh/v1.19/docs/revisions-overview) to your namespace. The label that you add also depends on whether you deployed [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh) or installed the [in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh). The label is used by the sidecar injector webhook to associate injected sidecars with a particular control plane revision.

### In-cluster

  1. Use the following command to locate the label on `istiod`:
         
         kubectl get deploy -n istio-system -l app=istiod -o \
           jsonpath={.items[*].metadata.labels.'istio\.io\/rev'}'{"\n"}'
         

The command outputs the revision label that corresponds to the Cloud Service Mesh version, for example: `asm-11910-9`

  2. Apply the revision label to the application namespaces. In the following command, REVISION is the value of the `istiod` revision label that you noted in the previous step.

**Note:** You can substitute `istio.io/rev` with the `istio-injection=enabled` label if the [default tag](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) is configured. Verify the default tag exists by running ` istioctl tag list` with the `istioctl` from `OUTPUT_DIR`. 
         
         for ns in ad cart checkout currency email frontend loadgenerator \
           payment product-catalog recommendation shipping; do
             kubectl label namespace $ns istio.io/rev=REVISION --overwrite
         done;
         

Expected output:
         
         namespace/ad labeled
         namespace/cart labeled
         namespace/checkout labeled
         namespace/currency labeled
         namespace/email labeled
         namespace/frontend labeled
         namespace/loadgenerator labeled
         namespace/payment labeled
         namespace/product-catalog labeled
         namespace/recommendation labeled
         namespace/shipping labeled
         

  3. Restart the pods:
         
         for ns in ad cart checkout currency email frontend loadgenerator \
           payment product-catalog recommendation shipping; do
             kubectl rollout restart deployment -n ${ns}
         done;
         

Expected output:
         
         deployment.apps/adservice restarted
         deployment.apps/cartservice restarted
         deployment.apps/checkoutservice restarted
         deployment.apps/currencyservice restarted
         deployment.apps/emailservice restarted
         deployment.apps/frontend restarted
         deployment.apps/loadgenerator restarted
         deployment.apps/paymentservice restarted
         deployment.apps/productcatalogservice restarted
         deployment.apps/recommendationservice restarted
         deployment.apps/shippingservice restarted
         




### Managed service mesh

  1. Apply the revision label to the application namespaces. In the following command, the REVISION label must be the value of your managed Cloud Service Mesh release channel: `asm-managed` for regular, `asm-managed-rapid` for rapid, or `asm-managed-stable` for stable.

**Note:** You can substitute `istio.io/rev` with the `istio-injection=enabled` label if the [default tag](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) is configured. Verify the default tag exists by running ` istioctl tag list` with the `istioctl` from `OUTPUT_DIR`. 
         
         for ns in ad cart checkout currency email frontend loadgenerator \
           payment product-catalog recommendation shipping; do
             kubectl label namespace $ns istio.io/rev=REVISION --overwrite
         done;
         

Expected output:
         
         namespace/ad labeled
         namespace/cart labeled
         namespace/checkout labeled
         namespace/currency labeled
         namespace/email labeled
         namespace/frontend labeled
         namespace/loadgenerator labeled
         namespace/payment labeled
         namespace/product-catalog labeled
         namespace/recommendation labeled
         namespace/shipping labeled
         

  2. If you also deployed the optional [managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh-asmcli#apply_the_managed_data_plane_optional), annotate the application namespaces as follows:
         
         for ns in ad cart checkout currency email frontend loadgenerator \
           payment product-catalog recommendation shipping; do
             kubectl annotate --overwrite namespace $ns mesh.cloud.google.com/proxy='{"managed":"true"}'
         done;
         

  3. Restart the pods:
         
         for ns in ad cart checkout currency email frontend loadgenerator \
           payment product-catalog recommendation shipping; do
             kubectl rollout restart deployment -n ${ns}
         done;
         

Expected output:
         
         deployment.apps/adservice restarted
         deployment.apps/cartservice restarted
         deployment.apps/checkoutservice restarted
         deployment.apps/currencyservice restarted
         deployment.apps/emailservice restarted
         deployment.apps/frontend restarted
         deployment.apps/loadgenerator restarted
         deployment.apps/paymentservice restarted
         deployment.apps/productcatalogservice restarted
         deployment.apps/recommendationservice restarted
         deployment.apps/shippingservice restarted
         




## Exposing and accessing the application

The way you expose the application outside the mesh depends on whether you deployed an ingress gateway. You can choose to expose the application using an istio ingress gateway or [using a Kubernetes Service](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).

### Using ingress gateway

If you deployed an ingress gateway to the cluster as specified in the [prerequisite](https://cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh#install_gateways), do the following steps to expose the application using the gateway.

  1. Deploy a `Gateway` and `VirtualService` for the frontend service
         
         kubectl apply -f istio-manifests/frontend-gateway.yaml
         

Expected output:
         
         gateway.networking.istio.io/frontend-gateway created
         virtualservice.networking.istio.io/frontend-ingress created
         

  2. Get the external IP address of the [ingress gateway](https://docs.cloud.google.com/service-mesh/v1.19/docs/glossary#ingress-gateway). Replace the placeholders with the following information:

     * GATEWAY_SERVICE_NAME : The name of the ingress gateway service. If you deployed the sample gateway without modification, or if you deployed the [default ingress gateway](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/plan-install#prepare_gateway_configuration), the name is `istio-ingressgateway`.

     * GATEWAY_NAMESPACE: The namespace in which you deployed the ingress gateway. If you deployed the default ingress gateway, the namespace is `istio-system`.
    
    kubectl get service GATEWAY_SERVICE_NAME  -n GATEWAY_NAMESPACE
    

The output is similar to:
    
    NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                      AGE
    istio-ingressgateway   LoadBalancer   10.19.247.233   35.239.7.64   80:31380/TCP,443:31390/TCP,31400:31400/TCP   27m
    

In this example, the IP address of the ingress gateway is `35.239.7.64`.

  3. Visit the application on your browser to confirm installation:
         
         http://EXTERNAL_IP/
         




### No ingress gateway

If you did not deploy an ingress gateway or choose to expose the application using a Kubernetes Service, do the following steps:

  1. Deploy a service of type `LoadBalancer` to expose the frontend service
         
         kubectl apply -f frontend-external.yaml
         

  2. Find the external IP address of the `frontend-external` service:
         
         kubectl get service frontend-external -n frontend
         

  3. Visit the application on your browser to confirm installation:
         
         http://EXTERNAL_IP/
         




You can [explore the Cloud Service Mesh observability features](https://docs.cloud.google.com/service-mesh/v1.19/docs/observability/explore-dashboard) in the Google Cloud console. Note that it can take up to 10 minutes for the topology graph to display the services in your mesh.

## Clean up

Before deleting Online Boutique, you might want to work through [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/v1.19/docs/by-example/mtls), which uses the sample. When you're finished exploring, use the following commands to remove the Online Boutique sample:

  1. Delete the application namespaces:
         
         kubectl delete -f kubernetes-manifests/namespaces
         

Expected output:
         
         namespace "ad" deleted
         namespace "cart" deleted
         namespace "checkout" deleted
         namespace "currency" deleted
         namespace "email" deleted
         namespace "frontend" deleted
         namespace "loadgenerator" deleted
         namespace "payment" deleted
         namespace "product-catalog" deleted
         namespace "recommendation" deleted
         namespace "shipping" deleted
         

  2. Delete the service entries:
         
         kubectl delete -f istio-manifests/allow-egress-googleapis.yaml
         

Expected output:
         
         serviceentry.networking.istio.io "allow-egress-googleapis" deleted
         serviceentry.networking.istio.io "allow-egress-google-metadata" deleted
         




## What's next?

  * [Cloud Service Mesh by example: mTLS](https://docs.cloud.google.com/service-mesh/v1.19/docs/by-example/mtls)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
