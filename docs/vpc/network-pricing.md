---
url: https://docs.cloud.google.com/vpc/network-pricing/
title: Network pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:25:08.268314+00:00
---

# Network pricing | Google Cloud

> Source: https://docs.cloud.google.com/vpc/network-pricing/

Page Contents




## All networking pricing

This page describes pricing for networking products.

## 

Virtual Private Cloud

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

  


### General network pricing information

**Data transfer**

Data transfer can be traffic coming into a Google Cloud resource (e.g. VM), leaving Google Cloud region out into the internet, or in between two resources within Google Cloud.

A region is a set of buildings operated by Google in a geographic location, such as a data center campus. Traffic can travel as follows:

  * Within the set of buildings at the location, which always used Google's network (intra-zone and intra-region pricing)
  * To another building operated by Google in another location, which always used Google's network (inter-region pricing)
  * To a location not operated by Google over a Cloud Interconnect connection (Cloud Interconnect pricing)
  * To a location not operated by Google  _not_ over a Cloud Interconnect connection (internet data transfer out pricing)



**Premium Tier**

The [Network Service Tiers Premium Tier](https://cloud.google.com/network-tiers/docs/overview#premium_tier) leverages Google's premium backbone to carry traffic to and from your external users. The public internet is usually only used between the user and the closest Google network ingress point.

**Standard Tier**

The [Network Service Tiers Standard Tier](https://cloud.google.com/network-tiers/docs/overview#standard_tier) leverages the public internet to carry traffic between your services and your users. While using the public internet provides a lower quality of service, it is more economical than Premium Tier.

### Inbound data transfer pricing

Traffic type| Price  
---|---  
Inbound data transfer| No charge for inbound data transfer. However there may be a charge for resource that processes data. Services that process inbound data are as follows:

  * [Load balancers](https://cloud.google.com/vpc/network-pricing#lb)
  * [Cloud NAT](https://cloud.google.com/nat/pricing)
  * [Protocol forwarding](https://cloud.google.com/vpc/network-pricing#pf)

Responses to requests count as data transfer out and are charged.  
  
### 

VM-VM data transfer pricing within Google Cloud

This section covers traffic that leaves a Google Cloud VM and travels to another Google Cloud VM. The cost is attributed to the project of the VM that is sending the traffic. This pricing affects Compute Engine VMs, Google Kubernetes Engine (GKE) nodes, and VMs running App Engine flexible environment.

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

  


#### Intra-zone/Inter-zone data transfer

VM-to-VM data transfer when the source and destination VM are in different zones of the same Google Cloud region.

Traffic type| Price  
---|---  
Data transfer to the same Google Cloud zone when using the  _internal_ IPv4 addresses or any IPv6 addresses within the same VPC network1| No charge  
Data transfer to a different Google Cloud zone in the same Google Cloud region when using the internal or external IP addresses within the same VPC network1 (per GiB)_Note: All traffic to and from external IPv4 addresses leaves the zone - regardless of the destination._|  $0.01  
Data transfer to the same or different Google Cloud zone when using external IPv4 addresses or external IPv6 addresses between different VPC networks.| Internet data transfer rates (see below)  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**1** The prices are used regardless of network or subnet. The price for traffic within a zone using internal IP addresses is the same even if the traffic is to a different subnet or network. The price on traffic between zones in the same region is the same if the two instances are in the same subnet, different subnets, or different networks. Pricing is the same whether the instances are in a VPC network or a legacy network.

#### Inter-region data transfer

VM-to-VM data transfer when the source and destination VMs are in different Google Cloud regions. All prices are per GiB in USD.

**Location of VM or Google Cloud service**|  North America| Europe| Asia3| Indonesia| Oceania2| Middle East| South America| Africa  
---|---|---|---|---|---|---|---|---  
**North America**|  $0.02| $0.05| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Europe**|  $0.05| $0.02| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Asia****3**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.11| $0.14| $0.11  
**Indonesia**|  $0.10| $0.10| $0.10| N/A| $0.08| $0.11| $0.14| $0.14  
**Bangkok**|  $0.08| $0.08| $0.08| $0.10| $0.10| $0.18| $0.14| $0.18  
**Oceania****2**|  $0.10| $0.10| $0.10| $0.08| $0.08| $0.11| $0.14| $0.14  
**Middle East**|  $0.11| $0.11| $0.11| $0.11| $0.11| $0.08| $0.14| $0.11  
**South America**|  $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14| $0.14  
**Africa**|  $0.11| $0.11| $0.11| $0.14| $0.14| $0.11| $0.14| $0.08  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**2** Oceania includes Australia, New Zealand, and surrounding Pacific Ocean islands such as Papua New Guinea and Fiji. This region excludes Hawaii.

**3** Includes all regions in Asia except Indonesia and Bangkok

### 

VM-to-Google service

This section covers traffic that leaves a Google Cloud VM and travels to a Google service. The cost is attributed to the project of the VM that is sending the traffic. This pricing affects Compute Engine VMs, Google Kubernetes Engine nodes, and VMs running App Engine flexible environment.

The following prices are applied both during and after the [Google Cloud Free Trial](https://cloud.google.com/free) period. During the Free Trial period, these prices are charged against the Free Trial credit amount.

Traffic type| Price  
---|---  
Data transfer to specific Google products such as Gmail, YouTube, Google Maps, [DoubleClick](https://developers.google.com/authorized-buyers/rtb/peer-guide#trading_locations), and Google Drive, whether from a VM in Google Cloud with an external IP address or an [internal IP address.](https://cloud.google.com/compute/docs/private-google-access/private-google-access)| No charge  
Data transfer to a different Google Cloud service within the same region using an external IP address or an [internal IP address](https://cloud.google.com/compute/docs/private-google-access/private-google-access), except for Memorystore for Redis, Filestore, GKE, and Cloud SQL.| No charge  
Data transfer from Compute Engine and GKE to [Cloud CDN](https://cloud.google.com/cdn/docs) and [Media CDN](https://cloud.google.com/media-cdn/docs).| No charge (cache fill might apply for Cloud CDN).  
Data transfer to [Memorystore for Redis](https://cloud.google.com/memorystore/docs/redis), [Filestore](https://cloud.google.com/filestore/docs), [Cloud SQL](https://cloud.google.com/sql/docs), and [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine/docs) within the same region is priced the same as VM-to-VM traffic.| [VM-VM data transfer pricing within Google Cloud](https://cloud.google.com/vpc/network-pricing#egress-within-gcp)  
Data transfer to a Google Cloud service in a different region.| [VM-VM data transfer pricing within Google Cloud](https://cloud.google.com/vpc/network-pricing#egress-within-gcp)  
For Spanner network pricing, see [Spanner pricing](https://cloud.google.com/spanner/pricing#network).|   
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Internet data transfer rates

#### Premium Tier pricing

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



Item| Price (USD)  
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

#### Standard Tier pricing

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
Standard Tier Price| 200 gibibyte to 10,240 gibibyte$0.085 / 1 gibibyte, per 1 month / account10,240 gibibyte to 153,600 gibibyte$0.065 / 1 gibibyte, per 1 month / account153,600 gibibyte and above$0.045 / 1 gibibyte, per 1 month / account  
  
Free Tier

  * First 200 GiB per month free (per account, across all regions)



Free Tier is available in all regions, and usage is calculated across all of them. [Learn more](https://cloud.google.com/free/docs/free-cloud-features?_gl=1*fbjvlh*_ga*NzM0OTk0NjMxLjE3MzI2MjYyMDc.*_ga_4LYFWVHBEB*MTczMzQ3NTk4Ny40NC4xLjE3MzM0ODA5MjYuMC4wLjA.#free-tier-usage-limits)

Contact sales for pricing beyond 500 TiB (512000 GiB).

### Internal IP address pricing

There is no charge for static or ephemeral internal IP addresses.

  


### External IP address pricing

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
  
Free Tier

  * For 0 hour to 1 hour, per 1 month per account



Free Tier is available for all regions except northamerica-northeast1 and northamerica-northeast2 [regions](https://cloud.google.com/compute/docs/regions-zones/regions-zones?_gl=1*o2jslg*_ga*NzM0OTk0NjMxLjE3MzI2MjYyMDc.*_ga_4LYFWVHBEB*MTczMzQ3NTk4Ny40NC4xLjE3MzM0ODA5MTcuMC4wLjA.). Usage calculations are combined across those regions. [Learn more](https://cloud.google.com/free/docs/free-cloud-features?_gl=1*fbjvlh*_ga*NzM0OTk0NjMxLjE3MzI2MjYyMDc.*_ga_4LYFWVHBEB*MTczMzQ3NTk4Ny40NC4xLjE3MzM0ODA5MjYuMC4wLjA.#free-tier-usage-limits)

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

HourlyHourly

MonthlyMonthly

Item| Price(USD)  
---|---  
Static and ephemeral IP addresses in use on **standard VM instances**|  $0.005 / 1 hour, per 1 month / account  
Static and ephemeral IP addresses in use on **preemptible and Spot VM instances**|  $0.0025 / 1 hour  
Static and ephemeral IP addresses used by [Cloud NAT](https://cloud.google.com/nat/docs).| $0.005 / 1 hour  
Static and ephemeral IP addresses attached to forwarding rules, or used as a public IP for a [Cloud VPN ](https://cloud.google.com/vpn/docs)tunnel.| No Charge  
  
Free Tier

  * Both static and ephemeral IP addresses assigned to standard VM instances are offered with a free tier. This free usage is limited to one hour per month per account.



#### In use or not

Google Cloud considers a static external IP address as in use if it is associated with a VM instance whether the instance is running or stopped. If the instance is deleted or if the IP address is dissociated from the instance, Google Cloud considers the static IP address as not in use.

For an ephemeral IP address, Google Cloud considers the address as in use only when the associated VM instance is running. When the instance is stopped or deleted, Google Cloud releases the ephemeral IP address and no longer considers it as in use.

You can check whether a static external IP address is in use by making a gcloud compute addresses list request. This command returns a list of static external IP addresses and their statuses:

bash

  * bash



Loading...

$ gcloud compute addresses list NAME REGION ADDRESS STATUS address-1 130.211.8.68 IN_USE address-2 35.186.217.84 RESERVED

 _content_copy_

In this example, IPv4 address-1 is in use while IPv4 address-2 is reserved but not being used. Both addresses are charged according to the External IP address pricing table in this document.

**Note:** If the same IP address is assigned to more than one forwarding rule, Google Cloud counts and adds each usage of the address towards the **IN_USE_ADDRESSES** quota rather than a unique count of IP address objects that are used.

### 

**Composite Health**

There is no additional charge for using [Composite Health.](https://docs.cloud.google.com/vpc/docs/about-composite-health) However, you are charged for resources and network traffic in your VPC network. Additionally, [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) applies to logging created by Composite Health.

### 

**Firewall rules**

For Cloud Next Generation Firewall pricing, see the [Cloud NGFW pricing page](https://cloud.google.com/firewall/pricing).

### 

**Private Service Connect**

The costs associated with Private Service Connect vary depending on the configuration.

### 

**Consumer charges**

Using a Private Service Connect endpoint (forwarding rule) to access Google APIs

HourlyHourly

MonthlyMonthly

Item| Price per hour (USD)  
| Price per GiB processed, inbound and outbound data transfer  
---|---|---  
Private Service Connect endpoint (forwarding rule) used to [access Google APIs](https://cloud.google.com/vpc/docs/configure-private-service-connect-apis)| $0.01 / 1 hour| No data charge  
Private Service Connect endpoint (forwarding rule) to access the regional endpoints of Google APIs| $0.01 / 1 hour| [Consumer data processing](https://docs.cloud.google.com/vpc/network-pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://cloud.google.com/vpc/network-pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect endpoints.Consumer-to-producer traffic is billed to the project of the consumer resource originating the traffic.Producer-to-consumer traffic is billed to the project containing the Private Service Connect endpoint (forwarding rule).For endpoints with [global access](https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access), when the endpoint is accessed by resources in other regions, [inter-regional data transfer](https://cloud.google.com/vpc/network-pricing#egress-within-gcp) charges also apply to that traffic.  
  
#### Using a Private Service Connect backend (load balancer) to access Google APIs

[Private Service Connect backends](https://cloud.google.com/vpc/docs/private-service-connect-backends) use a load balancer to access Google APIs. All load balancer pricing applies. Traffic to Private Service Connect NEGs that is directed to Google APIs incurs load balancing charges for  _data processed by load balancer_. However, there is no Private Service Connect charge for data transfer traffic between the Private Service Connect NEG and Google APIs.

For pricing information for your load balancer, see pricing for [global external Application Load Balancers](https://cloud.google.com/vpc/network-pricing#lb) or [internal Application Load Balancers](https://cloud.google.com/vpc/network-pricing#internal-https-lb).

**Note:** Private Service Connect backends were previously referred to as Private Service Connect endpoints with consumer HTTP(S) service controls.

  


#### Using a Private Service Connect endpoint (forwarding rule) to access a published service

HourlyHourly

MonthlyMonthly

Item| Price per hour (USD)| Price per GiB processed, inbound and outbound data transfer  
---|---|---  
Private Service Connect endpoint (forwarding rule)| $0.01 / 1 hour| [Consumer data processing](https://docs.cloud.google.com/vpc/network-pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://cloud.google.com/vpc/network-pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect endpoints.For endpoints with [global access](https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#global-access), when the endpoint is accessed by resources in other regions, [inter-regional data transfer](https://cloud.google.com/vpc/network-pricing#egress-within-gcp) charges also apply to that traffic.  
  
**Note:** For endpoints with global access, the service producer project is not charged inter-regional data transfer even if service consumer resources are accessing the endpoint from other regions.

Private Service Connect automatically creates a Service Directory namespace to register endpoints in. A single default namespace is used for endpoints in the same region of a project unless you explicitly create additional namespaces. For more information about Service Directory pricing, see [Service Directory pricing.](https://cloud.google.com/service-directory/pricing)

  


#### Using a Private Service Connect backend (load balancer) to access a published service

[Private Service Connect backends](https://cloud.google.com/vpc/docs/private-service-connect-backends) use a load balancer to access published services. All load balancer pricing applies. Traffic between Private Service Connect NEGs and Private Service Connect published services incurs both load balancing charges for  _data processed by load balancer_ and Private Service Connect charges data transfer traffic between the NEG and the published service.

The following table summarizes the applicable charges for this configuration.

Item| Price (USD)  
---|---  
Private Service Connect endpoint (load balancer) [used to access services in another VPC network](https://cloud.google.com/vpc/docs/configure-private-service-connect-services-controls)| All [global external Application Load Balancer](https://cloud.google.com/vpc/network-pricing#lb) or [internal Application Load Balancer](https://cloud.google.com/vpc/network-pricing#internal-https-lb) pricing applies.  
Traffic between a Private Service Connect NEG and the published service| [Consumer data processing](https://docs.cloud.google.com/vpc/network-pricing#psc-consumer-data-processing)Private Service Connect does not charge for [inter-zone data transfer](https://cloud.google.com/vpc/network-pricing#inter-zone-data-transfer) for traffic to or from Private Service Connect backends.  
  
#### Using a Private Service Connect interface for access to a producer or consumer VPC network

Item| Price per hour (USD)| Price per GB processed, data transfer in and out (USD)  
---|---|---  
[Private Service Connect interface](https://cloud.google.com/vpc/docs/about-private-service-connect-interfaces) used for access to a producer or consumer VPC network| No hourly charge| For both consumer-to-producer and producer-to-consumer traffic, [consumer data processing](https://docs.cloud.google.com/vpc/network-pricing#psc-consumer-data-processing) charges apply and are charged to the consumer.For consumer-to-producer inter-region traffic, [inter-region data transfer](https://cloud.google.com/vpc/pricing#inter-region-data-transfer) charges also apply and are charged to the consumer.  
  
**Service Directory**

Private Service Connect automatically creates a Service Directory namespace to register endpoints when****[accessing Google APIs](https://cloud.google.com/vpc/docs/about-accessing-google-apis-endpoints#service-directory) or when [accessing published services](https://cloud.google.com/vpc/docs/dns-vpc-hosted-services#auto-dns-consumer). A single default Service Directory namespace is created for Private Service Connect endpoints in the same region of a project. For more information about Service Directory pricing, see [Service Directory pricing](https://cloud.google.com/service-directory/pricing).

**Consumer data processing**

Private Service Connect consumers are charged consumer data processing according to the following table. Consumer data processing is charged inbound and outbound.

Monthly usage| Price (USD)  
---|---  
Price (USD)| 0 gibibyte to 1 pebibyte$0.01 / 1 gibibyte, per 1 month / account1 pebibyte to 5 pebibyte$0.006 / 1 gibibyte, per 1 month / account5 pebibyte and above$0.004 / 1 gibibyte, per 1 month / account  
  
**Producer charges**

**Charges to publish a managed service by using a Private Service Connect service attachment**

There are no Private Service Connect hourly or data transfer charges for publishing services through service attachments. Producers are charged for any load balancing charges incurred on the load balancer that is published to consumers.

**Note:** If resources use an endpoint with global access to access a published service from a different region than the service, the service producer project is not charged inter-regional data transfer. For information about service consumer project charges, see [Using a Private Service Connect endpoint (forwarding rule) to access a published managed service](https://cloud.google.com/vpc/network-pricing#psc-forwarding-rule-service).

  


**Deploying a service by using service connection maps**

When you [deploy a service by using service connection maps](https://docs.cloud.google.com/vpc/docs/about-service-connectivity-automation), there are no producer charges for the deployment of service connection maps themselves. However, the consumer is charged for the following:

  * Resources that are deployed into the consumer project through service connectivity automation
  * [Using a Private Service Connect endpoint to access a published service](https://cloud.google.com/vpc/pricing#psc-forwarding-rule-service)



  


Private services access

When you [create a private services access connection](https://cloud.google.com/vpc/docs/configure-private-services-access#creating-connection), there are no hourly or data charges for the connection itself. However, you are charged for the following:

  * Resources that you provision in the service producer's network
  * [Data transfer traffic](https://cloud.google.com/vpc/pricing#egress) from your VMs to the service producer's network



  


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

### 

Network telemetry

Network Vended Logs generate charges. You are charged for the following products:

Before enabling VPC Flow Logs, you can use the [VPC Flow Logs cost estimator](https://ssh.cloud.google.com/cloudshell/editor?show=terminal&cloudshell_git_repo=https://github.com/GoogleCloudPlatform/network-observability-tutorials&cloudshell_git_branch=main&cloudshell_tutorial=vpc-flowlogs-cost-estimator/tutorial.md) in the Gemini CLI to estimate your monthly costs and log volume. It provides a simplified estimate for all subnets in a Google Cloud project based on the listed pricing tiers and assumes no prior usage. You can also prompt the estimator to calculate costs for specific subnets, VPC networks, or custom sampling rates.

Products| Price (USD)  
---|---  
  
  * VPC Flow Logs
  * Firewall Rules Logging
  * Cloud NAT logging

  
| 0 gibibyte to 10,240 gibibyte$0.2510,240 gibibyte to 30,720 gibibyte$0.1530,720 gibibyte to 51,200 gibibyte$0.07551,200 gibibyte and above$0.05  
  
Logs are sent to Cloud Logging. Logs can be further exported to Pub/Sub, Cloud Storage, or BigQuery. Pub/Sub, Cloud Storage, or BigQuery charges apply in addition to log generation charges. Network Telemetry logs are charged as Vended Logs in Cloud Logging Storage. For more information on exporting logs, see [Overview of logs export](https://cloud.google.com/logging/docs/export).

The Networking Telemetry charges apply to all Network Telemetry logs irrespective of the destination, including the default option of storing these logs in Cloud Logging.

If you store your logs in Cloud Logging, Network Telemetry logs are billed separately from other logs, under the Cloud Logging Vended Logs Storage. For more information, see [Cloud Logging pricing](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary).

If you send and then exclude your logs from Cloud Logging, the Network Telemetry charges apply.

### 

Packet Mirroring

You are charged for the amount of data processed by Packet Mirroring. You are not charged for Packet Mirroring forwarding rules. Currently, there is no additional per-VM charge for using Packet Mirroring.

The costs for the data processed by Packet Mirroring are described in the following table.

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
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply._﻿_

Normal data transfer rates are charged for traffic outbound from a load balancer. There is no additional load balancer data transfer cost beyond normal data transfer out rates.

## 

Cloud Load Balancing

### Load balancing and forwarding rules

The pricing tables in this section apply to the following load balancers:

  * Internal and external passthrough Network Load Balancers
  * Internal and external proxy Network Load Balancers
  * Global, classic, and regional external Application Load Balancers



For regional and cross-region internal Application Load Balancers, see the [Internal Application Load Balancer](https://cloud.google.com/vpc/network-pricing#internal-https-lb) section.

For Private Service Connect forwarding rules, see the [Private Service Connect section](https://cloud.google.com/vpc/pricing#psc-forwarding-rules).

The following table shows the pricing for global forwarding rules. There are no global data processing charges. Data processing is charged by the region, depending on where the traffic is processed.

HourlyHourly

MonthlyMonthly

Item| Price (USD)  
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

#### Ways to lower external Application Load Balancer costs

Global external Application Load Balancer users can use Google Cloud Armor, Cloud CDN, or both, to minimize the impact of [ _Outbound data processing charges_](https://cloud.google.com/vpc/network-pricing#outbound-charge).

  * **Cloud CDN:** Static objects that are served to the client from the cache do not transit through the load balancer. An effective caching strategy would reduce the amount of outbound data being processed by the load balancer and lower your costs. To implement caching, it is necessary to understand which portion of your traffic is static and cacheable. For additional information, refer the [Cloud CDN documentation](https://cloud.google.com/cdn/docs/features#caching).
  * **Google Cloud Armor:** If your application receives a significant amount of undesirable traffic, you can deploy Google Cloud Armor to block such traffic. Requests that are blocked by Google Cloud Armor do not transit through the load balancer, effectively reducing the amount of outbound data processed by the load balancer. The impact on your costs depends on the percentage of undesirable traffic blocked by the [Google Cloud Armor security policies](https://cloud.google.com/armor/docs/security-policy-overview) you've implemented.



If your application can operate in a single region or is required to operate in a single region, you can use the [Regional external Application Load Balancer](https://cloud.google.com/load-balancing/docs/https#load-balancer-mode). The regional external Application Load Balancer uses only the Standard Network Tier which has [lower outbound data transfer charges](https://cloud.google.com/vpc/network-pricing#internet_egress) making it a cost effective option.

  


#### External Application Load Balancer pricing with Serverless NEGs

If you are using [serverless NEG backends](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) with an external Application Load Balancer ([global, regional, or classic](https://cloud.google.com/load-balancing/docs/https#load-balancer-mode)), existing load balancer charges will apply in addition to the serverless compute charges for Cloud Run, Cloud Run functions, or App Engine backends as applicable. If Google Cloud Armor or Cloud CDN are used, their respective charges also apply.

However, you will not be charged for serverless outbound data transfer. Only internet outbound data transfer rates apply. Cloud Run functions [outbound data transfer](https://cloud.google.com/functions/pricing) charges, App Engine [outgoing network traffic](https://cloud.google.com/appengine/pricing#network-resources-in-the-standard-environment) charges and Cloud Run [data transfer charges](https://cloud.google.com/run/pricing) do not apply to requests passed from an external Application Load Balancer (using serverless NEGs) to a Cloud Run functions, App Engine, or Cloud Run service.

  


#### Opt-In Network Regions

When Opt-in Network Regions are enabled with a BYOIP, Cloud CDN and Global External Application Load Balancer traffic will start to utilize the opt-in regions when clients are near one of the regions. When this occurs there is an additional cost for CDN traffic using an opt-in region or when Global External Application Load Balancer traffic uses the opt-in region while accessing a backend that is not in the same opt-in region.

| **Extended Region* (for both inbound and outbound data transfer in GiB)**  
---|---  
**Jakarta (CGK)**| **$0.018**  
**Doha (DIA)**| **$0.029**  
**Dammam (DMM)**| **$0.029**  
  
#### Cross-project service referencing with Shared VPC

Review the following points to understand how projects and billing accounts are charged for networking SKUs when you use [cross-project service referencing](https://cloud.google.com/load-balancing/docs/https#cross-project).

![Load balancer's frontend and backend components in different service projects](https://www.gstatic.com/bricks/image/cloud_google_com_static_load_balancing_images_global_ext_https_lb_shared_vpc_example_cross_project_svg.svg)

Load balancer's frontend and backend in different service projects

  * Cloud Load Balancing related charges are always attributed to the project where the forwarding rule is configured (service project A in figure 1). This includes charges for forwarding rules, inbound data processed, and outbound data processed by the global external Application Load Balancer. Review [Cloud Load Balancing pricing basics](https://cloud.google.com/vpc/network-pricing#lb).
  * Network internet data transfer out for Premium Tier and Standard Tier are always attributed to the project where the forwarding rule is configured (service project A in figure 1). Review [Network data transfer pricing](https://cloud.google.com/vpc/network-pricing#all-networking-pricing).
  * If you configure Cloud CDN on a backend service that is referenced by a URL map using cross-project service referencing, then all Cloud CDN charges for cacheable content (cache data transfer out, cache lookup, cache fill) are always attributed to the project that contains the Cloud CDN-enabled backend service (service project B in figure 1), and not the project that configured the forwarding rules. Review [Cloud CDN pricing](https://cloud.google.com/cdn/pricing).
  * If you configure Google Cloud Armor on a backend service that is referenced by a URL map using cross-project service referencing, then all Google Cloud Armor related charges are attributed to the project that contains the Google Cloud Armor-enabled backend service (service project B in figure 1), and not the project that configured the forwarding rules. Review [Google Cloud Armor pricing](https://cloud.google.com/armor/pricing). Specifically, all Google Cloud Armor Standard Tier and Cloud Armor Enterprise Tier charges are attributed to service project B.



The following additional considerations also apply when you're using Google Cloud Armor with cross-project service referencing:

  * Subscription changes related to [Cloud Armor Enterprise](https://cloud.google.com/armor/pricing) are attributed to the billing account that you specified during enrollment. If you want to use the same Cloud Armor Enterprise subscription across multiple projects to include all the backend services referenced using cross-project service referencing, make sure that you include all the relevant service projects as part of the same Cloud Armor Enterprise billing account.
  * When you're using cross-project service referencing, some features offered in Cloud Armor Enterprise, such as DDoS telemetry and DDoS response, require Cloud Armor Enterprise tier enrollment for both the frontend forwarding rule project and the backend service projects.



  


#### Forwarding rules pricing examples

Google Cloud charges for [forwarding rules](https://cloud.google.com/vpc/docs/forwarding-rules) whether they are created for [load balancing](https://cloud.google.com/compute/docs/load-balancing) or other uses, such as Packet Mirroring.

The following examples use US pricing:

You can create up to 5 forwarding rules for the price of $0.025/hour. For example, if you create one forwarding rule, you are charged $0.025/hour. If you have 3 forwarding rules, you are still charged $0.025/hour. However, if you have 10 forwarding rules, you are charged as follows:

  * 5 forwarding rules = $0.025/hour
  * Each additional forwarding rule = $0.01/hour



$0.025/hour for 5 rules + (5 additional rules * $0.01/hour) = $0.075/hour

For most load balancing use cases, you need only one forwarding rule per load balancer.

Google Cloud charges for [global forwarding rules](https://cloud.google.com/compute/docs/reference/rest/v1/globalForwardingRules) and [regional forwarding rules](https://cloud.google.com/compute/docs/reference/rest/v1/forwardingRules) separately, and also per project. For example, if you use one global forwarding and one regional forwarding rule in two separate projects (four rules total), you are charged $0.10/hour (4 x $0.025/hour).

  


#### Estimating load balancing charges

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



This example doesn't include the [internet data transfer out cost](https://cloud.google.com/vpc/network-pricing#internet_egress) of sending replies from the backends.

  


### Internal Application Load Balancer

The following charges apply to both regional internal Application Load Balancers and cross-region internal Application Load Balancers. Some additional [cross-region data transfer charges also apply to the cross-region internal Application Load Balancer](https://cloud.google.com/vpc/network-pricing#cross-region-egress).

  


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
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

*Internal Application Load Balancers use a fleet of managed proxy instances that are dynamically allocated to your network to handle traffic volume. The  _per proxy instance_ charge is determined based on the number of proxy instances required to handle your traffic over a specific time period.

#### Proxy instance charge

Envoy-based load balancers automatically scale the number of proxies available to handle your traffic based on your traffic needs. The proxy instance charge is based on the number of proxy instances needed to satisfy your traffic needs. Each additional proxy incurs an additional hourly charge according to the prices indicated in the [pricing table](https://cloud.google.com/vpc/network-pricing#internal-https-lb).

The number of proxies allocated to your load balancer is calculated based on the measured capacity needed to handle your traffic over a 10-minute time period. During this time period, we look at the greater of:

  * **The number of proxies needed to serve your traffic's bandwidth needs**. Each proxy instance can handle up to 18 MB per second. We monitor the total bandwidth required and divide that total by the bandwidth that a proxy instance can support.
  * **The number of proxies needed to handle connections and requests**. We count the total of each of the following resources and divide each value by what a proxy instance can handle:
  * 600 (HTTP) or 150 (HTTPS) new connections per second
  * 3,000 active connections
  * 1,400 requests per second*



* A proxy instance can handle 1,400 requests per sec if Cloud Logging is disabled. If you enable Logging, your proxy instance can handle fewer requests per second. For example: logging 100% of requests decreases the proxy's request handling capacity to 700 requests per second. You can set Logging to sample a smaller percentage of traffic. This enables you to meet your observability needs while controlling your cost.

#####   


##### Example calculation

In a 10-minute period, 180 MB per second of data pass through the load balancer. 180 MB per second / 18 MB per second per proxy instance = 10 proxy instances

During this same period, 300 new HTTPS connections are established per second, 3,000 connections are active and 2,800 requests are sent per second:

300 new HTTPS connections per second / 150 new HTTPS connections per second per proxy instance = 2 proxy instances 3,000 active connections / 3,000 active connections per proxy instance = 1 proxy instance 2,800 requests per second / 1,400 requests per second per proxy instance = 2 proxy instances.

This sums up to 5 proxy instances. This amount is lower than the 10 proxy instances required to serve bandwidth. Thus, the proxy instance charge for this 10-minute time period would be calculated as follows:

10 proxy instances * $0.025 per proxy instance per hour * (10 minutes / (60 minutes per hour)) = $0.0417Billing is calculated based on the measured capacity needed to satisfy your traffic needs, not the number of proxy instances that are establishing connections to your backends. As such, you might be billed for a different number of proxy instances than you see in your infrastructure.

  


##### Minimum proxy instance charge

To ensure optimal performance and reliability, each load balancer is allocated at least three proxy instances in the Google Cloud region where the load balancer is deployed. These proxy instances are allocated even if the load balancer handles no traffic. After a forwarding rule (with load balancing scheme INTERNAL_MANAGED) is deployed to your project, you start to accrue proxy instance charges. Additional forwarding rules incur additional proxy instance charges as described previously (in other words, three additional proxy instances per forwarding rule).

The three proxy instances that are allocated to your load balancer result in a minimum hourly proxy instance charge. For example, for the us-central1 Google Cloud region, the minimum charge is calculated as follows:

3 proxy instances * $0.025 per proxy per hour = $0.075 per hour

As described previously, these proxy instances can each handle a certain amount of traffic. Once your traffic needs surpass the capacity of these three proxy instances, you will incur costs for the proxy instances required to handle any additional traffic.

  


#### Data processing charge

The data processing charge is calculated by measuring the total volume of data for requests and responses processed by your load balancer during the billing cycle. This charge scales according to your usage and there is no minimum charge for data processing.

  


#### Cross-region data transfer charges

[Cross-region data transfer charges](https://cloud.google.com/vpc/network-pricing#vpc-pricing) apply if you're using a cross-region internal Application Load Balancer. For example, if you have a cross-region internal Application Load Balancer deployment where the client, the Envoy proxy, and the backend are in separate regions, you'll see cross-region data transfer charges for each hop separately (client <-> Envoy proxy, and Envoy proxy <-> backend). To reduce these cross-region data transfer charges, you can deploy Envoy proxies in multiple regions.

  


#### Cross-project service referencing with Shared VPC

For data processing, hourly proxy instance usage, and inter-zone VM data transfer, the forwarding rule project is charged.

  


#### Internal Application Load Balancer pricing with serverless NEGs

If you are using [serverless NEG backends](https://cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) for an internal Application Load Balancer, existing internal Application Load Balancer charges will apply in addition to the serverless compute charges for Cloud Run.

  


### Regional internet NEG charges

Regional internet NEGs require the use of a Cloud NAT gateway which incurs additional charges. You'll be charged for both internet data transfer out and Cloud NAT usage for any traffic sent to and from the Envoy proxy-only subnet, and for health check traffic. However, the load balancer's charges apply only to user request traffic.

Cloud NAT gateways allocated for Cloud Load Balancing incur hourly charges equivalent to a network with  _more than 32 VM instances_. For details, see [Cloud NAT pricing](https://cloud.google.com/vpc/network-pricing#nat-pricing)

  


### Authorization policy charges

| External Application Load Balancer| Internal Application Load Balancer  
---|---|---  
Data processing fee| $0.75 per million Requests| $0.60 per million Requests  
Authz Rules fee| $1 per rule per month| $1 per rule per month  
Authz policies fee| $5 per policy per month| $5 per policy per month  
  
The following additional considerations for Authz pricing apply when you're also using Google Cloud Armor:

Data Processing Fee will be included for free as part of Cloud Armor Enterprise for any backend that is counted as a Cloud Armor protected resource.

Data Processing Fee will be included for free as part of Cloud Armor Standard for any Cloud Armor requests.

Policy and Rule Fees will not be included for free as part of Cloud Armor, and will be charged whether or not you are using Cloud Armor policies.

### Custom request headers and Google Cloud Armor charges

If a backend service has a Google Cloud Armor policy associated with it, you can use the custom request headers feature with that backend service without any additional charge for the custom request headers feature.

If a backend service that uses the custom request headers feature does not have a Google Cloud Armor policy associated with it, the charges are $0.75 per 1,000,000 HTTP(S) requests per month per account. You are only charged for the first 666,666,667 requests per month per account. The charge for custom headers applies whether they are configured on a backend service or a URL map.

  


### Global access for internal load balancers

Global access allows client instances from any region to access your internal load balancer. If a forwarding rule has global access enabled, additional cross-region data transfer charges are incurred when traffic is sent to or from a client in a different region than the load balancer.

Global access is generally available for internal passthrough Network Load Balancers, regional internal Application Load Balancers, and regional internal proxy Network Load Balancers.

  


### Protocol forwarding

Protocol forwarding is charged at the same rate as load balancing. There is a charge for the forwarding rule and a charge for the inbound data processed by the target instance.

### 

SSL certificates

If you use Compute Engine self-managed TLS certificates, then the following pricing applies for self-managed TLS certificates deployed across all your load balancers.

Price| Description  
---|---  
$0.45 / 1,000,000 count| The number of load balancer connections established using self-managed certificates with the following key types:

  * RSA-3072
  * RSA-4096

  
  
There are no per-connection charges for Google-managed or self-managed certificates that use RSA-2048, ECDSA P-256, or ECDSA P-384 key types.

## 

Google Cloud Armor

This document explains Google Cloud Armor and Google Cloud Armor Enterprise pricing details. This pricing is active.

| Google Cloud ArmorStandard| Cloud Armor EnterprisePaygo| Cloud Armor EnterpriseAnnual  
---|---|---|---  
Billing model| Pay as you go| Pay as you go| Subscription  
Subscription price| N/A| Prorated $200/month

  * Includes up to 2 protected resources.
  * Billed to the project.

  
| $3,000/month

  * Includes up to 100 protected resources across all projects.
  * Billed to the billing account with the active subscription.

  
Protected resources| N/A| Prorated $200/protected resource per month after initial 2, aggregated within your project.| $30/protected resource per month after initial 100, aggregated among all projects in the subscribed billing account.  
Requests (globally scoped security policies)| $0.75 per million requests| All included| All included  
Requests (regionally scoped security policies)| $0.60 per million requests| All included| All included  
Security policies| $5 per policy per month| All included| All included  
Rules| $1 per rule per month| All included| All included  
Data processing fee| None| Yes; see the following section| Yes; see the following section  
Time commitment| None| None| One year  
Google Cloud Armor bot management| Billed in accordance with the reCAPTCHA [pricing model](https://cloud.google.com/recaptcha-enterprise/pricing)| Billed in accordance with the reCAPTCHA [pricing model](https://cloud.google.com/recaptcha-enterprise/pricing)| Billed in accordance with the reCAPTCHA [pricing model](https://cloud.google.com/recaptcha-enterprise/pricing)  
  
Protected resources include the following backend types in each enrolled project; the backends are counted as protected resources for all covered endpoint and load balancer types in the enrolled project.

Endpoint type| Protected resource (backend ty  
---|---  
External Application Load Balancer| \- Backend service\- Backend bucket  
External proxy Network Load Balancer| Backend service  
External passthrough Network Load Balancer| \- Backend service (regional)\- Target pool  
Protocol forwarding| Target instance  
Public IP address (VM)| Instance  
  
**Note:** When you enable advanced network DDoS protection for a particular region, all public virtual machine instances in the region are counted against your Cloud Armor Enterprise protected resources total.

### Data processing fee

The Cloud Armor Enterprise data processing fee meters the data transferred to the internet from all protected resources for every project that is enrolled in Cloud Armor Enterprise. When you use Cloud Armor Enterprise Annual, the data processing fee is billed at the project level, but usage is aggregated across all protected resources in all projects enrolled in Cloud Armor Enterprise Annual. When you use Cloud Armor Enterprise Paygo, the data processing fee is billed and usage is aggregated at the project level. The Cloud Armor Enterprise data processing fee is separate from the Cloud Load Balancing data processing fee.

Prices are per GiB transferred to the internet directly or through Carrier Peering, and are in addition to other data transfer fees. For example, for workloads behind a supported Google Cloud load balancer, the data processing fee meters the bits data transferred to the internet through the enrolled load balancer endpoints but does not meter the associated inter-region or inter-zone traffic by the underlying workload. The charge is $0.05 per GiB data transferred for the first 100 TiB and $0.04 per GiB for the next 400 TiB. If the content being served is using Cloud CDN and is considered cacheable, then the data processing fee for Cloud CDN is applied for that content. The following table contains complete pricing.

| GiB transferred| Price (USD)  
---|---|---  
Cloud Armor Enterprise Paygo  
| Cloud Load Balancing/Instance| 0 gibibyte to 102,400 gibibyte$0.075 / 1 gibibyte, per 1 month / project102,400 gibibyte to 512,000 gibibyte$0.06 / 1 gibibyte, per 1 month / project512,000 gibibyte and above$0.05 / 1 gibibyte, per 1 month / project  
Cloud CDN & Media CDN| 0 gibibyte to 102,400 gibibyte$0.0375 / 1 gibibyte, per 1 month / project102,400 gibibyte to 512,000 gibibyte$0.03 / 1 gibibyte, per 1 month / project512,000 gibibyte to 1,024,000 gibibyte$0.025 / 1 gibibyte, per 1 month / project1,024,000 gibibyte and above$0.02 / 1 gibibyte, per 1 month / project  
Cloud DNS| Included  
Cloud Armor Enterprise Annual| Cloud Load Balancing/Instance| 0 gibibyte to 102,400 gibibyte$0.05 / 1 gibibyte, per 1 month / account102,400 gibibyte to 512,000 gibibyte$0.04 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.03 / 1 gibibyte, per 1 month / account  
Cloud CDN & Media CDN| 0 gibibyte to 102,400 gibibyte$0.025 / 1 gibibyte, per 1 month / account102,400 gibibyte to 512,000 gibibyte$0.02 / 1 gibibyte, per 1 month / account512,000 gibibyte to 1,024,000 gibibyte$0.015 / 1 gibibyte, per 1 month / account1,024,000 gibibyte and above$0.01 / 1 gibibyte, per 1 month / account  
Cloud DNS| Included  
  
**Note:** Rules utilizing reCAPTCHA in the match condition or in the action are not treated any differently by Google Cloud Armor; usage billed still depends on your whether you are enrolled with the Standard or Cloud Armor Enterprise pricing model. However, reCAPTCHA usage is subject to reCAPTCHA billing.

If a backend service has a Google Cloud Armor security policy associated with it, you can use the [custom headers feature](https://cloud.google.com/load-balancing/docs/custom-headers) with that backend service without any additional charge for the custom headers feature.

If you pay in a currency other than USD, the prices listed in your currency on [Google Cloud Platform SKUs](https://cloud.google.com/skus) apply.

## 

Cloud Intrusion Detection System

This [document](https://cloud.google.com/intrusion-detection-system/pricing) explains Cloud IDS pricing details. This pricing is active. Prices on this page are listed in US dollars (USD).

HourlyHourly

MonthlyMonthly

Type of usage| Price (USD)  
---|---  
Per hour per endpoint| $1.50 / 1 hour  
Per GiB processed| $0.07 / 1 gigabyte  
  
## 

Cloud CDN

If you plan to serve a large volume of content from Cloud CDN (more than 500 TiB per month), you can [contact us](https://cloud.google.com/contact) to discuss volume-based discounts.

This document discusses pricing for Cloud CDN.

Prices on this page are listed in US dollars (USD). If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### Pricing structure

Case| What you pay for| Notes  
---|---|---  
Cacheable content, cache hit| cache lookup + cache data transfer out| \- When Cloud CDN serves your content, you're charged for bandwidth and HTTP/HTTPS requests.\- The GET and HEAD HTTP methods cause cache lookups. Other methods such as POST and PUT do not.\- This also applies to Cloud CDN cache hits for cacheable content from custom origins.  
Cacheable content, cache miss| cache lookup + cache data transfer out + cache fill + applicable Cloud Load Balancing data processing or Cloud Storage operation charges| \- Cache fill and cache data transfer out charges apply to cacheable content.\- On cache misses, any applicable [Cloud Load Balancing data processing](https://cloud.google.com/vpc/network-pricing#lb) or [Cloud Storage operation](https://cloud.google.com/storage/pricing#operations-pricing) charges apply.\- These charges replace the data transfer charges that apply when serving directly from Compute Engine or Cloud Storage.\- For Cloud CDN cache fills from external backends, requests to the external backend are charged at internet data transfer out rates. Cache fills continue to benefit from Google's global backbone network between Google's Cloud CDN edge and origin.  
Non-cacheable content| cache lookup + applicable Cloud Load Balancing data processing + standard Compute Engine or Cloud Storage data transfer rates| \- For non-cacheable content, standard [Compute Engine](https://cloud.google.com/vpc/network-pricing#internet_egress) and [Cloud Storage](https://cloud.google.com/storage/pricing#network-pricing) internet data transfer out rates apply for response bytes.\- For external backends, you're also charged for request bytes sent to external backends from the load balancer at the standard [Compute Engine](https://cloud.google.com/vpc/network-pricing#internet_egress) internet data transfer out rates.  
  
### 

Overview

Cache data transfer out and cache fill are calculated in [gibibytes (GiB)](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units).

Item| Price (USD)  
---|---  
Cache data transfer out| $0.02-$0.20 per GiB  
Cache fill| $0.01-$0.04 per GiB  
HTTP/HTTPS cache lookup requests| $0.0075 / 10,000 count  
Requests sent from Cloud CDN to external backends| [Compute Engine](https://cloud.google.com/vpc/network-pricing#internet_egress) internet data transfer out rates  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Cache data transfer out

### Pricing calculator

You can use the Google Cloud Pricing Calculator to estimate the cost of using Cloud CDN.

### [Go to the pricing calculator](https://cloud.google.com/products/calculator?hl=en&dl=CjhDaVF5WWpoaU56QTVNUzFqTURFekxUUTFOVEF0T1RNd05TMDROVGs0WmpVeU9ERmhORE1RQVE9PRAdGiQ0Mzg3M0Y5RC1ERkRCLTQxRUItQjkzOC0xMjVEQkQxMzY5NDk)

###   


### Cache data transfer out

Cache data transfer out charges represent cached responses served from Cloud CDN's caches, and vary based on the destination and your monthly usage. Monthly usage is calculated per project per destination. Destination is a geographic area that's determined by where traffic leaves the Google network.

Monthly usage| Price (USD)  
---|---  
Asia Pacific(including Hong Kong)  
| 0 byte to 10 tebibyte$0.09 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.06 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.05 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.04 / 1 gibibyte, per 1 month / account  
China[1](https://cloud.google.com/vpc/network-pricing#footnote-1)| 0 byte to 10 tebibyte$0.20 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.17 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.16 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.145 / 1 gibibyte, per 1 month / account  
Europe| 0 byte to 10 tebibyte$0.08 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.055 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.03 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.02 / 1 gibibyte, per 1 month / account  
North America(including Hawaii)  
| 0 byte to 10 tebibyte$0.08 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.055 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.03 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.02 / 1 gibibyte, per 1 month / account  
Oceania[2](https://cloud.google.com/vpc/network-pricing#footnote-2)| 0 byte to 10 tebibyte$0.11 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.09 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.08 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.065 / 1 gibibyte, per 1 month / account  
South America| 0 byte to 10 tebibyte$0.09 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.06 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.05 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.04 / 1 gibibyte, per 1 month / account  
All other destinations(including Mexico, Central America, and Middle East)  
| 0 byte to 10 tebibyte$0.09 / 1 gibibyte, per 1 month / account10 tebibyte to 150 tebibyte$0.06 / 1 gibibyte, per 1 month / account150 tebibyte to 1,000 tebibyte$0.05 / 1 gibibyte, per 1 month / account1,000 tebibyte and above$0.04 / 1 gibibyte, per 1 month / account  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply. **1** Traffic destined for mainland China is served from Google locations outside of mainland China. Performance and reliability may be lower than for traffic served from in-country locations.

**2** Oceania includes Australia, New Zealand, and surrounding Pacific Ocean islands such as Papua New Guinea and Fiji. This region excludes Hawaii.

  


### 

Cache fill

Monthly cache fill charges represent the data required to populate Cloud CDN's caches. For typical workloads where you are serving popular content, cache fill is often less than 10% of your total data transfer GiB. Charges vary based on the source and destination, where the source is the region of your backend service, or for external backends, the geographic area based on your origin's IP address.

Cache fill| Price (per GiB)  
---|---  
Within North America or Europe(including Hawaii)| $0.01 / 1 gibibyte  
Within each of Asia Pacific, South America, Middle East, Africa, and Oceania(including Hong Kong)| $0.02 / 1 gibibyte  
Inter-region cache fill(for example: between Asia Pacific and North America)  
| $0.04 / 1 gibibyte  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### Pricing notes

  * Network usage is calculated in [gibibytes (GiB)](https://en.wikipedia.org/wiki/Byte#Multiple-byte_units).
  * Charges accrue daily, but Cloud CDN bills you only at the end of the billing period. You can view unbilled usage on your project's billing page in the Google Cloud console.
  * The metered bytes for cache data transfer out or cache fill include HTTP response headers (after compression, if applicable) and the response body, as well as any trailers.



  


### Pricing example

The following example shows a simple scenario that might apply if you are just getting started with Cloud CDN.

Suppose you have the following Cloud CDN usage pattern in a given month.

Pricing category| Type of usage| Amount  
---|---|---  
Cache data transfer out| Cache data transfer out in North America| 500 GiB  
Cache fill| Data transfer to Cloud CDN caches| 25 GiB  
Cache lookup requests| **GET** and **HEAD** HTTP methods| 5,000,000 operations  
  
Your bill for the month is calculated as follows.

Pricing category| Calculation| Cost  
---|---|---  
Cache data transfer out| 500 GiB cache data transfer out * $0.08 per GiB| $40.00  
Cache fill| 25 GiB fill * $0.01 per GiB| $0.25  
Cache lookup requests| 5,000,000 operations (500 GiB of 100 KiB responses, on average)$0.0075 per 10,000 operations$0.0075 * 500| $3.75  
Total| | ~44.00  
  
## 

Global Front End Enterprise

This document explains Global Front End pricing details. Global Front End Enterprise offers a unified pricing for Cloud Load Balancing, Cloud CDN, Cloud Armor and Service extension required to scale and secure your internet facing applications.

### 

Overview

Global Front End pricing is based on the following components:

  * Data Processing volume
  * Request count
  * Instance charges based on number of forwarding rules



### 

Pricing details

Global Front End Enterprise enables scalable and secure delivery of your web assets by providing a unified offering consisting of Global External Application Load Balancer, Cloud CDN, Cloud Armor and Service extension. The unified pricing for Global Front End Enterprise simplifies the pricing by reducing the count of SKUs (as compared to individual product pricing) as well as metering.

**Data processing charge - cacheable:**

Resource usage| Price (USD)  
---|---  
North America (including Hawaii)| 0 gibibyte to 10,240 gibibyte$0.0966726 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.0809226 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.0765351 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0563976 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0410976 / 1 gibibyte, per 1 month / account  
Europe| 0 gibibyte to 10,240 gibibyte$0.0972 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.0815 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.0771 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.057 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0417 / 1 gibibyte, per 1 month / account  
Asia Pacific (including Hong Kong)| 0 gibibyte to 10,240 gibibyte$0.1033 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.0844 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.0801 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0694 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0541 / 1 gibibyte, per 1 month / account  
Oceania| 0 gibibyte to 10,240 gibibyte$0.1158 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.1032 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.0988 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0881 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0697 / 1 gibibyte, per 1 month / account  
South America| 0 gibibyte to 10,240 gibibyte$0.1037 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.0848 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.0804 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0697 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0544 / 1 gibibyte, per 1 month / account  
China| 0 gibibyte to 10,240 gibibyte$0.172 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.1531 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.1487 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.1381 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.1196 / 1 gibibyte, per 1 month / account  
All other destinations (including Mexico, Central America, and Middle East)| 0 gibibyte to 10,240 gibibyte$0.1033 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.0844 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.08 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0693 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.054 / 1 gibibyte, per 1 month / account  
Opt In - Jakarta| 0 gibibyte to 10,240 gibibyte$0.1243 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.1086 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.1042 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0904 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0814 / 1 gibibyte, per 1 month / account  
Opt In - Doha| 0 gibibyte to 10,240 gibibyte$0.121 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.1084 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.104 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0807 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0717 / 1 gibibyte, per 1 month / account  
Opt In - Dammam| 0 gibibyte to 10,240 gibibyte$0.121 / 1 gibibyte, per 1 month / account10,240 gibibyte to 51,200 gibibyte$0.1084 / 1 gibibyte, per 1 month / account51,200 gibibyte to 153,600 gibibyte$0.104 / 1 gibibyte, per 1 month / account153,600 gibibyte to 512,000 gibibyte$0.0807 / 1 gibibyte, per 1 month / account512,000 gibibyte and above$0.0717 / 1 gibibyte, per 1 month / account  
  
HourlyHourly

MonthlyMonthly

Resource usage| Price (USD)  
---|---  
Request count| $0.0075 / 10,000 count  
Instance charge| $0.20 / 1 hour  
  
### 

Pricing example

Assume the below consumption of a setup

Geography| Consumption| Unit  
---|---|---  
Asia Pacific (including Hong Kong)| 100| TiB  
Cacheable traffic| 70%|   
Requests per Month| 500| Million  
Number of forwarding rules| 4| #  
  
Data processing will be charged:

Cacheable: 70% * 100 TiB = 70 TiB. Charged as per tiered pricing:

10240*0.1033 + 40960*0.0844 + 20480*0.0801 = 6,155

UnCacheable: 30% * 100 TiB = 30 TiB. Charged as per tiered pricing:

10240*0.1033 + 20480*0.0844 = 2,786

Requests: 500 Million → 50000 * 10K → 50000* 0.0075 = 375

Instance charges: 4 * 0.2 * 720 = 576

**Total Charges: 9,892**

## 

Cloud Interconnect

This document explains Cloud Interconnect pricing details.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Dedicated Interconnect

Google charges you on an hourly basis for both Cloud Interconnect connections and VLAN attachments. The hourly charge for each resource, either Cloud Interconnect connection or VLAN attachment, is charged to the project that owns the resource.

Data transfer from your Virtual Private Cloud (VPC) networks through your Cloud Interconnect connections is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Data transfer out pricing depends on the number of gibibytes (GiB) transferred and the location of your Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for the data transfer. Specifically, costs for data transfer from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your Dedicated Interconnect connections, VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an IP address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer, you are charged only for Cloud Interconnect data transfer out. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

  


#### Pricing tables

##### Dedicated Interconnect pricing

HourlyHourly

MonthlyMonthly

Resource| Price  
---|---  
Cloud Interconnect connection-10Gbps Dedicated circuit| $2.328 / 1 hour  
Cloud Interconnect connection-100Gbps Dedicated circuit| $23.28 / 1 hour  
A 50-, 100-, 200-, 300-, 400-, or 500-Mbps VLAN attachment| $0.10 / 1 hour  
1-, 2-, 5-, or 10-Gbps VLAN attachment| $0.10 / 1 hour  
20-Gbps VLAN attachment| $0.20 / 1 hour  
50-Gbps VLAN attachment| $0.50 / 1 hour  
100-Gbps VLAN attachment| $1.00 / 1 hour  
  
#####   


##### Application awareness on Dedicated Interconnect pricing

HourlyHourly

MonthlyMonthly

Cloud Interconnect connection| Application awareness price  
---|---  
10-Gbps (per 10-Gbps connection)| $0.3492 / 1 hour  
100-Gbps (per 100-Gbps connection)| $3.492 / 1 hour  
  
##### Data transfer from a VPC network through a Cloud Interconnect connection

  


### North America

The following table shows the prices for the North America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
### Europe, Middle East, and Africa (EMEAR). 

The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
### Asia

The following table shows the prices for the Asia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
* Includes all of Asia except China, India, Indonesia, and the Philippines.

### Australia

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
### South America

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
##### Inbound data transfer through a Cloud Interconnect connection

Traffic type| Price  
---|---  
Data transfer in| Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
#### Pricing example

The following table shows an example usage pattern of Dedicated Interconnect connections for a single month.

Resources| Usage| Estimated cost  
---|---|---  
Cloud Interconnect connection| capacity 30 Gbps (3 x 10-Gbps circuit)| 3 x 10-Gbps circuit x 24 hrs @ $2.328 per hour x 30 days = $5,028.48  
Redundant Cloud Interconnect connection| capacity 30 Gbps (3 x 10-Gbps circuit)| 3 x 10-Gbps circuit x 24 hrs @ $2.328 per hour x 30 days = $5,028.48  
VLAN attachment| 6 (one per Cloud Interconnect connection circuit)| 6 x 10-Gbps attachment x 24 hrs @ $0.10 per hour x 30 days = $432.00  
Data transfer[(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#how-it-works-dedicated)| 20 TiB| 20,480 GiB x $0.02 = $409.60  
**Total cost**| | **﻿ $10,898.56**  
  
### 

Partner Interconnect

Google charges you on an hourly basis for VLAN attachments, depending on their capacity. The hourly charges are billed to the project that owns the VLAN attachment. Your service provider might also charge you for services such as using their network, which isn't included in your Google Cloud bills. For information about their pricing, contact your service provider.

Data transfer from your VPC networks though your attachments is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Outbound data transfer pricing depends on the number of gibibytes (GiB) transferred and the location of your Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for data transfer. Specifically, costs for data transfer traffic from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer, you are charged only for Cloud Interconnect outbound data transfer. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

#### Pricing tables

##### Partner Interconnect pricing

HourlyHourly

MonthlyMonthly

Partner VLAN attachment capacity| Price  
---|---  
50 Mbps| $0.05417 / 1 hour  
100 Mbps| $0.0625 / 1 hour  
200 Mbps| $0.08333 / 1 hour  
300 Mbps| $0.1111 / 1 hour  
400 Mbps| $0.1389 / 1 hour  
500 Mbps| $0.1736 / 1 hour  
1 Gbps| $0.2778 / 1 hour  
2 Gbps| $0.5694 / 1 hour  
5 Gbps| $1.25 / 1 hour  
10 Gbps| $2.36 / 1 hour  
20 Gbps| $3.61 / 1 hour  
50 Gbps| $9.02 / 1 hour  
  
##### Data transfer from a VPC network through a Cloud Interconnect connection

### North America

The following table shows the prices for the North America geographic area.

  


Connection location| Region of VLAN attachment| Price  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
### Europe, Middle East, and Africa (EMEAR)

The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
### Asia

The following table shows the prices for the Asia geographic area.

**Connection location**| **Region of VLAN attachment**| **Price**  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
* Includes all of Asia except China, India, Indonesia, and the Philippines.

### Australia

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
### South America

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
##### Inbound data transfer through a Cloud Interconnect connection

  


Traffic type| Price  
---|---  
Data transfer in| Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
#### Pricing example

The following table shows an example usage pattern of Partner Interconnect connections for a single month.

  


Resources| Usage| Estimated cost  
---|---|---  
VLAN attachment| 6 100-Mbps attachments| 6 x $0.0625 x 720 hours = $270.0  
Data transfer out[(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#how-it-works-partner)| 20 TiB| 20,480 GiB x $0.02 = $409.60  
**Total cost**| | **$679.60**  
  
### 

Cross-Cloud Interconnect

Google charges you on an hourly basis for both Cross-Cloud Interconnect connections and VLAN attachments. The hourly charge for each resource, either Cross-Cloud Interconnect connection or VLAN attachment, is charged to the project that owns the resource.

Data transfer from your Virtual Private Cloud (VPC) networks through your Cross-Cloud Interconnect connections is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Data transfer pricing depends on the number of gibibytes (GiB) transferred and the location of your Cross-Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cross-Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for data transfer. Specifically, costs for data transfer from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your Cross-Cloud Interconnect connections, VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an IP address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer out, you are charged only for Cloud Interconnect data transfer. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

  


  


#### Pricing tables

##### Cross-Cloud Interconnect pricing

HourlyHourly

MonthlyMonthly

Resource| Price  
---|---  
Cross-Cloud Interconnect connection (per 10-Gbps circuit)| $5.60 / 1 hour  
Cross-Cloud Interconnect connection ( per 100-Gbps circuit)| $30.00 / 1 hour  
50-, 100-, 200-, 300-, 400-, or 500-Mbps VLAN attachment (per VLAN attachment)| $0.10 / 1 hour  
1-, 2-, 5-, or 10-Gbps VLAN attachment (per VLAN attachment)| $0.10 / 1 hour  
20-Gbps VLAN attachment (per VLAN attachment)| $0.20 / 1 hour  
50-Gbps VLAN attachment (per VLAN attachment)| $0.50 / 1 hour  
100-Gbps VLAN attachment (per VLAN attachment)| $1.00 / 1 hour  
  
##### Application awareness on Cross-Cloud Interconnect pricing

HourlyHourly

MonthlyMonthly

Cloud Interconnect connection| Application awareness price  
---|---  
10-Gbps (per 10-Gbps connection)| $0.3492 / 1 hour  
100-Gbps (per 100-Gbps connection)| $3.492 / 1 hour  
  
##### Data transfer from a VPC network through a Cloud Interconnect connection

### North America

The following table shows the prices for the North America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
### Europe, Middle East, and Africa (EMEAR)

The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
### Asia

The following table shows the prices for the Asia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
* Includes all of Asia except China, India, Indonesia, and the Philippines.

### Australia

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
### South America

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
##### Inbound data transfer through a Cloud Interconnect connection

  


Traffic type| Price  
---|---  
Data transfer in|   
Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
  
#### Pricing example

The following table shows an example usage pattern of Cross-Cloud Interconnect connections for a single month.

  


Resources| Usage| Estimated cost  
---|---|---  
Cross-Cloud Interconnect connection| capacity 10 Gbps (1 x 10-Gbps circuit)| 1 x 10-Gbps circuit x 24 hrs @ $5.60 per hour x 30 days = $4,032  
Redundant Cross-Cloud Interconnect connection| capacity 10 Gbps (1 x 10-Gbps circuit)| 1 x 10-Gbps circuit x 24 hrs @ $5.60 per hour x 30 days = $4,032  
VLAN attachment| 2 (one per Cloud Interconnect connection circuit)| 2 x 10-Gbps attachment x 24 hrs @ $0.10 per hour x 30 days = $144.00  
Data transfer[(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#how-it-works-dedicated)| 200 TiB| 204,800 GiB x $0.02 = $4,096.00  
**Total cost**|  -| **$12,304**  
  
### 

Pricing scenarios

This section describes different pricing scenarios for how Google Cloud calculates pricing for Cloud Interconnect outbound data transfer; that is, when a virtual machine (VM) instance or a non-VM Google Cloud product or service sends traffic to your on-premises location over a VLAN attachment located in the same or different geographical location:

  * [A VM in the same region as a VLAN attachment, using either regional or global VPC dynamic routing](https://cloud.google.com/vpc/network-pricing#regional-routing)
  * [A VM in the same continent but different region than a VLAN attachment, using global VPC dynamic routing](https://cloud.google.com/vpc/network-pricing#global-routing-same-cont)
  * [A VM in a different continent than a VLAN attachment, using global VPC dynamic routing](https://cloud.google.com/vpc/network-pricing#global-routing-intercontinental)
  * [A VM in a different continent than a VLAN attachment, using VPC Network Peering](https://cloud.google.com/vpc/network-pricing#vpc-peering-intercontinental)
  * [A non-VM Google Cloud product or service in a different location than a VLAN attachment, using global VPC dynamic routing](https://cloud.google.com/vpc/network-pricing#global-routing-product)



**Note:** You have to pay standard inter-region charges for traffic between the region of the VM and the region of the VLAN attachment, which is more if they are in different continents. This applies to non-VM traffic as well.

For more information about costs for each scenario, including data transfer charges between regions within a continent and between continents, see [General network pricing](https://cloud.google.com/vpc/network-pricing).

#### A VM in the same region as a VLAN attachment, using either regional or global VPC dynamic routing

**Note:** The dynamic routing mode that you use does not impact the pricing.

In this scenario, there are two regions within North America, us-west1 and us-east1. These regions use VPC [regional dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#regional-dyn-routing) provided by Cloud Router. In this scenario, it doesn't matter which dynamic routing mode you use.

![VM in same continent, regional routing](https://www.gstatic.com/bricks/image/cloud_google_com_static_network_connectivity_docs_interconnect_images_vm_same_continent_regional_routing_svg.svg)

VM in same continent, regional routing. Cloud Interconnect data transfer charges for North America. No region-to-region data transfer charges.

  


You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create two VLAN attachments over that connection. One VLAN attachment goes to region us-east1, and the other VLAN attachment goes to region us-west1.

If you send traffic from a VM in us-east1 or from a VM in us-west1 to your on-premises location over your Cloud Interconnect connection in SJC, you are charged the following rates:

  * Cloud Interconnect data transfer out charges for North America (because that is where the Cloud Interconnect connection is located).
  * You are  _not_ charged region-to-region data transfer charges because the VMs are using a VLAN attachment in the same region.



**Note:** Unless you enable [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router, your regions without a VLAN attachment have no access to your Cloud Interconnect connection. This also means that you can't accidentally incur intercontinental data transfer charges if you have regions located on different continents.

####   


#### A VM in the same continent but different region than a VLAN attachment, using global VPC dynamic routing

In this scenario, you have VMs in two regions located in North America, us-west1 and us-east1. You have enabled [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router. Global dynamic routing enables VLAN attachments in one region to be used by one or more VMs located in another region.

![VM in same continent, global dynamic routing](https://www.gstatic.com/bricks/image/cloud_google_com_static_network_connectivity_docs_interconnect_images_vm_same_continent_dyn_routing_svg.svg)

VM in same continent, global dynamic routing. Region-to-region data transfer charges from us-east1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create one VLAN attachment over that connection to us-west1. You then send traffic from a VM in us-east1 to your on-premises location through the VLAN attachment located in us-west1. You are then charged the following rates:

  * Region-to-region data transfer charges for forwarding traffic from us-east1 to the VLAN attachment in us-west1. The VLAN attachment in us-west1 is considered the source of traffic.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location.



####   


#### A VM in a different continent than a VLAN attachment, using global VPC dynamic routing

This scenario is the same as the preceding example, except that one region, us-west1, is located in North America, and the other region, asia-east1, is located in Asia. Sending traffic between regions on different continents results in more expensive inter-region data transfer rates.

![VM in a different continent, global dynamic routing](https://www.gstatic.com/bricks/image/cloud_google_com_static_network_connectivity_docs_interconnect_images_vm_diff_continent_dyn_routing_svg.svg)

VM in a different continent, global dynamic routing. Intercontinental region-to-region data transfer charges for traffic forwarded from asia-east1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


The only way to send traffic from asia-east1 over Cloud Interconnect in North America is by enabling VPC global dynamic routing. This makes the VLAN attachment in us-west1 available to VMs in all regions in your VPC network. You are then charged the following rates:

  * Intercontinental region-to-region data transfer charges for traffic forwarded from asia-east1 to us-west1.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location.



####   


#### A VM in a different continent than a VLAN attachment, using VPC Network Peering

This scenario is similar to the preceding example, except that there are two VPC networks connected through VPC Network Peering. Sending traffic between regions results in the same rates as the preceding example that uses global dynamic routing.

![VM in a different continent, VPC Network Peering](https://www.gstatic.com/bricks/image/cloud_google_com_static_network_connectivity_docs_interconnect_images_vm_diff_continent_vpc_peering_svg.svg)

VM in a different continent, VPC Network Peering. Intercontinental region-to-region data transfer charges for traffic forwarded from us-east4 to asia-northeast1. Cloud Interconnect data transfer charges for Asia from asia-northeast1 to on-premises.

  


You send traffic from us-east4 to your on-premises network over Cloud Interconnect in Asia by using VPC Network Peering. You are then charged the following rates:

  * Intercontinental region-to-region data transfer charges for traffic forwarded from us-east4 to asia-northeast1.
  * Cloud Interconnect data transfer charges for Asia for traffic from region asia-northeast1 to your on-premises location.



  


#### A non-VM Google Cloud product or service in a different location than a VLAN attachment, using global VPC dynamic routing

In addition to the preceding scenarios, Cloud Interconnect data transfer charges apply to traffic sent from a Google Cloud product or service that is not a VM to your on-premises location over a VLAN attachment. You pay the product's data transfer charges to reach the region of the VLAN attachment, and then pay the Cloud Interconnect data transfer out charges based on the continent where the Cloud Interconnect connection is located.

**Note:** For information about data transfer charges for other Google Cloud products not described in this example, see the pricing page for that product.

The following example describes charges for traffic transferring out from a Cloud Storage bucket in a different region in North America than the region where the VLAN attachment is located.

![Non-VM in two North American regions, global dynamic routing](https://www.gstatic.com/bricks/image/cloud_google_com_static_network_connectivity_docs_interconnect_images_non_vm_global_routing_svg.svg)

Non-VM in two North American regions, global dynamic routing. Cloud Storage data transfer charges for traffic forwarded from a Cloud Storage bucket in northamerica-northeast1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


In this scenario, you have resources in two regions located in North America, us-west1 (Oregon) and northamerica-northeast1 (Montreal). You have enabled [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router.

You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create one VLAN attachment over that connection to us-west1. You then send traffic from a Cloud Storage bucket in northamerica-northeast1 to your on-premises location through the VLAN attachment located in us-west1. You are charged the following rates:

  * The Cloud Storage data transfer cost for forwarding traffic from a Cloud Storage bucket in northamerica-northeast1 to a VLAN attachment in us-west1.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location (because that is where your Cloud Interconnect connection is located).



If the Cloud Storage bucket is located in a different continent than the VLAN attachment, you pay Cloud Storage intercontinental data transfer charges to reach the VLAN attachment in us-west1.

For a full list of pricing scenarios for Cloud Storage, see the [Cloud Storage pricing](https://cloud.google.com/storage/pricing#network-pricing) page.

## 

Cloud Router

Cloud Router is provided free of charge. General networking costs apply to control plane (BGP) traffic. In most cases, these costs are negligible.

For more information about networking costs, see [General network pricing](https://cloud.google.com/vpc/network-pricing#general) in the Virtual Private Cloud (VPC) documentation.

## 

Cloud VPN

At a high level, your Cloud VPN charges consist of the following:

  * An hourly charge for each Cloud VPN gateway; this charge is determined partly by the number of tunnels attached to the gateway, as well as the location of the gateway
  * A monthly charge for IPsec traffic
  * An hourly charge for any external IP address assigned to a VPN gateway but  _not_ used by a tunnel



For more information about Cloud VPN, see the [Cloud VPN overview.](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview)

**Note:** Only VPN tunnels in [certain tunnel states](https://cloud.google.com/network-connectivity/docs/vpn/resources/troubleshooting#message_list) are billed.

### 

Pricing table

To view pricing, select the location of the Cloud VPN gateway. Except where otherwise noted, all details apply to both Classic VPN and HA VPN.

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

Component billed| Price (USD)  
---|---  
Hourly charge for each tunnel attached to the gateway.HA VPN only: For 99.99% availability, you must configure two tunnels, or, if working with an AWS peer gateway, four tunnels.| $0.05 / 1 hour  
IPsec traffic| You are charged as follows:

  * If the Cloud VPN tunnel connects to another Cloud VPN gateway, you are charged data transfer pricing as described in [VM-VM data transfer pricing within Google Cloud ](https://cloud.google.com/vpc/network-pricing#egress-within-gcp). Data transfer pricing is based on the IP addresses of the destination VPN gateway—not the destination VM address.
  * If the source and destination Cloud VPN gateways are in the same Google Cloud region, data transfer is billed as traffic between zones in the same region.
  * If the Cloud VPN tunnel connects to a VPN gateway outside of Google Cloud, you are charged as described in [Internet data transfer out rates ](https://cloud.google.com/vpc/network-pricing#internet_egress).

  
External IP address for VPN gateway| You are charged as described in [IP address pricing ](https://cloud.google.com/vpc/network-pricing#ipaddress).An external IP address is charged only if it is not being used by a VPN tunnel.  
  
Google does not charge for forwarding rules that send traffic to the VPN gateway.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## Pricing scenarios

For help understanding Cloud VPN pricing, refer to the following examples.

  


### us-central1 gateway to data center

Suppose you have a VPN gateway in us-central1. That gateway uses two tunnels to connect with an on-premises data center in Iowa.

Each month, you send 2 tebibytes (TiB) of data through the tunnel, from your Virtual Private Cloud (VPC) network to your data center. At the same time, you send 2 TiB in the other direction—from the data center to your VPC network.

Additionally, your gateway uses a reserved external IP address.

The following table shows the charges that you'd incur during a 30-day month with this setup.

Gateway| Data transfer| Data transfer in| IP address| Total  
---|---|---|---|---  
us-central1 gateway ($0.050) x 2 tunnels x 720 hours = $72.00| 2 TiB (or 2,048 GiB) x $0.11 = $225.28| No charge for data transfer in.| No charge for a reserved external IP address that is used by a tunnel.| $297.28  
  
### asia-northeast1 gateway to data center and another VPC network

Suppose your project has a VPC network called Network A, which includes a VPN gateway in asia-northeast1. This gateway uses two tunnels to connect with an on-premises data center in Tokyo. Additionally, this gateway uses two tunnels to connect with Network B, another VPC network in your project. Network B's gateway is located in europe-west6.

Each month, your data usage is as follows:

  * Users in Network A download 10 TiB of data from Cloud Storage and send it to the Tokyo data center.
  * Networks A and B send each other about 20 TiB of data.



Both the asia-northeast1 and europe-west6 gateways use reserved external IP addresses.

Additionally, you have a third VPN gateway in southamerica-east1. You created this gateway several months ago and assigned it a reserved external IP address. However, you never set up a tunnel for this gateway.

The following table shows the charges that this setup would incur during a 30-day month.

Gateway| Data transfer| Data transfer in| IP address| Total  
---|---|---|---|---  
asia-northeast1 gateway ($0.075), with four tunnels x 720 hours = $216.00| Traffic to the data center:10 TiB (or 10,240 GiB) x $0.14 = $1,433.60| No charge for data transfer in.| No charge for a reserved external IP address that is used by a tunnel.| $3,288.00  
Traffic to Network B:20 TiB (or 20,480 GiB) x $0.08 = $1,638.40| No charge for data transfer in.  
europe-west6 gateway ($0.065) x 2 tunnels x 720 hours = $93.60| Traffic to Network A:20 TiB (or 20,480 GiB) x $0.08 = $1,638.40| No charge for data transfer in.| No charge for a reserved external IP address that is used by a tunnel.| $1,732.00  
southamerica-east1 gateway ($0.075) x 0 tunnels x 720 hours = no charge| No data transfer out.| No charge for data transfer in.| One unused external IP address in southamerica-east1 ($0.015) x 720 hours = $10.80.| $10.80  
Grand total| | | | $5,030.80  
  
## Network Connectivity Center

This document describes pricing for Network Connectivity Center.

Network Connectivity Center is a hub-and-spoke model for network connectivity management in Google Cloud. With this model, virtual private cloud networks and on-premises networks connect to a Network Connectivity Center hub by using  _spokes_ that have [supported Google Cloud spoke resources](https://cloud.google.com/vpc/network-pricing#supported-spoke-resources) attached to them.

For more information about Network Connectivity Center, see the [Network Connectivity Center overview](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

##   


## Current pricing

The following sections describe the current pricing for Network Connectivity Center.

  


### Hubs and spokes

The following table describes charges for hubs and spokes.  _Spoke hours_ refers to the number of hours within a month that a spoke is [active](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status#spoke_states).

Spoke hour charges are waived for up to three VPN spokes and three Cloud Interconnect spokes.

Note: Cloud Interconnect spokes are sometimes referred to as  _VLAN attachment spokes_.

Resource| Price (USD)  
---|---  
Hub| No charge  
Spoke hours (Cloud Interconnect, Cloud VPN and Cloud Router appliance spokes)| $0.075 per hour  
Spoke hours (VPC spokes)| $0.10 per hour  
  
### Data transfer

 _Data transfer_ refers to any traffic that flows between a set of hybrid spokes connected to Network Connectivity Center.

Network Connectivity Center data transfer traffic is different from data transfer in and data transfer out, which flows either into or out of Google's network. In contrast, Network Connectivity Center data transfer can be both: it can flow into and out of Google's network, because it is traffic that is exchanged between any two hybrid spokes.

Data transfer charges are based on gibibytes (GiB) of traffic per month.

Item| Price (USD)  
---|---  
Data transfer to worldwide destinations(excluding Australia)(USD)| 0 gibibyte to 1,024 gibibyte$0.12 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.11 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data transfer to Australia destinations(USD)| 0 gibibyte to 1,024 gibibyte$0.19 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.18 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.15 / 1 gibibyte, per 1 month / account  
  
### Advanced Data Networking

 _Advanced Data Networking_ (ADN) refers to the processing fee charged for all traffic that is sent from a spoke through a hub.

The ADN charge is $0.02 per Gibibyte (GiB) per month.

This charge currently applies for traffic between VPC spokes. ADN charges for hybrid spokes are currently waived.

##   


## Pricing example

  


### Advanced Data Networking

In this example, an enterprise has two Virtual Private Cloud (VPC) global networks, VPC-1 and VPC-2, which it connects via VPC spokes to their Network Connectivity Center hub. Each VPC is in its own project distinct from the hub project.

Each month, VPC-1 sends 10 TiB of data to VPC-2, and VPC-2 sends 5 TiB of data to VPC-1.

The following table describes the charges for one 30-day month.

Resources| Usage| Formula| Estimated monthly cost  
---|---|---|---  
Spoke hour charges| 2 spokes| 2 x 24 hours x 30 days at $0.10| $144  
Advanced Data Networking charges| 10 TiB of data (VPC-1 -> VPC-2)5 TiB of data (VPC-2 -> VPC-1)| 10 TiB (10 * 1024 GiB = 10,240 GiB) at $0.02 per GiB5 TiB (5 *1024 GiB = 5120 GiB) at $0.02 per GiB| $204.80\+ $102.40  
Total cost| 15 TiB of data| | $451.20  
  
Note that both the Spoke hour charges and Advanced Data Networking charges for VPC spokes accrue in their respective projects.

### Data transfer

In this example, an enterprise connects two Router appliance spokes to their Network Connectivity Center hub. One spoke represents an office in Los Angeles (us-west2). Another represents an office in Mumbai (asia-south1).

Every month, the US office transfers 5 TiB of data to the Asia office, and the Asia office transfers 5 TiB to the US office.

The following table describes the charges for one 30-day month.

Resources| Usage| Formula| Estimated monthly cost  
---|---|---|---  
Spoke hour charges| 2 spokes| 2 x 24 hours x 30 days at $0.075| $108.00  
Data transfer charges| 5 TiB of data transferred(Los Angeles -> Mumbai)5 TiB of data transferred(Mumbai -> Los Angeles)Total: 10 TiB between one unique site pair.| 5 TiB (5 * 1,024 GiB = 5,120 GiB) at $0.11 per GiB5 TiB (5 * 1,024 GiB = 5,120 GiB) at $0.11 per GiB| $563.20$563.20  
Advanced Data Networking| 10 TiB of data| 10 TiB (10 * 1,024 GiB = 10,240 GiB) at $0.02 per GiB| $204.80 _Currently waived_  
Total cost| | | $1,234.40  
  
**Pricing for other Google Cloud resources**

The pricing on this page does not include charges for other Google Cloud resources and products that you might be using in conjunction with Network Connectivity Center. For example:

  * If you use Router appliance spokes, you pay for the underlying [Compute Engine](https://cloud.google.com/compute/all-pricing) resources.
  * If you use VLAN attachment spokes, you pay for the underlying [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/pricing) resources.
  * If you use VPN spokes, you pay for the underlying [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn/pricing) resources.



  


**Router appliance**

Pricing for Router appliance is part of Network Connectivity Center pricing. For pricing, see [Network Connectivity Center pricing](https://cloud.google.com/network-connectivity/pricing).

For more information about networking costs, see [General network pricing](https://cloud.google.com/vpc/network-pricing#general) in the Virtual Private Cloud documentation.

## 

Cloud NAT

Cloud NAT pricing is based on the following usage:

  * An  _hourly price for the NAT gateway_ that is based on the number of VM instances that are using the gateway. The per-hour rate is capped at 32 VM instances. Gateways that are serving instances beyond the maximum number are charged at the maximum per-hour rate.
  * Google Cloud counts VM instances that get a NAT assignment as using the gateway. The NAT gateway performs source NAT (SNAT) for data transfer traffic from resources that don't have external IP addresses, and destination NAT (DNAT) for ingress packets that arrive as responses to outbound packets.
  * A  _per-GiB cost for data transfer that is processed by the gateway_. The data processing price is the same across all regions. [Data transfer costs](https://cloud.google.com/vpc/network-pricing#internet_egress) to send traffic from the VM out of the network also apply.
  * An  _hourly price for each static or ephemeral external IP address_ that is used by a NAT gateway.



HourlyHourly

MonthlyMonthly

Number of assigned VM instances| Price per Instance for NAT gateway| Price per GiB processed, inbound and outbound data transfer| Price for a static or an ephemeral external IP address used by a NAT gateway**  
---|---|---|---  
Up to 32 VM instances| $0.0014 / 1 hour| $0.045 / 1 gibibyte| $0.005 / 1 hour  
More than 32 VM instances| $0.044 per hour| $0.045 / 1 gibibyte| $0.005 / 1 hour  
  
****** Applicable to only Public NAT

**Note:** To view your current NAT IP address usage, use the [**gcloud compute routers get-nat-ip-info** command](https://cloud.google.com/sdk/gcloud/reference/compute/routers/get-nat-ip-info).

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

  


The total cost for running a NAT gateway and running traffic through it is as follows:

_total cost for running the gateway_ **=** _hourly cost for the NAT gateway_

**+** _cost per GiB of data that is processed by the gateway_

**+** _hourly cost for the external IP addresses used by the gateway_

**+** _data transfer costs for any traffic leaving the network_

###   


### Pricing example

The following table shows the estimated monthly cost for a single NAT gateway that uses external IP addresses to serve a different number of VM instances. For both cases, the gateway runs for 720 hours in a billing cycle.

Usage| Estimated bill  
---|---  
14 VM instancesGateway uses one external IP addressGateway processes 100 GiB of traffic (data transfer)| ($0.0014 * 14 instances * 720 hours) +($0.005 * 1 external IP addresses * 720 hours) +(100 GiB processed traffic * $0.045) = $22.21  
36 VM instancesGateway uses two external IP addressesGateway processes 200 GiB of traffic (data transfer)| ($0.044 * 720 hours) +($0.005 * 2 external IP addresses * 720 hours) +(200 GiB processed traffic * $0.045) = $47.88  
  
### Logging pricing

NAT logging pricing is described in [Network Telemetry pricing](https://cloud.google.com/vpc/network-pricing#network-telemetry).

Standard pricing for Cloud Logging, BigQuery, or Pub/Sub apply.

## 

Cloud DNS

With Cloud DNS pricing, the charge is per zone per month (regardless of whether you use your zone), and you also pay for queries against your zones.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

**Note:** There is no free tier for Cloud DNS.

**Pricing Table**

The following pricing applies to all [zone types](https://cloud.google.com/dns/docs/zones): public, private, and forwarding. All zone types are aggregated for purposes of pricing. For example, if you have 10 public zones, 10 private zones, and 10 forwarding zones, then your pricing is based on having 30 zones. All queries are aggregated as well, regardless of zone type.

You can use [labels](https://cloud.google.com/dns/docs/zones#updating_labels) to label zones in certain ways. You can then use these labels to see per-label breakdowns in your billing.

  


### Query pricing

###   


Number of queries| Price (USD)  
---|---  
Regular queries| 0 count to 1,000,000,000 count$0.40 / 1,000,000 count, per 1 month / account1,000,000,000 count and above$0.20 / 1,000,000 count, per 1 month / account  
Routing policy queries| 0 count to 1,000,000,000 count$0.70 / 1,000,000 count, per 1 month / account1,000,000,000 count and above$0.35 / 1,000,000 count, per 1 month / account  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### Managed zone pricing

HourlyHourly

MonthlyMonthly

Managed zones*| Price (USD)  
---|---  
Price| 0 month to 25 month$0.00027397325 month to 10,000 month$0.00013698610,000 month and above$0.000041096  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

* Managed zone pricing is calculated based on the number of managed zones that exist at a time, prorated by the percentage of the month they exist. This prorating is measured by hour. Zones that exist for a fraction of an hour are counted as having existed for the whole hour.

Cloud DNS usage does not result in any data transfer out charges.

  


### Pricing for health checks

Health check type| Capabilities| Price  
---|---|---  
Internal fast health checks| \- Default 5s probes (configurable)\- SSL, TCP, and HTTP protocols| $0.50 per health check per month  
Internal premium health checks| \- Default 5s probes (configurable)\- SSL, TCP, HTTP, HTTPS, HTTP/2, and gRPC protocols-[ Content-based health checks](https://cloud.google.com/load-balancing/docs/health-check-concepts#content-based_health_checks) (all protocols except gRPC)| $2.00 per health check per month  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## Pricing example

The following table shows sample Cloud DNS usage patterns and the potential costs per month:

Usages| Standard website| Enterprise| Web virtual hosting provider  
---|---|---|---  
Zones| 5| 200| 100,000  
Zone cost| 5 * $0.20 = $1.00| 25 * $0.20 = $5.00175 * $0.10 = $17.50| 25 * $0.20 = $5.009,975 * $0.10 = $997.5090,000 * $0.03 = $2,700.00  
  
Monthly queries| 10,000,000| 50,000,000| 100,000,000  
Queries cost| 10 * $0.40 = $4.00| 50 * $0.40 = $20.00|   
100 * $0.40 = $40.00  
Total cost| $5.00/month| $42.50/month| $3,742.50/month  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Pricing for queries is proportional to usage. So 500,000 queries would be charged $0.20 (half the price of 1 million queries).

**Note:** ** _If you are a high volume user managing millions of DNS zones and/or record sets,_**[**_contact us_**](https://cloud.google.com/contact/)** _to tell us what you need._**

  


### Post GA pricing example for health checks

  


Resources| Usage| Formula| Estimated cost per month  
---|---|---|---  
**Internal fast health check**|  Single service deployed using 3 Layer 4 internal load balancers, situated in us-east, us-central, and us-west| 3 * 30 days @$0.50 per month| $1.5  
**Internal premium health check**|  Single service deployed using 3 Layer 7 internal load balancers, situated in us-east, us-central, and us-west| 3 * 30 days @ $2.0 per month| $6.0  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Service Directory

HourlyHourly

MonthlyMonthly

Component billed| Price (USD)  
---|---  
Service Directory namespace, service, or endpoint registered by using the API| $0.000136986 / 1 hour  
Service Directory namespace, service, or endpoint registered by using automatic integration, such as an internal load balancer, Private Service Connect, or Google Kubernetes Engine| $0.00 (Free) / 1 hour  
Service Directory API calls| $1.00 / 1,000,000 count  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

Note that if you use Service Directory zones, you are billed separately for Cloud DNS based on [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

## 

Service Extensions

This document explains Service Extensions pricing details.

### 

Service Extensions Plugins

The following charges apply for Service Extensions plugins on Cloud Load Balancing.

Type of usage| Price (USD)  
---|---  
Invocations*| 0 count to 2,000,000 count$0.00 (Free) / 1,000,000 count, per 1 month / account2,000,000 count and above$0.10 / 1,000,000 count, per 1 month / account  
  
* An invocation is defined as an individual callback. REQUEST_HEADERS, REQUEST_BODY, RESPONSE_HEADERS, RESPONSE_BODY are all treated as separate callbacks. A single HTTP request may have multiple invocations depending on how many callbacks are configured.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Service Extensions Callouts

The following charges apply for Service Extensions callouts on Cloud Load Balancing. Other relevant charges for data transfer may apply for cross-region traffic and any compute at the other end of the callout.

Type of usage| Price (USD)  
---|---  
Invocations*| $0.10 / 1,000,000 count  
  
* An invocation is defined as an individual callout. A single HTTP request may have multiple invocations depending on how many callouts are configured.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Cloud Domains

### Pricing overview

**Note:** On September 7, 2023 Squarespace acquired all domain registrations and related customer accounts from Google Domains. For more information about how this change affects Cloud Domains, see [Cloud Domains feature deprecations](https://cloud.google.com/domains/docs/deprecations/feature-deprecations), [Google Domains FAQ](https://support.google.com/domains/answer/13689670), and [Squarespace purchase of Google Domains FAQ](https://cloud.google.com/domains/docs/faq).

Domains are registered in increments of one year. By registering a domain, you're committing to paying for the whole year. Domains are renewed automatically. If your domain renews in Cloud Domains, you are billed for the 12 months following your renewal date. If you want to stop paying for your domain, or if don't want your domain to automatically renew, see [Turn off automatic renewal for a domain name](https://cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew).

**Note:** If you use Cloud DNS, you are billed separately for the DNS cost. For detailed information on Cloud DNS pricing, see the [Cloud DNS pricing page](https://cloud.google.com/dns/pricing).

### Pricing per domain ending

Prices vary based on domain endings (TLDs) listed in the [pricing table](https://cloud.google.com/vpc/network-pricing#pricing-table). For example, if you buy example.com, example.charity, and example.wiki, the yearly cost of each of these domains differ because the domain endings .com, .charity, and .wiki have different costs. The yearly price of each domain that you register is added to get the total cost. See the [Pricing example](https://cloud.google.com/vpc/network-pricing#pricing-example).

Cloud Domains does not support the following kinds of domains:

  * [Premium domains](https://cloud.google.com/domains/docs/key-terms#premium-domains)
  * Domains that require a trademark notice



###   


### Billing models

**Caution:** Transferring a registered domain from a third-party domain registrar to Cloud Domains is deprecated and removed. For more information, see [Google Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations).

  


#### Subscription billing (for Cloud Billing accounts outside Brazil)

The  _Subscription_ billing model bills you the yearly amount for the domain in the first month following a domain registration, renewal, or transfer. This applies to all domains that are registered, renewed, or transferred at Cloud Domains general availability.

Charges from Cloud Domains show up on your invoice under ** _Charges not specific to a project_** because the charges are tied to the Cloud Billing account.

The  _Subscription_ billing model is not included in the Enterprise Discount Program.

  


#### Commitment billing (for Cloud Billing accounts in Brazil)

If your Cloud Billing account has a Brazil address, the  _Commitment_ billing model bills you 1/12 of the total cost every month for the next 12 months until the domain expires. This applies to all domains that are registered, renewed, or transferred at Cloud Domains general availability.

Charges from Cloud Domains show up on your invoice under ** _Charges not specific to a project_** because the charges are tied to the billing account.

The  _Subscription_ billing model is not included in the Enterprise Discount Program.

If you choose to transfer a registered domain to another registrar during the 12-month period from your registration, renewal, or transfer to Cloud Domains date, you are charged a cancellation fee. The cancellation fee is equal to the unbilled portion of the annual cost of the domain.

  


### Billing for newly registered domains

When you register a domain using Cloud Domains, you are committing to paying for a full year of registration.

###   


### Billing for transferred-in domains

When you transfer in a domain from another provider, billing is as follows.

  * Your existing registration time with your original provider is maintained.
  * On completion of the transfer, the registration time is extended by a year.
  * You are billed for the extended year right away.
  * You are not billed again until your domain is about to expire and needs to be renewed.



Any domains transferred-in use subscription or commitment billing.

#### Example

The following examples explain how billing works for transferred-in domains.

  * If the domain had one month of registration time left before transfer, you get billed for 1 year at time of transfer. The next billing event after the transfer completes is the domain's next renewal, 13 months (1 month + 1 year) after the transfer.
  * If the domain had two years of registration time left before transfer, the next billing event is 3 years (2 years + 1 year) later.



###   


### Billing for renewals

Renewed domains are billed using either subscription or commitment billing.

**Caution:** Exporting a registered domain from Cloud Domains to Google Domains is deprecated and removed. For more information, see [Cloud Domains feature deprecation](https://cloud.google.com/domains/docs/deprecations/feature-deprecations).

To stop automatic renewal, see [Turn off automatic renewal for a domain name](https://cloud.google.com/domains/docs/edit-registration-settings#turn-off-renew). To manage a domain's billing account individually (outside of a Google Cloud project), you must transfer it out to a third-party registrar. However, once you register a domain with Cloud Domains, if you choose to transfer your domain to a third party before the 12-month period expires, you are still charged for the domain for the remainder of the 12 months. The billing frequency depends on the billing model for your resource.

For more information about renewals, see [Squarespace purchase of Google Domains FAQ.](https://cloud.google.com/domains/docs/faq)

You must use Cloud Domains billing to manage the billing of domains registered with Cloud Domains.

###   


### Free usage

Cloud Domains does not offer free usage for domain registration. For information on quotas, see the [Quotas](https://cloud.google.com/domains/quotas) page.

  


### Pricing table

Domain ending or TLD| Yearly price per unit (USD)  
---|---  
.academy| $30.00  
.accountant| $30.00  
.actor| $40.00  
.agency| $20.00  
.airforce| $30.00  
.apartments| $60.00  
.app| $14.00  
.army| $30.00  
.art| $14.00  
.associates| $30.00  
.attorney| $40.00  
.auction| $30.00  
.autos| $15.00  
.band| $20.00  
.bargains| $30.00  
.best| $20.00  
.bid| $30.00  
.bike| $30.00  
.bingo| $50.00  
.biz| $15.00  
.black| $60.00  
.blog| $30.00  
.blue| $20.00  
.boats| $15.00  
.boutique| $30.00  
.builders| $30.00  
.business| $12.00  
.buzz| $40.00  
.cab| $30.00  
.cafe| $40.00  
.camera| $40.00  
.camp| $40.00  
.capital| $50.00  
.cards| $30.00  
.care| $30.00  
.careers| $50.00  
.cash| $30.00  
.catering| $30.00  
.cc| $20.00  
.center| $20.00  
.charity| $30.00  
.chat| $40.00  
.cheap| $30.00  
.church| $40.00  
.city| $20.00  
.claims| $60.00  
.cleaning| $40.00  
.clinic| $50.00  
.clothing| $30.00  
.cloud| $20.00  
.club| $13.00  
.co| $30.00  
.co.in| $11.00  
.co.nz| $19.00  
.co.uk| $12.00  
.coach| $60.00  
.codes| $50.00  
.coffee| $30.00  
.com| $12.00  
.com.mx| $20.00  
.community| $30.00  
.company| $14.00  
.computer| $30.00  
.condos| $50.00  
.construction| $30.00  
.consulting| $30.00  
.contact| $12.00  
.contractors| $30.00  
.cool| $30.00  
.coupons| $60.00  
.cricket| $30.00  
.cruises| $50.00  
.dance| $20.00  
.date| $30.00  
.dating| $50.00  
.day| $12.00  
.de| $7.00  
.deals| $40.00  
.degree| $40.00  
.delivery| $60.00  
.democrat| $30.00  
.dental| $50.00  
.dentist| $40.00  
.design| $40.00  
.dev| $12.00  
.diamonds| $50.00  
.digital| $40.00  
.direct| $40.00  
.directory| $20.00  
.discount| $30.00  
.dog| $40.00  
.domains| $30.00  
.download| $30.00  
.earth| $20.00  
.education| $20.00  
.email| $20.00  
.engineer| $30.00  
.engineering| $50.00  
.enterprises| $30.00  
.equipment| $20.00  
.estate| $30.00  
.events| $30.00  
.exchange| $30.00  
.expert| $50.00  
.exposed| $20.00  
.express| $30.00  
.fail| $30.00  
.faith| $30.00  
.family| $20.00  
.fan| $40.00  
.fans| $12.00  
.farm| $30.00  
.finance| $60.00  
.financial| $50.00  
.fish| $30.00  
.fitness| $30.00  
.flights| $50.00  
.florist| $30.00  
.football| $30.00  
.forsale| $30.00  
.foundation| $30.00  
.fr| $10.00  
.fun| $20.00  
.fund| $50.00  
.furniture| $50.00  
.futbol| $13.00  
.fyi| $20.00  
.gallery| $20.00  
.games| $20.00  
.gifts| $40.00  
.gives| $30.00  
.glass| $40.00  
.gmbh| $30.00  
.golf| $60.00  
.graphics| $20.00  
.gratis| $20.00  
.gripe| $30.00  
.group| $20.00  
.guide| $40.00  
.guru| $28.00  
.haus| $28.00  
.healthcare| $60.00  
.hockey| $60.00  
.holdings| $50.00  
.holiday| $50.00  
.homes| $15.00  
.hospital| $50.00  
.house| $30.00  
.how| $30.00  
.icu| $12.00  
.immo| $40.00  
.immobilien| $30.00  
.in| $12.00  
.industries| $30.00  
.info| $12.00  
.ink| $28.00  
.institute| $20.00  
.insure| $60.00  
.international| $20.00  
.io| $60.00  
.irish| $14.00  
.jetzt| $20.00  
.jewelry| $60.00  
.jp| $40.00  
.kaufen| $30.00  
.kitchen| $40.00  
.land| $30.00  
.lawyer| $40.00  
.lease| $50.00  
.legal| $60.00  
.life| $40.00  
.lighting| $20.00  
.limited| $30.00  
.limo| $50.00  
.live| $20.00  
.llc| $30.00  
.loan| $30.00  
.love| $30.00  
.ltd| $20.00  
.luxury| $40.00  
.maison| $50.00  
.management| $20.00  
.market| $40.00  
.marketing| $30.00  
.mba| $40.00  
.me| $20.00  
.media| $30.00  
.memorial| $60.00  
.men| $30.00  
.mobi| $20.00  
.moda| $30.00  
.money| $40.00  
.mortgage| $40.00  
.mx| $40.00  
.navy| $30.00  
.net| $12.00  
.network| $20.00  
.news| $30.00  
.ninja| $19.00  
.ni| $8.00  
.one| $12.00  
.online| $30.00  
.ooo| $30.00  
.org| $12.00  
.page| $10.00  
.partners| $50.00  
.parts| $30.00  
.party| $30.00  
.photography| $20.00  
.photos| $20.00  
.pictures| $11.00  
.pizza| $60.00  
.place| $15.00  
.plumbing| $40.00  
.plus| $40.00  
.press| $60.00  
.pro| $20.00  
.productions| $30.00  
.promo| $20.00  
.properties| $30.00  
.pub| $30.00  
.pw| $9.00  
.racing| $30.00  
.recipes| $50.00  
.red| $20.00  
.rehab| $30.00  
.reisen| $20.00  
.rentals| $30.00  
.repair| $30.00  
.report| $20.00  
.republican| $30.00  
.rest| $40.00  
.restaurant| $60.00  
.review| $30.00  
.reviews| $20.00  
.rip| $20.00  
.rocks| $13.00  
.run| $20.00  
.sale| $30.00  
.salon| $50.00  
.sarl| $40.00  
.school| $40.00  
.schule| $20.00  
.science| $30.00  
.services| $30.00  
.shoes| $40.00  
.shopping| $30.00  
.show| $40.00  
.singles| $30.00  
.site| $20.00  
.ski| $50.00  
.soccer| $20.00  
.social| $30.00  
.software| $40.00  
.solar| $40.00  
.solutions| $20.00  
.soy| $20.00  
.space| $20.00  
.store| $50.00  
.stream| $30.00  
.studio| $20.00  
.style| $40.00  
.supplies| $20.00  
.supply| $20.00  
.support| $20.00  
.surgery| $50.00  
.systems| $20.00  
.tax| $50.00  
.taxi| $60.00  
.team| $40.00  
.tech| $40.00  
.technology| $20.00  
.tennis| $60.00  
.theater| $60.00  
.tienda| $50.00  
.tips| $20.00  
.today| $20.00  
.tools| $30.00  
.tours| $60.00  
.town| $30.00  
.toys| $40.00  
.trade| $30.00  
.training| $30.00  
.tube| $30.00  
.uk| $12.00  
.university| $50.00  
.uno| $20.00  
.vacations| $30.00  
.vegas| $60.00  
.ventures| $50.00  
.vet| $30.00  
.viajes| $50.00  
.video| $20.00  
.vilas| $50.00  
.vin| $60.00  
.vision| $30.00  
.voyage| $50.00  
.watch| $30.00  
.webcam| $30.00  
.website| $20.00  
.wiki| $28.00  
.win| $30.00  
.wine| $60.00  
.works| $30.00  
.world| $40.00  
.wtf| $30.00  
.xyz| $12.00  
.zone| $30.00  
  
If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## Billing SKUs

To search for appropriate SKUs for the billing model applicable to your registration, transfer, or renewal, use the following links.

  * [All Cloud Domains SKUs](https://cloud.google.com/skus?currency=USD&filter=Cloud+Domains).
  * [**Subscription** billing SKUs](https://cloud.google.com/skus?currency=USD&filter=Cloud+Domains+Subscription).
  * [**Commitment** billing SKUs](https://cloud.google.com/skus?currency=USD&filter=Cloud+Domains+Commitment+fee).
  * [**Cancellation** SKUs](https://cloud.google.com/skus?currency=USD&filter=Cloud+Domains+Cancellation+fee).



  


### Pricing example

The following examples use US pricing.

  


#### Example 1

**Subscription billing** : You buy a $12 .com domain. On your next monthly bill you are charged $12. Your next charge is one year later when the domain renews for $12.

**Commitment billing** : You buy a $12 .com domain. On your next monthly bill you are charged $1, and you are charged $1 for each monthly billing cycle until the domain expires. If you decide to delete the domain after being billed for 5 months ($5 total), you are billed a $7 cancellation fee to bring the billed total to $12.

  


#### Example 2

Suppose that you have registered three domains: example.charity, example.wiki, and example.info.

The cost is:

.charity = $30/year

.wiki = $28/year

.info = $12/year

 _Subscription_ cost = $30 + $28 + $12 = $70/year

 _Commitment_ billing = 1/12th of the yearly price = $70/12 = $5.83/month

## Whats's next

  * Read the [Virtual Private Cloud documentation](https://cloud.google.com/vpc/docs).
  * Try the [Pricing calculator](https://cloud.google.com/products/calculator).
  * Learn about [VPC solutions and use cases](https://cloud.google.com/architecture?text=Virtual%20Private%20Cloud).



  


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

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/vpc/network-pricing&hl=en-US&prompt=select_account&service=cloudconsole)

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


