---
url: https://docs.cloud.google.com/firewall/docs/setup-tls-inspection/
title: Set up TLS inspection \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:40:29.693540+00:00
---

# Set up TLS inspection  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/setup-tls-inspection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Set up TLS inspection Stay organized with collections  Save and categorize content based on your preferences. 

To inspect encrypted traffic and protect your Virtual Private Cloud (VPC) network from hidden threats, configure Transport Layer Security (TLS) inspection for Cloud Next Generation Firewall (Cloud NGFW).

If you are a network administrator or a security engineer who configures TLS inspection, then use this document to set up your environment.

This document shows you how to complete the following tasks:

  * Configure certificate authority (CA) resources
  * Create trust config resources
  * Enable TLS inspection



Before you begin, review the concepts in the [TLS inspection overview](https://docs.cloud.google.com/firewall/docs/about-tls-inspection).

## Before you begin

Before you configure TLS inspection, complete the tasks in the following sections.

### Enable Certificate Authority Service

Cloud NGFW uses [Certificate Authority Service](https://docs.cloud.google.com/certificate-authority-service) to generate intermediate certificate authorities (CAs). Cloud NGFW uses these intermediate CAs to generate the certificates used for TLS inspection.

You can enable the CA Service API by using Google Cloud console: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=privateca.googleapis.com)

To enable CA Service by using the Google Cloud CLI, use the following command: 
    
    
       gcloud services enable privateca.googleapis.com
      

### Enable Certificate Manager

Cloud NGFW uses [Certificate Manager](https://docs.cloud.google.com/certificate-manager/docs/overview) to create trust configs. If you don't want to use trust configs, skip this step.

You can enable the Certificate Manager API by using Google Cloud console: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=certificatemanager.googleapis.com)

To enable Certificate Manager by using the Google Cloud CLI, use the following command:
    
    
       gcloud services enable certificatemanager.googleapis.com
      

### Create a trust config

This is an optional step. To create a [trust config](https://docs.cloud.google.com/certificate-manager/docs/trust-configs#create), follow the steps in this section.

**Note:** If you already have a CA that you use to generate server certificates, skip to the last step in the following procedure.

  1. [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

The CA pool that you create in this step is different from the one you create for configuring the TLS inspection policy.

  2. [Create a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca) by using the CA pool you created earlier.

Alternatively, use an existing external root CA by [creating a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-sub-ca-from-external-ca) within the CA service. The external root CA must sign this subordinate CA. For Cloud NGFW to use the CA, the root and subordinate CAs in the CA pool must have a path length of at least one. The `pathLenConstraint` field in a CA certificate specifies the path length. This field defines the maximum number of subordinate CA certificates that can exist in a certification path below the current CA certificate.

  3. [Create a certificate using an auto-generated key](https://docs.cloud.google.com/certificate-authority-service/docs/requesting-certificates#auto-generated-key). Use the same CA pool name that you created earlier.

  4. Get the public certificate of the CA from the created certificate.
         
         $PEM-CERT=$(gcloud privateca roots describe ROOT_CA_NAME \
            --location LOCATION \
            --project PROJECT_ID \
            --pool CA_POOL \
            --format "value(pemCaCertificates)")
         

Replace the following:

     * `ROOT_CA_NAME`: the name of the root CA
     * `LOCATION`: the location of the root CA
     * `PROJECT_ID`: the project ID of the root CA
     * `CA_POOL`: the name of the CA pool to create the certificates from
  5. [Create and import a trust config](https://docs.cloud.google.com/certificate-manager/docs/trust-configs#create) by using the `PEM-CERT` obtained in the preceding step. If you use your own CA, use the public certificate obtained from your CA.




You use this trust config to create a TLS inspection policy.

### Create a CA pool

You must create a CA pool before you can use CA Service to create a CA.

**Important:** Cloud NGFW periodically generates an intermediate CA that your CA pool in Certificate Authority Service signs, and then it uses this intermediate CA to sign server certificates. **Cloud NGFW does not support any issuance policies or certificate name constraints attached to the CA pool**. If the CA pool has any constraints attached, Cloud NGFW can generate invalid certificates.

To create a CA pool, follow the instructions in [Creating CA pools](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

You use this CA pool to create a TLS inspection policy.

### Create a root CA

If you don't have an existing root CA, you can create one within CA Service. To create a root CA, follow the instructions in [Creating a root CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-root-ca), and use the same CA pool that you created earlier (see section Create a CA pool).

To use an existing external root CA, [create a subordinate CA](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#create-sub-ca-from-external-ca) within the CA service, signed by your external root CA.

For NGFW Enterprise, Subordinate certificates require a path length restriction of no less than 1 to be able to to generate an intermediate CA. By default, the subordinate certificate and the CSR is generated with a path length restriction of 0. This has to be changed. As of now, this cannot be done through the console and only through the CAS provided Google Cloud CLI commands using some of the following flags

  * `--extended-key-usages` flag: specifies the extended key usages for the certificate.

  * `--key-usages` flag: specifies the key usages for the certificate.

  * `--max-chain-length` flag: defines the maximum depth of subordinate CAs permitted under this CA for a CA certificate.




###  gcloud 
    
    
    gcloud privateca subordinates create SUBORDINATE_CA_ID \
        --pool=SUBORDINATE_POOL_ID \
        --location=LOCATION \
        --create-csr --csr-output-file=FILE_NAME \
        --key-algorithm="ec-p256-sha256" \
        --subject="CN=Example Server TLS CA, O=Example LLC
        --key-algorithm=rsa-pss-4096-sha256 \
        --key-usages=cert_sign,crl_sign \
        --extended-key-usages=server_auth \
        --max-chain-length=1"
      

Replace the following:

  * SUBORDINATE_CA_ID: the unique identifier of the subordinate CA.
  * SUBORDINATE_POOL_ID: the name of the CA pool.
  * LOCATION: the location of the CA pool.
  * FILE_NAME: the name of the file where the PEM-encoded CSR is written.



This creates the CSR returning the following 
    
    
        Created Certificate Authority [projects/my-project-pki/locations/us-west1/caPools/SUBORDINATE_POOL_ID/certificateAuthorities/SUBORDINATE_CA_ID] and saved CSR to FILE_NAME.
        

To activate the subordinate CA, you must [sign the CSR](https://docs.cloud.google.com/certificate-authority-service/docs/creating-certificate-authorities#sign-csr) after it is created.

### Create a service account

If you don't have a service account, you must create one and grant the required permissions.

  1. Create a service account:
         
         gcloud beta services identity create \
              --service networksecurity.googleapis.com \
              --project PROJECT_ID
         

Replace `PROJECT_ID` with the project ID of the service account.

The Google Cloud CLI creates a service account called `service-PROJECT_NUMBER@gcp-sa-networksecurity.iam.gserviceaccount.com`. Here, `PROJECT_NUMBER` is the unique identifier of the `PROJECT_ID` you provided in the preceding command.

  2. Grant permission to your service account to generate certificates that use your CA pool:
         
         gcloud privateca pools add-iam-policy-binding CA_POOL \
              --member 'serviceAccount:SERVICE_ACCOUNT' \
              --role 'roles/privateca.certificateRequester' \
              --location REGION
         

Replace the following:

     * `CA_POOL`: the name of the CA pool to create the certificates from
     * `SERVICE_ACCOUNT`: the name of the service account you created in the preceding step
     * `LOCATION`: the region of the CA pool



## Configure TLS inspection

Before you proceed with the tasks in this section, make sure you have configured your certificates, or you have completed the prerequisite tasks listed in the Before you begin section.

To configure TLS inspection, complete the tasks in the following sections.

### Create a TLS inspection policy

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles.

**Permissions**

  * `certificatemanager.trustconfigs.list`
  * `certificatemanager.trustconfigs.use`
  * `privateca.caPools.list`
  * `privateca.caPools.use`
  * `privateca.certificateAuthorities.list`
  * `networksecurity.operations.get`
  * `networksecurity.tlsInspectionPolicies.list`
  * `networksecurity.tlsInspectionPolicies.create`



**Roles**

  * `compute.securityAdmin`
  * `compute.networkAdmin`



###  Console 

  1. In the Google Cloud console, go to the **TLS inspection policies** page.

[Go to TLS inspection policies](https://console.cloud.google.com/net-security/tls/policies/list)

  2. In the project selector menu, select your project.

  3. Click **Create TLS inspection policy**.

  4. For **Name** , enter a name. Don't include sensitive information such as personally identifiable information or security data in the TLS inspection policy name.

  5. Optional: In the **Description** field, enter a description.

  6. In the **Region** list, select the region where you want to create the TLS inspection policy.

  7. In the **CA pool** list, select the CA pool from where you want to create the certificates.

If you don't have a CA pool configured, click **New Pool** and follow the instructions in [Create a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/creating-ca-pool).

  8. Optional: In the **Minimum TLS version** list, select the minimum TLS version supported by the policy.

  9. For the **Trust Configuration** , select one of the following options:

     * **Public CAs only:** Select this option if you want to trust servers with publicly signed certificates.
     * **Private CAs only:** Select this option if you want to trust servers with privately signed certificates.

In the **Private trust configuration** list, select the trust config with the configured [trust store](https://docs.cloud.google.com/certificate-manager/docs/core-components#trust-stores) to use for trusting upstream server certificates. For more information about how to create a trust config, see Create a trust config.

     * **Public and private CAs:** Select this option if you want to use both public and private CAs.

  10. Optional: In the **Cipher suite profile** list, select the TLS profile type. You can choose from one of the following values:

     * **Compatible** : allows the broadest set of clients, including clients that support only out-of-date TLS features, to negotiate TLS.
     * **Modern** : supports a wide set of TLS features, allowing modern clients to negotiate TLS.
     * **Restricted** : supports a reduced set of TLS features intended to meet stricter compliance requirements.
     * **Custom** : lets you select TLS features individually.

In the **Cipher suites** list, select the name of the [cipher suites](https://docs.cloud.google.com/firewall/docs/about-tls-inspection#tls-specification) supported by the custom profile.

  11. Click **Create**.




###  gcloud 

  1. Create a YAML file `TLS_INSPECTION_FILE.yaml`. Replace `TLS_INSPECTION_FILE` with a filename of your choice.

  2. Add the following code to the YAML file to configure the TLS inspection policy.
         
         name: projects/PROJECT_ID/locations/REGION/tlsInspectionPolicies/TLS_INSPECTION_NAME
         caPool: projects/PROJECT_ID/locations/REGION/caPools/CA_POOL
         minTlsVersion: TLS_VERSION
         tlsFeatureProfile: PROFILE_TYPECIPHER_NAME
         excludePublicCaSet: `TRUE`|`FALSE`
         trustConfig: projects/PROJECT_ID/locations/REGION/trustConfigs/TRUST_CONFIG_NAME
         

Replace the following:

     * `PROJECT_ID`: the project ID of the TLS inspection policy
     * `REGION`: the region where the TLS inspection policy is created
     * `TLS_INSPECTION_NAME`: the name of the TLS inspection policy Don't include sensitive information such as personally identifiable information or security data in the TLS inspection policy name.
     * `CA_POOL`: the name of the CA pool to create the certificates from

The CA pool _must_ exist within the same region.

     * `TLS_VERSION`: an optional argument that specifies the minimum TLS version supported by Cloud NGFW

You can select from one of the following values:

       * `TLS_1_0`
       * `TLS_1_1`
       * `TLS_1_2`
     * `PROFILE_TYPE`: an optional argument that specifies the type of TLS profile

You can select from one of the following values:

       * `PROFILE_COMPATIBLE`: allows the broadest set of clients, including clients that support only out-of-date TLS features, to negotiate TLS.
       * `PROFILE_MODERN`: supports a wide set of TLS features, allowing modern clients to negotiate TLS.
       * `PROFILE_RESTRICTED`: supports a reduced set of TLS features intended to meet stricter compliance requirements.
       * `PROFILE_CUSTOM`: lets you select TLS features individually.
     * `CIPHER_NAME`: an optional argument to specify the name of the [cipher suite](https://docs.cloud.google.com/firewall/docs/about-tls-inspection#tls-specification) supported by the custom profile

You specify this argument only when the profile type is set to `PROFILE_CUSTOM`.

     * `excludePublicCaSet`: an optional flag to include or exclude a public CA set. By default, this flag is set to false. When this flag is set to true, TLS connections don't trust public CA servers. In this case, Cloud NGFW can only make TLS connections to servers with certificates signed by CAs in the trust config.

     * `TRUST_CONFIG_NAME`: an optional argument to specify the name of the trust config resource

  3. Import the TLS inspection policy that you created in the section Create a TLS inspection policy
         
         gcloud network-security tls-inspection-policies import TLS_INSPECTION_NAME \
             --source TLS_INSPECTION_FILE.yaml \
             --location REGION
         

Replace the following:

     * `TLS_INSPECTION_NAME`: the name of the TLS inspection policy
     * `TLS_INSPECTION_FILE`: the name of the TLS inspection policy YAML file

**Important:** Certificates generated for TLS inspection have a short lifespan. After the certificates are issued, they cannot be changed or revoked through a CA service.

## Add TLS inspection policy to a firewall endpoint association

To add the TLS inspection policy to a firewall endpoint association, follow the steps mentioned in [Create firewall endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoint-associations#create-endpoint-association).

## Configure firewall policy rules with TLS inspection

To enable TLS inspection for your Virtual Private Cloud (VPC) network, set the `--tls-inspect` flag in your firewall policy rule. This flag indicates that the TLS inspection can be performed when the [security profile group](https://docs.cloud.google.com/firewall/docs/about-security-profile-groups) is applied.

To learn more about how to enable the `--tls-inspect` flag in hierarchical firewall policy rules, see [Firewall policy rule tasks](https://docs.cloud.google.com/firewall/docs/using-firewall-policies#rule_tasks).

To learn more about how to enable the `--tls-inspect` flag in global network firewall policy rules, see [Add firewall policy rule](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies#add_rules).

## What's next?

  * [Manage TLS inspection](https://docs.cloud.google.com/firewall/docs/manage-tls-inspection)
  * [Configure the URL filtering service](https://docs.cloud.google.com/firewall/docs/configure-url-filtering)
  * [Configure intrusion detection and prevention service](https://docs.cloud.google.com/firewall/docs/configure-intrusion-prevention)
  * [Create and manage firewall endpoints](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
