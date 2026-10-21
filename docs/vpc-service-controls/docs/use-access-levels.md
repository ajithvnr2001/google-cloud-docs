---
url: https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels/
title: Allow access to protected resources from outside a perimeter \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:28:52.058334+00:00
---

# Allow access to protected resources from outside a perimeter  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Allow access to protected resources from outside a perimeter Stay organized with collections  Save and categorize content based on your preferences. 

To grant controlled access to protected Google Cloud resources in service perimeters from outside a perimeter, use **access levels**.

An access level defines a set of attributes that a request must meet for the request to be honored. Access levels can include various criteria, such as IP address and user identity.

For a detailed overview of access levels, read the [Access Context Manager overview](https://docs.cloud.google.com/access-context-manager/docs/overview).

Before you use access levels in your perimeter, consider the following:

  * Access levels and [ingress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules#ingress-rules-reference) work together to control incoming traffic to a perimeter. VPC Service Controls allows a request if it satisfies the conditions of either the access level or the ingress rule.

  * If you add multiple access levels to a service perimeter, VPC Service Controls allows a request if it satisfies the conditions of any one of the access levels.




## Limitations of using access levels with VPC Service Controls

When using access levels with VPC Service Controls, certain limitations apply:

  * Access levels only allow requests from _outside_ a perimeter for the resources of a protected service _inside_ a perimeter.

You cannot use access levels to allow requests from a protected resource _inside_ a perimeter to resources _outside_ the perimeter. For example, a Compute Engine client within a service perimeter calling a Compute Engine `create` operation where the image resource is outside the perimeter. To allow access from a protected resource inside a perimeter to resources outside the perimeter, use an [egress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies).

  * Even though access levels are used to allow requests from outside a service perimeter, you cannot use access levels to allow requests from _another_ perimeter to a protected resource in your perimeter. To allow requests from _another_ perimeter to protected resources in your perimeter, the other perimeter must use an [egress policy](https://docs.cloud.google.com/vpc-service-controls/docs/configuring-ingress-egress-policies). For more information, read about [requests between perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#requests-between-perimeters).

  * To allow perimeter access from private resources deployed in a different project or organization, a Cloud NAT gateway is required in the source project. [Cloud NAT](https://docs.cloud.google.com/nat/docs/nat-product-interactions#interaction-pga) has an integration with [Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) that automatically enables Private Google Access on the resource's subnet, and keeps the traffic to Google APIs and services internal, as opposed to routing it to the internet using the Cloud NAT gateway external IP address. As the traffic is routed within the internal Google network, the `RequestMetadata.caller_ip` field of the `AuditLog` object is redacted to `gce-internal-ip`. Instead of using the Cloud NAT gateway external IP address in the access level for [IP-based allowlist](https://docs.cloud.google.com/vpc-service-controls/docs/access-level-design#source-ip), configure an ingress rule to allow access based on other attributes such as the project or service account.




## Create and manage access levels

Access levels are created and managed using Access Context Manager.

### Create an access level

To create an access level, read about [creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level) in the Access Context Manager documentation.

The following examples explain how to create an access level using different conditions:

  * [IP address](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#corporate-network-example)
  * [User and service accounts](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example) (principals)
  * [Device policy](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes#device-policy)



### Add access levels to service perimeters

You can add access levels to a service perimeter when creating the perimeter, or to an existing perimeter:

  * Read about [adding access levels when you create a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters#external-access)

  * Read about [adding access levels to an existing perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters#add-access-level)




### Manage access levels

For information about listing, modifying, and deleting existing access levels, read [Managing access levels](https://docs.cloud.google.com/access-context-manager/docs/manage-access-levels).

## What's next

  * [Creating an access level](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
