---
url: https://docs.cloud.google.com/service-directory/docs/key-terms/
title: Key terms \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:06.415727+00:00
---

# Key terms  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/key-terms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Key terms Stay organized with collections  Save and categorize content based on your preferences. 

This page provides key terminology that applies to Service Directory. Review these terms to better understand how Service Directory works.

Endpoint
    

An endpoint is an individual IP/port pair fronting a service that can handle requests. Any given service can have zero or more endpoints. The endpoint can be a VM, container, load balancer, or other entity capable of handling the requests. An example would be a cluster of user-managed Redis servers.

    

Endpoints can have optional annotations, in the form of key:value pairs, that clients can use. For example, a Redis service might have an annotation like `replica:server`. Annotations can be used to store URLs. You can use a tool such as [jq](https://stedolan.github.io/jq/) to pull the new URL out of the response.

    

For Service Directory, an endpoint can only exist within a service and is identified with an endpoint name that is a string identifier that is unique to that service.

Service
    

A service is a collection of endpoints (IP/ports) that provide a set of behaviors. Clients look up a service by its name and then connect to the endpoints that provide that service. Services can also have optional annotations (key-value pairs) associated with them (for example, `use_https:true`).

    

A service must belong to a namespace. Each service name must be unique within that namespace.

Namespace
    

A namespace holds a set of service names along with their endpoint information. A namespace is a means of grouping services together for easier management.

    

Namespaces are regional resources and belong to a project. The name of a namespace must be unique for that project and region.

Although a namespace is a regional resource, the services that belong to that namespace can exist anywhere and be queried from anywhere. We recommend customers choose a region that maps to where their endpoints are running.

HTTP/gRPC clients
    

Service Directory supports look up of service names using HTTP/gRPC. There are no requirements that the service and client be on the same network.

    

Lookup operations over gRPC are controlled by IAM.

Service Directory zone
    

A Service Directory zone is a specific type of [Cloud DNS private zone](https://docs.cloud.google.com/dns/docs/overview#concepts) whose complete and authoritative source of information is a Service Directory namespace. It allows you to look up Service Directory data using DNS requests.

    

If a namespace is attached to a Service Directory zone, then all services in that namespace are visible to all networks that are allowed to query the zone.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
