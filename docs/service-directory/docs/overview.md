---
url: https://docs.cloud.google.com/service-directory/docs/overview/
title: Service Directory overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:32:11.035689+00:00
---

# Service Directory overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Service Directory overview Stay organized with collections  Save and categorize content based on your preferences. 

Service Directory is a service covered by Google's obligations set forth in the [Cloud Data Processing Addendum](https://cloud.google.com/terms/data-processing-addendum).

Service Directory is a single place to publish, discover, and connect to services in a consistent and reliable way, regardless of their environment. Service Directory supports services in Google Cloud, multi-cloud, and on-premises environments and can scale up to thousands of services and endpoints for a single project.

Service Directory has the following features:

  * A **Registration and Lookup API** for creating and resolving [namespaces](https://docs.cloud.google.com/service-directory/docs/key-terms#namespace), [services](https://docs.cloud.google.com/service-directory/docs/key-terms#service), and [endpoints](https://docs.cloud.google.com/service-directory/docs/key-terms#endpoint)
  * Integration with [Cloud DNS](https://docs.cloud.google.com/dns/docs). Service Directory zones allow services to be made available on Virtual Private Cloud (VPC).
  * **[IAM integration](https://docs.cloud.google.com/iam)** to assign and control service visibility and permissions
  * Built-in **[Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/service-directory)** and **[Google Cloud console](https://console.cloud.google.com/net-services/service-directory/namespaces/list)** support for interacting with Service Directory
  * **Cloud Monitoring and Cloud Logging integration** for monitoring, auditing, and debugging Service Directory operations



## Why Service Directory

As applications adopt services, being able to resolve the location of a service becomes more difficult as the endpoints of those services change. Services deployed across hybrid environments present additional obstacles as neither may share the same naming system, making resolving and connecting services challenging. To illustrate the problem, consider the following.

Imagine that you are building a simple API and that your code needs to call some other application. When endpoint information remains static, you can hard-code these locations into your code or store them in a small configuration file. However, with microservices and multi-cloud, this problem becomes much harder to solve as instances, services, and environments can all change.

[ ![Service Directory without a load balancer \(click to enlarge\)](https://docs.cloud.google.com/static/service-directory/images/service-directory-01.svg)](https://docs.cloud.google.com/static/service-directory/images/service-directory-01.svg) Different changing services (click to enlarge)

With Service Directory, you can register all of your services in a single place and resolve them by using HTTP, gRPC, and DNS.

Let us revisit the previous diagram, but this time adding Service Directory. In the following diagram, each service instance is registered with Service Directory. These registrations are immediately reflected in DNS and can be queried by using HTTP/gRPC regardless of their implementation and environment.

[ ![Service Directory with a load balancer \(click to enlarge\)](https://docs.cloud.google.com/static/service-directory/images/service-directory-02.svg)](https://docs.cloud.google.com/static/service-directory/images/service-directory-02.svg) Service Directory with a load balancer (click to enlarge)

You can create a universal service name that works across Google Cloud products, like App Engine and GKE. You can make these services available over DNS. You can apply access controls to services based on network, project, and IAM roles of service accounts.

Service Directory solves the following problems:

  1. **Interoperability** : Service Directory is a universal naming service that works across Google Cloud, multi-cloud, and on-premises. You can migrate services between these environments and still use the same service name to register and resolve endpoints.
  2. **Service management** : Service Directory is a managed service. Your organization does not have to worry about the high availability, redundancy, scaling, or maintenance concerns of maintaining your own service registry.
  3. **Access Control** : With Service Directory, you can control who can register and resolve your services using IAM. Assign Service Directory roles to teams, service accounts, and organizations.
  4. **Limitations of pure DNS** : DNS resolvers can be unreliable in terms of respecting TTLs and caching, cannot handle larger record sizes, and do not offer an easy way to serve metadata to users. In addition to DNS support, Service Directory offers HTTP and gRPC APIs to query and resolve services.



## Use Cloud DNS with Service Directory

Cloud DNS is a fast, scalable, and reliable [Domain Name System](https://wikipedia.org/wiki/Domain_Name_System) (DNS) service running on Google's infrastructure.

In addition to public DNS zones, [Cloud DNS](https://docs.cloud.google.com/dns) also provides a managed internal DNS solution for private networks on Google Cloud. [Private DNS zones](https://docs.cloud.google.com/dns/docs/overview#concepts) enable you to internally name your virtual machine (VM) instances, load balancers, or other resources. DNS queries for those private DNS zones are restricted to your private networks.

The following diagram illustrates how you can use Service Directory zones to make service names available using DNS lookups.

[ ![Using Cloud DNS with Service Directory \(click to enlarge\)](https://docs.cloud.google.com/static/service-directory/images/service-directory-05.svg)](https://docs.cloud.google.com/static/service-directory/images/service-directory-05.svg) Using Cloud DNS with Service Directory (click to enlarge)

Overview of the individual components:

  1. The endpoints are registered directly with Service Directory by using the Service Directory API. You can register both Google Cloud and non-Google Cloud services with Service Directory.
  2. Both external and internal clients can look up those services at: https://servicedirectory.googleapis.com
  3. To enable DNS requests, [create a Service Directory zone in Cloud DNS](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone) that is associated with a Service Directory namespace.
  4. Internal clients can resolve this service by using DNS, HTTP, and gRPC. External clients (clients not on the private network) must use HTTP or gRPC to resolve service names.



## Example configuration

### How to expose a service over DNS

The following diagram illustrates how a microservice architecture is modeled in Service Directory and made available using DNS. Notice that Service Directory maintains the services and endpoints entirely, but the private zone is in Cloud DNS.

[ ![Exposing a service over DNS \(click to enlarge\)](https://docs.cloud.google.com/static/service-directory/images/service-directory-06.svg)](https://docs.cloud.google.com/static/service-directory/images/service-directory-06.svg) Exposing a service over DNS (click to enlarge)

In this diagram (left side), the **payments** service is registered to a namespace with the name `backend-namespace`, the region `us-east1`, and the project `gcp-project`. The namespace is linked to the private zone `example.com`.

To do a DNS lookup, the client requests the [SRV record](https://wikipedia.org/wiki/SRV_record) for the domain name `_payments._tcp.payments.example.com`, which resolves to the port numbers and address records for the payment service's endpoints.

## What's next

  * To learn how to set up a Service Directory namespace, create a service in the namespace, and assign endpoints to a service, see [Configure Service Directory](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory).
  * To learn how to create a Service Directory zone that leverages an an existing namespace, see [Configure a Service Directory DNS zone](https://docs.cloud.google.com/service-directory/docs/configuring-service-directory-zone).
  * To learn how to make a query to an existing Service Directory zone using DNS, see [Query using DNS](https://docs.cloud.google.com/service-directory/docs/query-dns).
  * To find solutions for common issues that you might encounter when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
