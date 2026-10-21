---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/private-access-from-agent-runtime/
title: Access Apigee privately from Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:57:00.230430+00:00
---

# Access Apigee privately from Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/private-access-from-agent-runtime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Access Apigee privately from Gemini Enterprise Agent Platform Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document describes how to configure private connectivity from an agent deployed on [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform) Agent Runtime to APIs and Model Context Protocol (MCP) tools published on Apigee, using [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect). With this pattern, traffic from the agent to Apigee stays entirely private and does not traverse the public internet. 

**Pricing information:** For information on how Private Service Connect is metered and billed, see [Private Service Connect](https://cloud.google.com/vpc/pricing#psc-forwarding-rules) on the Virtual Private Cloud pricing page. For Agent Platform pricing, see [Agent Platform pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing). 

## Overview

Agent Runtime deploys your agent in a secure, Google-managed network without access to your Virtual Private Cloud (VPC) network. Apigee similarly runs in a secure, Google-managed network. When you want an agent's calls to a Large Language Model (LLM) or to MCP tools exposed through Apigee to travel privately, you need a way to bridge these two Google-managed networks through a VPC network that you control. 

This document describes the following pattern for that bridge: 

  * Agent Runtime provisions a [Private Service Connect interface (PSC interface)](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface) that connects to a [network attachment](https://cloud.google.com/vpc/docs/about-network-attachments) in a subnet of your consumer VPC. Outbound traffic from your agent egresses into that VPC. 
  * In the same consumer VPC, you create a [Private Service Connect endpoint](https://cloud.google.com/vpc/docs/private-service-connect#endpoints) that targets the [service attachment](https://cloud.google.com/vpc/docs/private-service-connect#service-attachments) that your Apigee instance exposes. 
  * You create a [Cloud DNS private zone](https://cloud.google.com/dns/docs/zones) in the consumer VPC that resolves the Apigee environment group hostname to the Private Service Connect endpoint IP address. 
  * Agent Runtime uses [DNS peering](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup#set-up-private-dns-peering) to resolve that hostname from within the Agent Runtime environment by using the private zone in your consumer VPC. 



With this configuration, when your agent calls `https://APIGEE_HOSTNAME/...`, the request resolves to the Private Service Connect endpoint IP in your VPC, forwards through the service attachment to your Apigee instance, and is processed by the API proxy that matches the request path. 

**Note:** The pattern described in this document uses a Private Service Connect endpoint directly. TLS is terminated at the Apigee instance ingress, which presents a self-signed certificate to clients that connect over the Private Service Connect endpoint. If your client requires a publicly trusted certificate on the private path, use an internal Application Load Balancer with a [Private Service Connect network endpoint group (NEG)](https://cloud.google.com/load-balancing/docs/negs/pscneg-concepts) in front of the service attachment; see [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc) for that pattern. 

## Before you begin

This document uses the following placeholders in commands. Replace them with values from your environment. 

  * APIGEE_PROJECT_ID: the Google Cloud project ID that contains your Apigee organization.
  * SERVICE_PROJECT_ID: the Google Cloud project ID where you deploy your agent on Agent Runtime. This can be the same as APIGEE_PROJECT_ID or a different project, depending on how you organize your Google Cloud resources.
  * SERVICE_PROJECT_NUMBER: the numeric project number for SERVICE_PROJECT_ID. You can retrieve it with `gcloud projects describe SERVICE_PROJECT_ID --format="value(projectNumber)"`.
  * HOST_PROJECT_ID: the Google Cloud project ID that contains the consumer VPC network, subnet, and Cloud DNS private zone. This is the same as SERVICE_PROJECT_ID unless you are using [Shared VPC](https://cloud.google.com/vpc/docs/shared-vpc), in which case this is the host project that the service project attaches to.
  * REGION: the region of your Apigee instance (for example, `us-west1`).
  * VPC_NAME: the name of the consumer VPC network in HOST_PROJECT_ID.
  * SUBNET_NAME: the name of a subnet in VPC_NAME that is located in REGION.
  * APIGEE_HOSTNAME: the hostname you have configured on the Apigee environment group (for example, `api.internal.example.com`).
  * BASE_PATH: the base path of the API proxy deployed on Apigee (for example, `/mcp` or `/orders`).
  * PARENT_DNS_NAME: the parent DNS domain of APIGEE_HOSTNAME that you want to serve from the private zone (for example, `internal.example.com.`). The value must end with a dot.
  * APIGEE_INSTANCE_NAME: the name of your Apigee instance in REGION.

**Note on project topology:** APIGEE_PROJECT_ID, SERVICE_PROJECT_ID, and HOST_PROJECT_ID are independent. They can all be the same project, all different, or any combination that fits how you organize your Google Cloud resources. 

  * If you use [Shared VPC](https://cloud.google.com/vpc/docs/shared-vpc) for your consumer network, HOST_PROJECT_ID is the host project and SERVICE_PROJECT_ID is a service project attached to it. Otherwise, HOST_PROJECT_ID is the same as SERVICE_PROJECT_ID.
  * For details about which project owns the network attachment and the corresponding IAM roles in a Shared VPC deployment, see [Using Private Service Connect interface with Shared VPC](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#using-with-vpc-shared-vpc) in the Agent Platform documentation.



You need the following: 

  * One or more Google Cloud projects (as described in the preceding note) with billing enabled. 
  * An existing Apigee organization in APIGEE_PROJECT_ID with at least one [instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances). This document creates all of the consumer networking resources (network attachment, Private Service Connect endpoint, Agent Runtime deployment) in the same region as your Apigee instance, which is the simplest configuration. 
  * An [environment group](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with) whose environments are deployed to that Apigee instance, and that includes the hostname you want your agent to call. This document refers to that hostname as APIGEE_HOSTNAME. 
  * At least one API proxy deployed to an environment in that environment group. Any proxies you want the agent to call must be reachable at `https://APIGEE_HOSTNAME/BASE_PATH`. 
  * A VPC network and subnet in HOST_PROJECT_ID, in the same region as the Apigee instance. This document refers to these as VPC_NAME and SUBNET_NAME. Agent Runtime requires a minimum `/28` subnet, and imposes additional range restrictions. For details, see [Subnetwork IP range requirements](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#subnetwork-ip-range-requirements) in the Agent Platform documentation. 
  * The following APIs enabled in the appropriate project: 
    * Apigee (`apigee.googleapis.com`) in APIGEE_PROJECT_ID.
    * Compute Engine (`compute.googleapis.com`) and Cloud DNS (`dns.googleapis.com`) in HOST_PROJECT_ID.
    * Agent Platform (`aiplatform.googleapis.com`) in SERVICE_PROJECT_ID.
  * Sufficient IAM permissions to create Cloud DNS zones and records, Compute Engine addresses, network attachments, and Private Service Connect forwarding rules in HOST_PROJECT_ID, and to update Apigee instance and environment group configuration in APIGEE_PROJECT_ID. For details on the required roles, see [Apigee roles](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/apigee-roles), [Cloud DNS access control](https://docs.cloud.google.com/dns/docs/access-control), and [Compute Engine IAM roles](https://docs.cloud.google.com/compute/docs/access/iam). 



## Architecture

The following steps describe the traffic flow between an agent deployed on Agent Runtime and an API proxy hosted on Apigee, using a Private Service Connect endpoint in a consumer VPC as the bridge. 

  1. The agent, running on Agent Runtime, makes an HTTPS request to APIGEE_HOSTNAME. 
  2. DNS peering configured on the Agent Runtime PSC interface forwards the lookup to the Cloud DNS private zone in your consumer VPC, which returns the IP address of the Private Service Connect endpoint. 
  3. The agent's request egresses through the PSC interface into your consumer VPC and reaches the Private Service Connect endpoint on that IP address. 
  4. The Private Service Connect endpoint forwards the request over the service connection to the Apigee instance's service attachment. 
  5. The Apigee instance terminates TLS, matches the request hostname to the environment group, and routes to the correct API proxy. 



##  Step 1: Configure networking in the consumer VPC 

This section configures resources across two projects. Each command includes an explicit `--project` flag so you can run the commands from any active gcloud configuration: 

  * Cloud DNS resources (private zone and record) are created in HOST_PROJECT_ID, because the private zone attaches to the consumer VPC network.
  * The Private Service Connect endpoint resources (static internal IP address and forwarding rule) and the network attachment are created in SERVICE_PROJECT_ID. Each of these commands uses a cross-project reference to the shared subnet or VPC network in HOST_PROJECT_ID. In a single-project deployment, SERVICE_PROJECT_ID and HOST_PROJECT_ID are the same, so no ownership changes across steps. For more information about the Shared VPC model for Private Service Connect endpoints, see [Create an endpoint in a Shared VPC service project](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#shared-vpc).



### Create a Cloud DNS private zone

Create a Cloud DNS private zone that is visible only to your consumer VPC. The agent uses this zone (via DNS peering) to resolve APIGEE_HOSTNAME to a private IP address. 
    
    
    gcloud dns managed-zones create apigee-private \
      --project=HOST_PROJECT_ID \
      --dns-name="PARENT_DNS_NAME" \
      --description="Private zone for Apigee PSC access" \
      --visibility=private \
      --networks=VPC_NAME
    

For more information about Cloud DNS private zones, see [Private zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview#private-zones). 

### Create a network attachment

Create a [network attachment](https://cloud.google.com/vpc/docs/about-network-attachments) in the same region and subnet where you want the Agent Runtime PSC interface to appear. Agent Runtime binds its PSC interface to this attachment when the agent is deployed. 

In a single-project deployment, create the network attachment in SERVICE_PROJECT_ID (which is also HOST_PROJECT_ID). In a Shared VPC deployment, you can create the network attachment in either the service project or the host project; Agent Platform recommends the service project to simplify permissions. For guidance on choosing and the corresponding IAM roles, see [Using Private Service Connect interface with Shared VPC](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#using-with-vpc-shared-vpc). 

The following command creates the network attachment in SERVICE_PROJECT_ID. In a Shared VPC deployment, the subnet reference must include the host project ID. 
    
    
    gcloud compute network-attachments create agent-network-attachment \
      --project=SERVICE_PROJECT_ID \
      --region=REGION \
      --subnets=projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME \
      --connection-preference=ACCEPT_AUTOMATIC
    

### Reserve a static internal IP address

Reserve an internal IP address to use as the IP of the Private Service Connect endpoint that the agent connects to. Create the address resource in SERVICE_PROJECT_ID, and reference the shared subnet in HOST_PROJECT_ID so that the address value is allocated from that subnet's range. This matches the Shared VPC guidance in [Use a static internal IP address with Shared VPC](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address#sharedvpc). 
    
    
    gcloud compute addresses create apigee-psc-endpoint-ip \
      --project=SERVICE_PROJECT_ID \
      --region=REGION \
      --subnet=projects/HOST_PROJECT_ID/regions/REGION/subnetworks/SUBNET_NAME
    

Retrieve the reserved address, which you use in later steps: 
    
    
    gcloud compute addresses describe apigee-psc-endpoint-ip \
      --project=SERVICE_PROJECT_ID \
      --region=REGION \
      --format="value(address)"
    

This document refers to this address as PSC_ENDPOINT_IP. 

###  Get the service attachment for the Apigee instance 

Retrieve the service attachment URI for your Apigee instance using the [`organizations.instances.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/get) method of the Apigee API. You use this URI as the target for the Private Service Connect endpoint. 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/APIGEE_PROJECT_ID/instances/APIGEE_INSTANCE_NAME"
    

The response includes a `serviceAttachment` field. This document refers to that value as APIGEE_SERVICE_ATTACHMENT. For more information about how Apigee exposes a service attachment on each instance, see [Managing instances](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances). 

###  Create the Private Service Connect endpoint 

Create a forwarding rule that acts as the Private Service Connect endpoint. It targets the Apigee service attachment and uses the static IP that you reserved. Create the forwarding rule in SERVICE_PROJECT_ID and reference the shared VPC network in HOST_PROJECT_ID and the address in SERVICE_PROJECT_ID. 
    
    
    gcloud compute forwarding-rules create apigee-psc-endpoint \
      --project=SERVICE_PROJECT_ID \
      --region=REGION \
      --network=projects/HOST_PROJECT_ID/global/networks/VPC_NAME \
      --address=projects/SERVICE_PROJECT_ID/regions/REGION/addresses/apigee-psc-endpoint-ip \
      --target-service-attachment=APIGEE_SERVICE_ATTACHMENT
    

Verify that the Apigee service accepted the connection: 
    
    
    gcloud compute forwarding-rules describe apigee-psc-endpoint \
      --project=SERVICE_PROJECT_ID \
      --region=REGION \
      --format="value(pscConnectionStatus)"
    

The status must be `ACCEPTED` before the endpoint can forward traffic. For more information about Private Service Connect endpoints, see [About accessing published services through endpoints](https://cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints). 

### Add a DNS record for the hostname

In the private zone, create an `A` record that resolves APIGEE_HOSTNAME to PSC_ENDPOINT_IP. This record is only visible inside VPC_NAME, so external clients continue to resolve the hostname through public DNS. 
    
    
    gcloud dns record-sets create APIGEE_HOSTNAME. \
      --project=HOST_PROJECT_ID \
      --zone=apigee-private \
      --type=A \
      --ttl=60 \
      --rrdatas=PSC_ENDPOINT_IP
    

## Step 2: Configure Apigee

###  Add the service project to the instance consumer accept list 

The Apigee instance only accepts Private Service Connect connections from consumer projects that are on its [`consumerAcceptList`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances#Instance.FIELDS.consumer_accept_list). The consumer side of the connection is associated with SERVICE_PROJECT_ID, because that is the project where the agent is deployed. 

By default, the project associated with the Apigee organization (APIGEE_PROJECT_ID) is already on the list. If SERVICE_PROJECT_ID is the same as APIGEE_PROJECT_ID, no change is needed and you can skip this section. Otherwise, add SERVICE_PROJECT_ID to the list. 

First, check the current value of `consumerAcceptList` using the [`organizations.instances.get`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/get) method: 
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      "https://apigee.googleapis.com/v1/organizations/APIGEE_PROJECT_ID/instances/APIGEE_INSTANCE_NAME"
    

Look for the `consumerAcceptList` field in the response. 

Then update the list by calling the [`organizations.instances.patch`](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/patch) method with an update mask on `consumerAcceptList`. Because the field replaces the existing list, include every project ID that must retain access, including APIGEE_PROJECT_ID and any additional service projects that deploy agents: 
    
    
    curl -X PATCH \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -d '{"consumerAcceptList": ["APIGEE_PROJECT_ID", "SERVICE_PROJECT_ID"]}' \
      "https://apigee.googleapis.com/v1/organizations/APIGEE_PROJECT_ID/instances/APIGEE_INSTANCE_NAME?updateMask=consumerAcceptList"
    

Confirm the update by running the `get` command again and verifying that SERVICE_PROJECT_ID is now included in `consumerAcceptList`. 

**Alternative:** You can also add or remove accepted projects using the Google Cloud console. See [Edit the accepted projects list](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances#accepted-projects) in Managing instances. 

###  Verify the environment group hostname 

Confirm that APIGEE_HOSTNAME is listed on the environment group that hosts your API proxies. If it is not, add it. 

For instructions, see [Working with environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environmentgroups-working-with). 

##  Step 3: Deploy your agent with a PSC interface and DNS peering 

When you deploy your agent to Agent Runtime, configure it with a PSC interface that references the network attachment you created, and configure DNS peering to your private zone. For the full deployment procedure and supported frameworks, see [Using Private Service Connect interface with Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface) and [Deploy agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) in the Agent Platform documentation. 

Configure the following two fields on the agent's PSC interface configuration (see the [`PscInterfaceConfig`](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/Shared.Types/CustomJobSpec#PscInterfaceConfig) reference): 

  * **`networkAttachment`** : set this to the full resource name of the network attachment that you created in Step 1, in the form `projects/SERVICE_PROJECT_ID/regions/REGION/networkAttachments/agent-network-attachment`. If you created the network attachment in the host project instead, use HOST_PROJECT_ID in this path. 
  * **`dnsPeeringConfigs`** : add one entry with the following fields, so that Agent Runtime resolves APIGEE_HOSTNAME through your private zone: 
    * `domain`: PARENT_DNS_NAME. The value must end with a dot.
    * `targetProject`: HOST_PROJECT_ID. This is the project that contains the consumer VPC and the private zone.
    * `targetNetwork`: VPC_NAME.



The Agent Platform Service Agent for SERVICE_PROJECT_ID (`service-SERVICE_PROJECT_NUMBER@gcp-sa-aiplatform.iam.gserviceaccount.com`) must have permission to configure DNS peering and to update the network attachment. Grant the required roles as described in [Agent Platform service agent required role](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/general/vpc-psc-i-setup#service-agent-required-role). In a Shared VPC deployment, additional roles apply on the host project; see [Using Private Service Connect interface with Shared VPC](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface#using-with-vpc-shared-vpc). 

From the agent code, call the API proxy at `https://APIGEE_HOSTNAME/BASE_PATH`. Inside the Agent Runtime environment, this hostname resolves through DNS peering to PSC_ENDPOINT_IP, and the request traverses the Private Service Connect endpoint into your VPC and on to Apigee. 

**Note:** Because the Apigee instance presents a self-signed certificate on the private path, your agent's HTTP client must either accept self-signed certificates or use a configuration that places an internal Application Load Balancer with a managed TLS certificate in front of the service attachment. See [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc) for the load-balanced variant.

## Verify the private path

After you deploy the agent, verify that requests reach Apigee through the private path: 

  * Confirm the forwarding rule status is `ACCEPTED`, using the command in Create the Private Service Connect endpoint. 
  * From a Compute Engine VM attached to VPC_NAME in REGION (in a Shared VPC deployment, this VM can be in either the host project or a service project attached to the shared VPC), run `dig +short APIGEE_HOSTNAME`. The result must be PSC_ENDPOINT_IP. This confirms that the private zone resolves the hostname correctly inside the VPC. 
  * From the same VM, send a request to a deployed API proxy at `https://APIGEE_HOSTNAME/BASE_PATH` and confirm that you receive the expected response. 
  * Invoke the deployed agent and confirm that the request is served. Then use [Apigee Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview) or [Debug](https://docs.cloud.google.com/apigee/docs/api-platform/debug/trace-overview) to confirm that the request arrived at the expected API proxy on the environment group hostname. 



## What's next

  * Learn more about [Using Private Service Connect interface with Agent Runtime](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/private-service-connect-interface). 
  * Learn how to [Deploy agents](https://docs.cloud.google.com/gemini-enterprise-agent-platform/scale/runtime/deploy-an-agent) on Agent Runtime. 
  * Read about [Northbound networking with Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/northbound-networking-psc), the load-balancer-based variant that uses a managed TLS certificate. 
  * Read about [Southbound networking patterns](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints), which describe how Apigee connects privately to your backend targets. 
  * Learn about [MCP in Apigee](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-mcp/apigee-mcp-overview) for exposing your APIs as MCP tools to agentic applications. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
