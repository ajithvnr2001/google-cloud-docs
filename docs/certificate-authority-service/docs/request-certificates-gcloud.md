---
url: https://docs.cloud.google.com/certificate-authority-service/docs/request-certificates-gcloud/
title: Quickstart: Issue a certificate using the Google Cloud CLI \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:34.185635+00:00
---

# Quickstart: Issue a certificate using the Google Cloud CLI  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/request-certificates-gcloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Issue a certificate using the Google Cloud CLI

This page explains how you can generate or issue certificates through Certificate Authority Service using the Google Cloud CLI.

CA Service lets you deploy and manage private CAs without managing infrastructure.

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

  * Enable the Certificate Authority Service API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
        
        gcloud services enable privateca.googleapis.com

  * [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  * Configure a default location for use in the `gcloud` commands in this quickstart.
        
        gcloud config set privateca/location LOCATION
        

CA Service resources, such as CA pools and CAs, live in a single [Google Cloud location](https://cloud.google.com/about/locations) that you cannot change after creating these resources.

**Note:** If you skip this step, you must add the `--location` flag to some of the following commands.



## Create a CA pool

A certificate authority (CA) pool is a collection of multiple CAs. A CA pool provides the ability to rotate trust chains without any outage or downtime for workloads.

To create a CA pool in the Enterprise tier, run the following command:
    
    
    gcloud privateca pools create POOL_ID --location LOCATION --tier "enterprise"
    

Replace the following:

  * POOL_ID: the name of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



Resource names can contain letters, numbers, hyphens (-), and underscores (_) and can be up to 63 characters long.

## Create a root CA

A CA pool is empty on creation. To request certificates from a CA pool, you must add a CA in it.

To create a root CA and add it in the CA pool you created, run the following command:
    
    
    gcloud privateca roots create CA_ID --pool POOL_ID --location LOCATION --subject "CN=Example Prod Root CA,O=Google"
    

Replace the following:

  * CA_ID: the name of the root CA
  * POOL_ID: the name of the CA pool
  * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).



CA Service returns the following output when it creates the root CA:
    
    
    Created Certificate Authority [projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificateAuthorities/CA_ID]
    

Enable the root CA by entering `y` when prompted by the gcloud CLI.

## Optional: Create a subordinate CA pool

To create a subordinate CA pool, run the following command:
    
    
        gcloud privateca pools create SUBORDINATE_POOL_ID
            --location LOCATION
            --tier TIER
    

Replace the following:

  * SUBORDINATE_POOL_ID: the ID of the subordinate CA pool
  * LOCATION: the location of the subordinate CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * TIER: the subordinate CA tier, either devops or enterprise



## Optional: Create a subordinate CA that's signed by a root CA stored in Google Cloud

To create a subordinate CA in the subordinate CA pool that you created in the previous step, run the following command:
    
    
        gcloud privateca subordinates create SUBORDINATE_CA_ID \
            --location=LOCATION \
            --pool=SUBORDINATE_POOL_ID \
            --issuer-pool=POOL_ID \
            --issuer-location=ISSUER_LOCATION \
            --from-ca=EXISTING_CA_ID \
            --kms-key-version projects/PROJECT_ID/locations/LOCATION_ID/keyRings/KEY_RING/cryptoKeys/KEY/cryptoKeyVersions/KEY_VERSION
    

Replace the following:

  * SUBORDINATE_CA_ID: the ID of the subordinate CA
  * LOCATION: the location of the subordinate CA. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
  * SUBORDINATE_POOL_ID: the ID of the subordinate CA pool that you created in the previous section
  * POOL_ID: the ID of the parent CA pool
  * ISSUER_LOCATION: the location of the certificate
  * EXISTING_CA_ID: the ID of the source CA
  * PROJECT_ID: the ID of the project
  * LOCATION_ID: the location of the key ring
  * KEY_RING: the name of the key ring where the key is located
  * KEY: the name of the key
  * KEY_VERSION: the version of the key



The following statement is returned when the subordinate CA is created.
    
    
    Created Certificate Authority [projects/my-project-pki/locations/us-west1/caPools/SUBORDINATE_POOL_ID/certificateAuthorities/SUBORDINATE_CA_ID].
    

Enable the subordinate CA by entering `y` when prompted by the gcloud CLI.

## Create a certificate

To use the newly created CA to create a certificate, do the following:

  1. Install the Pyca cryptography library using the `pip` command.
         
         pip install --user "cryptography>=2.2.0"
         

CA Service uses the Pyca cryptography library to generate and store a new asymmetric key-pair on your local machine. This key is never sent to CA Service.

  2. To allow the Google Cloud SDK to use the Pyca cryptography library, you must enable site packages.

### macOS or Linux
         
         export CLOUDSDK_PYTHON_SITEPACKAGES=1
         

### Windows
         
         set CLOUDSDK_PYTHON_SITEPACKAGES=1
         

  3. Create a certificate.
         
         gcloud privateca certificates create \
               --issuer-pool POOL_ID \
               --issuer-location ISSUER_LOCATION \
               --subject "CN=Example Prod,O=Google" \
               --generate-key \
               --key-output-file=./key \
               --cert-output-file=./cert.pem
         

Replace the following:

     * POOL_ID: the resource ID of the CA pool you created
     * ISSUER_LOCATION: the location of the certificate authority that issued the digital certificate

CA Service returns the following response:
    
    Created Certificate [projects/PROJECT_ID/locations/LOCATION/caPools/POOL_ID/certificates/CERTIFICATE_ID]
    




## Clean up

Clean up by deleting the CA pool, the CA, and the project you created for this quickstart.

  1. Revoke the certificate.

To revoke a certificate, run the following command: 
         
         gcloud privateca certificates revoke --certificate CERT_NAME --issuer-pool POOL_ID --location 
         LOCATION
           

Replace the following: 

        * CERT_NAME: the name of the certificate that you want to revoke 
        * POOL_ID: the name of the CA pool that issued the certificate 
        * LOCATION: the location of the CA pool 
  2. Delete the CA.

You can delete a CA only after you have revoked all the certificates issued by it.

     1. Disable the CA.
            
            gcloud privateca roots disable CA_ID --pool=POOL_ID --location=LOCATION
            

Replace the following:

        * CA_ID: the resource ID of the CA
        * POOL_ID: the resource ID of the CA pool
        * LOCATION: the location of the CA pool. For the complete list of locations, see [Locations](https://docs.cloud.google.com/certificate-authority-service/docs/locations).
     2. Delete the CA.
            
            gcloud privateca roots delete CA_ID --pool=POOL_ID --location=LOCATION
            

The CA state changes to `Deleted`. CA Service permanently deletes the CA 30 days after you initiate the deletion.

  3. Delete the CA pool.

You can delete a CA pool only after the CA in it is permanently deleted.
         
         gcloud privateca pools delete POOL_ID --location=LOCATION
         

  4. Delete the project.


**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Learn more about [CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/ca-pool).
  * Learn more about [creating a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).
  * Learn more about [creating CAs](https://docs.cloud.google.com/certificate-authority-service/docs/creating-root-ca).
  * Learn more about [requesting certificates](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates).
  * Learn how you can [control the type of certificates a CA pool can issue](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
