---
url: https://docs.cloud.google.com/service-directory/docs/private-network-access-overview/
title: Private network access overview \u00a0|\u00a0 Service Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:01.891205+00:00
---

# Private network access overview  |  Service Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-directory/docs/private-network-access-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Service Directory ](https://docs.cloud.google.com/service-directory/docs)
  * [ Guides ](https://docs.cloud.google.com/service-directory/docs/overview)



Send feedback 

#  Private network access overview Stay organized with collections  Save and categorize content based on your preferences. 

Private network access enables supported Google Cloud products to send HTTP requests to a customer Virtual Private Cloud (VPC) network resource. The requests are sent over the private network while enforcing [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs/overview) and [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

The network resources supported as destinations are:

  * Virtual machine (VM) instances
  * Internal passthrough Network Load Balancers
  * Regional internal Application Load Balancers
  * On-premises IP addresses, reached through Cloud Interconnect or Cloud VPN



With [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect), you can create private endpoints within your VPC network by using internal IP addresses. Private network access extends the capability and helps Google Cloud services connect directly to VPC networks.

Private network access offers the following features:

  * Provides a unified way of managing customer network, security, and access policies applied to all network paths.
  * Enables Google Cloud products to reach one or more HTTP(S) endpoints in customer private networks through the private network of Google rather than the internet. It also provides a VPC Service Controls-compliant option. The communication helps in providing better security, managing network security policies, and protecting against exfiltration while using Google Cloud features such as [HTTP Push](https://wikipedia.org/wiki/HTTP/2_Server_Push).



The following diagram shows how Dialogflow connects to a Google Cloud VM through the internet without private network access. Note that Dialogflow runs within Google Cloud.

[ ![Dialogflow connectivity without private network access](https://docs.cloud.google.com/static/service-directory/images/without_pna.svg)](https://docs.cloud.google.com/static/service-directory/images/without_pna.svg) Dialogflow connectivity without private network access (click to enlarge)

The following diagram shows how Dialogflow connects to a Google Cloud VM through the private network with private network access.

[ ![Dialogflow connectivity with private network access](https://docs.cloud.google.com/static/service-directory/images/with_pna.svg)](https://docs.cloud.google.com/static/service-directory/images/with_pna.svg) Dialogflow connectivity with private network access (click to enlarge)

For detailed information about VPC Service Controls, see the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs).

For information about how to configure private network access, see [Configuring private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access).

For information about how you can use Service Directory private network access with Dialogflow, see [Using Service Directory for private network access](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#sd).

## Quotas and limits

The following quotas and limits apply for private network access:

  * [Service Directory limits](https://docs.cloud.google.com/service-directory/quotas#limits) apply when you use private network access.
  * Calls from Google Cloud services that use private network access don't count against your quotas.
  * [Service Directory pricing](https://cloud.google.com/service-directory/pricing) applies for calls from Google Cloud services that use private network access. Because Service Directory charges are per API call against the Service Directory service, each private network access is charged as one API call.



## What's next

  * To learn about Service Directory, see [Service Directory overview](https://docs.cloud.google.com/service-directory/docs/overview).
  * To learn how to configure private network access, see [Configure private network access](https://docs.cloud.google.com/service-directory/docs/configuring-private-network-access).
  * To find solutions for common problems that you might experience when using Service Directory, see [Troubleshooting](https://docs.cloud.google.com/service-directory/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
