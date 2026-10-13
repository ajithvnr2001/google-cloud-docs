---
url: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/set-up-proxyless-mesh/
title: Set up proxyless gRPC services \u00a0|\u00a0 Cloud Service Mesh v1.22 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:46.807976+00:00
---

# Set up proxyless gRPC services  |  Cloud Service Mesh v1.22  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/set-up-proxyless-mesh/

You are viewing archived v1.22 Service Mesh documentation.

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
  * [ v1.22 ](https://docs.cloud.google.com/service-mesh/v1.22/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.22/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up proxyless gRPC services

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This guide demonstrates how to set up a proxyless gRPC service mesh with `Mesh` and `GRPCRoute` resources.

[ ![Proxyless gRPC services with GRPCRoute and Mesh resources](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/mesh-grpcroute.svg)](https://docs.cloud.google.com/static/service-mesh/v1.22/docs/images/mesh-grpcroute.svg) Proxyless gRPC services with `GRPCRoute` and `Mesh` resources (click to enlarge)

## Before you begin

Make sure that you read [Prepare to set up with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.22/docs/onboarding/prepare-service-routing-envoy-proxyless) and complete the prerequisites described in that document.

## Configure the `Mesh` resource

When a proxyless gRPC application connects to an `xds://hostname`, the gRPC client library establishes a connection to Cloud Service Mesh. The client library uses the connection to obtain the routing configuration that is needed to route requests for the hostname.

Make sure that you note the name of the `Mesh` resource, which is the key that the proxyless gRPC application uses to request the configuration associated with this Mesh.

  1. Create the `Mesh` specification and save it in a file called mesh.yaml.
         
         name: grpc-mesh
         

  2. Create the `Mesh` resource using the `mesh.yaml` specification:
         
         gcloud network-services meshes import grpc-mesh \
           --source=mesh.yaml \
           --location=global
         




After the `Mesh` resource is created, Cloud Service Mesh is ready to serve the configuration, but because there are no services defined yet, the configuration is empty. In the next section, you define the services and attach them to the `Mesh` resource.

## Configure the gRPC server

For demonstration purposes, you create a backend service with autoscaled VMs in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups). The VMs serve the phrase `hello world` using the gRPC protocol on port `50051`.

  1. Create the Compute Engine VM instance template with a `helloworld` gRPC service that is exposed on port `50051`:
         
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
          curl -L https://github.com/grpc/grpc-java/archive/v1.38.0.tar.gz | tar -xz
          cd grpc-java-1.38.0/examples/example-hostname
          ../gradlew --no-daemon installDist
          sudo systemd-run ./build/install/hostname-server/bin/hostname-server')
          

  2. Create a managed instance group based on the template:
         
         gcloud compute instance-groups managed create grpc-td-mig-us-east1 \
           --zone=ZONE \
           --size=2 \
           --template=grpc-td-vm-template
         

  3. Create the named port for the gRPC service. The named port is the port on which the gRPC service listens for requests. In the following example, the named port is `50051`:
         
         gcloud compute instance-groups set-named-ports grpc-td-mig-us-east1 \
          --named-ports=grpc-helloworld-port:50051 \
          --zone=ZONE
         

  4. Create a gRPC health check. The services must implement the [gRPC health checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md) so that gRPC health checks work properly. For more information, see [health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks).
         
         gcloud compute health-checks create grpc grpc-helloworld-health-check \
           --use-serving-port
         

  5. Create a firewall rule to allow health check connections to instances in your network:
         
         gcloud compute firewall-rules create grpc-vm-allow-health-checks \
           --network=default \
           --action=ALLOW \
           --direction=INGRESS \
           --source-ranges=35.191.0.0/16,130.211.0.0/22 \
           --target-tags allow-health-checks \
           --rules=tcp:50051
         

  6. Create a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and add the health check to the backend service. The port specified here is used to connect to the VMs in the managed instance group.
         
         gcloud compute backend-services create grpc-helloworld-service \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --protocol=GRPC \
           --port-name=grpc-helloworld-port \
           --health-checks grpc-helloworld-health-check
         

  7. Add the managed instance group to the backend service.
         
         gcloud compute backend-services add-backend \
           grpc-helloworld-service \
           --instance-group=grpc-td-mig-us-east1 \
           --instance-group-zone=ZONE \
           --global
         




The `Mesh` resource and services are configured. In the next section, you set up routing.

## Set up routing with `GRPCRoute`

Use the following instructions to set up routing.

  1. Create the `GRPCRoute` specification and save it in a file called `grpc_route.yaml`.

You can use either `PROJECT_ID` or `PROJECT_NUMBER`.
         
         name: helloworld-grpc-route
         hostnames:
         - helloworld-gce
         meshes:
         - projects/PROJECT_NUMBER/locations/global/meshes/grpc-mesh
         rules:
         - action:
             destinations:
             - serviceName: projects/PROJECT_NUMBER/locations/global/backendServices/grpc-helloworld-service
         

  2. Create the `GrpcRoute` resource using the `grpc_route.yaml` specification:
         
         gcloud network-services grpc-routes import helloworld-grpc-route \
           --source=grpc_route.yaml \
           --location=global
         




Cloud Service Mesh is now configured to load balance traffic for the services specified in the `GRPCRoute` resource across backends in the managed instance group.

## Create a gRPC client

You can verify the configuration by instantiating a proxyless gRPC application and connecting it to Cloud Service Mesh. In its bootstrap file, the application must specify the VPC network indicated in the Mesh.

After it is configured, the application can send a request to the instances or endpoints associated with `helloworld-gce` using the `xds:///helloworld-gce` service URI.

In the following examples, you use the grpcurl tool to test the gRPC service.

  1. Create a client VM.
         
         gcloud compute instances create grpc-client \
           --zone=ZONE\
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --image-family=debian-10 \
           --image-project=debian-cloud \
           --metadata-from-file=startup-script=<(echo '#! /bin/bash
         set -e
         export GRPC_XDS_BOOTSTRAP=/run/td-grpc-bootstrap.json
         echo export GRPC_XDS_BOOTSTRAP=$GRPC_XDS_BOOTSTRAP | sudo tee /etc/profile.d/grpc-xds-bootstrap.sh
         curl -L https://storage.googleapis.com/traffic-director/td-grpc-bootstrap-0.19.0.tar.gz | tar -xz
         ./td-grpc-bootstrap-0.19.0/td-grpc-bootstrap --config-mesh-experimental grpc-mesh | tee $GRPC_XDS_BOOTSTRAP')
         




## Set up the bootstrap file

The client application must have a bootstrap configuration file. The startup script in the previous section sets the `GRPC_XDS_BOOTSTRAP` environment variable and uses a helper script to generate the bootstrap file. The values for `TRAFFICDIRECTOR_GCP_PROJECT_NUMBER` and zone in the generated bootstrap file are obtained from the metadata server that knows these details about your VM instances. You can provide these values to the helper script manually using the `--gcp-project-number` option. You must provide a mesh name matching the `Mesh` resource using the `--config-mesh-experimental` option.

**Note:** Per policy, we encourage users to check for updates of the TD gRPC bootstrap generator yearly.

To verify the configuration, sign in to the client VM and run the following.

  1. SSH to the client VM.
         
         gcloud compute ssh grpc-client
         

  2. Download and install the `grpcurl` tool.
         
         curl -L https://github.com/fullstorydev/grpcurl/releases/download/v1.8.1/grpcurl_1.8.1_linux_x86_64.tar.gz | tar -xz
         

  3. Run the `grpcurl` tool with `xds:///helloworld-gce` as the service URI and `helloworld.Greeter/SayHello` as the service name and method to invoke. The parameters to the `SayHello` method are passed using the `-d` option.
         
         ./grpcurl --plaintext \
           -d '{"name": "world"}' \
           xds:///helloworld-gce helloworld.Greeter/SayHello
         




You should see output similar to the following, where `INSTANCE_HOSTNAME` is the name of the VM instance:
    
    
       Greeting: Hello world, from INSTANCE_HOSTNAME
       

The output verifies that the proxyless gRPC client successfully connected to Cloud Service Mesh and learned about the backends for the `helloworld-gce` service using the `xds` name resolver. The client sent a request to one of the service's backends without needing to know about the IP address or performing DNS resolution.

## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.22/docs/service-routing/list-route-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
