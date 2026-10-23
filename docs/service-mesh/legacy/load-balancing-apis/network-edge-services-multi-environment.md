---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/network-edge-services-multi-environment/
title: Set up network edge services with hybrid connectivity network endpoint groups \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:26.973820+00:00
---

# Set up network edge services with hybrid connectivity network endpoint groups  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/network-edge-services-multi-environment/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up network edge services with hybrid connectivity network endpoint groups

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Google offers various network edge services that can augment the capabilities and security of services based outside of Google Cloud (on-premises and multi-cloud services)—for example, in an on-premises data center or in another public cloud.

These network edge services let you do the following:

  * Accept and route external customer traffic globally with a single Anycast VIP.

  * Reduce server load by terminating TLS traffic at the edge with an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) and [Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs).

  * Enable pre-configured web application firewall (WAF) rules and apply allowlists and denylists to incoming traffic with [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview).

  * Control user access to your applications and resources with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview).

  * Optimize content delivery and end-user latency with [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview).


[ ![Example of network edge services.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-solutions-1.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-on-prem-solutions-1.svg) Example of network edge services (click to enlarge)

To bring these benefits to your private, on-premises, or multi-cloud services, you deploy an external Application Load Balancer to receive traffic from the public internet. The external Application Load Balancer forwards traffic to a middle proxy that Cloud Service Mesh configures. This middle proxy routes traffic to your on-premises environment or non-Google Cloud environment by using [Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

**Note:** External Application Load Balancers provide similar functionality by using internet network endpoint groups (NEGs). Traffic can be sent directly to publicly accessible IP addresses and publicly resolvable fully qualified domain names (FQDNs) outside of Google Cloud, without the need for a middle proxy. This traffic, however, does not traverse your Virtual Private Cloud (VPC) network, and cannot be routed to a remote endpoint by using a private connection. For more information about public endpoint support, see the [Internet network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts).

This tutorial walks you through an end-to-end example that uses Cloud Armor at Google's edge to selectively allow clients to access an on-premises service privately. Clients are allowed access based on their IP address.

You complete the following tasks:

  1. Deploy Envoy as a middle proxy in a managed instance group (MIG). This Envoy proxy is automatically connected to Cloud Service Mesh.
  2. Create a simulated private, on-premises virtual machine (VM) instance. In a real-world example, you would probably already have an on-premises VM.
  3. Configure Cloud Service Mesh to route all requests that reach the middle proxy to the simulated on-premises VM.
  4. Create an external Application Load Balancer to receive traffic from the public internet and forward it to the middle proxy.
  5. Attach a Cloud Armor security policy to the external Application Load Balancer.



After you complete these tasks, you can optionally explore additional edge services and advanced traffic management features.

## Prerequisites

Before setting up your middle proxy, complete the following tasks:

  * Review [Prepare to set up Cloud Service Mesh with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/prepare-for-envoy-setup) and complete all the prerequisite tasks, which include granting the required permissions and roles and enabling the Cloud Service Mesh API.

  * Ensure that your private on-premises endpoints are reachable from within your Google Cloud Virtual Private Cloud (VPC) network through [Cloud VPN or Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product). The example used in this tutorial only routes traffic to an endpoint within Google Cloud, so you don't need to configure [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) to follow along. In a real-world deployment scenario, configuring hybrid connectivity would be required.

  * Ensure that your VPC subnet CIDR ranges don't conflict with your remote CIDR ranges. When IP addresses overlap, subnet routes are prioritized over remote connectivity.

  * For this demonstration, obtain the [necessary permissions](https://docs.cloud.google.com/armor/docs/configure-security-policies#iam-perms) to create and update Cloud Armor security policies. The permissions might vary if you want to use a different service, such as Cloud CDN.




## Deploy the middle proxy on Compute Engine VMs

This section describes how to deploy Envoy as a middle proxy on Compute Engine to receive traffic from the external load balancer and forward it to your remote destination.

### Create the instance template for the middle proxy

An instance template specifies configuration for VMs within a managed instance group (MIG).

  1. Use the following template to create VM instances with an Envoy proxy connected to Cloud Service Mesh:
         
         gcloud compute instance-templates create td-middle-proxy \
             --service-proxy=enabled \
             --tags=allow-hc
         

  2. To customize your Envoy deployment, such as by specifying the network name, setting a log path, or enabling tracing, see the [Automated Envoy deployment option guide](https://docs.cloud.google.com/service-mesh/docs/service-routing/auto-vms-options).




### Create the MIG for the middle proxy

  1. Create the MIG based on the template. In this example, you can keep the instance group size of 1 to deploy a single instance. For production usage, [enable autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu#enable_autoscaling_based_on_cpu_utilization)—for example, based on CPU utilization, to avoid creating a bottleneck if your middle proxy needs to handle a lot of traffic.
         
         gcloud compute instance-groups managed create td-middle-proxy-us-central1-a \
             --zone=us-central1-a \
             --template=td-middle-proxy \
             --size=1
         

  2. For future configurations and verification, identify and store the internal IP address of the instance in `MIDDLE_PROXY_IP`:
         
         MIDDLE_PROXY_IP=$(gcloud compute instances list \
             --filter="name~'td-middle-proxy-us-central1-a-.*'" \
             --zones=us-central1-a \
             --format="value(networkInterfaces.networkIP)")
         




In this example, we create the MIG that contains VM instances running Envoy in `us-central1-a`. Later in this tutorial, you create an external load balancer to handle public internet traffic from your clients.

Because the external load balancer can automatically route traffic to the region that is closest to your clients and to the MIG within that region, you might want to consider creating multiple MIGs. For a full list of Google Cloud's available regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#locations).

## Deploy the simulated on-premises service

This section describes deploying a hybrid connectivity network endpoint group (NEG). In a production deployment, this NEG would contain an endpoint (`IP:port`) that resolves to your on-premises server. In this example, you create a Compute Engine VM that is reachable on an `IP:port`. This VM acts as your simulated on-premises server.

### Create the simulated on-premises VM

  1. Deploy a single VM instance to simulate a private, on-premises server:
         
         gcloud compute instances create on-prem-vm \
             --zone=us-central1-a \
             --metadata startup-script='#! /bin/bash
         ## Installs apache and a custom homepage
         sudo su -
         apt-get update
         apt-get install -y apache2
         cat <<EOF > /var/www/html/index.html
         <html><body><h1>Hello world from on-premises!</h1></body></html>
         EOF'
         

  2. Identify and store its internal IP address for future configurations and verification. The server on this VM listens for inbound requests on port `80`:
         
         ON_PREM_IP=$(gcloud compute instances describe on-prem-vm \
             --zone=us-central1-a \
             --format="value(networkInterfaces.networkIP)" | sed "s/['\[\]]*//g")
         




### Create the NEG

Create the NEG for this demonstration setup by specifying the `non-gcp-private-ip-port` network endpoint type. Add the IP address and port for your simulated on-premises VM as an endpoint to this NEG. Following on the previous step, the IP address is stored in the `ON_PREM_IP` environment variable.

**Note:** In a production deployment, you would use the on-premises server's `IP:port` instead of the simulated on-premises VM's `IP:port`. This `IP:port` must be reachable from the middle proxy in your VPC network.

  1. Create the NEG:
         
         gcloud compute network-endpoint-groups create td-on-prem-neg \
             --network-endpoint-type=non-gcp-private-ip-port \
             --zone=us-central1-a
         

  2. Add the `IP:port` to your new NEG:
         
         gcloud compute network-endpoint-groups update td-on-prem-neg \
             --zone=us-central1-a \
             --add-endpoint="ip=$ON_PREM_IP,port=80"
         




## Configure Cloud Service Mesh with Cloud Load Balancing components

This section shows how to configure Cloud Service Mesh and enable your middle proxy to forward traffic to your private, on-premises service. You configure the following components:

  * A health check. This health check behaves slightly differently from the health checks configured for other NEG types.

  * A backend service. For more information, see the [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

  * A routing rule map. This step includes creating a forwarding rule, a target proxy, and a URL map. For more information, see [Routing rule maps](https://docs.cloud.google.com/service-mesh/docs/service-routing/routing-rule-maps).




### Create the health check

Health checks verify that your endpoints are healthy and able to receive requests. Health checking for this type of NEG relies on [Envoy's distributed health checking mechanism](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/health_checking).

Other NEG types use Google Cloud's centralized health checking system:
    
    
    gcloud compute health-checks create http td-on-prem-health-check
    

**Note:** Envoy's distributed health checking results in additional network traffic across your hybrid connectivity channel. Health checking traffic scales with the number of endpoints added to NEGs with type `non-gcp-private-ip-port`, and the number of Envoy proxies that health check these endpoints.

### Create the backend service

  1. Create a backend service with the `INTERNAL_SELF_MANAGED` load-balancing scheme to be used with Cloud Service Mesh. When you create this backend service, specify the health check that you previously created:
         
         gcloud compute backend-services create td-on-prem-backend-service \
             --global \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --health-checks=td-on-prem-health-check
         

  2. Add the NEG that you created earlier as the backend of this backend service:
         
         gcloud compute backend-services add-backend td-on-prem-backend-service \
             --global \
             --network-endpoint-group=td-on-prem-neg \
             --network-endpoint-group-zone=us-central1-a \
             --balancing-mode=RATE \
             --max-rate-per-endpoint=5
         


**Note:** A single backend service cannot include backends of different types. For example, you cannot mix MIGs and NEGs of different types in the same backend service. However, your URL map can have routing rules that resolve to different backend services, enabling advanced routing and traffic management for different types of services.

### Create the routing rule map

The routing rule map defines how Cloud Service Mesh routes traffic to your backend service.

  1. Create a URL map that uses the backend service defined previously:
         
         gcloud compute url-maps create td-hybrid-url-map \
             --default-service=td-on-prem-backend-service
         

  2. Create a file called `target_proxy.yaml` with the following contents:
         
         name: td-hybrid-proxy
         proxyBind: true
         urlMap: global/urlMaps/td-hybrid-url-map
         

  3. Use the `import` command to create the target HTTP proxy (for more information, see [Target proxies for Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/target-proxies)):
         
         gcloud compute target-http-proxies import td-hybrid-proxy \
             --source=target_proxy.yaml
         

  4. Create a forwarding rule that references this target HTTP proxy. Set the forwarding rule's IP address to `0.0.0.0`. Setting the rule's IP address to `0.0.0.0` routes traffic based on the inbound port, HTTP hostname, and path information configured in the URL map. The IP address specified in the HTTP request is ignored.
         
         gcloud compute forwarding-rules create td-hybrid-forwarding-rule \
             --global \
             --load-balancing-scheme=INTERNAL_SELF_MANAGED \
             --address=0.0.0.0 \
             --target-http-proxy=td-hybrid-proxy \
             --ports=8080 \
             --network=default
         


**Note:** With `proxyBind` enabled, setting the forwarding rule's address to anything other than `0.0.0.0` fails.

### Verify that the middle proxy can route requests to the simulated on-premises service

Cloud Service Mesh is now configured to route traffic through the middle proxy to your simulated private, on-premises service. You can verify this configuration by creating a test client VM, logging into that VM, and sending a request to the middle proxy that is running Envoy. After verifying the configuration, delete the test client VM.

  1. Get the IP address of the middle proxy. You only need this information for the verification step:
         
         gcloud compute instances list
         

  2. Write down or otherwise note the IP address of the instance in the `td-middle-proxy-us-central1-a` MIG.

  3. Create a test client instance:
         
         gcloud compute instances create test-client \
             --zone=us-central1-a
         

  4. Use `ssh` to sign in to the test client:
         
         gcloud compute ssh test-client
             --zone=us-central1-a
         

  5. Send a request to the middle proxy VM, substituting the IP address that you obtained previously for `MIDDLE_PROXY_IP`:
         
         curl $MIDDLE_PROXY_IP:8080
         

You should see the following output:
         
         Hello world from on-premises!
         

  6. Exit the test client VM. After you exit, you can delete the VM:
         
         gcloud compute instances delete test-client \
             --zone=us-central1-a
         




## Deploy the external Application Load Balancer

In this section, you deploy an external Application Load Balancer that sends incoming traffic to the middle proxy. This deployment is a standard external Application Load Balancer setup.

### Reserve an external IP address

Create a global static external IP address (`external-lb-vip`) to which external clients will send traffic. You retrieve this external IP address during the verification step later in this tutorial.
    
    
    gcloud compute addresses create external-lb-vip \
        --ip-version=IPV4 \
        --global
    

### Set up the external HTTP load balancer

Configure the external load balancer to route internet customer traffic to your already-configured middle proxy.

  1. Create a health check that is used to determine whether the MIG that runs the middle proxy is healthy and able to receive traffic:
         
         gcloud compute health-checks create tcp tcp-basic-check \
             --port=8080
         

  2. Create a firewall rule to allow health checking. You re-use the `allow-hc` tag here to apply the firewall rule to the middle proxy VMs:
         
         gcloud compute firewall-rules create fw-allow-health-checks \
             --network=default \
             --action=ALLOW \
             --direction=INGRESS \
             --source-ranges=35.191.0.0/16,130.211.0.0/22 \
             --target-tags=allow-hc \
             --rules=tcp
         

  3. Create a backend service:
         
         gcloud compute backend-services create td-middle-proxy-backend-service \
             --protocol=HTTP \
             --health-checks=tcp-basic-check \
             --global
         

  4. Add the middle proxy MIG as the backend to this backend service:
         
         gcloud compute backend-services add-backend td-middle-proxy-backend-service \
             --instance-group=td-middle-proxy-us-central1-a \
             --instance-group-zone=us-central1-a \
             --global
         

  5. Create a URL map to route the incoming requests to the middle proxy as the default backend service:
         
         gcloud compute url-maps create lb-map-http \
             --default-service=td-middle-proxy-backend-service
         

  6. Create a target HTTP proxy so that requests to the external load balancer's forwarding rule virtual IP address (VIP) are handled according to the URL map:
         
         gcloud compute target-http-proxies create http-lb-proxy \
             --url-map=lb-map-http
         

  7. Create a global forwarding rule to route incoming requests to the target HTTP proxy:
         
         gcloud compute forwarding-rules create http-forwarding-rule \
             --address=external-lb-vip\
             --global \
             --load-balancing-scheme=EXTERNAL \
             --target-http-proxy=http-lb-proxy \
             --ports=80
         


**Note:** To enable HTTPS communication from the client to the load balancer, configure a target HTTPS proxy instead of a target HTTP proxy. Then assign it a [Google-managed](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#permissions) or [self-managed](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/self-managed-certs) SSL certificate.

### Set the MIG's named port

Set a named port for the instance group to allow your middle proxy to receive HTTP traffic from the external load balancer:
    
    
    gcloud compute instance-groups managed set-named-ports td-middle-proxy-us-central1-a \
        --named-ports=http:8080 \
        --zone=us-central1-a
    

### Verify the external Application Load Balancer configuration

In this step, you verify that the external load balancer is set up correctly.

  1. You should be able to send a request to the load balancer's VIP and get a response from the simulated on-premises VM:
         
         PUBLIC_VIP=gcloud compute addresses describe external-lb-vip \
             --format="get(address)" \
             --global
         

  2. Issue a `curl` request to the external IP address (`PUBLIC_VIP`) and verify that you receive the `Hello world` message:
         
         curl $PUBLIC_VIP
         

You see the following output:
         
         Hello world from on-premises!
         




## Enable Cloud Armor

**Note:** Cloud Armor is used here for demonstration purposes. You can configure any other services available in the external load balancer in addition to, or instead of, Cloud Armor. The previous steps remain the same.

Configure Cloud Armor security policies to only allow access to your service from `CLIENT_IP_RANGE`, which should include the external IP address of the client device that you intend to test with—for example, `"192.0.2.0/24"`.

These policies are applied on the backend service of the external load balancer (in this example, `td-hybrid-backend-service` pointing at the middle proxy). For more information about the permissions required to set these rules, see [Configure Cloud Armor security policies](https://docs.cloud.google.com/armor/docs/configure-security-policies).

  1. Create the Cloud Armor security policy:
         
         gcloud compute security-policies create external-clients-policy \
             --description="policy for external clients"
         

  2. Update the default rule of the security policy to deny all traffic:
         
         gcloud compute security-policies rules update 2147483647 \
             --security-policy=external-clients-policy \
             --action="deny-404"
         

  3. Add a higher priority rule to allow traffic from a specific IP range:
         
         gcloud compute security-policies rules create 1000 \
             --security-policy=external-clients-policy \
             --description="allow traffic from CLIENT_IP_RANGE" \
             --src-ip-ranges="CLIENT_IP_RANGE" \
             --action="allow"
         

  4. Attach the Cloud Armor security policies to your backend service:
         
         gcloud compute backend-services update td-middle-proxy-backend-service \
             --security-policy=external-clients-policy
         




## Final verification

  1. Issue a `curl` request to the external Application Load Balancer's public virtual IP address. If your client device's IP address is within the allowed `CLIENT_IP_RANGE` specified previously, you should receive the expected response.
         
         curl $PUBLIC_VIP
         

You see the following output:
         
         Hello world from on-premises!
         

  2. Issue the same `curl` request from a different client device whose IP address lies outside of `CLIENT_IP_RANGE`, or update your security policy rule to no longer include your client IP address. You should now receive a `404 Not Found` error.




## Troubleshooting

The following instructiions describe how to fix problems with your configuration.

### My on-premises service is not accessible through the global external Application Load Balancer IP address

Assuming that your on-premises service is already accessible on the Google Cloud VMs where the Envoys are running, follow these steps to troubleshoot your setup:

  1. Make sure that the Google Cloud Envoy MIG is reported as healthy. In the Google Cloud console, go to **Network services > Load balancing** and click `url-map lb-map-http` to view its details. You should be able to see that 1/1 of the instance in `td-middle-proxy-us-central1-a` is healthy.

  2. If it's not healthy, check if a firewall rule has been configured to allow ingress health-check traffic to the Google Cloud VMs that are running Envoy:
         
         gcloud compute firewall-rules describe fw-allow-health-check
         

You should see the following output:
         
         allowed:
         ‑ IPProtocol: tcp
         ...
         direction: INGRESS
         disabled: false
         ...
         ...
         sourceRanges:
         ‑ 130.211.0.0/22
         ‑ 35.191.0.0/16
         targetTags:
         ‑ allow-hc
         




## What's next

  * To find more complex routing policies for your on-premises or multicloud services, see Cloud Service Mesh's [advanced traffic management features](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).

  * To deploy Cloud Service Mesh, see the [Setup guide overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/deploy).

  * To enable additional network edge services, see the following guides:

    * [Enable IAP for Compute Engine](https://docs.cloud.google.com/iap/docs/enabling-compute-howto)
    * [Set up Cloud CDN with a managed instance group](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-mig)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
