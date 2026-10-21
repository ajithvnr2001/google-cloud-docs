---
url: https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-shared-vpc/
title: Connect to a Shared VPC network \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.256829+00:00
---

# Connect to a Shared VPC network  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-shared-vpc/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Connect to a Shared VPC network

If your organization uses [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), you can connect Cloud Run functions directly to your Shared VPC network by using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access). This allows Cloud Run functions to access resources in your Shared VPC network, such as Compute Engine VM instances, Memorystore instances, and any other resources with an internal IP address.

If your organization does not use Shared VPC, see [Connect to a VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-vpc).

## Comparison of configuration methods

For Shared VPC, Serverless VPC Access connectors can be configured in two different ways. You can either set up connectors in each service project that has Cloud Run functions resources that need access to your network, or you can set up shared connectors in the host project. There are advantages to each method.

### Service projects

Advantages of creating connectors in the service projects:

  * **Isolation:** Each connector has dedicated bandwidth and is unaffected by bandwidth use of connectors in other service projects. This is good if you have a service that experiences spikes in traffic, or if you need to ensure that each service project is unaffected by connector use of other service projects.
  * **Chargebacks:** Charges incurred by connectors are associated with the service project containing the connector. This enables easier chargebacks.
  * **Security:** Allows you to follow the "principle of least privilege." Connectors must be granted access to the resources in your Shared VPC network that they need to reach. By creating a connector in the service project, you can limit what the services in the project can access by using firewall rules.
  * **Team independence:** Reduces dependency on the host project administrator. Teams can create and manage the connectors associated with their service project. A user with the Compute Engine [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) role or a custom [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) role with the [`compute.firewalls.create`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) permission enabled for the host project must still manage firewall rules for the connector.



To set up connectors in service projects, see [Configure connectors in service projects](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-service-projects).

### Host project

Advantages of creating connectors in the host project:

  * **Centralized network management:** Aligns with the Shared VPC model of centralizing network configuration resources in the host project.
  * **IP address space:** Preserves more of your IP address space. Connectors require an IP address for each instance, so having fewer connectors (and fewer instances in each connector) uses fewer IP addresses. This is good if you are concerned about running out of IP addresses.
  * **Maintenance:** Reduces maintenance, because each connector you create may be used by multiple service projects. This is good if you are concerned about maintenance overhead.
  * **Cost for idle time:** Can reduce the amount of connector idle time and associated cost. Connectors incur costs even when they are not serving traffic (see [pricing](https://cloud.google.com/vpc/pricing#serverless-vpc-pricing)). Having fewer connectors may reduce the amount of resource you pay for when not serving traffic, depending on your connector type and number of instances. This is often cost effective if your use case involves a large number of services, and the services are used infrequently.



To set up connectors in the host project, see [Configure connectors in the host project](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
