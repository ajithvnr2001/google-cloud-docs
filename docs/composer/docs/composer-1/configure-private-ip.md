---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip/
title: Configure private IP networking \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:05.415096+00:00
---

# Configure private IP networking  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure private IP networking Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#comparison "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-private-ip "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This page provides information about configuring your Google Cloud project networking for Private IP environments.

For Private IP environments, Managed Airflow assigns only private IP ([RFC 1918](https://www.ietf.org/rfc/rfc1918.txt)) addresses to the managed Google Kubernetes Engine and Cloud SQL VMs in your environment.

As an option, you can also use [privately used public IP addresses](https://docs.cloud.google.com/composer/docs/composer-1/configure-privately-used-public-ip) and [the IP Masquerade agent](https://docs.cloud.google.com/composer/docs/composer-1/enable-ip-masquerade-agent) to save the IP address space and to use non-RFC 1918 addresses.

For information about connecting to resources in your environment, see [Private IP](https://docs.cloud.google.com/composer/docs/composer-1/private-ip-environments).

## Before you begin

  * Make sure that you have the appropriate user and service account [permissions](https://docs.cloud.google.com/composer/docs/composer-1/access-control) to create an environment.
  * Check that [Incompatible organization policies](https://docs.cloud.google.com/composer/docs/composer-1/troubleshooting-environment-creation#incompatible-org-policies) are not defined in your project.



## Check network requirements

Verify that your project's VPC network meets the following requirements:

  * Make sure that there are no private IP block conflicts. If your VPC network and its established VPC peers have overlapping IP blocks with the VPC network in the Google-managed [tenant project](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture), Managed Airflow cannot create your environment. See the default IP ranges table for the defaults used in each region.

  * Make sure that there are sufficient secondary IP ranges for the Managed Airflow GKE pods and services. GKE searches for secondary IP ranges for IP Aliasing. If GKE cannot find a range, Managed Airflow cannot create your environment.

  * Make sure that the number of secondary ranges in your subnetwork does not exceed 30. Consider the following:

    * The GKE cluster for your Private IP environment creates two secondary ranges in the subnetwork. You can create multiple subnetworks in the same region for the same VPC network.
    * The maximum number of supported secondary ranges is 30. Each Private IP environment requires two secondary ranges for the Managed Airflow GKE pods and services.
  * Make sure that your project's network can accommodate the limit [on the maximum number of connections to a single VPC network](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering). The maximum number of Private IP environments you can create depends on the number of already existing VPC peering connections in your VPC network.

  * Each Private IP environment uses at most two VPC peerings per environment. Managed Airflow creates one VPC peering for the tenant project network. The second peering is created by the GKE cluster of your environment, and [GKE clusters can reuse this connection](https://docs.cloud.google.com/vpc/docs/quota#per_network).




## Choose a network, subnetwork, and network ranges

Choose the network ranges for your Private IP environment (or use the default ones). You use these network ranges later when you create a Private IP environment.

To create a Private IP environment, you need to have the following information:

  * Your VPC network ID
  * Your VPC subnetwork ID
  * Two secondary IP ranges in your VPC subnetwork: 
    * Secondary IP range for pods
    * Secondary IP range for services
  * IP ranges for the components of the environment:

    * **GKE Control Plane IP range**. IP range for the GKE control plane. 
      * Web server IP range.
    * **Web server IP range**. IP range for the Airflow web server instance.
    * **Cloud SQL IP range**. IP range for the Cloud SQL instance.

**Caution:** The `172.17.0.0/16` range [is reserved in Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/private-ip#network_issues).



See the default IP ranges table for the defaults used in each region.

## Default IP ranges

Region | GKE control plane IP range | Web server IP range | Cloud SQL IP range  
---|---|---|---  
africa-south1 | 172.16.64.0/23 | 172.31.223.0/24 | 10.0.0.0/12  
asia-east1 | 172.16.42.0/23 | 172.31.255.0/24 | 10.0.0.0/12  
asia-east2 | 172.16.0.0/23 | 172.31.255.0/24 | 10.0.0.0/12  
asia-northeast1 | 172.16.2.0/23 | 172.31.254.0/24 | 10.0.0.0/12  
asia-northeast2 | 172.16.32.0/23 | 172.31.239.0/24 | 10.0.0.0/12  
asia-northeast3 | 172.16.30.0/23 | 172.31.240.0/24 | 10.0.0.0/12  
asia-south1 | 172.16.4.0/23 | 172.31.253.0/24 | 10.0.0.0/12  
asia-south2 | 172.16.50.0/23 | 172.31.230.0/24 | 10.0.0.0/12  
asia-southeast1 | 172.16.40.0/23 | 172.31.235.0/24 | 10.0.0.0/12  
asia-southeast2 | 172.16.44.0/23 | 172.31.233.0/24 | 10.0.0.0/12  
australia-southeast1 | 172.16.6.0/23 | 172.31.252.0/24 | 10.0.0.0/12  
australia-southeast2 | 172.16.56.0/23 | 172.31.227.0/24 | 10.0.0.0/12  
europe-central2 | 172.16.36.0/23 | 172.31.237.0/24 | 10.0.0.0/12  
europe-north1 | 172.16.48.0/23 | 172.31.231.0/24 | 10.0.0.0/12  
europe-southwest1 | 172.16.58.0/23 | 172.31.226.0/24 | 10.0.0.0/12  
europe-west1 | 172.16.8.0/23 | 172.31.251.0/24 | 10.0.0.0/12  
europe-west10 | 172.16.62.0/23 | 172.31.224.0/24 | 10.0.0.0/12  
europe-west12 | 172.16.62.0/23 | 172.31.224.0/24 | 10.0.0.0/12  
europe-west2 | 172.16.10.0/23 | 172.31.250.0/24 | 10.0.0.0/12  
europe-west3 | 172.16.12.0/23 | 172.31.249.0/24 | 10.0.0.0/12  
europe-west4 | 172.16.42.0/23 | 172.31.234.0/24 | 10.0.0.0/12  
europe-west6 | 172.16.14.0/23 | 172.31.248.0/24 | 10.0.0.0/12  
europe-west8 | 172.16.60.0/23 | 172.31.225.0/24 | 10.0.0.0/12  
europe-west9 | 172.16.46.0/23 | 172.31.232.0/24 | 10.0.0.0/12  
me-central1 | 172.16.58.0/23 | 172.31.226.0/24 | 10.0.0.0/12  
me-central2 | 172.16.64.0/23 | 172.31.223.0/24 | 10.0.0.0/12  
me-west1 | 172.16.54.0/23 | 172.31.228.0/24 | 10.0.0.0/12  
northamerica-northeast1 | 172.16.16.0/23 | 172.31.247.0/24 | 10.0.0.0/12  
northamerica-northeast2 | 172.16.46.0/23 | 172.31.232.0/24 | 10.0.0.0/12  
northamerica-south1 | 172.16.68.0/23 | 172.31.221.0/24 | 10.0.0.0/12  
southamerica-east1 | 172.16.18.0/23 | 172.31.246.0/24 | 10.0.0.0/12  
southamerica-west1 | 172.16.58.0/23 | 172.31.226.0/24 | 10.0.0.0/12  
us-central1 | 172.16.20.0/23 | 172.31.245.0/24 | 10.0.0.0/12  
us-east1 | 172.16.22.0/23 | 172.31.244.0/24 | 10.0.0.0/12  
us-east4 | 172.16.24.0/23 | 172.31.243.0/24 | 10.0.0.0/12  
us-east5 | 172.16.52.0/23 | 172.31.229.0/24 | 10.0.0.0/12  
us-south1 | 172.16.56.0/23 | 172.31.227.0/24 | 10.0.0.0/12  
us-west1 | 172.16.38.0/23 | 172.31.236.0/24 | 10.0.0.0/12  
us-west2 | 172.16.34.0/23 | 172.31.238.0/24 | 10.0.0.0/12  
us-west3 | 172.16.26.0/23 | 172.31.242.0/24 | 10.0.0.0/12  
us-west4 | 172.16.28.0/23 | 172.31.241.0/24 | 10.0.0.0/12  
  
## (Optional) Configure connectivity to Google APIs and services

As an option, you might want to route all traffic to Google APIs and services through several IP addresses that belong to the `private.googleapis.com` domain. In this configuration, your environment accesses Google APIs and services through IP addresses only routable from within Google Cloud.

If your Private IP environment also uses VPC Service Controls, use [instructions for environments with VPC Service Controls](https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc#connectivity-restricted) instead.

Managed Airflow environments use the following domains:

  * `*.googleapis.com` is used to access other Google services.

  * `*.pkg.dev` is used to get environment images, such as when creating or updating an environment.

  * `*.gcr.io` GKE requires connectivity to Container Registry domain regardless of Managed Airflow version.


**Note:** If you do not configure DNS rules for Google APIs and services, they are resolved using the [domain option](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) for default domains.

Configure connectivity to the `private.googleapis.com` endpoint:

Domain | DNS name | CNAME Record | A Record  
---|---|---|---  
`*.googleapis.com` | `googleapis.com.` |  DNS Name: `*.googleapis.com.`  
Resource record type: `CNAME`  
Canonical name: `googleapis.com.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`  
`*.pkg.dev` | `pkg.dev.` |  DNS Name: `*.pkg.dev.`  
Resource record type: `CNAME`  
Canonical name: `pkg.dev.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`  
`*.gcr.io` | `gcr.io.` |  DNS Name: `*.gcr.io.`  
Resource record type: `CNAME`  
Canonical name: `gcr.io.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`  
  
To create a DNS rule:

  1. [Create a new DNS zone](https://docs.cloud.google.com/dns/docs/zones) and use **DNS name** as DNS name of this zone.

Example: `pkg.dev.`

  2. [Add a record set](https://docs.cloud.google.com/dns/docs/records) for **CNAME Record**.

Example:

     * DNS Name: `*.pkg.dev.`
     * Resource record type: `CNAME`
     * Canonical name: `pkg.dev.`
  3. [Add a record set](https://docs.cloud.google.com/dns/docs/records) with for **A Record** :

Example:

     * Resource record type: `A`
     * IPv4 addresses: `199.36.153.8`, `199.36.153.9`, `199.36.153.10`, `199.36.153.11`



For more information, see [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## (Optional) Configure firewall rules

Perform this step only if your project has non-default firewall rules, such as rules that override [implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules), or modify [pre-populated rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) in the default network.

For example, Managed Airflow might fail to create an environment if you have a firewall rule that denies all egress traffic. To avoid issues, define selective `allow` rules that follow the list and have higher priority than the global `deny` rule.

**Important:** Depending on how firewall rules are configured in your project, the following list of rules might be redundant. For example, if your firewall rules block only ingress, then you do not need the listed egress rules.

Configure your VPC network to allow traffic from your environment:

  * See [Using firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to learn how to check, add and update rules for your VPC network.
  * Use [Connectivity Tool](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) to validate the connectivity between IP ranges.
  * You can use [networking tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to further limit access. You can set these tags when you create an environment.

Description | Direction | Action | Source or Destination | Protocols | Ports  
---|---|---|---|---|---  
DNS | Egress | Allow | Any destination (`0.0.0.0/0`), or DNS server IP addresses | TCP, UDP | 53  
Google APIs and services | Egress | Allow | IP address range of the domain you chose for Google APIs and services. See [IP addresses for default domains](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#ip-addr-defaults) if you use defaults. | TCP | 443  
Environment's cluster Nodes | Egress | Allow | Environment's subnetwork primary IP address range | TCP, UDP | all  
Environment's cluster Pods | Egress | Allow | Secondary IP address range for Pods in the environment's subnetwork | TCP, UDP | all  
Environment's cluster Control Plane | Egress | Allow | GKE Control Plane IP range | TCP, UDP | all  
Web server | Egress | Allow | Web server network IP range | TCP | 3306, 3307  
**Caution:** GKE service automatically creates a number of ingress and egress firewall rules so that your environment's cluster functions correctly (such as ingress and egress rules for Google Cloud Health Checks). See [GKE Firewall Rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules) page for more information and don't delete or block firewall rules created by GKE services. You might see that your environment communicates with the `34.126.0.0/18` IP range, which is an IP range of Private Google Access. This traffic belongs to GKE service used by the environment's cluster.

To obtain environment cluster's IP ranges:

  * Pod, Service, and Control Plane address ranges are available on the **Clusters** page of your environment's cluster:

    1. In Google Cloud console, go to the **Environments** page.

[Go to Environments](https://console.cloud.google.com/composer/environments)

    2. In the list of environments, click the name of your environment. The **Environment details** page opens.

    3. Go to the **Environment configuration** tab.

    4. Follow the **view cluster details** link.

  * You can see environment's web server IP range on the **Environment configuration** tab.

  * You can see environment's network ID on the **Environment configuration** tab. To get IP ranges for a subnetwork, go to **VPC Networks** page and click on the network's name to see details:

[Go to VPC Networks](https://console.cloud.google.com/networking/networks/list)




## VPC-native cluster configuration

Managed Airflow supports VPC-native GKE clusters in your environment.

During [environment creation](https://docs.cloud.google.com/composer/docs/composer-1/create-environments), you can enable VPC Native (using alias IP) and configure networking, such as IP allocation, _without enabling private IP_.

Because a VPC native cluster is required for Airflow tasks to communicate with other VMs that are reachable through private IPs, you must also enable VPC Native to configure a private IP environment.

## Configure proxy server variables

**Important:** Routing with proxy variables is done on a best-effort basis. **There's no guarantee that every request goes through the proxy**. Instead, we recommend to route traffic by creating your environment [in a VPC network](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip) and configuring traffic routing rules in this network.

You can set `http_proxy` and `https_proxy` [environment variables](https://docs.cloud.google.com/composer/docs/composer-1/set-environment-variables) in your environment. These standard Linux variables are used by web clients that run in containers of your environment's cluster to route traffic through the specified proxies.

The `NO_PROXY` variable by default is set to a list of Google domains, the IP address of the environment's cluster Compute Engine metadata server, and `localhost` so that they are excluded from proxying:
    
    
    .google.com,.googleapis.com,metadata.google.internal,169.254.169.254,localhost
    

This configuration makes it possible to create an environment with set `http_proxy` and `https_proxy` environment variables in cases when the proxy isn't configured to handle traffic to Google services.

## What's next

  * [Connect an environment to a VPC network](https://docs.cloud.google.com/composer/docs/composer-3/connect-vpc-network)
  * [Configure internet access when installing PyPI packages][cc-packages-internet-access]



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
