---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/configure-dual-stack-ipv6/
title: Configure IPv6 dual-stack for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:09.180844+00:00
---

# Configure IPv6 dual-stack for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/configure-dual-stack-ipv6/

You are viewing v1.27 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure IPv6 dual-stack for Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

This page shows you how to load balance IPv6 traffic on Cloud Service Mesh using Traffic Director (TD) proxy-based load balancers as well as how to migrate from IPv4-based deployments to dual-stack (IPv4 and IPv6) deployments and how to migrate from dual-stack to IPv4.

On dual-stack deployments you have the option to indicate whether IPv4 or IPv6 is sent to the service backend. The proxy or gRPC client tests each datapath in your order of preference and selects the one that aligns with your preference and what is supported.

Dual-stack features are supported in gRPC 1.66.1 and later for C++ and Python, 1.12 and later for Node, and 1.71 and later for Go. Java is not supported at this time.

Versions of gRPC without dual-stack support (i.e., Go and versions prior to 1.66 in other languages) will use only the first address of each endpoint, in the order sent by TD.

## Before you begin

This guide assumes you have already:

  * [Set up the service routing APIs with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/provision-control-plane).
  * Completed the steps in the [Continue the setup process](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/prepare-service-routing-envoy-proxyless#continue-setup) section of the onboarding guide.



## Set up the IPv6 backend service

In this section you configure the following:

  * Two backend groups (either instance groups, managed instance groups, or network endpoint groups), one in each of two different zones within the same region.
  * Two VM instances in each backend group.
  * A health check for verifying instance health.
  * Firewall rules allowing health checks to reach backends.
  * A backend service.
  * The backend service to include the two backend groups configured.



### Set up a subnet for your backends

The following command allocates internal address ranges for both IPv4 and IPv6 and allows VMs on the subnet to be allocated with either address type.

Note that [only custom mode subnets](https://docs.cloud.google.com/vpc/docs/vpc) are supported. There is no auto-mode support. You can switch to custom mode for the entire VPC network and then populate the IPv6 Backends (MIGs or NEGs).

  1. Create a dual-stack network:
         
         gcloud compute networks create NETWORK \
             --subnet-mode=custom \
             --enable-ula-internal-ipv6
         

  2. Create a dual-stack Subnet for Backend VMs:
         
         gcloud compute networks subnets create SUBNET \
             --network=NETWORK \
             --range=PRIMARY_IPv4_RANGE \
             --stack-type=IPV4_IPV6 \
             --ipv6-access-type=IPv6_ACCESS_TYPE \
             --region=REGION
         

Replace the following:

     * SUBNET: a name for the new subnet.
     * NETWORK: the name of the VPC network that will contain the new subnet.
     * PRIMARY_IPv4_RANGE: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * IPv6_ACCESS_TYPE: the IPv6 access type. It can be `EXTERNAL` or `INTERNAL`.
     * REGION: the Google Cloud region in which the new subnet will be created.



### Set up backends

You can choose either to use [Managed Instance Groups (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), [Unmanaged Instance Groups](https://docs.cloud.google.com/compute/docs/instance-groups#unmanaged_instance_groups), or [Network Endpoint Groups (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs).

### MIG

  1. Create a Managed Instance Group with `dual-stack-gateway-template`:
         
         gcloud alpha compute instance-templates create dual-stack-gateway-template \
         --region=REGION \
         --image-family=debian-12 \
         --image-project=debian-cloud \
         --tags=dual-stack-http-server \
         --network=NETWORK \
         --subnet=SUBNET \
         --stack-type=IPV4_IPV6 \
         --service-proxy=enabled,scope=gateway-proxy
         

  2. Create a gateway proxy managed instance group:
         
         gcloud compute instance-groups managed create dual-stack-ZONE-gateway-mig \
         --zone=ZONE \
         --size=1 \
         --template=dual-stack-gateway-template
         

  3. Create a backend managed instance group:
         
         gcloud compute instance-templates create dual-stack-backend-template \
           --region=REGION \
           --image-family=debian-12 \
           --image-project=debian-cloud \
           --tags=dual-stack-http-server \
           --network=NETWORK \
           --subnet=SUBNET \
           --stack-type=IPV4_IPV6 \
           --metadata=startup-script="#! /bin/bash
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         sudo service apache2 restart
         echo '<!doctype <html><body><h1>'\`dual-stack-server\`'</h1></body></html>' | sudo tee /var/www/html/index.html"
         
         
         gcloud compute instance-groups managed create dual-stack-ZONE-backend-mig \
         --zone=ZONE \
         --size=1 \
         --template=dual-stack-backend-template
         

  4. Add a named port to the Managed Instance Group:
         
         gcloud compute instance-groups set-named-ports us-ig-1 \
           --named-ports http:80 \
           --zone ZONE \
         
         gcloud compute instance-groups set-named-ports us-ig-2 \
           --named-ports http:80 \
           --zone ZONE
         

We use separate [health checks](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs) for load balancing and for autohealing. Health checks for load balancing are typically configured to be more aggressive because these health checks determine whether a VM receives user traffic and if you want to quickly redirect traffic if necessary.

Health checking for autohealing causes Compute Engine to proactively replace failing VMs, so this health check should be more conservative than a load balancing health check. Note that Autohealing for dual-stack VMs will be based on IPv4 Health-checks.

  5. Create a health check:
         
         gcloud compute health-checks create http dualstack-health-check-http \
         

  6. Ensure that firewall rules allow health checks:

### IPv4
         
         gcloud compute firewall-rules create dual-stack-allow-ipv4-health-check \
         --network=NETWORK \
         --action=ALLOW \
         --direction=INGRESS \
         --source-ranges=35.191.0.0/16,130.211.0.0/22 \
         --target-tags=dual-stack-http-server \
         --rules=tcp:22,80
         

### IPv6
         
         gcloud compute firewall-rules create dual-stack-allow-ipv6-health-check \
         --network=NETWORK \
         --action=ALLOW \
         --direction=INGRESS \
         --source-ranges=::/0 \
         --target-tags=dual-stack-http-server \
         --rules=tcp:22,80
         

  7. Apply the health check by configuring an autohealing policy for your MIG:
         
         gcloud compute instance-groups managed update us-mig-1 \
           --health-check dualstack-health-check-http \
           --initial-delay 300 \
           --zone us-central1-a
         




The initial-delay setting delays autohealing from potentially prematurely recreating the VM if the VM is in the process of starting up. The initial delay timer starts when the VM's `currentAction` field changes to `VERIFYING`.

### Unmanged Instance Groups

  1. Configure Instance Groups:
         
         gcloud compute instance-groups unmanaged create us-ig-1 \
         --zone us-central1-a \
         
         gcloud compute instance-groups unmanaged create us-ig-2 \
         --zone us-central1-b
         

  2. Create two Dual Stack VM instances in each instance-group:
         
         gcloud compute instances create inst-us-central1-1 \
         --image-family debian-12 \
         --image-project debian-cloud \
         --tags network-lb \
         --zone us-central1-a \
         --network-interface [--network=NETWORK | --subnet=SUBNET] \
         --stack-type=IPV4_IPV6 \
         
         gcloud compute instances create inst-us-central1-2 \
         --image-family debian-12 \
         --image-project debian-cloud \
         --tags network-lb \
         --zone us-central1-a \
         --network-interface [--network=NETWORK | --subnet=SUBNET] \
         --stack-type=IPV4_IPV6 \
         
         gcloud compute instances create inst-us-central1-3 \
         --image-family debian-12 \
         --image-project debian-cloud \
         --tags network-lb \
         --zone us-central1-b \
         --network-interface [--network=NETWORK | --subnet=SUBNET] \
         --stack-type=IPV4_IPV6 \
         
         gcloud compute instances create inst-us-central1-4 \
         --image-family debian-12 \
         --image-project debian-cloud \
         --tags network-lb \
         --zone us-central1-b \
         --network-interface [--network=NETWORK | --subnet=SUBNET] \
         --stack-type=IPV4_IPV6
         

The IPv6 address will be auto-assigned.

  3. Add VMs to instance groups:
         
         gcloud compute instance-groups unmanaged add-instances us-ig-1 \
         --instances inst-us-central1-1,inst-us-central1-2 \
         --zone us-central1-a \
         
         gcloud compute instance-groups unmanaged add-instances us-ig-2 \
         --instances inst-us-central1-3,inst-us-central1-4 \
         --zone us-central1-b
         




### NEG

  1. Add a backend where `--network-endpoint-type` is GCE_VM_IP_PORT:
         
         gcloud compute network-endpoint-groups create us-neg-lb-1 \
           --network=NETWORK SUBNET \
           --zone=us-central1-a --network-endpoint-type=GCE_VM_IP_PORT \
         
         gcloud compute network-endpoint-groups create us-neg-lb-2 \
           --network=NETWORK SUBNET \
           --zone=us-central1-b  --network-endpoint-type=GCE_VM_IP_PORT
         

  2. Add endpoints to Network Endpoint Group:
         
         gcloud compute network-endpoint-groups update us-neg-lb-1 \--zone=us-central1-a \
         --add-endpoint 'instance=inst-us-central1-1,ip=IPV4_ADRS_1, ipv6=IPV6_ADRS_1,port=80' \
         --add-endpoint 'instance=inst-us-central1-2,ip=IPV4_ADRS_2, ipv6=IPV6_ADRS_2,port=80' \
         
         gcloud compute network-endpoint-groups update us-neg-lb-2 --zone=us-central1-b \
         --add-endpoint 'instance=inst-us-central1-3,ip=IPV4_ADRS_3, ipv6=IPV6_ADRS_3,port=80' \
         --add-endpoint 'instance=inst-us-central1-4,ip=IPV4_ADRS_4,ipv6=IPV6_ADRS_4,port=80'
         




### Configure Health Checking

  1. Create a Health-Check for the backend service:
         
         gcloud compute health-checks create http[s] my-health-check   
         
             --global   
         
             --request-path '/'   
         
             --port SERVICE_PORT
           

Replace SERVICE_PORT with the port number, from 1 to 65535.

  2. Create a firewall rule to allow health checks:
         
         gcloud compute firewall-rules create allow-scan-probe \
             --action allow \
             --description "allow-scan-probe" \
             --rules tcp:SERVICE_PORT \
             --source-ranges 2600:2d00:1:b029::/64 \
             --priority 10 \
             --network=NETWORK
         




The range 2600:2d00:1:b029::/64 is used for the source IP addresses of the Health-checkers to probe the VMs' health. Note that 2600:2d00:1:b029::/64 is used as the Source IP address for IPv6 Health-checkers to probe backend VM health of Network Load Balancing.

### Create and update backend service with Backends

  1. Create the backend service:
         
         gcloud compute backend-services create my-backend-service \
         --ip-address-selection-policy PREFER_IPV6  \
         --global \
         --health-checks my-health-check \
         --load-balancing-scheme=INTERNAL_SELF_MANAGED \
         --timeout=5m
         

  2. Add the backends to the backend service:
         
         gcloud compute backend-services add-backend my-backend-service \
         --instance-group us-ig-1 \
         --instance-group-zone us-central1-a \
         --global \
         
         gcloud compute backend-services add-backend my-backend-service \
         --instance-group us-ig-2 \
         --instance-group-zone us-central1-b \
         --global
         




## Set up a Cloud Service Mesh service

This section shows how to configure an IPv6 service in the Traffic Director. The service may be part of a Service Mesh configuration, or it may be used to configure a Service Gateway such as a VM running Envoy.

Now that the backend services with `PREFER_IPV6` are configured, you can create an appnet gateway resource.

### Create a gateway resource

  1. In a file called `dual-stack-gateway.yaml`, create the Gateway specification for HTTP traffic:
         
         cat <<EOF | tee dual-stack-gateway.yaml
         name: dual-stack-gateway
         scope: gateway-proxy
         ipVersion: IPV6
         ports:
         - 80
         type: OPEN_MESH
         EOF
         

  2. Create the Gateway resource from the `dual-stack-gateway.yaml` specification:
         
         gcloud network-services gateways import dual-stack-gateway \
           --source=dual-stack-gateway.yaml \
           --location=global
         




### Set up routing with HTTPRoute

  1. In a file called `dual-stack-http_route.yaml`, create the HTTPRoute specification:
         
         cat <<EOF | tee dual-stack-http-route.yaml
         name: dual-stack-http-route
         hostnames:
         - dual-stack-server
         gateways:
         - projects/PROJECT_ID/locations/global/gateways/dual-stack-gateway
         rules:
         - action:
             destinations:
             - serviceName: "projects/PROJECT_ID/locations/global/backendServices/dual-stack-backend-service"
         EOF
         

  2. Use the specification in `dual-stack-http-route.yaml` to create the HTTPRoute resource.
         
         gcloud network-services http-routes import dual-stack-http-route \
           --source=dual-stack-http-route.yaml \
           --location=global
         

  3. To verify end-to-end connectivity, SSH to the VM from gateway MIG and run the following command:
         
         curl -H 'Host: dual-stack-server' http://[::]
         

The output is similar to:
         
         <!doctype <html><body><h1>'`dual-stack-server`'</h1></body></html>
         




## Migrate from IPv4 to dual-stack

You must meet the following prerequisites before you can migrate from IPv4 to dual-stack:

  * Existing single stack VM instance groups `us-ig-1` and `us-ig-2` with `IPV4_ONLY` stack with existing VMs
  * A single IPv4 backend service `my-ipv4-backend-service` pointing at `us-ig-1` and `us-ig-2`
  * An `IPV4_ONLY` VM Subnet
  * A gateway resource configured with an IPv4 version address



### Upgrade the subnet to dual-stack

Update the existing subnet for the backend to support IPv6:
    
    
    gcloud compute networks subnets update SUBNET \
      --stack-type IPV4_IPV6 \
      --ipv6-access-type=IPv6_ACCESS_TYPE \
    

Replace the following:

  * SUBNET: a name for the new subnet.
  * IPv6_ACCESS_TYPE: the IPv6 access type. It can be `EXTERNAL` or `INTERNAL`.



### Upgrade each VM to dual-stack
    
    
    gcloud compute instances network-interfaces update EXISTING_VM_NAME \
      --stack-type=IPV4_IPV6 \
      --zone=us-central1
    

Replace EXISTING_VM_NAME with the name of your existing VM.

### Add new dual-stack VMs to each instance group

  1. Create new VM instances:
         
         gcloud compute instances create my-new-vm-1 \
           --image-family debian-12 \
           --tags network-lb \
           --zone us-central1-a \
           --network-interface [--network=NETWORK | --subnet=SUBNET] \
           --stack-type=IPV4_IPV6 \
         
         gcloud compute instances create my-new-vm-2 \
           --image-family debian-12 \
           --tags network-lb \
           --zone us-central1-b \
           --network-interface [--network=NETWORK | --subnet=SUBNET] \
           --stack-type=IPV4_IPV6
         

  2. Add the new instances to instance groups:
         
         gcloud compute instance-groups unmanaged add-instances us-ig-1 \
           --instances my-new-vm-1 \
           --zone us-central1-a \
         
         gcloud compute instance-groups unmanaged add-instances us-ig-2 \
           --instances my-new-vm-2 \
           --zone us-central1-b
         

  3. Create an IPv6 backend service:
         
         gcloud compute backend-services create dual-stack-backend-service \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --protocol=HTTP \
           --health-checks=dual-stack-health-check-http \
           --ip-address-selection-policy=PREFER_IPV6
         

  4. Add the updated Instance-Group to the newly created Dual Stack backend service:
         
         gcloud compute backend-services add-backend dual-stack-backend-service \
           --instance-group=us-ig-1 \
           --instance-group-zone=ZONE \
           --global
         
         
         gcloud compute backend-services add-backend dual-stack-backend-service \
           --instance-group=us-ig-2 \
           --instance-group-zone=ZONE \
           --global
         




## Migrate from dual-stack to IPv4

You must meet the following prerequisites before you can migrate from dual-stack to IPv4:

  * Existing dual-stack VM instance groups `us-ig-1` and `us-ig-2` with `IPV4_IPV6` stack with existing VMs
  * A single IPv6 backend service `my-ipv6-backend-service` pointing at `us-ig-1` and `us-ig-2`
  * An IPV4_IPV6 VM Subnet
  * A gateway resource



### Downgrade each VM to IPv4
    
    
    gcloud compute instances network-interfaces update EXISTING_VM_NAME \
      --stack-type=IPV4_ONLY \
      --zone=us-central1
    

### Add new IPv4-stack VMs to each instance group

  1. Create new VM instances:
         
         gcloud compute instances create my-new-vm-1 \
           --image-family debian-12 \
           --tags network-lb \
           --zone us-central1-a \
           --network-interface [--network=NETWORK | --subnet=SUBNET] \
           --stack-type=IPV4_ONLY \
         
         gcloud compute instances create my-new-vm-2 \
           --image-family debian-12 \
           --tags network-lb \
           --zone us-central1-b \
           --network-interface [--network=NETWORK | --subnet=SUBNET] \
           --stack-type=IPV4_ONLY
         

  2. Add the new instances to instance groups:
         
         gcloud compute instance-groups unmanaged add-instances us-ig-1 \
           --instances my-new-vm-1 \
           --zone us-central1-a \
         
         gcloud compute instance-groups unmanaged add-instances us-ig-2 \
           --instances my-new-vm-2 \
           --zone us-central1-b
         

  3. Create an IPv4 backend service:
         
         gcloud compute backend-services create my-ipv4-backend-service \
           –ip-address-selection-policy IPV4_ONLY \
           --global \
           --health-checks my-health-check \
           --load-balancing-scheme INTERNAL_SELF_MANAGED \
           --timeout=5m
         

  4. Add the updated Instance-Groups to the newly created IPv4 backend service:
         
         gcloud compute backend-services add-backend my-ipv4-backend-service \
           --instance-group us-ig1 \
           --instance-group-zone us-central1-a \
           --global \
         
         gcloud compute backend-services add-backend my-ipv4-backend-service \
           --instance-group us-ig2 \
           --instance-group-zone us-central1-b \
           --global
         

Now both IPv4 and IPv6 backend services can serve traffic. Update the URL map to direct some fraction of client traffic to the new IPv4 backend service.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
