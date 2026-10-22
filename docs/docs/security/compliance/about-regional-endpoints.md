---
url: https://docs.cloud.google.com/docs/security/compliance/about-regional-endpoints/
title: Regional and multi-regional API endpoints overview \u00a0|\u00a0 Security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:24:05.108019+00:00
---

# Regional and multi-regional API endpoints overview  |  Security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/security/compliance/about-regional-endpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Guides ](https://docs.cloud.google.com/docs/security/overview/whitepaper)



Send feedback 

#  Regional and multi-regional API endpoints overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud recommends using regional or multi-regional endpoints in the following scenarios:

  * Data in transit must remain within a specific region or jurisdiction.
  * You need evidence of regional data handling for compliance or audit purposes.
  * You need regionally isolated failure domains for accessing Google Cloud services.



Regional and multi-regional endpoints offer the most benefits to customers who require the use of location-specific services. These endpoints also ensure that in-transit data remains in a particular location. This data locality is maintained whether the data is accessed through private connectivity or through the public internet.

**Note:** Regional and multi-regional API endpoints are supported by a limited number of services, and their availability varies.

Regional and multi-regional endpoints are different than Private Google Access. Private Google Access allows VMs in private subnets to reach Google APIs without traversing the internet. Regional endpoints provide stricter regional isolation and data residency, because the entire request path and service frontend are regionalized.

## Regional endpoints

Regional API endpoints provide access to Google Cloud services through an API endpoint that is scoped to a single Google Cloud region. Traffic sent to a regional endpoint is processed and TLS terminated within the specified region.

For most Google Cloud services, you can use regional endpoints to work with regional resources within the specified region. Operations on global resources, multi-regional resources, and out-of-region regional resources are typically not supported from the regional endpoint.

## Multi-regional endpoints

Multi-regional API endpoints provide access to Google Cloud services through an API endpoint that is scoped to a set of Google Cloud regions within the same country, such as the United States, India, or Canada, or jurisdiction, such as the European Union. Traffic sent to a multi-regional endpoint is processed and TLS terminated entirely within the specified jurisdiction.

For most Google Cloud services, you can use multi-regional endpoints to work with multi-regional resources within the specified multi-region. Operations on global resources, regional resources, and multi-regional resources from other jurisdictions are typically not supported.

## Benefits of regional and multi-regional endpoints

Using regional and multi-regional endpoints has the following benefits:

  * **Data residency** : helps meet strict data residency requirements by keeping data in transit within the chosen region. The TLS session is always terminated within the specified region.
  * **Regional isolation** : reduces cross-regional dependencies, which reduces problems due to failures in other regions.
  * **Compliance** : helps you comply with regulatory or policy requirements that mandate that data is processed and stored within specific geographic boundaries.



## Limitations of regional and multi-regional endpoints

  * Regional and multi-regional endpoints are not accessible through Private Google Access. To connect to regional endpoints through private access, use Private Service Connect to create private endpoints. For more information, see [Access regional Google APIs through private endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).

  * Many services don't support cross-regional operations from regional endpoints. To run cross-regional operations, use global endpoints. If the cross-regional operations remain within one jurisdiction, use multi-regional endpoints.

  * Some Google Cloud services don't support regional or multi-regional endpoints. For a complete list of supported services, see [Regional service endpoints](https://docs.cloud.google.com/docs/security/compliance/regional-service-endpoints).

  * Regional and multi-regional endpoints might have higher latency than global endpoints. Performance varies based on your location and the region that you're using.




## Implement regional and multi-regional endpoints

You can access regional or multi-regional endpoints privately from your VPC through regional load balancers. For example, you can define a [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) perimeter to isolate the cloud resources of a given project from the internet and from unauthorized networks. For a given perimeter, you decide which services to enforce VPC Service Controls for, and then you put projects within the perimeter. For more information, see the Use VPC Service Controls section in this document.

### Public access

You can access regional and multi-regional endpoints publicly over the internet. When you access regional endpoints from the internet, traffic is routed through the Google Cloud [Standard Tier networking](https://docs.cloud.google.com/network-tiers/docs/overview). The connection, including TLS termination, is handled within the destination region.

For more information, see [Access regional Google APIs through public endpoints](https://docs.cloud.google.com/docs/security/compliance/access-public-regional-endpoints).

### Private access

For private access to regional and multi-regional endpoints, use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). Private Service Connect creates a private IP address in your [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/vpc). The private IP address routes to the regional service. Although global APIs often use standard Private Google Access by using special ranges, like `private.googleapis.com`, regional and multi-regional endpoints require explicit private endpoint configuration.

For more information, see [Access regional Google APIs through private endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).

### Configure routing and firewalls

Follow these guidelines to correctly configure your routing and firewalls.

#### On-premises routing

If you connect to regional endpoints from on-premises environments over Cloud Interconnect or Cloud VPN, you must advertise the regional endpoint private IP ranges. This configuration ensures proper routing from your on-premises network to the Google Cloud services.

  * **Cloud Router** : use [custom route advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-custom-learned-routes) to announce all private IP ranges over the hybrid connection.
  * **On-premises firewalls** : configure your on-premises firewalls to allow outbound traffic to the public or private virtual IP address ranges of the regional endpoints. For more information, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).



#### VPC firewall rules

Configure your egress firewall policies to allow traffic to the private IP addresses of the regional endpoints. If you remove default routes, verify that appropriate routes are in place for the regional endpoint virtual IP address (VIP) ranges:

  * For public VIP access, make sure that routes exist for the VIP ranges of the regional endpoints with the next hop set to the default internet gateway.

  * For Private Service Connect, use IP addresses or standard internal routing.




For more information, see [Configure a hierarchical firewall policy to allow egress traffic from a specific VPC network](https://docs.cloud.google.com/firewall/docs/quickstarts/configure-hfwpolicy-allow-egress-vpc).

## Use VPC Service Controls

Regional endpoints are compatible with VPC Service Controls perimeters. For more information about VPC Service Controls, see [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

VPC Service Controls helps prevent data exfiltration from Google Cloud services by creating security perimeters. Because you can't access regional endpoints through Private Google Access, to access the endpoints within a VPC perimeter, you must use Private Service Connect to configure private endpoints.

  * **Perimeter enforcement** : When you add a service, such as `storage.googleapis.com`, to the **Restricted services** list in your VPC Service Controls perimeter, VPC Service Controls rules apply to all access methods for that service, including access through regional endpoints.

  * **Service control checks:** API requests to regional endpoints, whether public or private, are subject to policy checks by the Service Control API. The Service Control API evaluates the request against the VPC Service Controls perimeter configuration and reviews the source network, the source project, and the target resource project.

  * **Inside the perimeter:** Resources within a VPC Service Controls perimeter, such as VMs, can access services through regional endpoints if the service is part of the perimeter's accessible services. The network endpoint must be within your VPC perimeter, which requires you to create private regional endpoints by using Private Service Connect. For more information, see [Access regional Google APIs through private endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).

  * **Outside the perimeter:** Attempts to access resources protected within the perimeter from outside of the perimeter using any endpoint type are blocked by VPC Service Controls, unless access levels or ingress and egress rules explicitly allow access.




For example, you define a VPC Service Controls perimeter to enforce a policy on Cloud Storage resources and then place `secure_project` within the perimeter. Only the VMs from `secure_project` can access the Cloud Storage resources of `secure_project`. In addition, the VMs are prevented from accessing Cloud Storage resources outside of the perimeter.

### Benefits of VPC Service Controls

Using VPC Service Controls provides the following benefits:

  * You get the benefits of regional isolation and data residency along with the data exfiltration protection of VPC Service Controls.

  * With VPC Service Controls, access that is scoped to a single region is also governed by the security boundaries of your VPC Service Controls perimeters.




### Configure VPC Service Controls

Within a VPC Service Controls perimeter, you must access [private regional endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints) by using Private Service Connect from within a VPC perimeter. For more information, see [Access regional Google APIs through private endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).

  * Standard public regional endpoint access might be blocked, because it appears to originate from outside of the perimeter.

  * Ensure that the service that you are accessing, such as `compute.googleapis.com` or `bigquery.googleapis.com`, is included in the list of services restricted by the perimeter.




## Use organization policies for additional enforcement

Organization policies provide additional controls for your organization's cloud resources. The following two policies work with regional endpoints to enforce data residency and to improve regional isolation:

  * Restrict Endpoint Usage (`constraints/gcp.restrictEndpointUsage`)
  * Resource location constraints (`constraints/gcp.resourceLocations`)



### Enforce regional endpoint use

To enforce the use of regional endpoints, use the **Restrict Endpoint Usage** organization policy constraint to deny access to global endpoints. For more information, see [Restrict endpoint usage](https://docs.cloud.google.com/docs/security/compliance/restrict-endpoint-usage).

Regional endpoints ensure that data in transit stays within a region, and the Restrict Endpoint Usage constraint ensures that the resources used to store data at rest are only created in the regions that you allow. Using both policies provides more comprehensive data residency protections for data at rest and for data in transit.

The Restrict Endpoint Usage constraint is set using a denylist, allowing requests to any supported services' API endpoints that are not explicitly denied. After you configure regional endpoints, global endpoints are still accessible unless you use the Restrict Endpoint Usage organization policy constraint.

The Restrict Endpoint Usage constraint controls the physical locations where users can create and store new Google Cloud resources, enforcing data residency at rest. This policy applies only to the creation of new resources for supported services. Existing resources are not impacted.

### Enforce location constraints

The resource locations constraint policy (`constraints/gcp.resourceLocations`) controls the physical locations where new Google Cloud resources can be created and stored, which addresses data residency at rest. For more information, see [Set the organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/defining-locations) in the Resource Manager documentation.

When you use the resource location constraint policy, you define a list of allowed or denied Google Cloud locations. For the locations, you can use regions, zones, or multi-regions. The policy applies only to the creation of new resources for supported services. Existing resources are not impacted.

Using this policy with regional endpoints is beneficial, because regional endpoints ensure that data in transit stays within a region, and the location constraint policy ensures that resources that store the the regions that you allow.

### Combined enforcement

By using the Restrict Endpoint Usage policy to deny global endpoints and the resource locations constraint policy to restrict the locations where resources can be created, you enforce data at rest and data in transit.

  * **Data at rest** : resources are only created and stored in allowed regions.
  * **Data in transit** : API interactions with those resources are handled entirely within the specified region when using the corresponding regional endpoint.



## Pricing

For private regional endpoints, pricing is based on [Private Service Connect usage](https://docs.cloud.google.com/vpc/pricing). Billing charges include the endpoint and data processing.

For public regional endpoints, ingress traffic is not billed. Egress traffic is billed based on [Standard Tier network pricing](https://docs.cloud.google.com/network-tiers/pricing).

## Reference documentation

  * Use the [Google Cloud CLI to manage regional endpoints](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/regional-endpoints).
  * See the [`regionalEndpoints` REST documentation](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.regionalEndpoints).



## What's next

  * [Access private regional endpoints](https://docs.cloud.google.com/docs/security/compliance/access-regional-google-apis-endpoints).
  * [Access public regional endpoints](https://docs.cloud.google.com/docs/security/compliance/access-public-regional-endpoints).
  * [Access regional Google APIs through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls).
  * See the Google Cloud [supported regional service endpoints](https://docs.cloud.google.com/docs/security/compliance/regional-service-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
