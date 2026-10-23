---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup/
title: Set up a Private Service Connect interface for Gemini Enterprise Agent Platform resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:44:50.015149+00:00
---

# Set up a Private Service Connect interface for Gemini Enterprise Agent Platform resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Set up a Private Service Connect interface for Gemini Enterprise Agent Platform resources Stay organized with collections  Save and categorize content based on your preferences. 

This guide shows how to set up a [Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) for Gemini Enterprise Agent Platform resources.

You can configure Private Service Connect interface connections for certain resources in Gemini Enterprise Agent Platform, including:

  * [Ray on Vertex AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray/create-cluster#enable-psc-i)
  * [Custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/psc-i-egress)
  * [Gemini Enterprise Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-private-service-connect)
  * [Agent Runtime](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#psc-i)



Unlike [VPC peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-peering) connections, Private Service Connect interface connections are transitive. This requires fewer IP addresses in the consumer VPC network. This allows greater flexibility in connecting to other VPC networks in your Google Cloud project and on-premises.

This guide is for network administrators familiar with Google Cloud networking concepts.

## Objectives

This guide covers the following tasks:

  * Configure a consumer VPC  network, subnet, and network attachment.
  * Add firewall rules to your Google Cloud network host project.
  * Create an Agent Platform resource specifying the network attachment to use a Private Service Connect interface.



## Before you begin

Use the following instructions to create or select a Google Cloud project and configure it for use with Gemini Enterprise Agent Platform and Private Service Connect.

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Gemini Enterprise Agent Platform, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com)

  5. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  6. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  7. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  8. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install beta

  9. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  10. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  11. Enable the Gemini Enterprise Agent Platform, Compute Engine, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com)

  12. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  13. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  14. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  15. After initializing the gcloud CLI, update it and install the required components: 
         
         gcloud components update
         gcloud components install beta

  16. If you're not the project owner and don't have the [Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)](https://docs.cloud.google.com/resource-manager/docs/access-control-proj#resourcemanager.projectIamAdmin) role, ask the owner to grant you the [Compute Network Admin (`roles/compute.networkAdmin`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) role to manage networking resources. If you're only creating a network attachment in an existing VPC network, you can instead use a custom role that includes the `compute.networkAttachments.create` permission. 
  17. Assign the required roles to the [AI Platform Service Agent](https://docs.cloud.google.com/iam/docs/service-agents#ai-platform-service-agent). For details about which roles to grant in different scenarios, see the Gemini Enterprise Agent Platform service agent required role section of this document. 



## Set up a VPC network and subnet

**Note:** If you already have an existing VPC network, ensure the subnet IPv4 range is in the [valid RFC 1918 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges), and then go to the Create a network attachment section.

Follow the configuration steps to create a new VPC network if you don't have an existing network.

  1. [Create a VPC network:](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#gcloud_1)
         
         gcloud compute networks create NETWORK \
             --subnet-mode=custom
         

Replace NETWORK with a name for the VPC network.

  2. [Create a subnet:](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets)
         
         gcloud compute networks subnets create SUBNET_NAME \
             --network=NETWORK \
             --range=PRIMARY_RANGE \
             --region=REGION
         

Replace the following:

     * SUBNET_NAME: a name for the subnet.
     * PRIMARY_RANGE: the primary IPv4 range for the new subnet, in CIDR notation.

The following are the IP requirements and limitations for Agent Platform:

       * Agent Platform recommends a `/28` subnetwork.
       * The subnet of the network attachment supports RFC 1918 and non RFC 1918 addresses with the exception of subnets 100.64.0.0/20 and 240.0.0.0/4.
       * Agent Platform can only connect to RFC 1918 IP address ranges that are routable from the specified network.
       * Agent Platform can't reach a privately used public IP address or these non-RFC 1918 ranges:

         * `100.64.0.0/20`
         * `192.0.0.0/24`
         * `192.0.2.0/24`
         * `198.18.0.0/15`
         * `198.51.100.0/24`
         * `203.0.113.0/24`
         * `240.0.0.0/4`

For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).

     * REGION: the Google Cloud region where you create the new subnet.




## Create a network attachment

In a Shared VPC deployment, create the subnet used for the Network Attachment in the Host Project, then create the Private Service Connect Network Attachment in the Service Project.

The following example shows how to [Create a network attachment](https://docs.cloud.google.com/vpc/docs/create-manage-network-attachments) that automatically accepts connections.
    
    
       gcloud compute network-attachments create NETWORK_ATTACHMENT_NAME \
           --region=REGION \
           --connection-preference=ACCEPT_AUTOMATIC \
           --subnets=SUBNET_NAME
    

Replace NETWORK_ATTACHMENT_NAME with a name for the network attachment.

If the network attachment is created in a project different from the Service Project, you need to pass the full network attachment path when calling the Gemini Enterprise.

## Gemini Enterprise Agent Platform service agent required role

The [Gemini Enterprise Agent Platform service agent](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/access-control#service-agents) (AI Platform Service Agent) requires specific IAM roles to manage networking resources and facilitate Private Service Connect (Private Service Connect) interface connections.

Depending on your network configuration, grant the following roles to the service agent (`service-PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`):

  1. **Compute Network Admin (`roles/compute.networkAdmin`)**

In the project where you create the network attachment, you must grant the `roles/compute.networkAdmin` role to the service agent. If you don't want to grant the `roles/compute.networkAdmin` role, you can create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles) with the following permissions and grant it to the service agent:

     * `compute.networkAttachments.get`
     * `compute.networkAttachments.update`
     * `compute.regionOperations.get`
  2. **Compute Network User (`roles/compute.networkUser`)**

If you are using a [Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#setting_up) and you create the network attachment in a service project, grant the service agent (located in the service project) the `roles/compute.networkUser` role on the VPC host project.

  3. **DNS Peer (`roles/dns.peer`)**

To enable resources like Agent Platform Managed Training or Agent Runtime to resolve private DNS records, grant the `roles/dns.peer` role to the service agent. Grant this role in the project where you are using the services. If using a Shared VPC, you must also grant the `roles/dns.peer` role to the service agent in the VPC host project.




## Configure firewall rules

The system applies [Ingress firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) in the consumer VPC to enable communication with the Private Service Connect interface network attachment subnet from compute and on-premises endpoints.

Configuring firewall rules is optional. However, we recommend that you set common firewall rules as shown in the following examples.

  1. Create a firewall rule that allows SSH access on TCP port 22:
         
         gcloud compute firewall-rules create NETWORK-firewall1 \
             --network NETWORK \
             --allow tcp:22
         

  2. Create a firewall rule that allows HTTPS traffic on TCP port 443:
         
         gcloud compute firewall-rules create NETWORK-firewall2 \
             --network NETWORK \
             --allow tcp:443
         

  3. Create a firewall rule that allows ICMP traffic (such as ping requests):
         
         gcloud compute firewall-rules create NETWORK-firewall3 \
             --network NETWORK \
             --allow icmp
         




## Set up a private DNS peering

To enable Agent Platform Managed Training jobs or Agent Runtime agents configured with Private Service Connect interfaces to resolve private DNS records in customer-managed Cloud DNS zones, you can specify your network attachment and create private DNS peering while configuring or deploying your resource.

You can configure DNS peering by specifying target networks and domain suffixes in the `dns_peering_configs` field under `psc_interface_config`:

  * **`dns_peering_configs`** : A list of DNS peering configurations: 
    * **`domain`** : The DNS name of the private Cloud DNS zone.
    * **`target_project`** : The project that hosts the VPC network. It can be different from the project where you created the network attachment.
    * **`target_network`** : The VPC network name in the target project to which the DNS peering is established.



For example, when creating a resource in Python, you can configure the private DNS peering as follows:
    
    
    psc_interface_config = {
        "network_attachment": "NETWORK_ATTACHMENT",
        "dns_peering_configs": [
            {
                "domain": "DOMAIN_SUFFIX",
                "target_project": "TARGET_PROJECT",
                "target_network": "TARGET_NETWORK",
            },
        ],
    }
    

Replace the following:

  * NETWORK_ATTACHMENT: the name or full path of your network attachment. For example, `projects/SERVICE_PROJECT/regions/REGION/networkAttachments/NETWORK_ATTACHMENT_NAME`. If you create the network attachment in a project different from the service project where you use Agent Platform, you must pass the full path of the network attachment.
  * DOMAIN_SUFFIX: the DNS name of the private Cloud DNS zone (for example, `example.com.`).
  * TARGET_PROJECT: the project that hosts the VPC network. It can be different from the project where you created the network attachment.
  * TARGET_NETWORK: the VPC network name in the target project to which the DNS peering is established.



## Troubleshooting

This section covers some common issues for configuring Private Service Connect with Gemini Enterprise Agent Platform.

When configuring Agent Platform with a Shared VPC, create the network attachment in the service project where you use Agent Platform. This approach helps prevent certain error messages, such as:
    
    
    _Please make sure that the Agent Platform API is enabled for the
    project_, by ensuring the
    necessary permissions and APIs are enabled in the correct project.
    

## What's next

  * Learn how to use Private Service Connect interface egress for [Ray on Vertex AI](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/open-source/ray/create-cluster).
  * Learn how to use Private Service Connect interface egress for [custom training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/psc-i-egress).
  * Learn how to use Private Service Connect interface egress for [Agent Platform Pipelines](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/pipelines/configure-private-service-connect).
  * Learn how to use Private Service Connect interface egress for [Agent Runtime](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/deploy#psc-i)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
