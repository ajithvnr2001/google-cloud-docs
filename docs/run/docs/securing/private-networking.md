---
url: https://docs.cloud.google.com/run/docs/securing/private-networking/
title: Private networking and Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:03.976405+00:00
---

# Private networking and Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/private-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Private networking and Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses configuration options for including Cloud Run resources in your private network. 

To get the most out of this content, you should have some familiarity with the following concepts:

  * Basic networking
  * Google Cloud [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/vpc) networks



To secure network traffic for their services and applications, many organizations use a private network on Google Cloud with perimeter controls to prevent data exfiltration. Your private network might have the following properties:

  * You might have a number of resources, such as VMs, sitting on one or more VPC networks.
  * These VMs might belong to many different projects, and they might be connected together with a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).
  * You might have on-premises workloads or workloads on other clouds connected to this environment using [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).
  * You might have enabled a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter to reduce the risk of data exfiltration.
  * You might have multiple private networks, one for each of several different environments, such as one for production, one for staging, and one for development.



Unlike VMs, Cloud Run resources are not associated with any particular VPC network by default. This page explains how to incorporate Cloud Run resources into your private network.

## Serverless networking narrative

To explore a range of common enterprise configurations for public and private networking, read our [Serverless networking narrative](https://services.google.com/fh/files/misc/serverless_networking_guide.pdf).

This starting point introduces the following basic-to-advanced Cloud Run scenarios:

  * Safely deploy a "Hello, World!" app that uses a custom domain
  * Develop enterprise applications and microservices
  * Access databases and file systems publicly or privately
  * Connect with SaaS providers
  * Apply security controls



See the list of corresponding [Terraform modules](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/blueprints/serverless/).

## Receive requests from your private network

Receiving requests from your private network requires configuration based on the following conditions:

  * Where the request comes from.
  * Whether the Cloud Run resource only allows requests from your private network.



For example, receiving requests from VPC networks might require different configuration than receiving requests from on-premises resources and other clouds.

### Receive requests from other Cloud Run resources or App Engine

When your _destination_ Cloud Run resource receives traffic from other Cloud Run resources or App Engine, and it uses the "internal" or "internal and load balancing" ingress setting, the traffic must use the VPC network to be considered internal.

To receive requests from other Cloud Run resources or App Engine, perform the following steps:

  1. Configure the _source_ resource to use either Direct VPC egress or a connector.

  2. Make sure traffic to Cloud Run routes through the VPC network by using one of the following options:

     * Configure the _source_ resource to [route all traffic](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress) through the VPC network and enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) on the subnet associated with Direct VPC egress or the connector.
     * Set up [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) or an internal Application Load Balancer to front your destination Cloud Run resource. With this configuration, you access Cloud Run by using internal IP addresses, so requests are routed through the VPC network.
     * Enable Private Google Access on the subnet associated with the _source_ resource and [configure DNS](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) to resolve `run.app` URLs to the `private.googleapis.com` (`199.36.153.8/30`) or `restricted.googleapis.com` (`199.36.153.4/30`) ranges. Requests to these ranges are routed through the VPC network.



### Receive requests from VPC networks

By default, only resources that have external IP addresses or use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) can directly access the internet and Google Cloud services such as Pub/Sub and Cloud Run. For other resources, there are a few options to enable the traffic path to Cloud Run:

  * The most direct path is to enable [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the subnets that host your resources. When Private Google Access is enabled, resources on the subnets can access your Cloud Run resources at the default `run.app` URL. Traffic from your VPC network to Cloud Run stays in Google's network. In that case, the IP range for requests sent to the Cloud Run resource is `0.0.0.0/32`. This means that in request log entries, the `remoteIp` attribute of the [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#httprequest) will be `0.0.0.0`.
  * If you need your Cloud Run resource (together with other Google APIs) to be accessible through an internal IP address in your VPC network, consider creating a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis) and [configuring a private DNS zone](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default) for `run.app`. With this configuration, resources in the VPC network can access Cloud Run resources at the default `run.app` URL through the Private Service Connect endpoint IP address.
  * If you need load balancing capabilities and controls, consider using an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless). With this approach, resources in the VPC network access your Cloud Run resources by using the URL associated with the internal Application Load Balancer.
  * If you want to expose your service to internal clients as a managed service and be able to control which projects can access it, you can host it with an internal Application Load Balancer and [publish the service by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer). Projects that need to consume the service can access it by using a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) or a [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).



Responses are returned by using the same path that the request went through.

#### Special considerations for Shared VPC

When using the `internal` setting with Cloud Run [ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress) to enforce that all traffic must come from your private network, Shared VPC traffic is only recognized as "internal" in the following situations:

  * The Cloud Run resource is running in the Shared VPC host project.

  * Shared VPC ingress: the Cloud Run resource is attached to a Shared VPC network. In this scenario, note the following considerations:

    * Only service revisions or Cloud Run instances that have configured [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) or that have configured a [Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors) to send traffic to the Shared VPC network will also accept traffic from that same Shared VPC network.

**Note:** We recommend that all active Cloud Run service revisions use the same Direct VPC egress or connector configuration to make sure that all traffic from the Shared VPC network is allowed.
    * Requests use different paths based on the traffic direction. Requests sent from Cloud Run to the Shared VPC network are routed by Direct VPC egress or the connector. However, requests sent from the Shared VPC network to Cloud Run use the standard ingress path.

    * To detach a Cloud Run resource from the Shared VPC network, redeploy without VPC network access, or with the resource configured to send traffic to a different VPC network.

  * You are using an internal Application Load Balancer to proxy traffic.

  * You have placed the Shared VPC host and all service projects inside the same [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter. To set up VPC Service Controls, see [Using VPC Service Controls (VPC SC)](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).




#### Special considerations for other VPC networks outside your project

When using the `internal` setting with Cloud Run [ingress controls](https://docs.cloud.google.com/run/docs/securing/ingress) to enforce that all traffic must come from your private network, traffic from other VPC networks outside your project is not recognized as "internal" except in the following situations:

  * VPC Service Controls is configured to allow the traffic with `run.googleapis.com` as a restricted service, and Private Google Access is enabled for the source subnet.
  * Your Cloud Run resource is [published](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) as a managed service by using Private Service Connect (requires an internal Application Load Balancer), and it is [accessed](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) from the other VPC network.



Peering with a VPC network that is outside of your project doesn't allow traffic to be recognized as "internal."

### Receive requests from other Google Cloud services

Requests to Cloud Run from Google Cloud services such as Pub/Sub stay within Google's network.

There are a few special considerations if you have configured Cloud Run ingress controls to only allow "internal" traffic:

  * Requests from BigQuery, Cloud Scheduler, Cloud Tasks, Dialogflow CX, Eventarc, Pub/Sub, [synthetic monitors (including uptime checks)](https://docs.cloud.google.com/monitoring/uptime-checks/introduction), and Workflows in the same project or VPC Service Controls perimeter are recognized as "internal."
  * Requests from Cloud Run or App Engine that are sent from within the same project or VPC Service Controls perimeter all require additional configuration before they are recognized as "internal." For details, see the Receive requests from other Cloud Run services or App Engine section.
  * If your chosen Google Cloud service is not able to access Cloud Run resources that have ingress set to `internal`, note that many services support authenticating to Cloud Run, such as [Pub/Sub](https://docs.cloud.google.com/run/docs/tutorials/pubsub#integrating-pubsub) (supports both `internal` and authentication), [API Gateway](https://docs.cloud.google.com/api-gateway/docs/securing-backend-services), and [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#cloud-run) (supports both `internal` and authentication). Depending on your security needs, it might be sufficient for the destination Cloud Run resource to require authentication instead of "internal" ingress.
  * Requests from Google Cloud services not mentioned previously are not recognized as internal and cannot be received by Cloud Run resources that have ingress set to `internal` or `internal-and-cloud-load-balancing`.



### Receive requests from on-premises resources or other clouds

There are multiple ways to privately receive requests from on-premises resources and other clouds.

  * **Basic configuration** : To have requests from on-premises resources and other clouds traverse your private network, configure [Private Google Access for on-premises hosts](https://docs.cloud.google.com/vpc/docs/private-google-access-hybrid).
  * **Make the Cloud Run resource accessible through an internal IP address** : To call Cloud Run resources using an internal IP address, create a [Private Service Connect endpoint to access Google APIs](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis), [configure a private DNS zone](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#configure-dns-default) for `run.app`, and [configure your on-premises network to access the endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-apis#on-premises). With this configuration, on-premises hosts can access Cloud Run resources at the default `run.app` URL through the Private Service Connect endpoint IP address.
  * **With load balancing capabilities** : If you need load balancing capabilities and controls, use an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless). For information about accessing internal Application Load Balancer from on-premises networks, see [Use Cloud VPN and Cloud Interconnect](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks#using-vpn-interconnect).
  * **Across administrative boundaries** : If you want to expose your service to internal clients as a managed service and be able to control which projects can access it, you can [publish the service by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) (requires an internal Application Load Balancer). To access the service from on-premises hosts, create a Private Service Connect endpoint and configure the on-premises network to access the endpoint. For more information, see [Access endpoints from hybrid networks](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#on-premises). Alternatively, you can use a [Private Service Connect backend](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends) with a load balancer. For information about accessing load balancers from on-premises networks, see the documentation for the load balancer that you're using--for example, for internal Application Load Balancers, see [Use Cloud VPN and Cloud Interconnect](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks#using-vpn-interconnect).



### Require requests to come from your private network

To prevent incoming traffic (ingress) from external sources, you specify a restrictive [ingress setting](https://docs.cloud.google.com/run/docs/securing/ingress#settings). The most restrictive ingress setting is `internal`. With ingress set to `internal`, your service only allows requests from your project, Shared VPC networks your project is attached to, and your VPC Service Controls perimeter. There are some limitations with this setting depending on where the requests come from. To learn about these limitations and how to navigate them, see the section Receive requests from your private network.

You can specify the ingress setting for each Cloud Run resource, or enforce the use of your preferred ingress setting for all Cloud Run resources in your organization.

  * **To specify the ingress setting for each Cloud Run resource** : See [Setting ingress](https://docs.cloud.google.com/run/docs/securing/ingress#setting_ingress).
  * **To enforce a particular ingress setting for all Cloud Run resources in your project, folder, or organization** : Configure the `run.allowedIngress` organization policy constraint. To learn how, see [Customizing policies for list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).



## Send requests to your private network

If your Cloud Run resource needs to access a resource on your private network, you configure a path for private requests to your network. The configuration depends on the final destination of the request.

### Send requests to your VPC network

To send requests to a VPC network, you must configure Direct VPC egress or a Serverless VPC Access connector. [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc). Review [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing) to understand costs.

When Direct VPC egress or connectors are configured, the following considerations apply by default:

  * All DNS queries are sent to the DNS server configured for the VPC network associated with your VPC network egress setup.

  * Requests to internal IP addresses are routed to the VPC network by using either Direct VPC egress or a connector. Requests to public destinations continue to be routed directly to the internet, unless your [egress setting](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress) is configured otherwise.




With requests routed using Direct VPC egress or connectors, responses return using the path that the request went through. Requests _from_ your VPC network to Cloud Run are enabled by using other technologies and are not routed through Direct VPC egress or connectors, and responses to those requests are returned using the same path. To learn more about sending requests from your VPC network to Cloud Run, see Receive requests from VPC networks.

#### Sending requests to a VPC network outside of your project

To send requests to a VPC network outside of your project:

  1. For Shared VPC users, see [Connect to a Shared VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc).
  2. For other VPC networks, configure Direct VPC egress or a connector to connect to a VPC in your project. 
     * **Peered VPC networks:** To send to a VPC that is peered to a VPC that uses VPC network egress, no additional configuration is required. However, the VMs in the subnet hosting VPC network egress must be able to reach the target VPC network.
     * **Other VPC networks:** For VPC networks outside of your project that are not part of the same Shared VPC environment or peered to your project VPC network, configure [Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services) after setting up VPC network egress.



### Send requests to other Cloud Run resources and Google Cloud services

Requests from one Cloud Run resource to another or to other Google Cloud services stay within Google's internal network and are subject to VPC Service Controls.

For requests to Cloud Run resources with restrictive ingress settings, additional configuration is required. See Receive requests from other Cloud Run resources or App Engine.

### Send requests to on-premises resources and other clouds

To send requests to on-premises resources and other clouds through your private network, you must do the following:

  1. Make sure your VPC network is configured to privately route your traffic to the destination, such as through a VPN tunnel.
  2. Configure your service to send requests to your VPC network.
  3. Require that all requests go to your VPC network.



### Require that all requests go to your VPC network

To require that all requests from your Cloud Run resource go to your VPC network, specify the `all-traffic` VPC network [egress setting](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress). You can specify the egress setting for each Cloud Run resource that uses VPC network egress, or you can enforce the use of your preferred egress setting for all Cloud Run resources in your project, folder, or organization.

This is useful in the following situations:

  1. You want to set up a [static outbound IP address](https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip) for your Cloud Run resource.
  2. You want to apply firewall rules for all egress from a Cloud Run resource.
  3. You want to send requests to on-premises resources and other clouds through your private network.



If your Cloud Run resource makes requests to final destinations outside of your VPC network, requiring that all requests go to your VPC network increases bandwidth use on configured Serverless VPC Access connectors and might increase costs accordingly. Connectors automatically scale out when traffic increases, but don't scale in if traffic decreases. Review [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing) to understand costs.

  * **To specify the egress setting for individual Cloud Run resources** : see [Control egress service traffic](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#egress-service).
  * **To enforce a particular egress setting for all Cloud Run resources in your project, folder, or organization** : configure the `run.allowedVPCEgress` organization policy constraint. To learn how, see [Customizing policies for list constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#list_constraints).



## Additional controls

  * **Perimeter controls** : To reduce the risk of data exfiltration for a group of resources, place them within a context-aware perimeter using VPC Service Controls. 
    * To understand VPC Service Controls, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
    * To get started, see the Cloud Run guide [Using VPC Service Controls (VPC SC)](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).
    * To understand costs, review [pricing](https://cloud.google.com/vpc-service-controls/pricing).
  * **Granular controls** : To control access for traffic from a specific resource within your private network, such as a specific Cloud Run resource or Compute Engine virtual machine, use service accounts to control permissions and authentication. 
    * To understand service accounts, see [What are service accounts?](https://docs.cloud.google.com/iam/docs/service-account-overview#what-are-service-accounts)
    * To get started, see the Cloud Run [authentication guides](https://docs.cloud.google.com/run/docs/authenticating/overview).



## What's next

To learn more about delivering low latency and high throughput using a direct network path, see [Direct VPC egress with a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
