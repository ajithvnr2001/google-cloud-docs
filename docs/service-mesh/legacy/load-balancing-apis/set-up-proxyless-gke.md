---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke/
title: Set up Google Kubernetes Engine and proxyless gRPC services \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:26.129243+00:00
---

# Set up Google Kubernetes Engine and proxyless gRPC services  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Google Kubernetes Engine and proxyless gRPC services

This guide describes how to configure Google Kubernetes Engine, gRPC applications, and the load balancing components that Cloud Service Mesh requires.

Before you follow the instructions in this guide, review [Preparing to set up Cloud Service Mesh with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-proxyless-grpc).

## Overview

Setting up Cloud Service Mesh with GKE and proxyless gRPC services involves the following:

  1. Preparing your GKE cluster.
  2. Deploying a gRPC server application as a Kubernetes service. Annotate the GKE deployment specification to automatically create a network endpoint group (NEG) for the service.
  3. Configuring Cloud Service Mesh using the NEG and other Google Cloud load balancing components.
  4. Verifying that the deployment works correctly by using a proxyless gRPC client application to send traffic to the gRPC server application.



## Configuring GKE clusters for Cloud Service Mesh

This section provides instructions for enabling GKE clusters to work with Cloud Service Mesh.

### GKE cluster requirements

GKE clusters must meet the following requirements:

  * You must enable support for network endpoint groups. For more information and examples, see [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg). The standalone NEGs feature is available in General Availability for Cloud Service Mesh.
  * The cluster nodes instances' service account must have permission to access the Cloud Service Mesh API. For more information on the required permissions, see [Enabling the service account to access the Cloud Service Mesh API](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-for-envoy-setup#enable-service-account).
  * The containers must have access to the Cloud Service Mesh API, which is protected by OAuth authentication. For more information, see [host configuration](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms#configure-vm-host).



### Creating the GKE cluster

The following example shows how to create a GKE cluster called `grpc-td-cluster` in the `us-central1-a zone`.

### Console

To create a cluster using Google Cloud console, perform the following steps:

  1. Go to the Kubernetes Engine menu in Google Cloud console.

[Go to the Google Kubernetes Engine menu](https://console.cloud.google.com/kubernetes/list)

  2. Click **Create cluster**.

  3. Choose the **Standard cluster** template or [choose an appropriate template](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster#cluster-templates) for your workload.

  4. Customize the template if necessary. The following fields are required:

     * **Name:** Enter `grpc-td-cluster`.
     * **Location type:** `Zonal`.
     * **Zone:** `us-central1-a`.
     * **Node pool:**
  5. In the left-hand menu, click **default-pool.**

  6. Change the **Name** to `grpc-td-cluster`.

  7. Under **Size** , enter the number of nodes to create. You must have available [resource quota](https://docs.cloud.google.com/kubernetes-engine/quotas#resource_quota) for the nodes and their resources (such as firewall routes).

  8. In the left-hand menu, click **Nodes**.

  9. Under **Machine Configuration** , in **Machine family** , click **Compute Optimized**.

  10. Select a **Machine type**. For machine type pricing information, see the [Compute Engine pricing page](https://cloud.google.com/compute/pricing).

  11. Under **Networking** , add the **Network tag** `allow-health-checks`.

  12. In the left-hand menu, click **Node security**.

  13. Under **Access scopes** , select **Allow full access to all Cloud APIs**.

  14. Click **Create**.




After you create a cluster in Google Cloud console, you need to configure `kubectl` to interact with the cluster. To learn more, refer to [Generating a `kubeconfig` entry](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#generate_kubeconfig_entry).

###  gcloud 

Create the cluster.
    
    
    gcloud container clusters create grpc-td-cluster \
       --zone us-central1-a \
       --scopes=https://www.googleapis.com/auth/cloud-platform \
       --tags=allow-health-checks \
       --enable-ip-alias
    

### Obtaining the required GKE cluster privileges

Switch to the cluster you just created by issuing the following command. This points `kubectl` to the correct cluster.

###  gcloud 
    
    
    gcloud container clusters get-credentials grpc-td-cluster \
        --zone us-central1-a
    

## Configuring GKE services

This section describes how to prepare GKE deployment specifications to work with Cloud Service Mesh. This consists of configuring a GKE `helloworld` example service with NEG annotations.

The `helloworld` example service is a gRPC server application that returns a message in response to a gRPC client's request. Note that there is nothing special about the `helloworld` service. It's not a proxyless gRPC service and can respond to requests from any gRPC client.

The "proxyless" part only comes into play when a gRPC client application connects to Cloud Service Mesh, learns about the `helloworld` service and can then send traffic to Pods associated with `helloworld`, without needing to rely on IP addresses or DNS-based name resolution.

### Configuring GKE services with NEGs

The first step in configuring GKE services for use with Cloud Service Mesh is to expose the service through a NEG. To be exposed through NEGs, each specification must have the following annotation, matching the port that you want to expose.
    
    
    ...
    metadata:
      annotations:
        cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
    

This annotation creates a standalone NEG when you first deploy your service. This NEG contains endpoints that are the Pod's IP addresses and ports. For more information and examples, see [Standalone network endpoint groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).

In the following example, you deploy a `helloworld` Kubernetes service that is exposed on port `8080`. This is the port on which the service is visible in the cluster. The gRPC service in the Pod is listening on `targetPort` `50051`. This is the port on the Pod to which the request is sent. Typically, the `port` and `targetPort` are set to the same value for convenience, but this example uses different values to indicate the correct value to use in the NEG annotation.
    
    
    cat << EOF > grpc-td-helloworld.yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: helloworld
      annotations:
        cloud.google.com/neg: '{"exposed_ports":{"8080":{"name": "example-grpc-server"}}}'
    spec:
      ports:
      - port: 8080
        name: helloworld
        protocol: TCP
        targetPort: 50051
      selector:
        run: app1
      type: ClusterIP
    
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: app1
      name: app1
    spec:
      selector:
        matchLabels:
          run: app1
      replicas: 2
      template:
        metadata:
          labels:
            run: app1
        spec:
          containers:
          - image: grpc/java-example-hostname:1.50.2
            name: app1
            ports:
            - protocol: TCP
              containerPort: 50051
    EOF
    
    
    
    kubectl apply -f grpc-td-helloworld.yaml
    

Verify that the new `helloworld` service is created:
    
    
    kubectl get svc
    

The output of `kubectl get svc` should be similar to this:
    
    
    NAME           TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
    helloworld     ClusterIP   10.71.9.71   <none>        8080/TCP  41m
    [..skip..]
    

Verify that the application Pod is running:
    
    
    kubectl get pods
    

The output of `kubectl get pods` should be similar to this:
    
    
    NAME                        READY     STATUS    RESTARTS   AGE
    app1-6db459dcb9-zvfg2   1/1       Running   0          6m
    app1-6db459dcb9-hlvhj   1/1       Running   0          6m
    [..skip..]
    

Verify that the NEG name is correct.

### Console

To view a list of network endpoint groups, go to the Network Endpoint Groups page in the Google Cloud console. You see a NEG named `example-grpc-server`.  
[Go to the Network Endpoint Groups page](https://console.cloud.google.com/compute/networkendpointgroups/list)

###  gcloud 
    
    
    # List the NEGs
    gcloud compute network-endpoint-groups list \
        --filter "name=example-grpc-server" --format "value(name)"
    
    # Optionally examine the NEG
    gcloud compute network-endpoint-groups describe example-grpc-server \
        --zone us-central1-a
    
    # Optionally examine the endpoint(s) contained
    gcloud compute network-endpoint-groups list-network-endpoints example-grpc-server \
        --zone us-central1-a
    

## Configuring Cloud Service Mesh with load balancing components

This section describe how to configure Google Cloud load balancing components for your services. These components contain configuration information that enables proxyless gRPC clients to communicate with your GKE services.

The Cloud Service Mesh configuration example that follows makes these assumptions:

  * The NEGs and all other resources are created in the automode default network, in the zone `us-central1-a`.
  * When you use the Google Cloud CLI, the NEG name for the cluster is `example-grpc-server`.



### Creating the health check, firewall rule, and backend service

In this section, you create a health check and the firewall rule for the health check. The health check must use the gRPC health check protocol. The firewall rule allows the health check probes to connect to the VMs in your deployment. The `--use-serving-port` directive is used by health checks to get the configured listening port for each endpoint.

The firewall rule allows incoming health check connections to instances in your network.

In this section, you create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and protocol `GRPC`, then associate the health check with the backend service.

For more information, see [Creating health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).

###  gcloud 

  1. Create the health check.
         
         gcloud compute health-checks create grpc grpc-gke-helloworld-hc \
          --use-serving-port
         

  2. Create the firewall rule.
         
         gcloud compute firewall-rules create grpc-gke-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges 35.191.0.0/16,130.211.0.0/22 \
           --target-tags allow-health-checks \
           --rules tcp:50051
         

  3. Create the backend service.
         
         gcloud compute backend-services create grpc-gke-helloworld-service \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED \
            --protocol=GRPC \
            --health-checks grpc-gke-helloworld-hc
         

  4. Add the backend NEGs to the backend service.
         
         gcloud compute backend-services add-backend grpc-gke-helloworld-service \
            --global \
            --network-endpoint-group example-grpc-server \
            --network-endpoint-group-zone us-central1-a \
            --balancing-mode RATE \
            --max-rate-per-endpoint 5
         




### Creating the routing rule map

In this section, you create a URL map, path matcher, and host rule to route traffic for your service, based on hostname and a path. The following example uses `helloworld-gke` as the service name. The gRPC client uses this service name in the target URI when connecting to the `helloworld` service. You also create the target gRPC proxy and forwarding rule.

For more information, see [Routing rule maps](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-map).

The following example uses the service name `helloworld-gke` and port `8000`. This means the gRPC client must use `xds:///helloworld-gke:8000` to connect to this service, and a host rule `helloworld-gke:8000` must be configured in the URL map. Note that the service port `8080` shown in the Kubernetes service spec in a previous section is not used by Cloud Service Mesh because `helloworld-gke:8000` is directly resolved to the NEG endpoints that are listening on the `targetPort` `50051`. Typically, the port in the URL map host rule and Kubernetes service spec `port` and `targetPort` are all set to the same value for convenience, but this example uses different values to show that the `port` in the service spec is not used by Cloud Service Mesh.

###  gcloud 

  1. Create the URL map.
         
         gcloud compute url-maps create grpc-gke-url-map \
         --default-service grpc-gke-helloworld-service
         

  2. Create the path matcher.
         
         gcloud compute url-maps add-path-matcher grpc-gke-url-map \
         --default-service grpc-gke-helloworld-service \
         --path-matcher-name grpc-gke-path-matcher \
         --new-hosts helloworld-gke:8000
         

  3. Create the target gRPC proxy.
         
         gcloud compute target-grpc-proxies create grpc-gke-proxy \
         --url-map grpc-gke-url-map \
         --validate-for-proxyless
         

  4. Create the forwarding rule.
         
         gcloud compute forwarding-rules create grpc-gke-forwarding-rule \
         --global \
         --load-balancing-scheme=INTERNAL_SELF_MANAGED \
         --address=0.0.0.0 \
         --target-grpc-proxy=grpc-gke-proxy \
         --ports 8000 \
         --network default
         




Cloud Service Mesh is now configured to load balance traffic across the endpoints in the NEG for the services specified in the URL map.

## Verifying the configuration

When the configuration process is complete, verify that you can reach the `helloworld` gRPC server using a proxyless gRPC client. This client connects to Cloud Service Mesh, obtains information about the `helloworld` service (configured with Cloud Service Mesh using the `grpc-gke-helloworld-service` backend service) and uses this information to send traffic to the service's backends.

You can also check the [Cloud Service Mesh section in the Google Cloud console](https://console.cloud.google.com/net-services/trafficdirector) for information on the configured service `helloworld-gke` and check whether the backends are reported as healthy.

### Verification with a proxyless gRPC client

In the following examples, you use gRPC clients in different languages or the `grpcurl` tool to verify that Cloud Service Mesh is routing traffic correctly in the mesh. You create a client Pod, then open a shell and run the verification commands from the shell.

#### Setting up the environment variable and bootstrap file

**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

The client application requires a bootstrap configuration file. Modify your Kubernetes application deployment specification by adding an `initContainer` that generates the bootstrap file and a volume to transfer the file. Update your existing container to find the file.

Add the following `initContainer` to the application deployment spec:
    
    
          initContainers:
          - args:
            - --output
            - "/tmp/bootstrap/td-grpc-bootstrap.json"
            image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
    
            imagePullPolicy: IfNotPresent
            name: grpc-td-init
            resources:
              limits:
                cpu: 100m
                memory: 100Mi
              requests:
                cpu: 10m
                memory: 100Mi
            volumeMounts:
            - name: grpc-td-conf
              mountPath: /tmp/bootstrap/
          volumes:
          - name: grpc-td-conf
            emptyDir:
              medium: Memory
    

Update the application container's `env` section to include the following:
    
    
            env:
            - name: GRPC_XDS_BOOTSTRAP
              value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
            volumeMounts:
            - name: grpc-td-conf
              mountPath: /tmp/grpc-xds/
    

This is a complete example of a client Kubernetes spec:
    
    
    cat << EOF  | kubectl apply -f -
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      labels:
        run: client
      name: sleeper
    spec:
      selector:
        matchLabels:
          run: client
      template:
        metadata:
          labels:
            run: client
        spec:
          containers:
          - image: openjdk:8-jdk
            imagePullPolicy: IfNotPresent
            name: sleeper
            command:
            - sleep
            - 365d
            env:
            - name: GRPC_XDS_BOOTSTRAP
              value: "/tmp/grpc-xds/td-grpc-bootstrap.json"
            resources:
              limits:
                cpu: "2"
                memory: 2000Mi
              requests:
                cpu: 300m
                memory: 1500Mi
            volumeMounts:
            - name: grpc-td-conf
              mountPath: /tmp/grpc-xds/
          initContainers:
          - args:
            - --output
            - "/tmp/bootstrap/td-grpc-bootstrap.json"
            image: gcr.io/trafficdirector-prod/td-grpc-bootstrap:0.19.0
            imagePullPolicy: IfNotPresent
            name: grpc-td-init
            resources:
              limits:
                cpu: 100m
                memory: 100Mi
              requests:
                cpu: 10m
                memory: 100Mi
            volumeMounts:
            - name: grpc-td-conf
              mountPath: /tmp/bootstrap/
          volumes:
          - name: grpc-td-conf
            emptyDir:
              medium: Memory
    EOF
    

When the deployment is ready, open a shell to the client Pod.
    
    
    kubectl exec -it $(kubectl get pods -o custom-columns=:.metadata.name \
        --selector=run=client) -- /bin/bash
    

To verify the configuration, run the appropriate examples in the Pod shell.

###  Java 

To verify the service with a gRPC Java client:

  1. Download the latest version of gRPC Java, with the most recent patch and build the `xds-hello-world` client application.
         
         curl -L https://github.com/grpc/grpc-java/archive/v1.37.0.tar.gz | tar -xz
          cd grpc-java-1.37.0/examples/example-xds
          ../gradlew --no-daemon installDist
          

  2. Run the client with `"world"` as its name and `"xds:///helloworld-gke:8000"` as the service URI and port.
         
         ./build/install/example-xds/bin/xds-hello-world-client "world" \
         xds:///helloworld-gke:8000
         




###  Go 

To verify the service with a gRPC Go client:

  1. Download the latest version of gRPC Go, with the most recent patch, and build the `xds-hello-world` client application.
         
         apt-get update -y
         apt-get install -y golang git
         curl -L https://github.com/grpc/grpc-go/archive/v1.37.0.tar.gz | tar -xz
         cd grpc-go-1.37.0/examples/features/xds/client
         go get google.golang.org/grpc@v1.37.0
         go build .
         

  2. Run the client with `"world"` as its name and `"xds:///helloworld-gke:8000"` as the service URI and port.
         
         ./client "world" xds:///helloworld-gke:8000
         




###  C++ 

To verify the service with a gRPC C++ client:

  1. Downloadi the latest version of gRPC C++,with the most recent patch, and build the `helloworld` client example.
         
         apt-get update -y
         apt-get install -y build-essential cmake git
         git clone --recurse-submodules -b v1.37.1 https://github.com/grpc/grpc
         cd grpc
         mkdir -p cmake/build
         pushd cmake/build
         cmake ../..
         make
         make install
         popd
         mkdir -p third_party/abseil-cpp/cmake/build
         pushd third_party/abseil-cpp/cmake/build
         cmake ../..
         make
         make install
         popd
         cd examples/cpp/helloworld
         mkdir -p cmake/build
         cd cmake/build/
         cmake ../..
         make
         

  2. Run the client with "xds:///helloworld-gke:8000" as the service URI and port.
         
         ./greeter_client --target=xds:///helloworld-gke:8000
         




###  grpcurl 

The `grpcurl` tool can also act as a proxyless gRPC client. In this case, `grpcurl` uses the environment variable and bootstrap information to connect to Cloud Service Mesh. It then learns about the `helloworld` service, which was configured with Cloud Service Mesh through the `grpc-gke-helloworld-service` backend service.

To verify your configuration using the `grpcurl` tool:

  1. Download and install the `grpcurl` tool.
         
         curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.8.1/grpcurl_1.8.1_linux_x86_64.tar.gz | tar -xz
         

  2. Run the `grpcurl` tool with "xds:///helloworld-gke:8000" as the service URI and `helloworld.Greeter/SayHello` as the service name and method to invoke. The parameters to the `SayHello` method are passed using the `-d` option.
         
         ./grpcurl --plaintext \
           -d '{"name": "world"}' \
           xds:///helloworld-gke:8000 helloworld.Greeter/SayHello
         




###  Python 

To verify the service with a gRPC Python client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    apt-get update -y
    apt-get install python3-pip -y
    pip3 install virtualenv
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1/examples/python/xds
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements.txt
    python client.py  xds:///helloworld-gke:8000
    

###  Ruby 

To verify the service with a gRPC Ruby client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    apt-get update -y
    apt-get install -y ruby-full
    gem install grpc
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1/examples/ruby
    ruby greeter_client.rb john xds:///helloworld-gke:8000
    

###  PHP 

To verify the service with a gRPC PHP client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    apt-get update -y
    apt-get install -y php7.3 php7.3-dev php-pear phpunit python-all zlib1g-dev git
    pecl install grpc
    curl -sS https://getcomposer.org/installer | php
    mv composer.phar /usr/local/bin/composer
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1
    export CC=/usr/bin/gcc
    ./tools/bazel build @com_google_protobuf//:protoc
    ./tools/bazel build src/compiler:grpc_php_plugin
    cd examples/php
    composer install
    ../../bazel-bin/external/com_google_protobuf/protoc --proto_path=../protos \
    --php_out=. --grpc_out=. \
    --plugin=protoc-gen-grpc=../../bazel-bin/src/compiler/grpc_php_plugin \
    ../protos/helloworld.proto
    php -d extension=grpc.so greeter_client.php john xds:///helloworld-gke:8000
    

###  Node.js 

To verify the service with a gRPC Node.js client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    apt-get update -y
    apt-get install -y nodejs npm
    curl -L https://github.com/grpc/grpc/archive/v1.34.0.tar.gz | tar -xz
    cd grpc-1.34.0/examples/node/xds
    npm install
    node ./greeter_client.js --target=xds:///helloworld-gke:8000
    

You should see output similar to this, where `INSTANCE_HOST_NAME` is the hostname of the VM instance::

`Greetings: Hello world, from INSTANCE_HOST_NAME`

This verifies that the proxyless gRPC client successfully connected to Cloud Service Mesh and learned about the backends for the `helloworld-gke` service using the xds name resolver. The client sent a request to one of the service's backends without needing to know about the IP address or performing DNS resolution.

## What's next

  * Learn about [Cloud Service Mesh service security](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/security-overview-legacy).
  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-traffic-management-legacy).
  * Learn how to [set up observability](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/observability-proxyless).
  * Learn how to [troubleshoot proxyless Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
