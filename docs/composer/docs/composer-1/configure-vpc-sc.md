---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc/
title: Configure VPC Service Controls \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:38.176553+00:00
---

# Configure VPC Service Controls  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-vpc-sc/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

[Managed Airflow (Gen 3)](https://docs.cloud.google.com/composer/docs/composer-3/configure-vpc-sc "View this page for Managed Airflow \(Gen 3\)") | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-vpc-sc "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

[VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) enable organizations to define a perimeter around Google Cloud resources to mitigate data exfiltration risks.

Managed Airflow environments can be deployed within a service perimeter. By configuring your environment with VPC Service Controls, you can keep sensitive data private while taking advantage of the fully-managed workflow orchestration capabilities of Managed Airflow.

VPC Service Controls support for Managed Airflow means that:

  * Managed Airflow can now be selected as a secured service inside a VPC Service Controls perimeter.
  * All underlying resources used by Managed Airflow are configured to support VPC Service Controls architecture and follow its rules.



Deploying Managed Airflow environments with VPC Service Controls gives you:

  * Reduced risk of data exfiltration.
  * Protection against data exposure due to misconfigured access controls.
  * Reduced risk of malicious users copying data to unauthorized Google Cloud resources, or external attackers accessing Google Cloud resources from the internet.



## About VPC Service Controls in Managed Airflow

  * All VPC Service Controls network constraints also apply to your Managed Airflow environments. See the [VPC Service Controls documentation](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for details.


  * Displaying a rendered template with functions in the web UI with DAG serialization enabled is supported for environments running Managed Airflow version 1.12.0 or later and Airflow version 1.10.9 or later.

  * Setting the `async_dagbag_loader` flag to `True` is not supported while DAG serialization is enabled.

  * Enabling DAG serialization disables all Airflow web server plugins, as they could risk the security of the VPC network where Managed Airflow is deployed. This doesn't impact the behaviour of scheduler or worker plugins, including Airflow operators and sensors.



  * If a Managed Airflow environment is protected by a perimeter, access to public PyPI repositories is restricted. See the Install PyPI packages in VPC Service Controls for more information.

  * If your environment uses [Private IP networking](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type), **all internal traffic is routed to your VPC network** , except the traffic to Google APIs, services, and domains that [are available to Private IP environments](https://docs.cloud.google.com/composer/docs/composer-3/change-networking-type#about-networking-type) through Private Google Access.

  * Depending on how you configure your VPC network, a Private IP environment **can gain access to the internet through you VPC network**.

  * In VPC Service Controls mode, Managed Airflow runs two instances of the Airflow web server. Identity-Aware Proxy load balances user traffic between these instances. Airflow web servers run in "read-only" mode, which means:

    * [DAG Serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization) is enabled. As a result, Airflow web server does not parse DAG files.

    * Plugins are not synced to the web server, so you cannot modify or extend the web server's capabilities with plugins.

    * The Airflow web server uses a container image that is pre-built by the Managed Airflow service. If you install PyPI images in your environment, these images are not installed on the web server container image.

**Caution:** In Managed Airflow (Legacy Gen 1), the web server endpoint is accessible from outside the perimeter regardless of the access level configuration. We recommend to protect access to the Airflow web server by [restricting access to web server to specific IP ranges](https://docs.cloud.google.com/composer/docs/composer-1/access-airflow-web-interface#network-access-controls).



## Perimeters for environments with Shared VPC and CMEK

If your environment is protected by a service perimeter and uses [Shared VPC](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc), [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/composer/docs/composer-1/configure-cmek-encryption), or both, then make sure that the following projects are located in the **same service perimeter** :

  * Service project: The project that contains the Managed Airflow environment.
  * Host project: The project that contains the Shared VPC network.
  * Project that hosts the Cloud Key Management Service keys.

**Important:** Perimeter misalignment between these projects can block critical database management operations and cause environment creation or update failures.

## Create environments in a perimeter

The following steps are required to deploy Managed Airflow inside a perimeter:

  1. Enable **Access Context Manager API** and **Cloud Composer API** for your project. See [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis) for reference.

  2. Make sure that your service perimeter has the following VPC accessible services, otherwise your environment might fail to create:

     * Cloud Composer API (composer.googleapis.com)
     * Compute Engine API (compute.googleapis.com)
     * Kubernetes Engine API (container.googleapis.com)
     * Container Registry API (containerregistry.googleapis.com)
     * Artifact Registry API (artifactregistry.googleapis.com)
     * Cloud Storage API (storage.googleapis.com)
     * Cloud SQL Admin API (sqladmin.googleapis.com)
     * Cloud Logging API (logging.googleapis.com)
     * Cloud Monitoring API (monitoring.googleapis.com)
     * Cloud Pub/Sub API (pubsub.googleapis.com)
     * Cloud Cloud Resource Manager API (cloudresourcemanager.googleapis.com)
     * Service Directory API (servicedirectory.googleapis.com)
     * Cloud Key Management Service API (cloudkms.googleapis.com), if you are using Cloud KMS or CMEK keys.
     * Secret Manager API (secretmanager.googleapis.com), if you are using Secret Manager as a secret backend.
**Warning:** In all versions of Managed Airflow (Legacy Gen 1), if you include Cloud Identity-Aware Proxy API (iap.googleapis.com) or Identity-Aware Proxy TCP API (iaptunnel.googleapis.com) in your perimeter, then **Managed Airflow environments cannot be created**. To address this issue, see [Environment creation fails in projects with VPC Service Controls enabled](https://docs.cloud.google.com/composer/docs/composer-1/known-issues#vpc-issue).
  3. Create a new Managed Airflow environment with [Private IP](https://docs.cloud.google.com/composer/docs/composer-1/configure-private-ip) enabled. Note that **this setting must be configured during the environment creation**.

     * Use version [composer-1.10.4](https://docs.cloud.google.com/composer/docs/composer-versions) or later.

     * Make sure that [DAGs serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization) is enabled. If your environment uses Managed Airflow version 1.15.0 and later, the serialization is enabled by default.

     * When creating your environment, remember to configure access to the Airflow web server. To improve protection, only allow access to the web server from specific IP ranges. For details, see [Configure web server network access](https://docs.cloud.google.com/composer/docs/composer-1/create-environments#web-server-access).




## Add an existing environment to the perimeter

  * You already created or configured the perimeter as described in the previous section.
  * Your environment uses Private IP.
  * Your environments have [DAG serialization](https://docs.cloud.google.com/composer/docs/composer-1/dag-serialization) enabled.



## Install PyPI packages in VPC Service Controls

In the default VPC Service Controls configuration, Managed Airflow only supports installing PyPI packages from private repositories that are reachable from the internal IP address space of the VPC network.

### Install from a private repository

The recommended configuration is to set up a private PyPI repository:

  1. Populate it with vetted packages used by your organization, then configure Managed Airflow to [install Python dependencies from a private repository](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-private-repo).

  2. Grant additional permissions for installing packages from private repositories repositories to the service account of your environment, as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control#custom-service-account).




### Install from a public repository

**Caution:** When using this setup, make sure that you understand the **risks of using external repositories**. Be sure that you trust the content and integrity of any external repositories, because these connections can potentially be used as an exfiltration vector.

###  Remote repository 

This is the recommended approach to installing packages from a public repository.

To install PyPI packages from repositories outside the private IP space, follow these steps:

  1. Create an [Artifact Registry remote repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo).
  2. Grant this repository [access to upstream sources](https://docs.cloud.google.com/artifact-registry/docs/repositories/remote-repo#vpc).
  3. Configure Airflow to [install packages from an Artifact Registry repository](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-ar-repo).
  4. Grant additional permissions for installing packages from Artifact Registry repositories to the service account of your environment, as described in [Access control](https://docs.cloud.google.com/composer/docs/composer-1/access-control#custom-service-account).



###  External connections 

To install PyPI packages from repositories outside the private IP space, follow these steps:

  1. Configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to allow Managed Airflow running in the private IP space to connect with external PyPI repositories.

  2. Configure your [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) to allow outbound connections from the Composer cluster to the repository.




## Configure connectivity to Google APIs and services

In a VPC Service Controls configuration, to control network traffic, configure access to Google APIs and services through the `restricted.googleapis.com`. This domain blocks access to Google APIs and services that do not support VPC Service Controls.

Managed Airflow environments use the following domains:

  * `*.googleapis.com` is used to access other Google services.

  * `*.pkg.dev` is used to get environment images, such as when creating or updating an environment.

  * `*.gcr.io` GKE requires connectivity to Container Registry domain regardless of Managed Airflow version.


**Note:** If you do not configure DNS rules for Google APIs and services, they are resolved using the [domain option](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#domain-options) for default domains.

Configure connectivity to the `restricted.googleapis.com` endpoint:

Domain | DNS name | CNAME Record | A Record  
---|---|---|---  
`*.googleapis.com` | `googleapis.com.` |  DNS Name: `*.googleapis.com.`  
Resource record type: `CNAME`  
Canonical name: `googleapis.com.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`  
`*.pkg.dev` | `pkg.dev.` |  DNS Name: `*.pkg.dev.`  
Resource record type: `CNAME`  
Canonical name: `pkg.dev.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`  
`*.gcr.io` | `gcr.io.` |  DNS Name: `*.gcr.io.`  
Resource record type: `CNAME`  
Canonical name: `gcr.io.`  
|  Resource record type: `A`  
IPv4 addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`  
  
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
     * IPv4 addresses: `199.36.153.4`, `199.36.153.5`, `199.36.153.6`, `199.36.153.7`



For more information, see [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity).

## Configure firewall rules

If your project has non-default firewall rules, such as rules that override [implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules), or modify [pre-populated rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) in the default network, then verify that the following firewall rules are configured.

For example, Managed Airflow might fail to create an environment if you have a firewall rule that denies all egress traffic. To avoid issues, define selective `allow` rules that follow the list and have higher priority than the global `deny` rule.

**Important:** Depending on how firewall rules are configured in your project, the following list of rules might be redundant. For example, if your firewall rules block only ingress, then you do not need the listed egress rules.

Configure your VPC network to allow traffic from your environment:

  * See [Using firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to learn how to check, add and update rules for your VPC network.
  * Use [Connectivity Tool](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests) to validate the connectivity between IP ranges.
  * You can use [networking tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) to further limit access. You can set these tags when you create an environment.

Description | Direction | Action | Source or Destination | Protocols | Ports  
---|---|---|---|---|---  
DNS  
  
Configure as described in [VPC Service Controls support for Cloud DNS](https://docs.cloud.google.com/dns/docs/vpc-sc-support) | - | - | - | - | -  
Google APIs and services | Egress | Allow | IPv4 addresses of `restricted.googleapis.com` that you use for Google APIs and services. | TCP | 443  
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




## VPC Service Controls logs

When troubleshooting environment creation issues, you can analyze audit logs generated by VPC Service Controls.

In addition to other log messages, you can check logs for information about `cloud-airflow-prod@system.gserviceaccount.com` and `service-PROJECT_ID@cloudcomposer-accounts.iam.gserviceaccount.com` service accounts that configure components of your environments.

Managed Airflow service uses the `cloud-airflow-prod@system.gserviceaccount.com` service account to manage [tenant project components](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture#about-customer-tenant) of your environments.

The `service-PROJECT_ID@cloudcomposer-accounts.iam.gserviceaccount.com` service account, also known as Composer Service Agent Service Account manages environment components in [service and host projects](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc#shared-vpc-guidelines).

## What's next

  * [Create environments](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)
  * [Install PyPI packages](https://docs.cloud.google.com/composer/docs/composer-1/install-python-dependencies#install-private-repo)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
