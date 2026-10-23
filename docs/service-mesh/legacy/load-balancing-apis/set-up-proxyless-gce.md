---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gce/
title: Set up Compute Engine VMs and proxyless gRPC services \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:52.960998+00:00
---

# Set up Compute Engine VMs and proxyless gRPC services  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gce/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Compute Engine VMs and proxyless gRPC services

This guide shows you how to configure Compute Engine VM hosts, gRPC applications, and the load balancing components that Cloud Service Mesh requires.

Before you follow the instructions in this guide, review [Prepare to set up Cloud Service Mesh with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/prepare-proxyless-grpc)

## Overview

Setting up Cloud Service Mesh with Compute Engine virtual machines (VMs) and proxyless gRPC services involves the following:

  1. Setting up a managed instance group that hosts your backends.
  2. Configuring the backends to run a gRPC server that returns `hello world` in response to a request from a client.
  3. Configuring Cloud Service Mesh using the managed instance group and other Google Cloud load balancing components.
  4. Verifying that the deployment works correctly by using a proxyless gRPC client application to send traffic to the gRPC server application.



The proxyless gRPC client connects to Cloud Service Mesh using xDS. When the client connects to Cloud Service Mesh, Cloud Service Mesh sends information to the client about the backends associated with the `hello world` service. Using this information, the proxyless gRPC client sends requests to the `hello world` gRPC server.

## Configuring a managed instance group for Cloud Service Mesh

Managed instance groups use autoscaling to create new backend VMs, as needed by your deployment. This example shows you how to do the following:

  * Create an instance template with a sample service that serves a `hello world` service using the gRPC protocol.
  * Configure a managed instance group using the template.



### Creating the instance template

This section provides instructions for creating an instance template. In the example, you deploy a `helloworld` gRPC service that is exposed on port 50051.

###  Console 

  1. In the Google Cloud console, go to the Instance Templates page. 

[Go to the Instance templates page](https://console.cloud.google.com/compute/instanceTemplates/list)

  2. Click **Create instance template**.
  3. Fill in the fields as follows:

     * Name: grpc-td-vm-template
     * Boot disk version: Debian / Linux 10
     * Service account: Compute Engine default service account
     * Access scopes: Allow full access to all Google Cloud APIs
  4. Under **Firewall** , select the boxes next to **Allow HTTP traffic** and **Allow HTTPS traffic**.

  5. Click **Management, Security, Disks, Networking, Sole Tenancy**.

  6. In the **Management** tab, copy the following script into the **[Startup script](https://docs.cloud.google.com/compute/docs/startupscript)** field.
         
         #! /bin/bash
         set -e
         cd /root
         sudo apt-get update -y
         sudo apt-get install -y openjdk-11-jdk-headless
         curl -L https://github.com/grpc/grpc-java/archive/v1.37.0.tar.gz | tar -xz
         cd grpc-java-1.37.0/examples/example-hostname
         ../gradlew --no-daemon installDist
         # Server listens on 50051
         sudo systemd-run ./build/install/hostname-server/bin/hostname-server
         

  7. Click **Create**.




###  gcloud 

Create the instance template.
    
    
    gcloud compute instance-templates create grpc-td-vm-template \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --tags=allow-health-checks \
      --image-family=debian-10 \
      --image-project=debian-cloud \
      --metadata-from-file=startup-script=<(echo '#! /bin/bash
    set -e
    cd /root
    sudo apt-get update -y
    sudo apt-get install -y openjdk-11-jdk-headless
    curl -L https://github.com/grpc/grpc-java/archive/v1.37.0.tar.gz | tar -xz
    cd grpc-java-1.37.0/examples/example-hostname
    ../gradlew --no-daemon installDist
    # Server listens on 50051
    sudo systemd-run ./build/install/hostname-server/bin/hostname-server')
    

### Creating the managed instance group

In this section, you create a managed instance group using the instance template you created in the previous section.

###  Console 

  1. Go to the Instance Groups page in the Google Cloud console. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click **Create an instance group**. By default, you see the page for creating a managed instance group.
  3. Enter `grpc-td-mig-us-central1` for the name for the managed instance group, and select the `us-central1-a` zone.
  4. Under **Instance template** , select `grpc-td-vm-template`, which is the instance template you created.
  5. Specify 2 as the minimum and maximum number of instances that you want to create in the group.
  6. Click **Create**.



###  gcloud 

Create the managed instance group.
    
    
    gcloud compute instance-groups managed create grpc-td-mig-us-central1 \
      --zone us-central1-a \
      --size=2 \
      --template=grpc-td-vm-template
    

### Configuring the named port

In this section, you configure the named port for the gRPC service. The named port is the port on which the gRPC service listens for requests. In this example, the named port is port 50051.

###  Console 

  1. Go to the Instance Groups page in the Google Cloud console. 

[Go to the Instance Groups page](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the instance group `grpc-td-mig-us-central1`, which you created.
  3. Click **Edit group**.
  4. In the **Port name** field, enter `grpc-helloworld-port`.
  5. In the **Port number** field, enter `50051`.
  6. Click **Save**.



###  gcloud 

Configure the named port.
    
    
    gcloud compute instance-groups set-named-ports grpc-td-mig-us-central1 \
      --named-ports=grpc-helloworld-port:50051 \
      --zone us-central1-a
    

## Configuring Cloud Service Mesh with Google Cloud load balancing components

This section provides instructions for configuring Cloud Service Mesh with Google Cloud load balancing components for your services.

### Creating the health check, firewall rule, and backend service

In this section, you create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and protocol `GRPC`, and then associate the health check and instance group with the backend service. In this example, you use the managed instance group you created in Creating the managed instance group. This managed instance group runs the sample gRPC service. The port in the `--port-name` flag is the named port you created in Configuring the named port.

###  gcloud 

  1. Create the health check.
         
         gcloud compute health-checks create grpc grpc-helloworld-health-check \
          --use-serving-port
         

  2. Create the health check firewall rule.
         
         gcloud compute firewall-rules create grpc-vm-allow-health-checks \
           --network default --action allow --direction INGRESS \
           --source-ranges=35.191.0.0/16,130.211.0.0/22 \
           --target-tags allow-health-checks \
           --rules tcp:50051
         

  3. Create the backend service.
         
         gcloud compute backend-services create grpc-helloworld-service \
            --global \
            --load-balancing-scheme=INTERNAL_SELF_MANAGED \
            --protocol=GRPC \
            --port-name=grpc-helloworld-port \
            --health-checks=grpc-helloworld-health-check
         

  4. Add the managed instance group to the backend service.
         
         gcloud compute backend-services add-backend grpc-helloworld-service \
          --instance-group grpc-td-mig-us-central1 \
          --instance-group-zone us-central1-a \
          --global
         




### Creating the routing rule map, target proxy, and forwarding rule

In this section, you create a URL map, path matcher, and host rule to route traffic for your service based on hostname and a path. The following example uses `helloworld-gce` as the service name. The gRPC application uses this service name in the target URI when connecting to this service. By default, the path matcher matches all path requests (`/*`) for this host. You also create the target gRPC proxy and forwarding rule.

For more information, see [Routing rule maps](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-map).

In the following example, port 80 is the specified port.

###  gcloud 

  1. Create the URL map.
         
         gcloud compute url-maps create grpc-vm-url-map \
           --default-service grpc-helloworld-service
         

  2. Create the path matcher.
         
         gcloud compute url-maps add-path-matcher grpc-vm-url-map \
           --default-service grpc-helloworld-service \
           --path-matcher-name grpc-vm-path-matcher \
           --new-hosts helloworld-gce
         

  3. Create the target gRPC proxy.
         
         gcloud compute target-grpc-proxies create grpc-vm-proxy \
          --url-map grpc-vm-url-map \
          --validate-for-proxyless
         

  4. Create the forwarding rule.
         
         gcloud compute forwarding-rules create grpc-vm-forwarding-rule \
          --global \
          --load-balancing-scheme=INTERNAL_SELF_MANAGED \
          --address=0.0.0.0 --address-region=us-central1 \
          --target-grpc-proxy=grpc-vm-proxy \
          --ports 80 \
          --network default
         




Cloud Service Mesh is now configured to load balance traffic across the backends in the managed instance group for the services specified in the URL map.

## Verifying the configuration

When the configuration process is complete, verify that you can establish a gRPC connection to the Cloud Service Mesh load balanced service that you previously created.

To verify that the service is available, do one of the following:

  * Sign in to one of the VM hosts (the gRPC service backend) and verify that the gRPC service is running on the listening port. In the example, the port is 50051.
  * Check the [Cloud Service Mesh page in the Console](https://console.cloud.google.com/net-services/trafficdirector/services/list) for information on the configured service `helloworld-gce`, and confirm that the backends are reported as healthy.
  * Use the following instructions to use a Compute Engine gRPC client for verification.



### Verifying the service with a gRPC client application

In the following examples, you use a gRPC client in the language of your choice or the `grpcurl` tool to test the gRPC service.

First, create a client VM on which you run the gRPC client to test the service.
    
    
    gcloud compute instances create grpc-client \
      --zone us-central1-a \
      --scopes=https://www.googleapis.com/auth/cloud-platform \
      --image-family=debian-10 \
      --image-project=debian-cloud \
      --metadata-from-file=startup-script=<(echo '#! /bin/bash
    set -e
    export GRPC_XDS_BOOTSTRAP=/run/td-grpc-bootstrap.json
    # Expose bootstrap variable to SSH connections
    echo export GRPC_XDS_BOOTSTRAP=$GRPC_XDS_BOOTSTRAP | sudo tee /etc/profile.d/grpc-xds-bootstrap.sh
    # Create the bootstrap file
    curl -L https://storage.googleapis.com/traffic-director/td-grpc-bootstrap-0.19.0.tar.gz | tar -xz
    ./td-grpc-bootstrap-0.19.0/td-grpc-bootstrap | tee $GRPC_XDS_BOOTSTRAP')
    

#### Setting up the environment variable and bootstrap file

**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

The client application needs a bootstrap configuration file. The startup script in the previous section sets the `GRPC_XDS_BOOTSTRAP` environment variable and uses a helper script to generate the bootstrap file. The values for `TRAFFICDIRECTOR_GCP_PROJECT_NUMBER`, `TRAFFICDIRECTOR_NETWORK_NAME`, and `zone` in the generated bootstrap file are obtained from the metadata server that knows these details about your Compute Engine VM instances. You can provide these values to the helper script manually by using the `-gcp-project-number` and `-vpc-network-name` options.

**Note:** Adding bootstrap generation to the VM init script ensures that an up-to-date bootstrap file is created each time the VM reboots.

To verify the configuration, sign in to the client VM and run the following examples.

###  Java 

To verify the service with a gRPC Java client:

  1. Download the latest version of gRPC Java, with the most recent patch and build the `xds-hello-world` client application.
         
         sudo apt-get update -y
         sudo apt-get install -y openjdk-11-jdk-headless
         curl -L https://github.com/grpc/grpc-java/archive/v1.37.0.tar.gz | tar -xz
         cd grpc-java-1.37.0/examples/example-xds
         ../gradlew --no-daemon installDist
         

  2. Run the client with `world` as its name and `xds:///helloworld-gce` as the service URI.
         
         ./build/install/example-xds/bin/xds-hello-world-client "world" \
            xds:///helloworld-gce
         




###  Go 

To verify the service with a gRPC Go client:

  1. Download the latest version of gRPC Go, with the most recent patch, and build the `xds-hello-world` client application.
         
         sudo apt-get update -y
         sudo apt-get install -y golang git
         curl -L https://github.com/grpc/grpc-go/archive/v1.37.0.tar.gz | tar -xz
         cd grpc-go-1.37.0/examples/features/xds/client
         go get google.golang.org/grpc@v1.37.0
         go build .
         

  2. Run the client with `world` as its name and `xds:///helloworld-gce` as the service URI.
         
         ./client "world" xds:///helloworld-gce
         




###  C++ 

To verify the service with a gRPC C++ client:

  1. Download the latest version of gRPC C++, with the most recent patch, and build the `helloworld` client example.
         
         sudo apt-get update -y
         sudo apt-get install -y build-essential cmake git
         git clone --recurse-submodules -b v1.37.1 https://github.com/grpc/grpc
         cd grpc
         mkdir -p cmake/build
         pushd cmake/build
         cmake ../..
         make
         sudo make install
         popd
         mkdir -p third_party/abseil-cpp/cmake/build
         pushd third_party/abseil-cpp/cmake/build
         cmake ../..
         make
         sudo make install
         popd
         cd examples/cpp/helloworld
         mkdir -p cmake/build
         cd cmake/build/
         cmake ../..
         make
         

  2. Run the client with "xds:///helloworld-gce" as the service URI.
         
         ./greeter_client --target=xds:///helloworld-gce
         




###  grpcurl 

To verify the service using the `grpcurl` tool:

  1. Download and install the `grpcurl` tool.
         
         curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.8.1/grpcurl_1.8.1_linux_x86_64.tar.gz | tar -xz
         

  2. Run the `grpcurl` tool with "xds:///helloworld-gce" as the service URI and `helloworld.Greeter/SayHello` as the service name and method to invoke. The parameters to the `SayHello` method are passed using the `-d` option.
         
         ./grpcurl --plaintext \
           -d '{"name": "world"}' \
           xds:///helloworld-gce helloworld.Greeter/SayHello
         




###  Python 

To verify the service with a gRPC Python client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    sudo apt-get update
    sudo apt-get -y install python3-pip
    sudo pip3 install virtualenv
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1/examples/python/xds
    virtualenv venv -p python3
    source venv/bin/activate
    pip install -r requirements.txt
    python client.py  xds:///helloworld-gce
    

###  Ruby 

To verify the service with a gRPC Ruby client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    sudo apt-get update
    sudo apt-get install -y ruby-full
    sudo gem install grpc
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1/examples/ruby
    ruby greeter_client.rb john xds:///helloworld-gce
    

###  PHP 

To verify the service with a gRPC PHP client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    sudo apt-get update
    sudo apt-get install -y php7.3 php7.3-dev php-pear phpunit python-all zlib1g-dev git
    sudo pecl install grpc
    curl -sS https://getcomposer.org/installer | php
    sudo mv composer.phar /usr/local/bin/composer
    curl -L https://github.com/grpc/grpc/archive/v1.37.1.tar.gz | tar -xz
    cd grpc-1.37.1
    export CC=/usr/bin/gcc
    ./tools/bazel build @com_google_protobuf//:protoc
    ./tools/bazel build src/compiler:grpc_php_plugin
    cd examples/php
    composer install
    ./../../bazel-bin/external/com_google_protobuf/protoc --proto_path=../protos \
    --php_out=. --grpc_out=. \
    --plugin=protoc-gen-grpc=../../bazel-bin/src/compiler/grpc_php_plugin \
    ../protos/helloworld.proto
    php -d extension=grpc.so greeter_client.php john xds:///helloworld-gce
    

###  Node.js 

To verify the service with a gRPC Node.js client, run the following. Use the latest version of gRPC with the most recent patch.
    
    
    sudo apt-get update
    sudo apt-get install -y nodejs npm
    curl -L https://github.com/grpc/grpc/archive/v1.34.0.tar.gz | tar -xz
    cd grpc-1.34.0/examples/node/xds
    npm install
    node ./greeter_client.js --target=xds:///helloworld-gce
    

You should see output similar to this, where `INSTANCE_NAME` is the name of the VM instance:

`Greeting: Hello world, from INSTANCE_HOSTNAME`

This verifies that the proxyless gRPC client successfully connected to Cloud Service Mesh and learned about the backends for the `helloworld-gce` service using the `xds` name resolver. The client sent a request to one of the service's backends without needing to know about the IP address or performing DNS resolution.

## What's next

  * Learn about [advanced traffic management](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-traffic-management-legacy).
  * Learn how to [set up observability](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/observability-proxyless).
  * Learn how to [troubleshoot proxyless Cloud Service Mesh deployments](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
