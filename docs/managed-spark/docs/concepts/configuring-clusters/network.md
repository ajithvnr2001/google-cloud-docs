---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network/
title: Managed Service for Apache Spark cluster network configuration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:44.628021+00:00
---

# Managed Service for Apache Spark cluster network configuration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Managed Service for Apache Spark cluster network configuration Stay organized with collections  Save and categorize content based on your preferences. 

Description: Understand Dataproc cluster network configuration. Implement VPC routes, firewall rules, Private Google Access, and Shared VPC for secure, internal-IP-only deployments.

This page explains Managed Service for Apache Spark cluster network configuration requirements and options.

## Managed Service for Apache Spark connectivity requirements

Your Managed Service for Apache Spark cluster must be in a Virtual Private Cloud network that meets route and firewall requirements to securely access Google APIs and other resources.

### Route requirements

To establish communication between the Managed Service for Apache Spark agent running on cluster VMs and the Dataproc control API, the cluster VPC network must have a route to the internet gateway. This is also required for internal-ip-only clusters.

By default, Managed Service for Apache Spark 2.2 and later image version clusters provision VMs with internal-IP-only addresses. Managed Service for Apache Spark automatically enables Private Google Access (PGA) on the cluster subnet to allow cluster VMs with internal IP addresses to reach Google APIs and services using a [system-generated default route](https://docs.cloud.google.com/vpc/docs/routes#routingpacketsinternet) to the default internet gateway.

Rule | Type | Destination IP range | Priority | Scope limits | Next hop  
---|---|---|---|---|---  
`default-route-[id]` | Static | `0.0.0.0/0` | `1000` | - | Default internet gateway  
  
PGA ensures that cluster traffic does not traverse the public internet and does not leave Google data centers (see the [PGA example diagram](https://docs.cloud.google.com/vpc/docs/private-google-access#example)).

**Note:** Despite being called _default internet gateway_ , packets sent from VMs in your VPC network to Google APIs and services remain within Google's network. See [Routing options](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-routing) for further information on how packets are sent to Google APIs and services using the default internet gateway.

Deleting the default route to the internet gateway is not recommended; If you want to control network access to the internet, use firewall rules or policies instead.

If you have deleted the default route to the internet gateway, you must [add a default route](https://docs.cloud.google.com/vpc/docs/using-routes#add-default-route-ipv4). The destination IP range has to be `0.0.0.0/0` as the IP ranges for the Dataproc control API are not static.

### Firewall requirements

The VPC network of your Managed Service for Apache Spark cluster must explicitly allow the following traffic:

  * Traffic initiated from Managed Service for Apache Spark cluster VMs to the Dataproc control API and other Managed Service for Apache Spark cluster VMs. This traffic is allowed by default from the egress [allow-all implied rule](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules) of the VPC network. If you have added overriding egress deny firewall rules, create an egress allow firewall rule.

  * Response traffic from Dataproc control API to the Managed Service for Apache Spark cluster VMs is allowed by default, due to the statefulness of the VPC network firewall.

  * Traffic received by Managed Service for Apache Spark cluster VMs from other Managed Service for Apache Spark cluster VMs. This traffic will be denied by default from the ingress deny all implied firewall rule of the VPC network. You must create an ingress allow firewall rule.




**Best practices:**

  * Use [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags) for your Managed Service for Apache Spark cluster VMs so that you can restrict the applicability of the required firewall rules to Managed Service for Apache Spark cluster VMs only. If you don't use network tags, you can specify targets by the service account used for the cluster VMs. Otherwise, you can configure firewall rules to apply to all VMs in the VPC network.
  * For more secure network access and connectivity, [use secure tags](https://docs.cloud.google.com/managed-spark/docs/guides/use-secure-tags) instead of network tags to define firewall rule sources and targets.



**Create an ingress allow firewall rule**

If you or your network or security administrator [create an ingress firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to apply to a Managed Service for Apache Spark cluster VPC network, it must have the following characteristics:

  * The [sources](https://docs.cloud.google.com/vpc/docs/firewalls#sources_for_the_rule) parameter specifies the sources for packets. All Managed Service for Apache Spark cluster VMs must be able to communicate with each other. You can identify the VMs in the cluster by IP address range (the primary range of the Managed Service for Apache Spark cluster subnet), network tags, or service accounts associated with the VMs.

**Don't omit a source parameter specification.** If you omit specifying source IP ranges, source tags, or source service accounts, the firewall rule will use the IP address range `0.0.0.0/0` (any IP address) as the source. If your Managed Service for Apache Spark VMs have external IP addresses, this means they can accept traffic from **anywhere** on the internet. Therefore, **define the source to be as narrow as possible** to meet your needs and secure your cluster.
  * The [targets](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) for the rule must identify the cluster VMs. The targets can be all VMs in the VPC network, or you can identify VMs by target network tag, or target service account.

  * The rule must include the following [protocols and ports](https://docs.cloud.google.com/vpc/docs/firewalls#protocols_and_ports):

    * TCP (all ports, 0 through 65535)
    * UDP (all ports, 0 through 65535)
    * ICMP

Managed Service for Apache Spark uses services that run on multiple ports. Specifying all ports helps the services run successfully.

  * The [priority](https://docs.cloud.google.com/firewall/docs/firewalls#priority_order_for_firewall_rules) of the rule must be higher than the priority of any ingress deny firewall rules that apply to the same sources and targets.




**Create an egress allow firewall rule**

If you or your network or security administrator [create an egress firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to apply to a Managed Service for Apache Spark cluster VPC network, it must have the following characteristics:

  * The [destinations](https://docs.cloud.google.com/firewall/docs/firewalls#destinations_for_the_rule) parameter specifies the destinations for packets. All Managed Service for Apache Spark cluster VMs must be able to initiate traffic to each other and the Dataproc control API. Because the IP addresses of the control API are not static, the destination must be specified by IP range `0.0.0.0/0`.

  * The [targets](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment) for the rule must identify the cluster VMs. The targets can be all VMs in the VPC network, or you can identify VMs by target network tag, or target service account.

  * The rule must include the following [protocols and ports](https://docs.cloud.google.com/vpc/docs/firewalls#protocols_and_ports):

    * TCP (all ports, 0 through 65535)
    * UDP (all ports, 0 through 65535)
    * ICMP

Managed Service for Apache Spark uses services that run on multiple ports. Specifying all ports helps the services run successfully.

  * The [priority](https://docs.cloud.google.com/firewall/docs/firewalls#priority_order_for_firewall_rules) of the rule must be higher than the priority of any egress deny firewall rules that apply to the same destinations and targets.




**Diagnose VPC network firewall rules**

To audit packets not processed by higher priority firewall rules, you can create the following two low priority (65534) deny firewall rules. Unlike the implied firewall rules, you can enable [firewall rules logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging) on each of these low priority rules:

  1. An ingress deny rule (sources `0.0.0.0/0`, all protocols, all targets in the VPC network)

  2. An egress deny rule (destinations `0.0.0.0/0`, all protocols, all targets in the VPC network)



  * With these low priority rules and firewall rules logging, you can log packets not processed by higher priority, and potentially more specific, firewall rules. These two low priority rules also align with security best practices by implementing a "final drop packets" strategy.

  * Examine the firewall rules logs for these rules to determine if you want to create or amend higher priority rules to permit packets. For example, if packets sent between Managed Service for Apache Spark cluster VMs are dropped, this can be a signal that your firewall rules must be adjusted.




## Create a VPC network

Instead of using the `default` VPC network, you can create your own [auto mode](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network) or [custom](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) VPC network. When you create the cluster, you associate your network with the cluster.

**Assured Workloads environment:** When you use an [Assured Workloads environment](https://docs.cloud.google.com/assured-workloads/docs/deploy-resource) for regulatory compliance, the cluster, its VPC network, and its Cloud Storage buckets must be contained within the Assured Workloads environment.

## Create a cluster that uses your VPC network

### Google Cloud console

To configure the network:

  1. Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Network configuration**.
  4. In the panel that opens, select your network and subnetwork. The **Internal IP only** checkbox is enabled by default.



### gcloud CLI

Use [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) with the `‑‑network` or `‑‑subnet` flag to create a cluster on a subnet in your network. If you use the ‑‑network flag, the cluster will use a subnetwork with the same name as the specified network in the region where the cluster is created.

`--network example`. Since auto networks are created with subnets in each region, with each subnet given the network name, you can pass the auto mode VPC network name to the `‑‑network` flag. The cluster will use the auto mode VPC subnetwork in the region specified with the ‑‑region flag.
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --network NETWORK_NAME \
        --region=REGION \
        ... other args ...
    

`--subnet example`. You can use the `‑‑subnet` flag to create a cluster that uses an auto mode or custom VPC network subnet in the cluster region. Specify the full resource path of the subnet.
    
    
    gcloud dataproc clusters create CLUSTER_NAMEW \
        --subnet projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
        --region=REGION \
        ... other args ...
    

**Let the Google Cloud console construct your cluster create request.** : You can click the **Equivalent Command Line → Equivalent REST** links on the [**Create a cluster**](https://console.cloud.google.com/dataproc/clusters/create) page in the Google Cloud console to have the Google Cloud console construct an equivalent gcloud CLI or API REST request.

### REST API

You can specify either the [networkUri or subnetworkUri](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig) `GceClusterConfig` field as part of a [clusters.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request.

**Example**
    
    
    POST /v1/projects/my-project-id/regions/us-central1/clusters/
    {
      "projectId": "PROJECT_ID",
      "clusterName": CLUSTER_NAME,
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          **"subnetworkUri":** SUBNET_NAME,
        },
        ...
    

**Let the Google Cloud console construct your cluster create request.** : You can click the **Equivalent Command Line → Equivalent REST** links at the bottom of the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page in the Google Cloud console to have the Google Cloud console construct an equivalent gcloud CLI or API REST request.

### Create a cluster that uses a VPC network in another project

A Managed Service for Apache Spark cluster can use a [Shared VPC network](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is defined in a **host project**. The project where the Managed Service for Apache Spark cluster is created is referred to as the **service project**.

  1. Find the Managed Service for Apache Spark cluster project number:

     1. Open the **IAM & Admin** [Settings](https://console.cloud.google.com/iam-admin/settings/project) page in the Google Cloud console. Select the project where you will create the Managed Service for Apache Spark cluster. Copy the project ID.
  2. A principal with the [Shared VPC Admin role](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#permissions) must perform the following steps. See [directions for setting up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc) for background information.

     1. Make sure that the Shared VPC host project [is enabled](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host).

     2. [Attach the project with the Managed Service for Apache Spark cluster](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared) to the host project.

     3. Configure the [Managed Service for Apache Spark service agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) (`service-[project-number]@dataproc-accounts.iam.gserviceaccount.com`) to have the [Network User](https://docs.cloud.google.com/compute/docs/access/iam#network_user_role) role for the host project:

        1. Open the [**IAM & Admin**](https://console.cloud.google.com/iam-admin/iam/) page in the Google Cloud console.

        2. Use the project selector to select the new host project.

        3. Click **Grant Access**.

        4. Fill in the Grant Access form:

           1. **Add principals** : Input the service account.

           2. **Assign roles** : Insert "Compute Network" In the filter box, then select the **Compute Network User** role.

           3. Click **Save**.

**Note:** In clusters created with Managed Service for Apache Spark image versions prior to 2.0.58, 2.1.4, or 2.2.1 (released in 2023), you must also assign the Compute Network User role to the [Google APIs Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent) (`PROJECT_NUMBER@cloudservices.gserviceaccount.com`).
  3. After the service account has the `Network User` role for the host project, [create a cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create_a_cluster_that_uses_your_network) that uses the Shared VPC network.




### Create a cluster that uses a VPC subnetwork in another project

**Note:** The previous section explained how your Managed Service for Apache Spark cluster can use another project's VPC **network**. To set permissions at a more granular level, this section shows you how your Managed Service for Apache Spark cluster can use another project's VPC **subnetwork**.

A Managed Service for Apache Spark cluster can use a [Shared VPC subnetwork](https://docs.cloud.google.com/vpc/docs/shared-vpc) that is defined in a **host project**. The project where the Managed Service for Apache Spark cluster is created is referred to as the **service project**.

  1. Find the Managed Service for Apache Spark cluster project number:

     1. Open the **IAM & Admin** [Settings](https://console.cloud.google.com/iam-admin/settings/project) page in the Google Cloud console. Select the project where you will create the Managed Service for Apache Spark cluster. Copy the project ID.
  2. A principal with the [Shared VPC Admin role](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#permissions) must perform the following steps. See [directions for setting up Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up_shared_vpc) for background information.

     1. Make sure that the Shared VPC host project [is enabled](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#enable-shared-vpc-host).

     2. [Attach the project with the Managed Service for Apache Spark cluster](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared) to the host project.

     3. Configure the [Managed Service for Apache Spark service agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) (`service-[project-number]@dataproc-accounts.iam.gserviceaccount.com`) to have the [Network User](https://docs.cloud.google.com/compute/docs/access/iam#network_user_role) role for the host project:

        1. Open the [VPC networks](https://console.cloud.google.com/networking/networks/list) page in the Google Cloud console.

        2. Use the project selector to select the host project.

        3. Click the network that contains the subnetwork that your Managed Service for Apache Spark cluster will use.

        4. In the **VPC Network Details** page, click the checkbox next to the name of the subnetwork that your cluster will use.

        5. If the Info Panel is not open, click **Show Info Panel**.

        6. Perform the following steps for each service account:

           1. In the Info Panel, click **Add Principal**.

           2. FIll in the Grant Access form:

              1. **Add principals** : Input the service account.

              2. **Assign roles** : Insert "Compute Network" In the filter box, then select the **Compute Network User** role. **Recommendation:** Also grant the **Compute Network Viewer** role to each service account. This role includes the `compute.subnetworks.list` permission, which allows Managed Service for Apache Spark to validate the existence of necessary service account permissions and to provide meaningful messages if needed permissions are missing.

              3. Click **Save**.

**Note:** In clusters created with Managed Service for Apache Spark image versions prior to 2.0.58, 2.1.4, or 2.2.1 (released in 2023), you must also assign the Compute Network User role to the [Google APIs Service Agent service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#google_apis_service_agent) (`PROJECT_NUMBER@cloudservices.gserviceaccount.com`).
  3. After the service account has the `Network User` role for the host project, [create a cluster](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/network#create_a_cluster_that_uses_your_network) that uses the Shared VPC subnetwork.




## Create an internal-IP-only cluster

This section applies to pre-`2.2` image version clusters. Cluster VMs with internal-IP-only addresses is enabled by default when creating Managed Service for Apache Spark clusters with [2.2 and later image versions](https://docs.cloud.google.com/managed-spark/docs/concepts/versioning/dataproc-version-clusters#supported-dataproc-image-versions).

You can use the Google Cloud console, gcloud CLI, or Dataproc API to create a cluster with internal IP addresses only. Note that Managed Service for Apache Spark automatically enables [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) on the cluster's regional subnet when internal-IP-only is enabled to allow connections to Google APIs and services.

### Google Cloud console

To configure internal IP addresses only:

  1. Open the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Click **Additional configuration** to expand that section.
  3. Edit **Network configuration**.
  4. In the panel that opens, select your network and subnetwork. Select the **Internal IP only** checkbox.



### gcloud CLI

You can create a cluster with internal IP addresses only by using the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) command with the `‑‑no-address` flag. 
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --no-address \
        --network NETWORK_NAME \
        --region=REGION \
        ... other args ...
    

Since auto networks are created with subnets in each region with the same name as the auto network, you can pass the auto network name to the `‑‑network flag` to create a cluster that will use the auto subnetwork in the cluster's region.

Alternatively, you can use the `‑‑subnet` flag to create a cluster that will use an auto or custom subnetwork in the region where the cluster will be created. Pass the `‑‑subnet` flag the full resource path of the subnet.
    
    
    gcloud dataproc clusters create cluster-name \
        --no-address \
        --subnet projects/project-id/regions/region/subnetworks/subnetwork-name \
        --region=region \
        ... other args ...
    

**Let the Google Cloud console construct your cluster create request.** : You can click the **Equivalent Command Line → Equivalent REST** links on the [**Create a cluster**](https://console.cloud.google.com/dataproc/clusters/create) page in the Google Cloud console to have the Google Cloud console construct an equivalent gcloud CLI or API REST request.

### REST API

You can use the [`GceClusterConfig.internalIpOnly`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#GceClusterConfig.FIELDS.internal_ip_only) field as part of a [`clusters.create`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) request to create a cluster enable internal IP addresses only.

**Example:**
    
    
    POST /v1/projects/my-project-id/regions/us-central1/clusters/
    {
      "projectId": "my-project-id",
      "clusterName": "example-cluster",
      "config": {
        "configBucket": "",
        "gceClusterConfig": {
          "subnetworkUri": "custom-subnet-1",
          "zoneUri": "us-central1-b",
          **"internalIpOnly": true**
        },
        ...
    

**Let the Google Cloud console construct your cluster create request** : At the bottom of the [Create cluster](https://console.cloud.google.com/dataproc/clusters/create) page, click **Equivalent command line** or **Equivalent REST** to have the Google Cloud console construct an equivalent gcloud CLI command or API REST request.

### Download dependencies with internal-ip-only clusters

By default, internal-ip-only clusters don't have access to the internet. Therefore, jobs that download dependencies from the internet, such as jobs that download Spark dependency packages from Maven Central, will fail. There are several workarounds to avoid the problem:

  1. Use [Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) to enable cluster access to the internet.

  2. Create a [custom image](https://docs.cloud.google.com/managed-spark/docs/guides/images) that includes the dependencies (for example, Spark dependency packages in `/usr/lib/spark/jars/`).

  3. Upload the dependencies to a Cloud Storage bucket, then use an [initialization action](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/init-actions) to download the dependencies from the bucket during cluster creation.




## Managed Service for Apache Spark and VPC Service Controls networks

With [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs), administrators can define a security perimeter around resources of Google-managed services to control communication to and between those services.

Note the following limitations and strategies when using VPC Service Controls networks with Managed Service for Apache Spark clusters:

  * To install components outside the VPC Service Controls perimeter, create a Managed Service for Apache Spark [custom image](https://docs.cloud.google.com/managed-spark/docs/guides/images) that pre-installs the components, then create the cluster using the custom image.

  * See [Managed Service for Apache Spark special steps to protect using VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_dataproc).




## What's next

  * To troubleshoot issues with the creation of your Managed Service for Apache Spark cluster, see [Troubleshoot cluster creation issues](https://docs.cloud.google.com/managed-spark/docs/support/troubleshoot-cluster-creation).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
