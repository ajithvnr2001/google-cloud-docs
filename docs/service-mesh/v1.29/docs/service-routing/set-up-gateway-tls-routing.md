---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/set-up-gateway-tls-routing/
title: Set up Gateway TLS routing \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:33.929616+00:00
---

# Set up Gateway TLS routing  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/set-up-gateway-tls-routing/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up Gateway TLS routing

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

This guide demonstrates how to set up an Envoy proxy-based ingress gateway with `Gateway` and `TLSRoute` resources. You can also attach a `TLSRoute` resource.

The deployment you configure is illustrated in the following diagram. A regional external passthrough Network Load Balancer directs traffic to Envoy proxies that act as an ingress gateway. The Envoy proxies use TLS passthrough routing and direct traffic to HTTPS servers running on the backend VM instances.

[ ![TLS passthrough with an ingress gateway](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-passthrough-nlb.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-passthrough-nlb.svg) TLS passthrough with an ingress gateway (click to enlarge)

## Before you begin

Make sure that you complete the tasks described in [Prepare to set up with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.29/docs/onboarding/prepare-service-routing-envoy-proxyless).

## Configure firewall rules

In this section, you create firewall rules to allow incoming health check connections to VM instances in your network.

  1. Create a firewall rule:
         
         gcloud compute firewall-rules create allow-gateway-health-checks \
          --network=NETWORK_NAME \
          --direction=INGRESS \
          --action=ALLOW \
          --rules=tcp \
          --source-ranges="35.191.0.0/16,209.85.152.0/22,209.85.204.0/22" \
          --target-tags=gateway-proxy
         

  2. Configure firewall rules to allow traffic from any source. Edit the commands for your ports and source IP address ranges:
         
         gcloud compute firewall-rules create allow-gateway-ingress-traffic \
           --network=NETWORK_NAME \
           --direction=INGRESS \
           --action=ALLOW \
           --rules=tcp:443 \
           --source-ranges="0.0.0.0/0" \
           --target-tags=gateway-proxy
         




## Configure Identity and Access Management permissions

In this section, you designate the service account for the gateway proxies and assign the correct IAM roles to the service account.

  1. Create a service account identity for the gateway proxies:
         
         gcloud iam service-accounts create gateway-proxy
         

  2. Assign the required IAM roles to the service account identity:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/trafficdirector.client"
         
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
           --member="serviceAccount:gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --role="roles/logging.logWriter"
         




## Configure the `Gateway` resource

  1. In a file called `gateway443.yaml`, create the `Gateway` specification for HTTP traffic:
         
         name: gateway443
         scope: gateway-proxy
         ports:
         - 443
         type: OPEN_MESH
         

  2. Create the `Gateway` resource using the `gateway443.yaml` specification:
         
         gcloud network-services gateways import gateway443 \
             --source=gateway443.yaml \
             --location=global
         




## Create a managed instance group with Envoy proxies

In this section, you create the Envoy proxies that are associated with the ingress gateway.

  1. Create an instance template for a VM running an automatically deployed Envoy service proxy. The Envoys have the scope set to `gateway-proxy`. Don't pass the serving port as a parameter of the `--service-proxy` flag.
         
         gcloud beta compute instance-templates create gateway-proxy \
           --machine-type=n1-standard-1 \
           --boot-disk-size=10GB \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=gateway-proxy \
           --network-interface=network=NETWORK_NAME,no-address \
           --service-account="gateway-proxy@PROJECT_ID.iam.gserviceaccount.com" \
           --service-proxy=enabled,scope=gateway-proxy
         

  2. Create a regional managed instance group from the instance template:
         
         gcloud compute instance-groups managed create gateway-proxy \
           --region=REGION \
           --size=1 \
           --template=gateway-proxy
         

  3. Set the serving port name for the managed instance group:
         
         gcloud compute instance-groups managed set-named-ports gateway-proxy \
           --named-ports=https:443 \
           --region=REGION
         




## Set up the regional external passthrough Network Load Balancer

In this section, you create the regional external passthrough Network Load Balancer.

  1. Create a static external regional IP address:
         
         gcloud compute addresses create xnlb-REGION \
           --region=REGION
         

  2. Obtain the IP address that is reserved for the external load balancer:
         
         gcloud compute addresses describe xnlb-REGION \
           --region=REGION --format='value(address)'
         

This IP address is used as the variable `IP_ADDRESS` later in this setup guide.

  3. Create a health check for the gateway proxies:
         
         gcloud compute health-checks create tcp xnlb-REGION \
           --region=REGION \
           --use-serving-port
         

  4. Create a backend service for the gateway proxies:
         
         gcloud compute backend-services create xnlb-REGION \
           --health-checks=xnlb-REGION \
           --health-checks-region=REGION \
           --load-balancing-scheme=EXTERNAL \
           --protocol=TCP \
           --region=REGION \
           --port-name=https
         

  5. Add the managed instance group as a backend:
         
         gcloud compute backend-services add-backend xnlb-REGION \
           --instance-group=gateway-proxy \
           --instance-group-region=REGION \
           --region=REGION
         

  6. Create a forwarding rule to route traffic to the gateway proxies:
         
         gcloud compute forwarding-rules create xnlb-REGION \
           --region=REGION \
           --load-balancing-scheme=EXTERNAL \
           --address=IP_ADDRESS \
           --ip-protocol=TCP \
           --ports=443 \
           --backend-service=xnlb-REGION \
           --backend-service-region=REGION
         




### Configure a managed instance group running an HTTPS service

For demonstration purposes, create a backend service with autoscaled VMs in a managed instance group. The VMs echo details about web requests using the HTTPS protocol on port `443`.

  1. Create an instance template with an HTTPS service that is exposed on port `443`:
         
         gcloud compute instance-templates create td-https-vm-template \
           --scopes=https://www.googleapis.com/auth/cloud-platform \
           --tags=https-td-server \
           --image-family=debian-10 \
           --image-project=debian-cloud \
           --metadata=startup-script='#! /bin/bash
         
         sudo rm -rf /var/lib/apt/lists/*
         sudo apt-get -y clean
         sudo apt-get -y update
         sudo apt-get -y install apt-transport-https ca-certificates curl gnupg2 software-properties-common
         sudo curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
         sudo add-apt-repository -y "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
         sudo apt-get -y update
         sudo apt-get -y install docker-ce
         sudo which docker
         echo "{ \"registry-mirrors\": [\"https://mirror.gcr.io\"] }" | sudo tee -a /etc/docker/daemon.json
         sudo service docker restart
         sudo docker run -e HTTPS_PORT=9999 -p 443:9999 --rm -dt mendhak/http-https-echo:22'
         

  2. Create a managed instance group based on the instance template:
         
         gcloud compute instance-groups managed create https-td-mig-us-REGION \
           --zone=ZONE \
           --size=2 \
           --template=td-https-vm-template
         

  3. Set the name of the serving port for the managed instance group:
         
         gcloud compute instance-groups managed set-named-ports https-td-mig-us-REGION \
           --named-ports=https:443 \
           --zone=ZONE
         

  4. Create a health check:
         
         gcloud compute health-checks create https https-helloworld-health-check \
           --port=443
         

  5. Create a firewall rule to allow incoming health check connections to instances in your network:
         
         gcloud compute firewall-rules create https-vm-allow-health-checks \
            --network NETWORK_NAME --action allow --direction INGRESS \
            --source-ranges 35.191.0.0/16,130.211.0.0/22 \
            --target-tags https-td-server \
            --rules tcp:443
         

  6. Create a global [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) with a load balancing scheme of `INTERNAL_SELF_MANAGED` and add the health check:
         
         gcloud compute backend-services create https-helloworld-service \
           --global \
           --load-balancing-scheme=INTERNAL_SELF_MANAGED \
           --port-name=https \
           --health-checks https-helloworld-health-check
         

  7. Add the managed instance group as a backend to the backend service:
         
         gcloud compute backend-services add-backend https-helloworld-service \
           --instance-group=https-td-mig-us-REGION \
           --instance-group-zone=ZONE \
           --global
         




### Set up routing with a `TLSRoute` resource

In previous sections, you configured a `Gateway` resource and HTTPS server. Next, connect them using a `TLSRoute` resource that associates an SNI hostname with a backend service.

  1. In a file called `tls_route.yaml`, create the `TLSRoute` specification:
         
         name: helloworld-tls-route
         gateways:
         - projects/PROJECT_NUMBER/locations/global/gateways/gateway443
         rules:
         - matches:
           - sniHost:
             - example.com
             alpn:
             - h2
           action:
            destinations:
            - serviceName: projects/PROJECT_NUMBER/locations/global/backendServices/https-helloworld-service
         

In the previous instruction, `TLSRoute` matches `example.com` as SNI _and_ `h2` as ALPN. If the matches are changed as follows, `TLSRoute` matches SNI _or_ ALPN:
         
         - matches:
           - sniHost:
             - example.com
           - alpn:
             - h2
         

  2. Use the `tls_route.yaml` specification to create the `TLSRoute` resource:
         
         gcloud network-services tls-routes import helloworld-tls-route \
             --source=tls_route.yaml \
             --location=global
         




Cloud Service Mesh is configured to load balance traffic for the services specified in the `TLSRoute` resource across the backends in the managed instance group.

### Validate the deployment

In this section, you verify that you can access the service from an external client through the regional external passthrough Network Load Balancer and the Cloud Service Mesh `Gateway` resource.

  1. Run the following `curl` command to verify HTTP connectivity to the test services that you created:
         
         curl https://example.com --resolve example.com:443:IP_ADDRESS -k
         




The command returns a response from one of the VMs in the managed instance group. The output is the following:
    
    
     "path": "/",
      "headers": {
        "host": "example.com",
        "user-agent": "curl/7.81.0",
        "accept": "*/*"
      },
      "method": "GET",
      "body": "",
      "fresh": false,
      "hostname": "example.com",
      "ip": "::ffff:10.142.0.2",
      "ips": [],
      "protocol": "https",
      "query": {},
      "subdomains": [],
      "xhr": false,
      "os": {
        "hostname": "0cd3aec9b351"
      },
      "connection": {
        "servername": "example.com"
      }
    }
    

#### Verify with a negative verification

You can also run a negative verification. If you run the commands in this section, the request is dropped because it does not match the `TLSRoute` match criteria.

In the following command, the SNI does not match example.com, so the `Gateway` rejects the connection:
    
    
    curl https://invalid-server.com --resolve invalid-server.com:443:IP_ADDRESS -k
    

In the following command, the ALPN does not match h2 (HTTP2 protocol), so the `Gateway` rejects the connection:
    
    
    curl https://example.com --resolve example.com:443:IP_ADDRESS -k --http1.1
    

In the following command, the client is creating a plain text (unencrypted) connection, so the `Gateway` rejects the connection:
    
    
    curl example.com:443 --resolve example.com:443:IP_ADDRESS -k
    

The previous commands all return the following error:
    
    
    curl: (35) OpenSSL SSL_connect: Connection reset by peer in connection.
    

## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/list-route-resources).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
