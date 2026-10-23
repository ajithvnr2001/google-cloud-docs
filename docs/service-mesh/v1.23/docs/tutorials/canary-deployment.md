---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/tutorials/canary-deployment/
title: Cloud Service Mesh by example: canary deployments \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:31.610925+00:00
---

# Cloud Service Mesh by example: canary deployments  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/tutorials/canary-deployment/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback 

#  Cloud Service Mesh by example: canary deployments Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

In this tutorial, you walk through a common use case: rolling out a canary deployment with Cloud Service Mesh using Istio APIs.

### What is a canary deployment?

A canary deployment routes a small percentage of traffic to a new version of a microservice, then gradually increases that percentage while phasing out and retiring the old version. If something goes wrong during this process, traffic can be switched back to the earlier version. With Cloud Service Mesh, you can route traffic to ensure that new services are introduced safely.

## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://docs.cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.23/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish this tutorial, you can avoid ongoing costs by deleting the resources you created. For more information, see Clean up.

## Before you begin

  * Make sure that billing is enabled for your Google Cloud project. [Learn how to confirm that billing is enabled for your project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#confirm_billing_is_enabled_on_a_project).

  * Provision Cloud Service Mesh [on a GKE cluster](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/provision-control-plane) or [on another supported Kubernetes cluster](https://docs.cloud.google.com/service-mesh/v1.23/docs/onboarding/kubernetes-workloads).

  * [Deploy an Ingress Gateway](https://docs.cloud.google.com/service-mesh/v1.23/docs/operate-and-maintain/gateways#deploy_gateways).

  * Clone the repository:
        
        git clone https://github.com/GoogleCloudPlatform/anthos-service-mesh-samples
        cd anthos-service-mesh-samples/docs/canary-service
        




## Deploy Online Boutique

  1. Set the current context for `kubectl` to the cluster where you plan to deploy Online Boutique. The command depends on whether you provisioned Cloud Service Mesh on a GKE cluster or a Kubernetes cluster outside GKE:

### GKE on Google Cloud
         
         gcloud container clusters get-credentials CLUSTER_NAME  \
             --project=PROJECT_ID \
             --zone=CLUSTER_LOCATION 
         

### GKE outside Google Cloud
         
         kubectl config use-context CLUSTER_NAME 
         

  2. Create the namespace for the sample application and the ingress gateway:
         
         kubectl create namespace onlineboutique
         

  3. Label the `onlineboutique` namespace to automatically inject Envoy proxies. Follow the steps on [how to enable automatic sidecar injection](https://docs.cloud.google.com/service-mesh/v1.23/docs/anthos-service-mesh-proxy-injection).

  4. Deploy the sample app. For this tutorial, you deploy [Online Boutique](https://github.com/GoogleCloudPlatform/microservices-demo), a microservice demo app.
         
         kubectl apply \
         -n onlineboutique \
         -f https://raw.githubusercontent.com/GoogleCloudPlatform/anthos-service-mesh-samples/main/docs/shared/online-boutique/kubernetes-manifests.yaml
         

  5. Add a label `version=v1` to the `productcatalog` deployment by running the following command:
         
         kubectl patch deployments/productcatalogservice -p '{"spec":{"template":{"metadata":{"labels":{"version":"v1"}}}}}' \
         -n onlineboutique
         

View the services that you deployed:
         
         kubectl get pods -n onlineboutique
         

Expected output:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         adservice-85598d856b-m84m6               2/2     Running   0          2m7s
         cartservice-c77f6b866-m67vd              2/2     Running   0          2m8s
         checkoutservice-654c47f4b6-hqtqr         2/2     Running   0          2m10s
         currencyservice-59bc889674-jhk8z         2/2     Running   0          2m8s
         emailservice-5b9fff7cb8-8nqwz            2/2     Running   0          2m10s
         frontend-77b88cc7cb-mr4rp                2/2     Running   0          2m9s
         loadgenerator-6958f5bc8b-55q7w           2/2     Running   0          2m8s
         paymentservice-68dd9755bb-2jmb7          2/2     Running   0          2m9s
         productcatalogservice-84f95c95ff-c5kl6   2/2     Running   0          114s
         recommendationservice-64dc9dfbc8-xfs2t   2/2     Running   0          2m9s
         redis-cart-5b569cd47-cc2qd               2/2     Running   0          2m7s
         shippingservice-5488d5b6cb-lfhtt         2/2     Running   0          2m7s
         

A `2/2` in the `READY` column indicates that a pod is up and running with an Envoy proxy successfully injected.

  6. Deploy your `VirtualService` and `DestinationRule` for v1 of `productcatalog`:
         
         kubectl apply -f destination-vs-v1.yaml -n onlineboutique
         
         
         apiVersion: networking.istio.io/v1beta1
         kind: DestinationRule
         metadata:
           name: productcatalogservice
         spec:
           host: productcatalogservice
           subsets:
           - labels:
               version: v1
             name: v1
         ---
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: productcatalogservice
         spec:
           hosts:
           - productcatalogservice
           http:
           - route:
             - destination:
                 host: productcatalogservice
                 subset: v1

Note that only `v1` is present in the resources.

View the `Destination Rule` created.
         
         kubectl get destinationrules -n onlineboutique
         

Expected output:
         
         NAME                    HOST                    AGE
           productcatalogservice   productcatalogservice   2m
         

View the `VirtualService` created.
         
         kubectl get virtualservices -n onlineboutique
         

Expected outcome:
         
         NAME                    GATEWAYS   HOSTS                       AGE
           productcatalogservice              ["productcatalogservice"]   2m
         

  7. Visit the application in your browser using the external IP address of your ingress gateway:
         
         kubectl get services -n GATEWAY_NAMESPACE
         




This next section tours the Cloud Service Mesh UI and show how you can view your metrics.

## View your services in Google Cloud console

  1. In Google Cloud console, go to the **Google Kubernetes Engine (GKE) Enterprise edition Services** page.

[Go to Google Kubernetes Engine (GKE) Enterprise edition Services](https://console.cloud.google.com/kubernetes/services)

  2. By default, you view your services in the **List** view.

The Table Overview lets you observe all your services, as well as important metrics at a glance.

  3. In the top right, click **Topology**. Here you can view your services and their interaction with each other.

You can expand **Services** and view the **Requests per second** for each of your services by hovering over on them with your cursor.

  4. Navigate back to the **Table View**.

  5. In the **Services Table** , select `productcatalogservice`. This takes you to an overview of your service.

  6. On the left side of the screen, click **Traffic**.

  7. Ensure 100% of the incoming traffic to `productcatalogservice` goes to the workload service.




The next section goes through creating a v2 of the `productcatalog` service.

## Deploy v2 of a service

  1. For this tutorial, `productcatalogservice-v2` introduces a 3-second latency into requests with the `EXTRA_LATENCY` field. This simulates a regression in the new version of the service.
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: productcatalogservice-v2
         spec:
           selector:
             matchLabels:
               app: productcatalogservice
           template:
             metadata:
               labels:
                 app: productcatalogservice
                 version: v2
             spec:
               containers:
               - env:
                 - name: PORT
                   value: '3550'
                 - name: EXTRA_LATENCY
                   value: 3s
                 name: server
                 image: gcr.io/google-samples/microservices-demo/productcatalogservice:v0.3.6
                 livenessProbe:
                   exec:
                     command: ["/bin/grpc_health_probe", "-addr=:3550"]
                 ports:
                 - containerPort: 3550
                 readinessProbe:
                   exec:
                     command: ["/bin/grpc_health_probe", "-addr=:3550"]
                 resources:
                   limits:
                     cpu: 200m
                     memory: 128Mi
                   requests:
                     cpu: 100m
                     memory: 64Mi
               terminationGracePeriodSeconds: 5

Apply this resource to the `onlineboutique` namespace.
         
         kubectl apply -f productcatalog-v2.yaml -n onlineboutique
         

  2. Check on your application pods.
         
         kubectl get pods -n onlineboutique
         

Expected output:
         
         NAME                                     READY   STATUS    RESTARTS   AGE
         adservice-85598d856b-8wqfd                  2/2     Running   0          25h
         cartservice-c77f6b866-7jwcr                 2/2     Running   0          25h
         checkoutservice-654c47f4b6-n8c6x            2/2     Running   0          25h
         currencyservice-59bc889674-l5xw2            2/2     Running   0          25h
         emailservice-5b9fff7cb8-jjr89               2/2     Running   0          25h
         frontend-77b88cc7cb-bwtk4                   2/2     Running   0          25h
         loadgenerator-6958f5bc8b-lqmnw              2/2     Running   0          25h
         paymentservice-68dd9755bb-dckrj             2/2     Running   0          25h
         productcatalogservice-84f95c95ff-ddhjv      2/2     Running   0          25h
         productcatalogservice-v2-6df4cf5475-9lwjb   2/2     Running   0          8s
         recommendationservice-64dc9dfbc8-7s7cx      2/2     Running   0          25h
         redis-cart-5b569cd47-vw7lw                  2/2     Running   0          25h
         shippingservice-5488d5b6cb-dj5gd            2/2     Running   0          25h
         

Note that there are now two `productcatalogservices` listed.

  3. Use `DestinationRule` to specify the subsets of a service. In this scenario, there is a subset for v1 and then a separate subset for v2 of `productcatalogservice`.
         
         apiVersion: networking.istio.io/v1beta1
         kind: DestinationRule
         metadata:
           name: productcatalogservice
         spec:
           host: productcatalogservice
           subsets:
           - labels:
               version: v1
             name: v1
           - labels:
               version: v2
             name: v2

Note the `labels` field. The versions of `productcatalogservice` are distinguished after the traffic is routed by the `VirtualService`.

Apply the `DestinationRule`:
         
         kubectl apply -f destination-v1-v2.yaml -n onlineboutique
         




### Split traffic between v1 and v2

  1. Use `VirtualService` to define a small percentage of the traffic to direct to v2 of the `productcatalogservice`.
         
         apiVersion: networking.istio.io/v1beta1
         kind: VirtualService
         metadata:
           name: productcatalogservice
         spec:
           hosts:
           - productcatalogservice
           http:
           - route:
             - destination:
                 host: productcatalogservice
                 subset: v1
               weight: 75
             - destination:
                 host: productcatalogservice
                 subset: v2
               weight: 25

The subset field indicates the version, and the weight field indicates the percentage split of traffic. 75% of traffic goes to v1 of productcatalog, and 25% goes to v2.

Apply the `VirtualService`:
         
         kubectl apply -f vs-split-traffic.yaml -n onlineboutique
         




If you visit the `EXTERNAL_IP` of the cluster's ingress, you should notice that periodically, the frontend is slower to load.

In the next section, explore the traffic split in Google Cloud console.

## Observe the traffic split in Google Cloud console

  1. Return to Google Cloud console and go to the GKE Enterprise Services page. [Go to GKE Enterprise Services](https://console.cloud.google.com/kubernetes/services)

  2. In the top right, click **Topology**.

**Expand** the `productcatalogservice` workload and note the `productcatalogservice` and `productcatalogservice-v2` deployments.

  3. Return to the **Table View**. 

  4. Click `productcatalogservice` in the Services Table.

  5. Return to **Traffic** on the left navigation bar.

  6. Note that the incoming traffic is split between v1 and v2 by the percentage specified in the `VirtualService` file, and that there are 2 workloads of the productcatalog service.

On the right side of the page, you see **Requests** , **Error Rate** , and **Latency Metrics**. With Cloud Service Mesh, each service has these metrics outlined to provide you with observability metrics.

**Note:** It may take some time for the actual 75-25 split to be shown, since traffic over time is redirected to the `v2` service.



## Roll out or roll back to a version

After observing the metrics during a canary deployment, you can complete the roll out the new service version, or roll back to the original service version by leveraging the `VirtualService` resource.

### Roll out

After you are satisfied with the behavior of a v2 service, you can incrementally increase the percentage of traffic directed to the v2 service. Eventually, traffic can be 100% directed to the new service in the VirtualService resource you created above by removing the traffic split from that resource.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: productcatalogservice
    spec:
      hosts:
      - productcatalogservice
      http:
      - route:
        - destination:
            host: productcatalogservice
            subset: v2

To direct all the traffic to v2 of `productcatalogservice`:
    
    
    kubectl apply -f vs-v2.yaml -n onlineboutique
    

### Roll back

If you need to roll back to the v1 service, apply the `destination-vs-v1.yaml` from earlier. This directs traffic only to v1 of `productcatalogservice`.
    
    
    apiVersion: networking.istio.io/v1beta1
    kind: VirtualService
    metadata:
      name: productcatalogservice
    spec:
      hosts:
      - productcatalogservice
      http:
      - route:
        - destination:
            host: productcatalogservice
            subset: v1

To direct all the traffic to v1 of `productcatalogservice`:
    
    
    kubectl apply -f vs-v1.yaml -n onlineboutique
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

To avoid incurring continuing charges to your Google Cloud account for the resources used in this tutorial, you can either delete the project or delete the individual resources.

### Delete the project

**Caution:** Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for this tutorial, when you delete it, you also delete any other work you've done in the project.
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an appspot.com URL, delete selected resources inside the project instead of deleting the whole project.



In Cloud Shell, delete the project:
    
    
    gcloud projects delete PROJECT_ID
    

### Delete the resources

If you want to prevent additional charges, delete the cluster:
    
    
    gcloud container clusters delete  CLUSTER_NAME  \
      --project=PROJECT_ID \
      --zone=CLUSTER_LOCATION 
    

If you registered your cluster with fleet using `gcloud container fleet memberships` (rather than `--enable-fleet` or `--fleet-project` during cluster creation) then remove the stale membership:
    
    
    gcloud container fleet memberships delete  MEMBERSHIP  \
      --project=PROJECT_ID
    

If you want to keep your cluster configured for Cloud Service Mesh but remove the Online Boutique sample:

  1. Delete the application namespaces:
         
         kubectl delete -f namespace onlineboutique
         

Expected output:
         
         namespace "onlineboutique" deleted
         

  2. Delete the service entries:
         
         kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/istio-manifests/frontend.yaml -n onlineboutique
         kubectl delete -f https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/istio-manifests/frontend-gateway.yaml -n onlineboutique
         

Expected output:
         
         serviceentry.networking.istio.io "allow-egress-googleapis" deleted
         serviceentry.networking.istio.io "allow-egress-google-metadata" deleted
         




## What's next

  * For a general guide on configuring `PeerAuthentication` policies, see [Configuring transport security](https://docs.cloud.google.com/service-mesh/v1.23/docs/security/configuring-mtls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
