---
url: https://docs.cloud.google.com/certificate-manager/docs/public-ca-tutorial/
title: Request a certificate using Public CA and an ACME client \u00a0|\u00a0 Certificate Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:32.313607+00:00
---

# Request a certificate using Public CA and an ACME client  |  Certificate Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/public-ca-tutorial/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-manager/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Request a certificate using Public CA and an ACME client

This tutorial walks you through requesting a TLS certificate with Public Certificate Authority by using the Google Cloud CLI. For information about the root and intermediate CAs used by Public Certificate Authority, see [Google Trust Services](https://pki.goog/). There is no charge for requesting certificates from Public CA.

## Before you begin

  * [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
        
        gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** You can run the gcloud CLI in the Google Cloud console without installing the Google Cloud CLI. To run the gcloud CLI in the Google Cloud console, [use Cloud Shell](https://console.cloud.google.com/?cloudshell=true). 
  * [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

    * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
    * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
    * Create a Google Cloud project:
          
          gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

    * Select the Google Cloud project that you created:
          
          gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  * Make sure that you have the Public CA External Account Key Creator (`roles/publicca.externalAccountKeyCreator`) IAM role.

To grant this role, run the following command:
        
        gcloud projects add-iam-policy-binding PROJECT_ID \
          --member=user:USER \
          --role=roles/publicca.externalAccountKeyCreator
        

Replace the following:

    * `PROJECT_ID`: the ID of your Google Cloud project
    * `USER`: the unique identifier of the user to whom you want to assign the IAM role

For information about granting an IAM role, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

  * Enable the Public CA API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable publicca.googleapis.com




## Install a client

To get started using Public CA, you must install an [ACME client](https://acmeclients.com/). The following instructions use [Certbot](https://certbot.eff.org/pages/about) as the ACME client. You can use any other ACME client if the client supports external account binding (EAB).

To install Certbot, see the [Certbot instructions](https://certbot.eff.org/instructions).

Make sure to point your client to the Public CA server. The first time the ACME client interacts with Public CA, the client generates a new key pair and sends the public key to Public CA.

## Request an EAB key ID and HMAC

After you install an ACME client, you must register your ACME account with Public CA to request certificates from Public CA. An EAB secret can help you register your ACME account with Public CA. An EAB secret consists of a key ID and a hash-based message authentication code (HMAC).

You can use the [Public CA API](https://docs.cloud.google.com/certificate-manager/docs/reference/public-ca/rest) or the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud/reference/publicca) to request an EAB secret.

To request an EAB key ID and HMAC, run the following command:
    
    
    gcloud publicca external-account-keys create
    

This command returns an EAB secret that is valid on the production environment of Public CA. In the response body, the `keyId` field contains the EAB key ID, and the `b64MacKey` field contains the EAB HMAC.

**Note:** To request an EAB secret for the staging environment, you must first configure your `gcloud` client to use the staging API endpoint. For more information, see the Staging section.

You must use an EAB secret within 7 days of obtaining it. The EAB secret is invalidated if you don't use it within 7 days. The ACME account registered by using an EAB secret has no expiration.

## Register an ACME account

This section explains how to register an ACME account with Public CA by providing the EAB secret that you just obtained.

Use a regular ACME client to register an ACME account, and provide the EAB key ID and HMAC while registering.

**Note:** If you are using the API, know that the HMAC is [base64 URL-encoded](https://datatracker.ietf.org/doc/html/rfc4648#section-5), which is slightly different from the regular base64 encoding.

To register an ACME account with Public CA and bind the ACME account to the Google Cloud project that you used to request the EAB secret, run the following command:
    
    
    certbot register \
        --email "EMAIL_ADDRESS" \
        --no-eff-email \
        --server "SERVER" \
        --eab-kid "EAB_KID" \
        --eab-hmac-key "EAB_HMAC_KEY"
    

Replace the following:

  * `EMAIL_ADDRESS`: your email address
  * `SERVER`: the ACME directory URL for the production or staging environment
  * `EAB_KID`: the EAB key ID
  * `EAB_HMAC_KEY`: the EAB HMAC key



The following table provides the description and the ACME directory URL for the production and staging environment:

Environment | Description | ACME directory URL  
---|---|---  
**Production** | The production environment lets you obtain publicly trusted certificates. | `https://dv.acme-v02.api.pki.goog/directory`  
Staging | The staging environment returns certificates that are _not_ publicly trusted. The staging environment performs the same validation checks as the production environment. You can use the staging environment for integration or any other kind of testing. | `https://dv.acme-v02.test-api.pki.goog/directory`  
  
You can only register one ACME account with an EAB secret. After you have registered an ACME account by using an EAB secret, the EAB secret becomes invalid and you can't reuse it. If you want to register multiple ACME accounts, you must request a unique EAB secret for each of the accounts.

## Request certificates

After Public CA validates your control of the certificate target and acknowledges that your ACME client works as expected to perform certificate management operations, you can use the regular ACME workflows to request, renew, and revoke certificates. You can perform these operations by using your ACME client. To request and renew a certificate, you must complete an [ACME challenge](https://docs.cloud.google.com/certificate-manager/docs/public-ca#public-ca-challenges), such as the manual DNS challenge.

To use the manual DNS challenge to request a certificate, run the following command:
    
    
    certbot certonly \
        --manual \
        --preferred-challenges "dns-01" \
        --server "SERVER" \
        --domains "DOMAINS"
    

Replace the following:

  * `SERVER`: the ACME directory URL for the production or staging environment
  * `DOMAINS`: a comma-separated list of domains for which you are requesting certificates



## Clean up

**Caution:** Deleting a Google Cloud project invalidates all the ACME accounts that you have linked to the project. After your Google Cloud project is deleted, you will not be able to renew or issue certificates.

If you no longer need certificates for your domains, delete the project that you created.

## Staging

You can use the staging environment of Public CA to request certificates for testing purposes. The certificates issued by the staging environment chain up to a [test root CA](https://pki.goog/test_roots.pem). Certificates from the staging environment will not be trusted by Browsers or other clients that have not been configured to trust the staging root certificate. To obtain an EAB secret that is valid on the staging environment, override the API endpoint to use the endpoint for the staging environment:
    
    
    gcloud config set api_endpoint_overrides/publicca https://preprod-publicca.googleapis.com/
    

Then run the account key creation command to create a staging key: 
    
    
    gcloud publicca external-account-keys create
    

To revert to the endpoint for the production environment, run the following command: 
    
    
    gcloud config unset api_endpoint_overrides/publicca
    

**Caution** : Deleting a project has the following effects: 

  * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
  * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 



If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    
    gcloud projects delete PROJECT_ID

## What's next

  * [Public Certificate Authority](https://docs.cloud.google.com/certificate-manager/docs/public-ca)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
