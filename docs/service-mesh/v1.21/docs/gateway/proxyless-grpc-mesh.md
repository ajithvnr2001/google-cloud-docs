---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/gateway/proxyless-grpc-mesh/
title: Set up a proxyless gRPC service mesh on GKE \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:18.460009+00:00
---

# Set up a proxyless gRPC service mesh on GKE  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/gateway/proxyless-grpc-mesh/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a proxyless gRPC service mesh on GKE

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This pages describes how to deploy an example proxyless gRPC client and server to a Cloud Service Mesh.

## Prerequisites

As a starting point, this guide assumes that you have already:

  * [Created a GKE cluster and registered it to a fleet](https://docs.cloud.google.com/service-mesh/v1.21/docs/gateway/prepare-gateway#create_and_register_a_cluster).
  * [Installed the custom resource definitions](https://docs.cloud.google.com/service-mesh/v1.21/docs/gateway/prepare-gateway#install_custom_resource_definitions).



## Requirements

This section lists the requirements for supported services:

  * gRPC C++ - version 1.62.0 or later
  * gRPC Java - version 1.65.0 or later
  * gRPC Go - version 1.65.0 or later
  * gRPC Python - version 1.65.0 or later



## Set up the Service

Deploy a gRPC service:

### C++
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
    spec:
      selector:
        app: psm-grpc-server
      ports:
      - port: 50051
        targetPort: 50051
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-server
      labels:
        app: psm-grpc-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: psm-grpc-server
      template:
        metadata:
          labels:
            app: psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-cpp-server:latest
            imagePullPolicy: Always
            args:
              "--port=50051"
            ports:
              - containerPort: 50051
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
    spec:
      selector:
        app: psm-grpc-server
      ports:
      - port: 50051
        targetPort: 50051
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-server
      labels:
        app: psm-grpc-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: psm-grpc-server
      template:
        metadata:
          labels:
            app: psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-java-server:latest
            imagePullPolicy: Always
            args:
              "50051"
              "9464"
            ports:
              - containerPort: 50051
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
    spec:
      selector:
        app: psm-grpc-server
      ports:
      - port: 50051
        targetPort: 50051
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-server
      labels:
        app: psm-grpc-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: psm-grpc-server
      template:
        metadata:
          labels:
            app: psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-go-server:latest
            imagePullPolicy: Always
            args:
              "--port=50051"
            ports:
              - containerPort: 50051
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
    spec:
      selector:
        app: psm-grpc-server
      ports:
      - port: 50051
        targetPort: 50051
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-server
      labels:
        app: psm-grpc-server
    spec:
      replicas: 2
      selector:
        matchLabels:
          app: psm-grpc-server
      template:
        metadata:
          labels:
            app: psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-python-server:latest
            imagePullPolicy: Always
            args:
              "--port=50051"
            ports:
              - containerPort: 50051
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    EOF
    

The output is similar to
    
    
    service/helloworld created
    deployment.apps/psm-grpc-server created
    

  1. Verify that the Pods have been created:
         
         kubectl get pods
         

The output is similar to
         
         NAME                               READY   STATUS    RESTARTS   AGE
         psm-grpc-server-65966bf76d-2wwxz   1/1     Running   0          13s
         psm-grpc-server-65966bf76d-nbxd2   1/1     Running   0          13s
         

Wait for all Pods to be ready and have the `Status` Running before continuing.

  2. Deploy a HTTPRoute:
         
         kubectl apply -f - <<EOF
         apiVersion: gateway.networking.k8s.io/v1beta1
         kind: HTTPRoute
         metadata:
           name: app1
         spec:
           parentRefs:
           - name: helloworld
             kind: Service
             group: ""
           rules:
           - backendRefs:
             - name: helloworld
               port: 50051
         EOF
         

This command creates an HTTPRoute called app1 and sends all RPCs to the `helloworld` service.

Note that the `parentRef` service is also `helloworld` which means our HTTPRoute is attached to this service and will process all RPCs addressed to this service. In case of proxyless gRPC it means any client sending RPCs on a gRPC channel for target `xds:///helloworld.default.svc.cluster.local:50051`.

  3. Verify that the new app1 HTTPRoute has been created:
         
         kubectl get httproute
         

The output is similar to
         
         NAME   HOSTNAMES   AGE
         app1               72s
         




## Set up the Client

This sections describes how to use a gRPC client to verify that Cloud Service Mesh is routing traffic correctly in the mesh.

Run a gRPC client and direct it to use the routing configuration specified by the HTTPRoute:

### C++
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      labels:
        app: psm-grpc-client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: psm-grpc-client
      template:
        metadata:
          labels:
            app: psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-cpp-server:latest
            imagePullPolicy: Always
            args:
              "--target=xds:///helloworld.default.svc.cluster.local:50051"
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CONTAINER_NAME
                value: psm-grpc-client
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image:  gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      labels:
        app: psm-grpc-client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: psm-grpc-client
      template:
        metadata:
          labels:
            app: psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-java-server:latest
            imagePullPolicy: Always
            args:
              "world"<br/>"xds:///helloworld.default.svc.cluster.local:50051"
              "9464"
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CONTAINER_NAME
                value: psm-grpc-client
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image:  gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      labels:
        app: psm-grpc-client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: psm-grpc-client
      template:
        metadata:
          labels:
            app: psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-go-server:latest
            imagePullPolicy: Always
            args:
              "--target=xds:///helloworld.default.svc.cluster.local:50051"
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CONTAINER_NAME
                value: psm-grpc-client
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image:  gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      labels:
        app: psm-grpc-client
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: psm-grpc-client
      template:
        metadata:
          labels:
            app: psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-python-server:latest
            imagePullPolicy: Always
            args:
              "--target=xds:///helloworld.default.svc.cluster.local:50051"
            env:
              - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CONTAINER_NAME
                value: psm-grpc-client
              - name: OTEL_RESOURCE_ATTRIBUTES
                value: k8s.pod.name=\$(POD_NAME),k8s.namespace.name=\$(NAMESPACE_NAME),k8s.container.name=\$(CONTAINER_NAME)
            volumeMounts:
              - mountPath: /tmp/grpc-xds/
                name: grpc-td-conf
                readOnly: true
          initContainers:
            - name: grpc-td-init
              image:  gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.16.0
              imagePullPolicy: Always
              args:
                - "--output=/tmp/bootstrap/td-grpc-bootstrap.json"
                - "--vpc-network-name=default"
                - "--xds-server-uri=trafficdirector.googleapis.com:443"
                - "--generate-mesh-id"
              volumeMounts:
                - mountPath: /tmp/bootstrap/
                  name: grpc-td-conf
          volumes:
            - name: grpc-td-conf
              emptyDir:
                medium: Memory
    
    EOF
    

The output is similar to
    
    
    deployment.apps/psm-grpc-client created
    

## Google Cloud Managed Service for Prometheus Setup (Optional)

You can deploy the [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) `PodMonitoring` resource to export the metrics to Cloud Monitoring.

  * For servers, run the following command:
        
        kubectl apply -f - <<EOF
        apiVersion: monitoring.googleapis.com/v1
        kind: PodMonitoring
        metadata:
          name: psm-grpc-server-gmp
        spec:
          selector:
            matchLabels:
              app: psm-grpc-server
          endpoints:
          - port: 9464
            interval: 10s
        EOF
        

  * For clients, , run the following command:
        
        kubectl apply -f - <<EOF
        apiVersion: monitoring.googleapis.com/v1
        kind: PodMonitoring
        metadata:
          name: psm-grpc-client-gmp
        spec:
          selector:
            matchLabels:
              app: psm-grpc-client
          endpoints:
          - port: 9464
            interval: 10s
        EOF
        

After deploying the `PodMonitoring` resource, each matching pod's `localhost:9464/metrics` will be scraped every 10 seconds and will export the results to Cloud Monitoring.




To view the metrics in Cloud Monitoring, perform the following steps:

you can navigate to the Metrics Explorer section of your Google Cloud console, select Prometheus Target > Grpc to find the metrics.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

## Verify the proxyless gRPC service mesh setup and mesh Observability

  1. Check the metrics output from the client Pod:
         
         kubectl exec $(kubectl get po | grep psm-grpc-client | awk '{print $1;}') -- /usr/bin/curl -s http://localhost:9464/metrics
         

The output shows the metrics (with the service mesh labels) that were scraped from the endpoint:
         
         Defaulted container "psm-grpc-client" out of: psm-grpc-client, grpc-td-init (init)
         # HELP exposer_transferred_bytes_total Transferred bytes to metrics services
         # TYPE exposer_transferred_bytes_total counter
         exposer_transferred_bytes_total 36047
         # HELP exposer_scrapes_total Number of times metrics were scraped
         # TYPE exposer_scrapes_total counter
         exposer_scrapes_total 1
         # HELP exposer_request_latencies Latencies of serving scrape requests, in microseconds
         # TYPE exposer_request_latencies summary
         exposer_request_latencies_count 1
         exposer_request_latencies_sum 1246
         exposer_request_latencies{quantile="0.5"} Nan
         exposer_request_latencies{quantile="0.9"} Nan
         exposer_request_latencies{quantile="0.99"} Nan
         # HELP grpc_client_attempt_rcvd_total_compressed_message_size_By Compressed message bytes received per call attempt
         # TYPE grpc_client_attempt_rcvd_total_compressed_message_size_By histogram
         grpc_client_attempt_rcvd_total_compressed_message_size_By_count{csm_mesh_id="gsmmesh-35av-my-cluster-3-us-east7-c-35av6nnbi9jz",csm_remote_workload_canonical_service="unknown",csm_remote_workload_cluster_name="my-cluster-3",csm_remote_workload_location="us-east7-c",csm_remote_workload_name="psm-grpc-server",csm_remote_workload_namespace_name="default",csm_remote_workload_project_id="grpc-testing",csm_remote_workload_type="gcp_kubernetes_engine",csm_workload_canonical_service="unknown",grpc_method="helloworld.Greeter/SayHello",grpc_status="OK",grpc_target="xds:///helloworld.default.svc.cluster.local:50051"} 114 1695445356167
         ...
         

  2. Check the metrics output from the server:
         
         kubectl exec $(kubectl get po | grep psm-grpc-server | awk '{print $1;}' | head -n 1) -- /usr/bin/curl -s http://localhost:9464/metrics
         

The output shows the metrics (with the service mesh labels) that were scraped from the endpoint:
         
         Defaulted container "psm-grpc-server" out of: psm-grpc-server, grpc-td-init (init)
         # HELP exposer_transferred_bytes_total Transferred bytes to metrics services
         # TYPE exposer_transferred_bytes_total counter
         exposer_transferred_bytes_total 35945
         # HELP exposer_scrapes_total Number of times metrics were scraped
         # TYPE exposer_scrapes_total counter
         exposer_scrapes_total 1
         # HELP exposer_request_latencies Latencies of serving scrape requests, in microseconds
         # TYPE exposer_request_latencies summary
         exposer_request_latencies_count 1
         exposer_request_latencies_sum 2369
         exposer_request_latencies{quantile="0.5"} Nan
         exposer_request_latencies{quantile="0.9"} Nan
         exposer_request_latencies{quantile="0.99"} Nan
         # HELP target Target metadata
         # TYPE target gauge
         target_info{otel_scope_name="grpc-c++",otel_scope_version="1.62.0-dev",service_name="unknown_service",k8s_pod_name="psm-grpc-server-6f75c8f857-qst5k",k8s_namespace_name="default",k8s_container_name="$(CONTAINER_NAME)",telemetry_sdk_version="1.13.0",telemetry_sdk_name="opentelemetry",telemetry_sdk_language="cpp"} 1 1708157423871
         # HELP grpc_server_call_sent_total_compressed_message_size_bytes Compressed message bytes sent per server call
         # TYPE grpc_server_call_sent_total_compressed_message_size_bytes histogram
         grpc_server_call_sent_total_compressed_message_size_bytes_count{csm_mesh_id="gsmmesh-fogj-my-cluster-us-central1-a-fogjnvmqo8fn",csm_remote_workload_canonical_service="unknown",csm_remote_workload_cluster_name="my-cluster",csm_remote_workload_location="us-central1-a",csm_remote_workload_name="test-workload-name",csm_remote_workload_namespace_name="default",csm_remote_workload_project_id="project-id",csm_remote_workload_type="gcp_kubernetes_engine",csm_workload_canonical_service="unknown",grpc_method="helloworld.Greeter/SayHello",grpc_status="OK",otel_scope_name="grpc-c++",otel_scope_version="1.62.0-dev"} 1796 1708157423871
         …
         




## Troubleshoot Cloud Service Mesh observability

This section shows how to troubleshoot common issues.

### An attribute value on the metric shows up as unknown

If an attribute value on the metric shows up as unknown, make sure that all binaries involved (both client and server) are [set up a proxyless gRPC service mesh on GKE](https://docs.cloud.google.com/service-mesh/v1.21/docs/gateway/proxyless-grpc-mesh).

Note that Cloud Service Mesh Observability determines the mesh topological information through environment labels. Make sure that the Pod or service spec for both the client and the service specify all the labels as described in the example.

  1. Describe the psm-grpc-server deployment:
         
         kubectl describe Deployment psm-grpc-server | grep "psm-grpc-server:" -A 12
         

The output is similar to:
         
         psm-grpc-server:
         Image:      grpc/csm-example-server:2024-02-13
         Port:       50051/TCP
         Host Port:  0/TCP
         Args:
           --port=50051
         Environment:
           GRPC_XDS_BOOTSTRAP:          /tmp/grpc-xds/td-grpc-bootstrap.json
           POD_NAME:                     (v1:metadata.name)
           NAMESPACE_NAME:               (v1:metadata.namespace)
           CSM_WORKLOAD_NAME:           psm-grpc-server
           OTEL_RESOURCE_ATTRIBUTES:    k8s.pod.name=$(POD_NAME),k8s.namespace.name=$(NAMESPACE_NAME),k8s.container.name=$(CONTAINER_NAME)
         

  2. Describe the psm-grpc-client deployment:
         
         kubectl describe Deployment psm-grpc-client | grep "psm-grpc-client:" -A 12
         

The output is similar to:
         
         psm-grpc-client:
         Image:      grpc/csm-example-client:2024-02-13
         Port:       <none>
         Host Port:  <none>
         Args:
           --target=xds:///helloworld.default.svc.cluster.local:50051
         Environment:
           GRPC_XDS_BOOTSTRAP:          /tmp/grpc-xds/td-grpc-bootstrap.json
           CSM_WORKLOAD_NAME:           test-workload-name
           POD_NAME:                     (v1:metadata.name)
           NAMESPACE_NAME:               (v1:metadata.namespace)
           CONTAINER_NAME:              psm-grpc-client
         




### Metrics are not displayed

If you're using the Prometheus exporter, verify that the URL for the Prometheus exporter is set up as expected.

Make sure that the gRPC channels are Cloud Service Mesh enabled. The channels should have a target of the form `xds:///`. gRPC servers are always enabled for Cloud Service Mesh.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
