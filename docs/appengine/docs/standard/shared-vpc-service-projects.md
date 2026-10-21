---
url: https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-service-projects/
title: Configure connectors in Shared VPC service projects \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:58:59.661136+00:00
---

# Configure connectors in Shared VPC service projects  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-service-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Configure connectors in Shared VPC service projects Stay organized with collections  Save and categorize content based on your preferences. 

If your organization uses Shared VPC, you can set up Serverless VPC Access connectors in either the service project or the host project. This guide shows how to set up a connector in the service project.

If you need to set up a connector in the host project, see [Configure connectors in the host project](https://docs.cloud.google.com/appengine/docs/standard/shared-vpc-host-project). To learn about the advantages of each method, see [Connecting to a Shared VPC network](https://docs.cloud.google.com/appengine/docs/standard/connecting-shared-vpc).

At a high level, you must take the following steps:

  1. Grant permissions
  2. Create a subnet
  3. In the page [Configuring Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access), complete the steps in the following sections: 
     * [Create a Serverless VPC Access connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#create-connector)
     * [Configure your serverless environment to use a connector](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#configure-environment)
     * [Configure firewall rules for connectors](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#restrict-access)



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
