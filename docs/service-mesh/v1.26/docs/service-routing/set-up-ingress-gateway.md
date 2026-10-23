---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/set-up-ingress-gateway/
title: Set up an ingress gateway \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:53:23.786865+00:00
---

# Set up an ingress gateway  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/set-up-ingress-gateway/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up an ingress gateway

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview).

This guide demonstrates how to configure Cloud Service Mesh to configure proxies as _ingress gateways_. You set up an Envoy proxy as the gateway and a hello-world in-mesh service.

In this configuration, a regional external passthrough Network Load Balancer directs traffic from the internet to your service mesh through an ingress gateway. A `Gateway` resource manages an Envoy proxy that acts as a _gateway_ into the service mesh. A gateway is also known as a middle proxy or ingress. The Envoy proxies deployed to act as ingress gateways are standalone proxies rather than sidecars to workloads. In this mode, Envoy listens on a defined list of ports, and forwards traffic according to routing rules that you configure in Cloud Service Mesh. A `Gateway` API resource is used to configure such Envoy proxies.

[ ![Envoy proxy as ingress gateway, with regional external passthrough Network Load Balancer, and Gateway resource](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/gateway-httproute-ingress.svg)](https://docs.cloud.google.com/static/service-mesh/v1.26/docs/images/gateway-httproute-ingress.svg) Envoy proxy as ingress gateway, with regional external passthrough Network Load Balancer, and `Gateway` resource (click to enlarge)

Set up routing to ensure that traffic destined for the `Gateway` proxies is directed to the VMs hosting the Envoys. The ingress service can be paired with an external Application Load Balancer or an internal passthrough Network Load Balancer, but such configurations are not included in this demonstration setup. For information about setting up an external Application Load Balancer, see the [External Application Load Balancer documentation](https://docs.cloud.google.com/load-balancing/docs/https). For information about setting up an internal passthrough Network Load Balancer, see the [Internal passthrough Network Load Balancer documentation](https://docs.cloud.google.com/load-balancing/docs/internal).

This guide does not cover the service-to-service communication and the `Mesh` resource behind the `Gateway`.

## Before you begin

Make sure that you complete the tasks described in [Prepare to set up with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.26/docs/onboarding/prepare-service-routing-envoy-proxyless).

## Configure firewall rules

In this section, you configure two firewall rules. One rule allows health check probes to access instances in the Virtual Private Cloud network. The other rule allows traffic from any source into the network.

  1. Configure firewall rules to allow health checks.
         
         gcloud compute firewall-rules create allow-health-checks \
           --network=NETWORK_NAME \
           --direction=INGRESS \
           --action=ALLOW \
           --rules=tcp \
           --source-ranges="35.191.0.0/16,130.211.0.0/22,209.85.152.0/22,209.85.204.0/22"
         

  2. Configure firewall rules to allow traffic from any source on the internet to reach the gateway proxies. You can optionally edit the command for your source IP address range.
         
         gcloud compute firewall-rules create allow-gateway-ingress-traffic \
           --network=NETWORK_NAME \
           --direction=INGRESS \
           --action=ALLOW \
           --rules=tcp:80 \
           --source-ranges="0.0.0.0/0" \
           --target-tags=gateway-proxy
         




## Configure Identity and Access Management permissions

In this section, you designate the service account for the gateway proxies and assign them the correct IAM roles.

  1. Create a service account identity for the gateway proxies.
         
         gcloud iam service-accounts create gateway-proxy
         

  2. Assign the required IAM roles to the service account identity.
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/trafficdirector.client"
         
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         




## Configure the `Gateway` resource

In this section, you configure the gateway resource.

  1. In a file called `gateway80.yaml`, create the `Gateway` specification for HTTP traffic.
         
         cat <<EOF | tee gateway80.yaml
         name: gateway80
         scope: gateway-proxy
         ports:
         - 80
         type: OPEN_MESH
         EOF
         

  2. Create the `Gateway` resource from the `gateway80.yaml` specification:
         
         gcloud network-services gateways import gateway80 \
           --source=gateway80.yaml \
           --location=global
         




## Create a managed instance group with Envoy proxies

In this section, you create the Envoy proxies that are associated with the ingress gateway configuration.

  1. Create an instance template for a VM running an automatically deployed Envoy service proxy. The Envoys have a `scope` of `gateway-proxy`. Don't pass the serving port as a parameter of `--service-proxy`.
         
         gcloud beta compute instance-templates create gateway-proxy \
           --machine-type=n1-standard-1 \
           --boot-disk-size=10GB \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=gateway-proxy \
           --network=NETWORK_NAME \
           --service-account="gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --service-proxy=enabled,scope=gateway-proxy
         

  2. Create a regional managed instance group from the instance template.
         
         gcloud compute instance-groups managed create gateway-proxies-REGION \
           --region=REGION \
           --size=3 \
           --template=gateway-proxy \
           --target-distribution-shape=EVEN
         

  3. Set a named port to enable TCP health checking for the regional external passthrough Network Load Balancer.
         
         gcloud compute instance-groups managed set-named-ports gateway-proxies-REGION \
           --region=REGION \
           --named-ports=serving-port:80
         




## Set up the regional external passthrough Network Load Balancer

In this section, you create the regional external passthrough Network Load Balancer, a backend service forwarding rule, and required health check, to forward traffic from the internet to the gateway proxies.

  1. Create an external IP address for the regional external passthrough Network Load Balancer.
         
         gcloud compute addresses create xnlb-REGION \
           --region=REGION
         

  2. Get the IP address that was created for the regional external passthrough Network Load Balancer.
         
         gcloud compute addresses describe xnlb-REGION \
           --region=REGION --format='value(address)'
         

This IP address is used as the variable `IP_ADDRESS` in later sections of this setup guide.

  3. Create a health check for the gateway proxies.
         
         gcloud compute health-checks create tcp xnlb-REGION \
           --region=REGION \
           --port-name=serving-port
         

  4. Create a backend service for the gateway proxies.
         
         gcloud compute backend-services create xnlb-REGION \
           --health-checks=xnlb-REGION \
           --health-checks-region=REGION \
           --load-balancing-scheme=EXTERNAL \
           --protocol=TCP \
           --region=REGION \
           --port-name=serving-port
         

  5. Add the managed instance group as the backend to the backend service.
         
         gcloud compute backend-services add-backend xnlb-REGION \
           --instance-group=gateway-proxies-REGION \
           --instance-group-region=REGION \
           --region=REGION
         

  6. Create a forwarding rule pointing to the gateway proxies.
         
         gcloud compute forwarding-rules create xnlb-REGION \
           --region=REGION \
           --load-balancing-scheme=EXTERNAL \
           --address=IP_ADDRESS \
           --ip-protocol=TCP \
           --ports=80 \
           --backend-service=xnlb-REGION \
           --backend-service-region=REGION
         




## Configure the HTTP server

In this section, you create a hello-world HTTP test service running in the service mesh that gateway proxies are routing into.

  1. Create an instance template running an Apache web server, serving the instance's hostname as it responds to HTTP requests.
         
         gcloud compute instance-templates create helloworld-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=private-instance \
           --image-family=debian-11 \
           --image-project=debian-cloud \
           --network=NETWORK_NAME \
           --metadata=startup-script="#! /bin/bash
         
         sudo apt-get update -y
         sudo apt-get install apache2 -y
         echo \"Hello from \`/bin/hostname\`\" | sudo tee /var/www/html/index.html
         sudo service apache2 restart"
         

  2. Create a managed instance group based on the template.
         
         gcloud compute instance-groups managed create helloworld-mig-REGION \
           --zone=ZONE \
           --size=1 \
           --template=helloworld-template
         

  3. Create an HTTP health check.
         
         gcloud compute health-checks create http helloworld-health-check
         

  4. Create a firewall rule to allow incoming connections from gateway proxies and health checks to instances in your network.
         
         gcloud compute firewall-rules create allow-rfc1918-traffic \
            --network=NETWORK_NAME \
            --action=allow \
            --direction=INGRESS \
            --source-ranges=10.0.0.0/8,172.16.0.0/12,192.168.0.0/16 \
            --target-tags=private-instance \
            --rules=tcp:80
         

  5. Create a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and attach the health check.
         
         gcloud compute backend-services create http-helloworld-service \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --protocol=HTTP \
           --health-checks=helloworld-health-check \
           --global
         

  6. Add the managed instance group to the backend service.
         
         gcloud compute backend-services add-backend http-helloworld-service \
           --instance-group helloworld-mig-REGION \
           --instance-group-zone=ZONE \
           --global
         




## Set up routing with `HTTPRoute`

You now have a Cloud Service Mesh `Gateway` resource and a service configured. Next, you connect them by using an `HTTPRoute` resource that associates a hostname with a backend service. The `HTTPRoute` also references the `Gateway`.

  1. In a file called `http_route.yaml`, create the `HTTPRoute` specification. The specification references `gateway80`, which is the `Gateway` resource that you created earlier, and it points to the backend service `http-helloworld-service`.

You can use either `PROJECT_ID` or `PROJECT_NUMBER`.
         
         cat <<EOF | tee http_route.yaml
         name: helloworld-http-route
         hostnames:
         - helloworld-gce
         gateways:
         - projects/PROJECT_NUMBER/locations/global/gateways/gateway80
         rules:
         - action:
             destinations:
             - serviceName: "projects/PROJECT_NUMBER/locations/global/backendServices/http-helloworld-service"
         EOF
         

  2. Use the specification in `http_route.yaml` to create the `HTTPRoute` resource.
         
         gcloud network-services http-routes import helloworld-http-route \
           --source=http_route.yaml \
           --location=global
         

  3. Verify that you can access the service from an external client through the regional external passthrough Network Load Balancer and the Cloud Service Mesh `Gateway`.
         
         curl -H "Host: helloworld-gce" IP_ADDRESS
         




## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.26/docs/service-routing/list-route-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
