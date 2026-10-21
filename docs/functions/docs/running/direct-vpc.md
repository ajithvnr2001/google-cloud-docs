---
url: https://docs.cloud.google.com/functions/docs/running/direct-vpc/
title: Configure Direct VPC egress for 2nd gen functions \u00a0|\u00a0 Cloud Run functions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:26:25.948846+00:00
---

# Configure Direct VPC egress for 2nd gen functions  |  Cloud Run functions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/functions/docs/running/direct-vpc/

If you are creating a new function, see the [Console Quickstart](https://docs.cloud.google.com/run/docs/quickstarts/functions/deploy-functions-console) on Cloud Run. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Cloud Run functions ](https://docs.cloud.google.com/functions/docs)
  * [ Guides ](https://docs.cloud.google.com/functions/docs/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure Direct VPC egress for 2nd gen functions

Direct VPC egress lets you route traffic from your Cloud Run functions (2nd gen) function directly to your VPC network.

## Limitations

  * Direct VPC egress is not available for 1st gen functions.
  * You can't use Direct VPC egress and Serverless VPC Access connectors at the same time. See [Compare Direct VPC egress and VPC connectors](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) for details.
  * To learn about general limitations of using Direct VPC, see [Direct VPC with a VPC network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc).



## Before you begin

  * Enable the Cloud Functions API.
  * Install the Google Cloud CLI, then initialize it by running `gcloud init`.
  * Update `gcloud` components to version 558.0.0 or later: 
        
        gcloud components update
        

  * If you don't already have a VPC network in your project, [create one](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * Optional: If your function needs to access Google APIs and services using their internal IP addresses, enable Private Google Access on the subnet that you use for Direct VPC egress.




## Set up IAM permissions

To authorize Direct VPC egress, ask your administrator to grant the Cloud Run Invoker (`roles/run.invoker`) role to your function's service account.

Ensure that Cloud Run has access to the VPC network by using one of the following methods:

  * **Cloud Run Service Agent role** : By default, the Cloud Run [service agent](https://docs.cloud.google.com/iam/docs/service-agents) has the [Cloud Run Service Agent role (`roles/run.serviceAgent`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.serviceAgent) that contains the necessary permissions.

  * **Custom permissions** : For more granular control, grant the Cloud Run service agent with the following additional permissions on the project:

    * `compute.networks.get`
    * `compute.subnetworks.get`
    * `compute.subnetworks.use` on the project or the specific subnet
    * `compute.addresses.get`
    * `compute.addresses.list`
    * `compute.addresses.create` (required only for [dual-stack subnets with external IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet))
    * `compute.addresses.delete` (required only for dual-stack subnets with external IPv6)
    * `compute.addresses.createInternal`
    * `compute.addresses.deleteInternal`
    * `compute.regionOperations.get`
  * **Compute Network User role** : If you don't use the default Cloud Run Service Agent role or the custom permissions, grant the [Compute Network User role (`roles/compute.networkUser`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkUser) on the Cloud Run Service Agent service account. Subnets with external IPv6 also require the [Compute Public IP Admin role (`roles/compute.publicIpAdmin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin).

For example, to grant the Compute Network User role, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
        --member "serviceAccount:service-PROJECT_NUMBER@serverless-robot-prod.iam.gserviceaccount.com" \
        --role "roles/compute.networkUser"

Replace the following:

    * PROJECT_ID: the ID of your project.
    * PROJECT_NUMBER: the project number where you deploy your Cloud Run function.



## Configure Direct VPC egress

Configure Direct VPC egress for new or existing 2nd gen functions.

### gcloud

  1. To configure Direct VPC egress when you deploy a function, use the `gcloud functions deploy` command with flags for your network settings.
         
         gcloud functions deploy FUNCTION_NAME \
             --source . \
             --runtime RUNTIME \
             --trigger-http \
             --region REGION \
             --network=NETWORK \
             --subnet=SUBNET \
             --network-tags=NETWORK_TAG_NAMES \
             --direct-vpc-egress=EGRESS_SETTING
         

Replace the following:

     * FUNCTION_NAME: the name of your function.
     * RUNTIME: the runtime for your function, for example, `nodejs20`.
     * REGION: the region where you deploy your function.
     * Optional: NETWORK with the name of your VPC network. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network.
     * Optional: SUBNET with the name of your subnet. Specify either a VPC network or a subnet, or both. If you specify only a network, the subnet uses the same name as the network. You can deploy or execute multiple functions on the same subnet.
     * Optional: NETWORK_TAG_NAMES with the comma-separated names of the [network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags#restrictions) you want to associate with a function. Each function can have different network tags, such as `network-tag-2`.
     * EGRESS_SETTING with an [egress setting value](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy#--egress-settings): 
       * `all`: Default. Sends all outbound traffic through the VPC network.
       * `private-ranges-only`: Sends only traffic to internal addresses through the VPC network.
  2. Optional: To remove all Direct VPC egress settings from a function, redeploy the function with the `--clear-network` and `--clear-network-tags` flags.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

This feature (support for using Direct VPC egress with 2nd gen Cloud Run functions) adds the fields `direct_vpc_network_interface.network` and `direct_vpc_egress`.

To use this feature, follow these guidelines:

  * You must use Terraform version 7.21.0 or later.
  * If you redeploy a function that has existing Direct VPC, you now must explicitly set the values in the configuration.



Using the Cloud Run functions (2nd gen) [Direct VPC egress example](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloudfunctions2_function#example-usage---cloudfunctions2-directvpc) as a starting point, update the following fields:

  * `service_config.direct_vpc_network_interface.network`: the name of your VPC network.
  * `service_config.direct_vpc_network_interface.subnetwork`: the name of your VPC subnetwork.
  * `service_config.direct_vpc_egress`: which traffic to send to the VPC network. `VPC_EGRESS_ALL_TRAFFIC` sends all outbound traffic through the VPC network. `VPC_EGRESS_PRIVATE_RANGES_ONLY` only sends traffic to private IP address ranges to the VPC network.



## Example: Call an internal service from a function

This example shows how to create an internal Cloud Run service and then call it from a Cloud Run functions (2nd gen) function that uses Direct VPC egress.

### Create the internal backend service

  1. Create a new directory for the backend service and change into it:
         
         mkdir backend-service
         cd backend-service
         

  2. Create a `package.json` file with the following content:
         
         {
             "name": "backend-service",
             "version": "1.0.0",
             "description": "",
             "scripts": {
                 "start": "node index.js"
             },
             "dependencies": {
                 "express": "^4.18.1"
             }
         }
         

  3. Create an `index.js` file with the following content:
         
         const express = require('express');
         const app = express();
         
         app.get('/', (req, res) => {
             res.send("hello world");
         });
         
         const port = parseInt(process.env.PORT) || 8080;
         app.listen(port, () => {
             console.log(`helloworld: listening on port ${port}`);
         });
         

  4. Deploy the service to Cloud Run with internal ingress:
         
         gcloud run deploy backend \
             --source . \
             --no-allow-unauthenticated \
             --region=REGION \
             --ingress internal
         

Replace `REGION` with your region, for example, `us-west1`.

  5. Save the URL of the new service. You need it in the next section.




### Create and deploy the function

  1. Create a new directory for the function and change into it:
         
         cd ..
         mkdir dvpc-function
         cd dvpc-function
         

  2. Create a `package.json` file with the following content:
         
         {
           "name": "sample-http",
           "version": "0.0.1",
           "dependencies": {
             "axios": "0.21.1",
             "@google-cloud/functions-framework": "^3.0.0"
           }
         }
         

  3. Create an `index.js` file with the following content. This code makes an authenticated request to the internal backend service.
         
         const axios = require('axios');
         const functions = require('@google-cloud/functions-framework');
         
         const callVPCService = async (req, res) => {
           const backendUrl = process.env.BACKEND_URL;
         
           if (!backendUrl) {
             console.error('BACKEND_URL environment variable not set.');
             res.status(500).send('BACKEND_URL not configured.');
             return;
           }
         
           try {
             const metadataServerURL = 'http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience=';
             const tokenUrl = metadataServerURL + backendUrl;
         
             const tokenResponse = await axios.get(tokenUrl, {
               headers: {
                 'Metadata-Flavor': 'Google',
               },
             });
             const token = tokenResponse.data;
         
             const response = await axios.get(backendUrl, {
               headers: {
                 Authorization: `bearer ${token}`,
               },
         });
         
         res.status(200).send(`Response from backend: ${response.data}`);
           } catch (error) {
             console.error(`Error calling backend service: ${error.message}`);
             res.status(500).send(`Error calling backend: ${error.message}`);
           }
         };
         
         functions.http('callVPCService', callVPCService);
         

  4. Deploy the function with Direct VPC egress configured to route all traffic to your default VPC network:
         
         gcloud functions deploy my-2ndgen-function \
           --source . \
           --runtime nodejs20 \
           --trigger-http \
           --entry-point callVPCService \
           --network=default \
           --subnet=default \
           --direct-vpc-egress=all \
           --region=REGION \
           --allow-unauthenticated \
           --set-env-vars BACKEND_URL=BACKEND_URL
         

Replace the following:

     * `REGION`: the region where you deployed the backend service.
     * `BACKEND_URL`: the URL of the backend service you created.
  5. After the function deploys, invoke it by visiting its URL. The function calls the internal backend service and returns its response.




## What's next

  * Learn about Direct VPC egress and [IP allocation](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-ip-allocation).
  * Learn about [dual-stack subnet setup](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet).
  * See [Troubleshooting tips](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#troubleshooting).
  * Compare egress methods in [Connecting to a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).
  * See the [`gcloud functions deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/functions/deploy) command reference.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
