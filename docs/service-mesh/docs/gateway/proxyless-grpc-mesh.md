---
url: https://docs.cloud.google.com/service-mesh/docs/gateway/proxyless-grpc-mesh/
title: Set up a proxyless gRPC service mesh on GKE \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:23.443193+00:00
---

# Set up a proxyless gRPC service mesh on GKE  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/gateway/proxyless-grpc-mesh/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a proxyless gRPC service mesh on GKE

This pages describes how to deploy an example proxyless gRPC client and server to a Cloud Service Mesh.

## Prerequisites

As a starting point, this guide assumes that you have already:

  * [Created a GKE cluster and registered it to a fleet](https://docs.cloud.google.com/service-mesh/docs/gateway/prepare-gateway#create_and_register_a_cluster).
  * [Installed the custom resource definitions](https://docs.cloud.google.com/service-mesh/docs/gateway/prepare-gateway#install_custom_resource_definitions).



## Requirements

This section lists the requirements for supported services:

  * gRPC C++ - version 1.68.1 or later
  * gRPC Java - version 1.68.2 or later
  * gRPC Go - version 1.68.0 or later
  * gRPC Python - version 1.68.1 or later



## Set up the Proxyless gRPC Service

This guide outlines two methods for setting up a proxyless gRPC service within your service mesh:

#### Method 1: Manual Configuration

This method requires you to manually configure the necessary components for your proxyless gRPC service.

  * **InitContainer** : Use an initContainer within your pod's specification to execute the Traffic Director gRPC Bootstrap generator. This generator produces the required configuration for your service.
  * **Volume Mount** : Mount a volume that contains the generated configuration from the initContainer. This ensures your application can access the necessary settings.
  * **Environment Variables** : Include the appropriate environment variables to enable CSM Observability metrics emission from your application. These metrics provide valuable insights into your service's performance.



#### Method 2: Automatic using Proxyless Bootstrap Injector

Instead of manually configuring your proxyless gRPC service, you can opt for a simplified approach using the Proxyless Bootstrap Injector.

This feature automates the setup process, making it easier to deploy your service. To enable it, add the label `mesh.cloud.google.com/csm-injection=proxyless` to your namespace.

By adding this label to your namespace, the injector takes care of all the necessary configurations, saving you valuable time and effort.

If you need more granular control you can also apply this label directly to individual pods. This lets you to override the namespace-level setting and customize the injection behavior on a per-pod basis.

**Note:** The Proxyless Bootstrap Injector simplifies the setup of your proxyless gRPC service. However, it does introduce a dependency on Google infrastructure for pod initialization. If you prefer to avoid this dependency for reliability or other reasons, you can maintain greater control by using the manual configuration method. This provides a more self-contained approach, though it requires additional steps.

By following either of these methods, you can successfully establish a proxyless gRPC service within your service mesh.

### Manual

  1. Apply the Namespace
         
         kubectl apply -f - <<EOF
         ---
         kind: Namespace
         apiVersion: v1
         metadata:
          name: proxyless-example
         EOF
         

  2. Deploy a gRPC service:




### C++
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-cpp-server:v1.68.1
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: CONTAINER_NAME
                value: psm-grpc-server
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-java-server:v1.68.2
            imagePullPolicy: Always
            args:
              - "50051"
              - "9464"
            ports:
              - containerPort: 50051
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: CONTAINER_NAME
                value: psm-grpc-server
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-go-server:v1.69.4
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: CONTAINER_NAME
                value: psm-grpc-server
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-server
        spec:
          containers:
          - name: psm-grpc-server
            image: grpc/csm-o11y-example-python-server:v1.68.1
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: POD_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.name
              - name: CONTAINER_NAME
                value: psm-grpc-server
              - name: NAMESPACE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.namespace
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-server
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    EOF
    

The output is similar to
    
    
    namespace/proxyless-example created
    service/helloworld created
    deployment.apps/psm-grpc-server created
    

### Automatic

  1. Apply the Namespace
         
         kubectl apply -f - <<EOF
         ---
         kind: Namespace
         apiVersion: v1
         metadata:
          name: proxyless-example
         EOF
         

  2. Run the following command to enable Proxyless Bootstrap Injector in the proxyless-example namespace:
         
         kubectl label namespace proxyless-example mesh.cloud.google.com/csm-injection=proxyless
         

  3. Deploy a gRPC service:




### C++
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-cpp-server:v1.68.1
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-java-server:v1.68.2
            imagePullPolicy: Always
            args:
              - "50051"
              - "9464"
            ports:
              - containerPort: 50051
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-go-server:v1.69.4
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    ---
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      namespace: proxyless-example
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
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-python-server:v1.68.1
            imagePullPolicy: Always
            args:
              - "--port=50051"
            ports:
              - containerPort: 50051
    EOF
    

The output is similar to
    
    
    namespace/proxyless-example created
    service/helloworld created
    deployment.apps/psm-grpc-server created
    

  1. Verify that the Pods have been created:
         
         kubectl get pods -n proxyless-example
         

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
           namespace: proxyless-example
         spec:
           parentRefs:
           - name: helloworld
             namespace: proxyless-example
             kind: Service
             group: ""
           rules:
           - backendRefs:
             - name: helloworld
               port: 50051
         EOF
         

This command creates an HTTPRoute called app1 and sends all RPCs to the `helloworld` service.

Note that the `parentRef` service is also `helloworld` which means our HTTPRoute is attached to this service and will process all RPCs addressed to this service. In case of proxyless gRPC it means any client sending RPCs on a gRPC channel for target `xds:///helloworld.proxyless-example.svc.cluster.local:50051`.

  3. Verify that the new app1 HTTPRoute has been created:
         
         kubectl get httproute -n proxyless-example
         

The output is similar to
         
         NAME   HOSTNAMES   AGE
         app1               72s
         




## Set up the Proxyless gRPC Client

This sections describes how to use a gRPC client to verify that Cloud Service Mesh is routing traffic correctly in the mesh.

Just like configuring the service, you have two choices for setting up the client:

#### Method 1: Manual Configuration

This approach involves manually setting up the necessary components for your client, mirroring the manual service configuration.

#### Method 2: Automatic using Proxyless Bootstrap Injector

Alternatively, you can use the automatic injector to streamline the client setup process. This simplifies configuration and reduces manual intervention. This is achieved by applying the label on the namespace.

Both options provide the necessary capabilities for your client. Choose the method that best suits your needs and preferences.

### Manual

Run a gRPC client and direct it to use the routing configuration specified by the HTTPRoute:

### C++
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-cpp-client:v1.68.1
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-java-client:v1.68.2
            imagePullPolicy: Always
            args:
              - "world"
              - "xds:///helloworld.proxyless-example.svc.cluster.local:50051"
              - "9464"
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-go-client:v1.69.4
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            service.istio.io/canonical-name: deployment-psm-grpc-client
        spec:
          containers:
          - name: psm-grpc-client
            image: grpc/csm-o11y-example-python-client:v1.68.1
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
            **env:          - name: GRPC_XDS_BOOTSTRAP
                value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
              - name: CSM_WORKLOAD_NAME
                value: psm-grpc-client
              - name: CSM_CANONICAL_SERVICE_NAME
                valueFrom:
                  fieldRef:
                    fieldPath: metadata.labels['service.istio.io/canonical-name']
              - name: CSM_MESH_ID
                value: proj-PROJECT_NUMBER
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
                medium: Memory**
    
    EOF
    

### Automatic

Run a gRPC client and direct it to use the routing configuration specified by the HTTPRoute:

### C++
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-cpp-client:v1.68.1
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
    EOF
    

### Java
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-java-client:v1.68.2
            imagePullPolicy: Always
            args:
              - "world"
              - "xds:///helloworld.proxyless-example.svc.cluster.local:50051"
              - "9464"
    EOF
    

### Go
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-go-client:v1.69.4
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
    EOF
    

### Python
    
    
    kubectl apply -f - <<EOF
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: psm-grpc-client
      namespace: proxyless-example
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
            image: grpc/csm-o11y-example-python-client:v1.68.1
            imagePullPolicy: Always
            args:
              - "--target=xds:///helloworld.proxyless-example.svc.cluster.local:50051"
    EOF
    

The output is similar to
    
    
    deployment.apps/psm-grpc-client created
    

To verify if the client was able to reach the service, view the client's logs:
    
    
    kubectl logs -n proxyless-example $(kubectl get po -n proxyless-example | grep psm-grpc-client | awk '{print $1;}') -f
    

The output is similar to:
    
    
    Defaulted container "psm-grpc-client" out of: psm-grpc-client, grpc-td-init (init)
    Greeter received: Hello from psm-grpc-server-xxxxxxx-xxxx world
    

## Google Cloud Managed Service for Prometheus Setup (Optional)

You can deploy the [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) `PodMonitoring` resource to export the metrics to Cloud Monitoring.

  * For servers, run the following command:
        
        kubectl apply -f - <<EOF
        apiVersion: monitoring.googleapis.com/v1
        kind: PodMonitoring
        metadata:
          name: psm-grpc-server-gmp
          namespace: proxyless-example
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
          namespace: proxyless-example
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

you can navigate to the "Metrics Explorer" section of your Google Cloud console, select Prometheus Target > Grpc to find the metrics.

[Go to Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

You can observe the deployed workloads and services in the "Service Mesh" section of your Google Cloud console. 

[Go to Service Mesh](https://console.cloud.google.com/kubernetes/services)

## Troubleshoot Cloud Service Mesh observability

This section shows how to troubleshoot common issues.

### Metrics are not exported / displayed

Make sure that all binaries involved (both client and server) are [set up with Observability](https://docs.cloud.google.com/service-mesh/docs/service-routing/observability-proxyless-grpc).

If you're using the Prometheus exporter, verify that the URL for the Prometheus exporter is set up as expected.

Make sure that the gRPC channels are Cloud Service Mesh enabled. The channels should have a target of the form `xds:///`. gRPC servers are always enabled for Cloud Service Mesh.

### No metrics exported / An attribute value on a metric shows up as unknown

Cloud Service Mesh Observability determines the mesh topological information through environment labels. Make sure that the Pod or service spec for both the client and the service specify all the labels as described in the example.

  1. Describe the psm-grpc-server deployment:
         
         kubectl describe Deployment psm-grpc-server -n proxyless-example \
         | grep "psm-grpc-server:" -A 12
         

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
         
         kubectl describe Deployment psm-grpc-client -n proxyless-example \
         | grep "psm-grpc-client:" -A 12
         

The output is similar to:
         
         psm-grpc-client:
         Image:      grpc/csm-example-client:2024-02-13
         Port:       <none>
         Host Port:  <none>
         Args:
           --target=xds:///helloworld.proxyless-example.svc.cluster.local:50051
         Environment:
           GRPC_XDS_BOOTSTRAP:          /tmp/grpc-xds/td-grpc-bootstrap.json
           CSM_WORKLOAD_NAME:           test-workload-name
           POD_NAME:                     (v1:metadata.name)
           NAMESPACE_NAME:               (v1:metadata.namespace)
           CONTAINER_NAME:              psm-grpc-client
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
