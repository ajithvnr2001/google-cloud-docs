---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless/
title: Managed Service for Apache Spark network configuration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:48.529315+00:00
---

# Managed Service for Apache Spark network configuration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/network-serverless/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark network configuration Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the requirements for Managed Service for Apache Spark network configuration.

## Virtual Private Cloud subnetwork requirements

This document describes Virtual Private Cloud network requirements for Managed Service for Apache Spark batch workloads and interactive sessions.

### Private Google Access

Managed Service for Apache Spark batch workloads and interactive sessions run on VMs with internal IP addresses only and on a regional subnet with [ Private Google Access (PGA)](https://docs.cloud.google.com/vpc/docs/configure-private-google-access) enabled automatically on the subnet.

If you don't specify a subnet, Managed Service for Apache Spark selects the `default` subnet in the batch workload or session region as the subnet for a batch workload or session.

If your workload requires external network or internet access, for example, to download resources such as ML models from [PyTorch Hub](https://pytorch.org/hub/) or [Hugging Face](https://huggingface.co/), you can set up [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow outbound traffic using internal IPs on your VPC network.

### Open subnet connectivity

The VPC subnet for the region selected for the Managed Service for Apache Spark batch workload or interactive session must allow internal communication on all ports between VM instances within the subnet.

To prevent malicious scripts in one workload from affecting other workloads, Managed Service for Apache Spark deploys [default security measures](https://docs.cloud.google.com/managed-spark/docs/concepts/security).

The following Google Cloud CLI command attaches a network firewall to a subnet that allows internal ingress communications among VMs using all protocols on all ports:
    
    
    gcloud compute firewall-rules create allow-internal-ingress \
        --network=NETWORK_NAME \
        --source-ranges=SUBNET_RANGES \
        --destination-ranges=SUBNET_RANGES \
        --direction=ingress \
        --action=allow \
        --rules=all
    

Notes:

  * SUBNET_RANGES: See [Allow internal ingress connections between VMs](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-internal). The `default` VPC network in a project with the `default-allow-internal` firewall rule, which allows ingress communication on all ports (`tcp:0-65535`, `udp:0-65535`, and `icmp protocols:ports`), meets the open-subnet-connectivity requirement. However, this rule also allows ingress by any VM instance on the network.

**Use network tags to limit connectivity**. In production, the recommended practice is to limit firewall rules to the IP addresses used by your Spark workloads.



#### Automatically created [regional system firewall policy](https://docs.cloud.google.com/firewall/docs/firewall-policies-overview)

To satisfy the open subnet connectivity requirement, Managed Service for Apache Spark batch workloads and interactive sessions that use runtime version `3.0` or later automatically create a regional system firewall policy `dataproc-firewall-policy-[network-id]-region` or `dataproc-fw-[network-id]-region` on the batch or session VPC subnet. This policy contains the following ingress and egress rules.

Name | Purpose | Priority | Direction | Action | Source and Destination | Protocol and ports  
---|---|---|---|---|---|---  
`dataproc-allow-internal-ingress-rule-[subnetworkId]` |  Allows all necessary internal communication only from other tagged Managed Service for Apache Spark VMs within the same subnet.  | 4 | INGRESS | ALLOW | 
* `srcSecureTag`: secure tag value for this subnet.
* `targetSecureTags`:secure tag value for this subnet.
| tcp:0-65535, udp:0-65535, icmp protocols:ports  
`dataproc-allow-internal-egress-rule-[subnetworkId]` |  Allows Managed Service for Apache Spark VMs to download packages, for example pip and apt-get, and access Google APIs using Private Google Access.  | 5 | EGRESS | ALLOW | 
* `destIpRanges`: 0.0.0.0/0.
* `targetSecureTags`:secure tag value for this subnet.
| tcp:0-65535, udp:0-65535, icmp protocols:ports  
  
Notes:

  * Managed Service for Apache Spark provisions a [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) associated with the user project to store secure tags. Managed Service for Apache Spark creates a [secure tag](https://docs.cloud.google.com/managed-spark/docs/guides/use-secure-tags#benefits_of_using_secure_tags) for the subnet in the [tenant project](https://docs.cloud.google.com/service-infrastructure/docs/glossary#tenant) and attaches it to Managed Service for Apache Spark VMs, which ensures that the created system firewall policy only applies to Managed Service for Apache Spark VMs.

  * Automatically created system firewall policy is not supported for [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).




## Managed Service for Apache Spark and VPC-SC networks

With [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs), network administrators can define a security perimeter around resources of Google-managed services to control communication to and between those services.

Consider the following strategies when you use VPC-SC networks with Managed Service for Apache Spark:

  * [Set up private connectivity](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

  * Create a [custom container image](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers) that pre-installs dependencies outside the VPC-SC perimeter, and then [submit a Spark batch workload](https://docs.cloud.google.com/managed-spark/docs/guides/custom-containers#submit_a_spark_batch_workload_using_a_custom_container_image) that uses your custom container image.




For more information, see [VPC Service Controls— Managed Service for Apache Spark](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataproc_serverless).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
