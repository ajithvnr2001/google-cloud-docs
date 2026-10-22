---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application/
title: Create an Azure Active Directory application \u00a0|\u00a0 GKE on Azure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:41.576297+00:00
---

# Create an Azure Active Directory application  |  GKE on Azure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-ad-application/

The product described by this documentation, GKE on Azure, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE on Azure ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/concepts/architecture)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create an Azure Active Directory application

In this section, you create an [Azure Active Directory](https://azure.microsoft.com/en-us/services/active-directory/) (Azure AD) application and service principal objects. GKE on Azure uses these objects to store configuration information on Azure.

  1. To create the Azure AD application, run the following command:
         
         az ad app create --display-name APPLICATION_NAME
         

Replace `APPLICATION_NAME` with a name for your application—for example, `anthos-clusters`.

  2. To save the application's ID to an environment variable for later use, run the following command:
         
         APPLICATION_ID=$(az ad app list --all \
          --query "[?displayName=='APPLICATION_NAME'].appId" \
          --output tsv)
         

Replace `APPLICATION_NAME` with the name of your application.

  3. To create a service principal for the application, run the following command:
         
         az ad sp create --id "${APPLICATION_ID}"
         




## Set up Workload identity federation

**Note:** GKE on Azure provides two methods of authenticating to Azure: workload identity federation authentication and _AzureClient_ authentication. We recommend that you use the workload identity federation method described in this document, because it's simpler and more secure.

Workload identity federation allows GKE on Azure to authenticate to Azure using a Google service account. This method of authenticating to Azure is simpler than the legacy AzureClient authentication method, which requires you to manage certificates and manually upload them to Azure Active Directory (AD).

To configure a federated identity credential on your Azure AD application, run the following commands. Note that you can add up to twenty credentials to each Azure AD application.

  1. Create a JSON file named `credential.json`.
         
         {
           "name": "CREDENTIAL_NAME",
           "issuer": "https://accounts.google.com",
           "subject": "service-PROJECT_NUMBER@gcp-sa-gkemulticloud.iam.gserviceaccount.com",
           "audiences": ["api://AzureADTokenExchange"],
           "description": "Allow GKE on Azure to authenticate to the Azure AD application using a Google service account."
         }
         

     * `CREDENTIAL_NAME`: the credential name.
     * `PROJECT_NUMBER`: the number of the Google Cloud project that hosts the cluster.
  2. Create a federated identity credential on the Azure AD application:
         
         az ad app federated-credential create --id "${APPLICATION_ID}" --parameters credential.json
         




For more details, see the Azure documentation [Azure AD workload identity federation with Google Cloud](https://blog.identitydigest.com/azuread-federate-gcp/).

You can also provision the Azure federated identity credential using Terraform. For details, see [azuread_application_federated_identity_credential](https://registry.terraform.io/providers/hashicorp/azuread/latest/docs/resources/application_federated_identity_credential).

## What's next

  * [Create Azure role assignments](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/how-to/create-azure-role-assignments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
