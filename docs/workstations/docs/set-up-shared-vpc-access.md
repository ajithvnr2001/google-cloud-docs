---
url: https://docs.cloud.google.com/workstations/docs/set-up-shared-vpc-access/
title: Set up Shared VPC access \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:57.297108+00:00
---

# Set up Shared VPC access  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/set-up-shared-vpc-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Set up Shared VPC access Stay organized with collections  Save and categorize content based on your preferences. 

Shared VPC is an optional deployment model that lets an organization connect resources from multiple projects to a common VPC network. Organization administrators can use Shared VPC to delegate administrative responsibilities while maintaining centralized control over network resources, such as subnets, routes, and firewalls.

**Note:** Private clusters and Shared VPC are independent features. You can use a private cluster either in a standard VPC network or in a Shared VPC network.

## Grant the required roles

The [Cloud Workstations Service Agent](https://docs.cloud.google.com/workstations/docs/service-accounts#workstations-service-agent) allows Cloud Workstations perform service duties on your project. When you activated the Cloud Workstations Service in your project, the service agent was automatically created. To enable Cloud Workstations to use your Shared VPC network and subnetwork, grant the Cloud Workstations Service Agent for your project the [Compute Engine Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) on the Shared VPC subnet.

  1. To retrieve the Cloud Workstations Service Agent for your project, use the following command:
         
         gcloud beta services identity create \
             --service=workstations.googleapis.com \
             --project=WORKSTATIONS_PROJECT_ID
         

Replace `WORKSTATIONS_PROJECT_ID` with the ID of the project where you will create your workstations cluster.

The Cloud Workstations Service Agent uses the following format:  
`service-$WORKSTATIONS_PROJECT_NUMBER@gcp-sa-workstations.iam.gserviceaccount.com`.

  2. Grant the Cloud Workstations Service Agent the [Compute Engine Network User role](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) (`roles/compute.networkUser`) role on the Shared VPC subnet.




## Create workstation clusters using a Shared VPC

When you [create your workstation cluster](https://docs.cloud.google.com/workstations/docs/create-configuration) in the Google Cloud console, specify the Shared VPC network and subnetwork. This step is only possible if the subnet is shared with the user using the console. For more information, see [Provision Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) .

For general information about Shared VPC access, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) .

When you create a workstation cluster, Cloud Workstations associates the cluster with a particular subnet and all workstations are placed in that subnet. To enable VPC Flow Logs, make sure that you turn on logging for that subnet. For more information, see [Enable VPC Flow Logs for an existing subnet](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enable-logging-existing).

**Tip:** When using Shared VPC, make sure that you add and configure firewall rules for the Shared VPC network. For more information, see [Configure firewall rules](https://docs.cloud.google.com/workstations/docs/configure-firewall-rules) .

## What's next

  * [Troubleshoot policy and access problems](https://docs.cloud.google.com/vpc/docs/troubleshooting-policy-and-access-problems)
  * [Configure VPC Service Controls and private clusters](https://docs.cloud.google.com/workstations/docs/configure-vpc-service-controls-private-clusters)
  * [Enable VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
