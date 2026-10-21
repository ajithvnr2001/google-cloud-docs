---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/pricing/
title: Network Connectivity pricing | Google Cloud
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:07:39.573879+00:00
---

# Network Connectivity pricing | Google Cloud

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/pricing/

Page Contents




# 

Network Connectivity pricing

This page describes pricing for all Network Connectivity products.

## 

Cloud VPN pricing

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

If the source and destination Cloud VPN gateways are in the same Google Cloud region, data transfer is billed as traffic between zones in the same region.

  * If the Cloud VPN tunnel connects to a VPN gateway outside of Google Cloud, you are charged as described in [Internet data transfer out rates ](https://cloud.google.com/vpc/network-pricing#internet_egress).

  
External IP address for VPN gateway| You are charged as described in [IP address pricing ](https://cloud.google.com/vpc/network-pricing#ipaddress).An external IP address is charged only if it is not being used by a VPN tunnel.  
  
  
Google does not charge for forwarding rules that send traffic to the VPN gateway.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

### 

Pricing scenarios

For help understanding Cloud VPN pricing, refer to the following examples.

**us-central1 gateway to data center**

Suppose you have a VPN gateway in us-central1. That gateway uses two tunnels to connect with an on-premises data center in Iowa.

Each month, you send 2 tebibytes (TiB) of data through the tunnel, from your Virtual Private Cloud (VPC) network to your data center. At the same time, you send 2 TiB in the other direction—from the data center to your VPC network.

Additionally, your gateway uses a reserved external IP address.

The following table shows the charges that you'd incur during a 30-day month with this setup.

Gateway| Data transfer| Data transfer in| IP address| Total  
---|---|---|---|---  
**us-central1** gateway ($0.050) x 2 tunnels x 720 hours = $72.00| 2 TiB (or 2,048 GiB) x $0.11 = $225.28| No charge for data transfer in  
| No charge for a reserved external IP address that is used by a tunnel  
| $297.28  
  
**asia-northeast1 gateway to data center and another VPC network**

Suppose your project has a VPC network called Network A, which includes a VPN gateway in asia-northeast1. This gateway uses two tunnels to connect with an on-premises data center in Tokyo. Additionally, this gateway uses two tunnels to connect with Network B, another VPC network in your project. Network B's gateway is located in europe-west6.

Each month, your data usage is as follows:

  * Users in Network A download 10 TiB of data from Cloud Storage and send it to the Tokyo data center.
  * Networks A and B send each other about 20 TiB of data.



Both the asia-northeast1 and europe-west6 gateways use reserved external IP addresses.

Additionally, you have a third VPN gateway in southamerica-east1. You created this gateway several months ago and assigned it a reserved external IP address. However, you never set up a tunnel for this gateway.

The following table shows the charges that this setup would incur during a 30-day month.

Gateway| Data transfer| Data transfer in| IP address| Total  
---|---|---|---|---  
**asia-northeast1** gateway ($0.075), with four tunnels x 720 hours = $216.00| Traffic to the data center: 10 TiB (or 10,240 GiB) x $0.14 = $1,433.60  
| No charge for data transfer in.| No charge for a reserved external IP address that is used by a tunnel.  
| $3,288.00  
  
| Traffic to Network B: 20 TiB (or 20,480 GiB) x $0.08 = $1,638.40  
| No charge for data transfer in.| |   
**europe-west6** gateway ($0.065) x 2 tunnels x 720 hours = $93.60| Traffic to Network A: 20 TiB (or 20,480 GiB) x $0.08 = $1,638.40  
| No charge for data transfer in.  
| No charge for a reserved external IP address that is used by a tunnel.  
| $1,732.00  
  
**southamerica-east1** gateway ($0.075) x 0 tunnels x 720 hours = no charge| No data transfer out  
| No charge for data transfer in.| One unused external IP address in **southamerica-east1** ($0.015) x 720 hours = $10.80.  
| $10.80  
  
Grand total| | | | $5,030.80  
  
## 

Cloud Interconnect pricing

This document explains Cloud Interconnect pricing details.

If you pay in a currency other than USD, the prices listed in your currency on [Cloud Platform SKUs](https://cloud.google.com/skus/) apply.

## 

Dedicated Interconnect

Google charges you on an hourly basis for both Cloud Interconnect connections and VLAN attachments. The hourly charge for each resource, either Cloud Interconnect connection or VLAN attachment, is charged to the project that owns the resource.

Data transfer from your Virtual Private Cloud (VPC) networks through your Cloud Interconnect connections is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Data transfer out pricing depends on the number of gibibytes (GiB) transferred and the location of your Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for the data transfer. Specifically, costs for data transfer from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your Dedicated Interconnect connections, VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an IP address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer, you are charged only for Cloud Interconnect data transfer out. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

### 

Pricing tables

**Dedicated Interconnect pricing**

HourlyHourly

MonthlyMonthly

Resource| Price (USD)  
---|---  
Cloud Interconnect connection 10-Gbps circuit| $2.328 / 1 hour  
Cloud Interconnect connection 100-Gbps circuit| $23.28 / 1 hour  
50-, 100-, 200-, 300-, 400-, or 500-Mbps VLAN attachment| $0.10 / 1 hour  
1-, 2-, 5-, or 10-Gbps VLAN attachment| $0.10 / 1 hour  
20-Gbps VLAN attachment| $0.20 / 1 hour  
50-Gbps VLAN attachment| $0.50 / 1 hour  
100-Gbps VLAN attachment| $1.00 / 1 hour  
  
**Application awareness on Dedicated Interconnect pricing**

HourlyHourly

MonthlyMonthly

Cloud Interconnect connection| Application awareness price  
---|---  
10-Gbps| $0.3492 / 1 hour  
100-Gbps| $3.492 / 1 hour  
  
**Data transfer from a VPC network through a Cloud Interconnect connection**

**North America**

The following table shows the prices for the North America geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
**Europe, Middle East, and Africa (EMEAR)**

﻿The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
**Asia**

﻿The following table shows the prices for the Asia geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
﻿* Includes all of Asia except China, India, Indonesia, and the Philippines.

**Australia**

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
**South America**

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
**Inbound data transfer through a Cloud Interconnect connection**

Traffic type| Price  
---|---  
Data transfer in| Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
**Pricing example**

The following table shows an example usage pattern of Dedicated Interconnect connections for a single month.

Resources| Usage| Estimated cost  
---|---|---  
Cloud Interconnect connection| capacity 30 Gbps (3 x 10-Gbps circuit)| 3 x 10-Gbps circuit x 24 hrs @ $2.328 per hour x 30 days = $5,028.48  
Redundant Cloud Interconnect connection| capacity 30 Gbps (3 x 10-Gbps circuit)| 3 x 10-Gbps circuit x 24 hrs @ $2.328 per hour x 30 days = $5,028.48  
VLAN attachment| 6 (one per Cloud Interconnect connection circuit)| 6 x 10-Gbps attachment x 24 hrs @ $0.10 per hour x 30 days = $432.00  
Data transfer [(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#how-it-works-dedicated)| 20 TiB  
| 20,480 GiB x $0.02 = $409.60  
  
Total cost| | $10,898.56  
  
## 

Partner Interconnect

Google charges you on an hourly basis for VLAN attachments, depending on their capacity. The hourly charges are billed to the project that owns the VLAN attachment. Your service provider might also charge you for services such as using their network, which isn't included in your Google Cloud bills. For information about their pricing, contact your service provider.

Data transfer from your VPC networks though your attachments is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Outbound data transfer pricing depends on the number of gibibytes (GiB) transferred and the location of your Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for data transfer. Specifically, costs for data transfer traffic from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer, you are charged only for Cloud Interconnect outbound data transfer. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

### 

Pricing tables

Partner Interconnect pricing

HourlyHourly

MonthlyMonthly

Partner VLAN attachment capacity| Price (USD)  
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
  
### 

Data transfer from a VPC network through a Cloud Interconnect connection

**North America**

The following table shows the prices for the North America geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
**Europe, Middle East, and Africa (EMEAR)**

The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
**Asia**

The following table shows the prices for the Asia geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
* Includes all of Asia except China, India, Indonesia, and the Philippines.

**Australia**

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
**South America**

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
### 

Inbound data transfer through a Cloud Interconnect connection

Traffic type| Price (USD)  
---|---  
Data transfer in| Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
### 

Pricing example

The following table shows an example usage pattern of Partner Interconnect connections for a single month.

Resources| Usage| Estimated cost  
---|---|---  
VLAN attachment| 6 100-Mbps attachments| 6 x $0.0625 x 720 hours = $270.00  
Data transfer out [(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#how-it-works-partner)| 20 TiB  
| 20,480 GiB x $0.02 = $409.60  
  
Total cost| | $679.60  
  
## 

Cross-Cloud Interconnect

Google charges you on an hourly basis for both Cross-Cloud Interconnect connections and VLAN attachments. The hourly charge for each resource, either Cross-Cloud Interconnect connection or VLAN attachment, is charged to the project that owns the resource.

Data transfer from your Virtual Private Cloud (VPC) networks through your Cross-Cloud Interconnect connections is discounted compared to [general network pricing for Google Cloud](https://cloud.google.com/vpc/network-pricing#general). Data transfer pricing depends on the number of gibibytes (GiB) transferred and the location of your Cross-Cloud Interconnect connection.

This discounted pricing applies only to traffic that originates in the region where the VLAN attachment is located. You can use VLAN attachments to access services located in a different region than the VLAN attachment. In this case, you are charged standard cross-region rates for traffic between the region where the VLAN attachment is located and the region where the service is located.

Cross-Cloud Interconnect data transfer out charges accrue to the project that owns the VLAN attachment. The project that owns the Cloud Interconnect connection is not billed for data transfer. Specifically, costs for data transfer from a VLAN attachment in a Shared VPC service project, which travels through a Cloud Interconnect connection in a different host project, are attributed to the service project.

For [HA VPN over Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect) deployments, you are charged for your Cross-Cloud Interconnect connections, VLAN attachments, HA VPN tunnels, and regional external IP addresses, if an IP address is assigned to a VPN gateway but not used by a tunnel.

In terms of HA VPN over Cloud Interconnect data transfer out, you are charged only for Cloud Interconnect data transfer. You are not charged for Cloud VPN data transfer.

For more information, see [Cloud VPN pricing](https://cloud.google.com/vpc/network-pricing#vpn-pricing).

### 

Pricing tables

Cross-Cloud Interconnect pricing

HourlyHourly

MonthlyMonthly

Resource| Price (USD)  
---|---  
Cross-Cloud Interconnect connection| $5.60 / 1 hour  
Cross-Cloud Interconnect connection| $30.00 / 1 hour  
A 50-, 100-, 200-, 300-, 400-, or 500-Mbps VLAN attachment| $0.10 / 1 hour  
A 1-, 2-, 5-, or 10-Gbps VLAN attachment| $0.10 / 1 hour  
A 20-Gbps VLAN attachment| $0.20 / 1 hour  
A 50-Gbps VLAN attachment| $0.50 / 1 hour  
A 100-Gbps VLAN attachment| $1.00 / 1 hour  
  
### 

Application awareness on Cross-Cloud Interconnect pricing

HourlyHourly

MonthlyMonthly

Cloud Interconnect connection| Application awareness price  
---|---  
10-Gbps| $0.3492 / 1 hour  
100-Gbps| $3.492 / 1 hour  
  
### 

Data transfer from a VPC network through a Cloud Interconnect connection

**North America**

The following table shows the prices for the North America geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
United States, Canada| United States, Canada| $0.02 / 1 gibibyte  
Mexico| United States, Canada| $0.1107 / 1 gibibyte  
  
**Europe, Middle East, and Africa (EMEAR)**

The following table shows the prices for the Europe, Middle East, and Africa (EMEAR) geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Europe| Europe| $0.02 / 1 gibibyte  
Middle East| Europe| $0.10 / 1 gibibyte  
Africa| Europe| $0.11 / 1 gibibyte  
Middle East| Middle East| $0.09 / 1 gibibyte  
Europe| Middle East| $0.10 / 1 gibibyte  
Africa| Africa| $0.11 / 1 gibibyte  
  
**Asia**

The following table shows the prices for the Asia geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Asia*| Asia*| $0.042 / 1 gibibyte  
Indonesia| Asia*| $0.0594 / 1 gibibyte  
Indonesia| Indonesia| $0.0484 / 1 gibibyte  
Asia*| Indonesia| $0.0594 / 1 gibibyte  
Manila| Indonesia| $0.1306 / 1 gibibyte  
India| India| $0.045 / 1 gibibyte  
  
* Includes all of Asia except China, India, Indonesia, and the Philippines.

**Australia**

The following table shows the prices for the Australia geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
Australia| Australia| $0.042 / 1 gibibyte  
  
**South America**

The following table shows the prices for the South America geographic area.

Connection location| Region of VLAN attachment| Price (USD)  
---|---|---  
South America| South America| $0.11 / 1 gibibyte  
South America| United States| $0.1107 / 1 gibibyte  
  
### 

Inbound data transfer through a Cloud Interconnect connection

Traffic type| Price (USD)  
---|---  
Data transfer in| Google does not charge for inbound data transfer. However, there might be a charge for resources that process the transferred data. For a list of these resources, see the [VPC section of All networking pricing](https://cloud.google.com/vpc/network-pricing#vpc-pricing).Responses to requests count as outbound data transfer traffic and are charged.  
  
### 

Pricing example

The following table shows an example usage pattern of Cross-Cloud Interconnect connections for a single month.

Resources| Usage| Estimated cost  
---|---|---  
Cross-Cloud Interconnect connection| capacity 10 Gbps (1 x 10-Gbps circuit)| 1 x 10-Gbps circuit x 24 hrs @ $5.60 per hour x 30 days = $4,032  
Redundant Cross-Cloud Interconnect connection| capacity 10 Gbps (1 x 10-Gbps circuit)| 1 x 10-Gbps circuit x 24 hrs @ $5.60 per hour x 30 days = $4,032  
VLAN attachment| 2 (one per Cloud Interconnect connection circuit)| 2 x 10-Gbps attachment x 24 hrs @ $0.10 per hour x 30 days = $144.00  
Data transfer [(leaving from a Google Cloud region in the United States over a Cloud Interconnect connection in the United States)](https://cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview#how-it-works-dedicated)| 200 TiB  
| 204,800 GiB x $0.02 = $4,096.00  
  
Total cost| | $12,304  
  
## 

Cross-Site Interconnect pricing

Google charges you on an hourly basis for Cross-Site Interconnect connections. The hourly charge for those resources is charged to the project that owns the resource.

### 

Pricing tables

Cross-Site Interconnect pricing

HourlyHourly

MonthlyMonthly

Resource| Price (USD)  
---|---  
Cross-Site Interconnect connection: per 10-Gbps circuit| $2.328 / 1 hour  
Cross-Site Interconnect connection: per 100-Gbps circuit| $23.28 / 1 hour  
  
**Note:** Hourly wire charges apply on top of the Interconnect connection, and they depend on the source/destination locations of the wire and the wire size. To request wire pricing, contact your account team.

## 

Pricing scenarios

This section describes different pricing scenarios for how Google Cloud calculates pricing for Cloud Interconnect outbound data transfer; that is, when a virtual machine (VM) instance or a non-VM Google Cloud product or service sends traffic to your on-premises location over a VLAN attachment located in the same or different geographical location:

  * [A VM in the same region as a VLAN attachment, using either regional or global VPC dynamic routing](https://docs.cloud.google.com/network-connectivity/pricing#regional-routing)
  * [A VM in the same continent but different region than a VLAN attachment, using global VPC dynamic routing](https://docs.cloud.google.com/network-connectivity/pricing#global-routing-same-cont)
  * [A VM in a different continent than a VLAN attachment, using global VPC dynamic routing](https://docs.cloud.google.com/network-connectivity/pricing#global-routing-intercontinental)
  * [A VM in a different continent than a VLAN attachment, using VPC Network Peering](https://docs.cloud.google.com/network-connectivity/pricing#vpc-peering-intercontinental)
  * [A non-VM Google Cloud product or service in a different location than a VLAN attachment, using global VPC dynamic routing](https://docs.cloud.google.com/network-connectivity/pricing#global-routing-product)



**Note:** You have to pay standard inter-region charges for traffic between the region of the VM and the region of the VLAN attachment, which is more if they are in different continents. This applies to non-VM traffic as well.

For more information about costs for each scenario, including data transfer charges between regions within a continent and between continents, see [General network pricing](https://cloud.google.com/vpc/network-pricing).

### 

A VM in the same region as a VLAN attachment, using either regional or global VPC dynamic routing

**Note:** The dynamic routing mode that you use does not impact the pricing.

In this scenario, there are two regions within North America, us-west1 and us-east1. These regions use VPC [regional dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#regional-dyn-routing) provided by Cloud Router. In this scenario, it doesn't matter which dynamic routing mode you use.

![Cloud Interconnect data transfer charges for North America](https://www.gstatic.com/bricks/image/c3f3864d-da78-44f0-a0a0-db5ba84a8807.svg)

VM in same continent, regional routing (click to enlarge). Cloud Interconnect data transfer charges for North America. No region-to-region data transfer charges.

  


You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create two VLAN attachments over that connection. One VLAN attachment goes to region us-east1, and the other VLAN attachment goes to region us-west1.

If you send traffic from a VM in us-east1 or from a VM in us-west1 to your on-premises location over your Cloud Interconnect connection in SJC, you are charged the following rates:

  * Cloud Interconnect data transfer out charges for North America (because that is where the Cloud Interconnect connection is located).
  * You are  _not_ charged region-to-region data transfer charges because the VMs are using a VLAN attachment in the same region.



**Note:** Unless you enable [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router, your regions without a VLAN attachment have no access to your Cloud Interconnect connection. This also means that you can't accidentally incur intercontinental data transfer charges if you have regions located on different continents.

### 

A VM in the same continent but different region than a VLAN attachment, using global VPC dynamic routing

In this scenario, you have VMs in two regions located in North America, us-west1 and us-east1. You have enabled [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router. Global dynamic routing enables VLAN attachments in one region to be used by one or more VMs located in another region.

![Region-to-region data transfer charges from us-east1 to us-west1](https://www.gstatic.com/bricks/image/d9f9cd6a-63a4-499d-8c37-334e187de6b5.svg)

VM in same continent, global dynamic routing (click to enlarge). Region-to-region data transfer charges from us-east1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create one VLAN attachment over that connection to us-west1. You then send traffic from a VM in us-east1 to your on-premises location through the VLAN attachment located in us-west1. You are then charged the following rates:

  * Region-to-region data transfer charges for forwarding traffic from us-east1 to the VLAN attachment in us-west1. The VLAN attachment in us-west1 is considered the source of traffic.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location.



### 

A VM in a different continent than a VLAN attachment, using global VPC dynamic routing

This scenario is the same as the preceding example, except that one region, us-west1, is located in North America, and the other region, asia-east1, is located in Asia. Sending traffic between regions on different continents results in more expensive inter-region data transfer rates.

![Intercontinental region-to-region data transfer charges for traffic forwarded from asia-east1 to us-west1](https://www.gstatic.com/bricks/image/9e05ba96-6216-43ff-b66d-691217f3ce86.svg)

VM in a different continent, global dynamic routing (click to enlarge). Intercontinental region-to-region data transfer charges for traffic forwarded from asia-east1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


The only way to send traffic from asia-east1 over Cloud Interconnect in North America is by enabling VPC global dynamic routing. This makes the VLAN attachment in us-west1 available to VMs in all regions in your VPC network. You are then charged the following rates:

  * Intercontinental region-to-region data transfer charges for traffic forwarded from asia-east1 to us-west1.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location.



### 

A VM in a different continent than a VLAN attachment, using VPC Network Peering

This scenario is similar to the preceding example, except that there are two VPC networks connected through VPC Network Peering. Sending traffic between regions results in the same rates as the preceding example that uses global dynamic routing.

![Intercontinental region-to-region data transfer charges for traffic forwarded from us-east4 to asia-northeast1](https://www.gstatic.com/bricks/image/33c5cae9-0b6d-433c-a340-35fd04c14a6a.svg)

VM in a different continent, VPC Network Peering (click to enlarge). Intercontinental region-to-region data transfer charges for traffic forwarded from us-east4 to asia-northeast1. Cloud Interconnect data transfer charges for Asia from asia-northeast1 to on-premises.

You send traffic from us-east4 to your on-premises network over Cloud Interconnect in Asia by using VPC Network Peering. You are then charged the following rates:

  * Intercontinental region-to-region data transfer charges for traffic forwarded from us-east4 to asia-northeast1.
  * Cloud Interconnect data transfer charges for Asia for traffic from region asia-northeast1 to your on-premises location.



### 

A non-VM Google Cloud product or service in a different location than a VLAN attachment, using global VPC dynamic routing

In addition to the preceding scenarios, Cloud Interconnect data transfer charges apply to traffic sent from a Google Cloud product or service that is not a VM to your on-premises location over a VLAN attachment. You pay the product's data transfer charges to reach the region of the VLAN attachment, and then pay the Cloud Interconnect data transfer out charges based on the continent where the Cloud Interconnect connection is located.

**Note:** For information about data transfer charges for other Google Cloud products not described in this example, see the pricing page for that product.

The following example describes charges for traffic transferring out from a Cloud Storage bucket in a different region in North America than the region where the VLAN attachment is located.

![Cloud Storage data transfer charges for traffic forwarded from a Cloud Storage bucket in northamerica-northeast1 to us-west1.](https://www.gstatic.com/bricks/image/0e032bd1-9f0f-442b-921e-9be0a5ab073f.svg)

Non-VM in two North American regions, global dynamic routing (click to enlarge). Cloud Storage data transfer charges for traffic forwarded from a Cloud Storage bucket in northamerica-northeast1 to us-west1. Cloud Interconnect data transfer charges for North America from us-west1 to on-premises.

  


In this scenario, you have resources in two regions located in North America, us-west1 (Oregon) and northamerica-northeast1 (Montreal). You have enabled [global dynamic routing](https://cloud.google.com/network-connectivity/docs/router/concepts/overview#global_dynamic_routing_examples) for your VPC network by using Cloud Router.

You order a Cloud Interconnect connection running from your on-premises location to San Jose (SJC) and create one VLAN attachment over that connection to us-west1. You then send traffic from a Cloud Storage bucket in northamerica-northeast1 to your on-premises location through the VLAN attachment located in us-west1. You are charged the following rates:

  * The Cloud Storage data transfer cost for forwarding traffic from a Cloud Storage bucket in northamerica-northeast1 to a VLAN attachment in us-west1.
  * Cloud Interconnect data transfer charges for North America for traffic from region us-west1 to your on-premises location (because that is where your Cloud Interconnect connection is located).



If the Cloud Storage bucket is located in a different continent than the VLAN attachment, you pay Cloud Storage intercontinental data transfer charges to reach the VLAN attachment in us-west1.

For a full list of pricing scenarios for Cloud Storage, see the [Cloud Storage pricing](https://cloud.google.com/storage/pricing#network-pricing) page.

## 

Cloud Router pricing

Cloud Router is provided free of charge. General networking costs apply to control plane (BGP) traffic. In most cases, these costs are negligible.

For more information about networking costs, see [General network pricing](https://cloud.google.com/vpc/network-pricing#general) in the Virtual Private Cloud (VPC) documentation.

## 

Network Connectivity Center pricing

This document describes pricing for Network Connectivity Center.

Network Connectivity Center is a hub-and-spoke model for network connectivity management in Google Cloud. With this model, virtual private cloud networks and on-premises networks connect to a Network Connectivity Center hub by using  _spokes_ that have supported Google Cloud spoke resources attached to them.

For more information about Network Connectivity Center, see the [Network Connectivity Center overview](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

### 

Current pricing

The following sections describe the current pricing for Network Connectivity Center.

### 

Hubs and spokes

The following table describes charges for hubs and spokes.  _Spoke hours_ refers to the number of hours within a month that a spoke is [active](https://cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status#spoke_states).

Spoke hour charges are waived for up to three VPN spokes and three Cloud Interconnect spokes.

**Note** : Cloud Interconnect spokes are sometimes referred to as  _VLAN attachment spokes_.

Resource| Price (USD)  
---|---  
Hub| No charge  
Spoke hours (Cloud Interconnect, Cloud VPN and Cloud Router appliance spokes)| $0.075 per hour  
Spoke hours (VPC and producer VPC spokes)| $0.10 per hour  
  
### 

Advanced Data Networking

 _Advanced Data Networking_ (ADN) refers to the data processing fee charged for all traffic that is sent from a spoke through a hub. Charges are attributed to the spoke project that originates the traffic.

The ADN charge is $0.02 per Gibibyte (GiB) per month.

This charge applies for traffic originating from VPC spokes. Traffic that is sent within a VPC network does not incur ADN. ADN charges for traffic originating from hybrid spokes are currently waived. Hybrid spokes are of type Cloud Interconnect, Cloud VPN or Router Appliance.

### 

Data transfer

Site-to-site data transfer refers to any traffic sent from one hybrid endpoint (VPN, Interconnect VLAN attachment, or Router Appliance) to another hybrid endpoint in a different supported cloud region.

These charges apply even if the hybrid endpoint happens to be connected to another network or project in Google Cloud and doesn't actually leave Google's network; for example, if a VPN tunnel connects to another VPC in Google cloud, traffic from that VPN to an Interconnect VLAN attachment is still considered site-to-site data transfer.

We recommend connecting hybrid endpoints together using Network Connectivity Center (NCC), but note that these charges apply even if NCC isn't used. For example, if static routes are configured to send traffic from one hybrid endpoint to another hybrid endpoint then that traffic would still be billed as site-to-site data transfer.

Data transfer charges are based on gibibytes (GiB) of traffic per month.

Item| Price (USD)  
---|---  
Data transfer to worldwide destinations(excluding Australia)(USD)| 0 gibibyte to 1,024 gibibyte$0.12 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.11 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.08 / 1 gibibyte, per 1 month / account  
Data transfer to Australia destinations(USD)| 0 gibibyte to 1,024 gibibyte$0.19 / 1 gibibyte, per 1 month / account1,024 gibibyte to 10,240 gibibyte$0.18 / 1 gibibyte, per 1 month / account10,240 gibibyte and above$0.15 / 1 gibibyte, per 1 month / account  
  
### 

Pricing example

Advanced Data Networking

In this example, an enterprise has two Virtual Private Cloud (VPC) global networks, VPC-1 and VPC-2, which it connects via VPC spokes to their Network Connectivity Center hub. Each VPC is in its own project distinct from the hub project. Additionally, there is also a Cloud Interconnect (IC-1) spoke connected to the same hub for on-premise network access.

Each month, VPC-1 sends 10 TiB of data to VPC-2, and VPC-2 sends 5 TiB of data to VPC-1. Each VPC-1 and VPC-2 also send an additional 1 TiB of data to the IC-1 spoke over the same period.

The following table describes the charges for one 30-day month.

Resources| Usage| Formula| Estimated monthly cost  
---|---|---|---  
Spoke hour charges| 3 spokes| 2 x 24 hours x 30 days at $0.101 x 24 hours x 30 days at $0.075| $198  
Advanced Data Networking charges| 10 TiB of data (VPC-1 -> VPC-2)5 TiB of data (VPC-2 -> VPC-1)1 TiB of data (VPC-1 -> IC-1)1 TiB of data (VPC-2 -> IC-1)| 10 TiB (10 * 1024 GiB = 10,240 GiB) at $0.02 per GiB5 TiB (5 * 1024 GiB = 5120 GiB) at $0.02 per GiB1 TiB (1 * 1024 GiB = 1024 GiB) at $0.02 per GiB1 TiB (1 * 1024 GiB = 1024 GiB) at $0.02 per GiB| $204.80+$102.40+$20.48+$20.48  
Total cost| 17 TiB of data| | $546.16  
  
Note that both the Spoke hour charges and Advanced Data Networking charges for VPC spokes accrue in their respective projects.

### 

Data transfer

In this example, an enterprise connects two Router appliance spokes to their Network Connectivity Center hub. One spoke represents an office in Los Angeles (us-west2). Another represents an office in Mumbai (asia-south1).

Every month, the US office transfers 5 TiB of data to the Asia office, and the Asia office transfers 5 TiB to the US office.

The following table describes the charges for one 30-day month.

Resources| Usage| Formula| Estimated monthly cost  
---|---|---|---  
Spoke hour charges| 2 spokes| 2 x 24 hours x 30 days at $0.075| $108.00  
Data transfer charges| 5 TiB of data transferred (Los Angeles -> Mumbai)5 TiB of data transferred (Mumbai -> Los Angeles)Total: 10 TiB between one unique site pair.| |   
Advanced Data Networking| 10 TiB of data| 10 TiB (10 * 1,024 GiB = 10,240 GiB) at $0.02 per GiB| $204.80 _Currently waived_  
Total cost| | | $1,234.40  
  
### 

Pricing for other Google Cloud resources

The pricing on this page does not include charges for other Google Cloud resources and products that you might be using in conjunction with Network Connectivity Center. For example:

  * If you use Router appliance spokes, you pay for the underlying [Compute Engine](https://cloud.google.com/compute/all-pricing) resources.
  * If you use VLAN attachment spokes, you pay for the underlying [Cloud Interconnect](https://cloud.google.com/network-connectivity/docs/interconnect/pricing) resources.
  * If you use VPN spokes, you pay for the underlying [Cloud VPN](https://cloud.google.com/network-connectivity/docs/vpn/pricing) resources.



## 

NCC Gateway pricing

Pricing for NCC Gateway is going to change. While the pricing structure is detailed below, there are currently no charges for using NCC Gateway. However, you will incur charges after billing is enabled. The change to billing will be announced at least 90 days before it goes into effect.

### 

Pricing overview

Network Connectivity Center Gateway pricing is based on the following components:

  * **NCC Gateway Spoke Hours:** An hourly charge based on the provisioned capacity tier of the NCC Gateway spoke.
  * **NCC Advanced Data Networking (ADN):** A per-GiB charge for data processed through the Network Connectivity Center, with specific rules applied for traffic to and from the NCC Gateway.



### 

NCC Gateway Spoke Hour Pricing

You are charged hourly for each NCC Gateway spoke attached to an NCC hub, based on its provisioned capacity. The price per hour varies by the capacity tier you select.

Capacity Tier| Price (USD)  
---|---  
1 Gbps| $0.45 per hour  
10 Gbps| $0.95 per hour  
100 Gbps| $3.95 per hour  
  
  * Charges are incurred for each hour the spoke is provisioned, regardless of the data volume.
  * You can choose the capacity tier that best suits your needs.



### 

Advanced Data Networking (ADN) Pricing for NCC Gateway

ADN is charged at $0.02 per GiB of traffic. When using NCC Gateway, the following charging principles apply:

  * **Charged Traffic:**
  * Traffic originating from a VPC spoke and going _to_ an NCC Gateway spoke is charged standard [ADN rates](https://docs.cloud.google.com/network-connectivity/pricing#advanced-data-networking).
  * Traffic originating from an NCC Gateway spoke and going _to_ a third-party service (e.g., Secure Service Edge) is charged standard [ADN rates](https://docs.cloud.google.com/network-connectivity/pricing#advanced-data-networking).
  * **Non-Charged Traffic (Waived):**
  *   

  * Traffic originating from a third-party service and going to an NCC Gateway spoke.
  * Traffic originating from an NCC Gateway spoke and going to a VPC spoke.



### 

Pricing Example

Consider a scenario where you have a 10 Gbps NCC Gateway spoke connected to your NCC hub, used to route traffic between VPCs and a Third-Party Security Service Edge (SSE).

  * **NCC Gateway Spoke Hour:** You will be charged $0.95 per hour for the 10 Gbps gateway.
  * Monthly cost (approx. 730 hours): $0.95 * 730 = $693.50
  * **ADN Charges:**
  * Traffic from your VPC to the NCC Gateway: Charged at $0.02/GiB.
  * Traffic from the NCC Gateway to the 3P SSE: Charged at $0.02/GiB.
  * Traffic from the 3P SSE back to the NCC Gateway: No charge.
  * Traffic from the NCC Gateway back to your VPC: No charge.



If, in a month, 10,000 GiB flows from your VPC to the SSE and 5000 GiB flows back:

  * VPC -> NCC GW: 10000 GiB * $0.02/GiB = $200.00
  * NCC GW -> 3P SSE: 10000 GiB * $0.02/GiB = $200.00
  * 3P SSE -> NCC GW: 5000 GiB * $0.02/GiB = $0 (Waived)
  * NCC GW -> VPC: 5000 GiB * $0.02/GiB = $0 (Waived)
  * Total ADN Charges: $400.00



**Total Estimated Monthly Cost:** $693.50 (Spoke Hour) + $400.00 (ADN) = $1093.50

## 

Router appliance pricing

Pricing for Router appliance is part of Network Connectivity Center pricing. For pricing, see [Network Connectivity Center pricing](https://docs.cloud.google.com/network-connectivity/pricing#network-connectivity-pricing).

For more information about networking costs, see [General network pricing](https://cloud.google.com/vpc/network-pricing#general) in the Virtual Private Cloud documentation.

## 

CDN Interconnect pricing

Traffic between Google Cloud and pre-approved CDN Interconnect locations is billed as follows:

Ingress traffic is free for all regions.

Egress traffic rates apply only to data leaving Compute Engine or Cloud Storage. Egress charges for CDN Interconnect appear on the invoice as "Network Data Transfer Out via Carrier Peering Network" or "Storage Data Transfer Out via peered/interconnect network".

For inter-region CDN Interconnect traffic rates, see [Internet egress rates](https://docs.cloud.google.com/vpc/network-pricing#internet_egress).

Continental location| Intra-region CDN Interconnect traffic rate  
---|---  
North America| $0.08 / 1 gibibyte  
Europe| $0.08 / 1 gibibyte  
Asia| $0.085 / 1 gibibyte  
  
## What's next?

  * Read the [Network Connectivity documentation](https://cloud.google.com/network-connectivity/docs).
  * Get started with [Network Connectivity](https://cloud.google.com/network-connectivity/docs/support).
  * Try the [Pricing calculator](https://cloud.google.com/products/calculator).



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

[Sign in](https://accounts.google.com/AccountChooser?continue=https://cloud.google.com/network-connectivity/pricing&hl=en-US&prompt=select_account&service=cloudconsole)

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


