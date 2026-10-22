---
url: https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project/
title: Configure your Google Cloud project for Mainframe Assessment Tool \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:44.612637+00:00
---

# Configure your Google Cloud project for Mainframe Assessment Tool  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/mainframe-assessment-tool/docs/configure-your-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Mainframe Assessment Tool ](https://docs.cloud.google.com/mainframe-assessment-tool/docs)
  * [ Guides ](https://docs.cloud.google.com/mainframe-assessment-tool/docs/overview)



Send feedback 

#  Configure your Google Cloud project for Mainframe Assessment Tool Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the process to set up and configure your Google Cloud project to work with Mainframe Assessment Tool.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

**Note:** If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. Make sure that billing is enabled for your Google Cloud project. For more information, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  3. Create a dedicated service account to access Mainframe Assessment Tool. For more information, see [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create).

  4. For large assessments, make sure that you have sufficient quota in the region where you plan to create the Mainframe Assessment Tool instance. Larger quotas can be allocated by purchasing a [Provisioned Throughput](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput/overview).




## Enable APIs

  1. Enable the Compute Engine API.

[Enable Compute Engine API](https://console.cloud.google.com/apis/api/compute.googleapis.com/overview)

  2. Enable the Agent Platform API.

[Enable Agent Platform API](https://console.cloud.google.com/apis/api/aiplatform.googleapis.com/overview)

  3. Enable the Cloud Resource Manager API.

Mainframe Assessment Tool uses this API to verify that the service account has the roles listed in Assign IAM roles and permissions. The API call only reports the permissions that the caller already has, so the service account doesn't require any additional roles.

[Enable Cloud Resource Manager API](https://console.cloud.google.com/apis/api/cloudresourcemanager.googleapis.com/overview)




## Configure firewall rules

To enable secure access to the Mainframe Assessment Tool instance through IAP, create the following firewall rules:

  1. Create a firewall rule to allow ingress traffic on TCP port `4000` by [using IAP for TCP forwarding](https://docs.cloud.google.com/iap/docs/using-tcp-forwarding):
         
         gcloud compute firewall-rules create allow-ingress-from-iap \
           --direction=INGRESS \
           --action=allow \
           --rules=tcp:4000\
           --source-ranges=35.235.240.0/20
         

  2. Create a firewall rule to deny all other ingress traffic to your Mainframe Assessment Tool instance:
         
         gcloud compute firewall-rules create deny-all-other-ingress \
           --direction=ingress \
           --action=deny \
           --rules=all \
           --source-ranges=0.0.0.0/0 \
           --network=your-network-name \
           --priority=65535
         




## Optional: Configure private connectivity for data residency

Complete this section only if your Mainframe Assessment Tool instance doesn't have an external IP address, and you plan to run assessments with the **Keep data in my region** option enabled. If your instance has an external IP address or you don't use data residency, you can skip this section.

Without an external IP address, the Mainframe Assessment Tool instance uses [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access) to reach Agent Platform. Private Google Access doesn't support the multi-region endpoints (hosts in the `rep.googleapis.com` domain, such as `aiplatform.eu.rep.googleapis.com`) used for the `eu` and `us` multi-regions.

When you enable the **Keep data in my region** option, the model calls are restricted to the assessment region and its multi-region without a global fallback. Therefore, models served only on a multi-region endpoint are unreachable. If data residency is disabled, Mainframe Assessment Tool falls back to the global endpoint. Private Google Access supports the global endpoint, so no additional configuration is required.

To let your Mainframe Assessment Tool instance reach these endpoints, follow these steps:

  1. Create a [Private Service Connect endpoint](https://docs.cloud.google.com/vpc/docs/access-regional-google-apis-endpoints) that targets the multi-region endpoint in your VPC network:
         
         gcloud network-connectivity regional-endpoints create ENDPOINT_NAME \
             --project=PROJECT_ID \
             --region=REGION \
             --address=INTERNAL_IP \
             --network=projects/PROJECT_ID/global/networks/VPC_NETWORK \
             --subnetwork=projects/PROJECT_ID/regions/REGION/subnetworks/SUBNET \
             --target-google-api=aiplatform.eu.rep.googleapis.com
         

Replace the following:

     * ENDPOINT_NAME: a name for the Private Service Connect endpoint.
     * PROJECT_ID: the project ID of your VPC network.
     * REGION: the region in which to create the endpoint.
     * INTERNAL_IP: an unused internal IP address from your subnet.
     * VPC_NETWORK: the name of your VPC network.
     * SUBNET: the name of the subnet in the endpoint's region.

Replace `aiplatform.eu.rep.googleapis.com` with the multi-region endpoint for your region. For example, use `aiplatform.us.rep.googleapis.com` for the `us` multi-region.

If the Mainframe Assessment Tool instance and the Private Service Connect endpoint are in different regions, add the `--enable-global-access` flag. Otherwise, the endpoint accepts connections only from clients in its own region.

  2. Resolve the multi-region endpoint to the Private Service Connect endpoint.

Creating the endpoint doesn't change how the hostname resolves. If your VPC network uses a private zone to route Google APIs to a Private Google Access virtual IP address, that zone typically contains a `*.googleapis.com` record. Because this record also matches the multi-region endpoint, requests are routed to the virtual IP address, which cannot serve them. To resolve the multi-region endpoint to the Private Service Connect endpoint instead, add a more specific record:
         
         gcloud dns record-sets create aiplatform.eu.rep.googleapis.com. \
             --project=PROJECT_ID \
             --zone=DNS_ZONE \
             --type=A \
             --ttl=300 \
             --rrdatas=INTERNAL_IP
         

Replace the following:

     * `DNS_ZONE`: the name of the private zone for `googleapis.com` in your VPC network. If your VPC network doesn't have a private zone for `googleapis.com`, create a [private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone) to hold this record.
     * `INTERNAL_IP`: the internal IP address that you assigned to the endpoint.
  3. Restart your Mainframe Assessment Tool instance.

Mainframe Assessment Tool caches the models served by each endpoint and continues to use the previous results until restarted.




To verify the configuration, connect to the Compute Engine VM or a GKE node, and run the following command:
    
    
    openssl s_client -connect aiplatform.eu.rep.googleapis.com:443 \
        -servername aiplatform.eu.rep.googleapis.com < /dev/null 2>/dev/null \
        | openssl x509 -noout -subject

The command must return `subject=CN=aiplatform.eu.rep.googleapis.com`. If it returns `subject=CN=*.googleapis.com`, the hostname is still resolving to the Private Google Access virtual IP address. In this case, verify the DNS record you created.

The command returns `subject=CN=aiplatform.eu.rep.googleapis.com`. If it returns `subject=CN=*.googleapis.com`, then the hostname still resolves to the Private Google Access virtual IP address, and you need to check the record that you created.

## Assign IAM roles and permissions

To ensure that the dedicated service account that you created has the necessary permissions to give the Mainframe Assessment Tool components the required access to the Agent Platform API and other services, ask your administrator to grant the following IAM roles to the dedicated service account that you created: 

**Important:** You must grant these roles to the dedicated service account that you created, _not_ to your user account. Failure to grant the roles to the correct principal might result in permission errors. 

  * [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`)
  * Cloud Logging: [Logs Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter) (`roles/logging.logWriter`) 



## What's next

  * Learn how to [Set up and access Mainframe Assessment Tool](https://docs.cloud.google.com/mainframe-assessment-tool/docs/create-vm).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
