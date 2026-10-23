---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/provisioning-overview/
title: Partner Cross-Cloud Interconnect for AWS provisioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:25.152875+00:00
---

# Partner Cross-Cloud Interconnect for AWS provisioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/provisioning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Partner Cross-Cloud Interconnect for AWS provisioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and provision a partner Cross-Cloud Interconnect for Amazon Web Services (AWS) connection.

You can initiate connectivity from either Google Cloud or Amazon Web Services. To achieve a successful connection, you must create the `transport` resource. After a resource is created and connectivity is established, the flow is identical regardless of where the provisioning is initiated. You can manage the resource from either side to enable, disable, or change the bandwidth of the resource.

Before you start the partner Cross-Cloud Interconnect for AWS provisioning process, ensure that the following conditions are met:

  * You already have an AWS account.
  * If you're using VPC Network Peering to connect, you [create a Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks), if it doesn't already exist, to connect your transport to.
  * If you're using Network Connectivity Center (NCC) to connect, you [create a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub) to connect your transport resource to.



If you have VPC Service Controls enabled, contact [Google Cloud support](https://cloud.google.com/support).

## Connect with NCC

This section describes the steps to connect if you are connecting using NCC.

You can enable [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) by using the `--psc-routing-enabled` flag when you create the `transport` resource.

### Initiate NCC connection from Google Cloud if you don't have an activation key

If you don't have an activation key from AWS, you can initiate and provision a partner Cross-Cloud Interconnect for AWS connection from Google Cloud. To do so, follow these steps.

  1. [Choose a paired location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/paired-locations).

Google Cloud regions are paired with specific AWS regions. When you choose a specific Google Cloud region to create your resources in, you must choose the corresponding AWS region.

  2. [List the available profiles in the region](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#list-available-profiles).

  3. Select the correct profile and [create the transport resource](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#initiate-connection-gcp-to-aws).

  4. Use the generated activation key to [create the connection in your AWS account](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#complete-aws-api).

  5. [Create an NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub) to connect your `transport` resource to.

  6. [Create the `transport` resource](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#create-transport-gcp-to-aws).

  7. [Complete the steps on the AWS API](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#complete-aws-api).

  8. [Verify the connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-gcp-to-aws#verify-connection).




### Initiate NCC connection from AWS if you have an activation key

If you already have an activation key from AWS, you can initiate and provision a partner Cross-Cloud Interconnect for AWS connection from AWS. To do so, follow these steps.

  1. Activate your key by using the AWS Console.

  2. [Create an NCC hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-hub) to connect your `transport` resource to.

  3. [Create the `transport` resource](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-aws-to-gcp#create-transport-aws-to-gcp-with-ncc).

  4. Follow instructions to [create a connection from the AWS Console](https://docs.aws.amazon.com/interconnect/latest/userguide/getting-started.html#create-first-interconnect). You must provide the project and region where you want the connection to land in Google Cloud. For a list of paired locations, see [Choose a paired location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/paired-locations).

  5. After the resource is created on the AWS side, [create the Google Cloud resource with the provided activation key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-aws-to-gcp#create-transport-aws-to-gcp-with-ncc).

  6. [Verify the connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-ncc-connectivity-aws-to-gcp#verify-connection).




## Connect with VPC Network Peering

This section describes the steps to connect if you are connecting using VPC Network Peering.

Connecting with VPC Network Peering doesn't let you access Google APIs through Private Service Connect.

### Initiate connection from Google Cloud if you don't have an activation key

If you don't have an activation key from AWS, you can initiate and provision a partner Cross-Cloud Interconnect for AWS connection from Google Cloud. To do so, follow these steps.

  1. [Choose a paired location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/paired-locations).

Google Cloud regions are paired with specific AWS regions. When you choose a specific Google Cloud region to create your resources in, you must choose the corresponding AWS region.

  2. [List the available profiles in the region](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#list-available-profiles).

  3. Select the correct profile and [create the transport resource](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#create-transport-resource).

  4. Use the generated activation key to [create the connection in your AWS account](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#complete-aws-api).

  5. [Establish VPC Network Peering](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#establish-vpc-peering).

  6. [Verify the connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#verify-connection) by listing the peered VPC networks and route tables.




### Initiate a connection from AWS if you have an activation key

If you already have an activation key from AWS, you can initiate and provision a partner Cross-Cloud Interconnect for AWS connection from AWS. To do so, follow these steps.

  1. Activate your key by using the AWS Console.

  2. Follow instructions to [create a connection from the AWS Console](https://docs.aws.amazon.com/interconnect/latest/userguide/getting-started.html#create-first-interconnect). You must provide the project and region where you want the connection to land in Google Cloud. For a list of paired locations, see [Choose a paired location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/paired-locations).

  3. After the resource is created on the AWS side, create the Google Cloud resource with the provided activation key.

  4. [Peer your VPC network to the transport's peering VPC network](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-aws/create-vpc-peering-gcp-to-aws#establish-vpc-peering).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
