---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2-maglev/
title: Use Maglev load balancing in GKE Dataplane V2 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:31.051849+00:00
---

# Use Maglev load balancing in GKE Dataplane V2  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2-maglev/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Use Maglev load balancing in GKE Dataplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document shows you how to configure and verify Maglev load balancing for Services in GKE Dataplane V2.

Maglev is a consistent hashing algorithm that provides high-throughput and low-latency load balancing. Maglev minimizes packet drops and connection disruption when backend Pods scale, update, or reschedule by helping to ensure that the same flow consistently maps to the same backend.

For more information, see the [Maglev consistent hashing algorithm](https://research.google/pubs/pub44824/) research paper.

We recommend this feature for workloads with long-lived connections or stateful applications where backend changes shouldn't disrupt existing flows.

For information about resource overhead and scalability considerations, see [GKE Dataplane V2 concepts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#maglev-support).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Prerequisites and limits

  * **GKE version:** 1.36.0-gke.2882000 and later
  * **GKE Dataplane V2:** enabled
  * **Cluster modes:** Autopilot and Standard



## Create a GKE cluster with GKE Dataplane V2

To use Maglev, you must have a GKE cluster with GKE Dataplane V2 enabled.

###  Autopilot 

Autopilot clusters have GKE Dataplane V2 enabled by default. To create an Autopilot cluster and retrieve its configuration, run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --region=COMPUTE_REGION \
        --release-channel=rapid
    gcloud container clusters get-credentials CLUSTER_NAME \
        --region=COMPUTE_REGION
    

###  Standard 

To enable GKE Dataplane V2 on a Standard cluster, use the `--enable-dataplane-v2` flag. To create a Standard cluster and retrieve its configuration, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --zone=COMPUTE_ZONE \
        --enable-dataplane-v2 \
        --cluster-version=1.36.0-gke.2882000
    gcloud container clusters get-credentials CLUSTER_NAME \
        --zone=COMPUTE_ZONE
    

## Deploy a backend application

Before configuring your load balancing Services, deploy a backend application to handle traffic. This Deployment runs five replicas of the `hello-app` sample application.

  1. Save the following manifest as `echo-backend.yaml`:
         
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: echo-backend
         spec:
           replicas: 5
           selector:
             matchLabels:
               app: echo-backend
           template:
             metadata:
               labels:
                 app: echo-backend
             spec:
               containers:
               - name: hello
                 image: "us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0"
                 ports:
                 - containerPort: 8080
         

  2. Apply the manifest:
         
         kubectl apply -f echo-backend.yaml
         




## Configure load balancing Services

You can configure Services to use either the Maglev load balancing algorithm or the default random load balancing algorithm. Both Services target the `echo-backend` Deployment created in the previous step.

### Configure a Maglev Service

To enable Maglev load balancing, add the `gke.networking.io/lb-algorithm: "maglev"` annotation to the Service metadata during creation.

**Important:** You can only set the `gke.networking.io/lb-algorithm` annotation when you create the Service. To enable Maglev on an existing Service, you must delete and re-create the Service. 

  1. Save the following manifest as `maglev-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: maglev-service
           annotations:
             gke.networking.io/lb-algorithm: "maglev"
         spec:
           selector:
             app: echo-backend
           ports:
             - protocol: TCP
               port: 80
               targetPort: 8080
         

  2. Apply the manifest:
         
         kubectl apply -f maglev-service.yaml
         




### Configure a random Service

By default, Services use a random load balancing algorithm. You don't need to specify an annotation to use the default algorithm, but the following example explicitly configures it for comparison.

  1. Save the following manifest as `random-service.yaml`:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: random-service
           annotations:
             gke.networking.io/lb-algorithm: "random"
         spec:
           selector:
             app: echo-backend
           ports:
             - protocol: TCP
               port: 80
               targetPort: 8080
         

  2. Apply the manifest:
         
         kubectl apply -f random-service.yaml
         




## Verify traffic consistency

You can verify the routing consistency differences between Maglev and random load balancing by deploying test client Pods that send traffic from a fixed source port.

### Verify Maglev traffic consistency

Maglev routes requests from the same source port consistently to the same backend Pod.

  1. Save the following manifest as `client-maglev.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: client-maglev
         spec:
           restartPolicy: Never
           containers:
           - name: curl
             image: curlimages/curl:8.2.0
             command: ["/bin/sh", "-c"]
             args:
             - |
               while true; do
                 curl -s -H "Connection: close" http://maglev-service:80 --local-port 54321 | grep Hostname
                 sleep 0.5
               done
         

The `--local-port` flag forces the source port, and the `Connection: close` header helps to ensure that the client can reuse the source port immediately for subsequent requests.

  2. Apply the manifest:
         
         kubectl apply -f client-maglev.yaml
         

  3. While the Pod is running, check the logs:
         
         kubectl logs client-maglev
         

**Expected output:**

The output shows the same hostname printed repeatedly, indicating that all traffic from the client is consistently routed to the same backend Pod:
         
         Hostname: echo-backend-5c78f66dbf-abcde
         Hostname: echo-backend-5c78f66dbf-abcde
         

**Note:** Because Pods created by Deployments have non-deterministic names, your actual hostname will differ from the example. 



### Verify default (random) traffic distribution

The default Service distributes traffic from the same source port across different backend Pods.

  1. Save the following manifest as `client-random.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: client-random
         spec:
           restartPolicy: Never
           containers:
           - name: curl
             image: curlimages/curl:8.2.0
             command: ["/bin/sh", "-c"]
             args:
             - |
               while true; do
                 curl -s -H "Connection: close" http://random-service:80 --local-port 54321 | grep Hostname
                 sleep 0.5
               done
         

  2. Apply the manifest:
         
         kubectl apply -f client-random.yaml
         

  3. While the Pod is running, check the logs:
         
         kubectl logs client-random
         

**Expected output:**

The output shows multiple different hostnames, indicating that traffic is distributed across different Pods:
         
         Hostname: echo-backend-5c78f66dbf-abcde
         Hostname: echo-backend-5c78f66dbf-fghij
         Hostname: echo-backend-5c78f66dbf-klmno
         ...
         




## Cleanup

To clean up the resources used in this tutorial, run the following commands:

  1. Delete the client Pods, Services, and Deployment:
         
         kubectl delete service maglev-service random-service
         kubectl delete deployment echo-backend
         kubectl delete pod client-maglev client-random
         

  2. Delete the GKE clusters:




###  Autopilot 
    
    
    gcloud container clusters delete CLUSTER_NAME --region=COMPUTE_REGION
    

###  Standard 
    
    
    gcloud container clusters delete CLUSTER_NAME --zone=COMPUTE_ZONE
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
