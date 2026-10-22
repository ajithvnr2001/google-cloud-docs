---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client/
title: Create a client certificate \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:40.953053+00:00
---

# Create a client certificate  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-client/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a client certificate

**Note:** The legacy _AzureClient_ method of authenticating to Azure requires you to manage secrets and upload them manually. We recommend that you use [workload identity federation](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application#workload-identity-federation) instead.

GKE on Azure authenticates to Azure with an _AzureClient_ resource. When you create a client, Google generates a key pair. You upload the public key to Azure Active Directory (Azure AD). The GKE Multi-Cloud API uses the AzureClient to authenticate as the application's service principal.

You can use the same AzureClient to create multiple clusters in the same Google Cloud project. If you already have an AzureClient, skip to [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair).

To create an AzureClient, run the following commands:

  1. Set environment variables with your Azure tenant and application IDs:
         
         export SUBSCRIPTION_ID=$(az account show --query "id" --output tsv)
         export TENANT_ID=$(az account list \
           --query "[?id=='${SUBSCRIPTION_ID}'].{tenantId:tenantId}" --output tsv)
         export APPLICATION_ID=$(az ad app list --all \
           --query "[?displayName=='APPLICATION_NAME'].appId" --output tsv)
         

Replace `APPLICATION_NAME` with the Azure AD application name that you used when completing the [prerequisites](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application).

  2. Create the client:
         
         gcloud container azure clients create CLIENT_NAME \
           --location=GOOGLE_CLOUD_LOCATION \
           --tenant-id="${TENANT_ID}" \
           --application-id="${APPLICATION_ID}"
         

Replace the following:

     * `CLIENT_NAME`: the name of your AzureClient
     * `GOOGLE_CLOUD_LOCATION`: the [supported Google Cloud region](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/supported-regions) that manages your cluster—for example, `us-west1`
  3. Get the certificate from an AzureClient and save it to an environment variable:
         
         CERT=$(gcloud container azure clients get-public-cert --location=GOOGLE_CLOUD_LOCATION \
               CLIENT_NAME)
         

Replace the following:

     * `GOOGLE_CLOUD_LOCATION`
     * `CLIENT_NAME`
  4. Upload the certificate to your application on Azure AD:
         
         az ad app credential reset --id "${APPLICATION_ID}" --cert "${CERT}" --append
         

  5. After the certificate uploads and before you create a cluster, wait at least one minute for the certificate to be ready to use. If the command fails, you can try again.

**Note:** If the preceding command fails with the following message, save the certificate to a file and upload it to your application's page on the Azure portal:
         
         Update to existing credential with KeyId 'XXXXXXX-XXXXX-XXX-XXXX-XXXXXXXXXXXX' is not allowed.
         

To get a link to your application's page, replace APPLICATION_ID in the following URL with your application's ID: 
         
         https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/Credentials/appId/APPLICATION_ID
         




## What's next

  * [Create an SSH key pair](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-ssh-keypair)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
