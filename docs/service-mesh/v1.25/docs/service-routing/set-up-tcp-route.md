---
url: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-tcp-route/
title: Set up TCP services \u00a0|\u00a0 Cloud Service Mesh v1.25 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:39:18.732576+00:00
---

# Set up TCP services  |  Cloud Service Mesh v1.25  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/set-up-tcp-route/

You are viewing archived v1.25 Service Mesh documentation.

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
  * [ v1.25 ](https://docs.cloud.google.com/service-mesh/v1.25/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up TCP services

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.25/docs/overview).

This guide tells you how to set up Cloud Service Mesh to use TCP services and `TCPRoute` resources.

Cloud Service Mesh with TCP services and `TCPRoute` is similar to the Envoy sidecar proxy configuration with HTTP services. The exceptions are that the backend service provides a TCP service and routing is based on TCP/IP parameters rather than on the HTTP protocol.

[ ![Mesh resource with TCPRoute resource](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/mesh-tcp.svg)](https://docs.cloud.google.com/static/service-mesh/v1.25/docs/images/mesh-tcp.svg) `Mesh` resource with `TCPRoute` resource (click to enlarge)

## Before you begin

Make sure that you complete the tasks described in [Prepare to set up with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.25/docs/onboarding/prepare-service-routing-envoy-proxyless).

## Configure the `Mesh` resource

  1. In a file called `mesh.yaml`, create the `mesh` resource specification.
         
         name: sidecar-mesh
         

  2. Use the `mesh.yaml` file to create the `mesh` resource.
         
         gcloud network-services meshes import sidecar-mesh \
           --source=mesh.yaml \
           --location=global
         




## Configure the TCP server

This part of the guide is not specific to the new APIs and uses existing backend service, health check, and MIG resources.

For demonstration purposes, you create a backend service with autoscaled VMs using [managed instance groups](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) that serve a test TCP service on port `10000`.

  1. Create a Compute Engine VM instance template with a test service on port `10000`.
         
         gcloud compute instance-templates create tcp-td-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=allow-health-checks \
           --image-family=debian-10 \
           --image-project=debian-cloud \
           --metadata=startup-script="#! /bin/bash
         sudo apt-get update -y
         sudo apt-get install netcat -y
         while true;
           do echo 'Hello from TCP service' | nc -l -s 0.0.0.0 -p 10000;
         done &"
         

  2. Create a managed instance group based on the template.
         
         gcloud compute instance-groups managed create tcp-td-mig-us-east1 \
           --zone=ZONE \
           --size=1 \
           --template=tcp-td-vm-template
         

  3. Set the named ports on the created managed instance group to port 10000. 
         
         gcloud compute instance-groups set-named-ports tcp-td-mig-us-east1   
         
           --zone=ZONE   
         
           --named-ports=tcp:10000
         

  4. Create a health check.
         
         gcloud compute health-checks create tcp tcp-helloworld-health-check --port 10000
         

  5. Create a firewall rule to allow incoming health check connections to instances in your network.
         
         gcloud compute firewall-rules create tcp-vm-allow-health-checks \
            --network default \
            --action allow \
            --direction INGRESS \
            --source-ranges=35.191.0.0/16,130.211.0.0/22 \
            --target-tags allow-health-checks \
            --rules tcp:10000
         

  6. Create a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and attach the health check to the backend service. The example uses the managed instance group that runs the sample TCP service that you created earlier.
         
         gcloud compute backend-services create tcp-helloworld-service \
             --global \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --protocol=TCP \
             --health-checks tcp-helloworld-health-check
         

  7. Add the managed instance group to the backend service.
         
         gcloud compute backend-services add-backend tcp-helloworld-service \
           --instance-group tcp-td-mig-us-east1 \
           --instance-group-zone=ZONE \
           --global
         




## Set up routing with `TCPRoute`

In this section, you set up routing.

  1. In a file called `tcp_route.yaml`, create the `TcpRoute` specification.

You can use either `$PROJECT_ID` or `$PROJECT_NUMBER`.
         
         name: helloworld-tcp-route
         meshes:
         - projects/$PROJECT_NUMBER/locations/global/meshes/sidecar-mesh
         rules:
         - action:
             destinations:
             - serviceName: projects/$PROJECT_NUMBER/locations/global/backendServices/tcp-helloworld-service
           matches:
           - address: '10.0.0.1/32'
             port: '10000'
         

  2. Using the `tcp_route.yaml` specification, create the `TcpRoute` resource.
         
         gcloud network-services tcp-routes import helloworld-tcp-route \
           --source=tcp-route.yaml \
           --location=global
         




## Create a TCP client with an Envoy sidecar

  1. Create an instance template and then create a VM with Envoy that is connected to Cloud Service Mesh.
         
         gcloud beta compute instance-templates create td-vm-client-template \
           --image-family=debian-10 \
           --image-project=debian-cloud \
           --service-proxy=enabled,mesh=sidecar-mesh \
           --metadata=startup-script="#! /bin/bash
         sudo apt-get update -y
         sudo apt-get install netcat -y"
         
         
         gcloud compute instances create td-vm-client \
           --zone=ZONE \
           --source-instance-template td-vm-client-template
         

  2. Sign in to the VM that you created.
         
         gcloud compute ssh td-vm-client
         

  3. Verify connectivity to the test services that you created using the `netcat` utility.
         
         echo 'Hi TCP Service' | nc 10.0.0.1 10000
         




The test service should return the phrase **Hello from TCP service**. You should also be able to see any text that you type returned by the `netcat` service running on the remote VM.

## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.25/docs/service-routing/list-route-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
