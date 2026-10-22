---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern/
title: Handover patterns \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:19.632307+00:00
---

# Handover patterns  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/handover-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Handover patterns Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

With the _handover_ pattern, the architecture is based on using Google Cloud-provided storage services to connect a private computing environment to projects in Google Cloud. This pattern applies primarily to setups that follow the [_analytics hybrid multicloud_ architecture pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns#analytics-hybrid-multicloud-patterns), where:

  * Workloads that are running in a private computing environment or in another cloud upload data to shared storage locations. Depending on use cases, uploads might happen in bulk or in smaller increments.
  * Google Cloud-hosted workloads or other Google services (data analytics and artificial intelligence services, for example) consume data from the shared storage locations and process it in a streaming or batch fashion.



## Architecture

The following diagram shows a reference architecture for the handover pattern.

![Data flows from an on-premises environment to a VPC-hosted workload and a data analytics service hosted in a Google Cloud environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-secure-networking-patterns/handover.svg)

The preceding architecture diagram shows the following workflows:

  * On the Google Cloud side, you deploy workloads into an application VPC. These workloads can include data processing, analytics, and analytics-related frontend applications.
  * To securely expose frontend applications to users, you can use Cloud Load Balancing or API Gateway.
  * A set of Cloud Storage buckets or Pub/Sub queues uploads data from the private computing environment and makes it available for further processing by workloads deployed in Google Cloud. Using Identity and Access Management (IAM) policies, you can restrict access to trusted workloads.
  * Use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) to restrict access to services and to minimize unwarranted data exfiltration risks from Google Cloud services.
  * In this architecture, communication with Cloud Storage buckets, or Pub/Sub, is conducted over public networks, or through private connectivity using VPN, Cloud Interconnect, or Cross-Cloud Interconnect. Typically, the decision on how to connect depends on several aspects, such as the following: 
    * Expected traffic volume
    * Whether it's a temporary or permanent setup
    * Security and compliance requirements



## Variation

The design options outlined in the [_gated ingress_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-ingress), which uses Private Service Connect endpoints for Google APIs, can also be applied to this pattern. Specifically, it provides access to Cloud Storage, BigQuery, and other Google Service APIs. This approach requires private IP addressing over a hybrid and multicloud network connection such as VPN, Cloud Interconnect and Cross-Cloud Interconnect.

## Best practices

  * Lock down access to Cloud Storage buckets and Pub/Sub topics.
  * When applicable, use cloud-first, integrated data movement solutions like the Google Cloud [suite of solutions](https://cloud.google.com/data-movement). To meet your use case needs, these solutions are designed to efficiently move, integrate, and transform data.
  * Assess the different factors that influence the data transfer options, such as cost, expected transfer time, and security. For more information, see [Evaluating your transfer options](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets#step_3_evaluating_your_transfer_options).

  * To minimize latency and prevent high-volume data transfer and movement over the public internet, consider using Cloud Interconnect or Cross-Cloud Interconnect, including accessing Private Service Connect endpoints within your Virtual Private Cloud for Google APIs.

  * To protect Google Cloud services in your projects and to mitigate the risk of data exfiltration, use VPC Service Controls. These service controls can specify service perimeters at the project or VPC network level.

    * You can [extend service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/overview#hybrid_access) to a hybrid environment over an authorized VPN or Cloud Interconnect. For more information about the benefits of service perimeters, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).
  * Communicate with publicly published data analytics workloads that are hosted on VM instances through an API gateway, a load balancer, or a virtual network appliance. Use one of these communication methods for added security and to avoid making these instances directly reachable from the internet.

  * If internet access is required, [Cloud NAT](https://docs.cloud.google.com/nat/docs) can be used in the same VPC to handle outbound traffic from the instances to the public internet.

  * Review the [general best practices](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices) for hybrid and multicloud networking topologies.




[ Previous arrow_back  Gated egress and gated ingress  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress-ingress)

[ Next General best practices  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/general-best-practices)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
