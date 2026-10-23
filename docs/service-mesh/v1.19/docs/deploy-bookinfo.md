---
url: https://docs.cloud.google.com/service-mesh/v1.19/docs/deploy-bookinfo/
title: Deploying the Bookinfo sample \u00a0|\u00a0 Cloud Service Mesh v1.19 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:44.496060+00:00
---

# Deploying the Bookinfo sample  |  Cloud Service Mesh v1.19  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.19/docs/deploy-bookinfo/

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

# Deploying the Bookinfo sample

This page explains how to deploy a sample application to demonstrate Cloud Service Mesh. If you haven't installed Cloud Service Mesh, see the [Installation guide](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh).

Several sample applications come with the Cloud Service Mesh installation. This guide walks you through deploying the [BookInfo](https://istio.io/v1.19/docs/examples/bookinfo/) sample. This is a simple mock bookstore application made up of four services that provide a web product page, book details, reviews (with several versions of the review service), and ratings—all managed using Cloud Service Mesh. You can find the source code and all the other files used in this example in your Cloud Service Mesh installation's directory in `samples/bookinfo`.

## Enabling sidecar auto-injection

To enable sidecar auto-injection, you must label your namespaces so that the sidecar injector webhook associate injected sidecars with a particular control plane revision. If you set up the default tag, then label your namespaces with the [default injection labels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel#how-to-select-a-release-channel). Otherwise, label your namespaces with the [revision label](https://docs.cloud.google.com/service-mesh/v1.19/docs/revisions-overview). Additionally, the label that you add also depends on whether you deployed [managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh) or installed the [in-cluster control plane](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/install-anthos-service-mesh).

### Managed

  1. You can either use the default injection label or the revision label for your namespace

### Default injection labels

Apply the default injection label to the namespace.
         
         kubectl label namespace NAMESPACE istio-injection=enabled istio.io/rev-
         

### Revision label

Before you deploy applications, remove any previous `istio-injection` labels from their namespaces and set the `istio.io/rev=REVISION_LABEL` label instead.

To change it to a specific revision label, click `REVISION_LABEL`, and replace it with the applicable label: `asm-managed-rapid` for rapid channel, `asm-managed` for regular channel, or `asm-managed-stable` for stable channel.

The revision label corresponds to a [release channel](https://docs.cloud.google.com/service-mesh/v1.19/docs/release-channels-managed-control-plane):

Revision label | Channel  
---|---  
`asm-managed` | Regular  
`asm-managed-rapid` | Rapid  
`asm-managed-stable` | Stable  
           
         kubectl label namespace NAMESPACE istio-injection- istio.io/rev=REVISION_LABEL --overwrite
         

**Note:** You can ignore any `label "istio-injection" not found` errors.

  2. If you also deployed the optional [managed data plane](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh#managed_data_plane), annotate the `NAMESPACE`namespace as follows:
         
         kubectl annotate --overwrite namespace NAMESPACE \
         mesh.cloud.google.com/proxy='{"managed":"true"}'
         




### In-cluster

  1. Use the following command to locate the label on `istiod`:
         
         kubectl -n istio-system get pods -l app=istiod --show-labels
         

The output looks similar to the following:
         
         NAME                                READY   STATUS    RESTARTS   AGE   LABELS
         istiod-asm-173-3-5788d57586-bljj4   1/1     Running   0          23h   app=istiod,istio.io/rev=asm-11910-9,istio=istiod,pod-template-hash=5788d57586
         istiod-asm-173-3-5788d57586-vsklm   1/1     Running   1          23h   app=istiod,istio.io/rev=asm-11910-9,istio=istiod,pod-template-hash=5788d57586
         

In the output, under the `LABELS` column, note the value of the `istiod` revision label, which follows the prefix `istio.io/rev=`. In this example, the value is `asm-11910-9`.

**Note:** You can substitute `istio.io/rev` with the `istio-injection=enabled` label if the [default tag](https://istio.io/latest/docs/setup/upgrade/canary/#default-tag) is configured. Verify the default tag exists by running ` istioctl tag list` with the `istioctl` from `OUTPUT_DIR`. 

  2. Apply the revision label to the default namespace. In the following command, `REVISION` is the value of the `istiod` revision label that you noted in the previous step.
         
         kubectl label namespace default istio-injection- istio.io/rev=REVISION --overwrite
         

You can ignore the message `"istio-injection not found"` in the output. That means that the namespace didn't previously have the `istio-injection` label, which you should expect in new installations of Cloud Service Mesh or new deployments. Because auto-injection behavior is undefined when a namespace has both the `istio-injection` and the revision label, all `kubectl label` commands in the Cloud Service Mesh documentation explicitly ensure that only one is set. 




## Deploying the application

Now that auto-injection is enabled on the `default` namespace, when you deploy the BookInfo application's services, sidecar proxies are injected alongside each service.

  1. On the command line on the computer where you installed Cloud Service Mesh, go to the root of the Cloud Service Mesh installation directory. If you need to, [download the installation file](https://docs.cloud.google.com/service-mesh/v1.19/docs/downloading-istioctl).

  2. Deploy your application to the default namespace using `kubectl`:
         
         kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
         

  3. Confirm that the application has been deployed correctly by running the following commands:
         
         kubectl get services
         

Output:
         
         NAME                       CLUSTER-IP   EXTERNAL-IP   PORT(S)              AGE
         details                    10.0.0.31    <none>        9080/TCP             6m
         kubernetes                 10.0.0.1     <none>        443/TCP              7d
         productpage                10.0.0.120   <none>        9080/TCP             6m
         ratings                    10.0.0.15    <none>        9080/TCP             6m
         reviews                    10.0.0.170   <none>        9080/TCP             6m

and
         
         kubectl get pod
         

Output:
         
         NAME                                        READY     STATUS    RESTARTS   AGE
         details-v1-1520924117-48z17                 2/2       Running   0          6m
         productpage-v1-560495357-jk1lz              2/2       Running   0          6m
         ratings-v1-734492171-rnr5l                  2/2       Running   0          6m
         reviews-v1-874083890-f0qf0                  2/2       Running   0          6m
         reviews-v2-1343845940-b34q5                 2/2       Running   0          6m
         reviews-v3-1813607990-8ch52                 2/2       Running   0          6m

  4. Finally, define the ingress gateway routing for the application:
         
         kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
         

Output:
         
         gateway.networking.istio.io/bookinfo-gateway created
         virtualservice.networking.istio.io/bookinfo created




## Validating the application deployment

To see if the BookInfo application is working, you need to send traffic to the ingress gateway.

  * If you installed Cloud Service Mesh on Google Distributed Cloud, get the external IP address for the ingress gateway that you [configured](https://docs.cloud.google.com/service-mesh/v1.19/docs/unified-install/external-ip-load-balance) after installing Cloud Service Mesh

  * If you installed Cloud Service Mesh on GKE, get the external IP address of the ingress gateway as follows:
        
        kubectl get service istio-ingressgateway -n istio-system
        

Output:
        
        NAME                   TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                                      AGE
        istio-ingressgateway   LoadBalancer   10.19.247.233   35.239.7.64   80:31380/TCP,443:31390/TCP,31400:31400/TCP   27m

In this example, the IP address of the ingress service is `35.239.7.64`.




### Trying the application

  1. Check that the BookInfo app is running with `curl`:
         
         curl -I http://EXTERNAL_IP/productpage
         

If the response shows `200`, it means the application is working properly with Cloud Service Mesh.

  2. To view the BookInfo web page, enter the following address in your browser:
         
         http://EXTERNAL_IP/productpage
         

If you refresh the page several times, you should see different versions of reviews shown in the product page, presented in a round robin style (red stars, black stars, no stars).




Now that you have an application that is generating traffic, you can [explore the Cloud Service Mesh pages](https://docs.cloud.google.com/service-mesh/v1.19/docs/observability/explore-dashboard) in the Google Cloud console to see metrics and the other observability features.

## Cleaning up

When you are finished experimenting with the Bookinfo sample, remove it from your cluster.

  1. Uninstall Bookinfo using the following script:
         
         samples/bookinfo/platform/kube/cleanup.sh
         

  2. Confirm shutdown:
         
         kubectl get virtualservices   #-- there should be no virtual services
         kubectl get destinationrules  #-- there should be no destination rules
         kubectl get gateway           #-- there should be no gateway
         kubectl get pods              #-- the Bookinfo pods should be deleted
         




## What's next

[Learn more about the Bookinfo sample](https://archive.istio.io/v1.19/docs/examples/bookinfo/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
