---
url: https://docs.cloud.google.com/datastream/docs/network-connectivity-options/
title: Network connectivity methods \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:21.641812+00:00
---

# Network connectivity methods  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/network-connectivity-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Network connectivity methods Stay organized with collections  Save and categorize content based on your preferences. 

To use Datastream to create a stream from the source database to the destination, you must establish connectivity to the source database. Use the information in the following table to help you decide which method works best for you for your specific workload.

Network connectivity method | Description | Things to consider  
---|---|---  
[IP allowlist](https://docs.cloud.google.com/datastream/docs/ip-allowlists) | Works by configuring the source database server to allow incoming connections from Datastream's external IP addresses. To find out the IP addresses for your regions, see [IP allowlists and regions](https://docs.cloud.google.com/datastream/docs/ip-allowlists-and-regions). | 

  * The source database is exposed to a public IP address.
  * The connection isn't encrypted by default. SSL must be enabled on the source database to encrypt the connection.
  * Configuring the firewall may require assistance from the IT department.

  
[Forward SSH tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel) |  Establish an encrypted connection over public networks between Datastream and the source, through a forward-SSH tunnel. | 

  * Limited bandwidth
  * You must set up and maintain the bastion host.

  
[Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces) |  Works by [creating a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration). Datastream uses this configuration to communicate with the data source over a private network. This communication happens through a network attachment set up in the customer VPC network.  | 

  * Requires setting up a network attachment and adjusting firewall rules.
  * You can't migrate existing private connectivity configurations to Private Service Connect interfaces.
  * You can't change the network attachment after you create your Private Service Connect interface connection.
  * Allowlisting incoming connections from the Datastream IP addresses is available only on a project ID basis.

  
[VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering) |  Works by [creating a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration). Datastream uses this configuration to communicate with the data source over a private network. This communication happens through a Virtual Private Cloud (VPC) peering connection.  | 

  * Requires a private network connection (VPN, Interconnect, etc.) between the database and Google Cloud.

  
  
## What's next

  * Learn more about [IP allowlists](https://docs.cloud.google.com/datastream/docs/ip-allowlists).
  * Learn more about [Forward SSH tunnel](https://docs.cloud.google.com/datastream/docs/ssh-tunnel).
  * Learn more about [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces).
  * Learn more about [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
