---
url: https://docs.cloud.google.com/vpc/docs/apis/
title: APIs and reference \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:31.060608+00:00
---

# APIs and reference  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# APIs and reference

This page describes Google Cloud CLI commands and APIs that can be used with Virtual Private Cloud (VPC) networks.

Most networking gcloud CLI commands and APIs are part of Compute Engine. However, some services on this page use gcloud CLI commands or APIs that are not part of Compute Engine— for example, Serverless VPC Access and policy-based routes.

## gcloud CLI and API references

Use the following resources and their methods when working with VPC networks.

  * **Addresses** : Use to create internal and external IP address resources, assign those address resources to Google Cloud resources, and modify address resources.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/addresses)

  * **Firewall rules** : Use to create and modify firewall rules in your Google Cloud VPC network. Firewall rules enable you to allow or deny traffic to or from virtual machine (VM) instances based on IP addresses, protocol, and ports.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls)

  * **Forwarding rules** : Use to create and modify forwarding rules in your VPC network. Forwarding rules tell the network where to send matching packets that enter or pass through the network.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)

  * **Networks** : Use to create, modify, and peer VPC networks.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks)

  * **Private Service Connect** : Use to access managed services and offer managed services to service consumers. 
    * Resources for service consumers: Use to access managed services privately from inside your VPC network.
      * Endpoints: Use to access managed services. Endpoints are deployed by using forwarding rules.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/forwarding-rules), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/forwardingRules)

      * Backends: Use to connect to supported managed services by using a load balancer. Backends use Cloud Load Balancing resources. For more information, see Cloud Load Balancing [API and gcloud references](https://docs.cloud.google.com/load-balancing/docs/apis).
      * Network attachments: Use to let service producer VPC networks initiate connections to consumer networks.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-attachments), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkAttachments)

      * Service connection policies: Use to automate deployment and connectivity for eligible managed service instances.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/service-connection-policies), [API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.serviceConnectionPolicies)

    * Resources for service producers: Use to host managed services in their own separate VPC networks and offer a private connection to their consumers. 
      * Service attachments: Use to publish services.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/service-attachments), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments)

      * Interfaces: Use to let service producer VPC networks initiate connections to consumer VPC networks.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances)

  * **Routes** : Use to create and modify VPC network routes. 
    * Static routes: Use to manually configure instructions to the VPC network for how to forward traffic that is leaving VM instances.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routes), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routes)

    * Policy-based routes: Use to forward traffic based on policies you create. Policy-based routes have higher priority than static routes.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/policy-based-routes), [API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.global.policyBasedRoutes)

  * **Shared VPC** : Use to share a VPC network with other projects and control that sharing. In the API, modify these settings by using the `projects` resource.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/shared-vpc), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/projects)

  * **Subnets** : Use to create, modify, and delete subnets in a VPC network.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks)

  * **Serverless VPC Access** : Use to create, modify, and delete Serverless VPC Access connectors.

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/beta/compute/networks/vpc-access), [API](https://docs.cloud.google.com/vpc/docs/reference/vpcaccess/rest)

  * **VPC Flow Logs** : Use to monitor VPC networks and understand your network usage.

    * Manage VPC Flow Logs configurations for subnets:

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets), [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks)

    * Manage VPC Flow Logs configurations for VLAN attachments for Cloud Interconnect and Cloud VPN tunnels:

[gcloud](https://docs.cloud.google.com/sdk/gcloud/reference/network-management/vpc-flow-logs-configs), [API](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/rest/v1/projects.locations.vpcFlowLogsConfigs)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
