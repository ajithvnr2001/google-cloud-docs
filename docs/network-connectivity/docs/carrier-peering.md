---
url: https://docs.cloud.google.com/network-connectivity/docs/carrier-peering/
title: Carrier Peering overview \u00a0|\u00a0 Network Connectivity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:37:50.597901+00:00
---

# Carrier Peering overview  |  Network Connectivity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/carrier-peering/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product)



Send feedback 

#  Carrier Peering overview Stay organized with collections  Save and categorize content based on your preferences. 

Carrier Peering enables you to access Google applications, such as Google Workspace, by using a [service provider](https://docs.cloud.google.com/network-connectivity/docs/carrier-peering#service-providers) to obtain enterprise-grade network services that connect your infrastructure to Google.

When connecting to Google through a service provider, you can get connections with higher availability and lower latency, using one or more links. Work with your service provider to get the connection that you need.

**When to use Carrier Peering**

The following example describes a common use case for Carrier Peering.

To access Google Workspace applications from an on-premises network, an organization might need a perimeter network to reach Google's network. The perimeter network enables organizations to expose an isolated subnetwork to the public internet instead of their entire network. Instead of setting up and maintaining a perimeter network, the organization can work with a service provider so that their traffic travels on a dedicated link from their systems to Google. With the dedicated link, the organization gets a higher availability and lower latency connection to Google's network.

Unless you need to access Google Workspace applications as described in the preceding use case, [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview) is the recommended way to connect to Google through a service provider. To choose a product, see the **Considerations** section and the [table that compares Carrier Peering with Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cp-compare).

**Considerations**

Review the following considerations to decide if Carrier Peering meets your needs:

  * Carrier Peering exists outside of Google Cloud. Instead of Carrier Peering, the recommended methods of access to Google Cloud are [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview), which uses a service provider, or [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview), which provides a direct connection to Google.
  * If used with Google Cloud, Carrier Peering doesn't produce any custom routes in a VPC network. Traffic sent from resources in a VPC network leaves by way of a route whose next hop is either a _default internet gateway_ (a default route, for example) or a Cloud VPN tunnel.
  * To send traffic through Carrier Peering by using a route whose next hop is a Cloud VPN tunnel, the IP address of your on-premises network's VPN gateway must be in your configured destination range.



## Service providers

Review the list of Carrier Peering service providers and choose the option that best suits your needs.

* * *

[![CyrusOne](https://docs.cloud.google.com/static/network-connectivity/docs/images/logos/logo-cyrusone-200px.png)](http://www.cyrusone.com/)

CyrusOne 

[More information](http://www.cyrusone.com/)

* * *

[![Orange Business Services](https://docs.cloud.google.com/static/network-connectivity/docs/images/logos/logo-orange-200px.png)](http://www.orange-business.com/en/products/business-vpn-galerie)

Orange Business Services 

[More information](http://www.orange-business.com/en/products/business-vpn-galerie)

* * *

[![Verizon](https://docs.cloud.google.com/static/network-connectivity/docs/images/logos/logo-verizon-200px.png)](http://www.verizonenterprise.com/products/networking/sdn-nfv/secure-cloud-interconnect/)

Verizon 

[More information](http://www.verizonenterprise.com/products/networking/sdn-nfv/secure-cloud-interconnect/)

* * *

## FAQ

**Where are the connections physically located?**

Service providers offer service in a range of locations around the world. Contact them for local availability of their service. Google and its networking partners are working to increase the number of locations throughout the world where Google's networks connect with carrier networks to deliver the best possible experience.

**Can I purchase connections from multiple service providers?**

Yes, you can purchase from multiple service providers. Doing so may be helpful in situations where you want to connect disparate parts of your WAN that different providers manage and provision separately. In such a case, you would have a commercial relationship with both providers for connectivity.

**Does Google offer a service level agreement (SLA)?**

Customers should consult with their network service provider to determine whether that provider may offer an SLA. Google does not offer an SLA with this program.

**Is the Carrier Peering connection secure?**

Google has no control over the connection traffic while it traverses the provider's network; we encourage customers who have security needs to consider using strong encryption.

**Can I connect to the internet by using this connection?**

No, you cannot connect to non-Google products or services through the Carrier Peering connection.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
