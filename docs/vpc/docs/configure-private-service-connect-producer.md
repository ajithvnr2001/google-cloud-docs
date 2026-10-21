---
url: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer/
title: Publish services by using Private Service Connect \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:28.534736+00:00
---

# Publish services by using Private Service Connect  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Publish services by using Private Service Connect

As a service producer, you can use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to publish services using internal IP addresses in your VPC network. Your published services are accessible to service consumers by using internal IP addresses in the consumer VPC networks.

This guide describes how to use Private Service Connect to publish a service. To publish a service, do the following:

  * Create a target service, which can be one of the following: 
    * The forwarding rule of a supported load balancer with a [supported configuration](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility)
    * A [Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)
  * [Create a service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#publish-service) that points to the target service.



Private Service Connect provides two methods to connect to published services:

  * [Endpoints (based on a forwarding rule)](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints)

  * [Backends (based on a load balancer)](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends)




These endpoint types require slightly different producer configurations. For more information, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility).

## Roles

The following [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) provides the permissions needed to perform the tasks in this guide.

  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)



## Before you begin

  * Read [About published services](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services) for information about publishing services, including limitations.

  * Decide whether the service should be accessible from all projects, or if you want to control which projects can access your service.

  * Decide whether you want this service to support endpoints, backends, or both. For more information about endpoints and backends, see [ Private Service Connect types](https://docs.cloud.google.com/vpc/docs/private-service-connect#types).

For more information about the service configuration requirements, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility).

  * Decide if you want to [configure a domain name for the service](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services), which automates DNS configuration for service consumer endpoints. If you do configure a domain name, the same IAM principal that publishes the service must verify that they have Owner permissions for the domain in the Google Search Console. If you configure a domain name, but you don't own the domain, publishing the service fails. To verify ownership, go to the [Google Search Console](https://search.google.com/search-console/welcome).

The domain name that you specify in the service attachment can be a subdomain of the domain that you verify. For example, you can verify `example.com` and then create a service attachment with a domain name of `us-west1.p.example.com`.

  * Decide whether your service will use [PROXY protocol](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility) to provide details about consumers' connections. If you plan to use PROXY protocol, make sure that it's supported by both your target service type and the service's backend web server software. For information about the types of target services that support PROXY protocol, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility).




## Create a target service

To host the service, create one of the following target services in a service producer VPC network:

  * [Internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal)

  * [Regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)

  * [Cross-region internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal)

  * [Internal protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)

  * [Regional internal proxy Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)

  * [Secure Web Proxy instance](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment)




For information about supported configurations for each target service, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility).

A service attachment can have only one target service. However, multiple service attachments can share the same target service.

The IP version of your target service (IPv4 or IPv6) affects which consumers can connect to your published service. For more information, see [IP version translation](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#ip-version-translation).

For regional internal proxy Network Load Balancers, the backends can be located in Google Cloud, in other clouds, in an on-premises environment, or any combination of these locations.

You can also publish a service that is hosted on an internal passthrough Network Load Balancer on Google Kubernetes Engine. This configuration, including load balancer and service attachment configuration, is described in [Create an internal passthrough Network Load Balancer with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#ilb_psc) in the GKE documentation.

## Create a subnet for Private Service Connect

Create one or more dedicated subnets to use with Private Service Connect. You must create the subnet in the same region as the service's load balancer.

If you're using the Google Cloud console to publish a service, you can create the subnets during that procedure.

You can create a Private Service Connect subnet in a Shared VPC host project.

You can't convert a regular subnet to a Private Service Connect subnet.

The IP stack type of the subnet that you create must be compatible with the IP version of your load balancer's forwarding rule:

  * For IPv4 forwarding rules, create an IPv4-only or dual-stack subnet.
  * For IPv6 forwarding rules, create an IPv6-only or dual-stack subnet that has an [internal IPv6 address range](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6).
  * If you use a dual-stack subnet, either the IPv4 or IPv6 address range is used, but not both.



If you need to make more IP addresses available to an existing service, see Add or remove subnets from a published service.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.subnetworks.create`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of a VPC network to show its **VPC network details** page.

  3. Click **Subnets**.

  4. Click **Add subnet**. In the panel that appears, do the following:

     1. Provide a name.
     2. Select a region.
     3. In the **Purpose** section, select **Private Service Connect**.
     4. In the **IP stack type** section, select an IP stack type.
     5. If you are creating an IPv4-only or dual-stack subnet, enter an IPv4 address range—for example, `10.10.10.0/24`.
     6. If you are creating an IPv6-only or dual-stack subnet, click **IPv6 access type** and select **Internal**.
     7. Click **Add**.



###  gcloud 

Use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).

  * To create an IPv4-only Private Service Connect subnet, do the following:
        
        gcloud compute networks subnets create SUBNET_NAME \
            --network=NETWORK_NAME \
            --region=REGION \
            --range=SUBNET_RANGE \
            --purpose=PRIVATE_SERVICE_CONNECT
        

  * To create a dual-stack Private Service Connect subnet, do the following:
        
        gcloud compute networks subnets create SUBNET_NAME \
            --network=NETWORK_NAME \
            --region=REGION \
            --stack-type=IPV4_IPV6 \
            --ipv6-access-type=INTERNAL \
            --range=SUBNET_RANGE \
            --purpose=PRIVATE_SERVICE_CONNECT
        

  * To create an IPv6-only Private Service Connect subnet, do the following:
        
        gcloud compute networks subnets create SUBNET_NAME \
            --network=NETWORK_NAME \
            --region=REGION \
            --stack-type=IPV6_ONLY \
            --ipv6-access-type=INTERNAL \
            --purpose=PRIVATE_SERVICE_CONNECT
        




Replace the following:

  * `SUBNET_NAME`: the name to assign to the subnet.

  * `NETWORK_NAME`: the name of the VPC for the new subnet.

  * `REGION`: the region for the new subnet. This must be the same region as the service you are publishing.

  * `SUBNET_RANGE`: the IPv4 address range to use for the subnet—for example, `10.10.10.0/24`.




###  API 

Send a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).

  * To create an IPv4-only Private Service Connect subnet, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
        
        {
          "ipCidrRange": "SUBNET_RANGE",
          "name": "SUBNET_NAME",
          "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
          "purpose": "PRIVATE_SERVICE_CONNECT"
        }
        

  * To create a dual-stack Private Service Connect subnet, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
        
        {
          "ipCidrRange": "SUBNET_RANGE",
          "name": "SUBNET_NAME",
          "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
          "purpose": "PRIVATE_SERVICE_CONNECT",
          "stackType": "IPV4_IPV6",
          "ipv6AccessType": "INTERNAL"
        }
        

  * To create an IPv6-only Private Service Connect subnet, do the following:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
        
        {
          "name": "SUBNET_NAME",
          "network": "projects/PROJECT_ID/global/networks/NETWORK_NAME",
          "purpose": "PRIVATE_SERVICE_CONNECT",
          "stackType": "IPV6_ONLY",
          "ipv6AccessType": "INTERNAL"
        }
        




Replace the following:

  * `PROJECT_ID`: the project for the subnet.

  * `REGION`: the region for the new subnet. This must be the same region as the service you are publishing.

  * `SUBNET_RANGE`: the IPv4 address range to use for the subnet. For example, `10.10.10.0/24`.

  * `SUBNET_NAME`: the name to assign to the subnet.

  * `NETWORK_NAME`: the name of the VPC network for the new subnet.




## Configure firewall rules

Your network configuration must allow traffic from appropriate source IP address ranges to the instances or network endpoints that are configured as backends for your backend services. If your service uses health checks, you must also allow traffic from the health check probes to your backends.

You don't need to take any steps to allow traffic between a Private Service Connect endpoint or Private Service Connect backend and the associated service attachment, or between a service attachment and the associated load balancer. Endpoints, backends, and service attachments are [logical components that don't participate in the flow of traffic](https://docs.cloud.google.com/vpc/docs/private-service-connect-architecture).

If your backends are in a VPC network, you can use VPC ingress firewall rules or firewall policies to allow this traffic. For backends that are on-premises or in another cloud, configure that environment to allow traffic to the backends.

When you configure ingress firewall rules for backend services, the source of traffic depends on the type of load balancer that your service uses:

Category | Source of traffic to backends  
---|---  
**Passthrough load balancers:**

  * Internal passthrough Network Load Balancer
  * Internal protocol forwarding
  * Port mapping service

| The IP address ranges of the Private Service Connect (NAT) subnets associated with the service  
**Proxy load balancers:**

  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer
  * Regional internal proxy Network Load Balancer
  * Secure Web Proxy

| The IP address ranges of the associated proxy-only subnets  
**Services with health checks** | [The probe IP address ranges of your load balancer type](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges)  
  
## Publish a service

To publish a service, you create a service attachment. You can make the service available in one of two ways:

  * You can publish a service with automatic approval.
  * You can publish a service with explicit approval.



Create the service attachment in the same region as the service's load balancer.

Each service attachment can point to one or more Private Service Connect subnets, but a Private Service Connect subnet cannot be used in more than one service attachment.

If you want to view consumer connection information, you can enable PROXY protocol on supported services. Only enable PROXY protocol if it's supported by both your target service type (known issue) and the service's backend web server software. For information about the types of target services that support PROXY protocol, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility). For more information about PROXY protocol, see [Consumer connection information](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol).

The following sections provide instructions for publishing a service that's based on a load balancer. For information about creating a service attachment that refers to a Secure Web Proxy instance, see [Deploy Secure Web Proxy as a Private Service Connect service attachment](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment).

### Publish a service with automatic approval

Use these instructions to publish a service and automatically let any consumer connect to this service. If you want to approve consumer connections explicitly, see publishing a service with explicit approval.

When you publish a service, you create a service attachment. Service consumers use the service attachment details to connect to your service.

When you publish a service with automatic approval, the propagated connection limit applies to each consumer project that connects to your service attachment.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.subnetworks.use`
  * `compute.serviceAttachments.create`



**Roles**

See Roles for role information.

###  Console 

**Configure the service**

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click **Publish service**.

  4. In the **Target details** section, select **Load balancer**.

  5. Select a load balancer type.

  6. Select the internal load balancer that hosts the service that you want to publish. The network and region fields are populated with the details for the selected internal load balancer.

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can select an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

  7. If prompted, select the forwarding rule that is associated with the service that you want to publish.

  8. For **Service name** , enter a name for the service attachment.




**Configure a Private Service Connect subnet**

  1. Select or create one or more Private Service Connect subnets for the service. The list is populated with subnets from the selected internal load balancer's VPC network, including subnets that are shared with a service project through Shared VPC.

If your service attachment uses an internal load balancer with an IP address from a Shared VPC network, you must select a shared subnet from the same Shared VPC network.

If you want to add a new subnet, you can create one:

     1. Click **Subnets** , and then click **Reserve new subnet**.
     2. Enter a name and optional description for the subnet.
     3. Select a region for the subnet.
     4. Select an IP stack type.
     5. If you are creating an IPv4-only or dual-stack subnet, enter an IPv4 address range to use for the subnet.
     6. Click **Add**.
  2. Optional: If you want to assign two NAT IP addresses to each accepted consumer endpoint or backend, click **Allocated IPs per PSC endpoint** , and then select **2**.

Setting this value to **2** can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.




**Complete the configuration**

  1. If you want to view consumer connection information, select **Use Proxy Protocol**.
  2. Select **Automatically accept all connections**.
  3. If you want to disable [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation), clear the **Enable connection reconciliation** checkbox.
  4. Optional: Click **Advanced configuration** , and then do the following:

     1. If you want to configure a domain name, enter a domain name, including a trailing dot.

The recommended format for the domain name is `REGION.p.DOMAIN.`

You must own the domain name. For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).

     2. Enter a [propagated connections limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). If unspecified, the default value is `250`.

  5. Click **Add service**.




###  gcloud 

Use the [`gcloud compute service-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/create).
    
    
    gcloud compute service-attachments create ATTACHMENT_NAME \
        --region=ATTACHMENT_REGION \
        --target-service=TARGET_SERVICE \
        --connection-preference=ACCEPT_AUTOMATIC \
        --nat-subnets=PSC_SUBNET_LIST \
        [ --propagated-connection-limit=PROPAGATED_CONNECTION_LIMIT ] \
        [ --nat-ips-per-endpoint=NAT_IPS_PER_ENDPOINT ] \
        [ --enable-proxy-protocol ] \
        [ --domain-names=DOMAIN_NAME ]
    

Replace the following:

  * `ATTACHMENT_NAME`: the name to assign to the service attachment.

  * `ATTACHMENT_REGION`: the region for the new service attachment. This must be the same region as the IP address of the target forwarding rule.

  * `TARGET_SERVICE`: the URI of the forwarding rule that is associated with the service that you are publishing.

    * For Cross-region internal Application Load Balancers, use the following format: `projects/PROJECT_ID/global/forwardingRules/RULE_NAME`
    * For all other producer forwarding rules, use the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can specify the forwarding rule of an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

  * `PSC_SUBNET_LIST`: a comma-separated list of one or more subnet names to use with this service attachment.

If you're creating a service attachment with a forwarding rule that has an IP address from a Shared VPC network, use shared subnets from the same Shared VPC network. For each shared subnet, specify the full resource URI—for example, `--nat-subnets=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET`.

  * `PROPAGATED_CONNECTION_LIMIT`: the per-project [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). The default value is `250`.

  * `NAT_IPS_PER_ENDPOINT`: the number of NAT IP addresses to assign to each accepted consumer endpoint or backend.

Options are `1` or `2`. The default value is `1`. Setting this value to `2` can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.

  * `DOMAIN_NAME`: a DNS domain name for the service, including a trailing dot. Recommended format: `REGION.p.DOMAIN.`

For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).




###  API 

Send a `POST` request to the [`serviceAttachments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/insert).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/ATTACHMENT_REGION/serviceAttachments
    {
      "name": "ATTACHMENT_NAME",
      "connectionPreference": "ACCEPT_AUTOMATIC",
      "targetService": "TARGET_SERVICE",
      "enableProxyProtocol": false,
      "natIpsPerEndpoint": NAT_IPS_PER_ENDPOINT,
      "natSubnets": [
        "PSC_SUBNET_1_URI",
        "PSC_SUBNET_2_URI"
      ],
      "propagatedConnectionLimit": "PROPAGATED_CONNECTION_LIMIT",
      "domainNames": [
        "DOMAIN_NAME"
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project for the service attachment.

  * `ATTACHMENT_REGION`: the region for the new service attachment. This must be the same region as the IP address of the target forwarding rule.

  * `ATTACHMENT_NAME`: the name to assign to the service attachment.

  * `TARGET_SERVICE`: the URI of the forwarding rule associated with the service you are publishing.

    * For Cross-region internal Application Load Balancers, use the following format: `projects/PROJECT_ID/global/forwardingRules/RULE_NAME`
    * For all other producer forwarding rules, use the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can specify the forwarding rule of an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

  * `PSC_SUBNET_1_URI` and `PSC_SUBNET_2_URI`: the subnet URIs to use for this service attachment. You can specify one or more subnets by URI.

If you're creating a service attachment with a forwarding rule that has an IP address from a Shared VPC network, use shared subnets from the same Shared VPC network.

  * `NAT_IPS_PER_ENDPOINT`: the number of NAT IP addresses to assign to each accepted consumer endpoint or backend.

Options are `1` or `2`. The default value is `1`. Setting this value to `2` can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.

  * `DOMAIN_NAME`: a DNS domain name for the service, including a trailing dot. Recommended format: `REGION.p.DOMAIN.`

For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).

  * `PROPAGATED_CONNECTION_LIMIT`: the per-project [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). The default value is `250`.




### Publish a service with explicit approval

Use these instructions to publish a service if you want to explicitly approve consumers before they can connect to this service. If you want to approve consumer connections automatically, see publishing a service with automatic approval.

When you publish a service, you create a service attachment. Service consumers use the service attachment details to connect to your service.

Each service attachment has a [consumer accept list and a consumer reject list](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#consumer-lists). The consumer lists determine which endpoints can connect to the service. A given service attachment can accept or reject consumers based on one of the following types:

  * Project
  * VPC network
  * Private Service Connect endpoint



Each entry in the consumer lists must be of the same type. For example, a given service attachment can't accept some consumers based on project and some based on VPC network. Additionally, specifying consumers by folder is not supported.

If you add a value to both the accept list and the reject list, connection requests from that consumer are rejected.

To accept users based on individual Private Service Connect endpoints, publish a service with explicit approval, but don't add any values to the consumer lists. After a consumer connects to your service attachment, you can find the endpoint's ID-based URI by [describing the service attachment](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer#attachment-details) or asking the consumer to [describe the endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#endpoint-details). To accept the connection, [add the Private Service Connect endpoint's ID-based URI to your service's consumer accept list](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access).

If your consumer accept and reject lists refer to projects or individual endpoints, the propagated connection limit applies to consumer projects. If your consumer accept and reject lists refer to VPC networks, the propagated connection limit applies to consumer VPC networks.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.subnetworks.use`
  * `compute.serviceAttachments.create`



**Roles**

See Roles for role information.

###  Console 

**Configure the service**

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click **Publish service**.

  4. In the **Target details** section, select **Load balancer**.

  5. Select a load balancer type.

  6. Select the internal load balancer that hosts the service that you want to publish. The network and region fields are populated with the details for the selected internal load balancer.

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can select an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

  7. If prompted, select the forwarding rule associated with the service you want to publish.

  8. For **Service name** , enter a name for the service attachment.




**Configure a Private Service Connect subnet**

  1. Select or create one or more Private Service Connect subnets for the service. The list is populated with subnets from the selected internal load balancer's VPC network, including subnets that are shared with a service project through Shared VPC.

If your service attachment uses an internal load balancer with an IP address from a Shared VPC network, you must select a shared subnet from the same Shared VPC network.

If you want to add a new subnet, you can create one:

     1. Click **Subnets** , and then click **Reserve new subnet**.
     2. Enter a name and optional description for the subnet.
     3. Select a region for the subnet.
     4. Select an IP stack type.
     5. If you are creating an IPv4-only or dual-stack subnet, enter an IPv4 address range to use for the subnet.
     6. Click **Add**.
  2. Optional: If you want to assign two NAT IP addresses to each accepted consumer endpoint or backend, click **Allocated IPs per PSC endpoint** , and then select **2**.

Setting this value to **2** can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.




**Configure consumer access**

  1. If you want to view consumer connection information, select **Use Proxy Protocol**.
  2. To configure your consumer accept and reject lists, do one of the following.

     * To accept connections for selected projects, select **Accept connections for selected projects** , and then:

       1. For each project that you want to accept connections from, click **Add accepted project** , and then enter the following:

          * The project ID or project number of the project that you want to accept connections from.
          * A connection limit to specify the maximum number of endpoints from the specified project that can connect.
       2. Optional: For each project that you want to explicitly reject connections from, click **Add rejected project** , and then enter the project ID or project number.

     * To accept connections for selected networks, select **Accept connections for selected networks** , and then:

       1. For each VPC network that you want to accept connections from, click **Add accepted network** , and then enter the following:

          * The project ID or project number of the parent project of the network that you want to accept connections from.
          * The name of the network that you want to accept connections from.
          * A connection limit to specify the maximum number of endpoints from the specified network that can connect.
       2. Optional: For each network that you want to explicitly reject connections from, click **Add rejected network** , and then enter the ID or project number of the network's parent project and the network's name.

     * To accept connections for individual Private Service Connect endpoints, select **Accept connections for selected projects**. Don't add any values to the consumer accept list at this time. After a consumer requests a connection to your service, you can [add the endpoint to your consumer accept list](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access).




**Complete the configuration**

  1. Optional: If you want to disable [connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation), clear the **Enable connection reconciliation** checkbox.
  2. Optional: Click **Advanced configuration** , and then do the following:

     1. If you want to configure a domain name, enter a domain name, including a trailing dot.

The recommended format for the domain name is `REGION.p.DOMAIN.`

You must own the domain name. For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).

     2. Enter a [propagated connections limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). If unspecified, the default value is `250`.

  3. Click **Add service**.




###  gcloud 

Use the [`gcloud compute service-attachments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/create).
    
    
    gcloud compute service-attachments create ATTACHMENT_NAME \
        --region=ATTACHMENT_REGION \
        --target-service=TARGET_SERVICE \
        --connection-preference=ACCEPT_MANUAL \
        --consumer-accept-list=ACCEPTED_PROJECT_OR_NETWORK_1=LIMIT_1,ACCEPTED_PROJECT_OR_NETWORK_2=LIMIT_2 \
        --consumer-reject-list=REJECTED_PROJECT_OR_NETWORK_1,REJECTED_PROJECT_OR_NETWORK_2 \
        --nat-subnets=PSC_SUBNET_LIST \
        [ --propagated-connection-limit=PROPAGATED_CONNECTION_LIMIT ] \
        [ --nat-ips-per-endpoint=NAT_IPS_PER_ENDPOINT ] \
        [ --enable-proxy-protocol ] \
        [ --domain-names=DOMAIN_NAME ] \
        [ --reconcile-connections ]
    

Replace the following:

  * `ATTACHMENT_NAME`: the name to assign to the service attachment.

  * `ATTACHMENT_REGION`: the region for the new service attachment. This must be the same region as the IP address of the target forwarding rule.

  * `TARGET_SERVICE`: the URI of the forwarding rule that is associated with the service that you are publishing.

    * For Cross-region internal Application Load Balancers, use the following format: `projects/PROJECT_ID/global/forwardingRules/RULE_NAME`
    * For all other producer forwarding rules, use the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can specify the forwarding rule of an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

  * `ACCEPTED_PROJECT_OR_NETWORK_1` and `ACCEPTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URIs to accept. `--consumer-accept-list` is optional and can contain one or more projects or networks, but not a mix of both types.

  * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects or networks. The connection limit is the number of consumer endpoints or backends that can connect to this service. Each accepted project or network must have a connection limit configured.

  * `REJECTED_PROJECT_OR_NETWORK_1` and `REJECTED_PROJECT_OR_NETWORK_2`: the project IDs, project names, or network URIs to reject. `--consumer-reject-list` is optional and can contain one or more projects or networks, but not a mix of both types.

  * `PSC_SUBNET_LIST`: a comma-separated list of one or more subnet names to use with this service attachment.

If you're creating a service attachment with a forwarding rule that has an IP address from a Shared VPC network, use shared subnets from the same Shared VPC network. For each shared subnet, specify the full resource URI—for example, `--nat-subnets=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET`.

  * `PROPAGATED_CONNECTION_LIMIT`: the [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). The default value is `250`.

  * `NAT_IPS_PER_ENDPOINT`: the number of NAT IP addresses to assign to each accepted consumer endpoint or backend.

Options are `1` or `2`. The default value is `1`. Setting this value to `2` can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.

  * `DOMAIN_NAME`: a DNS domain name for the service, including a trailing dot. Recommended format: `REGION.p.DOMAIN.`

For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).




###  API 

Send a `POST` request to the [`serviceAttachments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/insert).

  * To publish a service and explicitly approve consumers based on project, send the following request:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/ATTACHMENT_REGION/serviceAttachments
        {
          "name": "ATTACHMENT_NAME",
          "region": "ATTACHMENT_REGION",
          "connectionPreference": "ACCEPT_MANUAL",
          "targetService": "TARGET_SERVICE",
          "enableProxyProtocol": false,
          "natIpsPerEndpoint": NAT_IPS_PER_ENDPOINT,
          "natSubnets": [
            "PSC_SUBNET_1_URI",
            "PSC_SUBNET_2_URI"
          ],
          "consumerRejectLists": [
            "REJECTED_PROJECT_1",
            "REJECTED_PROJECT_2"
          ],
          "consumerAcceptLists": [
            {
              "projectIdOrNum": "ACCEPTED_PROJECT_1",
              "connectionLimit": "LIMIT_1"
            },
            {
              "projectIdOrNum": "ACCEPTED_PROJECT_2",
              "connectionLimit": "LIMIT_2"
            }
          ],
          "propagatedConnectionLimit": "PROPAGATED_CONNECTION_LIMIT",
          "domainNames": [
            "DOMAIN_NAME"
          ]
        }
        

Replace the following:

    * `PROJECT_ID`: the project for the service attachment.

    * `ATTACHMENT_REGION`: the region for the new service attachment. This must be the same region as the IP address of the target forwarding rule.

    * `ATTACHMENT_NAME`: the name to assign to the service attachment.

    * `TARGET_SERVICE`: the URI of the forwarding rule associated with the service you are publishing.

      * For Cross-region internal Application Load Balancers, use the following format: `projects/PROJECT_ID/global/forwardingRules/RULE_NAME`
      * For all other producer forwarding rules, use the following format: `projects/PROJECT_ID/regions/RULE_REGION/forwardingRules/RULE_NAME`

[Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) can specify the forwarding rule of an internal load balancer that has an IP address from a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc#shared_vpc_networks). For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#shared-vpc).

    * `PSC_SUBNET_1_URI` and `PSC_SUBNET_2_URI`: the subnet URIs to use for this service attachment. You can specify one or more subnets by URI.

If you're creating a service attachment with a forwarding rule that has an IP address from a Shared VPC network, use shared subnets from the same Shared VPC network.

    * `NAT_IPS_PER_ENDPOINT`: the number of NAT IP addresses to assign to each accepted consumer endpoint or backend.

Options are `1` or `2`. The default value is `1`. Setting this value to `2` can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.

    * `REJECTED_PROJECT_1` and `REJECTED_PROJECT_2`: the project IDs or numbers of projects to reject. `consumerRejectLists` is optional and can contain one or more projects.

    * `ACCEPTED_PROJECT_1` and `ACCEPTED_PROJECT_2`: the project IDs or numbers of the projects to accept. `consumerAcceptLists` is optional and can contain one or more projects.

    * `LIMIT_1` and `LIMIT_2`: the connection limits for the projects. The connection limit is the number of consumer endpoints or backends that can connect to this service. Each accepted project must have a connection limit configured.

    * `PROPAGATED_CONNECTION_LIMIT`: the [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). The default value is `250`.
    * `DOMAIN_NAME`: a DNS domain name for the service, including a trailing dot. Recommended format: `REGION.p.DOMAIN.` For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).
  * To publish a service and explicitly approve consumers based on VPC network, send the following request:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/ATTACHMENT_REGION/serviceAttachments
        {
          "name": "ATTACHMENT_NAME",
          "region": "ATTACHMENT_REGION",
          "connectionPreference": "ACCEPT_MANUAL",
          "targetService": "TARGET_SERVICE",
          "enableProxyProtocol": false,
          "natIpsPerEndpoint": NAT_IPS_PER_ENDPOINT,
          "natSubnets": [
            "PSC_SUBNET_1_URI",
            "PSC_SUBNET_2_URI"
          ],
          "consumerRejectLists": [
            "projects/REJECTED_PROJECT_ID_1/global/networks/REJECTED_NETWORK_1",
            "projects/REJECTED_PROJECT_ID_2/global/networks/REJECTED_NETWORK_2"
          ],
          "consumerAcceptLists": [
            {
              "networkUrl": "projects/ACCEPTED_PROJECT_ID_1/global/networks/ACCEPTED_NETWORK_1",
              "connectionLimit": "LIMIT_1"
            },
            {
              "networkUrl": "projects/ACCEPTED_PROJECT_ID_2/global/networks/ACCEPTED_NETWORK_2",
              "connectionLimit": "LIMIT_2"
            }
          ],
          "propagatedConnectionLimit": PROPAGATED_CONNECTION_LIMIT,
          "domainNames": [
            "DOMAIN_NAME"
          ]
        }
        

Replace the following:

    * `REJECTED_PROJECT_ID_1` and `REJECTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to reject. `consumerRejectLists` is optional and can contain one or more networks.
    * `REJECTED_NETWORK_1` and `REJECTED_NETWORK_2`: the names of the networks that you want to reject.
    * `ACCEPTED_PROJECT_ID_1` and `ACCEPTED_PROJECT_ID_2`: the IDs of the parent projects of the networks that you want to accept. `consumerAcceptLists` is optional and can contain one or more networks.
    * `ACCEPTED_NETWORK_1` and `ACCEPTED_NETWORK_2`: the names of the networks that you want to accept.
    * `LIMIT_1` and `LIMIT_2`: the connection limits for the networks. The connection limit is the number of consumer endpoints or backends that can connect to this service. Each accepted project must have a connection limit configured.

    * `NAT_IPS_PER_ENDPOINT`: the number of NAT IP addresses to assign to each accepted consumer endpoint or backend.

Options are `1` or `2`. The default value is `1`. Setting this value to `2` can increase [the maximum number of simultaneous IPv4 connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections) that individual endpoints or backends can establish to your service.

    * `PROPAGATED_CONNECTION_LIMIT`: the [propagated connection limit](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#propagated-connection-limit). The default value is `250`.
    * `DOMAIN_NAME`: a DNS domain name for the service, including a trailing dot. Recommended format: `REGION.p.DOMAIN.` For more information, see [DNS configuration](https://docs.cloud.google.com/vpc/docs/dns-vpc-hosted-services#dns-configuration-producer).
  * To publish a service with connection reconciliation enabled, send a request that's similar to the previous requests, but include the following field: 
        
        {
          ...
          "reconcileConnections": true
          ...
        }
        




## View consumer connection information

For information about viewing consumer connection information by using PROXY protocol, see [Viewing consumer connection information](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#proxy-protocol).

## Manage requests for access to a published service

If you have a published service with explicit approval, you can accept or reject connection requests from consumer projects or networks. For more information, see [Manage requests for access to a published service](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#access).

You can also switch between automatic and explicit project acceptance for a published service. For more information, see [Change the connection preference for a published service](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#connection-pref)

## Add or remove subnets from a published service

You can add or remove subnets from a published service. For more information, see [Add or remove subnets from a published service](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#subnets).

## List published services

You can list all services.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.list`



**Roles**

See Roles for role information.

###  Console

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

The Private Service Connect service attachments are displayed.




###  gcloud 

Use the [`gcloud compute service-attachments list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/list).
    
    
    gcloud compute service-attachments list [--regions=REGION_LIST]
    

Replace `REGION_LIST` with a comma-separated list of one or more regions that you want to view service attachments for. For example, `us-central1` or `us-west1,us-central1`.

###  API 

To view all service attachments in a given region or in all regions, send a `GET` request to the [`serviceAttachments.list` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/list).

  * View all service attachments in a region:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments
        

  * View all service attachments in all regions:
        
        GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/aggregated/serviceAttachments
        

Replace the following:

    * `PROJECT_ID`: the project for the service attachment.

    * `REGION`: the region for the service attachment.

    * `ATTACHMENT_NAME`: the name of the service attachment.




## View details for a published service

You can view some configuration details, such as the service attachment URI that consumers need to connect to your service, in the Google Cloud console. To view all details, including the `pscConnectionId` and the ID-based endpoint URI (`endpointWithId`) values for the service attachment's consumers, use the Google Cloud CLI or send an API request.

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.get`



**Roles**

See Roles for role information.

###  Console 

To view details for a published service, do the following.

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to view.

The **Service attachment** field contains the service attachment URI.

  4. If your service attachment is configured to accept or reject individual endpoints, you can view connection requests by clicking **Awaiting approval** , **Accepted list** , or **Rejected list**. Details are displayed for each endpoint, including the **Endpoint ID** that you can use to accept or reject connections from individual Private Service Connect endpoints.




###  gcloud 

To view details for a published service, use the [`gcloud compute service-attachments describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/describe).

The `selfLink` field contains the service attachment URI. For each endpoint in the list of connected endpoints, the `endpointWithId` field contains the endpoint's ID-based URI that you can use to accept or reject connections from individual Private Service Connect endpoints.

If you include the `--show-nat-ips` flag, the `connectedEndpoints` list displays the NAT IP addresses for each endpoint or backend.
    
    
    gcloud compute service-attachments describe \
        ATTACHMENT_NAME --region=REGION \
        --show-nat-ips
    

Replace the following:

  * `ATTACHMENT_NAME`: the name of the service attachment.

  * `REGION`: the region for the service attachment.




###  API 

To view details for a published service, send a `GET` request to the [`serviceAttachments.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/get).

The `selfLink` field contains the service attachment URI. For each endpoint in the list of connected endpoints, the `endpointWithId` field contains the endpoint's ID-based URI that you can use to accept or reject connections from individual Private Service Connect endpoints.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project for the service attachment.

  * `REGION`: the region for the service attachment.

  * `ATTACHMENT_NAME`: the name of the service attachment.




## Delete a published service

You can delete a published service, even if there are consumer connections to the service attachment. Deleting the published service removes the service attachment only. The associated load balancer is not deleted. When you delete a published service, the following applies:

  * Traffic from [endpoints (based on forwarding rules)](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) is no longer sent to the load balancer.

  * Traffic from [backends (based on global external Application Load Balancers)](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services-controls) is sent to the load balancer until the load balancer is deleted.




#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `compute.serviceAttachments.delete`



**Roles**

See Roles for role information.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Published services** tab.

  3. Click the service that you want to delete.

  4. Click **Delete**.




###  gcloud 

Use the [`gcloud compute service-attachments delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments/delete).
    
    
    gcloud compute service-attachments delete \
        ATTACHMENT_NAME --region=REGION
    

###  API 

Send a `DELETE` request to the [`serviceAttachments.delete` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/delete).
    
    
    DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/serviceAttachments/ATTACHMENT_NAME
    

Replace the following:

  * `PROJECT_ID`: the project for the service attachment.

  * `REGION`: the region for the service attachment.

  * `ATTACHMENT_NAME`: the name of the service attachment.




## Known issues

### Health check failures with global access consumer endpoints

Consumers can connect a [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) endpoint to a published service that's not configured for global access. However, health checks don't work correctly in this configuration. As a result, traffic might be sent to unhealthy backends and dropped.

If you publish a service by using an internal passthrough Network Load Balancer or internal protocol forwarding (target instance), and your service is affected by this issue, do the following.

  * If you want to use global access, do the following: 
    1. [Enable global access for the load balancer's forwarding rule](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access).
    2. If the load balancer is managed by Google Kubernetes Engine, you must also update the corresponding Service manifest and apply it to your cluster. For more information about this GKE-specific configuration, see [Global access](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#global_access_internal_lb).
    3. Update any automation so that new producer load balancers that support global access Private Service Connect endpoints are configured for global access.
  * If you don't want to use global access, ask the consumer to [disable global access for the endpoint](https://docs.cloud.google.com/vpc/docs/manage-endpoints-published-services#disable-global-access).



Turning on global access for a published service doesn't interrupt network traffic.

### Health check failures with global access Private Service Connect NEGs

There is a known issue with consumer Private Service Connect NEGs that are configured for global access. A Private Service Connect NEG is configured for global access if it's associated with a [global backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service).

If a consumer connects a Private Service Connect NEG that is configured for global access to a producer load balancer, and the service producer disables global access for that load balancer, health checks don't work correctly. As a result, traffic might be sent to unhealthy backends and dropped.

If you publish a service by using an internal load balancer that supports global access, and your service is affected by this issue, do the following.

  * If you want to use global access, do the following: 
    1. [Enable global access](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules/update#--allow-global-access) for the load balancer's forwarding rule.
    2. If the load balancer is managed by Google Kubernetes Engine, you must also update the corresponding Service manifest and apply it to your cluster. For more information about this GKE-specific configuration, see [Global access](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#global_access_internal_lb).
    3. Update any automation so that new producer load balancers that support global access Private Service Connect NEGs are configured for global access.
  * If you don't want to use global access, ask the consumer to reconfigure the Private Service Connect NEG for regional access. To do this, the consumer must [remove their Private Service Connect NEG from the global backend service](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/remove-backend) and then [attach the NEG to a regional backend service](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/add-backend).



Turning on global access for a published service doesn't interrupt network traffic.

### Disconnections after upgrading the Google provider for Terraform

If you've used the Google provider for Terraform with versions earlier than 4.76.0 to create service attachments, don't upgrade to versions 4.76.0 through 4.81.x. When you run `terraform apply` after upgrading to versions 4.76.0 through 4.81.x, Terraform might unintentionally delete and recreate the service attachments and close existing Private Service Connect connections. Recreated service attachments don't automatically re-establish Private Service Connect connections.

If you upgrade to version 4.82.0 and then run `terraform apply`, your service attachments are not deleted, but the [reconcile connections](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation) setting is set to true. If the setting was previously set to false, some Private Service Connect connections might close.

  * **Upgrading to Google provider versions 4.76.0 through 4.81.x.** In this scenario, the output of `terraform plan` includes the following:
        
        -/+ resource "google_compute_service_attachment" "SERVICE_NAME" {
          ...
                ~ reconcile_connections = false -> true # forces replacement
          ...
        

**Caution:** If you ignore this warning and apply the changes, Terraform deletes and recreate the service attachment. All existing Private Service Connect connections are closed, and new connections are not automatically re-established.

Use the workaround to prevent this issue.

  * **Upgrading to Google provider versions 4.82.0.** In this scenario, the output of `terraform plan` includes the following:
        
        ~ reconcile_connections = false -> true
        

If you ignore this warning and apply the changes, Terraform updates the service attachment to turn on connection reconciliation. Depending on their connection status, changing from `false` to `true` might close some existing connections. For more information, see [Connection reconciliation](https://docs.cloud.google.com/vpc/docs/about-controlling-access-published-services#connection-reconciliation).

Use the workaround to prevent this issue.




#### Workaround

We recommend that you upgrade the [Google provider for Terraform to version 4.82.0 or later](https://registry.terraform.io/providers/hashicorp/google/latest). This version prevents the unintentional deletion and recreation of service attachments.

If you can't upgrade immediately, or if you can upgrade but you also want to prevent Terraform from changing the connection reconciliation setting, update your Terraform configuration to explicitly set the connection reconciliation setting.

  1. View the detailed configuration for the service attachment, and note the `reconcileConnections` setting.
         
         gcloud compute service-attachments describe SERVICE_NAME --region=REGION
         

The output includes the `reconcileConnections` field, which can be true or false.
         
         reconcileConnections: false
         

  2. Update your Terraform configuration file to explicitly use the same setting that is used on the service attachment.
         
         resource "google_compute_service_attachment" "SERVICE_NAME" {
           ...
           reconcile_connections    = false
         }
         

For an example configuration, see [Service Attachment Reconcile Connections](https://github.com/terraform-google-modules/docs-examples/blob/master/service_attachment_reconcile_connections/main.tf) on GitHub.




### TLS errors with PROXY protocol

If you publish a service with PROXY protocol enabled, but your target service type doesn't support PROXY protocol, consumers can connect to your service with endpoints. However, traffic doesn't flow through the connection, and workloads receive errors related to TLS.

To resolve this issue, update the service attachment to disable PROXY protocol.

For information about the types of target services that support PROXY protocol, see [Features and compatibility](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#features-compatibility).

## Troubleshooting

### Error when updating a service attachment

If you see the following error message when you update a service attachment, the accept list or the reject list might include deleted projects: `The resource PROJECT was not found`.

Remove the deleted projects from the service attachment configuration to resolve the issue.

  1. Use the `gcloud compute service-attachments describe` command to show the configuration of the service attachment that you want to modify.

     * To output the accept list in a format you can use later to update the service attachment, do the following:
           
           gcloud compute service-attachments describe ATTACHMENT_NAME \
               --region=REGION --flatten="consumerAcceptLists[]" \
               --format="csv[no-heading,separator='='](consumerAcceptLists.projectIdOrNum,consumerAcceptLists.connectionLimit)" \
               | xargs | sed -e 's/ /,/g'
           

The accept list output looks similar to the following:
           
           PROJECT_1=LIMIT_1,PROJECT_2=LIMIT_2,PROJECT_3=LIMIT_3
           

     * To output the reject list in a format you can use later to update the service attachment, do the following:
           
           gcloud compute service-attachments describe ATTACHMENT_NAME \
               --region=REGION \
               --format="value[delimiter=','](consumerRejectLists[])"
           

The reject list output looks similar to the following:
           
           PROJECT_1,PROJECT_2,PROJECT_3
           

  2. Edit the command output to remove any deleted projects from the accept list and the reject list.

  3. Update the service attachment to remove the deleted projects.

     * To update the accept list, do the following:
           
           gcloud compute service-attachments update ATTACHMENT_NAME \
               --region=REGION \
               --consumer-accept-list=UPDATED_ACCEPT_LIST
           

     * To update the reject list, do the following:
           
           gcloud compute service-attachments update ATTACHMENT_NAME \
               --region=REGION \
               --consumer-reject-list=UPDATED_REJECT_LIST
           




### Connectivity is not established

If a consumer has created an endpoint or backend that refers to your service attachment but connectivity is not established, check the service attachment's [connection status](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#connection-statuses). The connection status might indicate steps that you can take to resolve the issue.

### Consumer connections time out

If consumer connections time out, check if your service requires long-running connections. The TCP Established Connection Idle Timeout for Private Service Connect NAT is 20 minutes. If your service needs a longer timeout, you might need to make some configuration changes to help ensure that the connections don't time out. For more information, see [NAT specifications](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#nat-subnets-other).

### Propagated connection errors

For information about troubleshooting propagated connections, see [Troubleshoot Private Service Connect connection propagation errors](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshoot-psc-propagation-errors).

### Published service has performance issues or connection timeouts

If your published service has performance issues or intermittent connection timeouts, it might be due to dropped packets. You can investigate dropped packets by checking the metrics that are described in the following sections.

#### Dropped packets from consumers

The [`private_service_connect/producer/dropped_received_packets_count`](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/producer/dropped_received_packets_count) metric tracks packets from an endpoint or backend to a published service that are dropped because the endpoint or backend exceeded its maximum connections to the service.

If a published service reports values for this metric, consider the following solutions to address specific limits described in [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections):

  * Increase the capacity of your published service—for example, by adding more virtual machine (VM) instances or network endpoints.
  * For IPv4 connections, if the service attachment is configured with one NAT IP address per endpoint or backend (the default), do both of the following: 
    * [Update the service attachment](https://docs.cloud.google.com/vpc/docs/manage-private-service-connect-services#update-nat-ips-per-endpoint) to assign two NAT IP addresses per endpoint or backend.
    * Make sure that the producer backend VMs have sufficient vCPUs. Increasing the number of vCPUs in a backend VM can increase the per-backend connection limit. For specific limits, see [Maximum connections](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#max-connections). Increasing the number of vCPUs doesn't affect the maximum connections for [services that use Envoy proxies](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#envoy-lb).
  * Ask the service consumer to reduce the number of connections through their endpoint or backend.



#### Dropped packets to consumers

The [`private_service_connect/producer/dropped_sent_packets_count`](https://docs.cloud.google.com/vpc/docs/monitor-private-service-connect-connections#compute/private_service_connect/producer/dropped_sent_packets_count) metric tracks packets sent from a published service to an endpoint or backend that are dropped because Private Service Connect can't find a matching connection for response packets.

Private Service Connect only allows connections that are initiated from the consumer VPC network. When a consumer initiates a connection, the connection is tracked in order to match response packets from the published service with an existing connection. If Private Service Connect can't find a match for a response packet, the packet is dropped.

This might happen if a published service sends response packets after a connection has timed out. For information about avoiding issues with connections timing out, see [NAT specifications](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#nat-subnets-other).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
