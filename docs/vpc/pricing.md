---
url: https://docs.cloud.google.com/vpc/pricing/
title: Virtual Private Cloud pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:43:26.513821+00:00
---

# Virtual Private Cloud pricing | Google Cloud

> Source: https://docs.cloud.google.com/vpc/pricing/

Page Contents




## Virtual Private Cloud pricing

This page describes the networking pricing for resources in Virtual Private Cloud (VPC) networks.

For pricing for other Google Cloud products, see [All networking pricing](https://cloud.google.com/vpc/network-pricing).

## 

General network pricing information

### 

Data transfer

Data transfer can be traffic coming into a Google Cloud resource (e.g. VM), leaving Google Cloud region out into the internet, or in between two resources within Google Cloud.

A region is a set of buildings operated by Google in a geographic location, such as a data center campus. Traffic can travel as follows:

  * Within the set of buildings at the location, which always used Google's network (intra-zone and intra-region pricing)
  * To another building operated by Google in another location, which always used Google's network (inter-region pricing)
  * To a location not operated by Google over a Cloud Interconnect connection (Cloud Interconnect pricing)
  * To a location not operated by Google  _not_ over a Cloud Interconnect connection (internet data transfer out pricing)



### 

Premium Tier

The [Network Service Tiers Premium Tier](https://cloud.google.com/network-tiers/docs/overview#premium_tier) leverages Google's premium backbone to carry traffic to and from your external users. The public internet is usually only used between the user and the closest Google network ingress point.

### 

Standard Tier

The [Network Service Tiers Standard Tier](https://cloud.google.com/network-tiers/docs/overview#standard_tier) leverages the public internet to carry traffic between your services and your users. While using the public internet provides a lower quality of service, it is more economical than Premium Tier.

## 

Inbound data transfer pricing

Traffic type| Price  
---|---  
Inbound data transfer| No charge for inbound data transfer. However there may be a charge for resource that processes data. Services that process inbound data are as follows:

  * [Load balancers](https://cloud.google.com/vpc/network-pricing#lb)
  * [Cloud NAT](https://cloud.google.com/nat/pricing)
  * [Protocol forwarding](https://cloud.google.com/vpc/network-pricing#pf)

Responses to requests count as data transfer out and are charged.  
  
## 

VM-VM data transfer pricing within Google Cloud

This section covers traffic that leaves a Google Cloud VM and travels to another Google Cloud VM. The cost is attributed to the project of the VM that is sending the traffic. This pricing affects Compute Engine VMs, Google Kubernetes Engine (GKE) nodes, and VMs running App Engine flexible environment.

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

  


### 

Intra-zone/Inter-zone data transfer

VM-to-VM data transfer when the source and destination VM are in different zones of the same Google Cloud region

Traffic type| Price  
---|---  
Data transfer to the same Google Cloud zone when using the  _internal_ IPv4 addresses or any IPv6 addresses within the same VPC network1| No charge  
Data transfer to a different Google Cloud zone in the same Google Cloud region when using the internal or external IP addresses within the same VPC network1 (per GiB)_Note: All traffic to and from external IPv4 leaves the zone - regardless of the destination._|  $0.01  
Data transfer to the same or different Google Cloud zone when using external IPv4 addresses or external IPv6 addresses between different VPC networks.| Internet data transfer rates (see below)  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

1 The prices are used regardless of network or subnet. The price for traffic within a zone using internal IP addresses is the same even if the traffic is to a different subnet or network. The price on traffic between zones in the same region is the same if the two instances are in the same subnet, different subnets, or different networks. Pricing is the same whether the instances are in a VPC network or a legacy network.

### 

Inter-region data transfer

VM-to-VM data transfer when the source and destination VMs are in different Google Cloud regions. All prices are per GiB in USD

Location of VM or Google Cloud service| North America| Europe| Asia3| Indonesia| Oceania2| Middle East| South America| Africa  
---|---|---|---|---|---|---|---|---  
**North America**|  $0.02| $0.05| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Europe**|  $0.05| $0.02| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Asia****3**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Indonesia**|  $0.10| $0.10| $0.10| N/A| $0.08| $0.11| $0.14| $0.14  
**Oceania****2**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Middle East**|  $0.11| $0.11| $0.11| $0.11| $0.11| $0.08| $0.14| $0.11  
**South America**|  $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14  
**Africa**|  $0.11| $0.11| $0.11| $0.14| $0.14| $0.11| $0.14| $0.08  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

2 Oceania includes Australia, New Zealand, and surrounding Pacific Ocean islands such as Papua New Guinea and Fiji. This region excludes Hawaii.

3 Includes all regions in Asia except Indonesia.

## 

VM-to-Google service

This section covers traffic that leaves a Google Cloud VM and travels to a Google service. The cost is attributed to the project of the VM that is sending the traffic. This pricing affects Compute Engine VMs, Google Kubernetes Engine nodes, and VMs running App Engine flexible environment.

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

Traffic type| Price  
---|---  
Data transfer to specific Google products such as Gmail, YouTube, Google Maps, [DoubleClick](https://developers.google.com/authorized-buyers/rtb/peer-guide#trading_locations), and Google Drive, whether from a VM in Google Cloud with an external IP address or an [internal IP address.](https://cloud.google.com/compute/docs/private-google-access/private-google-access)| No charge  
Data transfer to a different Google Cloud service within the same region using an external IP address or an [internal IP address](https://cloud.google.com/compute/docs/private-google-access/private-google-access), except for Memorystore for Redis, Filestore, GKE, and Cloud SQL.| No charge  
Data transfer from Compute Engine and GKE to [Cloud CDN](https://cloud.google.com/cdn/docs) and [Media CDN](https://cloud.google.com/media-cdn/docs).| No charge (cache fill might apply for Cloud CDN).  
Data transfer to [Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis), [Filestore](https://cloud.google.com/filestore/docs), [Cloud SQL](https://cloud.google.com/sql/docs), and [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs) within the same region is priced the same as VM-to-VM traffic.| [VM-VM data transfer pricing within Google Cloud](https://docs.cloud.google.com/vpc/pricing#egress-within-gcp)  
Data transfer to a Google Cloud service in a different region.| [VM-VM data transfer pricing within Google Cloud](https://docs.cloud.google.com/vpc/pricing#egress-within-gcp)  
For Spanner network pricing, see [Spanner pricing](https://cloud.google.com/spanner/pricing#network).  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Internet data transfer rates

### 

Premium Tier pricing

Premium Tier is the default tier for all Google Cloud data transfer. To use Standard Tier, you must specify it explicitly.

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

**Important:** Starting **February 1, 2024** , we'll increase the price for some SKUs for Premium Tier internet data transfer out. For more information, see [Announcement of pricing change for data transfer](https://cloud.google.com/vpc/pricing-announce).

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Item| Price  
---|---  
Network (data transfer out) TO North America (per GiB in USD)| 0 gibibyte to 1 gibibyte$0.00 (Free) / 1 gibibyte, per 1 month / account1 gibibyte to 1,024 gibibyte$0.12 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.11 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Network (data transfer out) TO Europe (per GiB in USD)| 0 gibibyte to 1 gibibyte$0.00 (Free) / 1 gibibyte, per 1 month / account1 gibibyte to 1,024 gibibyte$0.12 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.11 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.085 / 1 gibibyte, per 1 month / account  
Network (data transfer out) TO Asia Excl Korea, Indonesia (per GiB in USD)| 0 gibibyte to 1 gibibyte$0.00 (Free) / 1 gibibyte, per 1 month / account1 gibibyte to 1,024 gibibyte$0.12 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.11 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.085 / 1 gibibyte, per 1 month / account  
Network (data transfer out) TO Australia, Indonesia, Korea, South America, Saudi Arabia (per GiB in USD)| 0 gibibyte to 1,024 gibibyte$0.19 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.18 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.15 / 1 gibibyte, per 1 month / account  
Network (data transfer out) TO Middle East excl Saudi Arabia, Africa (per GiB in USD)| 0 gibibyte to 1 gibibyte$0.00 (Free) / 1 gibibyte, per 1 month / account1 gibibyte to 1,024 gibibyte$0.15 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.13 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.11 / 1 gibibyte, per 1 month / account  
Network (data transfer out) TO China destinations (excluding Hong Kong) (per GiB in USD)| 0 gibibyte to 1,024 gibibyte$0.23 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.22 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.20 / 1 gibibyte, per 1 month / account  
Network (data transfer in)| Free  
  
  
**Note:** The monthly usage is counted by each SKU, while the "Wordwide Destinations" may contain multiple SKUs. For more information, see [Google Cloud SKUs](https://cloud.google.com/skus/?currency=USD&filter=compute%20engine%20network%20google%20egress).

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

*These rates do not apply for [Cloud CDN](https://cloud.google.com/cdn), [CDN Interconnect](https://cloud.google.com/interconnect/docs/how-to/cdn-interconnect), [Carrier Peering](https://cloud.google.com/interconnect/docs/how-to/carrier-peering), [Direct Peering](https://cloud.google.com/interconnect/docs/how-to/direct-peering), and [Cloud Interconnect](https://cloud.google.com/interconnect/docs) traffic. Instead, see pricing for [Cloud CDN](https://cloud.google.com/cdn/pricing), [CDN Interconnect](https://cloud.google.com/interconnect/docs/how-to/cdn-interconnect#pricing), [Carrier Peering](https://cloud.google.com/interconnect/docs/how-to/carrier-peering#pricing), [Direct Peering](https://cloud.google.com/interconnect/docs/how-to/direct-peering#pricing), or [Cloud Interconnect](https://cloud.google.com/interconnect/pricing).

### 

Standard Tier pricing

Data transfer out pricing is  _per GiB_ delivered. Pricing is based on source geolocation of traffic. Ingress pricing is still free. [Always Free usage limits](https://cloud.google.com/free/docs/gcp-free-tier#always-free-usage-limits) do  _not_ apply to Standard Tier.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Item| Price (USD)  
---|---  
Standard Tier Price| 0 gibibyte to 200 gibibyte$0.00 (Free) / 1 gibibyte, per 1 month / account200 gibibyte to 10,240 gibibyte$0.085 / 1 gibibyte, per 1 month / account10,240 gibibyte to 153,600 gibibyte$0.065 / 1 gibibyte, per 1 month / account153,600 gibibyte and above$0.045 / 1 gibibyte, per 1 month / account  
  
Contact sales for pricing beyond 500 TiB.

## 

Cloud Number Registry

Pricing for Cloud Number Registry (preview) will be published when the product is generally available.

## 

Internal IP address pricing

There is no charge for static or ephemeral internal IP addresses.

## 

External IP address pricing

You are charged for static and ephemeral external IP addresses according to the following table.

If you reserve a static external IP address and do not assign it to a resource such as a VM instance or a forwarding rule, you are charged at a higher rate than for static and ephemeral external IP addresses that are in use.

You are not charged for [static external IP addresses](https://cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static) that are assigned to forwarding rules.

You are not charged for external IPv6 address ranges that are [assigned to subnets](https://cloud.google.com/vpc/docs/create-modify-vpc-networks#subnet-enable-ipv6) or for external IPv6 addresses that are [assigned to VM instances](https://cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address). You are not charged for [static regional IPv6 addresses](https://cloud.google.com/vpc/docs/reserve-static-external-ip-address#regional-ext-ipv6) ([Preview](https://cloud.google.com/products#product-launch-stages)).

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Static IP address (assigned but unused)| $0.01 / 1 hour, per 1 month / account  
  
HourlyHourly

MonthlyMonthly

Type| Price (USD)  
---|---  
Static and ephemeral IP addresses in use on **standard VM instances**|  $0.005 / 1 hour, per 1 month / account  
Static and ephemeral IP addresses in use on **preemptible and Spot VM instances**|  $0.0025 / 1 hour  
Static and ephemeral IP addresses used by [Cloud NAT ](https://cloud.google.com/nat/docs).| $0.005 / 1 hour  
Static and ephemeral IP addresses attached to forwarding rules, or used as a public IP for a [Cloud VPN ](https://cloud.google.com/vpn/docs)tunnel.| No Charge  
  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

In use or not

Google Cloud considers a static external IP address as in use if it is associated with a VM instance whether the instance is running or stopped. If the instance is deleted or if the IP address is dissociated from the instance, Google Cloud considers the static IP address as not in use.

For an ephemeral IP address, Google Cloud considers the address as in use only when the associated VM instance is running. When the instance is stopped or deleted, Google Cloud releases the ephemeral IP address and no longer considers it as in use.

You can check whether a static external IP address is in use by making a gcloud compute addresses list request. This command returns a list of static external IP addresses and their statuses:

  * 


Loading...

gcloud compute addresses list

 _content_copy_

NAME| REGION| ADDRESS| STATUS  
---|---|---|---  
address-1| | 130.211.8.68| IN_USE  
address-2| | 35.186.217.84| RESERVED  
  
In this example, IPv4 address-1 is in use while IPv4 address-2 is reserved but not being used. Both addresses are charged according to the [External IP address pricing](https://docs.cloud.google.com/vpc/pricing#ipaddress) table in this document.

**Note:** If the same IP address is assigned to more than one forwarding rule, Google Cloud counts and adds each usage of the address towards the **IN_USE_ADDRESSES** quota rather than a unique count of IP address objects that are used.

## 

Composite Health

There is no additional charge for using [Composite Health.](https://docs.cloud.google.com/vpc/docs/about-composite-health) However, you are charged for resources and network traffic in your VPC network. Additionally, [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) applies to logging created by Composite Health.

## 

Firewall rules

For Cloud Next Generation Firewall pricing, see the [Cloud NGFW pricing page](https://cloud.google.com/firewall/pricing).

## 

Hybrid Subnets

Using a [Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets) are charged per subnet according to the following table. Please note that pricing will adjust to $0.315/hour per subnet in the next couple of months.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Dublin (europe-west7)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * Oklahoma (us-central2)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Item| Price (USD)  
---|---  
Per subnet with the attribute Hybid subnet enabled.| $0.00 (Free) / 1 hour  
  
## 

Private Service Connect

The costs associated with Private Service Connect vary depending on the configuration.

### 

Consumer charges

Using a Private Service Connect endpoint (forwarding rule) to access Google APIs

HourlyHourly

MonthlyMonthly

Item| Price per hour (USD)| Price per GiB processed, inbound and outbound data transfer  
---|---|---  
Private Service Connect endpoint (forwarding rule) used to [access Google APIs](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis)| $0.01 / 1 hour| No data charge  
Private Service Connect endpoint (forwarding rule) to access the regional endpoints of Google APIs| $0.01 / 1 hour| [Consumer data processing](https://docs.cloud.google.com/vpc/pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://docs.cloud.google.com/vpc/pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect endpoints.Consumer-to-producer traffic is billed to the project of the consumer resource originating the traffic.Producer-to-consumer traffic is billed to the project containing the Private Service Connect endpoint (forwarding rule).For endpoints with [global access](https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access), when the endpoint is accessed by resources in other regions, [inter-regional data transfer](https://docs.cloud.google.com/vpc/pricing#egress-within-gcp) charges also apply to that traffic.  
  
Using a Private Service Connect backend (load balancer) to access Google APIs

[Private Service Connect backends](https://cloud.google.com/vpc/docs/private-service-connect-backends) use a load balancer to access Google APIs. All load balancer pricing applies. Traffic to Private Service Connect NEGs that is directed to Google APIs incurs load balancing charges for  _data processed by load balancer_. However, there is no Private Service Connect charge for data transfer traffic between the Private Service Connect NEG and Google APIs.

For pricing information for your load balancer, see pricing for [global external Application Load Balancers](https://docs.cloud.google.com/vpc/pricing#lb) or [internal Application Load Balancers](https://docs.cloud.google.com/vpc/pricing#internal-https-lb).

**Note:** Private Service Connect backends were previously referred to as Private Service Connect endpoints with consumer HTTP(S) service controls.

### 

Using a Private Service Connect endpoint (forwarding rule) to access a published service

HourlyHourly

MonthlyMonthly

Item| Price per hour (USD)| Price per GiB processed, inbound and outbound data transfer  
---|---|---  
Private Service Connect endpoint (forwarding rule)  
| $0.01 / 1 hour| [Consumer data processing](https://docs.cloud.google.com/vpc/pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://docs.cloud.google.com/vpc/pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect endpoints.Consumer-to-producer traffic is billed to the project of the consumer resource originating the traffic.Producer-to-consumer traffic is billed to the project of the consumer resource receiving the traffic.For endpoints with [global access](https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access), when the endpoint is accessed by resources in other regions, [inter-regional data transfer](https://docs.cloud.google.com/vpc/pricing#egress-within-gcp) charges also apply to that traffic.  
  
**Note:** For endpoints with global access, the service producer project is not charged inter-regional data transfer even if service consumer resources are accessing the endpoint from other regions.

Private Service Connect automatically creates a Service Directory namespace to register endpoints in. A single default namespace is used for endpoints in the same region of a project unless you explicitly create additional namespaces. For more information about Service Directory pricing, see [Service Directory pricing.](https://cloud.google.com/service-directory/pricing)

Using a Private Service Connect backend (load balancer) to access a published service

[Private Service Connect backends](https://cloud.google.com/vpc/docs/private-service-connect-backends) use a load balancer to access published services. All load balancer pricing applies. Traffic between Private Service Connect NEGs and Private Service Connect published services incurs both load balancing charges for  _data processed by load balancer_ and Private Service Connect charges data transfer traffic between the NEG and the published service.

The following table summarizes the applicable charges for this configuration.

Item| Price (USD)  
---|---  
Private Service Connect endpoint (load balancer) [used to access services in another VPC network](https://cloud.google.com/vpc/docs/configure-private-service-connect-services-controls)| All [global external Application Load Balancer](https://docs.cloud.google.com/vpc/pricing#lb) or [internal Application Load Balancer](https://docs.cloud.google.com/vpc/pricing#internal-https-lb) pricing applies  
  
Traffic between a Private Service Connect NEG and the published service| [Consumer data processing](https://docs.cloud.google.com/vpc/pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://docs.cloud.google.com/vpc/pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect backends.Consumer-to-producer traffic is billed to the project of the consumer resource originating the traffic.Producer-to-consumer traffic is billed to the project of the consumer resource receiving the traffic.  
  
Using a Private Service Connect interface for access to a producer or consumer VPC network

Item| Price (USD)| Price per GB processed, data transfer in and out (USD)  
---|---|---  
[Private Service Connect interface](https://cloud.google.com/vpc/docs/about-private-service-connect-interfaces) used for access to a producer or consumer VPC network| No hourly charge| For both consumer-to-producer and producer-to-consumer traffic, [consumer data processing](https://docs.cloud.google.com/vpc/pricing#psc-consumer-data-processing) charges apply and are charged to the consumer.For consumer-to-producer inter-region traffic, [inter-region data transfer](https://docs.cloud.google.com/vpc/pricing#inter-region-data-transfer) charges also apply and are charged to the consumer.  
  
Service Directory

Private Service Connect automatically creates a Service Directory namespace to register endpoints when [accessing Google APIs](https://cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#service-directory) or when [accessing published services](https://cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer). A single default Service Directory namespace is created for Private Service Connect endpoints in the same region of a project. For more information about Service Directory pricing, see [Service Directory pricing](https://cloud.google.com/service-directory/pricing).

### 

Consumer data processing

Private Service Connect consumers are charged consumer data processing according to the following table. Consumer data processing is charged inbound and outbound.

Monthly usage| Price (USD)  
---|---  
Price (USD)| 0 gibibyte to 1 pebibyte$0.01 / 1 gibibyte, per 1 month / account1 pebibyte to 5 pebibyte$0.006 / 1 gibibyte, per 1 month / account5 pebibyte and above$0.004 / 1 gibibyte, per 1 month / account  
  
### 

Producer charges

Charges to publish a managed service by using a Private Service Connect service attachment

There are no Private Service Connect hourly or data transfer charges for publishing services through service attachments. Producers are charged for any load balancing charges incurred on the load balancer that is published to consumers.

**Note:** If resources use an endpoint with global access to access a published service from a different region than the service, the service producer project is not charged inter-regional data transfer. For information about service consumer project charges, see [Using a Private Service Connect endpoint (forwarding rule) to access a published managed service.](https://docs.cloud.google.com/vpc/pricing#psc-forwarding-rule-service)

Deploying a service by using service connection maps

When you deploy a service by using service connection maps, there are no producer charges for the deployment of service connection maps themselves. However, the consumer is charged for the following:

  * Resources that are deployed into the consumer project through service connectivity automation
  * [Using a Private Service Connect endpoint to access a published service](https://docs.cloud.google.com/vpc/pricing#psc-forwarding-rule-service)



## 

Private services access

When you [create a private services access connection](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection), there are no hourly or data charges for the connection itself. However, you are charged for the following:

  * Resources that you provision in the service producer's network
  * Data transfer traffic from your VMs to the service producer's network



## 

Serverless VPC Access

Serverless VPC Access is priced as follows.

Resource| Price  
---|---  
Serverless VPC Access connector| Charged by the number of instances in your connector. Connector instances bill as Compute Engine VMs, but you cannot view or manage them as VMs in the Google Cloud console. See the pricing for your instance type:

  * f1-micro: [N1 shared-core machine types](https://cloud.google.com/compute/vm-instance-pricing#sharedcore)
  * e2-micro: [E2 shared-core machine types](https://cloud.google.com/compute/vm-instance-pricing#e2_sharedcore_machine_types)
  * e2-standard-4: [E2 standard machine types](https://cloud.google.com/compute/vm-instance-pricing#e2_standard_machine-types)

  
Data transfer out| Charged at [Compute Engine networking rates](https://cloud.google.com/vpc/network-pricing#egress). Serverless VPC Access connector instances are distributed across zones for increased reliability. The rate is based on which connector instance handles the request and whether the destination resource is in the same zone. Data transfer out to a connector from a serverless resource such as a function, app, or service is not charged.  
  
You can view your Serverless VPC Access costs in the Google Cloud console by filtering your billing reports by the label key serverless-vpc-access.

## 

Network telemetry

Network Vended Logs generate charges. You are charged for the following products.

Before enabling VPC Flow Logs, you can use the [VPC Flow Logs cost estimator](https://ssh.cloud.google.com/cloudshell/editor?show=terminal&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/network-observability-tutorials&cloudshell_git_branch=main&cloudshell_tutorial=vpc-flowlogs-cost-estimator/tutorial.md) in the Gemini CLI to estimate your monthly costs and log volume. It provides a simplified estimate for all subnets in a Google Cloud project based on the listed pricing tiers and assumes no prior usage. You can also prompt the estimator to calculate costs for specific subnets, VPC networks, or custom sampling rates.

Products| Price (USD)  
---|---  
  
  * VPC Flow Logs
  * Firewall Rules Logging
  * Cloud NAT logging

| 0 gibibyte to 10,240 gibibyte$0.25 / 1 gibibyte, per 1 month / account10,240 gibibyte to 30,720 gibibyte$0.15 / 1 gibibyte, per 1 month / account30,720 gibibyte to 51,200 gibibyte$0.075 / 1 gibibyte, per 1 month / account51,200 gibibyte and above$0.05 / 1 gibibyte, per 1 month / account  
  
Logs are sent to Cloud Logging. Logs can be further exported to Pub/Sub, Cloud Storage, or BigQuery. Pub/Sub, Cloud Storage, or BigQuery charges apply in addition to log generation charges. Network Telemetry logs are charged as Vended Logs in Cloud Logging Storage. For more information on exporting logs, see [Overview of logs export](https://cloud.google.com/logging/docs/export).

The Networking Telemetry charges apply to all Network Telemetry logs irrespective of the destination, including the default option of storing these logs in Cloud Logging.

If you store your logs in Cloud Logging, Network Telemetry logs are billed separately from other logs, under the Cloud Logging Vended Logs Storage. For more information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).

If you send and then exclude your logs from Cloud Logging, the Network Telemetry charges apply.

## 

Packet Mirroring

You are charged for the amount of data processed by Packet Mirroring. You are not charged for Packet Mirroring forwarding rules. Currently, there is no additional per-VM charge for using Packet Mirroring. The costs for the data processed by Packet Mirroring are described in the following table.

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



Item| Price per unit (USD)  
---|---  
Inbound data processed by load balancer for Packet Mirroring| $0.008 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Normal data transfer rates are charged for traffic outbound from a load balancer. There is no additional load balancer data transfer cost beyond normal data transfer out rates.

## 

Load balancing and forwarding rules

The pricing tables in this section apply to the following load balancers:

  * Internal and external passthrough Network Load Balancers
  * Internal and external proxy Network Load Balancers
  * Global, classic, and regional external Application Load Balancers



For regional and cross-region [internal Application Load Balancers](https://docs.cloud.google.com/vpc/pricing#internal-https-lb), see the Internal Application Load Balancer section.

For Private Service Connect forwarding rules, see the [Private Service Connect section](https://docs.cloud.google.com/vpc/pricing#psc-forwarding-rules).

The following table shows the pricing for global forwarding rules. There are no global data processing charges. Data processing is charged by the region, depending on where the traffic is processed.

HourlyHourly

MonthlyMonthly

Item| Price per unit (USD)  
---|---  
First 5 forwarding rules| $0.025 / 1 hour  
Per additional forwarding rule| $0.01 / 1 hour  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

The following table shows regional forwarding rule charges and inbound and outbound data processing charges by region.

  


Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Item| Price (USD)  
---|---  
First 5 forwarding rules| $0.025 / 1 hour  
Per additional forwarding rule| $0.01 / 1 hour  
Inbound data processed by load balancer| $0.008 / 1 gibibyte  
Outbound data processed by load balancer| $0.008 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Ways to lower external Application Load Balancer costs

Global external Application Load Balancer users can use Google Cloud Armor, Cloud CDN, or both, to minimize the impact of  _Outbound data processing charges_.

  * **Cloud CDN:** Static objects that are served to the client from the cache do not transit through the load balancer. An effective caching strategy would reduce the amount of outbound data being processed by the load balancer and lower your costs. To implement caching, it is necessary to understand which portion of your traffic is static and cacheable. For additional information, refer the [Cloud CDN documentation](https://cloud.google.com/cdn/docs/features#caching).
  * **Cloud Armor:** If your application receives a significant amount of undesirable traffic, you can deploy Cloud Armor to block such traffic. Requests that are blocked by Cloud Armor do not transit through the load balancer, effectively reducing the amount of outbound data processed by the load balancer. The impact on your costs depends on the percentage of undesirable traffic blocked by the [Cloud Armor security policies](https://cloud.google.com/armor/docs/security-policy-overview) you've implemented.



If your application can operate in a single region or is required to operate in a single region, you can use the [Regional external Application Load Balancer](https://cloud.google.com/load-balancing/docs/https#load-balancer-mode). The regional external Application Load Balancer uses only the Standard Network Tier which has [lower outbound data transfer charges](https://cloud.google.com/vpc/network-pricing#internet_egress) making it a cost effective option.

### 

External Application Load Balancer pricing with Serverless NEGs

If you are using [serverless NEG backends](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) with an external Application Load Balancer ([global, regional, or classic](https://cloud.google.com/load-balancing/docs/https#load-balancer-mode)), existing load balancer charges will apply in addition to the serverless compute charges for Cloud Run, Cloud Run functions, or App Engine backends as applicable. If Google Cloud Armor or Cloud CDN are used, their respective charges also apply.

However, you will not be charged for serverless outbound data transfer. Only internet outbound data transfer rates apply. Cloud Run functions [outbound data transfer](https://cloud.google.com/functions/pricing) charges, App Engine [outgoing network traffic](https://cloud.google.com/appengine/pricing#network-resources-in-the-standard-environment) charges and Cloud Run [data transfer charges](https://cloud.google.com/run/pricing) do not apply to requests passed from an external Application Load Balancer (using serverless NEGs) to a Cloud Run functions, App Engine, or Cloud Run service.

### 

Cross-project service referencing with Shared VPC

Review the following points to understand how projects and billing accounts are charged for networking SKUs when you use [cross-project service referencing](https://cloud.google.com/load-balancing/docs/https#cross-project).

![Load balancer's frontend and backend in different service projects](https://www.gstatic.com/bricks/image/6c3c292a-e530-4f9e-875d-4b914ae3071b.svg)

Load balancer's frontend and backend in different service projects

  * Cloud Load Balancing related charges are always attributed to the project where the forwarding rule is configured (service project A in figure 1). This includes charges for forwarding rules, inbound data processed, and outbound data processed by the global external Application Load Balancer. Review [Cloud Load Balancing pricing basics](https://cloud.google.com/vpc/network-pricing#lb).
  * Network internet data transfer out for Premium Tier and Standard Tier are always attributed to the project where the forwarding rule is configured (service project A in figure 1). Review [Network data transfer pricing](https://cloud.google.com/vpc/network-pricing#all-networking-pricing).
  * If you configure Cloud CDN on a backend service that is referenced by a URL map using cross-project service referencing, then all Cloud CDN charges for cacheable content (cache data transfer out, cache lookup, cache fill) are always attributed to the project that contains the Cloud CDN-enabled backend service (service project B in figure 1), and not the project that configured the forwarding rules. Review [Cloud CDN pricing](https://cloud.google.com/cdn/pricing).
  * If you configure Google Cloud Armor on a backend service that is referenced by a URL map using cross-project service referencing, then all Google Cloud Armor related charges are attributed to the project that contains the Google Cloud Armor-enabled backend service (service project B in figure 1), and not the project that configured the forwarding rules. Review [Google Cloud Armor pricing](https://cloud.google.com/armor/pricing). Specifically, all Google Cloud Armor Standard Tier and Cloud Armor Enterprise Tier charges are attributed to service project B.



The following additional considerations also apply when you're using Cloud Armor with cross-project service referencing:

  * Subscription changes related to [Cloud Armor Enterprise](https://cloud.google.com/armor/pricing) are attributed to the billing account that you specified during enrollment. If you want to use the same Cloud Armor Enterprise subscription across multiple projects to include all the backend services referenced using cross-project service referencing, make sure that you include all the relevant service projects as part of the same Cloud Armor Enterprise billing account.
  * When you're using cross-project service referencing, some features offered in Cloud Armor Enterprise, such as DDoS telemetry and DDoS response, require Cloud Armor Enterprise tier enrollment for both the frontend forwarding rule project and the backend service projects.



### 

Forwarding rules pricing examples

Google Cloud charges for [forwarding rules](https://cloud.google.com/vpc/docs/forwarding-rules) whether they are created for [load balancing](https://cloud.google.com/compute/docs/load-balancing) or other uses, such as Packet Mirroring.

The following examples use US pricing:

You can create up to 5 forwarding rules for the price of $0.025/hour. For example, if you create one forwarding rule, you are charged $0.025/hour. If you have 3 forwarding rules, you are still charged $0.025/hour. However, if you have 10 forwarding rules, you are charged as follows:

  * 5 forwarding rules = $0.025/hour
  * Each additional forwarding rule = $0.01/hour



$0.025/hour for 5 rules + (5 additional rules * $0.01/hour) = $0.075/hour

For most load balancing use cases, you need only one forwarding rule per load balancer.

Google Cloud charges for [global forwarding rules](https://cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules) and [regional forwarding rules](https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) separately, and also per project. For example, if you use one global forwarding and one regional forwarding rule in two separate projects (four rules total), you are charged $0.10/hour (4 x $0.025/hour).

### 

Estimating load balancing charges

To estimate load balancing charges:

  1. Go to the [Pricing Calculator](https://cloud.google.com/products/calculator/).
  2. On the **Cloud Load Balancing** tab.
  3. From the dropdown menu, select a region.
  4. Enter your estimated number of forwarding rules.
  5. Enter your monthly estimated amount of network traffic processed.



For example:

  * Iowa
  * Number of forwarding rules: 10
  * Inbound data processed by load balancer: 2,048 GiB
  * Total Estimated Cost: USD 71.13 per 1 month



This example doesn't include the [internet data transfer out cost](https://docs.cloud.google.com/vpc/pricing#internet_egress) of sending replies from the backends.

## 

Internal Application Load Balancer

The following charges apply to both regional internal Application Load Balancers and cross-region internal Application Load Balancers. Some additional [cross-region data transfer charges also apply to the cross-region internal Application Load Balancer](https://docs.cloud.google.com/vpc/pricing#cross-region-egress).

Iowa (us-central1)

  * Johannesburg (africa-south1)
  * Taiwan (asia-east1)
  * Hong Kong (asia-east2)
  * Tokyo (asia-northeast1)
  * Osaka (asia-northeast2)
  * Seoul (asia-northeast3)
  * Mumbai (asia-south1)
  * Delhi (asia-south2)
  * Singapore (asia-southeast1)
  * Jakarta (asia-southeast2)
  * Bangkok (asia-southeast3)
  * Kuala Lumpur (asia-southeast4)
  * Sydney (australia-southeast1)
  * Melbourne (australia-southeast2)
  * Warsaw (europe-central2)
  * Finland (europe-north1)
  * Stockholm (europe-north2)
  * Madrid (europe-southwest1)
  * Belgium (europe-west1)
  * Berlin (europe-west10)
  * Turin (europe-west12)
  * London (europe-west2)
  * Frankfurt (europe-west3)
  * Netherlands (europe-west4)
  * Galaxy Frankfurt (europe-west5)
  * Zurich (europe-west6)
  * Milan (europe-west8)
  * Paris (europe-west9)
  * Doha (me-central1)
  * Dammam (me-central2)
  * Tel Aviv (me-west1)
  * Montreal (northamerica-northeast1)
  * Toronto (northamerica-northeast2)
  * Mexico (northamerica-south1)
  * Sao Paulo (southamerica-east1)
  * Santiago (southamerica-west1)
  * Iowa (us-central1)
  * South Carolina (us-east1)
  * Northern Virginia (us-east4)
  * Columbus (us-east5)
  * Alabama (us-east7)
  * Dallas (us-south1)
  * Oregon (us-west1)
  * Los Angeles (us-west2)
  * Salt Lake City (us-west3)
  * Las Vegas (us-west4)
  * Phoenix (us-west8)



HourlyHourly

MonthlyMonthly

Item| Price (USD)  
---|---  
Per proxy instance*| $0.025 / 1 hour  
Data processed by load balancer| $0.008 / 1 gibibyte  
  
* Internal Application Load Balancers use a fleet of managed proxy instances that are dynamically allocated to your network to handle traffic volume. The  _per proxy instance_ charge is determined based on the number of proxy instances required to handle your traffic over a specific time period.

### 

Proxy instance charge

Envoy-based load balancers automatically scale the number of proxies available to handle your traffic based on your traffic needs. The proxy instance charge is based on the number of proxy instances needed to satisfy your traffic needs. Each additional proxy incurs an additional hourly charge according to the prices indicated in the [pricing table](https://cloud.google.com/vpc/network-pricing#internal-https-lb).

The number of proxies allocated to your load balancer is calculated based on the measured capacity needed to handle your traffic over a 10-minute time period. During this time period, we look at the greater of:

  * **The number of proxies needed to serve your traffic's bandwidth needs**. Each proxy instance can handle up to 18 MB per second. We monitor the total bandwidth required and divide that total by the bandwidth that a proxy instance can support.
  * **The number of proxies needed to handle connections and requests**. We count the total of each of the following resources and divide each value by what a proxy instance can handle:
  * 600 (HTTP) or 150 (HTTPS) new connections per second
  * 3,000 active connections
  * 1,400 requests per second*



* A proxy instance can handle 1,400 requests per sec if Cloud Logging is disabled. If you enable Logging, your proxy instance can handle fewer requests per second. For example: logging 100% of requests decreases the proxy's request handling capacity to 700 requests per second. You can set Logging to sample a smaller percentage of traffic. This enables you to meet your observability needs while controlling your cost.

### 

Example calculation

In a 10-minute period, 180 MB per second of data pass through the load balancer. 180 MB per second / 18 MB per second per proxy instance = 10 proxy instances

During this same period, 300 new HTTPS connections are established per second, 3,000 connections are active and 2,800 requests are sent per second:

300 new HTTPS connections per second / 150 new HTTPS connections per second per proxy instance = 2 proxy instances 3,000 active connections / 3,000 active connections per proxy instance = 1 proxy instance 2,800 requests per second / 1,400 requests per second per proxy instance = 2 proxy instances.

This sums up to 5 proxy instances. This amount is lower than the 10 proxy instances required to serve bandwidth. Thus, the proxy instance charge for this 10-minute time period would be calculated as follows:

10 proxy instances * $0.025 per proxy instance per hour * (10 minutes / (60 minutes per hour)) = $0.0417.

Billing is calculated based on the measured capacity needed to satisfy your traffic needs, not the number of proxy instances that are establishing connections to your backends. As such, you might be billed for a different number of proxy instances than you see in your infrastructure.

### 

Minimum proxy instance charge

To ensure optimal performance and reliability, each load balancer is allocated at least three proxy instances in the Google Cloud region where the load balancer is deployed. These proxy instances are allocated even if the load balancer handles no traffic. After a forwarding rule (with load balancing scheme INTERNAL_MANAGED) is deployed to your project, you start to accrue proxy instance charges. Additional forwarding rules incur additional proxy instance charges as described previously (in other words, three additional proxy instances per forwarding rule).

The three proxy instances that are allocated to your load balancer result in a minimum hourly proxy instance charge. For example, for the us-central1 Google Cloud region, the minimum charge is calculated as follows:

3 proxy instances * $0.025 per proxy per hour = $0.075 per hour.

As described previously, these proxy instances can each handle a certain amount of traffic. Once your traffic needs surpass the capacity of these three proxy instances, you will incur costs for the proxy instances required to handle any additional traffic.

### 

Data processing charge

The data processing charge is calculated by measuring the total volume of data for requests and responses processed by your load balancer during the billing cycle. This charge scales according to your usage and there is no minimum charge for data processing.

### 

Cross-region data transfer charges

[Cross-region data transfer charges](https://cloud.google.com/vpc/network-pricing#vpc-pricing) apply if you're using a cross-region internal Application Load Balancer. For example, if you have a cross-region internal Application Load Balancer deployment where the client, the Envoy proxy, and the backend are in separate regions, you'll see cross-region data transfer charges for each hop separately (client <-> Envoy proxy, and Envoy proxy <-> backend). To reduce these cross-region data transfer charges, you can deploy Envoy proxies in multiple regions.

### 

Cross-project service referencing with Shared VPC

For data processing, hourly proxy instance usage, and inter-zone VM data transfer, the forwarding rule project is charged.

### 

Internal Application Load Balancer pricing with serverless NEGs

If you are using [serverless NEG backends](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) for an internal Application Load Balancer, existing internal Application Load Balancer charges will apply in addition to the serverless compute charges for Cloud Run.

## 

Regional internet NEG charges

Regional internet NEGs require the use of a Cloud NAT gateway which incurs additional charges. You'll be charged for both internet data transfer out and Cloud NAT usage for any traffic sent to and from the Envoy proxy-only subnet, and for health check traffic. However, the load balancer's charges apply only to user request traffic.

Cloud NAT gateways allocated for Cloud Load Balancing incur hourly charges equivalent to a network with  _more than 32 VM instances_. For details, see [Cloud NAT pricing](https://cloud.google.com/vpc/network-pricing#nat-pricing)

## 

Authorization policy charges

Authorization policies are offered without usage fees for the duration of the Preview.

## 

Custom request headers and Cloud Armor charges

If a backend service has a Cloud Armor policy associated with it, you can use the custom request headers feature with that backend service without any additional charge for the custom request headers feature.

If a backend service that uses the custom request headers feature does  _not_ have a Cloud Armor policy associated with it, the charges are $0.75 per 1,000,000 HTTP(S) requests per month per account. You are only charged for the first 666,666,667 requests per month per account.

## 

Global access for internal load balancers

Global access allows client instances from any region to access your internal load balancer. If a forwarding rule has global access enabled, additional cross-region data transfer charges are incurred when traffic is sent to or from a client in a different region than the load balancer.

Global access is generally available for internal passthrough Network Load Balancers, regional internal Application Load Balancers, and regional internal proxy Network Load Balancers.

## 

Protocol forwarding

Protocol forwarding is charged at the same rate as load balancing. There is a charge for the forwarding rule and a charge for the inbound data processed by the target instance.

## 

SSL certificates

There is no charge for self-managed and Google-managed SSL certificates.

## What's next

  * Read the [Cloud Load Balancing documentation](https://cloud.google.com/vpc/docs).
  * Try the [Pricing calculator](https://cloud.google.com/products/calculator).
  * Learn about [Cloud Load Balancing solutions and use cases](https://cloud.google.com/architecture?text=Cloud%20Load%20Balancing).



## Request a custom quote

With Google Cloud's pay-as-you-go pricing, you only pay for the services you use. Connect with our sales team to get a custom quote for your organization.

Contact sales[](https://cloud.google.com/contact?direct=true)

menu

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

[Overview](https://cloud.google.com/why-google-cloud)[Solutions](https://cloud.google.com/solutions)[Products](https://cloud.google.com/products)[Pricing](https://cloud.google.com/pricing)[Resources](https://cloud.google.com/docs/get-started)[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)[Contact us](https://cloud.google.com/contact)



 _search_ _send_




[Docs](https://cloud.google.com/docs)[Support](https://cloud.google.com/support-hub)

[Console](https://console.cloud.google.com/)

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/vpc/pricing&hl=en-US&prompt=select_account&service=cloudconsole)

Start free[](https://console.cloud.google.com/freetrial)

Start free[](https://console.cloud.google.com/freetrial)

Contact us[](https://cloud.google.com/contact)

close

  * Accelerate your digital transformation
  * Whether your business is early in its journey or well on its way to digital transformation, Google Cloud can help solve your toughest challenges.
  * [Learn more](https://cloud.google.com/transform)




  * Key benefits
  * [Why Google CloudTop reasons businesses choose us.](https://cloud.google.com/why-google-cloud)

  * [AI and AgentsGet enterprise-ready AI.](https://cloud.google.com/ai)

  * [MulticloudRun your apps wherever you need them.](https://cloud.google.com/multicloud)

  * [Global infrastructureBuild on the same infrastructure as Google.](https://cloud.google.com/infrastructure)




  * [Data CloudMake smarter decisions with unified data.](https://cloud.google.com/data-cloud)

  * [Modern Infrastructure CloudNext generation of cloud infrastructure.](https://cloud.google.com/solutions/modern-infrastructure)

  * [SecurityProtect your users, data, and apps.](https://cloud.google.com/security)

  * [Productivity and collaborationConnect your teams with AI-powered apps.](https://workspace.google.com)




  * Reports and insights
  * [Executive insightsCurated C-suite perspectives.](https://cloud.google.com/executive-insights)

  * [Analyst reportsRead what industry analysts say about us.](https://cloud.google.com/analyst-reports)

  * [WhitepapersBrowse and download popular whitepapers.](https://cloud.google.com/whitepapers)

  * [Customer storiesExplore case studies and videos.](https://cloud.google.com/customers)




close

  * Industry Solutions
  * Application Modernization
  * Artificial Intelligence
  * APIs and Applications
  * Data Analytics
  * Databases
  * Infrastructure Modernization
  * Productivity and Collaboration
  * Security
  * Startups and SMB



See all solutions[](https://cloud.google.com/solutions)

  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Industry SolutionsReduce cost, increase operational agility, and capture new market opportunities.](https://cloud.google.com/solutions#industry-solutions)


  * [![](https://www.gstatic.com/cloud/images/navigation/retail.svg)RetailAnalytics and collaboration tools for the retail value chain.](https://cloud.google.com/solutions/retail)


  * [![](https://www.gstatic.com/cloud/images/navigation/cpg.svg)Consumer Packaged GoodsSolutions for CPG digital transformation and brand growth.](https://cloud.google.com/solutions/cpg)


  * [![](https://www.gstatic.com/cloud/images/navigation/finance.svg)Financial ServicesComputing, data management, and analytics tools for financial services.](https://cloud.google.com/solutions/financial-services)


  * [![](https://www.gstatic.com/cloud/images/navigation/hcls.svg)Healthcare and Life SciencesAdvance research at scale and empower healthcare innovation.](https://cloud.google.com/solutions/healthcare-life-sciences)


  * [![](https://www.gstatic.com/cloud/images/navigation/media.svg)Media and EntertainmentSolutions for content production and distribution operations.](https://cloud.google.com/solutions/media-entertainment)


  * [![](https://www.gstatic.com/cloud/images/navigation/telecommunications.svg)TelecommunicationsHybrid and multi-cloud services to deploy and monetize 5G.](https://cloud.google.com/solutions/telecommunications)


  * [![](https://www.gstatic.com/cloud/images/navigation/gaming.svg)GamesAI-driven solutions to build and scale games faster.](https://cloud.google.com/solutions/games)


  * [![](https://www.gstatic.com/cloud/images/navigation/manufacturing.svg)ManufacturingMigration and AI tools to optimize the manufacturing value chain.](https://cloud.google.com/solutions/manufacturing)


  * [![](https://www.gstatic.com/cloud/images/navigation/supply-chain.svg)Supply Chain and LogisticsEnable sustainable, efficient, and resilient data-driven operations across supply chain and logistics operations.](https://cloud.google.com/solutions/supply-chain-logistics)


  * [![](https://www.gstatic.com/cloud/images/navigation/government.svg)GovernmentData storage, AI, and analytics solutions for government agencies.](https://cloud.google.com/gov)


  * [![](https://www.gstatic.com/cloud/images/navigation/icon-sprite.svg#education)EducationTeaching tools to provide more engaging learning experiences.](https://cloud.google.com/edu/higher-education)


  * Not seeing what you're looking for?
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Application ModernizationModernize, automate, and scale your application and data portfolio using enterprise AI, intelligent engineering practices, and cloud-native infrastructure.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Application Modernization with AIAI-assisted code refactoring, assessment, and transformation for legacy applications.](https://cloud.google.com/solutions/application-modernization-with-ai)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Mainframe ModernizationAutomated tools and AI-driven guidance for moving your mainframe apps to the cloud.](https://cloud.google.com/solutions/mainframe-modernization)


  * [Database ModernizationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Data Lake ModernizationUnify and govern multimodal data on an open, high-performance cloud data lake.](https://cloud.google.com/solutions/data-lakehouse)


  * [Data Warehouse ModernizationMigrate and modernize your enterprise data warehouse for serverless analytics and AI.](https://cloud.google.com/solutions/data-migration)


  * [APIsUnlock legacy applications and build new digital channels using APIs and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [Platform EngManaged services and golden paths to build, manage, and scale internal developer platforms.](https://cloud.google.com/solutions/platform-engineering)


  * [DevOps Best PracticesProcesses and resources for implementing DevOps in your org.](https://cloud.google.com/devops)


  * [SRE PrinciplesTools and resources for adopting SRE in your org.](https://cloud.google.com/sre)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Artificial IntelligenceAdd intelligence and efficiency to your business with AI and machine learning.](https://cloud.google.com/solutions/ai)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Gemini for enterpriseUnified agentic portfolio for your entire organization.](https://cloud.google.com/gemini-enterprise)


  * [AI Commerce SearchGoogle-quality search and product recommendations for retailers.](https://cloud.google.com/gemini-enterprise-cx/commerce)


  * [Google Cloud with GeminiAI assistants for application development, coding, and more.](https://cloud.google.com/ai/gemini)


  * [Physical AISimulate, train, and operate the next generation of robots, autonomous vehicles, industrial devices, and machines.](https://cloud.google.com/solutions/physical-ai)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)APIs and ApplicationsSpeed up the pace of innovation without coding, using APIs, apps, and automation.](https://cloud.google.com/solutions/apis-and-applications)


  * [New Business Channels Using APIsAttract and empower an ecosystem of developers and partners.](https://cloud.google.com/solutions/new-channels-using-apis)


  * [Unlocking Legacy Applications Using APIsCloud services for extending and modernizing legacy apps.](https://cloud.google.com/solutions/unlocking-legacy-applications)


  * [Open Banking APIxSimplify and accelerate secure delivery of open banking compliant APIs.](https://cloud.google.com/solutions/open-banking-apix)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data AnalyticsGenerate instant insights from data at any scale with a serverless, fully managed analytics platform that significantly simplifies analytics.](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [Data MigrationMigrate and modernize your data warehouse and data lakes with AI-powered migration services.](https://cloud.google.com/solutions/data-migration)


  * [Data LakehouseUnify and govern your multimodal data with a high-performance and open data lakehouse.](https://cloud.google.com/solutions/data-lakehouse)


  * [Real-time AnalyticsInsights from ingesting, processing, and analyzing event streams.](https://cloud.google.com/solutions/stream-analytics)


  * [Marketing AnalyticsSolutions for collecting, analyzing, and activating customer data.](https://cloud.google.com/solutions/marketing-analytics)


  * [DatasetsData from Google, public, and commercial providers to enrich your analytics and AI initiatives.](https://cloud.google.com/datasets)


  * [Business IntelligenceSolutions for modernizing your BI stack and creating rich data experiences.](https://cloud.google.com/solutions/business-intelligence)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Geospatial AnalyticsA comprehensive platform to solve for geospatial use cases at scale.](https://cloud.google.com/solutions/geospatial)


  * [Data ScienceManaged services and integrated workflows to build, manage, and scale data science.](https://cloud.google.com/solutions/data-science)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)DatabasesMigrate and manage enterprise data with security, reliability, high availability, and fully managed data services.](https://cloud.google.com/solutions/databases)


  * [Database MigrationGuides and tools to simplify your database migration life cycle.](https://cloud.google.com/solutions/database-migration)


  * [Database ModernizationUpgrades to modernize your operational database infrastructure.](https://cloud.google.com/solutions/database-modernization)


  * [Databases for GamesBuild global, live games with Google Cloud databases.](https://cloud.google.com/solutions/databases/games)


  * [Google Cloud DatabasesDatabase services to migrate, manage, and modernize data.](https://cloud.google.com/products/databases)


  * [Migrate Oracle workloads to Google CloudRehost, replatform, rewrite your Oracle workloads.](https://cloud.google.com/solutions/oracle)


  * [Open Source DatabasesFully managed open source databases with enterprise-grade support.](https://cloud.google.com/solutions/open-source-databases)


  * [SQL Server on Google CloudOptions for running SQL Server virtual machines on Google Cloud.](https://cloud.google.com/sql-server)


  * [Gemini for DatabasesSupercharge database development and management with AI.](https://cloud.google.com/products/gemini/databases)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Infrastructure ModernizationMigrate core systems rapidly and modernize enterprise workloads with AI-powered infrastructure and automated cloud solutions.](https://cloud.google.com/solutions/modernize)


  * [Google Cloud ModernizeUnified program and AI-powered tools for end-to-end cloud migration and modernization.](https://cloud.google.com/solutions/modernize)


  * [Gemini for businessEnterprise-ready generative AI and agents to accelerate innovation across your organization.](https://cloud.google.com/gemini-enterprise)


  * [AI HypercomputerIntegrated supercomputing architecture to train, tune, and serve AI workloads.](https://cloud.google.com/ai-infrastructure)


  * [Rapid Migration and Modernization Program (RaMP)End-to-end migration program to simplify and accelerate your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Data Center ExitsMigration solutions for moving VMs, apps, databases, and workloads out of data centers.](https://cloud.google.com/solutions/data-center-migration)


  * [Application Modernization & MigrationDiscovery, assessment, and migration tools for moving and modernizing applications.](https://cloud.google.com/solutions/application-migration)


  * [Database Modernization & MigrationFully managed database services to migrate, manage, and modernize enterprise data.](https://cloud.google.com/products/databases)


  * [Cross-Cloud NetworkingSimplify hybrid and multicloud networking, and secure your workloads, data, and users.](https://cloud.google.com/solutions/cross-cloud-network)


  * [High Performance Computing (HPC)Compute, storage, and networking options to support any high-performance workload.](https://cloud.google.com/solutions/hpc)


  * [VMwareFully managed, native VMware Cloud Foundation software stack on Google Cloud.](https://cloud.google.com/vmware-engine)


  * [SAPCertified infrastructure and AI solutions for running SAP applications and SAP HANA.](https://cloud.google.com/solutions/sap)


  * [WindowsTools, licenses, and partner solutions for running enterprise Windows workloads.](https://cloud.google.com/windows)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Productivity and CollaborationChange the way teams work with solutions designed for humans and built for impact.](https://workspace.google.com/enterprise/)


  * [Google WorkspaceCollaboration and productivity tools for enterprises.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome Browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)SecurityDetect, investigate, and respond to online threats to help protect your business.](https://cloud.google.com/solutions/security)


  * [Agentic SOCDelivering better security outcomes with AI agents.](https://cloud.google.com/solutions/agentic-soc)


  * [Web App and API ProtectionThreat and fraud protection for your web applications and APIs.](https://cloud.google.com/security/solutions/web-app-and-api-protection)


  * [Security and Resilience FrameworkSolutions for each phase of the security and resilience life cycle.](https://cloud.google.com/security/solutions/security-and-resilience)


  * [Risk and compliance as code (RCaC)Solution to modernize your governance, risk, and compliance function with automation.](https://cloud.google.com/solutions/risk-and-compliance-as-code)


  * [Software Supply Chain SecuritySolution for improving end-to-end software supply chain security.](https://cloud.google.com/security/solutions/software-supply-chain-security)


  * [Security FoundationRecommended products to help achieve a strong security posture.](https://cloud.google.com/security/solutions/security-foundation)


  * [Google Cloud Cybershield™Strengthen nationwide cyber defense.](https://cloud.google.com/security/solutions/secops-cybershield)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Startups and SMBAccelerate startup and SMB growth with tailored solutions and programs.](https://cloud.google.com/solutions#section-13)


  * [Startup ProgramGet financial, business, and technical support to take your startup to the next level.](https://cloud.google.com/startup)


  * [Small and Medium BusinessExplore solutions for web hosting, app development, AI, and analytics.](https://cloud.google.com/solutions/smb)


  * [Software as a ServiceBuild better SaaS products, scale efficiently, and grow your business.](https://cloud.google.com/saas)



close

  * Featured Products
  * AI and Machine Learning
  * Business Intelligence
  * Compute
  * Containers
  * Data Analytics
  * Databases
  * Developer Tools
  * Distributed Cloud
  * Hybrid and Multicloud
  * Industry Specific
  * Integration Services
  * Management Tools
  * Maps and Geospatial
  * Media Services
  * Migration
  * Networking
  * Operations
  * Productivity and Collaboration
  * Security and Identity
  * Serverless
  * Storage
  * Web3



See all products (100+)[](https://cloud.google.com/products#featured-products)

  * Featured Products


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [![](https://www.gstatic.com/images/branding/productlogos/gemini_2025/v1/web-24dp/logo_gemini_2025_color_2x_web_24dp.png)Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [![](https://www.gstatic.com/cloud/images/navigation/compute-engine.png)Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-storage.png)Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [![](https://www.gstatic.com/cloud/images/navigation/bigquery.png)BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-run.png)Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [![](https://www.gstatic.com/cloud/images/navigation/kubernetes-engine.png)Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [![](https://www.gstatic.com/cloud/images/navigation/looker.png)LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [![](https://www.gstatic.com/cloud/images/navigation/apigee.png)Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [![](https://www.gstatic.com/cloud/images/navigation/cloud-sql.png)Cloud SQLRelational database services for MySQL, PostgreSQL and SQL Server.](https://cloud.google.com/sql)


  * [![](https://www.gstatic.com/cloud/images/navigation/networking.png)Cloud CDNContent delivery network for delivering web and video.](https://cloud.google.com/cdn)


  * Not seeing what you're looking for?
  * [See all products (100+)](https://cloud.google.com/products#featured-products)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)AI and Machine Learning](https://cloud.google.com/products/ai)


  * [Gemini platformUnified platform for ML models, generative AI, and agent building.](https://cloud.google.com/products/gemini-enterprise-agent-platform)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Gemini for customer experienceBuild and manage agents that live across the entire customer lifecycle.](https://cloud.google.com/gemini-enterprise-cx)


  * [Model GardenSingle place to discover over 200 models from Google and Google partners.](https://console.cloud.google.com/agent-platform/model-garden)


  * [Customer Experience Agent StudioBuild conversational AI with both deterministic and gen AI functionality.](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)


  * [Agent SearchBuild Google-quality search for your enterprise apps and experiences.](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)


  * [Speech-to-TextSpeech recognition and transcription across 125 languages.](https://cloud.google.com/speech-to-text)


  * [Text-to-SpeechSpeech synthesis in 220+ voices and 40+ languages.](https://cloud.google.com/text-to-speech)


  * [Translation AILanguage detection, translation, and glossary support.](https://cloud.google.com/translate)


  * [Vision AICustom and pre-trained models to detect emotion, text, and more.](https://cloud.google.com/vision)


  * [Contact Center as a ServiceOmnichannel contact center solution that is native to the cloud.](https://cloud.google.com/solutions/contact-center-ai-platform)


  * Not seeing what you're looking for?
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)



  * Business Intelligence


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [Data StudioInteractive data suite for dashboarding, reporting, and analytics.](https://cloud.google.com/data-studio)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Compute](https://cloud.google.com/products/compute)


  * [Compute EngineVirtual machines running in Google’s data center.](https://cloud.google.com/products/compute)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [Cloud GPUsGPUs for ML, scientific computing, and 3D visualization.](https://cloud.google.com/gpu)


  * [Migrate to Virtual MachinesServer and virtual machine migration to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Spot VMsCompute instances for batch jobs and fault-tolerant workloads.](https://cloud.google.com/spot-vms)


  * [BatchFully managed service for scheduling batch jobs.](https://cloud.google.com/batch)


  * [Sole-Tenant NodesDedicated hardware for compliance, licensing, and management.](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)


  * [Bare MetalInfrastructure to run specialized workloads on Google Cloud.](https://cloud.google.com/bare-metal)


  * [RecommenderUsage recommendations for Google Cloud products and services.](https://cloud.google.com/recommender/docs/whatis-activeassist)


  * [VMware EngineFully managed, native VMware Cloud Foundation software stack.](https://cloud.google.com/vmware-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * Not seeing what you're looking for?
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Containers](https://cloud.google.com/containers)


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud BuildSolution for running build steps in a Docker container.](https://cloud.google.com/build)


  * [Artifact RegistryPackage manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Deep Learning ContainersContainers with data science frameworks, libraries, and tools.](https://cloud.google.com/deep-learning-containers/docs)


  * [KnativeComponents to create Kubernetes-native cloud-based software.](https://knative.dev/docs/)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)


  * [BigQueryAutonomous data to AI platform for analytics and data science.](https://cloud.google.com/bigquery)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [DataflowReal-time analytics for stream and batch processing.](https://cloud.google.com/products/dataflow)


  * [LookerPlatform for BI, data applications, and embedded analytics.](https://cloud.google.com/looker)


  * [LakehouseOpen lakehouse platform with enterprise storage and performance capabilities.](https://cloud.google.com/products/lakehouse)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Knowledge CatalogAlways-on catalog for AI that provides universal context for agents.](https://cloud.google.com/products/knowledge-catalog)


  * [Data Analytics AgentsBuilt-in agents for data lifecycle and tools to build your own agents.](https://cloud.google.com/use-cases/data-analytics-agents)


  * [Data Analytics Migration ServicesFree-to-use, cloud-native and AI-powered data migration services.](https://cloud.google.com/solutions/data-migration)


  * [Managed Service for Apache KafkaManaged Kafka service to operate highly available Apache Kafka clusters.](https://cloud.google.com/products/managed-service-for-apache-kafka)


  * Not seeing what you're looking for?
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Databases](https://cloud.google.com/products/databases)


  * [AlloyDB for PostgreSQLFully managed, PostgreSQL-compatible database for enterprise workloads.](https://cloud.google.com/alloydb)


  * [Cloud SQLFully managed database for MySQL, PostgreSQL, and SQL Server.](https://cloud.google.com/sql)


  * [FirestoreHighly scalable and serverless NoSQL document database, with MongoDB compatibility.](https://cloud.google.com/firestore)


  * [SpannerCloud-native relational database with unlimited scale and 99.999% availability.](https://cloud.google.com/spanner)


  * [BigtableCloud-native wide-column database for large-scale, low-latency workloads.](https://cloud.google.com/bigtable)


  * [DatastreamServerless change data capture and replication service.](https://cloud.google.com/datastream)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Bare Metal SolutionFully managed infrastructure for your Oracle workloads.](https://cloud.google.com/bare-metal)


  * [MemorystoreFully managed Redis and Memcached for sub-millisecond data access.](https://cloud.google.com/memorystore)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Developer Tools](https://cloud.google.com/products/tools)


  * [Artifact RegistryUniversal package manager for build artifacts and dependencies.](https://cloud.google.com/artifact-registry/docs)


  * [Cloud CodeIDE support to write, run, and debug Kubernetes applications.](https://cloud.google.com/code)


  * [Cloud BuildContinuous integration and continuous delivery platform.](https://cloud.google.com/build)


  * [Cloud DeployFully managed continuous delivery to GKE and Cloud Run.](https://cloud.google.com/deploy)


  * [Cloud Deployment ManagerService for creating and managing Google Cloud resources.](https://cloud.google.com/deployment-manager/docs)


  * [Cloud SDKCommand-line tools and libraries for Google Cloud.](https://cloud.google.com/sdk)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Cloud Source RepositoriesPrivate Git repository to store, manage, and track code.](https://cloud.google.com/source-repositories/docs)


  * [Infrastructure ManagerAutomate infrastructure management with Terraform.](https://cloud.google.com/infrastructure-manager/docs)


  * [Cloud WorkstationsManaged and secure development environments in the cloud.](https://cloud.google.com/workstations)


  * [Gemini Code AssistAI-powered assistant available across Google Cloud and your IDE.](https://cloud.google.com/products/gemini/code-assist)


  * Not seeing what you're looking for?
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Distributed Cloud](https://cloud.google.com/distributed-cloud)


  * [Google Distributed Cloud ConnectedDistributed cloud services for edge workloads.](https://cloud.google.com/distributed-cloud-connected)


  * [Google Distributed Cloud Air-gappedDistributed cloud for air-gapped workloads.](https://cloud.google.com/distributed-cloud-air-gapped)



  * Hybrid and Multicloud


  * [Google Kubernetes EngineManaged environment for running containerized apps.](https://cloud.google.com/kubernetes-engine)


  * [Apigee API ManagementAPI management, development, and security platform.](https://cloud.google.com/apigee)


  * [Migrate to ContainersTool to move workloads and existing applications to GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Cloud BuildService for executing builds on Google Cloud infrastructure.](https://cloud.google.com/build)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Cloud Service MeshFully managed service mesh based on Envoy and Istio.](https://cloud.google.com/products/service-mesh)


  * [Google Distributed CloudFully managed solutions for the edge and data centers.](https://cloud.google.com/distributed-cloud)



  * Industry Specific


  * [Anti Money Laundering AIDetect suspicious, potential money laundering activity with AI.](https://cloud.google.com/anti-money-laundering-ai)


  * [Cloud Healthcare APISolution for bridging existing care systems and apps on Google Cloud.](https://cloud.google.com/healthcare-api)


  * [Device Connect for FitbitGain a 360-degree patient view with connected Fitbit data on Google Cloud.](https://cloud.google.com/device-connect)


  * [Telecom Network AutomationReady to use cloud-native automation for telecom networks.](https://cloud.google.com/telecom-network-automation)


  * [Telecom Data FabricTelecom data management and analytics with an automated approach.](https://cloud.google.com/telecom-data-fabric)


  * [Telecom Subscriber InsightsIngests data to improve subscriber acquisition and retention.](https://cloud.google.com/telecom-subscriber-insights)


  * [Spectrum Access System (SAS)Controls fundamental access to the Citizens Broadband Radio Service (CBRS).](https://cloud.google.com/products/spectrum-access-system)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Integration Services](https://cloud.google.com/integration-services)


  * [Application IntegrationConnect to 3rd party apps and enable data consistency without code.](https://cloud.google.com/application-integration)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [Apigee API ManagementManage the full life cycle of APIs anywhere with visibility and control.](https://cloud.google.com/apigee)


  * [Cloud TasksTask management service for asynchronous task execution.](https://cloud.google.com/tasks/docs)


  * [Cloud SchedulerCron job scheduler for task automation and management.](https://cloud.google.com/scheduler/docs)


  * [Managed Service for Apache SparkZero-ops serverless or managed clusters, accelerated by Lightning Engine.](https://cloud.google.com/products/managed-service-for-apache-spark)


  * [Cloud Data FusionData integration for building and managing data pipelines.](https://cloud.google.com/data-fusion)


  * [Managed Service for Apache AirflowWorkflow orchestration service built on Apache Airflow.](https://cloud.google.com/products/managed-service-for-apache-airflow)


  * [Pub/SubMessaging service for event ingestion and delivery.](https://cloud.google.com/pubsub)


  * [EventarcBuild an event-driven architecture that can connect any service.](https://cloud.google.com/eventarc/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Management Tools](https://cloud.google.com/products/management)


  * [Cloud ShellInteractive shell environment with a built-in command line.](https://cloud.google.com/shell/docs)


  * [Cloud consoleWeb-based interface for managing and monitoring cloud apps.](https://cloud.google.com/cloud-console)


  * [Cloud EndpointsDeployment and development management for APIs on Google Cloud.](https://cloud.google.com/endpoints/docs)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Cloud APIsProgrammatic interfaces for Google Cloud services.](https://cloud.google.com/apis)


  * [Service CatalogService catalog for admins managing internal enterprise solutions.](https://cloud.google.com/service-catalog/docs)


  * [Cost ManagementTools for monitoring, controlling, and optimizing your costs.](https://cloud.google.com/cost-management)


  * [ObservabilityMonitoring, logging, and application performance suite.](https://cloud.google.com/products/observability)


  * [Carbon FootprintDashboard to view and export Google Cloud carbon emissions reports.](https://cloud.google.com/carbon-footprint)


  * [Config ConnectorKubernetes add-on for managing Google Cloud resources.](https://cloud.google.com/config-connector/docs/overview)


  * [Active AssistTools for easily managing performance, security, and cost.](https://cloud.google.com/solutions/active-assist)


  * Not seeing what you're looking for?
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Maps and Geospatial](https://cloud.google.com/solutions/geospatial)


  * [Earth EngineGeospatial platform for Earth observation data and analysis.](https://cloud.google.com/earth-engine)


  * [Google Maps PlatformCreate immersive location experiences and improve business operations.](https://mapsplatform.google.com)



  * Media Services


  * [Cloud CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Live Stream APIService to convert live video and package for streaming.](https://cloud.google.com/livestream/docs)


  * [OpenCueOpen source render manager for visual effects and animation.](https://www.opencue.io/docs/getting-started/)


  * [Transcoder APIConvert video files and package them for optimized delivery.](https://cloud.google.com/transcoder/docs)


  * [Video Stitcher APIService for dynamic or server side ad insertion.](https://cloud.google.com/video-stitcher/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Migration](https://cloud.google.com/products/cloud-migration)


  * [Migration CenterUnified platform for migrating and modernizing with Google Cloud.](https://cloud.google.com/migration-center/docs)


  * [Application MigrationApp migration to the cloud for low-cost refresh cycles.](https://cloud.google.com/solutions/application-migration)


  * [Migrate to Virtual MachinesComponents for migrating VMs and physical servers to Compute Engine.](https://cloud.google.com/products/cloud-migration/virtual-machines)


  * [Cloud Foundation ToolkitReference templates for Deployment Manager and Terraform.](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)


  * [Database Migration ServiceServerless, minimal downtime migrations to Cloud SQL.](https://cloud.google.com/database-migration)


  * [Migrate to ContainersComponents for migrating VMs into system containers on GKE.](https://cloud.google.com/products/cloud-migration/containers)


  * [Data Analytics Migration ServicesStreamlined data warehouse and data lake migration tooling and incentives.](https://cloud.google.com/solutions/data-migration)


  * [Rapid Migration and Modernization ProgramEnd-to-end migration program to simplify your path to the cloud.](https://cloud.google.com/solutions/cloud-migration-program)


  * [Transfer ApplianceStorage server for moving large volumes of data to Google Cloud.](https://cloud.google.com/transfer-appliance/docs/4.0/overview)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [VMware EngineMigrate and run your VMware workloads natively on Google Cloud.](https://cloud.google.com/vmware-engine)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Networking](https://cloud.google.com/products/networking)


  * [Cloud ArmorSecurity policies and defense against web and DDoS attacks.](https://cloud.google.com/security/products/armor)


  * [Cloud CDN and Media CDNContent delivery network for serving web and video content.](https://cloud.google.com/cdn)


  * [Cloud DNSDomain name system for reliable and low-latency name lookups.](https://cloud.google.com/dns)


  * [Cloud Load BalancingService for distributing traffic across applications and regions.](https://cloud.google.com/load-balancing)


  * [Cloud NATNAT service for giving private instances internet access.](https://cloud.google.com/nat)


  * [Cloud ConnectivityConnectivity options for VPN, peering, and enterprise needs.](https://cloud.google.com/hybrid-connectivity)


  * [Network Connectivity CenterConnectivity management to help simplify and scale networks.](https://cloud.google.com/network-connectivity-center)


  * [Network Intelligence CenterNetwork monitoring, verification, and optimization platform.](https://cloud.google.com/network-intelligence-center)


  * [Network Service TiersCloud network options based on performance, availability, and cost.](https://cloud.google.com/network-tiers)


  * [Virtual Private CloudSingle VPC for an entire organization, isolated within projects.](https://cloud.google.com/vpc)


  * [Private Service ConnectSecure connection between your VPC and services.](https://cloud.google.com/private-service-connect)


  * Not seeing what you're looking for?
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Operations](https://cloud.google.com/products/operations)


  * [Cloud LoggingGoogle Cloud audit, platform, and application logs management.](https://cloud.google.com/logging)


  * [Cloud MonitoringInfrastructure and application health with rich metrics.](https://cloud.google.com/monitoring)


  * [Error ReportingApplication error identification and analysis.](https://cloud.google.com/error-reporting/docs/grouping-errors)


  * [Managed Service for PrometheusFully-managed Prometheus on Google Cloud.](https://cloud.google.com/managed-prometheus)


  * [Cloud TraceTracing system collecting latency data from applications.](https://cloud.google.com/trace/docs)


  * [Cloud ProfilerCPU and heap profiler for analyzing application performance.](https://cloud.google.com/profiler/docs)


  * [Cloud QuotasManage quotas for all Google Cloud services.](https://cloud.google.com/docs/quotas)



  * Productivity and Collaboration


  * [AppSheetNo-code development platform to build and extend applications.](https://about.appsheet.com/home/)


  * [AppSheet AutomationBuild automations and applications on a unified platform.](https://cloud.google.com/appsheet/automation)


  * [Gemini for businessSecure platform to discover, create, run, and govern AI agents for employees.](https://cloud.google.com/gemini-enterprise)


  * [Google WorkspaceCollaboration and productivity tools for individuals and organizations.](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)


  * [Google Workspace EssentialsSecure video meetings and modern collaboration for teams.](https://workspace.google.com/essentials/)


  * [Cloud IdentityUnified platform for IT admins to manage user devices and apps.](https://cloud.google.com/identity)


  * [Chrome EnterpriseChromeOS, Chrome browser, and Chrome devices built for business.](https://chromeenterprise.google)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Security and Identity](https://cloud.google.com/products/security-and-identity)


  * [Cloud IAMPermissions management system for Google Cloud resources.](https://cloud.google.com/security/products/iam)


  * [Sensitive Data ProtectionDiscover, classify, and protect your valuable data assets.](https://cloud.google.com/security/products/sensitive-data-protection)


  * [Mandiant Managed DefenseFind and eliminate threats with confidence 24x7.](https://cloud.google.com/security/products/managed-defense)


  * [Google Threat IntelligenceKnow who’s targeting you.](https://cloud.google.com/security/products/threat-intelligence)


  * [Security Command CenterPlatform for defending against threats to your Google Cloud assets.](https://cloud.google.com/security/products/security-command-center)


  * [Cloud Key ManagementManage encryption keys on Google Cloud.](https://cloud.google.com/security/products/security-key-management)


  * [Mandiant Incident ResponseMinimize the impact of a breach.](https://cloud.google.com/security/consulting/mandiant-incident-response-services)


  * [Chrome Enterprise PremiumGet secure enterprise browsing with extensive endpoint visibility.](https://docs.cloud.google.com/chrome-enterprise-premium/)


  * [Assured WorkloadsCompliance and security controls for sensitive workloads.](https://cloud.google.com/security/products/assured-workloads)


  * [Google Security OperationsDetect, investigate, and respond to cyber threats.](https://cloud.google.com/security/products/security-operations)


  * [Mandiant ConsultingGet expert guidance before, during, and after an incident.](https://cloud.google.com/security/consulting/mandiant-services)


  * Not seeing what you're looking for?
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Serverless](https://cloud.google.com/serverless)


  * [Cloud RunFully managed environment for running containerized apps.](https://cloud.google.com/run)


  * [Cloud FunctionsPlatform for creating functions that respond to cloud events.](https://cloud.google.com/functions)


  * [App EngineServerless application platform for apps and back ends.](https://cloud.google.com/appengine)


  * [WorkflowsWorkflow orchestration for serverless products and API services.](https://cloud.google.com/workflows)


  * [API GatewayDevelop, deploy, secure, and manage APIs with a fully managed gateway.](https://cloud.google.com/api-gateway/docs)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Storage](https://cloud.google.com/products/storage)


  * [Cloud StorageObject storage that’s secure, durable, and scalable.](https://cloud.google.com/storage)


  * [Block StorageHigh-performance storage for AI, analytics, databases, and enterprise applications.](https://cloud.google.com/products/block-storage)


  * [FilestoreFile storage that is highly scalable and secure.](https://cloud.google.com/filestore)


  * [Persistent DiskBlock storage for virtual machine instances running on Google Cloud.](https://cloud.google.com/persistent-disk)


  * [Cloud Storage for FirebaseObject storage for storing and serving user-generated content.](https://firebase.google.com/products/storage)


  * [Local SSDBlock storage that is locally attached for high-performance needs.](https://cloud.google.com/products/local-ssd)


  * [Storage Transfer ServiceData transfers from online and on-premises sources to Cloud Storage.](https://cloud.google.com/storage-transfer-service)


  * [Google Cloud Managed LustreHigh performance managed parallel file service.](https://cloud.google.com/products/managed-lustre)


  * [Google Cloud NetApp VolumesFile storage service for NFS, SMB, and multi-protocol environments.](https://cloud.google.com/netapp-volumes)


  * [Backup and DR ServiceService for centralized, application-consistent data protection.](https://cloud.google.com/backup-disaster-recovery)



  * [![](https://www.gstatic.com/cloud/images/navigation/forward.svg)Web3](https://cloud.google.com/web3)


  * [Blockchain Node EngineFully managed node hosting for developing on the blockchain.](https://cloud.google.com/blockchain-node-engine)


  * [Blockchain RPCEnterprise-grade RPC for building on the blockchain.](https://cloud.google.com/products/blockchain-rpc)



close

  * Save money with our transparent approach to pricing
  * Google Cloud's pay-as-you-go pricing offers automatic savings based on monthly usage and discounted rates for prepaid resources. Contact us today to get a quote.
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)




  * Pricing overview and tools
  * [Google Cloud pricingPay only for what you use with no lock-in.](https://cloud.google.com/pricing)

  * [Pricing calculatorCalculate your cloud savings.](https://cloud.google.com/products/calculator)

  * [Google Cloud free tierExplore products with free monthly usage.](https://cloud.google.com/free)




  * [Cost optimization frameworkGet best practices to optimize workload costs.](https://cloud.google.com/architecture/framework/cost-optimization)

  * [Cost management toolsTools to monitor and control your costs.](https://cloud.google.com/cost-management)




  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)

  * [Cloud SQL](https://cloud.google.com/sql/pricing)

  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)

  * [Cloud Storage](https://cloud.google.com/storage/pricing)

  * [BigQuery](https://cloud.google.com/bigquery/pricing)

  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)




close

  * Learn & build
  * [Google Cloud Free Program$300 in free credits and 20+ free products.](https://cloud.google.com/free)

  * [Solution GeneratorGet AI generated solution recommendations.](https://cloud.google.com/solution-generator)

  * [QuickstartsGet tutorials and walkthroughs.](https://cloud.google.com/docs/tutorials?doctype=quickstart)

  * [BlogRead our latest product news and stories.](https://cloud.google.com/blog)




  * [Learning HubGrow your career with role-based training.](https://cloud.google.com/learn)

  * [Google Cloud certificationPrepare and register for certifications.](https://cloud.google.com/certification)

  * [Cloud computing basicsLearn more about cloud computing basics.](https://cloud.google.com/discover)

  * [Cloud Architecture CenterGet reference architectures and best practices.](https://cloud.google.com/architecture)




  * Connect
  * [InnovatorsJoin Google Cloud's developer program.](https://cloud.google.com/innovators/innovatorsplus)

  * [Developer CenterStay in the know and stay connected.](https://cloud.google.com/developers)

  * [Events and webinarsBrowse upcoming and on demand events.](https://cloud.google.com/events)

  * [Google Cloud CommunityAsk questions, find answers, and connect.](https://discuss.google.dev/c/google-cloud/14)




  * Consulting and Partners
  * [Google Cloud ConsultingWork with our experts on cloud projects.](https://cloud.google.com/consulting)

  * [Google Cloud MarketplaceDeploy ready-to-go solutions in a few clicks.](https://cloud.google.com/marketplace)

  * [Find a partnerExplore the benefits of working with a partner.](https://cloud.google.com/partners)

  * [Google Cloud partnersLearn about the ecosystem and resources.](https://partners.cloud.google.com)




close

[![Google Cloud](https://www.gstatic.com/cgc/google-cloud-logo-fullcolor.svg)](https://cloud.google.com/)

  * [Overview](https://cloud.google.com/why-google-cloud)
    * arrow_forward
  * [Solutions](https://cloud.google.com/solutions)
    * arrow_forward
  * [Products](https://cloud.google.com/products)
    * arrow_forward
  * [Pricing](https://cloud.google.com/pricing)
    * arrow_forward
  * [Resources](https://cloud.google.com/docs/get-started)
    * arrow_forward
  * [Docs](https://cloud.google.com/docs)
  * [Support](https://cloud.google.com/support-hub)
  * [Console](https://console.cloud.google.com/)



  * Accelerate your digital transformation
  * [Learn more](https://cloud.google.com/transform)
  * Key benefits
  * [Why Google Cloud](https://cloud.google.com/why-google-cloud)
  * [AI and Agents](https://cloud.google.com/ai)
  * [Multicloud](https://cloud.google.com/multicloud)
  * [Global infrastructure](https://cloud.google.com/infrastructure)
  * [Data Cloud](https://cloud.google.com/data-cloud)
  * [Modern Infrastructure Cloud](https://cloud.google.com/solutions/modern-infrastructure)
  * [Security](https://cloud.google.com/security)
  * [Productivity and collaboration](https://workspace.google.com)
  * Reports and insights
  * [Executive insights](https://cloud.google.com/executive-insights)
  * [Analyst reports](https://cloud.google.com/analyst-reports)
  * [Whitepapers](https://cloud.google.com/whitepapers)
  * [Customer stories](https://cloud.google.com/customers)


  * [Industry Solutions](https://cloud.google.com/solutions#industry-solutions)
  * [Retail](https://cloud.google.com/solutions/retail)
  * [Consumer Packaged Goods](https://cloud.google.com/solutions/cpg)
  * [Financial Services](https://cloud.google.com/solutions/financial-services)
  * [Healthcare and Life Sciences](https://cloud.google.com/solutions/healthcare-life-sciences)
  * [Media and Entertainment](https://cloud.google.com/solutions/media-entertainment)
  * [Telecommunications](https://cloud.google.com/solutions/telecommunications)
  * [Games](https://cloud.google.com/solutions/games)
  * [Manufacturing](https://cloud.google.com/solutions/manufacturing)
  * [Supply Chain and Logistics](https://cloud.google.com/solutions/supply-chain-logistics)
  * [Government](https://cloud.google.com/gov)
  * [Education](https://cloud.google.com/edu/higher-education)
  * [See all industry solutions](https://cloud.google.com/solutions#industry-solutions)
  * [See all solutions](https://cloud.google.com/solutions)
  * [Application Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Application Modernization with AI](https://cloud.google.com/solutions/application-modernization-with-ai)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Mainframe Modernization](https://cloud.google.com/solutions/mainframe-modernization)
  * [Database Modernization](https://cloud.google.com/products/databases)
  * [Data Lake Modernization](https://cloud.google.com/solutions/data-lakehouse)
  * [Data Warehouse Modernization](https://cloud.google.com/solutions/data-migration)
  * [APIs](https://cloud.google.com/solutions/apis-and-applications)
  * [Platform Eng](https://cloud.google.com/solutions/platform-engineering)
  * [DevOps Best Practices](https://cloud.google.com/devops)
  * [SRE Principles](https://cloud.google.com/sre)
  * [Artificial Intelligence](https://cloud.google.com/solutions/ai)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Gemini for enterprise](https://cloud.google.com/gemini-enterprise)
  * [AI Commerce Search](https://cloud.google.com/gemini-enterprise-cx/commerce)
  * [Google Cloud with Gemini](https://cloud.google.com/ai/gemini)
  * [Physical AI](https://cloud.google.com/solutions/physical-ai)
  * [APIs and Applications](https://cloud.google.com/solutions/apis-and-applications)
  * [New Business Channels Using APIs](https://cloud.google.com/solutions/new-channels-using-apis)
  * [Unlocking Legacy Applications Using APIs](https://cloud.google.com/solutions/unlocking-legacy-applications)
  * [Open Banking APIx](https://cloud.google.com/solutions/open-banking-apix)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [Data Migration](https://cloud.google.com/solutions/data-migration)
  * [Data Lakehouse](https://cloud.google.com/solutions/data-lakehouse)
  * [Real-time Analytics](https://cloud.google.com/solutions/stream-analytics)
  * [Marketing Analytics](https://cloud.google.com/solutions/marketing-analytics)
  * [Datasets](https://cloud.google.com/datasets)
  * [Business Intelligence](https://cloud.google.com/solutions/business-intelligence)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Geospatial Analytics](https://cloud.google.com/solutions/geospatial)
  * [Data Science](https://cloud.google.com/solutions/data-science)
  * [Databases](https://cloud.google.com/solutions/databases)
  * [Database Migration](https://cloud.google.com/solutions/database-migration)
  * [Database Modernization](https://cloud.google.com/solutions/database-modernization)
  * [Databases for Games](https://cloud.google.com/solutions/databases/games)
  * [Google Cloud Databases](https://cloud.google.com/products/databases)
  * [Migrate Oracle workloads to Google Cloud](https://cloud.google.com/solutions/oracle)
  * [Open Source Databases](https://cloud.google.com/solutions/open-source-databases)
  * [SQL Server on Google Cloud](https://cloud.google.com/sql-server)
  * [Gemini for Databases](https://cloud.google.com/products/gemini/databases)
  * [Infrastructure Modernization](https://cloud.google.com/solutions/modernize)
  * [Google Cloud Modernize](https://cloud.google.com/solutions/modernize)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [AI Hypercomputer](https://cloud.google.com/ai-infrastructure)
  * [Rapid Migration and Modernization Program (RaMP)](https://cloud.google.com/solutions/cloud-migration-program)
  * [Data Center Exits](https://cloud.google.com/solutions/data-center-migration)
  * [Application Modernization & Migration](https://cloud.google.com/solutions/application-migration)
  * [Database Modernization & Migration](https://cloud.google.com/products/databases)
  * [Cross-Cloud Networking](https://cloud.google.com/solutions/cross-cloud-network)
  * [High Performance Computing (HPC)](https://cloud.google.com/solutions/hpc)
  * [VMware](https://cloud.google.com/vmware-engine)
  * [SAP](https://cloud.google.com/solutions/sap)
  * [Windows](https://cloud.google.com/windows)
  * [Productivity and Collaboration](https://workspace.google.com/enterprise/)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security](https://cloud.google.com/solutions/security)
  * [Agentic SOC](https://cloud.google.com/solutions/agentic-soc)
  * [Web App and API Protection](https://cloud.google.com/security/solutions/web-app-and-api-protection)
  * [Security and Resilience Framework](https://cloud.google.com/security/solutions/security-and-resilience)
  * [Risk and compliance as code (RCaC)](https://cloud.google.com/solutions/risk-and-compliance-as-code)
  * [Software Supply Chain Security](https://cloud.google.com/security/solutions/software-supply-chain-security)
  * [Security Foundation](https://cloud.google.com/security/solutions/security-foundation)
  * [Google Cloud Cybershield™](https://cloud.google.com/security/solutions/secops-cybershield)
  * [Startups and SMB](https://cloud.google.com/solutions#section-13)
  * [Startup Program](https://cloud.google.com/startup)
  * [Small and Medium Business](https://cloud.google.com/solutions/smb)
  * [Software as a Service](https://cloud.google.com/saas)


  * Featured Products
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Cloud Run](https://cloud.google.com/run)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Looker](https://cloud.google.com/looker)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [See all products (100+)](https://cloud.google.com/products#featured-products)
  * [AI and Machine Learning](https://cloud.google.com/products/ai)
  * [Gemini platform](https://cloud.google.com/products/gemini-enterprise-agent-platform)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Gemini for customer experience](https://cloud.google.com/gemini-enterprise-cx)
  * [Model Garden](https://console.cloud.google.com/agent-platform/model-garden)
  * [Customer Experience Agent Studio](https://cloud.google.com/gemini-enterprise-cx/cx-agent-studio)
  * [Agent Search](https://cloud.google.com/products/gemini-enterprise-agent-platform/agent-search)
  * [Speech-to-Text](https://cloud.google.com/speech-to-text)
  * [Text-to-Speech](https://cloud.google.com/text-to-speech)
  * [Translation AI](https://cloud.google.com/translate)
  * [Vision AI](https://cloud.google.com/vision)
  * [Contact Center as a Service](https://cloud.google.com/solutions/contact-center-ai-platform)
  * [See all AI and machine learning products](https://cloud.google.com/products?pds=CAE#ai-and-machine-learning)
  * Business Intelligence
  * [Looker](https://cloud.google.com/looker)
  * [Data Studio](https://cloud.google.com/data-studio)
  * [Compute](https://cloud.google.com/products/compute)
  * [Compute Engine](https://cloud.google.com/products/compute)
  * [App Engine](https://cloud.google.com/appengine)
  * [Cloud GPUs](https://cloud.google.com/gpu)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Spot VMs](https://cloud.google.com/spot-vms)
  * [Batch](https://cloud.google.com/batch)
  * [Sole-Tenant Nodes](https://cloud.google.com/compute/docs/nodes/sole-tenant-nodes)
  * [Bare Metal](https://cloud.google.com/bare-metal)
  * [Recommender](https://cloud.google.com/recommender/docs/whatis-activeassist)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [See all compute products](https://cloud.google.com/products?pds=CAUSAQw#compute)
  * [Containers](https://cloud.google.com/containers)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Build](https://cloud.google.com/build)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Deep Learning Containers](https://cloud.google.com/deep-learning-containers/docs)
  * [Knative](https://knative.dev/docs/)
  * [Data Analytics](https://cloud.google.com/solutions/data-analytics-and-ai)
  * [BigQuery](https://cloud.google.com/bigquery)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Dataflow](https://cloud.google.com/products/dataflow)
  * [Looker](https://cloud.google.com/looker)
  * [Lakehouse](https://cloud.google.com/products/lakehouse)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Knowledge Catalog](https://cloud.google.com/products/knowledge-catalog)
  * [Data Analytics Agents](https://cloud.google.com/use-cases/data-analytics-agents)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Managed Service for Apache Kafka](https://cloud.google.com/products/managed-service-for-apache-kafka)
  * [See all data analytics products](https://cloud.google.com/products?pds=CAQ#data-analytics)
  * [Databases](https://cloud.google.com/products/databases)
  * [AlloyDB for PostgreSQL](https://cloud.google.com/alloydb)
  * [Cloud SQL](https://cloud.google.com/sql)
  * [Firestore](https://cloud.google.com/firestore)
  * [Spanner](https://cloud.google.com/spanner)
  * [Bigtable](https://cloud.google.com/bigtable)
  * [Datastream](https://cloud.google.com/datastream)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Bare Metal Solution](https://cloud.google.com/bare-metal)
  * [Memorystore](https://cloud.google.com/memorystore)
  * [Developer Tools](https://cloud.google.com/products/tools)
  * [Artifact Registry](https://cloud.google.com/artifact-registry/docs)
  * [Cloud Code](https://cloud.google.com/code)
  * [Cloud Build](https://cloud.google.com/build)
  * [Cloud Deploy](https://cloud.google.com/deploy)
  * [Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs)
  * [Cloud SDK](https://cloud.google.com/sdk)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Cloud Source Repositories](https://cloud.google.com/source-repositories/docs)
  * [Infrastructure Manager](https://cloud.google.com/infrastructure-manager/docs)
  * [Cloud Workstations](https://cloud.google.com/workstations)
  * [Gemini Code Assist](https://cloud.google.com/products/gemini/code-assist)
  * [See all developer tools](https://cloud.google.com/products?pds=CAI#developer-tools)
  * [Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * [Google Distributed Cloud Connected](https://cloud.google.com/distributed-cloud-connected)
  * [Google Distributed Cloud Air-gapped](https://cloud.google.com/distributed-cloud-air-gapped)
  * Hybrid and Multicloud
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Cloud Build](https://cloud.google.com/build)
  * [Observability](https://cloud.google.com/products/observability)
  * [Cloud Service Mesh](https://cloud.google.com/products/service-mesh)
  * [Google Distributed Cloud](https://cloud.google.com/distributed-cloud)
  * Industry Specific
  * [Anti Money Laundering AI](https://cloud.google.com/anti-money-laundering-ai)
  * [Cloud Healthcare API](https://cloud.google.com/healthcare-api)
  * [Device Connect for Fitbit](https://cloud.google.com/device-connect)
  * [Telecom Network Automation](https://cloud.google.com/telecom-network-automation)
  * [Telecom Data Fabric](https://cloud.google.com/telecom-data-fabric)
  * [Telecom Subscriber Insights](https://cloud.google.com/telecom-subscriber-insights)
  * [Spectrum Access System (SAS)](https://cloud.google.com/products/spectrum-access-system)
  * [Integration Services](https://cloud.google.com/integration-services)
  * [Application Integration](https://cloud.google.com/application-integration)
  * [Workflows](https://cloud.google.com/workflows)
  * [Apigee API Management](https://cloud.google.com/apigee)
  * [Cloud Tasks](https://cloud.google.com/tasks/docs)
  * [Cloud Scheduler](https://cloud.google.com/scheduler/docs)
  * [Managed Service for Apache Spark](https://cloud.google.com/products/managed-service-for-apache-spark)
  * [Cloud Data Fusion](https://cloud.google.com/data-fusion)
  * [Managed Service for Apache Airflow](https://cloud.google.com/products/managed-service-for-apache-airflow)
  * [Pub/Sub](https://cloud.google.com/pubsub)
  * [Eventarc](https://cloud.google.com/eventarc/docs)
  * [Management Tools](https://cloud.google.com/products/management)
  * [Cloud Shell](https://cloud.google.com/shell/docs)
  * [Cloud console](https://cloud.google.com/cloud-console)
  * [Cloud Endpoints](https://cloud.google.com/endpoints/docs)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Cloud APIs](https://cloud.google.com/apis)
  * [Service Catalog](https://cloud.google.com/service-catalog/docs)
  * [Cost Management](https://cloud.google.com/cost-management)
  * [Observability](https://cloud.google.com/products/observability)
  * [Carbon Footprint](https://cloud.google.com/carbon-footprint)
  * [Config Connector](https://cloud.google.com/config-connector/docs/overview)
  * [Active Assist](https://cloud.google.com/solutions/active-assist)
  * [See all management tools](https://cloud.google.com/products?pds=CAY#managment-tools)
  * [Maps and Geospatial](https://cloud.google.com/solutions/geospatial)
  * [Earth Engine](https://cloud.google.com/earth-engine)
  * [Google Maps Platform](https://mapsplatform.google.com)
  * Media Services
  * [Cloud CDN](https://cloud.google.com/cdn)
  * [Live Stream API](https://cloud.google.com/livestream/docs)
  * [OpenCue](https://www.opencue.io/docs/getting-started/)
  * [Transcoder API](https://cloud.google.com/transcoder/docs)
  * [Video Stitcher API](https://cloud.google.com/video-stitcher/docs)
  * [Migration](https://cloud.google.com/products/cloud-migration)
  * [Migration Center](https://cloud.google.com/migration-center/docs)
  * [Application Migration](https://cloud.google.com/solutions/application-migration)
  * [Migrate to Virtual Machines](https://cloud.google.com/products/cloud-migration/virtual-machines)
  * [Cloud Foundation Toolkit](https://cloud.google.com/docs/terraform/blueprints/terraform-blueprints)
  * [Database Migration Service](https://cloud.google.com/database-migration)
  * [Migrate to Containers](https://cloud.google.com/products/cloud-migration/containers)
  * [Data Analytics Migration Services](https://cloud.google.com/solutions/data-migration)
  * [Rapid Migration and Modernization Program](https://cloud.google.com/solutions/cloud-migration-program)
  * [Transfer Appliance](https://cloud.google.com/transfer-appliance/docs/4.0/overview)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [VMware Engine](https://cloud.google.com/vmware-engine)
  * [Networking](https://cloud.google.com/products/networking)
  * [Cloud Armor](https://cloud.google.com/security/products/armor)
  * [Cloud CDN and Media CDN](https://cloud.google.com/cdn)
  * [Cloud DNS](https://cloud.google.com/dns)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing)
  * [Cloud NAT](https://cloud.google.com/nat)
  * [Cloud Connectivity](https://cloud.google.com/hybrid-connectivity)
  * [Network Connectivity Center](https://cloud.google.com/network-connectivity-center)
  * [Network Intelligence Center](https://cloud.google.com/network-intelligence-center)
  * [Network Service Tiers](https://cloud.google.com/network-tiers)
  * [Virtual Private Cloud](https://cloud.google.com/vpc)
  * [Private Service Connect](https://cloud.google.com/private-service-connect)
  * [See all networking products](https://cloud.google.com/products?pds=CAUSAQ0#networking)
  * [Operations](https://cloud.google.com/products/operations)
  * [Cloud Logging](https://cloud.google.com/logging)
  * [Cloud Monitoring](https://cloud.google.com/monitoring)
  * [Error Reporting](https://cloud.google.com/error-reporting/docs/grouping-errors)
  * [Managed Service for Prometheus](https://cloud.google.com/managed-prometheus)
  * [Cloud Trace](https://cloud.google.com/trace/docs)
  * [Cloud Profiler](https://cloud.google.com/profiler/docs)
  * [Cloud Quotas](https://cloud.google.com/docs/quotas)
  * Productivity and Collaboration
  * [AppSheet](https://about.appsheet.com/home/)
  * [AppSheet Automation](https://cloud.google.com/appsheet/automation)
  * [Gemini for business](https://cloud.google.com/gemini-enterprise)
  * [Google Workspace](https://workspace.google.com/solutions/enterprise/?enterprise-benefits_activeEl=connect/)
  * [Google Workspace Essentials](https://workspace.google.com/essentials/)
  * [Cloud Identity](https://cloud.google.com/identity)
  * [Chrome Enterprise](https://chromeenterprise.google)
  * [Security and Identity](https://cloud.google.com/products/security-and-identity)
  * [Cloud IAM](https://cloud.google.com/security/products/iam)
  * [Sensitive Data Protection](https://cloud.google.com/security/products/sensitive-data-protection)
  * [Mandiant Managed Defense](https://cloud.google.com/security/products/managed-defense)
  * [Google Threat Intelligence](https://cloud.google.com/security/products/threat-intelligence)
  * [Security Command Center](https://cloud.google.com/security/products/security-command-center)
  * [Cloud Key Management](https://cloud.google.com/security/products/security-key-management)
  * [Mandiant Incident Response](https://cloud.google.com/security/consulting/mandiant-incident-response-services)
  * [Chrome Enterprise Premium](https://docs.cloud.google.com/chrome-enterprise-premium/)
  * [Assured Workloads](https://cloud.google.com/security/products/assured-workloads)
  * [Google Security Operations](https://cloud.google.com/security/products/security-operations)
  * [Mandiant Consulting](https://cloud.google.com/security/consulting/mandiant-services)
  * [See all security and identity products](https://cloud.google.com/products?pds=CAg#security-and-identity)
  * [Serverless](https://cloud.google.com/serverless)
  * [Cloud Run](https://cloud.google.com/run)
  * [Cloud Functions](https://cloud.google.com/functions)
  * [App Engine](https://cloud.google.com/appengine)
  * [Workflows](https://cloud.google.com/workflows)
  * [API Gateway](https://cloud.google.com/api-gateway/docs)
  * [Storage](https://cloud.google.com/products/storage)
  * [Cloud Storage](https://cloud.google.com/storage)
  * [Block Storage](https://cloud.google.com/products/block-storage)
  * [Filestore](https://cloud.google.com/filestore)
  * [Persistent Disk](https://cloud.google.com/persistent-disk)
  * [Cloud Storage for Firebase](https://firebase.google.com/products/storage)
  * [Local SSD](https://cloud.google.com/products/local-ssd)
  * [Storage Transfer Service](https://cloud.google.com/storage-transfer-service)
  * [Google Cloud Managed Lustre](https://cloud.google.com/products/managed-lustre)
  * [Google Cloud NetApp Volumes](https://cloud.google.com/netapp-volumes)
  * [Backup and DR Service](https://cloud.google.com/backup-disaster-recovery)
  * [Web3](https://cloud.google.com/web3)
  * [Blockchain Node Engine](https://cloud.google.com/blockchain-node-engine)
  * [Blockchain RPC](https://cloud.google.com/products/blockchain-rpc)


  * Save money with our transparent approach to pricing
  * [Request a quote](https://cloud.google.com/contact/form?direct=true)
  * Pricing overview and tools
  * [Google Cloud pricing](https://cloud.google.com/pricing)
  * [Pricing calculator](https://cloud.google.com/products/calculator)
  * [Google Cloud free tier](https://cloud.google.com/free)
  * [Cost optimization framework](https://cloud.google.com/architecture/framework/cost-optimization)
  * [Cost management tools](https://cloud.google.com/cost-management)
  * Product-specific Pricing
  * [Compute Engine](https://cloud.google.com/compute/all-pricing)
  * [Cloud SQL](https://cloud.google.com/sql/pricing)
  * [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [See full price list with 100+ products](https://cloud.google.com/pricing/list)


  * Learn & build
  * [Google Cloud Free Program](https://cloud.google.com/free)
  * [Solution Generator](https://cloud.google.com/solution-generator)
  * [Quickstarts](https://cloud.google.com/docs/tutorials?doctype=quickstart)
  * [Blog](https://cloud.google.com/blog)
  * [Learning Hub](https://cloud.google.com/learn)
  * [Google Cloud certification](https://cloud.google.com/certification)
  * [Cloud computing basics](https://cloud.google.com/discover)
  * [Cloud Architecture Center](https://cloud.google.com/architecture)
  * Connect
  * [Innovators](https://cloud.google.com/innovators/innovatorsplus)
  * [Developer Center](https://cloud.google.com/developers)
  * [Events and webinars](https://cloud.google.com/events)
  * [Google Cloud Community](https://discuss.google.dev/c/google-cloud/14)
  * Consulting and Partners
  * [Google Cloud Consulting](https://cloud.google.com/consulting)
  * [Google Cloud Marketplace](https://cloud.google.com/marketplace)
  * [Find a partner](https://cloud.google.com/partners)
  * [Google Cloud partners](https://partners.cloud.google.com)


