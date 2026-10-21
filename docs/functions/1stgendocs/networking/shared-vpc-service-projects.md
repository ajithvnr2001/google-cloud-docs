---
url: https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-service-projects/
title: Configure connectors in Shared VPC service projects \u00a0|\u00a0 Cloud Run functions (1st gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:29:40.685885+00:00
---

# Configure connectors in Shared VPC service projects  |  Cloud Run functions (1st gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-service-projects/

If you are creating a new function, see the [Console Quickstart](https://cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. The content on this page only applies to existing legacy functions created with the Cloud Functions v1 API. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ 1st generation ](https://docs.cloud.google.com/functions/1stgendocs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/functions/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure connectors in Shared VPC service projects

If your organization uses Shared VPC, you can set up Serverless VPC Access connectors in either the service project or the host project. This guide shows how to set up a connector in the service project.

If you need to set up a connector in the host project, see [Configure connectors in the host project](https://docs.cloud.google.com/functions/1stgendocs/networking/shared-vpc-host-project). To learn about the advantages of each method, see [Connecting to a Shared VPC network](https://docs.cloud.google.com/functions/1stgendocs/networking/connecting-shared-vpc).

At a high level, you must take the following steps:

  1. Add firewall rules to allow required IP ranges
  2. Grant permissions
  3. Create a subnet
  4. In the page [Configuring Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access), complete the steps in the following sections: 
     * [Create a Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#create-connector)
     * [Configure your serverless environment to use a connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#configure-environment)



## Add firewall rules to allow IP ranges

To perform these steps, you must have one of the following roles on the host project:

  * Compute Engine [Security Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) role
  * Custom [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) role with the [`compute.firewalls.create`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert#iam-permissions) permission enabled



You must create firewall rules to allow requests from the following IP ranges to reach the connector and to be reached by the connector:

  * NAT ranges 
    * `107.178.230.64/26`
    * `35.199.224.0/19`
  * Health check ranges 
    * `130.211.0.0/22`
    * `35.191.0.0/16`
    * `108.170.220.0/23`



These ranges are used by the Google infrastructure underlying Cloud Run, Cloud Run functions, and App Engine Standard. All requests from these IPs are guaranteed to originate from Google infrastructure, which ensures that your function only communicates with the VPC connector it is connected to.

For a simple configuration, apply the rules to allow serverless services in any service project connected to the Shared VPC network to send requests to any resource in the network.

**Important:** The rules you create using the following process apply to existing and future connectors. If you want to scope these rules so they only apply to specified connectors, see Create firewall rules for specific connectors.

To apply these rules:

  1. Run the following three commands to set the rules to allow requests from the serverless environment to reach all VPC Connectors in the network:

**Note:** In these commands, UDP and TCP ports are used for proxying and HTTP health checks, respectively.
         
         gcloud compute firewall-rules create serverless-to-vpc-connector \
         --allow tcp:667,udp:665-666,icmp \
         --source-ranges 107.178.230.64/26,35.199.224.0/19 \
         --direction=INGRESS \
         --target-tags vpc-connector \
         --network=VPC_NETWORK
         
         gcloud compute firewall-rules create vpc-connector-to-serverless \
         --allow tcp:667,udp:665-666,icmp \
         --destination-ranges 107.178.230.64/26,35.199.224.0/19 \
         --direction=EGRESS \
         --target-tags vpc-connector \
         --network=VPC_NETWORK
         
         gcloud compute firewall-rules create vpc-connector-health-checks \
         --allow tcp:667 \
         --source-ranges 130.211.0.0/22,35.191.0.0/16,108.170.220.0/23 \
         --direction=INGRESS \
         --target-tags vpc-connector \
         --network=VPC_NETWORK

Where `VPC_NETWORK` is the VPC network to attach your connector to.

  2. Create an ingress rule on your VPC network to allow requests from connectors:
         
         gcloud compute firewall-rules create vpc-connector-requests \
         --allow tcp,udp,icmp \
         --direction=INGRESS \
         --source-tags vpc-connector \
         --network=VPC_NETWORK

This rule gives the VPC connector access to every resource in the network. To limit the resources that your serverless environment can reach using Serverless VPC Access, [specify a target for these firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#rule_assignment).




### Create firewall rules for specific connectors

Following the procedure in Add firewall rules to allow IP ranges results in firewall rules that apply to _all_ connectors, both current ones and ones created in the future. If you don't want this, but instead want to create rules for specific connectors only, you can scope the rules so that they apply only to those connectors.

To limit the scope of the rules to specific connectors, you can use one of the following mechanisms:

  * Network tags. Every connector has two network tags: `vpc-connector` and `vpc-connector-REGION-CONNECTOR_NAME`. Use the latter format to limit the scope of your firewall rules to a specific connector.
  * IP ranges. Use this for the Egress rules only, because it doesn't work for Ingress. You can use the IP range of the connector subnet to limit the scope of your firewall rules to a single VPC connector.



## Grant permissions to service accounts in your service projects

For each service project that will use VPC Connectors, a Shared VPC Admin must grant the Compute Network User role ([`compute.networkUser`](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)) in the host project to the service project `cloudservices` and `vpcaccess` service accounts.

To grant the role:

  1. Use these commands:
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --role "roles/compute.networkUser" \
         --member "serviceAccount:service-SERVICE_PROJECT_NUMBER@gcp-sa-vpcaccess.iam.gserviceaccount.com"
         
         gcloud projects add-iam-policy-binding HOST_PROJECT_ID \
         --role "roles/compute.networkUser" \
         --member "serviceAccount:SERVICE_PROJECT_NUMBER@cloudservices.gserviceaccount.com"

  2. If the `@gcp-sa-vpcaccess` service account does not exist, turn on the Serverless VPC Access API in the service project and try again: 
         
         gcloud services enable vpcaccess.googleapis.com




If you prefer not to grant these service accounts access to the entire Shared VPC network and would rather only grant access to specific subnets, you can instead [grant these roles to these service accounts on specific subnets only](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins).

## Create a subnet

When using Shared VPC, the Shared VPC Admin must create a subnet for each connector. Follow the documentation in [adding a subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) to add a `/28` subnet to the Shared VPC network. This subnet must be in the same region as the serverless services that will use the connector.

## Next steps

  * In the page [Configuring Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access), complete the steps in the following sections: 
    * [Create a Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#create-connector)
    * [Configure your serverless environment to use a connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#configure-environment)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
