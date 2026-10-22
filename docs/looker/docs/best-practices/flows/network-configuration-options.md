---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/network-configuration-options/
title: Understanding the Right Network Configuration for Looker (Google Cloud core) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:38.485416+00:00
---

# Understanding the Right Network Configuration for Looker (Google Cloud core)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/network-configuration-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Understanding the Right Network Configuration for Looker (Google Cloud core) Stay organized with collections  Save and categorize content based on your preferences. 

When configuring Looker (Google Cloud core), it's essential to select the appropriate [network configuration](https://docs.cloud.google.com/looker/docs/looker-core-networking-options) to ensure seamless integration and optimal performance. This page provides a guide to help you choose between public secure connections and the various private connections configurations.

## Considerations for network configuration

Before choosing a network configuration, identify the systems Looker (Google Cloud core) will be configured to connect to:

  * **Data Sources** : What data sources will Looker (Google Cloud core) connect to (e.g., BigQuery, Cloud SQL, on-premises databases)?
  * **Git Repository** : Where is the Git repository hosted (e.g., public GitHub, private GitHub Enterprise hosted on Google Cloud)?
  * **Team Expertise** : Does your team have networking expertise?



### Foundational information

Consider the following when choosing your network configuration:

  * **Connections to BigQuery** : All connections to BigQuery use Google's private network, across all network configuration options.
  * **SSO Configuration** : If a third-party identity provider is configured for SSO, communication is from the user's browser to the identity provider and then redirected to the Looker (Google Cloud core) instance. This will work for all options as long as the redirect URL is accessible to your users.
  * **Instance Creation** : The network configuration must be chosen at the time of instance creation. It cannot be changed later, except when adding Public IP connectivity to a private services access or Private Service Connect Private IP-only instance, or removing Public IP connectivity from a private services access or Private Service Connect hybrid connections instance, after creation.
  * **Feature Availability** : Out-of-box feature availability varies by network option. Refer to [Looker (Google Cloud core) feature differences](https://cloud.google.com/looker/docs/looker-core-feature-differences#feature_compatibility_by_network_connection_type) for more details.



## Network configuration options

The following diagram can help you decide which network configuration option is right for you. The diagram uses the acronyms PSC to refer to Private Service Connect and PSA to refer to private services access.

### Public IP Only

  * **Explanation** : Instance has a public URL and traffic is over the public internet. This is the simplest setup and requires no advanced network configuration. If you require a custom URL, such as `looker.mycompany.com`, you can [set up a custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain).



### Private Service Connect - Private IP Only - Recommended

  * **Why choose Private Service Connect?** : Private Service Connect is Google's recommended, service-oriented approach for connecting to resources in a private network. It avoids the complexities of network-wide VPC peering, IP range conflicts, and transitive peering limitations. It uses service-oriented connections rather than network-wide peering and is designed to support all new and advanced Looker (Google Cloud core) features.
  * **Explanation** : With Private Service Connect, Looker (Google Cloud core) connects to your resources through Private Service Connect endpoints, and you connect to your Looker (Google Cloud core) instance through its exposed Private Service Connect endpoint.
  * **Limitations** : Your instance is only accessible using its Private Service Connect endpoint; it does not have a public IP address. Each distinct data source in your VPC may require a separate endpoint configuration.
  * **Requirements** : If connecting to resources on the public internet (such as github.com), you can use [controlled native egress](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#controlled-native-egress) or configure a [southbound Private Service Connect connection](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound) using an Internet NEG. For Private Service Connect to function, ensure that the Private Service Connect connection status in the Looker (Google Cloud core) instance details page is **Accepted**.
  * **Learn more** : 
    * [Private Service Connect overview](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview)
    * [Private inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access)
    * [Looker (Google Cloud core) outbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-create-southbound)



### Private Service Connect - Public and Private IP - Recommended

  * **Why choose Private Service Connect?** : Private Service Connect is Google's recommended, service-oriented approach for connecting to resources in a private network. It avoids the complexities of network-wide VPC peering, IP range conflicts, and transitive peering limitations. It uses service-oriented connections rather than network-wide peering and is designed to support all new and advanced Looker (Google Cloud core) features. This option provides a public URL for access from the internet, like the Public IP Only option, but routes outgoing traffic from Looker (Google Cloud core) to your data sources or Git repository through your VPC using Private Service Connect connections.
  * **Explanation** : Your instance has a public URL for access from the internet, but all _outgoing_ traffic from Looker (Google Cloud core) to your data sources or Git repository is routed through Private Service Connect connections to your VPC.
  * **Limitations** : Each distinct data source in your VPC may require a separate endpoint configuration.
  * **Requirements** : If connecting to resources on the public internet that are not in your VPC (such as github.com), you can use Controlled Native Egress or configure a southbound Private Service Connect connection using an Internet NEG. For Private Service Connect to function, ensure that the Private Service Connect connection status in the Looker (Google Cloud core) instance details page is **Accepted**.
  * **Learn more** : 
    * [Private Service Connect overview](https://docs.cloud.google.com/looker/docs/looker-core-psc-overview)
    * [Private inbound access to a Looker (Google Cloud core) instance using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-access)
    * [Looker (Google Cloud core) outbound access to external services using Private Service Connect](https://docs.cloud.google.com/looker/docs/looker-core-psc-southbound)



### Private services access - Private IP Only - Legacy

  * **Why choose private services access?** : Private services access is an older method that relies on VPC Network Peering. It may be suitable if you have an existing VPC peering setup, but it is prone to scaling issues, IP range exhaustion, and lacks support for transitive peering. For more information about private services access, see [Create a private connections (private services access) Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip).
  * **Explanation** : Your instance is only accessible from within your VPC or other peered networks using its private IP address; it does not have a public URL. This option requires custom domain configuration for a user-friendly URL. All traffic is routed through your VPC.
  * **Limitations** : Requires a `/22` IP range for setup. Certain [BI connectors](https://docs.cloud.google.com/looker/docs/looker-core-networking-options#how_to_choose_a_networking_option) may not be available. Requires networking expertise for setup. **Transitive peering is not supported** ; if your data source is in a network that is peered with your VPC (as in a hub-and-spoke model), Looker (Google Cloud core) won't be able to reach it using private services access. If you are using a [Shared VPC](https://docs.cloud.google.com/looker/docs/looker-core-create-private-ip#shared-vpc), consult your Network Administrator to discuss the `/22` IP range allocation and peering implications within the host project.
  * **Requirements** : If connecting to a public Git repository (e.g., github.com), requires additional infrastructure such as a Proxy VM or Cloud NAT.



### Private services access - Public and Private IP - Legacy

  * **Why choose private services access?** : Private services access is an older method that relies on VPC Network Peering. It may be suitable if you have an existing VPC peering setup, but it is prone to scaling issues, IP range exhaustion, and lacks support for transitive peering. For more information about private services access, see [Create a private connection with Private Service Access for Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-psa).
  * **Explanation** : Your instance has a public URL for access from the internet, but all _outgoing_ traffic from Looker (Google Cloud core) to your data sources or Git repository is routed through your VPC using VPC Network Peering.
  * **Limitations** : Requires a `/22` IP range for setup. Requires networking expertise for setup. **Transitive peering is not supported** ; if your data source is in a network that is peered with your VPC (as in a hub-and-spoke model), Looker (Google Cloud core) won't be able to reach it using private services access. If you are using a Shared VPC, consult your Network Administrator to discuss the `/22` IP range allocation and peering implications within the host project.



## What's next

  * Read an overview of [Looker (Google Cloud core) networking options](https://docs.cloud.google.com/looker/docs/looker-core-networking-options).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
