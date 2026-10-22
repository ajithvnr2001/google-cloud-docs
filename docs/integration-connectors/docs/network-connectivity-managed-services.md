---
url: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services/
title: Network connectivity in Google Cloud managed services \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:36.670792+00:00
---

# Network connectivity in Google Cloud managed services  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network connectivity in Google Cloud managed services

This page describes how to setup private connectivity from Integration Connectors to your backend service such as [CloudSQL for MySQL](https://docs.cloud.google.com/sql/docs/mysql/features), [CloudSQL for PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/features), and [CloudSQL for SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/features). This page assumes that you are familiar with the following concepts:

  * [Endpoint attachments](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private#endpoint-attachments)
  * [Managed zones](https://docs.cloud.google.com/dns/docs/zones)
  * [Private Service Connect (PSC)](https://docs.cloud.google.com/vpc/docs/private-service-connect)
  * [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing)



## Considerations

When you create a PSC service attachment, consider the following key points:

  * The PSC service attachment and the load balancer are created in different subnets within the same VPC. And specifically, the service attachment is always created in a NAT subnet.
  * SOCKS5 proxy servers must be bound to the `0.0.0.0:<port>` IP address because this is required for incoming traffic from the load balancer and the health check probes. For more information, see [Health check](https://docs.cloud.google.com/load-balancing/docs/internal#health-checking).
  * Traffic from load balancer and health check probe should be sent to the same port.
  * Configure the firewall rules to facilitate the traffic flow. 

**Ingress rules**

    * Traffic from the PSC service attachment's subnet should reach your backend service. 
    * Within the ILB's subnet, ILB should be able to send traffic to the SOCKS5 proxy servers.
    * The health check probe should be able to access the SOCKS5 proxy servers. The Google Cloud health check probes have a fixed IP range (`35.191.0.0/16, 130.211.0.0/22`). So these IPs can be allowed to send traffic to the SOCKS proxy servers.

**Egress rules**

Egress traffic is enabled by default in a Google Cloud project, unless specific deny rules are configured.

  * All your Google Cloud components such as the PSC service attachment and the load balancer should be in the same region.
  * Ensure that your SOCKS5 proxy servers accept traffic in the following scenarios: 
    * **Pass-through load balancers (L4 TCP/UDP ILB):** Requests from the PSC service attachment's NAT IPs should be able to reach your SOCKS5 proxy servers. Therefore, you must allow the entire NAT subnet's IP range for the service attachment. For more information, see [Private Service Connect subnets](https://docs.cloud.google.com/vpc/docs/private-service-connect#psc-subnets). 
    * **Proxy-based/HTTP(s) load balancers (L4 proxy ILB, L7 ILB):** All new requests originate from the load balancer. Therefore, your SOCKS5 proxy servers should accept requests from the proxy subnet of your VPC network. For more information, see [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets).



## Configure private connectivity

A few of the managed Google Cloud services such as [CloudSQL MySQL](https://docs.cloud.google.com/sql/docs/mysql/about-private-service-connect#service-attachment) expose a PSC service attachment for private connectivity. In those cases, you can skip this step to create a PSC service attachment, and the PSC service attachment provided by the managed service provided can be used to create the Integration Connectors endpoint attachment. 

You must create a new PSC service attachment in the following scenarios:

  * The Google Cloud managed service doesn't expose a service attachment, but exposes an IP address using private service access.
  * The Google Cloud managed service exposes a service attachment but doesn't support allowlisting the Integration Connectors project to consume the service attachment. 



The steps to create the service attachment for these two scenarios is described in detail in the following sections. After you create the service attachment, you must [create an endpoint attachment](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services#create-endpoint-attachment) and [configure a connection](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-managed-services#configure-connection) to use the endpoint attachment.

### Create a service attachment for a managed service that restricts access

The managed service might not allow Integration Connectors project to be allowlisted to consume the service attachment it exposes. In this case, you must create a load balancer that consumes the service attachment and exposes the load balancer to Integration Connectors by creating another service attachment in your project. 

The following image shows a managed service that exposes a service attachment:

![](https://docs.cloud.google.com/static/integration-connectors/images/sa-non-exposed.png)

For an example of a managed service that exposes a service attachment, see [Private connectivity for a MongoDB Atlas cluster](https://docs.cloud.google.com/integration-connectors/docs/connectors/mongodb/configure-psc-mongodb).

#### Create a load balancer with PSC NEG as the backend

  1. Create a NEG to connect to a published service.
  2. Add a backend to a regional internal proxy Network Load Balancer.



For more information, see [Create a Private Service Connect NEG](https://docs.cloud.google.com/vpc/docs/access-apis-managed-services-private-service-connect-backends#create-neg). 

#### Create a service attachment

  1. Create a subnet for PSC NAT. 
  2. Create a firewall rule to allow request from PSC NAT to load balancer 
  3. Create service attachment.



For more information, see [Create a PSC service attachment](https://docs.cloud.google.com/integration-connectors/docs/configure-psc#create-a-psc-service-attachment)

#### Allow PSC connection from Integration Connectors project

Ensure the Integration Connectors project in Service Directory is allowlisted in the service attachment. For more information, see [Allowlist the Integration Connectors project in a service attachment](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private#allowlist-the-integration-connectors-project-in-a-service-attachment). 

### Create a service attachment for a managed service that exposes IP address

If the managed service doesn't expose a service attachment, the traffic from Integration Connectors must be proxied through your project.

The following image shows a managed service that doesn't expose a service attachment:

![](https://docs.cloud.google.com/static/integration-connectors/images/sa-exposed.png)

To configure private connectivity, do the following steps:

  1. Create a PSC service attachment. 
     1. Create [Compute Engine VM instances](https://docs.cloud.google.com/vpc/docs/special-configurations) for running SOCKS5 proxy servers. 
        1. Create proxy instance 1. 
               
               gcloud compute instances create PROXY_INSTANCE_1 \
                           --project=PROJECT_ID \
                           --network-interface=network-tier=PREMIUM,subnet=SUBNET_NAME_2,no-address
                         

Based on your requirement, you can create as many VM instances as required.

     2. Create a firewall rule for allowing SSH to your VM instances. 
            
            gcloud compute firewall-rules create FIREWALL_RULE_NAME_SSH \
                        --direction=INGRESS --priority=1000 --network=VPC_NETWORK --allow=tcp:22
                        

The VM instance will be used to proxy the traffic from Integration Connectors to the managed service. Install a [SOCKS5 proxy](https://en.wikipedia.org/wiki/SOCKS) in the VM instance. The Cloud SQL Auth proxy supports chaining through a SOCKS5 proxy, which lets you forward encrypted traffic from the Cloud SQL Auth proxy to the destination Cloud SQL instance. 

**Note:** While you can continue to use a SOCKS5 proxy for connectivity, the **Cloud SQL for MySQL** connector now additionally supports direct routing via Private Service Connect (PSC). If you choose this path, you can route traffic directly by creating an endpoint attachment and selecting **Private Service Connect (PSC)** as the host type in your connector configuration. Note that **Cloud SQL for PostgreSQL** and **Cloud SQL for SQL Server** must continue to use the SOCKS5 proxy configuration workflow detailed below.**Important:** The Cloud SQL for MySQL connector currently supports only unencrypted traffic. If you use the direct PSC routing path, ensure that your Cloud SQL instance is configured to **"Allow unencrypted network traffic"**. Connections to instances configured to "Allow only SSL connections" are not supported.

Detailed steps to install and configure a SOCKS5 proxy server are outside the scope of this document, and you can install any SOCKS5 proxy of your choice. The following steps show how to install and configure the Dante SOCKS5 proxy server.

        1. SSH to your VM instance. 
               
               gcloud compute ssh \
                           --tunnel-through-iap \
                           PROXY_INSTANCE_1
                       

        2. Install the Dante SOCKS5 proxy server. 
               
               sudo apt update
                       sudo apt install dante-server

        3. Check the server interface. 
               
               sudo ip a

        4. Create backup of the Dante configuration. 
               
               sudo mv /etc/danted.conf /etc/danted.conf.bak

        5. Create a new Dante configuration file. 
               
               sudo nano /etc/danted.conf

        6. Copy the following configuration to the config file: 
               
               logoutput: /var/log/socks.log
                       # Bind the server to the 0.0.0.0 IP address to allow traffic
                       # traffic from the load balancer and the health check probes.
                       internal: 0.0.0.0 port = 1080
                       external: ens4
                       clientmethod: none
                       socksmethod: none
                       user.privileged: root
                       user.notprivileged: nobody
                       client pass {
                               from: 0.0.0.0/0 to: 0.0.0.0/0
                               log: error connect disconnect
                       }
                       client block {
                               from: 0.0.0.0/0 to: 0.0.0.0/0
                               log: connect error
                       }
                       socks pass {
                               from: 0.0.0.0/0 to: 0.0.0.0/0
                               log: error connect disconnect
                       }
                       socks block {
                               from: 0.0.0.0/0 to: 0.0.0.0/0
                               log: connect error
                       }

        7. Restart the Dante server and check the status. 
               
               sudo systemctl restart danted
                       sudo systemctl status danted

        8. Exit from the VM instance. 
               
               exit

  2. Create a load balancer with the VM instance as the backend. 
     1. Create an [unmanaged instance group](https://docs.cloud.google.com/integration-connectors/docs/compute/docs/instance-groups). 
            
            gcloud compute instance-groups unmanaged create INSTANCE_GROUP_NAME

**Note:** You can create a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups) for better reliability.
     2. Add the VM instances created in step 3 to the group. 
            
            gcloud compute instance-groups unmanaged add-instances INSTANCE_GROUP_NAME \
                        --instances=PROXY_INSTANCE_1

  3. Create a [health check probe](https://docs.cloud.google.com/load-balancing/docs/health-checks) and allow the traffic from the probe. 
     1. Create the health check probe. 
            
            gcloud compute health-checks create tcp HEALTH_CHECK_NAME \
                        --port BACKEND_SERVER_PORT --region=REGION

In this command, set BACKEND_SERVER_PORT to 1080 which is the default port on which the SOCKS5 proxy servers run.

     2. Create a firewall rule to allow traffic from the probe. 
            
            gcloud compute firewall-rules create FIREWALL_RULE_NAME_HEALTHCHECK \
                        --direction=INGRESS --priority=1000 --network=VPC_NETWORK --allow=tcp:BACKEND_SERVER_PORT \
                        --source-ranges=35.191.0.0/16,130.211.0.0/22

  4. Create an [L4 internal load balancer](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal) and allow traffic from the load balancer. 
     1. Create a [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service). 
            
            gcloud compute backend-services create BACKEND_SERVICE \
                        --load-balancing-scheme=internal --protocol=tcp --health-checks=HEALTH_CHECK_NAME \
                        --health-checks-region=REGION 

     2. Add instance group to the backend service. 
            
            gcloud compute backend-services add-backend BACKEND_SERVICE \
                        --instance-group=INSTANCE_GROUP_NAME \
                        --instance-group-zone=ZONE

     3. Create a [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts). 
            
            gcloud compute forwarding-rules create FORWARDING_RULE_NAME \
                        --load-balancing-scheme=internal --network=VPC_NETWORK --subnet=SUBNET_NAME_2 \
                        --ip-protocol=TCP --ports=BACKEND_SERVER_PORT --backend-service=BACKEND_SERVICE \
                        --backend-service-region=REGION

     4. Create a firewall rule to allow internal traffic from load-balancer to the instance group. 
            
            gcloud compute firewall-rules create FIREWALL_RULE_NAME_INTERNAL \
                        --direction=INGRESS --priority=1000 --network=VPC_NETWORK \
                        --action=ALLOW --rules=all --source-ranges=SUBNET_RANGE_2




## Create an endpoint attachment

After you create a service attachment for a managed service, you must create an endpoint attachment and then use it in your connection.

**Endpoint attachment as an IP address**

For instructions on how to create an endpoint attachment as an IP address, see [Create an endpoint attachment as an IP address](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-ipaddr).

**Endpoint attachment as a hostname**

In certain cases such as TLS enabled backends, the destination requires you to use hostnames instead of private IPs to perform TLS validation. In those cases where a private DNS is used instead of an IP address for the host destination, in addition to creating an endpoint attachment as an IP address, you must also configure managed zones. For instructions on how to create an endpoint attachment as a hostname, see [Create an endpoint attachment as a hostname](https://docs.cloud.google.com/integration-connectors/docs/create-endpoint-attachment#create-ep-hostname). 

Later, when you configure your connection to use the endpoint attachment, you can select this endpoint attachment.

## Configure a connection to use the endpoint attachment

Now that you have created an endpoint attachment, use the endpoint attachment in your connection. When you create a new connection or update an existing connection, in the Destinations section, select **Endpoint attachment** as the **Destination Type** and select the endpoint attachment that you created from the **Endpoint Attachment** list.

If you created a managed zone, select **Host Address** as the **Destination Type** and use the A-record that you created while creating the managed zone.

## Troubleshooting tips

If you are having issues with private connectivity, follow the guidelines listed in this section to avoid common issues.

  * Ensure Integration Connectors project in Service Directory is allowlisted in the service attachment. For more information, see [Allowlist the Integration Connectors project in a service attachment](https://docs.cloud.google.com/integration-connectors/docs/network-connectivity-private#allowlist-the-integration-connectors-project-in-a-service-attachment).
  * Ensure the following configuration for the firewall rules: 
    * Traffic from the PSC service attachment's subnet must be allowed to reach your backend service.
  * The health check probe must be able to access your backend system. The Google Cloud health check probes have a fixed IP range (35.191.0.0/16, 130.211.0.0/22). So these IP addresses must be allowed to send traffic to your backend server.


* [Google Cloud Connectivity test](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) can be used to identify any gaps in your network configuration. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
