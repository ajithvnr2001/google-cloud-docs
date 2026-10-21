---
url: https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity/
title: Private Google Access with VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:29:53.185696+00:00
---

# Private Google Access with VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Private Google Access with VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Private Google Access offers private connectivity for hosts in either a VPC network or an on-premises network that uses private IP addresses to access [Google APIs and services](https://developers.google.com/apis-explorer/#p/). You can extend a Virtual Private Cloud service perimeter to hosts in those networks to control access to protected resources.

Hosts in a VPC network must have a private IP address only (no public IP address) and be in a subnet with Private Google Access enabled.

For on-premises hosts to reach restricted Google API services, requests to Google APIs must be sent through a VPC network, either through a [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) tunnel or a [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect) connection.

In both cases, we recommend that you send all requests to Google APIs and services to the virtual IP (VIP) address ranges for `restricted.googleapis.com`. The IP address ranges are not announced to the internet. Traffic sent to the VIP stays within Google Cloud's network only.

If you require access to Google APIs and services that aren't supported by VPC Service Controls, we recommend that you use `private.googleapis.com` or a Private Service Connect endpoint with the `all-apis` bundle, combined with [VPC Service Controls service patterns](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services#service-patterns). Service patterns let you control which unsupported APIs are accessible on the private VIP path, mitigating data exfiltration risks. Using `private.googleapis.com` without service patterns can allow access to services that are not compliant with VPC Service Controls and might introduce data exfiltration risks.

If you don't require access to unsupported APIs, we recommend that you use `restricted.googleapis.com`. Using `restricted.googleapis.com` denies access to Google APIs and services that are not supported by VPC Service Controls.

For more information about the `private.googleapis.com` and `restricted.googleapis.com` VIPs, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

## IP address ranges for `restricted.googleapis.com`

There are two IP address ranges associated with the `restricted.googleapis.com` domain:

  * IPv4 range: `199.36.153.4/30`
  * IPv6 range: `2600:2d00:0002:1000::/56`



For information about using the IPv6 range to access Google APIs, see [IPv6 support](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#ipv6-support).

## VPC network example

In the following example, the service perimeter contains two projects: one that has an authorized VPC network and another with the protected Cloud Storage resource. In the VPC network, VM instances must be in a subnet with [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access#pga) enabled and only require access to Virtual Private Cloud restricted services. Queries to Google APIs and services from VM instances in the authorized VPC network resolve to `restricted.googleapis.com` and can access the protected resource.

[ ![Private Google Access with VPC Service
                                  Controls \(click to enlarge\)](https://docs.cloud.google.com/static/vpc-service-controls/images/pga-for-vpc-service-controls-1.svg)](https://docs.cloud.google.com/static/vpc-service-controls/images/pga-for-vpc-service-controls-1.svg) Private Google Access with VPC Service Controls (click to enlarge)

  * DNS was configured in the VPC network to map `*.googleapis.com` requests to `restricted.googleapis.com`, which resolves to `199.36.153.4/30`.
  * A custom static route was added to the VPC network that directs traffic with the destination `199.36.153.4/30` to the `default-internet-gateway` as the next hop. Even though `default-internet-gateway` is used as the next hop, traffic is routed privately through Google's network to the appropriate API or service.
  * The VPC network was authorized to access the `My-authorized-gcs-project` because both projects are in the same service perimeter.



## On-premises network example

You can use either static routing, by simply configuring a static route in the on-premises router, or by announcing the restricted Google API address range through border gateway protocol (BGP) from [Cloud Router](https://docs.cloud.google.com/compute/docs/cloudrouter).

To use Private Google Access for on-premises hosts with Virtual Private Cloud, [set up private connectivity](https://docs.cloud.google.com/vpc/docs/configure-private-google-access-hybrid) for on-premises hosts and then configure VPC. Define a service perimeter for the project that contains the VPC network that's connected to your on-premises network.

In the following scenario, the storage buckets in project `sensitive-buckets` can only be accessed from VM instances in the project `main-project` and from connected on-premises applications. On-premises hosts can access storage buckets in the project `sensitive-buckets` because traffic goes through a VPC network that's inside the same service perimeter as `sensitive-buckets`.

[ ![A diagram that demonstrates an example of using Virtual Private Cloud
              with on-premises hosts.](https://docs.cloud.google.com/static/vpc-service-controls/images/pga-hybrid-use-case1.svg)](https://docs.cloud.google.com/static/vpc-service-controls/images/pga-hybrid-use-case1.svg) Private Google Access for hybrid cloud use case (click to enlarge)

  * The on-premises DNS configuration maps `*.googleapis.com` requests to `restricted.googleapis.com`, which resolves to `199.36.153.4/30`.
  * The Cloud Router was configured to advertise the `199.36.153.4/30` IP address range through the VPN tunnel. Traffic going to Google APIs is routed through the tunnel to the VPC network.
  * A custom static route was added to the VPC network that directs traffic with the destination `199.36.153.4/30` to the `default-internet-gateway` as the next hop. Even though `default-internet-gateway` is used as the next hop, traffic is routed privately through Google's network to the appropriate API or service.
  * The VPC network was authorized to access the `sensitive-buckets` projects, and on-premises hosts have the same access.
  * On-premises hosts can't access other resources that are outside of the service perimeter.



The project that connects to your on-premises network must be a member of the service perimeter to reach restricted resources. On-premises access also works if the relevant projects are connected by a perimeter bridge.

## What's next

  * To configure private connectivity, refer to [Setting up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).
  * Complete the [Deploy an agent and Agent Gateway with VPC codelab](https://codelabs.developers.google.com/agw-vpcsc-codelab) to learn how to configure private connectivity and secure Agent Gateway within a service perimeter.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
