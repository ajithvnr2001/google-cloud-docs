---
url: https://docs.cloud.google.com/service-mesh/v1.24/docs/gateway/set-up-envoy-mesh/
title: Set up an Envoy sidecar service mesh on GKE \u00a0|\u00a0 Cloud Service Mesh v1.24 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:13.316541+00:00
---

# Set up an Envoy sidecar service mesh on GKE  |  Cloud Service Mesh v1.24  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.24/docs/gateway/set-up-envoy-mesh/

You are viewing archived v1.24 Service Mesh documentation.

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
  * [ v1.24 ](https://docs.cloud.google.com/service-mesh/v1.24/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.24/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up an Envoy sidecar service mesh on GKE

This page describes how to set up an Envoy sidecar service mesh on GKE.

## Prerequisites

As a starting point, this guide assumes that you have already:

  * [Created a GKE cluster and registered it to a fleet](https://docs.cloud.google.com/service-mesh/v1.24/docs/gateway/prepare-gateway#create_and_register_a_cluster).
  * [Installed the custom resource definitions](https://docs.cloud.google.com/service-mesh/v1.24/docs/gateway/prepare-gateway#install_custom_resource_definitions).



## Set up the Service

  1. Create a sample HTTP service:
         
         kubectl apply -f - <<EOF
         kind: Namespace
         apiVersion: v1
         metadata:
           name: sidecar-example
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: whereami
           namespace: sidecar-example
         spec:
           replicas: 2
           selector:
             matchLabels:
               app: whereami
           template:
             metadata:
               labels:
                 app: whereami
             spec:
               containers:
               - name: whereami
                 image: us-docker.pkg.dev/google-samples/containers/gke/whereami:v1
                 ports:
                 - containerPort: 8080
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: whereami
           namespace: sidecar-example
         spec:
           selector:
             app: whereami
           ports:
           - port: 8080
             targetPort: 8080
         EOF
         

  2. Create a baseline HTTPRoute for the service:
         
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: HTTPRoute
         metadata:
           name: whereami-route
           namespace: sidecar-example
         spec:
           parentRefs:
           - name: whereami
             kind: Service
             group: ""
           rules:
           - backendRefs:
             - name: whereami
               port: 8080
         EOF
         

Alternatively, the following manifest describes a sample gRPC Service:
         
         apiVersion: v1
         kind: Service
         metadata:
           name: sample-service
           namespace: sample-ns
           annotations:
             networking.gke.io/app-protocols: '{"50051": "HTTP2"}' # 50051 is backendref.port
         spec:
           ports:
           - port: 50051
             targetPort: 50051
         

**Note:** If you are setting up a Service that runs gRPC but uses an Envoy sidecar proxy, the Service metadata should include `networking.gke.io/app-protocols: '{"<port>": "HTTP2"}'` label to apply the correct protocol to the backend service.



## Set up the Client

  1. Run the following command to enable sidecar injection in the `sidecar-example` namespace:
         
         kubectl label namespace sidecar-example mesh.cloud.google.com/csm-injection=sidecar
         

  2. Create a client:
         
         kubectl apply -f - <<EOF
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           labels:
             run: client
           name: client
           namespace: sidecar-example
         spec:
           replicas: 1
           selector:
             matchLabels:
               run: client
           template:
             metadata:
               labels:
                 run: client
             spec:
               containers:
               - name: client
                 image: curlimages/curl
                 command:
                 - sh
                 - -c
                 - while true; do sleep 1; done
         EOF
         

  3. Verify that the client Pod has an Envoy sidecar container automatically injected:
         
         kubectl get pods -n sidecar-example -l run=client
         

The output is similar to:
         
         NAME                    READY   STATUS    RESTARTS   AGE
         client-xxxx             2/2     Running   0          20s
         

Wait for the client to be ready and have the `Status` Running before continuing.

  4. Verify Envoy-sidecar service mesh setup. The following command sends a request to the whereami service from the client
         
         CLIENT_POD=$(kubectl get pod -n sidecar-example -l run=client -o=jsonpath='{.items[0].metadata.name}')
         
         # The VIP where the following request will be sent. Because all requests
         # from the client container are redirected to the Envoy proxy sidecar, you
         # can use any IP address, including 10.0.0.2, 192.168.0.1, and others.
         VIP='10.0.0.1'
         
         TEST_CMD="curl -v -H 'host: whereami.sidecar-example.svc.cluster.local' $VIP"
         
         kubectl exec -it $CLIENT_POD -n sidecar-example -c client -- /bin/sh -c "$TEST_CMD"
         

The output is similar to:
         
         < Trying 10.0.0.1:80...
         < Connected to 10.0.0.1 (10.0.0.1) port 80 (#0)
         < GET / HTTP/1.1
         < Host: whereami
         < User-Agent: curl/7.82.0-DEV
         < Accept: */*
         <
         < Mark bundle as not supporting multiuse
         < HTTP/1.1 200 OK
         < content-type: application/json
         < content-length: 318
         < access-control-allow-origin: *
         < server: envoy
         < date: Tue, 12 Apr 2022 22:30:13 GMT
         <
         {
           "cluster_name": "${CLUSTER_NAME}",
           "location": "${LOCATION}",
           "host_header": "whereami",
           ...
         }
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
