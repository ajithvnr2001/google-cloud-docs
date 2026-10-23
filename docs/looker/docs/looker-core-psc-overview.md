---
url: https://docs.cloud.google.com/looker/docs/looker-core-psc-overview/
title: Use Private Service Connect with Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:15.325433+00:00
---

# Use Private Service Connect with Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-psc-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Use Private Service Connect with Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to access a private connections Looker (Google Cloud core) instance or connect a private connections Looker (Google Cloud core) instance to other internal or external services. In order to use Private Service Connect, your Looker (Google Cloud core) instance must meet the following criteria:

  * [Instance editions](https://docs.cloud.google.com/looker/docs/looker-core-overview#looker_\(google_cloud_core\)_editions) must be Enterprise (`core-enterprise-annual`) or Embed (`core-embed-annual`).
  * [Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) must be enabled upon instance creation.



Private Service Connect allows inbound access to Looker (Google Cloud core) using endpoints or backends. Network endpoint groups (NEGs), once exposed as Private Service Connect service producers, enable Looker (Google Cloud core) to access outbound on-premises resources, multi-cloud environments, VPC workloads, or internet services.

To learn more about Private Service Connect, watch the [What is Private Service Connect?](https://www.youtube.com/watch?v=JAFagcQBV08) and [Private Service Connect and Service Directory: A revolution to connect your application in Cloud](https://www.youtube.com/watch?v=TYumathiFRI) videos.

## Service attachment

When you [create a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc) that is enabled to use Private Service Connect, Looker (Google Cloud core) creates a service attachment for the instance automatically. A [_service attachment_](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services#service-attachments) is an attachment point that VPC networks use to access the instance. The service attachment has a URI, which is used for making connections. You can find that URI on the [**Details** tab](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab) of the instance configuration page of the Google Cloud console.

You next create a Private Service Connect backend that another VPC network uses to connect to the service attachment. This enables the network to access the Looker (Google Cloud core) instance.

### Updating your service attachment

To enable new features like global access and Google-managed certificates, your instance's inbound Private Service Connect endpoints or backends must point to an updated service attachment. See the [Migrating Private Service Connect connections to the new service attachment URI](https://docs.cloud.google.com/looker/docs/looker-core-psc-migration) documentation page for more information and instructions.

## Using global access

Looker (Google Cloud core) instances that use the updated Private Service Connect service attachment URI support global access. Global access lets you create a Private Service Connect endpoint in a different region from your Looker (Google Cloud core) instance. For example, if your instance is in `us-central1`, you can create a load balancer with a Private Service Connect network endpoint group (NEG) in `us-west1` to access the instance.

To enable this feature, select the **Enable global access** [on the forwarding rule](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access) for your Private Service Connect [backend or endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#specifications-global-access).

## Inbound access

**Note:** You use Private Service Connect for inbound access when your Looker (Google Cloud core) instance is configured to use private connections. Looker (Google Cloud core) instances that are configured to use [hybrid connections](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#private-ip-public-ip) use the [web URL](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) to gain inbound access.

[_Inbound_](https://docs.cloud.google.com/looker/docs/glossary#northbound-traffic) access concerns configuring routing from clients to Looker (Google Cloud core). Looker (Google Cloud core) deployed with Private Service Connect supports [backend](https://docs.cloud.google.com/vpc/docs/private-service-connect#backends) connections for inbound access.

![Private Service Connect lets you send traffic to endpoints and backends that forward the traffic to Looker \(Google Cloud core\).](https://docs.cloud.google.com/static/looker/docs/images/psc-backend.png)

Looker (Google Cloud core) Private Service Connect instances can be accessed by service consumers through an external regional application load balancer or privately through a Private Service Connect backend. However, Looker (Google Cloud core) supports a single custom domain, so inbound access to a Looker (Google Cloud core) instance must be either public or private, not both public and private.

### Backends

Backends are deployed by using [network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs), which let consumers direct public and private traffic to their load balancer before the traffic reaches a Private Service Connect service, and also offer certificate termination. With a load balancer, backends provide the following options:

  * Observability (every connection is logged)
  * [Cloud Armor integration](https://docs.cloud.google.com/armor/docs/cloud-armor-overview)
  * URL private labeling and client-side certificates
  * Request decoration (adding custom request headers)
  * [Response decoration (adding custom response headers)](https://docs.cloud.google.com/looker/docs/looker-core-psc-access#inject-custom-security-response-headers)

**Note:** For information about setting up inbound access using private networking, see the [Private inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access) documentation page. For information about setting up inbound access using hybrid networking, see the [Public inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access-public) documentation page.

### Using Google-managed certificates with a custom domain

You can use a Google-managed certificate for custom domains that use the `*.private.looker.app` format. To do this, configure your private DNS to point your custom domain (for example, `my-instance.private.looker.app`) to the IP address of your PSC endpoint.

Because the certificate for the `*.private.looker.app` domain is managed by Google, you don't need to create or manage your own certificates.

You can continue to use other custom domains, but you must manage and provide your own certificates for them. For more information, see the [Using a custom domain with Google-managed certificates](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain-google-managed-certs) documentation page.

## Access outbound services

Looker (Google Cloud core) acts as a service consumer when establishing communication to other services in your VPC, multi-cloud network, or the internet. Connecting to these services from Looker (Google Cloud core) is considered [_outbound traffic_](https://docs.cloud.google.com/looker/docs/glossary#southbound-traffic).

If you want to connect to an external service that uses the standard web protocol, HTTPS, with available ports 443 or 8443, you can use Looker (Google Cloud core)'s [controlled native egress](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#controlled-native-egress) and the [**Global FQDN**](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#global-fqdn) setting to set up your connection. However, if the external service uses a different protocol, that external service must be [published using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#set_up_for_external_services) to enable it to connect to your Looker (Google Cloud core) instance using [**Local FQDN**](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn).

To connect to [published services](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#local-fqdn), perform the following steps:

  1. Ensure that the service [is published](https://docs.cloud.google.com/vpc/docs/about-vpc-hosted-services). Some Google Cloud services may take care of this for you; for example, Cloud SQL offers a way to [create an instance with Private Service Connect enabled](https://docs.cloud.google.com/sql/docs/mysql/configure-private-service-connect). Otherwise, follow [the instructions for publishing a service by using Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer) and refer to the additional guidance in the [Looker (Google Cloud core) instructions](https://docs.cloud.google.com/looker/docs/looker-core-psc#set_up_psc_for_external_services).
  2. Specify the [outbound (egress) connection](https://docs.cloud.google.com/looker/docs/looker-core-create-psc#specify_southbound_connections) from Looker (Google Cloud core) to the service.



You can use hybrid connectivity NEGs or internet NEGs when accessing services with Private Service Connect:

![Private Service Connect connects Looker \(Google Cloud core\) to services through load balancers and hybrid or internet NEGs.](https://docs.cloud.google.com/static/looker/docs/images/psc-service-consumer.png)

  * A [hybrid connectivity NEG](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#regional-internal-https) provides access to private endpoints, such as on-premises or multi-cloud endpoints. A hybrid connectivity NEG is a combination of an IP address and port configured as a backend to a load balancer. It is deployed within the same VPC as the Cloud Router. This deployment enables services in your VPC to reach routable endpoints through hybrid connectivity, such as Cloud VPN or Cloud Interconnect.

  * An [internet NEG](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) provides access to public endpoints, for example, a GitHub endpoint. An internet NEG specifies an external backend for the load balancer. This external backend referenced by the internet NEG is accessible through the internet.




You can establish a outbound connection from Looker (Google Cloud core) to service producers in any region. For example, if you have Cloud SQL Private Service Connect instances in regions `us-west1` and `us-east4`, you can create a outbound connection from a Looker (Google Cloud core) Private Service Connect instance deployed in `us-central1`.

![](https://docs.cloud.google.com/static/looker/docs/images/psc-southbound-multi-region.png)

The two regional service attachments with unique domain names would be specified as follows. The `--region` flags refer to the region of the Looker (Google Cloud core) Private Service Connect instance, while the regions of the Cloud SQL instances are included in their service attachment URIs:
    
    
    gcloud looker instances update looker-psc-instance \
    --psc-service-attachment domain=sql.database1.com,attachment=projects/123/regions/us-west1/serviceAttachments/sql-database1-svc-attachment --region=us-central1 \
    --psc-service-attachment domain=sql.database2.com,attachment=projects/123/regions/us-east4/serviceAttachment/sql-database2-svc-attachment --region=us-central1
    

Outbound access to non-Google managed services requires that you enable [global access](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access) on the producer load balancer to allow inter-region communication.

## What's next

  * [Create a Looker (Google Cloud core) Private Service Connect instance](https://docs.cloud.google.com/looker/docs/looker-core-create-psc)
  * [Access a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access)
  * [Troubleshoot Looker (Google Cloud core) networking issues](https://docs.cloud.google.com/looker/docs/looker-core-networking-troubleshooting)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
