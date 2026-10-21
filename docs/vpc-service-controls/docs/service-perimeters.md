---
url: https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters/
title: Service perimeter details and configuration \u00a0|\u00a0 VPC Service Controls \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:27:19.430770+00:00
---

# Service perimeter details and configuration  |  VPC Service Controls  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ VPC Service Controls ](https://docs.cloud.google.com/vpc-service-controls/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc-service-controls/docs/overview)



Send feedback 

#  Service perimeter details and configuration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes service perimeters and includes the high-level steps for configuring perimeters.

## About service perimeters

This section provides details about the way service perimeters function, and the differences between enforced and dry run perimeters.

To protect Google Cloud services in your projects and mitigate the risk of data exfiltration, you can specify service perimeters at the project or VPC network level. For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Also, the services that are accessible _inside_ a perimeter, such as from VMs in a VPC network that is hosted inside a perimeter, can be restricted using the [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) feature.

You can configure VPC Service Controls perimeters in enforced or dry run mode. The same configuration steps apply to both enforced and dry run perimeters. The difference is that dry run perimeters log violations as though the perimeters are enforced but don't prevent access to restricted services.

### Enforced mode

Enforced mode is the default mode for service perimeters. When a service perimeter is enforced, requests that violate the perimeter policy, such as requests to restricted services from outside a perimeter, are denied.

A perimeter in enforced mode protects Google Cloud resources by enforcing the perimeter boundary for the services restricted in the perimeter configuration. API requests to restricted services do not cross the perimeter boundary unless the conditions of the necessary [ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) of the perimeter are satisfied. An enforced perimeter protects against data exfiltration risks, such as stolen credentials, misconfigured permissions, or malicious insiders that have access to the projects.

### Dry run mode

In dry run mode, requests that violate the perimeter policy are not denied but only logged. _Dry run service perimeters_ are used to test perimeter configuration and to monitor usage of services without preventing access to resources. The following are some of the common use cases:

  * Determining the impact when you change existing service perimeters.

  * Previewing the impact when you add new service perimeters.

  * Monitoring requests to restricted services that originate from outside a service perimeter. For example, to identify from where requests to a given service are coming from or to identify unexpected service usage in your organization.

  * Creating a perimeter architecture in your development environment that is analogous to your production environment. You can identify and mitigate any issues caused by your service perimeters before submitting changes to your production environment.




For more information, see [Dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode).

## Service perimeter configuration stages

To configure VPC Service Controls, you can use the Google Cloud console, [the `gcloud` command-line tool](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager), and the [Access Context Manager APIs](https://docs.cloud.google.com/access-context-manager/docs/apis).

You can configure VPC Service Controls as described in the following high-level steps:

  1. Create an access policy.

  2. Secure Google-managed resources with service perimeters.

  3. Set up VPC accessible services to add additional restrictions to how services can be used inside your perimeters (optional).

  4. Set up private connectivity from a VPC network (optional).

  5. Allow context-aware access from outside a service perimeter using ingress rules (optional).

  6. Configure secure data exchange using ingress and egress rules (optional).




### Create an access policy

An access policy collects the service perimeters and access levels you create for your organization. An organization can have one access policy for the entire organization and multiple scoped access policies for the folders and projects.

You can use the Google Cloud console, [the `gcloud` command-line tool](https://docs.cloud.google.com/sdk/gcloud/reference/access-context-manager), or the [Access Context Manager APIs](https://docs.cloud.google.com/access-context-manager/docs/apis) to [create an access policy](https://docs.cloud.google.com/access-context-manager/docs/create-access-policy).

To learn more about Access Context Manager and access policies, read the [overview of Access Context Manager](https://docs.cloud.google.com/access-context-manager/docs/overview).

### Secure Google-managed resources with service perimeters

Service perimeters are used to protect services used by projects in your organization. After identifying the projects and services you want to protect, [create one or more service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

**Note:** If you're using [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you must [include the host project](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting#shared_vpc) in a service perimeter along with any projects that belong to the Shared VPC.

To learn more about how service perimeters work and what services VPC Service Controls can be used to secure, read the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

Some services have limitations with how they can be used with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#service-limitations). If you encounter issues with your projects after setting up your service perimeters, read [Troubleshooting](https://docs.cloud.google.com/vpc-service-controls/docs/troubleshooting).

### Set up VPC accessible services

When you enable VPC accessible services for a perimeter, access from network endpoints inside your perimeter is limited to a set of services that you specify.

To learn more about how to limit access inside your perimeter to only a specific set of services, read about [VPC accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services).

### Set up private connectivity from a VPC network

To provide additional security for VPC networks and on-premises hosts that are protected by a service perimeter, we recommend using Private Google Access. For more information, see [private connectivity from on-premises networks](https://docs.cloud.google.com/vpc-service-controls/docs/private-connectivity).

To learn about configuring private connectivity, read [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

Restricting access to Google Cloud resources to only private access from VPC networks means that access using interfaces such as the Google Cloud console and the Cloud Monitoring console are denied. You can continue to use the `gcloud` command-line tool or API clients from VPC networks that share a service perimeter or perimeter bridge with the restricted resources.

### Allow context-aware access from outside a service perimeter using ingress rules

You can allow context-aware access to resources restricted by a perimeter based on client attributes. You can specify client attributes, such as identity type (service account or user), identity, device data, and network origin (IP address or VPC network).

For example, you can set up ingress rules to allow internet access to resources within a perimeter based on the range of IPv4 and IPv6 addresses. For more information about using ingress rules to set up context-aware access, see [Context-aware access](https://docs.cloud.google.com/vpc-service-controls/docs/context-aware-access).

### Configure secure data exchange using ingress and egress rules

You can include your project only in one service perimeter. If you want to allow communication across the perimeter boundary, set up ingress and egress rules. For example, you can specify ingress and egress rules to let projects from multiple perimeters to share logs in a separate perimeter. To learn more about secure data exchange use cases, read [secure data exchange](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
  *[VPC]: Virtual Private Cloud
